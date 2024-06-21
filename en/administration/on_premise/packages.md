# Packaged installers

Konvergo ERP provides packaged installers for Debian-based Linux distributions
(Debian, Ubuntu, etc.), RPM-based Linux distributions (Fedora, CentOS, RHEL,
etc.), and Windows for the Community and Enterprise editions.

Official **Community** nightly packages with all relevant dependency
requirements are available on the [nightly server](https://nightly.odoo.com).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Nightly packages may be difficult to keep up to date.</p>
</div>

Official **Community** and **Enterprise** packages can be downloaded from the
[Konvergo ERP download page](https://www.odoo.com/page/download).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is required to be logged in as a paying on-premise customer or partner to download the
Enterprise packages.</p>
</div>

## Linux

### Prepare

Konvergo ERP needs a [PostgreSQL](https://www.postgresql.org/) server to run properly.

Debian/UbuntuFedora

The default configuration for the Konvergo ERP ‘deb’ package is to use the PostgreSQL
server on the same host as the Konvergo ERP instance. Execute the following command to
install the PostgreSQL server:

    
    
    $ sudo apt install postgresql -y
    

Make sure that the `sudo` command is available and well configured and, only
then, execute the following command to install the PostgreSQL server:

    
    
    $ sudo dnf install -y postgresql-server
    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p><code>wkhtmltopdf</code> is not installed through <b>pip</b> and must be installed manually in <a href="https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3">version 0.12.6</a> for it to support headers
and footers. Check out the <a href="https://github.com/odoo/odoo/wiki/Wkhtmltopdf">wkhtmltopdf wiki</a>
for more details on the various versions.</p>
</div>

### Repository

Konvergo ERP S.A. provides a repository that can be used to install the **Community**
edition by executing the following commands:

Debian/UbuntuFedora

    
    
    $ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
    $ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/16.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
    $ sudo apt-get update && sudo apt-get install odoo
    

Use the usual `apt-get upgrade` command to keep the installation up-to-date.

    
    
    $ sudo dnf config-manager --add-repo=https://nightly.odoo.com/16.0/nightly/rpm/odoo.repo
    $ sudo dnf install -y odoo
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Currently, there is no nightly repository for the Enterprise edition.</p>
</div>

### Distribution package

Instead of using the repository, packages for both the **Community** and
**Enterprise** editions can be downloaded from the [Konvergo ERP download
page](https://www.odoo.com/page/download).

Debian/UbuntuFedora

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP 16 ‘deb’ package currently supports <a href="https://www.debian.org/releases/buster/">Debian Buster</a> and <a href="https://releases.ubuntu.com/18.04">Ubuntu 18.04</a> or above.</p>
</div>

Once downloaded, execute the following commands **as root** to install Konvergo ERP as
a service, create the necessary PostgreSQL user, and automatically start the
server:

    
    
    # dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
    # apt-get install -f # should install the missing dependencies
    # dpkg -i <path_to_installation_package>
    

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><ul>
<li><p>The <code>python3-xlwt</code> Debian package, needed to export into the XLS format, does not exist
in Debian Buster nor Ubuntu 18.04. If needed, install it manually with the following:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install xlwt
</pre></div>
</div>
</li>
<li><p>The <code>num2words</code> Python package - needed to render textual amounts - does not exist in
Debian Buster nor Ubuntu 18.04, which could cause problems with the <code>l10n_mx_edi</code> module.
If needed, install it manually with the following:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install num2words
</pre></div>
</div>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP 16 ‘rpm’ package supports Fedora 36.</p>
</div>

Once downloaded, the package can be installed using the ‘dnf’ package manager:

    
    
    $ sudo dnf localinstall odoo_16.0.latest.noarch.rpm
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

## Windows

> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Windows packaging is offered for the convenience of testing or running single-user local
instances but production deployment is discouraged due to a number of limitations and risks
associated with deploying Konvergo ERP on a Windows platform.</p>
</div>

  1. Download the installer from the [nightly server](https://nightly.odoo.com) (Community only) or the Windows installer from the [Konvergo ERP download page](https://www.odoo.com/page/download) (any edition.

  2. Execute the downloaded file.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>On Windows 8 and later, a warning titled <em>Windows protected your PC</em> may be displayed. Click
<b>More Info</b> and then <b>Run anyway</b> to proceed.</p>
</div>

  3. Accept the [UAC](https://en.wikipedia.org/wiki/User_Account_Control) prompt.

  4. Go through the installation steps.

Konvergo ERP launches automatically at the end of the installation.

