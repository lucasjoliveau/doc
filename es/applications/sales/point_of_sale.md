# Punto de venta

Con el **Punto de venta de Konvergo ERP** es fácil gestionar tus tiendas y
restaurantes. La aplicación funciona en cualquier aplicación que tenga un
navegador web, incluso si no está conectado a internet por un momento. Los
movimientos de inventario se registran de manera automática en sus
existencias, podrá ver estadísticas en tiempo real, y sus datos se consolidan
en todas las tiendas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/point-of-sale-28">Tutoriales de Konvergo ERP: Tutoriales de punto de ventas</a></p></li>
<li><p><a href="../general/iot">Documentación sobre las cajas IoT</a></p></li>
</ul>
</div>

## Iniciar una sesión

Desde el **tablero de punto de ventas** haga clic en **Nueva sesión** y en la
pantalla **Control de efectivo de apertura** haga clic en **Abrir sesión**
para iniciar una sesión en el PdV. También puede hacer clic en **Continuar
venta** si la sesión ya está abierta.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><a href="point_of_sale/employee_login">Varios usuarios</a> pueden trabajar en la misma sesión al mismo tiempo, pero solo puede abrir la sesión una vez en el mismo navegador.</p>
</div>

## Vender productos

Haga clic en los productos para agregarlos al carrito. Para cambiar la
**cantidad** , haga clic en **Cant.** e ingrese el número de productos con el
teclado. Para agregar un **descuento** o modificar el **precio** del producto,
haga clic en **% de desc.** o en **precio** para ingresar la cantidad.

Una vez que se complete una orden haga clic en **pago** para proceder a la
página de pago. Seleccione el **método de pago** , ingrese la cantidad
recibida y haga clic en **Validar**. Haga clic en **Nueva orden** para ir con
el siguiente cliente.

![Interfaz de una sesión del punto de venta](../../_images/pos-interface.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Como separador decimal, puede usar tanto <code>,</code> como <code>.</code>.</p></li>
<li><p>La opción <b>efectivo</b> se selecciona de manera automática si ingresa una cantidad sin seleccionar un método de pago.</p></li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El sistema solo puede cargar un número limitado de productos para que la aplicación abra sin dificultades. Haga clic en <b>Buscar más</b> si el producto que necesita no aparece de forma automática.</p>
</div>

## Configurar clientes

Es necesario registrar a su clienta para [poder juntar sus puntos de lealtad y
otorgarle recompensas](point_of_sale/pricing/loyalty), aplicar la [lista
de precios correcta](point_of_sale/pricing/pricelists) de manera
apropiada, o [generar e imprimir una
factura](point_of_sale/receipts_invoices#receipts-invoices-invoices).

Para crear clientes desde una sesión del PdV abierta haga clic en Cliente ‣
Crear, e ingrese la información de contacto. También puede crear clientes
desde el backend, solo debe ir a Punto de venta ‣ Órdenes ‣ Clientes y haga
clic en **Nuevo**. Llena la información de contacto y guarde los cambios.

Para elegir al cliente durante una orden, en la interfaz del Punto de venta
haga clic en **Cliente**. También puede seleccionar al cliente en la pantalla
del pago, solo haga clic en **Cliente**.

## Notas del cliente

Puede agregar **notas del cliente** sobre productos específicos desde una
sesión de punto de venta abierta. Por ejemplo, para dar consejos sobre
limpieza y mantenimiento. También se puede usar para rastrear solicitudes
específicas de los clientes, por ejemplo, es posible que no quieran que
ensamblemos un producto por ellos.

Para hacerlo, seleccione un producto y haga clic en **Nota de cliente**. Se
abrirá una ventana emergente en la que podrá agregar una nota o modificarla.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las notas de un producto de una <a href="point_of_sale/shop/sales_order">orden de venta importada</a>  se muestran tal cual en el carrito.</p>
</div> ![Botón de notas del cliente y notas de los productos en
los carritos del cliente \(orden de venta y sesión de punto de
venta\)](../../_images/customer-notes.png)

Las notas de los clientes también aparecen en los recibos y en las facturas,
como aparecen en el carrito abajo de producto relacionado.

![Recibo para el cliente con notas de la orden de venta y de la función de
nota del cliente](../../_images/notes-receipt.png)

## Regresar y reembolsar productos

Para regresar o reembolsar un producto,

  1. inicie una sesión desde el **tablero del PdV** ;

  2. haga clic en **Reembolsar** y seleccione una orden correspondiente;

  3. seleccione el producto y la cantidad a reembolsar con el teclado;

  4. haga clic en **Reembolso** para regresar a la ventana anterior;

  5. una vez que complete la orden, haga clic en **Pago** para avanzar al reembolso;

  6. haga clic en **Validar** y en **Nueva orden** para seguir con el siguiente cliente.

![vista de reembolso desde el PdV.](../../_images/refund.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Con la barra de búsqueda puede filtrar la <b>lista de órdenes</b> por <b>Número de recibo</b>, <b>Fecha</b> o <b>Cliente</b>.</p></li>
<li><p>Otra forma de reembolsar un producto es seleccionar el producto que se regresó desde una sesión abierta y ponga una cantidad negativa que sea igual al número de productos regresados. Para hacerlo, haga clic en <b>Cant.</b> y agregue <b>+/-</b> seguido por la cantidad de productos que se regresaron.</p></li>
</ul>
</div>

## Cierre de la sesión del PdV

Para cerrar su sesión haga clic en **Cerrar** en la esquina superior derecha
de su pantalla; así abrirá una ventana emergente de **Control de cierre**.
Desde esta ventana usted podrá obtener mucha información:

  * el número de ordenes que se hicieron y la cantidad total que se ganó durante la sesión;

  * las cantidades esperadas agrupadas por método de pago.

Antes de cerrar esta ventana, haga clic en el icono de calculadora para contar
su efectivo. Se abrirá una ventana emergente en donde se calculará la cantidad
total en la caja registradora dependiendo de las monedas y billetes que se
contaron y se sumaron de manera manual. Después, haga clic en **Confirmar** o
en **Descartar** para cerrar la venta. La cantidad calculada estará en la
columna **Contado** y los **Detalles monetarios** se especifican en la sección
de **Notas**.

![Cómo cerrar una sesión del PdV.](../../_images/closing-control.png)

Una vez que haya terminado de controlar las cantidades, haga clic en **Cerrar
sesión** para cerrar y regresar al **tablero del PdV**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si quiere dejar la sesión abierta haga clic en <b>Backend</b> o haga clic en <b>Descartar</b> para cancelar y seguir vendiendo.</p></li>
<li><p>Según su configuración, es posible que solo pueda cerrar sesión si el ingreso en efectivo esperado es igual al efectivo que contó. Para cerrar sesión aunque no coincida, haga clic en <b>De acuerdo</b> en la pantalla de <b>Diferencia de pagos</b>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Es extremadamente recomendable que cierre su sesión del punto de venta al final de cada día.</p></li>
<li><p>Para ver todas sus sesiones anteriores, vaya a Punto de venta ‣ Órdenes ‣ Sesiones.</p></li>
</ul>
</div>

  * [Gestión de varios empleados](point_of_sale/employee_login)
  * [Recibos y facturas](point_of_sale/receipts_invoices)
  * [Configuración](point_of_sale/configuration)
    * [Impresoras ePOS](point_of_sale/configuration/epos_printers)
    * [Conexión segura (HTTPS)](point_of_sale/configuration/https)
    * [Certificado autofirmado para impresoras electrónicas del PdV](point_of_sale/configuration/epos_ssc)
  * Funciones de tienda
    * [Orden de venta](point_of_sale/shop/sales_order)
    * [Códigos de barras](point_of_sale/shop/barcode)
    * [Números de serie y lotes](point_of_sale/shop/serial_numbers)
    * [Enviar después](point_of_sale/shop/ship_later)
    * [Pantalla del cliente](point_of_sale/shop/customer_display)
  * [Funciones para restaurantes](point_of_sale/restaurant)
    * [Cuentas](point_of_sale/restaurant/bill_printing)
    * [Gestión de pisos y mesas](point_of_sale/restaurant/floors_tables)
    * [Impresión de órdenes](point_of_sale/restaurant/kitchen_printing)
    * [Propinas](point_of_sale/restaurant/tips)
  * Funciones de precios
    * [Descuentos](point_of_sale/pricing/discounts)
    * [Etiquetas de descuento (lector de código de barras)](point_of_sale/pricing/discount_tags)
    * [Programas de lealtad](point_of_sale/pricing/loyalty)
    * [Listas de precios](point_of_sale/pricing/pricelists)
    * [Impuestos flexibles (posiciones fiscales)](point_of_sale/pricing/fiscal_position)
    * [Redondeo de efectivo](point_of_sale/pricing/cash_rounding)
  * [Métodos de pago](point_of_sale/payment_methods)
    * [Terminales de pago](point_of_sale/payment_methods/terminals)
      * [Adyen](point_of_sale/payment_methods/terminals/adyen)
      * [Ingenico](point_of_sale/payment_methods/terminals/ingenico)
      * [SIX](point_of_sale/payment_methods/terminals/six)
      * [Stripe](point_of_sale/payment_methods/terminals/stripe)
      * [Vantiv](point_of_sale/payment_methods/terminals/vantiv)
      * [Worldline](point_of_sale/payment_methods/terminals/worldline)
  * [Reportes](point_of_sale/reporting)

