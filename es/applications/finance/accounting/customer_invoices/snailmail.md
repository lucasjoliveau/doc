# Correo postal

Enviar correspondencia postal puede ser una estrategia eficaz para llamar la
atención de otras personas, sobre todo si suelen recibir muchos correos en sus
bandejas de entrada. Odoo le permite enviar facturas y reportes de seguimiento
a través de correo postal a todo el mundo, todo desde su base de datos.

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Factures de cliente y active
el Correo postal.

Para que esta sea una función predeterminada deberá seleccionar Enviar por
correo postal en la sección Opciones de envío predeterminadas.

![Activar la función de correo postal en los ajustes de la aplicación
Contabilidad de Odoo.](../../../../_images/setup-snailmail.png)

## Enviar facturas por correo

Abra su factura, haga clic en Enviar e imprimir y seleccione Enviar por correo
postal. Antes de enviar la carta asegúrese de que los datos en la dirección y
el país de su cliente sean correctos.

Importante

Su documento debe cumplir con las siguientes reglas para poder pasar la
validación antes de su envío:

  * Los márgenes deben de ser de **5 mm** en los cuatro costados. Odoo coloca márgenes exteriores blancos antes de enviar el correo postal, así que es posible que se corte la información si se sale de los márgenes. Active el [modo de desarrollador](../../../general/developer_mode.html#developer-mode) para revisar los márgenes, vaya a Ajustes generales ‣ Técnico ‣ Reportes: Formato de papel.

  * Debe dejar en blanco un cuadrado de **15 mm por 15 mm** en la esquina inferior izquierda.

  * El área postal debe estar despejada ([`descargue la plantilla PDF de correo postal`](../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf) para obtener más detalles).

  * Pingen (el proveedor de servicios de correo postal de Odoo) escanea esa área para procesar la dirección. Si escribe algo fuera del área, no contará como parte de la dirección.

## Precios

El correo postal es un servicio de [Compras dentro de la aplicación
(IAP)](../../../essentials/in_app_purchase.html) que necesita de timbres
prepagados (es decir, créditos) para funcionar. Enviar un documento consume un
timbre.

Para comprar timbres, vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Facturas
de cliente: Correo postal, haga clic en Comprar créditos o vaya a Ajustes ‣
Compras dentro de la aplicación de Odoo y haga clic en Ver mis servicios.

Ver también

[Política de privacidad de compras dentro de la aplicación de
Odoo](https://iap.odoo.com/privacy#header_4)

