# Correo postal

Enviar correspondencia postal puede ser una estrategia eficaz para llamar la
atención de otras personas, sobre todo si suelen recibir muchos correos en sus
bandejas de entrada. Konvergo ERP le permite enviar facturas y reportes de seguimiento
a través de correo postal a todo el mundo, todo desde su base de datos.

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Factures de cliente y active
el **Correo postal**.

Para que esta sea una función predeterminada deberá seleccionar **Enviar por
correo postal** en la sección **Opciones de envío predeterminadas**.

![Activar la función de correo postal en los ajustes de la aplicación
Contabilidad de Konvergo ERP.](../../../../_images/setup-snailmail.png)

## Enviar facturas por correo

Abra su factura, haga clic en **Enviar e imprimir** y seleccione **Enviar por
correo postal**. Antes de enviar la carta asegúrese de que los datos en la
dirección y el país de su cliente sean correctos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Su documento debe cumplir con las siguientes reglas para poder pasar la validación antes de su envío:</p>
<ul>
<li><p>Los márgenes deben de ser de <b>5 mm</b> en los cuatro costados. Konvergo ERP coloca márgenes exteriores blancos antes de enviar el correo postal, así que es posible que se corte la información si se sale de los márgenes. Active el <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> para revisar los márgenes, vaya a Ajustes generales ‣ Técnico ‣ Reportes: Formato de papel.</p></li>
<li><p>Debe dejar en blanco un cuadrado de <b>15 mm por 15 mm</b> en la esquina inferior izquierda.</p></li>
<li><p>El área postal debe estar despejada (<a download="" href="../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf"><code>descargue la plantilla PDF de correo postal</code></a> para obtener más detalles).</p></li>
<li><p>Pingen (el proveedor de servicios de correo postal de Konvergo ERP) escanea esa área para procesar la dirección. Si escribe algo fuera del área, no contará como parte de la dirección.</p></li>
</ul>
</div>

## Precios

El correo postal es un servicio de [Compras dentro de la aplicación
(IAP)](../../../essentials/in_app_purchase) que necesita de timbres
prepagados (es decir, créditos) para funcionar. Enviar un documento consume un
timbre.

Para comprar timbres, vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Facturas
de cliente: Correo postal, haga clic en **Comprar créditos** o vaya a Ajustes
‣ Compras dentro de la aplicación de Konvergo ERP y haga clic en **Ver mis
servicios**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://iap.odoo.com/privacy#header_4">Política de privacidad de compras dentro de la aplicación de Konvergo ERP</a></p>
</div>

