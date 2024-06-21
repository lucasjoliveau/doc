# Facturas proforma

Una factura _proforma_ es una factura resumida o estimada que se envía antes
de entregar la mercancía. Esta indica el tipo y la cantidad de bienes, su
valor y otra información importante como los cargos por peso y transporte.

Las facturas proforma se utilizan comúnmente como facturas preliminares con
una cotización. También se utilizan durante la importación para fines
aduaneros. Difieren de una factura normal, en que _no_ son una demanda (o
solicitud) de pago.

## Configuración

**Debe** activar la función _factura proforma_ para poder utilizar facturas
proforma.

Para activar esta función, vaya a la aplicación Ventas ‣ Configuración ‣
Ajustes y, en la sección **cotizaciones y órdenes** , haga clic en la casilla
que se encuentra junto a **factura proforma**. Luego, haga clic en el botón
correspondiente para **guardar** todos los cambios.

![Ajustes de la función para crear facturas proforma en la aplicación Ventas
de Konvergo ERP.](../../../../_images/pro-forma-setting.png)

## Enviar factura proforma

Una vez que activó la función **Factura proforma** , tendrá la opción de
enviarla desde cualquier cotización u orden de venta con el botón **Enviar
factura proforma**.

![El botón "Enviar factura proforma" en una orden de ventas común en la
aplicación Ventas en Konvergo ERP.](../../../../_images/send-pro-forma-invoice-
button.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las facturas proforma <b>no</b> se pueden enviar para una orden de venta o cotización si ya se ha enviado una factura por un pago inicial, o para una suscripción recurrente.</p>
<p>En cualquier caso, no aparecerá el botón <b>enviar factura proforma</b>.</p>
<p>Sin embargo, se pueden enviar facturas proforma para servicios, registros de eventos, cursos y nuevas suscripciones. Las facturas proforma no se limitan a bienes físicos, consumibles o almacenables.</p>
</div>

Cuando se hace clic en el botón **enviar factura proforma** , aparece una
ventana emergente desde la cual se puede enviar un correo electrónico.

En la ventana emergente, el campo **destinatarios** se completa
automáticamente con el cliente de la orden de venta o cotización. El campo
**asunto** y el cuerpo del correo electrónico se pueden modificar, si es
necesario.

La factura proforma se agrega automáticamente como un adjunto al correo
electrónico.

Una vez que esté listo, haga clic en **Enviar** y Konvergo ERP enviará el correo
electrónico con la factura proforma adjunta al cliente.

![La ventana emergente para redactar un correo electrónico que aparece con la
factura proforma adjunta en la aplicación Ventas de
Konvergo ERP.](../../../../_images/pro-forma-email-message-pop-up.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para previsualizar la factura proforma haga clic en el PDF en la parte inferior de la ventana emergente de correo electrónico <em>antes</em> de hacer clic en <b>enviar</b>. El documento se descargará de forma automática al hacer clic en el PDF, ábralo para ver y revisar el contenido de la factura proforma.</p>
<img alt="Ejemplo de una factura proforma en PDF de la aplicación Ventas de Konvergo ERP." class="align-center" src="../../../../_images/pro-forma-pdf.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="invoicing_policy">Facturar por cantidades entregadas u ordenadas</a></p>
</div>

