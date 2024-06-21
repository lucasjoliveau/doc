# Actualizar (IoT)

Debido a lo compleja que es la caja IoT y a la caja virtual de Windows IoT, el
término «actualizar» puede significar muchas cosas.

Los drivers se pueden actualizar, el código base de la caja IoT se puede
actualizar, o puede actualizar una imagen (usando una cajal IoT física).

En este documento se exploran varias formas de actualizar las cajas IoT para
asegurar un funcionamiento sin problemas de los procesos y dispositivos de la
caja IoT.

## Actualizar la memoria SD en la caja IoT

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Esta actualización <b>no</b> funciona con la caja <abbr title="Internet de las cosas">IoT</abbr> de Windows (Konvergo ERP 16 o versiones posteriores).</p>
<p>Para actualizar la caja <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> de Windows primero debe desinstalar la versión anterior del software de Konvergo ERP para Windows para después volver a instalarlo usando el paquete de instalación más reciente.</p>
<p>Para iniciar la instalación, vaya al paquete de instalación de Konvergo ERP 16 (o versiones posteriores) de Enterprise o Community - edición Windows, en la <a href="https://odoo.com/download">página de descarga de Konvergo ERP</a>.</p>
</div>

En algunos casos es probable que deba volver a actualizar la tarjeta micro SD
de la caja IoT con el software _Etcher_ para que pueda beneficiarse de la
actualización de imagen de IoT más reciente de Konvergo ERP. Esto significa que el
software de la caja IoT de Konvergo ERP debe actualizarse en caso de que una nueva
caja IoT, una actualización de un control o una actualización desde la página
de inicio de la caja IoT no solucione los problemas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Normalmente es necesario volver a actualizar la imagen de la caja <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> después de actualizar la base de datos de Konvergo ERP a una versión nueva.</p></li>
<li><p><b>Se necesita</b> una computadora con un lector o adaptador de memoria micro SD para actualizar la memoria de la tarjeta micro SD.</p></li>
</ul>
</div>

Primero descargue [Etcher](https://www.balena.io/etcher#download-etcher). Es
un servicio básico gratis de código abierto que se usa para quemar imágenes de
archivos en memorias. Después de que finalice la descarga, instale y ejecute
el programa en la computadora.

Después, descargue la imagen IoT más reciente desde
[nightly](http://nightly.odoo.com/master/iotbox), que podrá reconocer por el
nombre `iotbox-latest.zip`. Esta imagen es compatible con _todas_ las
versiones soportadas de Konvergo ERP.

Una vez completado este paso, inserte la memoria micro SD de la caja IoT en la
computadora o un lector. Abra _Etcher_ y seleccione **Actualizar desde
archivo** , después busque y seleccione la imagen `iotbox-latest.zip` y
extráigala. A continuación, seleccione la unidad en la que desee grabar la
imagen. Por último, haga clic en **Actualizar** y espere a que finalice el
proceso.

Finalmente, haga clic en **Actualizar** y espere a que el proceso finalice.

![Tablero del software Etcher de Balena.](../../../../_images/etcher-app.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El software <em>Etcher</em> de Balena también permite que el administrador actualice la tarjeta <abbr title="Secure Digital">SD</abbr> desde una <abbr title="Localizador Uniforme de Recursos">URL</abbr>. Para actualizarla desde un <abbr title="Uniform Resource Locator">URL</abbr>, simplemente haga clic en <b>Actualizar desde URL</b>, en lugar de <b>Actualizar desde archivo</b>.</p>
<p>Después, ingrese: <code>http://nightly.odoo.com/master/iotbox/iotbox-latest.zip</code>.</p>
<img alt="Una imagen del software Etcher de Balena, con la opción de actualizar desde URL resaltada." class="align-center" src="../../../../_images/url-flash.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Un software alternativo para actualizar la tarjeta micro SD es <a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a>.</p>
</div>

## Actualización de la caja IoT de Windows

Es posible que tenga que actualizar la caja virtual de IoT de Windows de vez
en cuando para que siga funcionando apropiadamente.

El siguiente proceso cubre la desinstalación y la forma de volver a instalar
la caja virtual de IoT de Windows.

### Desinstalar Windows IoT

Antes de actualizar la caja virtual de IoT de Windows, primero debe
desinstalar la versión previa.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Antes de desinstalar la versión prueba de la caja virtual de <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> de Windows asegúrese de que haya una nueva versión nueva de la caja virtual de <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> de Windows disponible. Para hacerlo vaya a la página <a href="https://nightly.odoo.com/">servidor nocturno de Konvergo ERP</a>.</p>
<p>En la página <b>Servidor nocturno de Konvergo ERP</b> vaya a Builds (versión estable) ‣ windows/ para ver la fecha para el siguiente archivo <code>odoo_(versión).latest.exe</code>, donde <em>(versión)</em> es igual a la versión de Konvergo ERP (por ejemplo, 16.0, 17.0). La versión más reciente de la caja virtual de <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> de Windows se puede descargar si hace clic en este archivo, o siempre estará disponible en la página <a href="https://odoo.com/download/">Descargar Konvergo ERP</a></p>
</div>

Desinstalar la caja virtual de IoT de Windows se hace a través del
Administrador de programas.

Busque `programa` en cualquier versión de Windows para abrir la sección
Programas ‣ Programas y funciones del **panel de control**. Después,
seleccione **Desinstalar o cambiar un programa**. Después, busque `Konvergo ERP` y
haga clic en el menú **… (tres puntos)** del programa **Konvergo ERP.exe** para
desinstalarlo.

Confirme la desinstalación y siga los pasos del asistente de desinstalación de
Konvergo ERP.

### Descargar y volver a instalar

La versión más reciente de la caja virtual de IoT de Windows se puede
descargar en la página [del servidor nocturno de
Konvergo ERP](https://nightly.odoo.com/) o siempre está disponible en la página
[Descargar Konvergo ERP](https://odoo.com/download/).

Para descargar desde la página **servidor nocturno de Konvergo ERP** vaya a Builds
(versión estable) ‣ windows/ y seleccione el archivo
`odoo_(versión).latest.exe`; donde _(versión)_ es igual a la versión de Konvergo ERP
(por ejemplo, 16.0, 17.0).

Para descargar desde la página de **Descargar Konvergo ERP** vaya a la sección para su
versión de Konvergo ERP (por ejemplo, 16.0, 17.0) y seleccione el botón **Descargar**
para **Windows**.

Después, instale y configure el archivo `.exe` que descargó de Konvergo ERP. Después
de la pantalla de instrucciones, haga clic en **Siguiente** para iniciar la
instalación y acepte los **Términos de servicio**.

Durante el siguiente paso de el proceso de volver a instalar, seleccione
**Konvergo ERP IoT** en el menú desplegable **Seleccione el tipo de instalación**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Como referencia, debe instalar lo siguiente:</p>
<ul>
<li><p><b>Servidor de Konvergo ERP</b></p></li>
<li><p><b>IoT de Konvergo ERP</b></p></li>
<li><p><b>Servidor web Nginx</b></p></li>
<li><p><b>El intérprete de lenguaje Ghostscript</b></p></li>
</ul>
</div>

Asegúrese de que hay suficiente espacio en el equipo para la instalación y
haga clic en **Siguiente**.

### Seleccionar una carpeta de destino y completar la instalación

Para completar el proceso de reinstalación, seleccione la **carpeta de
destino** y haga clic en **Instalar**.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Elegir <code>C:\odoo</code> como ubicación de instalación permite que el servidor <em>Nginx</em> se inicie. El software de la caja virtual <abbr title="Internet of Things">IoT</abbr> de Windows de Konvergo ERP no debe <b>instalarse* dentro de ninguno de los directorios del usuario Windows. Si lo hace, *Nginx* **no</b> se ejecutará.</p>
</div>

La instalación puede tardar algunos minutos. Cuando esté completa, haga clic
en **siguiente** para continuar.

Para asegúrese de que la casilla **Iniciar Konvergo ERP** está seleccionada y haga
clic en **Terminar**. Después de la instalación, el servidor de Konvergo ERP se
ejecutará y abrirá `http://localhost:8069` de forma automática en el navegador
web. La página web debe mostrar la página de inicio de la caja IoT.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Posiblemente deberá <a href="windows_iot#iot-restart-windows-iot"><span class="std std-ref">reiniciar</span></a> el programa IoT de Windows si el navegador web no muestra nada.</p>
</div>

## Actualizar desde la página de inicio de la caja IoT

En el fondo, la caja IoT usa una versión del código de Konvergo ERP para poder
funcionar y conectarse a la base de datos. Es posible que necesite actualizar
este código para que la caja IoT funcione bien. Esta operación se debe
realizar de forma rutinaria para asegurarse de que el sistema de la caja IoT y
sus procesos se mantengan actualizados.

Vaya a la página de inicio de la caja IoT en la aplicación IoT ‣ Cajas IoT y
haga clic en la **Dirección IP** de la caja IoT. Después, haga clic en
**Actualizar** (junto al número de versión).

Si hay disponible una nueva versión de la imagen de la caja IoT, aparecerá un
botón **Actualizar a _xx.xx_** en la parte inferior de la página. Haga clic en
este botón para actualizar la unidad y la caja IoT se actualizará a la nueva
versión. Se guardarán todas las configuraciones anteriores.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Este proceso puede durar más de 30 minutos. <b>No</b> apague ni desconecte la caja <abbr title="Internet de las cosas, por sus siglas en inglés">IoT</abbr> ya que la dejaría en un estado inestable. Esto significa que la caja <abbr title="Internet de las cosas, por sus siglas en inglés">IoT</abbr> necesitará <a href="#iot-config-flash"><span class="std std-ref">volver a actualizarse</span></a> con una nueva imagen.</p>
</div> ![Actualización del software de la caja IoT en la página
de inicio de la caja IoT.](../../../../_images/flash-upgrade.png)

## Actualización de controlador (driver)

Puede haber algunos casos en las que las memorias o interfaces que necesite
actualizar para dispositivos individuales (por ejemplo, escalas, herramientas
de medición, entre otros). Para modificar los controladores IoT (drivers e
interfaces) debe sincronizarlos con el código del controlador configurado en
el servidor.

Esto puede ser útil en aquellas situaciones donde los dispositivos IoT (como
básculas, herramientas de medición…) no estén funcionando de forma adecuada
con la caja IoT.

Tanto para la caja IoT de Windows (Konvergo ERP 16 y superior) como para la caja IoT
física, este proceso se puede realizar manualmente desde la página de inicio
de la caja IoT. Vaya a la página de inicio de la caja IoT navegando a
aplicación IoT ‣ cajas IoT, y haga clic en la **dirección IP** de la caja IoT.

Después, haga clic en **Lista de controladores** en la parte inferior de la
página.

![La lista de controladores en la caja IoT con el botón cargar controladores
resaltado.](../../../../_images/load-handlers.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>El código de controladores se obtiene del servidor configurado y necesita estar actualizado con las correcciones y parches más recientes.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Normalmente es necesario volver a actualizar la imagen de la caja <abbr title="internet de las cosas, por sus siglas en inglés">IoT</abbr> después de actualizar la base de datos de Konvergo ERP a una versión nueva.</p></li>
<li><p><b>Se necesita</b> una computadora con un lector o adaptador de memoria micro SD para actualizar la memoria de la tarjeta micro SD.</p></li>
</ul>
</div>0

  *[IoT]: Internet de las cosas, por sus siglas en inglés

