# Paquete de instaladores

Odoo cuenta con instalaciones en paquete para distribuciones Linux basadas en
Debian (Debian, Ubuntu, etc.), distribuciones Linux basadas en RPM (Fedora,
CentOS, RHEL, etc.) y Windows en la edición Community y Enterprise.

Los paquetes de compilación nocturna de Odoo **Community** están disponibles
en el [servidor nocturno](https://nightly.odoo.com) con todos los requisitos
de dependencias necesarios.

Nota

Es posible que sea complicado mantener los paquetes nocturnos al día.

Los paquetes oficiales de **Community** y **Enterprise** se pueden descargar
desde [la página de descargas de Odoo](https://www.odoo.com/page/download).

Nota

Para descargar los paquetes de Enterprise es necesario que haya iniciado
sesión como un cliente que paga Odoo de forma local o un partner.

## Linux

### Preparar

Odoo necesita un servidor [PostgreSQL](https://www.postgresql.org/) para
ejecutarse bien.

Debian/UbuntuFedora

La configuración predeterminada para el paquete “deb” de Odoo es para usar el
servidor PostgreSQL en el mismo huésped que la instancia de Odoo. Ejecute el
siguiente comando para instalar el servidor PostgreSQL:

    
    
    $ sudo apt install postgresql -y
    

Asegúrese de que el comando `sudo` esté disponible y bien configurado y, solo
entonces, ejecute el siguiente comando para poder instalar el servidor
PostgreSQL:

    
    
    $ sudo dnf install -y postgresql-server
    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    

Advertencia

`wkhtmltopdf` no está instalado mediante **pip** y debe instalarse de forma
manual en la [versión
0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) para
que sea compatible con los encabezados y pies de páginas. Consulte esta
[wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) para obtener más
detalles sobre las diferentes versiones.

### Repositorio

Odoo S.A. cuenta con un repositorio que se puede usar para instalar la edición
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
    

Nota

En este momento, no hay un repositorio nocturno para la edición Enterprise.

### Paquete de distribución

Los paquetes oficiales de **Community** y **Enterprise** se pueden descargar
desde [la página de descargas de Odoo](https://www.odoo.com/page/download).

Debian/UbuntuFedora

Nota

El paquete “deb” de Odoo 16 es compatible con [Debian
Buster](https://www.debian.org/releases/buster/) y [Ubuntu
18.04](https://releases.ubuntu.com/18.04) o versiones mayores.

Ya que lo haya descargado, ejecute los siguientes comandos **como root** para
instalar Odoo como un servicio, cree el usuario PostgreSQL necesario e inicie
el servidor de manera automática.

    
    
    # dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
    # apt-get install -f # should install the missing dependencies
    # dpkg -i <path_to_installation_package>
    

Advertencia

  * El paquete `python3-xlwt` Debian, que se necesita para exportarlo en el formato XLS, no existe en Debian Buster ni en Ubuntu 18.04. Si lo necesita, instálelo de manera manual con esto:
    
        $ sudo pip3 install xlwt
    

  * El paquete Python `num2words` es necesario para renderizar cantidades textuales, sin embargo, no existe en Debian Buster ni en Ubuntu 18.04, lo cual puede causar problemas con el módulo `l10n_mx_edi`. Si lo necesita, instálelo de manera manual con esto:
    
        $ sudo pip3 install num2words
    

Nota

El paquete “rpm” de Odoo 16 es compatible con Fedora 36.

Una vez que lo descargue, el paquete utilizará el gestor de paquete “dnf” para
instalarse:

    
    
    $ sudo dnf localinstall odoo_16.0.latest.noarch.rpm
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

## Windows

> Advertencia
>
> El paquete de Windows está disponible para propósitos de prueba o para
> utilizarse en instancias de un solo usuario local, pero no se le recomienda
> su uso para el despliegue de producción puesto que existen varias
> limitaciones y riesgos asociados con el despliegue de Odoo en una plataforma
> de Windows.

  1. Descargue el instalador desde el [servidor nocturno](https://nightly.odoo.com) (Solo Community) o el instalador de Windows dese [la página de descargas de Odoo](https://www.odoo.com/page/download) (cualquier edición).

  2. Ejecutar el archivo descargado.

Advertencia

En Windows 8 y versiones posteriores, es posible que se muestre una
advertencia que dice _Windows protegió su pc_. Haga clic en **más
información** y luego en **ejecutar de todas formas** para seguir.

  3. Acepte lo que diga sobre el [control de cuentas de usuario](https://es.wikipedia.org/wiki/Control_de_cuentas_de_usuario).

  4. Siga los pasos de instalación.

Odoo se ejecutará en automático al terminar la instalación.

