# System configuration

This document describes basic steps to set up Konvergo ERP in production or on an
internet-facing server. It follows [installation](../on_premise), and is
not generally necessary for a development systems that is not exposed on the
internet.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If you are setting up a public server, be sure to check our <a href="#security"><span class="std std-ref">Security</span></a> recommendations!</p>
</div>

## dbfilter

Konvergo ERP is a multi-tenant system: a single Konvergo ERP system may run and serve a number
of database instances. It is also highly customizable, with customizations
(starting from the modules being loaded) depending on the “current database”.

This is not an issue when working with the backend (web client) as a logged-in
company user: the database can be selected when logging in, and customizations
loaded afterwards.

However it is an issue for non-logged users (portal, website) which aren’t
bound to a database: Konvergo ERP needs to know which database should be used to load
the website page or perform the operation. If multi-tenancy is not used that
is not an issue, there’s only one database to use, but if there are multiple
databases accessible Konvergo ERP needs a rule to know which one it should use.

That is one of the purposes of [`--db-
filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter): it
specifies how the database should be selected based on the hostname (domain)
that is being requested. The value is a [regular
expression](https://docs.python.org/3/library/re), possibly including the
dynamically injected hostname (`%h`) or the first subdomain (`%d`) through
which the system is being accessed.

For servers hosting multiple databases in production, especially if `website`
is used, dbfilter **must** be set, otherwise a number of features will not
work correctly.

### Configuration samples

  * Show only databases with names beginning with ‘mycompany’

in [the configuration file](../../developer/reference/cli#reference-
cmdline-config-file) set:

    
    
    [options]
    dbfilter = ^mycompany.*$
    

  * Show only databases matching the first subdomain after `www`: for example the database “mycompany” will be shown if the incoming request was sent to `www.mycompany.com` or `mycompany.co.uk`, but not for `www2.mycompany.com` or `helpdesk.mycompany.com`.

in [the configuration file](../../developer/reference/cli#reference-
cmdline-config-file) set:

    
    
    [options]
    dbfilter = ^%d$
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>

## PostgreSQL

By default, PostgreSQL only allows connection over UNIX sockets and loopback
connections (from “localhost”, the same machine the PostgreSQL server is
installed on).

UNIX socket is fine if you want Konvergo ERP and PostgreSQL to execute on the same
machine, and is the default when no host is provided, but if you want Konvergo ERP and
PostgreSQL to execute on different machines 1 it will need to [listen to
network interfaces](https://www.postgresql.org/docs/12/static/runtime-config-
connection) 2, either:

  * Only accept loopback connections and [use an SSH tunnel](https://www.postgresql.org/docs/12/static/ssh-tunnels) between the machine on which Konvergo ERP runs and the one on which PostgreSQL runs, then configure Konvergo ERP to connect to its end of the tunnel

  * Accept connections to the machine on which Konvergo ERP is installed, possibly over ssl (see [PostgreSQL connection settings](https://www.postgresql.org/docs/12/static/runtime-config-connection) for details), then configure Konvergo ERP to connect over the network

### Configuration sample

  * Allow tcp connection on localhost

  * Allow tcp connection from 192.168.1.x network

in `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/pg_hba.conf` set:

    
    
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    host    all             all             192.168.1.0/24          md5
    

in `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/postgresql.conf` set:

    
    
    listen_addresses = 'localhost,192.168.1.2'
    port = 5432
    max_connections = 80
    

### Configuring Konvergo ERP

Out of the box, Konvergo ERP connects to a local postgres over UNIX socket via port
5432\. This can be overridden using [the database
options](../../developer/reference/cli#reference-cmdline-server-database)
when your Postgres deployment is not local and/or does not use the
installation defaults.

The [packaged installers](packages) will automatically create a new user
(`odoo`) and set it as the database user.

  * The database management screens are protected by the `admin_passwd` setting. This setting can only be set using configuration files, and is simply checked before performing database alterations. It should be set to a randomly generated value to ensure third parties can not use this interface.

  * All database operations use the [database options](../../developer/reference/cli#reference-cmdline-server-database), including the database management screen. For the database management screen to work requires that the PostgreSQL user have `createdb` right.

  * Users can always drop databases they own. For the database management screen to be completely non-functional, the PostgreSQL user needs to be created with `no-createdb` and the database must be owned by a different PostgreSQL user.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>the PostgreSQL user <em>must not</em> be a superuser</p>
</div>

#### Configuration sample

  * connect to a PostgreSQL server on 192.168.1.2

  * port 5432

  * using an ‘odoo’ user account,

  * with ‘pwd’ as a password

  * filtering only db with a name beginning with ‘mycompany’

in [the configuration file](../../developer/reference/cli#reference-
cmdline-config-file) set:

    
    
    [options]
    admin_passwd = mysupersecretpassword
    db_host = 192.168.1.2
    db_port = 5432
    db_user = odoo
    db_password = pwd
    dbfilter = ^mycompany.*$
    

### SSL Between Konvergo ERP and PostgreSQL

Since Konvergo ERP 11.0, you can enforce ssl connection between Konvergo ERP and PostgreSQL.
in Konvergo ERP the db_sslmode control the ssl security of the connection with value
chosen out of ‘disable’, ‘allow’, ‘prefer’, ‘require’, ‘verify-ca’ or ‘verify-
full’

[PostgreSQL Doc](https://www.postgresql.org/docs/12/static/libpq-ssl)

## Builtin server

Konvergo ERP includes built-in HTTP, cron, and live-chat servers, using either multi-
threading or multi-processing.

The **multi-threaded** server is a simpler server primarily used for
development, demonstrations, and its compatibility with various operating
systems (including Windows). A new thread is spawned for every new HTTP
request, even for long-lived connections such as websocket. Extra daemonic
cron threads are spawned too. Due to a Python limitation (GIL), it doesn’t
make the best use of the hardware.

The multi-threaded server is the default server, also for docker containers.
It is selected by leaving the
[`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-workers)
option out or setting it to `0`.

The **multi-processing** server is a full-blown server primarily used for
production. It is not liable to the same Python limitation (GIL) on resource
usage and hence makes the best use of the hardware. A pool of workers is
created upon server startup. New HTTP requests are queued by the OS until
there are workers ready to process them. An extra event-driven HTTP worker for
the live chat is spawned on an alternative port. Extra cron workers are
spawned too. A configurable process reaper monitors resource usage and can
kill/restart failed workers.

The multi-processing server is opt-in. It is selected by setting the
[`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-workers)
option to a non-null integer.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Because it is highly customized for Linux servers, the multi-processing server is not available
on Windows.</p>
</div>

### Worker number calculation

  * Rule of thumb : (#CPU * 2) + 1

  * Cron workers need CPU

  * 1 worker ~= 6 concurrent users

### memory size calculation

  * We consider 20% of the requests are heavy requests, while 80% are simpler ones

  * A heavy worker, when all computed field are well designed, SQL requests are well designed, … is estimated to consume around 1GB of RAM

  * A lighter worker, in the same scenario, is estimated to consume around 150MB of RAM

Needed RAM = #worker * ( (light_worker_ratio * light_worker_ram_estimation) +
(heavy_worker_ratio * heavy_worker_ram_estimation) )

### LiveChat

In multi-processing, a dedicated LiveChat worker is automatically started and
listens on the [`--gevent-port`](../../developer/reference/cli#cmdoption-
odoo-bin-gevent-port). By default, the HTTP requests will keep accessing the
normal HTTP workers instead of the LiveChat one. You must deploy a proxy in
front of Konvergo ERP and redirect incoming requests whose path starts with
`/websocket/` to the LiveChat worker. You must also start Konvergo ERP in [`--proxy-
mode`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode) so it
uses the real client headers (such as hostname, scheme, and IP) instead of the
proxy ones.

### Configuration sample

  * Server with 4 CPU, 8 Thread

  * 60 concurrent users

  * 60 users / 6 = 10 <\- theoretical number of worker needed

  * (4 * 2) + 1 = 9 <\- theoretical maximal number of worker

  * We’ll use 8 workers + 1 for cron. We’ll also use a monitoring system to measure cpu load, and check if it’s between 7 and 7.5 .

  * RAM = 9 * ((0.8*150) + (0.2*1024)) ~= 3Go RAM for Konvergo ERP

in [the configuration file](../../developer/reference/cli#reference-
cmdline-config-file):

    
    
    [options]
    limit_memory_hard = 1677721600
    limit_memory_soft = 629145600
    limit_request = 8192
    limit_time_cpu = 600
    limit_time_real = 1200
    max_cron_threads = 1
    workers = 8
    

## HTTPS

Whether it’s accessed via website/web client or web service, Konvergo ERP transmits
authentication information in cleartext. This means a secure deployment of
Konvergo ERP must use HTTPS3. SSL termination can be implemented via just about any
SSL termination proxy, but requires the following setup:

  * Enable Konvergo ERP’s [`proxy mode`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode). This should only be enabled when Konvergo ERP is behind a reverse proxy

  * Set up the SSL termination proxy ([Nginx termination example](https://nginx.com/resources/admin-guide/nginx-ssl-termination/))

  * Set up the proxying itself ([Nginx proxying example](https://nginx.com/resources/admin-guide/reverse-proxy/))

  * Your SSL termination proxy should also automatically redirect non-secure connections to the secure port

### Configuration sample

  * Redirect http requests to https

  * Proxy requests to odoo

in [the configuration file](../../developer/reference/cli#reference-
cmdline-config-file) set:

    
    
    proxy_mode = True
    

in `/etc/nginx/sites-enabled/odoo.conf` set:

    
    
    #odoo server
    upstream odoo {
      server 127.0.0.1:8069;
    }
    upstream odoochat {
      server 127.0.0.1:8072;
    }
    map $http_upgrade $connection_upgrade {
      default upgrade;
      ''      close;
    }
    
    # http -> https
    server {
      listen 80;
      server_name odoo.mycompany.com;
      rewrite ^(.*) https://$host$1 permanent;
    }
    
    server {
      listen 443 ssl;
      server_name odoo.mycompany.com;
      proxy_read_timeout 720s;
      proxy_connect_timeout 720s;
      proxy_send_timeout 720s;
    
      # SSL parameters
      ssl_certificate /etc/ssl/nginx/server.crt;
      ssl_certificate_key /etc/ssl/nginx/server.key;
      ssl_session_timeout 30m;
      ssl_protocols TLSv1.2;
      ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
      ssl_prefer_server_ciphers off;
    
      # log
      access_log /var/log/nginx/odoo.access.log;
      error_log /var/log/nginx/odoo.error.log;
    
      # Redirect websocket requests to odoo gevent port
      location /websocket {
        proxy_pass http://odoochat;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
    
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
        proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
      }
    
      # Redirect requests to odoo backend server
      location / {
        # Add Headers for odoo proxy mode
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
        proxy_pass http://odoo;
    
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
        proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
      }
    
      # common gzip
      gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
      gzip on;
    }
    

### HTTPS Hardening

Add the `Strict-Transport-Security` header to all requests, in order to
prevent browsers from ever sending a plain HTTP request to this domain. You
will need to maintain a working HTTPS service with a valid certificate on this
domain at all times, otherwise your users will see security alerts or be
entirely unable to access it.

Force HTTPS connections during a year for every visitor in NGINX with the
line:

    
    
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    

Additional configuration can be defined for the `session_id` cookie. The
`Secure` flag can be added to ensure it is never transmitted over HTTP and
`SameSite=Lax` to prevent authenticated
[CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

    
    
    # requires nginx 1.19.8
    proxy_cookie_flags session_id samesite=lax secure;
    

## Konvergo ERP as a WSGI Application

It is also possible to mount Konvergo ERP as a standard
[WSGI](https://wsgi.readthedocs.org/) application. Konvergo ERP provides the base for
a WSGI launcher script as `odoo-wsgi.example.py`. That script should be
customized (possibly after copying it from the setup directory) to correctly
set the configuration directly in `odoo.tools.config` rather than through the
command-line or a configuration file.

However the WSGI server will only expose the main HTTP endpoint for the web
client, website and webservice API. Because Konvergo ERP does not control the creation
of workers anymore it can not setup cron or livechat workers

### Cron Workers

Starting one of the built-in Konvergo ERP servers next to the WSGI server is required
to process cron jobs. That server must be configured to only process crons and
not HTTP requests using the [`--no-
http`](../../developer/reference/cli#cmdoption-odoo-bin-no-http) cli
option or the `http_enable = False` configuration file setting.

On Linux-like systems, using the multi-processing server over the multi-
threading one is recommended to benefit from better hardware usage and
increased stability, i.e., using the
[`--workers=-1`](../../developer/reference/cli#cmdoption-odoo-bin-
workers) and [`--max-cron-
threads=n`](../../developer/reference/cli#cmdoption-odoo-bin-max-cron-
threads) cli options.

### LiveChat

Using a gevent-compatible WSGI server is required for the correct operation of
the live chat feature. That server should be able to handle many simultaneous
long-lived connections but doesn’t need a lot of processing power. All
requests whose path starts with `/websocket/` should be directed to that
server. A regular (thread/process-based) WSGI server should be used for all
other requests.

The Konvergo ERP cron server can also be used to serve the live chat requests. Just
drop the [`--no-http`](../../developer/reference/cli#cmdoption-odoo-bin-
no-http) cli option from the cron server and make sure requests whose path
starts with `/websocket/` are directed to this server, either on the [`--http-
port`](../../developer/reference/cli#cmdoption-odoo-bin-http-port)
(multi-threading server) or on the [`--gevent-
port`](../../developer/reference/cli#cmdoption-odoo-bin-gevent-port)
(multi-processing server).

## Serving static files and attachments

For development convenience, Konvergo ERP directly serves all static files and
attachments in its modules. This may not be ideal when it comes to
performances, and static files should generally be served by a static HTTP
server.

### Serving static files

Konvergo ERP static files are located in each module’s `static/` folder, so static
files can be served by intercepting all requests to `/_MODULE_
/static/_FILE_`, and looking up the right module (and file) in the various
addons paths.

It is recommended to set the `Content-Security-Policy: default-src 'none'`
header on all images delivered by the web server. It is not strictly necessary
as users cannot modify/inject content inside of modules’ `static/` folder and
existing images are final (they do not fetch new resources by themselves).
However, it is good practice.

Using the above NGINX (https) configuration, the following `map` and
`location` blocks should be added to serve static files via NGINX.

    
    
    map $sent_http_content_type $content_type_csp {
        default "";
        ~image/ "default-src 'none'";
    }
    
    server {
        # the rest of the configuration
    
        location @odoo {
            # copy-paste the content of the / location block
        }
    
        # Serve static files right away
        location ~ ^/[^/]+/static/.+$ {
            # root and try_files both depend on your addons paths
            root ...;
            try_files ... @odoo;
            expires 24h;
            add_header Content-Security-Policy $content_type_csp;
        }
    }
    

The actual `root` and `try_files` directives are dependant on your
installation, specifically on your [`--addons-
path`](../../developer/reference/cli#cmdoption-odoo-bin-addons-path).

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-RGViaWFuIHBhY2thZ2U=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tab" tabindex="0">Debian package</button><button aria-controls="panel-0-R2l0IHNvdXJjZXM=" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tab" tabindex="-1">Git sources</button></div><div aria-labelledby="tab-0-RGViaWFuIHBhY2thZ2U=" class="sphinx-tabs-panel group-tab" id="panel-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tabpanel" tabindex="0"><p>Say Konvergo ERP has been installed via the <b>debian packages</b> for Community and Enterprise, and
that the <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> is
<code>'/usr/lib/python3/dist-packages/odoo/addons'</code>.</p>
<p>The <code>root</code> and <code>try_files</code> should be:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/usr/lib/python3/dist-packages/odoo/addons</span><span class="p">;</span>
<span class="k">try_files</span> <span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-0-R2l0IHNvdXJjZXM=" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tabpanel" tabindex="0"><p>Say Konvergo ERP has been installed via the <b>sources</b>, that both the Community and Enterprise git
repositories were cloned in <code>/opt/odoo/community</code> and <code>/opt/odoo/enterprise</code>
respectively, and that the <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> is
<code>'/opt/odoo/community/odoo/addons,/opt/odoo/community/addons,/opt/odoo/enterprise'</code>.</p>
<p>The <code>root</code> and <code>try_files</code> should be:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/opt/odoo</span><span class="p">;</span>
<span class="k">try_files</span> <span class="s">/community/odoo/addons</span><span class="nv">$uri</span> <span class="s">/community/addons</span><span class="nv">$uri</span> <span class="s">/enterprise</span><span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div></div>
</div>

### Serving attachments

Attachments are files stored in the filestore which access is regulated by
Konvergo ERP. They cannot be directly accessed via a static web server as accessing
them requires multiple lookups in the database to determine where the files
are stored and whether the current user can access them or not.

Nevertheless, once the file has been located and the access rights verified by
Konvergo ERP, it is a good idea to serve the file using the static web server instead
of Konvergo ERP. For Konvergo ERP to delegate serving files to the static web server, the
[X-Sendfile](https://tn123.org/mod_xsendfile/) (apache) or
[X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/)
(nginx) extensions must be enabled and configured on the static web server.
Once it is set up, start Konvergo ERP with the
[`--x-sendfile`](../../developer/reference/cli#cmdoption-odoo-bin-x-
sendfile) CLI flag (this unique flag is used for both X-Sendfile and X-Accel).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The X-Sendfile extension for apache (and compatible web servers) does not require any
supplementary configuration.</p></li>
<li><p>The X-Accel extension for NGINX <b>does</b> require the following additionnal configuration:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">location</span> <span class="s">/web/filestore</span> <span class="p">{</span>
    <span class="kn">internal</span><span class="p">;</span>
    <span class="kn">alias</span> <span class="s">/path/to/odoo/data-dir/filestore</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>In case you don’t know what is the path to your filestore, start Konvergo ERP with the
<a href="../../developer/reference/cli#cmdoption-odoo-bin-x-sendfile"><code>--x-sendfile</code></a> option and navigate to the <code>/web/filestore</code> URL
directly via Konvergo ERP (don’t navigate to the URL via NGINX). This logs a warnings, the message
contains the configuration you need.</p>
</li>
</ul>
</div>

## Security

For starters, keep in mind that securing an information system is a continuous
process, not a one-shot operation. At any moment, you will only be as secure
as the weakest link in your environment.

So please do not take this section as the ultimate list of measures that will
prevent all security problems. It’s only intended as a summary of the first
important things you should be sure to include in your security action plan.
The rest will come from best security practices for your operating system and
distribution, best practices in terms of users, passwords, and access control
management, etc.

When deploying an internet-facing server, please be sure to consider the
following security-related topics:

  * Always set a strong super-admin admin password, and restrict access to the database management pages as soon as the system is set up. See Database Manager Security.

  * Choose unique logins and strong passwords for all administrator accounts on all databases. Do not use ‘admin’ as the login. Do not use those logins for day-to-day operations, only for controlling/managing the installation. _Never_ use any default passwords like admin/admin, even for test/staging databases.

  * Do **not** install demo data on internet-facing servers. Databases with demo data contain default logins and passwords that can be used to get into your systems and cause significant trouble, even on staging/dev systems.

  * Use appropriate database filters ( [`--db-filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter)) to restrict the visibility of your databases according to the hostname. See dbfilter. You may also use [`-d`](../../developer/reference/cli#cmdoption-odoo-bin-d) to provide your own (comma-separated) list of available databases to filter from, instead of letting the system fetch them all from the database backend.

  * Once your `db_name` and `db_filter` are configured and only match a single database per hostname, you should set `list_db` configuration option to `False`, to prevent listing databases entirely, and to block access to the database management screens (this is also exposed as the [`--no-database-list`](../../developer/reference/cli#cmdoption-odoo-bin-no-database-list) command-line option)

  * Make sure the PostgreSQL user ([`--db_user`](../../developer/reference/cli#cmdoption-odoo-bin-r)) is _not_ a super-user, and that your databases are owned by a different user. For example they could be owned by the `postgres` super-user if you are using a dedicated non-privileged `db_user`. See also Configuring Konvergo ERP.

  * Keep installations updated by regularly installing the latest builds, either via GitHub or by downloading the latest version from <https://www.odoo.com/page/download> or <http://nightly.odoo.com>

  * Configure your server in multi-process mode with proper limits matching your typical usage (memory/CPU/timeouts). See also Builtin server.

  * Run Konvergo ERP behind a web server providing HTTPS termination with a valid SSL certificate, in order to prevent eavesdropping on cleartext communications. SSL certificates are cheap, and many free options exist. Configure the web proxy to limit the size of requests, set appropriate timeouts, and then enable the [`proxy mode`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode) option. See also HTTPS.

  * If you need to allow remote SSH access to your servers, make sure to set a strong password for **all** accounts, not just `root`. It is strongly recommended to entirely disable password-based authentication, and only allow public key authentication. Also consider restricting access via a VPN, allowing only trusted IPs in the firewall, and/or running a brute-force detection system such as `fail2ban` or equivalent.

  * Consider installing appropriate rate-limiting on your proxy or firewall, to prevent brute-force attacks and denial of service attacks. See also Blocking Brute Force Attacks for specific measures.

Many network providers provide automatic mitigation for Distributed Denial of
Service attacks (DDOS), but this is often an optional service, so you should
consult with them.

  * Whenever possible, host your public-facing demo/test/staging instances on different machines than the production ones. And apply the same security precautions as for production.

  * If your public-facing Konvergo ERP server has access to sensitive internal network resources or services (e.g. via a private VLAN), implement appropriate firewall rules to protect those internal resources. This will ensure that the Konvergo ERP server cannot be used accidentally (or as a result of malicious user actions) to access or disrupt those internal resources. Typically this can be done by applying an outbound default DENY rule on the firewall, then only explicitly authorizing access to internal resources that the Konvergo ERP server needs to access. [Systemd IP traffic access control](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd) may also be useful to implement per-process network access control.

  * If your public-facing Konvergo ERP server is behind a Web Application Firewall, a load-balancer, a transparent DDoS protection service (like CloudFlare) or a similar network-level device, you may wish to avoid direct access to the Konvergo ERP system. It is generally difficult to keep the endpoint IP addresses of your Konvergo ERP servers secret. For example they can appear in web server logs when querying public systems, or in the headers of emails posted from Konvergo ERP. In such a situation you may want to configure your firewall so that the endpoints are not accessible publicly except from the specific IP addresses of your WAF, load-balancer or proxy service. Service providers like CloudFlare usually maintain a public list of their IP address ranges for this purpose.

  * If you are hosting multiple customers, isolate customer data and files from each other using containers or appropriate “jail” techniques.

  * Setup daily backups of your databases and filestore data, and copy them to a remote archiving server that is not accessible from the server itself.

  * Deploying Konvergo ERP on Linux is strongly recommended over Windows. Should you choose nevertheless to deploy on a Windows platform, a thorough security hardening review of the server should be conducted and is outside of the scope of this guide.

### Blocking Brute Force Attacks

For internet-facing deployments, brute force attacks on user passwords are
very common, and this threat should not be neglected for Konvergo ERP servers. Konvergo ERP
emits a log entry whenever a login attempt is performed, and reports the
result: success or failure, along with the target login and source IP.

The log entries will have the following form.

Failed login:

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1
    

Successful login:

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login successful for db:db_name login:admin from 127.0.0.1
    

These logs can be easily analyzed by an intrusion prevention system such as
`fail2ban`.

For example, the following fail2ban filter definition should match a failed
login:

    
    
    [Definition]
    failregex = ^ \d+ INFO \S+ \S+ Login failed for db:\S+ login:\S+ from <HOST>
    ignoreregex =
    

This could be used with a jail definition to block the attacking IP on
HTTP(S).

Here is what it could look like for blocking the IP for 15 minutes when 10
failed login attempts are detected from the same IP within 1 minute:

    
    
    [odoo-login]
    enabled = true
    port = http,https
    bantime = 900  ; 15 min ban
    maxretry = 10  ; if 10 attempts
    findtime = 60  ; within 1 min  /!\ Should be adjusted with the TZ offset
    logpath = /var/log/odoo.log  ;  set the actual odoo log path here
    

### Database Manager Security

Configuring Konvergo ERP mentioned `admin_passwd` in passing.

This setting is used on all database management screens (to create, delete,
dump or restore databases).

If the management screens must not be accessible at all, you should set
`list_db` configuration option to `False`, to block access to all the database
selection and management screens.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>It is strongly recommended to disable the Database Manager for any internet-facing
system! It is meant as a development/demo tool, to make it easy to quickly create
and manage databases. It is not designed for use in production, and may even expose
dangerous features to attackers. It is also not designed to handle large databases,
and may trigger memory limits.</p>
<p>On production systems, database management operations should always be performed by
the system administrator, including provisioning of new databases and automated backups.</p>
</div>

Be sure to setup an appropriate `db_name` parameter (and optionally,
`db_filter` too) so that the system can determine the target database for each
request, otherwise users will be blocked as they won’t be allowed to choose
the database themselves.

If the management screens must only be accessible from a selected set of
machines, use the proxy server’s features to block access to all routes
starting with `/web/database` except (maybe) `/web/database/selector` which
displays the database-selection screen.

If the database-management screen should be left accessible, the
`admin_passwd` setting must be changed from its `admin` default: this password
is checked before allowing database-alteration operations.

It should be stored securely, and should be generated randomly e.g.

    
    
    $ python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)))'
    

which generates a 32-character pseudorandom printable string.

### Reset the master password

There may be instances where the master password is misplaced, or compromised,
and needs to be reset. The following process is for system administrators of
an Konvergo ERP on-premise database detailing how to manually reset and re-encrypt the
master password.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For more information about changing an Konvergo ERP.com account password, see this documentation:
<a href="../odoo_accounts#odoocom-change-password"><span class="std std-ref">Konvergo ERP.com account password change</span></a>.</p>
</div>

When creating a new on-premise database, a random master password is
generated. Konvergo ERP recommends using this password to secure the database. This
password is implemented by default, so there is a secure master password for
any Konvergo ERP on-premise deployment.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>When creating an Konvergo ERP on-premise database the installation is accessible to anyone on the
internet, until this password is set to secure the database.</p>
</div>

The master password is specified in the Konvergo ERP configuration file (`odoo.conf`
or `odoorc` (hidden file)). The Konvergo ERP master password is needed to modify,
create, or delete a database through the graphical user interface (GUI).

#### Locate configuration file

First, open the Konvergo ERP configuration file (`odoo.conf` or `odoorc` (hidden
file)).

WindowsLinux

The configuration file is located at:
`c:\ProgramFiles\Konvergo ERP{VERSION}\server\odoo.conf`

Depending on how Konvergo ERP is installed on the Linux machine, the configuration
file is located in one of two different places:

  * Package installation: `/etc/odoo.conf`

  * Source installation: `~/.odoorc`

#### Change old password

Once the appropriate file has been opened, proceed to modify the old password
in the configuration file to a temporary password.

Graphical user interfaceCommand-line interface

After locating the configuration file, open it using a (GUI). This can be
achieved by simply double clicking on the file. Then, the device should have a
default GUI to open the file with.

Next, modify the master password line `admin_passwd = $pbkdf2-sha…` to
`admin_passwd = newpassword1234`, for example. This password can be anything,
as long as it is saved temporarily. Make sure to modify all characters after
the `=`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The line appears like this:
<code>admin_passwd =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m</code></p>
<p>The modified line appears like this: <code>admin_passwd = newpassword1234</code></p>
</div>

Modify the master password line using the following Unix command detailed
below.

Connect to the Konvergo ERP server’s terminal via Secure Shell (SSH) protocol, and
edit the configuration file. To modify the configuration file, enter the
following command: **sudo nano /etc/odoo.conf**

After opening the configuration file, modify the master password line
`admin_passwd = $pbkdf2-sha…` to `admin_passwd = newpassword1234`. This
password can be anything, as long as it is saved temporarily. Make sure to
modify all characters after the `=`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>0

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>1

#### Restart Konvergo ERP server

After setting the temporary password, a restart of the Konvergo ERP server is
**required**.

Graphical user interfaceCommand-line interface

To restart the Konvergo ERP server, first, type `services` into the Windows **Search**
bar. Then, select the **Services** application, and scroll down to the
**Konvergo ERP** service.

Next, right click on **Konvergo ERP** , and select **Start** or **Restart**. This
action manually restarts the Konvergo ERP server.

Restart the Konvergo ERP server by typing the command: **sudo service odoo15 restart**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>2

#### Use web interface to re-encrypt password

First, navigate to `/web/database/manager` or
`http://server_ip:port/web/database/manager` in a browser.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>3

Next, click **Set Master Password** , and type in the previously-selected
temporary password into the **Master Password** field. Following this step,
type in a **New Master Password**. The **New Master Password** is hashed (or
encrypted), once the **Continue** button is clicked.

At this point, the password has been successfully reset, and a hashed version
of the new password now appears in the configuration file.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>4

## Supported Browsers

Konvergo ERP supports all the major desktop and mobile browsers available on the
market, as long as they are supported by their publishers.

Here are the supported browsers:

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge

  * Apple Safari

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Setting a proper <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> is an important part
of securing your deployment.
Once it is correctly working and only matching a single database per hostname, it
is strongly recommended to block access to the database manager screens,
and to use the <code>--no-database-list</code> startup parameter to prevent listing
your databases, and to block access to the database management screens.
See also <a href="#security">security</a>.</p>
</div>6

1

    

to have multiple Konvergo ERP installations use the same PostgreSQL database, or to
provide more computing resources to both software.

2

    

technically a tool like [socat](http://www.dest-unreach.org/socat/) can be
used to proxy UNIX sockets across networks, but that is mostly for software
which can only be used over UNIX sockets

3

    

or be accessible only over an internal packet-switched network, but that
requires secured switches, protections against [ARP
spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) and precludes usage of
WiFi. Even over secure packet-switched networks, deployment over HTTPS is
recommended, and possible costs are lowered as “self-signed” certificates are
easier to deploy on a controlled environment than over the internet.

  *[GUI]: graphical user interface

