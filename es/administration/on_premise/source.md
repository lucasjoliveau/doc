# Instalación desde la fuente

La “instalación” de origen no se trata de instalar Odoo, sino de ejecutarlo
directamente desde el origen.

Es posible que para desarrolladores de módulo sea más conveniente usar el
origen de Odoo que usar las instalaciones en paquete.

También hace que el iniciar y detener Odoo sea más flexible y explícito que
los servicios que las instalaciones en paquete configuraron. También permite
sobreescribir los ajustes usando [parámetros de líneas de
comando](../../developer/reference/cli.html#reference-cmdline) sin tener que
editar el archivo de configuración.

Finalmente, permite tener más control sobre la configuración del sistema y
hace que sea más fácil mantener (y ejecutar) varias versiones de Odoo al mismo
tiempo.

## Extraer los recursos

Puede obtener el código fuente de Odoo desde un **archivo** zip o **Git**.

### Archivar

Edición Community:

  * [Página de descarga de Odoo](https://www.odoo.com/page/download)

  * [Repositorio de la comunidad de GitHub](https://github.com/odoo/odoo)

  * [Servidor nocturno](https://nightly.odoo.com)

Edición Enterprise:

  * [Página de descarga de Odoo](https://www.odoo.com/page/download)

  * [repositorio Enterprise de GitHub](https://github.com/odoo/enterprise)

### Git

Nota

Es necesario tener [Git](https://git-scm.com/) instalado, y se recomienda
tener un conocimiento básico de comandos Git para continuar.

Para clonar un repositorio de Git, elija entre clonar con HTTPS o SSH. En la
mayoría de los casos la mejor opción es HTTPS, pero puede elegir SSH si desea
contribuir al código fuente de Odoo o cuando siga el [tutorial de inicio para
desarrolladores](../../developer/tutorials/getting_started.html).

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
    

Nota

**El repositorio git de Enterprise no contiene el código fuente de Odoo
completo** , solo es una colección de complementos. El servidor principal está
en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere
decir que estamos ejecutando el servidor de la versión Community con la opción
`addons-path` configurada en el folder que contiene la versión Enterprise.
Debe clonar tanto el repositorio de Community como de Enterprise para que la
instalación de Odoo Enterprise funcione.

## Preparar

### Python

Odoo necesita **Python 3.7** o posterior para funcionar.

LinuxWindowsMac OS

Utilice un administrador de paquetes para descargar e instalar Python 3 si es
necesario.

[Descargue la última versión de Python
3](https://www.python.org/downloads/windows/) e instálela.

Durante la instalación, marque **Agregue Python 3 a la RUTA** , después haga
clic en **Personalización de la instalación** y asegúrese de que **pip** esté
revisado.

Utilice un administrador de paquetes ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)) para descargar e instalar Python 3 si es
necesario.

Nota

Si Python 3 ya está instalado, asegúrese de que sea la versión 3.7 o más, ya
que las versiones previas no son compatibles con Odoo.

LinuxWindowsMac OS

    
    
    $ python3 --version
    
    
    
    C:\> python --version
    
    
    
    $ python3 --version
    

También verifique que [pip](https://pip.pypa.io) esté instalado para esta
versión.

LinuxWindowsMac OS

    
    
    $ pip3 --version
    
    
    
    C:\> pip --version
    
    
    
    $ pip3 --version
    

### PostgreSQL

Odoo utiliza PostgreSQL como sistema de gestión de bases de datos.

LinuxWindowsMac OS

Utilice un administrador de paquetes para descargar e instalar PostgreSQL
(versiones compatibles: 12.0 o superior). Puede conseguirlo si ejecuta lo
siguiente:

    
    
    $ sudo apt install postgresql postgresql-client
    

[Descargue PostgreSQL](https://www.postgresql.org/download/windows) (versiones
compatibles: 12.0 o superior) e instálelo.

Utilice [Postgres.app](https://postgresapp.com) para descargar e instalar
PostgreSQL (versión compatible: 12.0 o superior).

Truco

Para que los comandos de línea se junten cuando `postgres.app` está
disponible, asegúrese de configurar la variable `$PATH`. Para esto, siga las
indicaciones que encontrará en este enlace [Postgres.app CLI Tools
Instructions](https://postgresapp.com/documentation/cli-tools.html).

De forma predeterminada, el único usuario es `postgres`. Como Odoo prohíbe
conectarse como `postgres`, debe crear un nuevo usuario PostgreSQL.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

Nota

Ya que el usuario de PostgreSQL tiene el mismo nombre que el inicio de sesión
de Unix, podrá conectarse a la base de datos sin una contraseña.

  1. Agregue el directorio `papelera` de PostgreSQL (de manera predeterminado: `C:\Program Files\PostgreSQL\<version>\bin`) a su `RUTA`.

  2. Use la guía pg admin para crear un usuario postgres con contraseña:

    1. Abrir **pgAdmin**.

    2. Haga doble clic en el servidor para crear una conexión.

    3. Seleccione Objeto ‣ Crear ‣ Rol de Inicio de sesión/Grupo.

    4. Ingrese el nombre de usuario en el campo de **Nombre de la función** (por ejemplo, `odoo`)

    5. Abra la pestaña **Definición** e ingrese la contraseña (por ejemplo, `odoo`) y después haga clic en **Guardar**.

    6. Abra la pestaña de **Privilegios** y cambie **¿Puede iniciar sesión?** a `Sí` y **¿Crear una base de datos?** a `Sí`.

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

Nota

Ya que el usuario de PostgreSQL tiene el mismo nombre que el inicio de sesión
de Unix, podrá conectarse a la base de datos sin una contraseña.

### Dependencias

LinuxWindowsMac OS

La manera preferida de instalar dependencias es por medio de **paquetes de
distribución**. También puede instalar dependencias Python con **pip**.

Debian/UbuntuInstall with pip

En Debian/Ubunto, los siguientes comandos instalarán los paquetes requeridos:

    
    
    $ cd odoo #CommunityPath
    $ sudo ./setup/debinstall.sh
    

The `setup/debinstall.sh` script will parse the
[debian/control](https://github.com/odoo/odoo/blob/16.0/debian/control) file
and install the found packages.

Advertencia

Using pip may lead to security issues and broken dependencies; only do this if
you know what you are doing.

Como algunos de los paquetes de Python necesitan un paso de compilación, es
necesario instalar las bibliotecas del sistema.

En Debian/Ubuntu, este comando debería de instalar todas las bibliotecas
necesarias:

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Las dependencias de Odoo están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Odoo.

Nota

Los paquetes Python en `requirements.txt` se basan en su versión estable/LTS
Debian/Ubuntu correspondiente en el momento del lanzamiento de Odoo. Por
ejemplo, para Odoo 15.0, la versión del paquete `python3-babel` es 2.8.0 en
Debian Bullseye y 2.6.0 en Ubuntu Focal. La versión más baja se elige en el
archivo `requirements.txt`.

Truco

Puede ser mejor no mezclar los paquetes de módulos python entre diferentes
instancias de Odoo o con su sistema. Puede usar
[virtualenv](https://pypi.org/project/virtualenv/) para crear entornos Python
aislados.

Navegue a la ruta de su instalación de Odoo Community (`CommunityPath`) y
ejecute **pip** en el archivo de requerimientos para instalar los
requerimientos para el usuario actual

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Antes de instalar las dependencias, debe descargar e instalar [Herramientas de
creación para Visual Studio](https://visualstudio.microsoft.com/downloads/).
Cuando se lo pida, seleccione **herramientas de creación C++** en la pestaña
de **Carga de trabajo** e instálelo.

Las dependencias de Odoo están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Odoo.

> Truco
>
> Puede ser mejor no mezclar los paquetes de módulos python entre diferentes
> instancias de Odoo o con su sistema. Puede usar
> [virtualenv](https://pypi.org/project/virtualenv/) para crear entornos
> Python aislados.

Navegue a la ruta de su instalación de Odoo Community (`CommunityPath`) y
ejecute **pip** en el campo de requisitos en una terminal **con privilegios de
administrador** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Las dependencias de Odoo están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Odoo.

> Truco
>
> Puede ser mejor no mezclar los paquetes de módulos python entre diferentes
> instancias de Odoo o con su sistema. Puede usar
> [virtualenv](https://pypi.org/project/virtualenv/) para crear entornos
> Python aislados.

Vaya a la ruta de su instalación de Odoo Community (`CommunityPath`) y ejecute
**pip** en el archivo de requisitos:

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

Advertencia

Las dependencias que no sean de Python deben instalarse con un administrador
de paquetes ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)).

  1. Descargue e instale las **Herramientas de líneas de comando** :
    
        $ xcode-select --install
    

  2. Use el administrador de paquetes para instalar dependencias que no sean de Python.

Nota

Para idiomas que funcionan con una interfaz de **izquierda a derecha** (como
las interfaces de árabe y hebreo) se necesita el paquete `rtlcss`:

LinuxWindowsMac OS

  1. Descargue e instale **nodejs** y **npm** con su administrador de paquetes.

  2. Instale `rtlcss`:
    
        $ sudo npm install -g rtlcss
    

  1. Descargue e instale [nodejs](https://nodejs.org/en/download)

  2. Instale `rtlcss`:
    
        C:\> npm install -g rtlcss
    

  3. Edite la variable del entorno del sistema `PATH` para agregar una carpeta donde se encuentre `rtlcss.cmd` (usualmente: file:`C:\Users\<user>\AppData\Roaming\npm\`).

  1. Descargue e instale **nodejs** con un administrador de paquetes ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).

  2. Instale `rtlcss`:
    
        $ sudo npm install -g rtlcss
    

Advertencia

`wkhtmltopdf` no está instalado mediante **pip** y debe instalarse de forma
manual en la [versión
0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) para
que sea compatible con los encabezados y pies de páginas. Consulte esta
[wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) para obtener más
detalles sobre las diferentes versiones.

## Ejecutar Odoo

Una vez que termine de configurar todas las dependencias podrá ejecutar Odoo
con la interfaz de la línea de comando del servidor, `odoo-bin` . La puede
encontrar en la raíz del directorio de Odoo Community.

Para configurar el servidor puede especificar [argumentos de las líneas de
comando](../../developer/reference/cli.html#reference-cmdline-server) o un
[archivo de configuración](../../developer/reference/cli.html#reference-
cmdline-config).

Truco

Para la edición Enterprise, es necesario agregar la ruta de los complementos
de `enterprise` al argumento `addons-path`. Tenga en cuenta que debe ir antes
que otras rutas en `addons-path` para que los complementos se carguen
correctamente.

Estas son las configuraciones necesarias más comunes:

  * Usuario y contraseña de PostgreSQL

  * Rutas personalizadas para complementos adicionales que sirvan para cargar los módulos personalizados.

La forma normal de ejecutar el servidor es:

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Odoo Community y `mydb`
es la base de datos de PostgreSQL.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Odoo Community, `dbuser`
es el inicio de sesión de PostgreSQL, `dbpassword` es la contraseña de
PostgreSQL y `mydb` es la base de datos de PostgreSQL.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Odoo Community y `mydb`
es la base de datos de PostgreSQL.

Después de que el servidor se haya iniciado (se imprime el registro INFO
`odoo.modules.loading: módulos cargados.`), abra <http://localhost:8069> en un
navegador web e inicie sesión en la base de datos de Odoo con la cuenta de
administrador base: utilice `admin` como correo electrónico y, de nuevo,
`admin` como contraseña.

Truco

  * Ahí podrá crear y gestionar nuevos [usuarios](../../applications/general/users.html).

  * La cuenta de usuario que usa para iniciar sesión en la interfaz del sitio web de Odoo es diferente al argumento CLI [`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r).

Ver también

[La lista de argumentos CLI para odoo-
bin](../../developer/reference/cli.html).

