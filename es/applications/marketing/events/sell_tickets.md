# Vender boletos

Cree niveles personalizados para sus boletos (con diferentes precios). Para
hacerlo vaya directamente a la pestaña Boletos en el formulario de la
plantilla del evento. Odoo simplifica el proceso de compra de boletos al
ofrecer varias opciones de pago.

## Configuración

Primero, para activar la creación (y venta) de boletos para eventos, vaya a
Configuración ‣ Configuración, y habilite las funciones Boletos y Venta de
boletos en línea.

La función Boletos permite que se vendan boletos para eventos.

La función Boletos en línea permite la venta de boletos a través del sitio
web.

Nota

Si no se activan estas opciones, aparecerá un botón de registro predeterminado
para las inscripciones gratuitas.

![Vista de la página de configuración de la aplicación Eventos de
Odoo.](../../../_images/events-settings-tickets.png)

## Venta de boletos mediante órdenes de venta

Desde la aplicación Ventas, seleccione un registro de evento creado
previamente (como si fuera un producto) y añádalo como línea de producto. Al
incluir el registro, aparecerá una ventana emergente que permitirá seleccionar
un evento específico (y un nivel de boleto). Dicho boleto de evento se
adjuntará a la orden de venta.

![Vista de una orden de venta con la opción de elegir el evento en la
aplicación Eventos de Odoo.](../../../_images/events-through-sales-order.png)

Los eventos que cuentan con la venta de boletos en línea o a través de órdenes
de venta disponen de un acceso directo con el :guilabel: `botón inteligente de
ventas`, ubicado en la parte superior del formulario de plantilla del evento
(en la aplicación :guilabel: `Eventos`).

Si hace clic en el botón inteligente de ventas se abrirá una página con todas
las órdenes de venta relacionadas con ese evento.

![Vista de un formulario de evento y el botón inteligente de ventas en la
aplicación Eventos de Odoo.](../../../_images/events-sales-smartbutton.png)
![Vista de un formulario de evento en el que destaca la columna de productos
en la pestaña de boletos](../../../_images/events-tickets-registration-
product.png)

## Venta de boletos en el sitio web

Si se compran boletos en el sitio web, el proceso es similar a la creación de
una orden de venta con un producto de registro específico. En este caso, los
boletos se añaden a un carrito virtual, y la transacción se puede completar
como siempre, utilizando cualquiera de las opciones de métodos de pago
preconfigurados del sitio web.

La compra realizada se registra automáticamente en una orden de venta, la cual
puede consultar fácilmente desde el backend de la base de datos.

![Vista de la transacción en el sitio web.](../../../_images/events-online-
ticket-purchase.png)

