# Confirmación de orden de pago en línea

La aplicación **Ventas** de Odoo permite que los clientes confirmen sus
órdenes mediante un pago en línea desde la orden de venta. Una vez que el
cliente paga de manera electrónica la orden de venta, el vendedor asignado a
la orden recibe una notificación al instante sobre la confirmación de esa
orden.

## Activar los pagos en línea

La función _Pago en línea_ **debe** estar habilitada para que los clientes
puedan confirmar sus órdenes con un pago en línea.

Para activar la función de _pago en línea_ , vaya a la aplicación Ventas ‣
Configuración ‣ Ajustes, diríjase a la sección Cotizaciones y órdenes, marque
la casilla junto a la función Pago en línea y haga clic en Guardar.

![Los ajustes de pago en línea en la aplicación Ventas de
Odoo.](../../../../_images/online-payment-setting.png)

Debajo de la opción Pago en línea en la página de ajustes de _Ventas_ se
encuentra el campo Validez de cotización predeterminada. En este campo le
proporciona la opción de agregar un número específico de días para que las
cotizaciones sean válidas durante ese tiempo de forma predeterminada.

Para habilitar esta función en una cotización estándar, marque la casilla de
la opción Pago. Está ubicada en el campo Confirmación en línea dentro de la
pestaña Otra información.

![Los ajustes de pago en línea de una cotización estándar en la aplicación
Ventas de Odoo.](../../../../_images/online-payment-option-quotation.png)

Para habilitar esta función en la plantilla de una cotización, marque la
casilla de la opción Pago. Está ubicada en el campo Confirmación en línea
dentro del formulario de la plantilla de la cotización.

![Los ajustes de pago en línea de los formularios de plantilla de la
cotización en la aplicación Ventas de Odoo.](../../../../_images/online-
payment-option-quotation-template.png)

## Proveedores de pago

Aparece un enlace para configurar los proveedores de pago después de activar
la función Pago en línea.

La página de Proveedores de pago se abre tras hacer clic en ese enlace. Allí
puede habilitar, personalizar y publicar una gran cantidad de proveedores de
pago.

![La página de proveedores de pago en la aplicación Ventas de
Odoo.](../../../../_images/payment-providers-page.png)

Ver también

[Pagos en línea](../../../finance/payment_providers.html)

## Registrar un pago

Luego de abrir las cotizaciones en su portal de clientes, los clientes pueden
hacer clic en Aceptar y pagar para confirmar su orden con un pago en línea.

![El botón Aceptar y pagar en una cotización en línea en la aplicación Ventas
de Odoo. ](../../../../_images/accept-and-pay-button.png)

Después de que los clientes hacen clic en Aceptar y pagar aparece la ventana
emergente Validar orden. Dentro hay distintas opciones para realizar pagos en
línea en la sección Pagar con.

![Cómo registrar un pago en una ventana emergente para validar órdenes en la
aplicación Ventas de Odoo.](../../../../_images/validate-order-pay-with.png)

Nota

Odoo **solo** mostrará, dentro de la ventana emergente Validar orden, las
opciones de pago que haya publicado y configurado en la página de proveedores
de pago.

Una vez que el cliente elija un método de pago deberá hacer clic en el botón
Pagar de la ventana emergente para confirmar la orden. Odoo notificará de
forma instantánea al vendedor asignado una vez que se pague y confirme la
orden en línea.

![Un ejemplo de la notificación que aparece en el chatter al realizar un pago
en línea.](../../../../_images/payment-confirmation-notification-chatter.png)

Ver también

  * [Plantillas de cotización](quote_template.html)

  * [Firmas electrónicas para la confirmación de órdenes.](get_signature_to_validate.html)

  * [Pagos en línea](../../../finance/payment_providers.html)

