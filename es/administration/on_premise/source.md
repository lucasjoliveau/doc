# Instalación desde la fuente

La “instalación” de origen no se trata de instalar Konvergo ERP, sino de ejecutarlo
directamente desde el origen.

Es posible que para desarrolladores de módulo sea más conveniente usar el
origen de Konvergo ERP que usar las instalaciones en paquete.

También hace que el iniciar y detener Konvergo ERP sea más flexible y explícito que
los servicios que las instalaciones en paquete configuraron. También permite
sobreescribir los ajustes usando [parámetros de líneas de
comando](../../developer/reference/cli#reference-cmdline) sin tener que
editar el archivo de configuración.

Finalmente, permite tener más control sobre la configuración del sistema y
hace que sea más fácil mantener (y ejecutar) varias versiones de Konvergo ERP al mismo
tiempo.

## Extraer los recursos

Puede obtener el código fuente de Konvergo ERP desde un **archivo** zip o **Git**.

### Archivar

Edición Community:

  * [Página de descarga de Konvergo ERP](https://www.odoo.com/page/download)

  * [Repositorio de la comunidad de GitHub](https://github.com/odoo/odoo)

  * [Servidor nocturno](https://nightly.odoo.com)

Edición Enterprise:

  * [Página de descarga de Konvergo ERP](https://www.odoo.com/page/download)

  * [repositorio Enterprise de GitHub](https://github.com/odoo/enterprise)

### Git

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Es necesario tener <a href="https://git-scm.com/">Git</a> instalado, y se recomienda tener un conocimiento básico de comandos Git para continuar.</p>
</div>

Para clonar un repositorio de Git, elija entre clonar con HTTPS o SSH. En la
mayoría de los casos la mejor opción es HTTPS, pero puede elegir SSH si desea
contribuir al código fuente de Konvergo ERP o cuando siga el [tutorial de inicio para
desarrolladores](../../developer/tutorials/getting_started).

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
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>

## Preparar

### Python

Konvergo ERP necesita **Python 3.7** o posterior para funcionar.

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

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si Python 3 ya está instalado, asegúrese de que sea la versión 3.7 o más, ya que las versiones previas no son compatibles con Konvergo ERP.</p>
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
<p>También verifique que <a href="https://pip.pypa.io">pip</a> esté instalado para esta versión.</p>
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

Konvergo ERP utiliza PostgreSQL como sistema de gestión de bases de datos.

LinuxWindowsMac OS

Utilice un administrador de paquetes para descargar e instalar PostgreSQL
(versiones compatibles: 12.0 o superior). Puede conseguirlo si ejecuta lo
siguiente:

    
    
    $ sudo apt install postgresql postgresql-client
    

[Descargue PostgreSQL](https://www.postgresql.org/download/windows) (versiones
compatibles: 12.0 o superior) e instálelo.

Utilice [Postgres.app](https://postgresapp.com) para descargar e instalar
PostgreSQL (versión compatible: 12.0 o superior).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para que los comandos de línea se junten cuando <code>postgres.app</code> está disponible, asegúrese de configurar la variable <code>$PATH</code>. Para esto, siga las indicaciones que encontrará en este enlace <a href="https://postgresapp.com/documentation/cli-tools">Postgres.app CLI Tools Instructions</a>.</p>
</div>

De forma predeterminada, el único usuario es `postgres`. Como Konvergo ERP prohíbe
conectarse como `postgres`, debe crear un nuevo usuario PostgreSQL.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Ya que el usuario de PostgreSQL tiene el mismo nombre que el inicio de sesión de Unix, podrá conectarse a la base de datos sin una contraseña.</p>
</div>

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
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Ya que el usuario de PostgreSQL tiene el mismo nombre que el inicio de sesión de Unix, podrá conectarse a la base de datos sin una contraseña.</p>
</div>

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

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Using pip may lead to security issues and broken dependencies; only do this if you
know what you are doing.</p>
</div>

Como algunos de los paquetes de Python necesitan un paso de compilación, es
necesario instalar las bibliotecas del sistema.

En Debian/Ubuntu, este comando debería de instalar todas las bibliotecas
necesarias:

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Las dependencias de Konvergo ERP están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los paquetes Python en <code>requirements.txt</code> se basan en su versión estable/LTS Debian/Ubuntu correspondiente en el momento del lanzamiento de Konvergo ERP. Por ejemplo, para Konvergo ERP 15.0, la versión del paquete <code>python3-babel</code> es 2.8.0 en Debian Bullseye y 2.6.0 en Ubuntu Focal. La versión más baja se elige en el archivo <code>requirements.txt</code>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede ser mejor no mezclar los paquetes de módulos python entre diferentes instancias de Konvergo ERP o con su sistema. Puede usar <a href="https://pypi.org/project/virtualenv/">virtualenv</a> para crear entornos Python aislados.</p>
</div>

Navegue a la ruta de su instalación de Konvergo ERP Community (`CommunityPath`) y
ejecute **pip** en el archivo de requerimientos para instalar los
requerimientos para el usuario actual

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Antes de instalar las dependencias, debe descargar e instalar [Herramientas de
creación para Visual Studio](https://visualstudio.microsoft.com/downloads/).
Cuando se lo pida, seleccione **herramientas de creación C++** en la pestaña
de **Carga de trabajo** e instálelo.

Las dependencias de Konvergo ERP están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Konvergo ERP.

> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede ser mejor no mezclar los paquetes de módulos python entre diferentes instancias de Konvergo ERP o con su sistema. Puede usar <a href="https://pypi.org/project/virtualenv/">virtualenv</a> para crear entornos Python aislados.</p>
</div>

Navegue a la ruta de su instalación de Konvergo ERP Community (`CommunityPath`) y
ejecute **pip** en el campo de requisitos en una terminal **con privilegios de
administrador** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Las dependencias de Konvergo ERP están enlistadas en el archivo `requirements.txt` que
se encuentra en el directorio raíz de la versión Community de Konvergo ERP.

> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>0

Vaya a la ruta de su instalación de Konvergo ERP Community (`CommunityPath`) y ejecute
**pip** en el archivo de requisitos:

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>1

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>3

## Ejecutar Konvergo ERP

Una vez que termine de configurar todas las dependencias podrá ejecutar Konvergo ERP
con la interfaz de la línea de comando del servidor, `odoo-bin` . La puede
encontrar en la raíz del directorio de Konvergo ERP Community.

Para configurar el servidor puede especificar [argumentos de las líneas de
comando](../../developer/reference/cli#reference-cmdline-server) o un
[archivo de configuración](../../developer/reference/cli#reference-
cmdline-config).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>4

Estas son las configuraciones necesarias más comunes:

  * Usuario y contraseña de PostgreSQL

  * Rutas personalizadas para complementos adicionales que sirvan para cargar los módulos personalizados.

La forma normal de ejecutar el servidor es:

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Konvergo ERP Community y `mydb`
es la base de datos de PostgreSQL.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Konvergo ERP Community, `dbuser`
es el inicio de sesión de PostgreSQL, `dbpassword` es la contraseña de
PostgreSQL y `mydb` es la base de datos de PostgreSQL.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Donde `CommunityPath` es la ruta de la instalación de Konvergo ERP Community y `mydb`
es la base de datos de PostgreSQL.

Después de que el servidor se haya iniciado (se imprime el registro INFO
`odoo.modules.loading: módulos cargados.`), abra <http://localhost:8069> en un
navegador web e inicie sesión en la base de datos de Konvergo ERP con la cuenta de
administrador base: utilice `admin` como correo electrónico y, de nuevo,
`admin` como contraseña.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>El repositorio git de Enterprise no contiene el código fuente de Konvergo ERP completo</b>, solo es una colección de complementos. El servidor principal está en la versión de Comunidad. Cuando ejecutamos la versión Enterprise quiere decir que estamos ejecutando el servidor de la versión Community con la opción <code>addons-path</code> configurada en el folder que contiene la versión Enterprise. Debe clonar tanto el repositorio de Community como de Enterprise para que la instalación de Konvergo ERP Enterprise funcione.</p>
</div>6

