# Command-line interface (CLI)

The CLI command-line interface offers several functionalities related to Konvergo ERP.
You can use it to run the server, launch Konvergo ERP as a Python console environment,
scaffold an Konvergo ERP module, populate a database, or count the number of lines of
code.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>The command to use to call the CLI depends on how you installed Konvergo ERP. In the examples below, we
assume that you are <a href="../../administration/on_premise/source">running Konvergo ERP from source</a> with the
<code>odoo-bin</code> file. If you installed Konvergo ERP <a href="../../administration/on_premise/packages">from a distribution package</a> or with <a href="https://hub.docker.com/_/odoo/">Docker</a>, you
must adapt the command.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Run Konvergo ERP from source</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">Konvergo ERP was installed from a distribution package</button><button aria-controls="panel-0-0-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-2" name="0-2" role="tab" tabindex="-1">Konvergo ERP was installed with Docker</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><ol class="arabic simple">
<li><p>Navigate to the root of the directory where you downloaded the source files of Konvergo ERP
Community.</p></li>
<li><p>Run all CLI commands with <b class="command o_code">./odoo-bin</b></p></li>
</ol>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><p>When Konvergo ERP was installed, an executable named <code>odoo</code> was added to your user’s PATH. Replace
all occurrences of <b class="command o_code">odoo-bin</b> with <b class="command o_code">odoo</b> in the examples below.</p>
</div><div aria-labelledby="tab-0-0-2" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-2" name="0-2" role="tabpanel" tabindex="0"><p>Please refer to the <a href="https://hub.docker.com/_/odoo/">documentation of the official Docker image of Konvergo ERP</a>.</p>
</div></div>
</div>

## Help & version

-h, \--help
    

shows help text with all available options

\--version

    

shows Konvergo ERP version e.g. «Konvergo ERP Server 16.0»

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>You can enable auto-completion in your shell by running</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">echo</span> <span class="s2">"complete -W '`./odoo-bin --help | \</span>
<span class="s2">  sed -e 's/[^a-z_-]\(-\+[a-z0-9_-]\+\)/\n\1\n/' | \</span>
<span class="s2">  grep -- '^-' | sort | uniq | tr '\n' ' '`' odoo-bin"</span> &gt;&gt; ~/.bash_completion
</pre></div>
</div>
</div>

## Running the server

-d <database>, \--database <database>
    

database(s) used when installing or updating modules. Providing a comma-
separated list restrict access to databases provided in list.

For advanced database options, take a look below.

-i <modules>, \--init <modules>
    

comma-separated list of modules to install before running the server (requires
`-d`).

-u <modules>, \--update <modules>
    

comma-separated list of modules to update before running the server. Use `all`
for all modules. (requires `-d`).

\--addons-path <directories>

    

comma-separated list of directories in which modules are stored. These
directories are scanned for modules.

\--upgrade-path <upgrade_path>

    

specify an additional upgrade path.

\--load <modules>

    

list of server-wide modules to load. Those modules are supposed to provide
features not necessarily tied to a particular database. This is in contrast to
modules that are always bound to a specific database when they are installed
(i.e. the majority of Konvergo ERP addons). Default is `base,web`.

-c <config>, \--config <config>
    

path to an alternate configuration file. If not defined, Konvergo ERP checks `ODOO_RC`
environmental variable and default location `_$HOME_ /.odoorc`. See
configuration file section below.

-D <data-dir-path>, \--data-dir <data-dir-path>
    

directory path where to store Konvergo ERP data (eg. filestore, sessions). If not
specified, Konvergo ERP will fallback to a predefined path. On Unix systems its one
defined in `$XDG_DATA_HOME` environmental variable or `~/.local/share/Konvergo ERP` or
`/var/lib/Konvergo ERP`.

-s, \--save
    

saves the server configuration to the current configuration file (`_$HOME_
/.odoorc` by default, and can be overridden using `-c`).

\--without-demo

    

disables demo data loading for modules installed comma-separated, use `all`
for all modules. Requires `-d` and `-i`.

\--pidfile=<pidfile>

    

path to a file where the server pid will be stored

\--stop-after-init

    

stops the server after its initialization.

\--geoip-db <path>

    

Absolute path to the GeoIP database file.

## Testing Configuration

\--test-enable

    

runs tests after module installation

\--test-file <file>

    

runs a python test file

\--test-tags [-][tag][/module][:class][.method]

    

Comma-separated list of specs to filter which tests to execute. Enable unit
tests if set.

Example: `--test-tags :TestClass.test_func,/test_module,external`

  * The `-` specifies if we want to include or exclude tests matching this spec.

  * The tag will match tags added on a class with a `tagged()` decorator (all [test classes](backend/testing#reference-testing) have `standard` and `at_install` tags until explicitly removed, see the decorator documentation).

  * `*` will match all tags.

  * If tag is omitted on include mode, its value is `standard`.

  * If tag is omitted on exclude mode, its value is `*`.

  * The module, class, and method will respectively match the module name, test class name and test method name.

Filtering and executing the tests happens twice: right after each module
installation/update and at the end of the modules loading. At each stage tests
are filtered by `--test-tags` specs and additionally by dynamic specs
`at_install` and `post_install` correspondingly.

\--screenshots

    

Specify directory where to write screenshots when an HttpCase.browser_js test
fails. It defaults to `/tmp/odoo_tests/_db_name_ /screenshots`

\--screencasts

    

Enable screencasts and specify directory where to write screencasts files. The
`ffmpeg` utility needs to be installed to encode frames into a video file.
Otherwise frames will be kept instead of the video file.

### Database

-r <user>, \--db_user <user>
    

database username, used to connect to PostgreSQL.

-w <password>, \--db_password <password>
    

database password, if using [password
authentication](https://www.postgresql.org/docs/12/static/auth-
methods#AUTH-PASSWORD).

\--db_host <hostname>

    

host for the database server

  * `localhost` on Windows

  * UNIX socket otherwise

\--db_port <port>

    

port the database listens on, defaults to 5432

\--db-filter <filter>

    

hides databases that do not match `<filter>`. The filter is a [regular
expression](https://docs.python.org/3/library/re), with the additions
that:

  * `%h` is replaced by the whole hostname the request is made on.

  * `%d` is replaced by the subdomain the request is made on, with the exception of `www` (so domain `odoo.com` and `www.odoo.com` both match the database `odoo`).

These operations are case sensitive. Add option `(?i)` to match all databases
(so domain `odoo.com` using `(?i)%d` matches the database `Konvergo ERP`).

Since version 11, it’s also possible to restrict access to a given database
listen by using the –database parameter and specifying a comma-separated list
of databases

When combining the two parameters, db-filter supersedes the comma-separated
database list for restricting database list, while the comma-separated list is
used for performing requested operations like upgrade of modules.

    
    
    $ odoo-bin --db-filter ^11.*$
    

Restrict access to databases whose name starts with 11

    
    
    $ odoo-bin --database 11firstdatabase,11seconddatabase
    

Restrict access to only two databases, 11firstdatabase and 11seconddatabase

    
    
    $ odoo-bin --database 11firstdatabase,11seconddatabase -u base
    

Restrict access to only two databases, 11firstdatabase and 11seconddatabase,
and update base module on one database: 11firstdatabase. If database
11seconddatabase doesn’t exist, the database is created and base modules is
installed

    
    
    $ odoo-bin --db-filter ^11.*$ --database 11firstdatabase,11seconddatabase -u base
    

Restrict access to databases whose name starts with 11, and update base module
on one database: 11firstdatabase. If database 11seconddatabase doesn’t exist,
the database is created and base modules is installed

\--db-template <template>

    

when creating new databases from the database-management screens, use the
specified [template
database](https://www.postgresql.org/docs/12/static/manage-ag-
templatedbs). Defaults to `template0`.

\--pg_path </path/to/postgresql/binaries>

    

Path to the PostgreSQL binaries that are used by the database manager to dump
and restore databases. You have to specify this option only if these binaries
are located in a non-standard directory.

\--no-database-list

    

Suppresses the ability to list databases available on the system

\--db_sslmode

    

Control the SSL security of the connection between Konvergo ERP and PostgreSQL. Value
should be one of “disable”, “allow”, “prefer”, “require”, “verify-ca” or
“verify-full” Default value is “prefer”

\--unaccent

    

Try to enable the unaccent extension when creating new databases

### Emails

\--email-from <address>

    

Email address used as <FROM> when Konvergo ERP needs to send mails

\--from-filter <address or domain>

    

Define which email address the SMTP configuration will apply to. The field can
be a domain name or an entire email address, or it can remain empty. If the
sender’s email address does not match this set filter, then the email will be
encapsulated using a combination of the two system parameters:
`mail.default.from` and `mail.catchall.domain`. For example, «Admin»
<admin@example.com> => «Admin» <notifications@mycompany.com>.

\--smtp <server>

    

Address of the SMTP server to connect to in order to send mails

\--smtp-port <port>

    

\--smtp-ssl

    

If set, odoo should use SSL/STARTSSL SMTP connections

\--smtp-user <name>

    

Username to connect to the SMTP server

\--smtp-password <password>

    

Password to connect to the SMTP server

\--smtp-ssl-certificate-filename <path/to/cert.pem>

    

An SSL certificate is to be used for authentication. If set, then `smtp-ssl-
private-key` is required.

\--smtp-ssl-private-key-filename <path/to/key.pem>

    

An SSL private key is used for authentication. If set, then `smtp-ssl-
certificate` is required.

### Internationalisation

Use these options to translate Konvergo ERP to another language. See i18n section of
the user manual. Option “-d” is mandatory. Option “-l” is mandatory in case of
importation

\--load-language <languages>

    

specifies the languages (separated by commas) for the translations you want to
be loaded

-l, \--language <language>
    

specify the language of the translation file. Use it with –i18n-export or
–i18n-import

\--i18n-export <filename>

    

export all sentences to be translated to a CSV file, a PO file or a TGZ
archive and exit.

\--i18n-import <filename>

    

import a CSV or a PO file with translations and exit. The “-l” option is
required.

\--i18n-overwrite

    

overwrites existing translation terms on updating a module or importing a CSV
or a PO file.

\--modules

    

specify modules to export. Use in combination with –i18n-export

### Advanced Options

#### Developer features

\--dev <feature,feature,...,feature>

    

comma-separated list of features. For development purposes only. Do not use it
in production. Possible features are:

  * `all`: all the features below are activated

  * `xml`: read QWeb template from xml file directly instead of database. Once a template has been modified in database, it will be not be read from the xml file until the next update/init. Particularly, templates are not translated on using this option.

  * `reload`: restart server when python file are updated (may not be detected depending on the text editor used)

  * `qweb`: break in the evaluation of QWeb template when a node contains `t-debug='debugger'`

  * `(i)p(u)db`: start the chosen python debugger in the code when an unexpected error is raised before logging and returning the error.

  * `werkzeug`: display the full traceback on the frontend page in case of exception

#### HTTP

\--no-http

    

do not start the HTTP or long-polling workers (may still start
[cron](backend/actions#reference-actions-cron) workers)

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>has no effect if <a href="#cmdoption-odoo-bin-test-enable"><code>--test-enable</code></a> is set, as tests
require an accessible HTTP server</p>
</div>

\--http-interface <interface>

    

TCP/IP address on which the HTTP server listens, defaults to `0.0.0.0` (all
addresses)

-p <port>
    

\--http-port <port>

    

Port on which the HTTP server listens, defaults to 8069.

\--gevent-port <port>

    

TCP port for websocket connections in multiprocessing or gevent mode, defaults
to 8072. Not used in default (threaded) mode.

\--proxy-mode

    

enables the use of `X-Forwarded-*` headers through [Werkzeug’s proxy
support](https://werkzeug.palletsprojects.com/en/0.16.x/middleware/proxy_fix/#module-
werkzeug.middleware.proxy_fix).

It ignores all `X-Forwarded-*` headers in case `X-Forwarded-Host` is missing
from the request.

It always gets the real IP from the last entry of the `X-Forwarded-For` chain.
Configure your web server accordingly using directives such as nginx’s
[set_real_ip_from](https://nginx.org/en/docs/http/ngx_http_realip_module)
in case there are other trusted proxies along the chain that must be ignored.

`X-Forwarded-Proto` and `X-Forwarded-Host` are used to update the request root
URL, which in turn is used to update the `web.base.url` system parameter upon
a successful admin authentication. This system parameter is used to generate
all links for the current database; see [URL web base de la base de
datos](../../applications/websites/website/configuration/domain_names#domain-
name-web-base-url).

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>proxy mode <em>must not</em> be enabled outside of a reverse proxy
scenario</p>
</div>

\--x-sendfile

    

delegates serving attachments files to the static web server and sets both
`X-Sendfile` (apache) and `X-Accel-*` (nginx) http headers on stream
responses. See [Gestión de archivos y archivos adjuntos
estáticos](../../administration/on_premise/deploy#deploy-streaming) for
web server configuration.

#### Logging

By default, Konvergo ERP displays all logging of
[level](https://docs.python.org/3/library/logging#logging.Logger.setLevel)
`INFO`, `WARNING` and `ERROR`. All logs independently of the level are output
on `stderr`. Various options are available to redirect logging to other
destinations and to customize the verbosity.

\--logfile <file>

    

sends logging output to the specified file instead of `stderr`. On Unix, the
file [can be managed by external log rotation
programs](https://docs.python.org/3/library/logging.handlers#watchedfilehandler)
and will automatically be reopened when replaced

\--syslog

    

logs to the system’s event logger: [syslog on
unices](https://docs.python.org/3/library/logging.handlers#sysloghandler)
and [the Event Log on
Windows](https://docs.python.org/3/library/logging.handlers#nteventloghandler).

Neither is configurable

\--log-db <dbname>

    

logs to the `ir.logging` model (`ir_logging` table) of the specified database.
The database can be the name of a database in the «current» PostgreSQL, or [a
PostgreSQL URI](https://www.postgresql.org/docs/12/static/libpq-
connect#AEN38208) for e.g. log aggregation.

\--log-handler <handler-spec>

    

`_LOGGER_ :_LEVEL_`, enables `LOGGER` at the provided `LEVEL` e.g.
`odoo.models:DEBUG` will enable all logging messages at or above `DEBUG` level
in the models.

  * The colon `:` is mandatory

  * The logger can be omitted to configure the root (default) handler

  * If the level is omitted, the logger is set to `INFO`

The option can be repeated to configure multiple loggers e.g.

    
    
    $ odoo-bin --log-handler :DEBUG --log-handler werkzeug:CRITICAL --log-handler odoo.fields:WARNING
    

\--log-web

    

enables DEBUG logging of HTTP requests and responses, equivalent to `--log-
handler=odoo.http:DEBUG`

\--log-sql

    

enables DEBUG logging of SQL querying, equivalent to `--log-
handler=odoo.sql_db:DEBUG`

\--log-level <level>

    

Shortcut to more easily set predefined levels on specific loggers. «real»
levels (`critical`, `error`, `warn`, `debug`) are set on the `odoo` and
`werkzeug` loggers (except for `debug` which is only set on `odoo`).

Konvergo ERP also provides debugging pseudo-levels which apply to different sets of
loggers:

`debug_sql`

    

sets the SQL logger to `debug`

equivalent to `--log-sql`

`debug_rpc`

    

sets the `odoo` and HTTP request loggers to `debug`

equivalent to `--log-level debug --log-request`

`debug_rpc_answer`

    

sets the `odoo` and HTTP request and response loggers to `debug`

equivalent to `--log-level debug --log-request --log-response`

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>In case of conflict between <a href="#cmdoption-odoo-bin-log-level"><code>--log-level</code></a> and
<a href="#cmdoption-odoo-bin-log-handler"><code>--log-handler</code></a>, the latter is used</p>
</div>

#### Multiprocessing

\--workers <count>

    

if `count` is not 0 (the default), enables multiprocessing and sets up the
specified number of HTTP workers (sub-processes processing HTTP and RPC
requests).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>multiprocessing mode is only available on Unix-based systems</p>
</div>

A number of options allow limiting and recycling workers:

\--limit-request <limit>

    

Number of requests a worker will process before being recycled and restarted.

Defaults to _8196_.

\--limit-memory-soft <limit>

    

Maximum allowed virtual memory per worker in bytes. If the limit is exceeded,
the worker is killed and recycled at the end of the current request.

Defaults to _2048MiB (2048*1024*1024B)_.

\--limit-memory-hard <limit>

    

Hard limit on virtual memory in bytes, any worker exceeding the limit will be
immediately killed without waiting for the end of the current request
processing.

Defaults to _2560MiB (2560*1024*1024B)_.

\--limit-time-cpu <limit>

    

Prevents the worker from using more than <limit> CPU seconds for each request.
If the limit is exceeded, the worker is killed.

Defaults to _60_.

\--limit-time-real <limit>

    

Prevents the worker from taking longer than <limit> seconds to process a
request. If the limit is exceeded, the worker is killed.

Differs from `--limit-time-cpu` in that this is a «wall time» limit including
e.g. SQL queries.

Defaults to _120_.

\--max-cron-threads <count>

    

number of workers dedicated to [cron](backend/actions#reference-actions-
cron) jobs. Defaults to _2_. The workers are threads in multi-threading mode
and processes in multi-processing mode.

For multi-processing mode, this is in addition to the HTTP worker processes.

## Configuration file

Most of the command-line options can also be specified via a configuration
file. Most of the time, they use similar names with the prefix `-` removed and
other `-` are replaced by `_` e.g. `--db-template` becomes `db_template`.

Some conversions don’t match the pattern:

  * `--db-filter` becomes `dbfilter`

  * `--no-http` corresponds to the `http_enable` boolean

  * logging presets (all options starting with `--log-` except for `--log-handler` and `--log-db`) just add content to `log_handler`, use that directly in the configuration file

  * `--smtp` is stored as `smtp_server`

  * `--database` is stored as `db_name`

  * `--i18n-import` and `--i18n-export` aren’t available at all from configuration files

The default configuration file is `_$HOME_ /.odoorc` which can be overridden
using `--config`. Specifying `--save` will save the current configuration
state back to that file. The configuration items relative to the command-line
are to be specified in the section `[options]`.

Here is a sample file:

    
    
    [options]
    db_user=odoo
    dbfilter=odoo
    

## Shell

The Konvergo ERP command line also allows launching Konvergo ERP as a Python console
environment, enabling direct interaction with the
[orm](backend/orm#reference-orm) and its functionalities.

    
    
    $ odoo-bin shell
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Adding an exclamation mark to all contacts” names:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">In</span> <span class="p">[</span><span class="mi">1</span><span class="p">]:</span> <span class="n">records</span> <span class="o">=</span> <span class="n">env</span><span class="p">[</span><span class="s2">"res.partner"</span><span class="p">]</span><span class="o">.</span><span class="n">search</span><span class="p">([])</span>

<span class="n">In</span> <span class="p">[</span><span class="mi">2</span><span class="p">]:</span> <span class="n">records</span>
<span class="n">Out</span><span class="p">[</span><span class="mi">2</span><span class="p">]:</span> <span class="n">res</span><span class="o">.</span><span class="n">partner</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span> <span class="mi">21</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>

<span class="n">In</span> <span class="p">[</span><span class="mi">3</span><span class="p">]:</span> <span class="k">for</span> <span class="n">partner</span> <span class="ow">in</span> <span class="n">records</span><span class="p">:</span>
   <span class="o">...</span><span class="p">:</span>     <span class="n">partner</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="s2">"</span><span class="si">%s</span><span class="s2"> !"</span> <span class="o">%</span> <span class="n">partner</span><span class="o">.</span><span class="n">name</span>
   <span class="o">...</span><span class="p">:</span>

<span class="n">In</span> <span class="p">[</span><span class="mi">4</span><span class="p">]:</span> <span class="n">env</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
</pre></div>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>By default, the shell is running in transaction mode. This means that any change made to the
database is rolled back when exiting the shell. To commit changes, use <code>env.cr.commit()</code>.</p>
</div>
</div>

\--shell-interface (ipython|ptpython|bpython|python)

    

Specify a preferred REPL to use in shell mode. This shell is started with the
`env` variable already initialized to be able to access the ORM and other Konvergo ERP
modules.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="backend/orm#reference-orm-environment"><span class="std std-ref">Environment</span></a></p>
</div>

## Scaffolding

Scaffolding is the automated creation of a skeleton structure to simplify
bootstrapping (of new modules, in the case of Konvergo ERP). While not necessary it
avoids the tedium of setting up basic structures and looking up what all
starting requirements are.

Scaffolding is available via the **odoo-bin scaffold** subcommand.

    
    
    $ odoo-bin scaffold my_module /addons/
    

name (required)

    

the name of the module to create, may munged in various manners to generate
programmatic names (e.g. module directory name, model names, …)

destination (default=current directory)

    

directory in which to create the new module, defaults to the current directory

-t <template>
    

a template directory, files are passed through
[jinja2](https://jinja.palletsprojects.com/) then copied to the `destination`
directory

This will create module _my_module_ in directory _/addons/_.

## Database Population

Konvergo ERP CLI supports database population features. If the feature is [implemented
on a given model](backend/performance#reference-performance-populate-
methods), it allows automatic data generation of the model’s records to test
your modules in databases containing non-trivial amounts of records.

    
    
    $ odoo-bin populate
    

\--models

    

list of models for which the database should be filled

\--size (small|medium|large)

    

population size, the actual records number depends on the model’s
`_populate_sizes` attribute. The generated records content is specified by the
`_populate_factories()` method of a given model (cf. the `populate` folder of
modules for further details).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="backend/performance#reference-performance-populate"><span class="std std-ref">Database population</span></a></p>
</div>

## Cloc

Konvergo ERP Cloc is a tool to count the number of relevant lines written in Python,
Javascript, CSS, SCSS, or XML. This can be used as a rough metric for pricing
maintenance of extra modules.

### Command-line options

-d <database>, \--database <database>
    

Process the code of all extra modules installed on the provided database, and
of all server actions and computed fields manually created in the provided
database.

The `--addons-path` option is required to specify the path(s) to the module
folder(s).

If combined with `--path`, the count will be that of the sum of both options”
results (with possible overlaps). At least one of these two options is
required to specify which code to process.

    
    
    $ odoo-bin cloc --addons-path=addons -d my_database
    

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>You can enable auto-completion in your shell by running</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">echo</span> <span class="s2">"complete -W '`./odoo-bin --help | \</span>
<span class="s2">  sed -e 's/[^a-z_-]\(-\+[a-z0-9_-]\+\)/\n\1\n/' | \</span>
<span class="s2">  grep -- '^-' | sort | uniq | tr '\n' ' '`' odoo-bin"</span> &gt;&gt; ~/.bash_completion
</pre></div>
</div>
</div>0

-p <path>, \--path <path>
    

Process the files in the provided path.

If combined with `--database`, the count will be that of the sum of both
options” results (with possible overlaps). At least one of these two options
is required to specify which code to process.

    
    
    $ odoo-bin cloc -p addons/account
    

Multiple paths can be provided by repeating the option.

    
    
    $ odoo-bin cloc -p addons/account -p addons/sale
    

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>You can enable auto-completion in your shell by running</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">echo</span> <span class="s2">"complete -W '`./odoo-bin --help | \</span>
<span class="s2">  sed -e 's/[^a-z_-]\(-\+[a-z0-9_-]\+\)/\n\1\n/' | \</span>
<span class="s2">  grep -- '^-' | sort | uniq | tr '\n' ' '`' odoo-bin"</span> &gt;&gt; ~/.bash_completion
</pre></div>
</div>
</div>1

\--addons-path <directories>

    

Comma-separated list of directories in which modules are stored. These
directories are scanned for modules.

Required if the `--database` option is used.

-c <directories>
    

Specify a configuration file to use in place of the `--addons-path` option.

    
    
    $ odoo-bin cloc -c config.conf -d my_database
    

-v, \--verbose
    

Show the details of lines counted for each file.

### Processed files

#### With the `--database` option

Konvergo ERP Cloc counts the lines in each file of extra installed modules in a given
database. In addition, it counts the Python lines of server actions and custom
computed fields that have been directly created in the database or imported.
Finally, it counts the lines of code of Javascript, CSS, and SCSS files, and
of QWeb views from imported modules.

Some files are excluded from the count by default:

  * The manifest (`__manifest__.py` or `__openerp__.py`)

  * The contents of the folder `static/lib`

  * The tests defined in the folder `tests` and `static/tests`

  * The migrations scripts defined in the folder `migrations` and `upgrades`

  * The XML files declared in the `demo` or `demo_xml` sections of the manifest

For special cases, a list of files that should be ignored by Konvergo ERP Cloc can be
defined per module. This is specified by the `cloc_exclude` entry of the
manifest:

    
    
    "cloc_exclude": [
        "lib/common.py", # exclude a single file
        "data/*.xml",    # exclude all XML files in a specific folder
        "example/**/*",  # exclude all files in a folder hierarchy recursively
        "**/*.scss",     # exclude all scss file from the module
    ]
    

The pattern `**/*` can be used to ignore an entire module. This can be useful
to exclude a module from maintenance service costs.

For more information about the pattern syntax, see
[glob](https://docs.python.org/3/library/pathlib#pathlib.Path.glob).

#### With the `--path` option

This method works the same as with the –database option if a manifest file is
present in the given folder. Otherwise, it counts all files.

### Identifying Extra Modules

To distinguish between standard and extra modules, Konvergo ERP Cloc uses the
following heuristic: modules that are located (real file system path, after
following symbolic links) in the same parent directory as the `base`, `web` or
`web_enterprise` standard modules are considered standard. Other modules are
treated as extra modules.

### Error Handling

Some file cannot be counted by Konvergo ERP Cloc. Those file are reported at the end
of the output.

#### Max file size exceeded

Konvergo ERP Cloc rejects any file larger than 25MB. Usually, source files are smaller
than 1 MB. If a file is rejected, it may be:

  * A generated XML file that contains lots of data. It should be excluded in the manifest.

  * A JavaScript library that should be placed in the `static/lib` folder.

#### Syntax Error

Konvergo ERP Cloc cannot count the lines of code of a Python file with a syntax
problem. If an extra module contains such files, they should be fixed to allow
the module to load. If the module works despite the presence of those files,
they are probably not loaded and should therefore be removed from the module,
or at least excluded in the manifest via `cloc_exclude`.

## TSConfig Generator

When working on javascript, there are ways to help your editor providing you
with powerful auto-completion. One of those ways is the use of a tsconfig.json
file. Originally meant for typescript, editors can use its information with
plain javascript also. With this config file, you will now have full auto-
completion across modules.

The command to generate this files takes as many unnamed arguments as you
need. Those are relative paths to your addon directories. In the example
below, we move up one folder to save the tsconfig file in the folder
containing community and enterprise.

    
    
    $ community/odoo-bin tsconfig --addons-path community/addons,community/odoo/addons,enterprise > tsconfig.json
    

