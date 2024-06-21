# Source install

The source ‘installation’ is not about installing Konvergo ERP but running it directly
from the source instead.

Using the Konvergo ERP source can be more convenient for module developers as it is
more easily accessible than using packaged installers.

It makes starting and stopping Konvergo ERP more flexible and explicit than the
services set up by the packaged installers. Also, it allows overriding
settings using [command-line
parameters](../../developer/reference/cli#reference-cmdline) without
needing to edit a configuration file.

Finally, it provides greater control over the system’s setup and allows to
more easily keep (and run) multiple versions of Konvergo ERP side-by-side.

## Fetch the sources

There are two ways to obtain the source code of Konvergo ERP: as a ZIP **archive** or
through **Git**.

### Archive

Community edition:

  * [Konvergo ERP download page](https://www.odoo.com/page/download)

  * [GitHub Community repository](https://github.com/odoo/odoo)

  * [Nightly server](https://nightly.odoo.com)

Enterprise edition:

  * [Konvergo ERP download page](https://www.odoo.com/page/download)

  * [GitHub Enterprise repository](https://github.com/odoo/enterprise)

### Git

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is required to have <a href="https://git-scm.com/">Git</a> installed, and it is recommended to have a
basic knowledge of Git commands to proceed.</p>
</div>

To clone a Git repository, choose between cloning with HTTPS or SSH. In most
cases, the best option is HTTPS. However, choose SSH to contribute to Konvergo ERP
source code or when following the [Getting Started developer
tutorial](../../developer/tutorials/getting_started).

LinuxWindowsMac OS

Clone with HTTPSClone with SSH

    
    
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/odoo/enterprise.git
    
    
    
    $ git clone git@github.com:odoo/odoo.git
    $ git clone git@github.com:odoo/enterprise.git
    

Clone with HTTPSClone with SSH

    
    
    C:\> git clone https://github.com/odoo/odoo.git
    C:\> git clone https://github.com/odoo/enterprise.git
    
    
    
    C:\> git clone git@github.com:odoo/odoo.git
    C:\> git clone git@github.com:odoo/enterprise.git
    

Clone with HTTPSClone with SSH

    
    
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/odoo/enterprise.git
    
    
    
    $ git clone git@github.com:odoo/odoo.git
    $ git clone git@github.com:odoo/enterprise.git
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>

## Prepare

### Python

Konvergo ERP requires **Python 3.7** or later to run.

LinuxWindowsMac OS

Use a package manager to download and install Python 3 if needed.

[Download the latest version of Python
3](https://www.python.org/downloads/windows/) and install it.

During installation, check **Add Python 3 to PATH** , then click **Customize
Installation** and make sure that **pip** is checked.

Use a package manager ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)) to download and install Python 3 if
needed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If Python 3 is already installed, make sure that the version is 3.7 or above, as previous
versions are not compatible with Konvergo ERP.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-5-TGludXg=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-5-TGludXg=" name="TGludXg=" role="tab" tabindex="0">Linux</button><button aria-controls="panel-5-V2luZG93cw==" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-5-V2luZG93cw==" name="V2luZG93cw==" role="tab" tabindex="-1">Windows</button><button aria-controls="panel-5-TWFjIE9T" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-5-TWFjIE9T" name="TWFjIE9T" role="tab" tabindex="-1">Mac OS</button></div><div aria-labelledby="tab-5-TGludXg=" class="sphinx-tabs-panel group-tab" id="panel-5-TGludXg=" name="TGludXg=" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python3 --version
</pre></div>
</div>
</div><div aria-labelledby="tab-5-V2luZG93cw==" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-5-V2luZG93cw==" name="V2luZG93cw==" role="tabpanel" tabindex="0"><div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:\&gt;</span> python --version
</pre></div>
</div>
</div><div aria-labelledby="tab-5-TWFjIE9T" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-5-TWFjIE9T" name="TWFjIE9T" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python3 --version
</pre></div>
</div>
</div></div>
<p>Verify that <a href="https://pip.pypa.io">pip</a> is also installed for this version.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-6-TGludXg=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-6-TGludXg=" name="TGludXg=" role="tab" tabindex="0">Linux</button><button aria-controls="panel-6-V2luZG93cw==" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-6-V2luZG93cw==" name="V2luZG93cw==" role="tab" tabindex="-1">Windows</button><button aria-controls="panel-6-TWFjIE9T" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-6-TWFjIE9T" name="TWFjIE9T" role="tab" tabindex="-1">Mac OS</button></div><div aria-labelledby="tab-6-TGludXg=" class="sphinx-tabs-panel group-tab" id="panel-6-TGludXg=" name="TGludXg=" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> pip3 --version
</pre></div>
</div>
</div><div aria-labelledby="tab-6-V2luZG93cw==" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-6-V2luZG93cw==" name="V2luZG93cw==" role="tabpanel" tabindex="0"><div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:\&gt;</span> pip --version
</pre></div>
</div>
</div><div aria-labelledby="tab-6-TWFjIE9T" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-6-TWFjIE9T" name="TWFjIE9T" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> pip3 --version
</pre></div>
</div>
</div></div>
</div>

### PostgreSQL

Konvergo ERP uses PostgreSQL as its database management system.

LinuxWindowsMac OS

Use a package manager to download and install PostgreSQL (supported versions:
12.0 or above). It can be achieved by executing the following:

    
    
    $ sudo apt install postgresql postgresql-client
    

[Download PostgreSQL](https://www.postgresql.org/download/windows) (supported
versions: 12.0 or above) and install it.

Use [Postgres.app](https://postgresapp.com) to download and install PostgreSQL
(supported version: 12.0 or above).

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To make the command line tools bundled with Postgres.app available, make sure to set up the
<code>$PATH</code> variable by following the <a href="https://postgresapp.com/documentation/cli-tools">Postgres.app CLI tools instructions</a>.</p>
</div>

By default, the only user is `postgres`. As Konvergo ERP forbids connecting as
`postgres`, create a new PostgreSQL user.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Because the PostgreSQL user has the same name as the Unix login, it is possible to connect
to the database without a password.</p>
</div>

  1. Add PostgreSQL’s `bin` directory (by default: `C:\Program Files\PostgreSQL\<version>\bin`) to the `PATH`.

  2. Create a postgres user with a password using the pg admin gui:

    1. Open **pgAdmin**.

    2. Double-click the server to create a connection.

    3. Select Object ‣ Create ‣ Login/Group Role.

    4. Enter the username in the **Role Name** field (e.g., `odoo`).

    5. Open the **Definition** tab, enter a password (e.g., `odoo`), and click **Save**.

    6. Open the **Privileges** tab and switch **Can login?** to `Yes` and **Create database?** to `Yes`.

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Because the PostgreSQL user has the same name as the Unix login, it is possible to connect
to the database without a password.</p>
</div>

### Dependencies

LinuxWindowsMac OS

Using **distribution packages** is the preferred way of installing
dependencies. Alternatively, install the Python dependencies with **pip**.

Debian/UbuntuInstall with pip

On Debian/Ubuntu, the following commands should install the required packages:

    
    
    $ cd odoo #CommunityPath
    $ sudo ./setup/debinstall.sh
    

The `setup/debinstall.sh` script will parse the
[debian/control](https://github.com/odoo/odoo/blob/16.0/debian/control) file
and install the found packages.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Using pip may lead to security issues and broken dependencies; only do this if you
know what you are doing.</p>
</div>

As some of the Python packages need a compilation step, they require system
libraries to be installed.

On Debian/Ubuntu, the following command should install these required
libraries:

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Konvergo ERP dependencies are listed in the `requirements.txt` file located at the
root of the Konvergo ERP Community directory.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The Python packages in <code>requirements.txt</code> are based on their stable/LTS
Debian/Ubuntu corresponding version at the moment of the Konvergo ERP release. For example,
for Konvergo ERP 15.0, the <code>python3-babel</code> package version is 2.8.0 in Debian Bullseye and
2.6.0 in Ubuntu Focal. The lowest version is then chosen in the
<code>requirements.txt</code>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It can be preferable not to mix Python module packages between different instances of
Konvergo ERP or with the system. However, it is possible to use <a href="https://pypi.org/project/virtualenv/">virtualenv</a> to create isolated Python environments.</p>
</div>

Navigate to the path of the Konvergo ERP Community installation (`CommunityPath`) and
run **pip** on the requirements file to install the requirements for the
current user.

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Before installing the dependencies, download and install the [Build Tools for
Visual Studio](https://visualstudio.microsoft.com/downloads/). Select **C++
build tools** in the **Workloads** tab and install them when prompted.

Konvergo ERP dependencies are listed in the `requirements.txt` file located at the
root of the Konvergo ERP Community directory.

> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It can be preferable not to mix Python module packages between different instances of
Konvergo ERP or with the system. However, it is possible to use <a href="https://pypi.org/project/virtualenv/">virtualenv</a> to create isolated Python environments.</p>
</div>

Navigate to the path of the Konvergo ERP Community installation (`CommunityPath`) and
run **pip** on the requirements file in a terminal **with Administrator
privileges** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Konvergo ERP dependencies are listed in the `requirements.txt` file located at the
root of the Konvergo ERP Community directory.

> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>0

Navigate to the path of the Konvergo ERP Community installation (`CommunityPath`) and
run **pip** on the requirements file:

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>1

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>3

## Running Konvergo ERP

Once all dependencies are set up, Konvergo ERP can be launched by running `odoo-bin`,
the command-line interface of the server. It is located at the root of the
Konvergo ERP Community directory.

To configure the server, either specify [command-line
arguments](../../developer/reference/cli#reference-cmdline-server) or a
[configuration file](../../developer/reference/cli#reference-cmdline-
config).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>4

Common necessary configurations are:

  * PostgreSQL user and password.

  * Custom addon paths beyond the defaults to load custom modules.

A typical way to run the server would be:

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Konvergo ERP Community installation, and
`mydb` is the name of the PostgreSQL database.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Konvergo ERP Community installation, `dbuser`
is the PostgreSQL login, `dbpassword` is the PostgreSQL password, and `mydb`
is the name of the PostgreSQL database.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Konvergo ERP Community installation, and
`mydb` is the name of the PostgreSQL database.

After the server has started (the INFO log `odoo.modules.loading: Modules
loaded.` is printed), open <http://localhost:8069> in a web browser and log
into the Konvergo ERP database with the base administrator account: use `admin` as the
email and, again, `admin` as the password.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>The Enterprise git repository does not contain the full Konvergo ERP source code</b>. It is only a
collection of extra add-ons. The main server code is in the Community edition. Running the
Enterprise version means running the server from the Community version with the <code>addons-path</code>
option set to the folder with the Enterprise edition. It is required to clone both the Community
and Enterprise repositories to have a working Konvergo ERP Enterprise installation.</p>
</div>6

