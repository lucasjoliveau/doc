# Chapter 2: Development environment setup

Depending on the intended use case, there are multiple ways to install Konvergo ERP.
For developers of the Konvergo ERP community and Konvergo ERP employees alike, the preferred
way is to perform a source install (running Konvergo ERP from the source code).

## Prepare the environment

First, follow the [Environment
setup](../../../contributing/development#contributing-development-setup)
section of the contributing guide to prepare your environment.

By now, you should have downloaded the source code into two local
repositories, one for `odoo/odoo` and one for `odoo/enterprise`. These
repositories are set up to push changes to pre-defined forks on GitHub. This
will prove to be convenient when you start contributing to the codebase, but
for the scope of this tutorial, we want to avoid polluting them with training
material. Let’s then develop your own module in a third repository
`odoo/tutorials`. Like the first two repositories, it will be part of the
`addons-path` that references all directories containing Konvergo ERP modules. In this
repository, we will create our first module!

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>This repository also already contains some bare modules that will be used in other tutorials.</p>
</div>

  1. Following the same process as with the `odoo/odoo` and `odoo/enterprise` repositories, clone the `odoo/tutorials` repository on your machine with:
    
        $ git clone git@github.com:odoo/tutorials.git
    

  2. Configure your fork and Git to push changes to your fork rather than to the main codebase. If you work at Konvergo ERP, configure Git to push changes to the shared fork created on the account **odoo-dev**.

Link Git with your forkLink Git with odoo-dev

    1. Visit [github.com/odoo/tutorials](https://github.com/odoo/tutorials) and click the **Fork** button to create a fork of the repository on your account.

    2. In the command below, replace `<your_github_account>` with the name of the GitHub account on which you created the fork.
        
                $ cd /TutorialsPath
        $ git remote add dev git@github.com:<your_github_account>/tutorials.git
        
    
        $ cd /tutorials
    $ git remote add dev git@github.com:odoo-dev/tutorials.git
    $ git remote set-url --push origin you_should_not_push_on_this_repository
    

That’s it! Your environment is now prepared to run Konvergo ERP from the sources, and
you have successfully created a repository to serve as an addons directory.
This will allow you to push your work to GitHub.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p><b>For Konvergo ERP employees only:</b></p>
<ol class="arabic">
<li><p>Make sure to read very carefully <a href="../../../contributing/development#contributing-development-first-contribution"><span class="std std-ref">Make your first contribution</span></a>. In particular,
your branch name must follow our conventions.</p></li>
<li><p>Once you have pushed your first change to the shared fork on <b>odoo-dev</b>, create a
<abbr title="Pull Request">PR</abbr>. Please put your quadrigram in the PR title (e.g., «abcd - Technical
Training»).</p>
<p>This will enable you to share your upcoming work and receive feedback from your coaches. To ensure
a continuous feedback loop, we recommend pushing a new commit as soon as you complete a chapter
of the tutorial. Note that the PR is automatically updated with commits you push to <b>odoo-dev</b>,
you don’t need to open multiple PRs.</p>
</li>
<li><p>At Konvergo ERP we use <a href="https://runbot.odoo.com">Runbot</a> extensively for our <abbr title="Continuous Integration">CI</abbr> tests. When you push your changes to <b>odoo-dev</b>, Runbot creates a new build
and test your code. Once logged in, you will be able to see your branches <a href="https://runbot.odoo.com/runbot/tutorials-12">Tutorials project</a>.</p></li>
</ol>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>The specific location of the repositories on your file system is not crucial. However, for the
sake of simplicity, we will assume that you have cloned all the repositories under the same
directory. If this is not the case, make sure to adjust the following commands accordingly,
providing the appropriate relative path from the <code>odoo/odoo</code> repository to the
<code>odoo/tutorials</code> repository.</p>
</div>

## Run the server

### Launch with `odoo-bin`

Once all dependencies are set up, Konvergo ERP can be launched by running `odoo-bin`,
the command-line interface of the server.

    
    
    $ cd $HOME/src/odoo/
    $ ./odoo-bin --addons-path="addons/,../enterprise/,../tutorials" -d rd-demo
    

There are multiple [command-line
arguments](../../reference/cli#reference-cmdline-server) that you can use
to run the server. In this training you will only need some of them.

-d <database>
    

The database that is going to be used.

\--addons-path <directories>

    

A comma-separated list of directories in which modules are stored. These
directories are scanned for modules.

\--limit-time-cpu <limit>

    

Prevent the worker from using more than <limit> CPU seconds for each request.

\--limit-time-real <limit>

    

Prevent the worker from taking longer than <limit> seconds to process a
request.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>The <a href="#cmdoption-limit-time-cpu"><code>--limit-time-cpu</code></a> and <a href="#cmdoption-limit-time-real"><code>--limit-time-real</code></a> arguments can be used to prevent
the worker from being killed when debugging the source code.</p></li>
<li><div class="line-block">
<div class="line">You may face an error similar to <code>AttributeError: module '&lt;MODULE_NAME&gt;' has no attribute
'&lt;$ATTRIBUTE'&gt;</code>. In this case, you may need to re-install the module with <b class="command o_code">$ pip
install --upgrade --force-reinstall &lt;MODULE_NAME&gt;</b>.</div>
<div class="line">If this error occurs with more than one module, you may need to re-install all the
requirements with <b class="command o_code">$ pip install --upgrade --force-reinstall -r requirements.txt</b>.</div>
<div class="line">You can also clear the python cache to solve the issue:</div>
</div>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> <span class="nb">cd</span> <span class="nv">$HOME</span>/.local/lib/python3.8/site-packages/
<span class="gp">$</span> find -name <span class="s1">'*.pyc'</span> -type f -delete
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Other commonly used arguments are:</p>
<ul>
<li><p><a href="../../reference/cli#cmdoption-odoo-bin-i"><code>-i</code></a>: Install some modules before running the server
(comma-separated list). This is equivalent to going to <b>Apps</b> in the user interface,
and installing the module from there.</p></li>
<li><p><a href="../../reference/cli#cmdoption-odoo-bin-u"><code>-u</code></a>: Update some modules before running the server
(comma-separated list). This is equivalent to going to <b>Apps</b> in the user interface,
selecting a module, and upgrading it from there.</p></li>
</ul>
</li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>For now you cannot add <code>../technical-training-sandbox</code> to your <code>addons-path</code> as it is empty
and will result into an invalid addons-path folder error, but you will have to add it back later on !</p>
</div>

### Log in to Konvergo ERP

Open <http://localhost:8069/> on your browser. We recommend using
[Chrome](https://www.google.com/intl/en/chrome/),
[Firefox](https://www.mozilla.org/firefox/new/), or any other browser with
development tools.

To log in as the administrator user, use the following credentials:

  * email: `admin`

  * password: `admin`

## Enable the developer mode

The developer or debug mode is useful for training as it gives access to
additional (advanced) tools. In the next chapters, **we will always assume
that you have enabled the developer mode**.

[Enable the developer
mode](../../../applications/general/developer_mode#developer-mode) now.
Choose the method that you prefer; they are all equivalent.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>The main page of the Settings screen is only accessible if at least one application is installed.
You will be led into installing your own application in the next chapter.</p>
</div>

## Extra tools

### Useful Git commands

Here are some useful Git commands for your day-to-day work.

  * Switch branches:

When you switch branches, both repositories (odoo and enterprise) must be
synchronized, i.e. both need to be in the same branch.

    
        $ cd $HOME/src/odoo
    $ git switch 16.0
    
    $ cd $HOME/src/enterprise
    $ git switch 16.0
    

  * Fetch and rebase:
    
        $ cd $HOME/src/odoo
    $ git fetch --all --prune
    $ git rebase --autostash odoo/16.0
    
    $ cd $HOME/src/enterprise
    $ git fetch --all --prune
    $ git rebase --autostash enterprise/16.0
    

### Code Editor

If you are working at Konvergo ERP, many of your colleagues are using
[VSCode](https://code.visualstudio.com), [VSCodium](https://vscodium.com) (the
open source equivalent),
[PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux), or
[Sublime Text](https://www.sublimetext.com). However, you are free to choose
your preferred editor.

It is important to configure your linters correctly. Using a linter helps you
by showing syntax and semantic warnings or errors. Konvergo ERP source code tries to
respect Python’s and JavaScript’s standards, but some of them can be ignored.

For Python, we use PEP8 with these options ignored:

  * `E501`: line too long

  * `E301`: expected 1 blank line, found 0

  * `E302`: expected 2 blank lines, found 1

For JavaScript, we use ESLint and you can find a [configuration file example
here](https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines#use-a-
linter).

### Administrator tools for PostgreSQL

You can manage your PostgreSQL databases using the command line as
demonstrated earlier or using a GUI application such as
[pgAdmin](https://www.pgadmin.org/download/pgadmin-4-apt/) or
[DBeaver](https://dbeaver.io/).

To connect the GUI application to your database we recommend you connect using
the Unix socket.

  * Host name/address: `/var/run/postgresql`

  * Port: `5432`

  * Username: `$USER`

### Python Debugging

When facing a bug or trying to understand how the code works, simply printing
things out can go a long way, but a proper debugger can save a lot of time.

You can use a classic Python library debugger
([pdb](https://docs.python.org/3/library/pdb),
[pudb](https://pypi.org/project/pudb/) or
[ipdb](https://pypi.org/project/ipdb/)), or you can use your editor’s
debugger.

In the following example we use ipdb, but the process is similar with other
libraries.

  1. Install the library:
    
        pip install ipdb
    

  2. Place a trigger (breakpoint):
    
        import ipdb; ipdb.set_trace()
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="hll">    <span class="kn">import</span> <span class="nn">ipdb</span><span class="p">;</span> <span class="n">ipdb</span><span class="o">.</span><span class="n">set_trace</span><span class="p">()</span>
</span>    <span class="bp">self</span><span class="o">.</span><span class="n">ensure_one</span><span class="p">()</span>
    <span class="n">chosen_name</span> <span class="o">=</span> <span class="n">default</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'name'</span><span class="p">)</span> <span class="k">if</span> <span class="n">default</span> <span class="k">else</span> <span class="s1">''</span>
    <span class="n">new_name</span> <span class="o">=</span> <span class="n">chosen_name</span> <span class="ow">or</span> <span class="n">_</span><span class="p">(</span><span class="s1">'</span><span class="si">%s</span><span class="s1"> (copy)'</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
    <span class="n">default</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">default</span> <span class="ow">or</span> <span class="p">{},</span> <span class="n">name</span><span class="o">=</span><span class="n">new_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">super</span><span class="p">(</span><span class="n">Partner</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">default</span><span class="p">)</span>
</pre></div>
</div>
</div>

Here is a list of commands:

h(elp) [command]

    

Print the list of available commands if not argument is supplied. With a
command as an argument, print the help about that command.

pp expression

    

The value of the `expression` is pretty-printed using the `pprint` module.

w(here)

    

Print a stack trace with the most recent frame at the bottom.

d(own)

    

Move the current frame one level down in the stack trace (to a newer frame).

u(p)

    

Move the current frame one level up in the stack trace (to an older frame).

n(ext)

    

Continue the execution until the next line in the current function is reached
or it returns.

c(ontinue)

    

Continue the execution and only stop when a breakpoint is encountered.

s(tep)

    

Execute the current line. Stop at the first possible occasion (either in a
function that is called or on the next line in the current function).

q(uit)

    

Quit the debugger. The program being executed is aborted.

Now that your server is running, it’s time to start [writing your own
application](03_newapp#tutorials-getting-started-03-newapp)!

