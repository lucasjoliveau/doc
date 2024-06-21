# Paquete de instaladores

Konvergo ERP cuenta con instalaciones en paquete para distribuciones Linux basadas en
Debian (Debian, Ubuntu, etc.), distribuciones Linux basadas en RPM (Fedora,
CentOS, RHEL, etc.) y Windows en la edición Community y Enterprise.

Los paquetes de compilación nocturna de Konvergo ERP **Community** están disponibles
en el [servidor nocturno](https://nightly.odoo.com) con todos los requisitos
de dependencias necesarios.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Es posible que sea complicado mantener los paquetes nocturnos al día.</p>
</div>

Los paquetes oficiales de **Community** y **Enterprise** se pueden descargar
desde [la página de descargas de Konvergo ERP](https://www.odoo.com/page/download).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para descargar los paquetes de Enterprise es necesario que haya iniciado sesión como un cliente que paga Konvergo ERP de forma local o un partner.</p>
</div>

## Linux

### Preparar

Konvergo ERP necesita un servidor [PostgreSQL](https://www.postgresql.org/) para
ejecutarse bien.

Debian/UbuntuFedora

La configuración predeterminada para el paquete “deb” de Konvergo ERP es para usar el
servidor PostgreSQL en el mismo huésped que la instancia de Konvergo ERP. Ejecute el
siguiente comando para instalar el servidor PostgreSQL:

    
    
    $ sudo apt install postgresql -y
    

Asegúrese de que el comando `sudo` esté disponible y bien configurado y, solo
entonces, ejecute el siguiente comando para poder instalar el servidor
PostgreSQL:

    
    
    $ sudo dnf install -y postgresql-server
    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p><code>wkhtmltopdf</code> no está instalado mediante <b>pip</b> y debe instalarse de forma manual en la <a href="https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3">versión 0.12.6</a> para que sea compatible con los encabezados y pies de páginas. Consulte esta <a href="https://github.com/odoo/odoo/wiki/Wkhtmltopdf">wiki</a> para obtener más detalles sobre las diferentes versiones.</p>
</div>

### Repositorio

Konvergo ERP S.A. cuenta con un repositorio que se puede usar para instalar la edición
**Community** si ejecuta los siguientes comandos:

Debian/UbuntuFedora

    
    
    $ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
    $ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/16.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
    $ sudo apt-get update && sudo apt-get install odoo
    

Utilice el comando usual `apt-get upgrade` para mantener su instalación
actualizada.

    
    
    $ sudo dnf config-manager --add-repo=https://nightly.odoo.com/16.0/nightly/rpm/odoo.repo
    $ sudo dnf install -y odoo
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En este momento, no hay un repositorio nocturno para la edición Enterprise.</p>
</div>

### Paquete de distribución

Los paquetes oficiales de **Community** y **Enterprise** se pueden descargar
desde [la página de descargas de Konvergo ERP](https://www.odoo.com/page/download).

Debian/UbuntuFedora

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El paquete “deb” de Konvergo ERP 16 es compatible con <a href="https://www.debian.org/releases/buster/">Debian Buster</a>  y <a href="https://releases.ubuntu.com/18.04">Ubuntu 18.04</a> o versiones mayores.</p>
</div>

Ya que lo haya descargado, ejecute los siguientes comandos **como root** para
instalar Konvergo ERP como un servicio, cree el usuario PostgreSQL necesario e inicie
el servidor de manera automática.

    
    
    # dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
    # apt-get install -f # should install the missing dependencies
    # dpkg -i <path_to_installation_package>
    

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><ul>
<li><p>El paquete <code>python3-xlwt</code> Debian, que se necesita para exportarlo en el formato XLS, no existe en Debian Buster ni en Ubuntu 18.04. Si lo necesita, instálelo de manera manual con esto:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install xlwt
</pre></div>
</div>
</li>
<li><p>El paquete Python <code>num2words</code>  es necesario para renderizar cantidades textuales, sin embargo, no existe en Debian Buster ni en Ubuntu 18.04, lo cual puede causar problemas con el módulo <code>l10n_mx_edi</code>. Si lo necesita, instálelo de manera manual con esto:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install num2words
</pre></div>
</div>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El paquete “rpm” de Konvergo ERP 16 es compatible con Fedora 36.</p>
</div>

Una vez que lo descargue, el paquete utilizará el gestor de paquete “dnf” para
instalarse:

    
    
    $ sudo dnf localinstall odoo_16.0.latest.noarch.rpm
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

## Windows

> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El paquete de Windows está disponible para propósitos de prueba o para utilizarse en instancias de un solo usuario local, pero no se le recomienda su uso para el despliegue de producción puesto que existen varias limitaciones y riesgos asociados con el despliegue de Konvergo ERP en una plataforma de Windows.</p>
</div>

  1. Descargue el instalador desde el [servidor nocturno](https://nightly.odoo.com) (Solo Community) o el instalador de Windows dese [la página de descargas de Konvergo ERP](https://www.odoo.com/page/download) (cualquier edición).

  2. Ejecutar el archivo descargado.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>En Windows 8 y versiones posteriores, es posible que se muestre una advertencia que dice <em>Windows protegió su pc</em>. Haga clic en <b>más información</b> y luego en <b>ejecutar de todas formas</b> para seguir.</p>
</div>

  3. Acepte lo que diga sobre el [control de cuentas de usuario](https://es.wikipedia.org/wiki/Control_de_cuentas_de_usuario).

  4. Siga los pasos de instalación.

Konvergo ERP se ejecutará en automático al terminar la instalación.

