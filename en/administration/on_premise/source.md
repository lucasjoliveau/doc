# Source install

The source ‘installation’ is not about installing Odoo but running it directly
from the source instead.

Using the Odoo source can be more convenient for module developers as it is
more easily accessible than using packaged installers.

It makes starting and stopping Odoo more flexible and explicit than the
services set up by the packaged installers. Also, it allows overriding
settings using [command-line
parameters](../../developer/reference/cli.html#reference-cmdline) without
needing to edit a configuration file.

Finally, it provides greater control over the system’s setup and allows to
more easily keep (and run) multiple versions of Odoo side-by-side.

## Fetch the sources

There are two ways to obtain the source code of Odoo: as a ZIP **archive** or
through **Git**.

### Archive

Community edition:

  * [Odoo download page](https://www.odoo.com/page/download)

  * [GitHub Community repository](https://github.com/odoo/odoo)

  * [Nightly server](https://nightly.odoo.com)

Enterprise edition:

  * [Odoo download page](https://www.odoo.com/page/download)

  * [GitHub Enterprise repository](https://github.com/odoo/enterprise)

### Git

Note

It is required to have [Git](https://git-scm.com/) installed, and it is
recommended to have a basic knowledge of Git commands to proceed.

To clone a Git repository, choose between cloning with HTTPS or SSH. In most
cases, the best option is HTTPS. However, choose SSH to contribute to Odoo
source code or when following the [Getting Started developer
tutorial](../../developer/tutorials/getting_started.html).

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
    

Note

**The Enterprise git repository does not contain the full Odoo source code**.
It is only a collection of extra add-ons. The main server code is in the
Community edition. Running the Enterprise version means running the server
from the Community version with the `addons-path` option set to the folder
with the Enterprise edition. It is required to clone both the Community and
Enterprise repositories to have a working Odoo Enterprise installation.

## Prepare

### Python

Odoo requires **Python 3.7** or later to run.

LinuxWindowsMac OS

Use a package manager to download and install Python 3 if needed.

[Download the latest version of Python
3](https://www.python.org/downloads/windows/) and install it.

During installation, check **Add Python 3 to PATH** , then click **Customize
Installation** and make sure that **pip** is checked.

Use a package manager ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)) to download and install Python 3 if
needed.

Note

If Python 3 is already installed, make sure that the version is 3.7 or above,
as previous versions are not compatible with Odoo.

LinuxWindowsMac OS

    
    
    $ python3 --version
    
    
    
    C:\> python --version
    
    
    
    $ python3 --version
    

Verify that [pip](https://pip.pypa.io) is also installed for this version.

LinuxWindowsMac OS

    
    
    $ pip3 --version
    
    
    
    C:\> pip --version
    
    
    
    $ pip3 --version
    

### PostgreSQL

Odoo uses PostgreSQL as its database management system.

LinuxWindowsMac OS

Use a package manager to download and install PostgreSQL (supported versions:
12.0 or above). It can be achieved by executing the following:

    
    
    $ sudo apt install postgresql postgresql-client
    

[Download PostgreSQL](https://www.postgresql.org/download/windows) (supported
versions: 12.0 or above) and install it.

Use [Postgres.app](https://postgresapp.com) to download and install PostgreSQL
(supported version: 12.0 or above).

Tip

To make the command line tools bundled with Postgres.app available, make sure
to set up the `$PATH` variable by following the [Postgres.app CLI tools
instructions](https://postgresapp.com/documentation/cli-tools.html).

By default, the only user is `postgres`. As Odoo forbids connecting as
`postgres`, create a new PostgreSQL user.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

Note

Because the PostgreSQL user has the same name as the Unix login, it is
possible to connect to the database without a password.

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
    

Note

Because the PostgreSQL user has the same name as the Unix login, it is
possible to connect to the database without a password.

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

Warning

Using pip may lead to security issues and broken dependencies; only do this if
you know what you are doing.

As some of the Python packages need a compilation step, they require system
libraries to be installed.

On Debian/Ubuntu, the following command should install these required
libraries:

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Odoo dependencies are listed in the `requirements.txt` file located at the
root of the Odoo Community directory.

Note

The Python packages in `requirements.txt` are based on their stable/LTS
Debian/Ubuntu corresponding version at the moment of the Odoo release. For
example, for Odoo 15.0, the `python3-babel` package version is 2.8.0 in Debian
Bullseye and 2.6.0 in Ubuntu Focal. The lowest version is then chosen in the
`requirements.txt`.

Tip

It can be preferable not to mix Python module packages between different
instances of Odoo or with the system. However, it is possible to use
[virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python
environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and
run **pip** on the requirements file to install the requirements for the
current user.

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Before installing the dependencies, download and install the [Build Tools for
Visual Studio](https://visualstudio.microsoft.com/downloads/). Select **C++
build tools** in the **Workloads** tab and install them when prompted.

Odoo dependencies are listed in the `requirements.txt` file located at the
root of the Odoo Community directory.

> Tip
>
> It can be preferable not to mix Python module packages between different
> instances of Odoo or with the system. However, it is possible to use
> [virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python
> environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and
run **pip** on the requirements file in a terminal **with Administrator
privileges** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Odoo dependencies are listed in the `requirements.txt` file located at the
root of the Odoo Community directory.

> Tip
>
> It can be preferable not to mix Python module packages between different
> instances of Odoo or with the system. However, it is possible to use
> [virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python
> environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and
run **pip** on the requirements file:

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

Warning

Non-Python dependencies must be installed with a package manager
([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).

  1. Download and install the **Command Line Tools** :
    
        $ xcode-select --install
    

  2. Use the package manager to install non-Python dependencies.

Note

For languages using a **right-to-left interface** (such as Arabic or Hebrew),
the `rtlcss` package is required.

LinuxWindowsMac OS

  1. Download and install **nodejs** and **npm** with a package manager.

  2. Install `rtlcss`:
    
        $ sudo npm install -g rtlcss
    

  1. Download and install [nodejs](https://nodejs.org/en/download).

  2. Install `rtlcss`:
    
        C:\> npm install -g rtlcss
    

  3. Edit the system environment’s variable `PATH` to add the folder where `rtlcss.cmd` is located (typically: `C:\Users\<user>\AppData\Roaming\npm\`).

  1. Download and install **nodejs** with a package manager ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).

  2. Install `rtlcss`:
    
        $ sudo npm install -g rtlcss
    

Warning

`wkhtmltopdf` is not installed through **pip** and must be installed manually
in [version
0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) for
it to support headers and footers. Check out the [wkhtmltopdf
wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) for more details on the
various versions.

## Running Odoo

Once all dependencies are set up, Odoo can be launched by running `odoo-bin`,
the command-line interface of the server. It is located at the root of the
Odoo Community directory.

To configure the server, either specify [command-line
arguments](../../developer/reference/cli.html#reference-cmdline-server) or a
[configuration file](../../developer/reference/cli.html#reference-cmdline-
config).

Tip

For the Enterprise edition, add the path to the `enterprise` add-ons to the
`addons-path` argument. Note that it must come before the other paths in
`addons-path` for add-ons to be loaded correctly.

Common necessary configurations are:

  * PostgreSQL user and password.

  * Custom addon paths beyond the defaults to load custom modules.

A typical way to run the server would be:

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Odoo Community installation, and
`mydb` is the name of the PostgreSQL database.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Odoo Community installation, `dbuser`
is the PostgreSQL login, `dbpassword` is the PostgreSQL password, and `mydb`
is the name of the PostgreSQL database.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Where `CommunityPath` is the path of the Odoo Community installation, and
`mydb` is the name of the PostgreSQL database.

After the server has started (the INFO log `odoo.modules.loading: Modules
loaded.` is printed), open <http://localhost:8069> in a web browser and log
into the Odoo database with the base administrator account: use `admin` as the
email and, again, `admin` as the password.

Tip

  * From there, create and manage new [users](../../applications/general/users.html).

  * The user account used to log into Odoo’s web interface differs from the [`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r) CLI argument.

See also

[The list of CLI arguments for odoo-bin](../../developer/reference/cli.html)

