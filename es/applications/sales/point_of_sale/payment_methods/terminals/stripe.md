# Stripe

Conectar una terminal de pago le permite ofrecerle a sus clientes un flujo de
pago ágil y facilitar el trabajo de sus cajeros.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Las terminales de pago Stripe no necesitan una <a href="../../../../general/iot">caja IoT</a>.</p></li>
<li><p>Las terminales de Stripe se pueden utilizar en muchos países, pero no en todo el mundo. Consulte la <a href="https://support.stripe.com/questions/global-availability-for-stripe-terminal">disponibilidad global de la terminal Stripe</a>.</p></li>
<li><p>La integración de Stripe funciona con los <a href="https://docs.stripe.com/terminal/smart-readers">lectores de Stripe Terminal</a></p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../../finance/payment_providers/stripe">Stripe como proveedor de pagos</a></p></li>
<li><p><a href="https://stripe.com/payments/payment-methods">Lista de métodos de pago compatibles con Stripe</a></p></li>
</ul>
</div>

## Configuración

### Configure el método de pago

Active **Stripe** en Punto de venta ‣ Configuración ‣ Ajustes ‣ Terminales de
pago y habilite **Stripe**.

Después, cree el método de pago:

  * Vaya a Punto de venta ‣ Configuración ‣ Métodos de pago, haga clic en **crear** y complete el campo **método** con el nombre de su método de pago.

  * Establezca el campo **diario** como **banco** y el campo **usar una terminal de pago** como **Stripe**.

  * Introduzca el número de serie de su terminal de pago en el campo **número de serie de Stripe**.

  * Haga clic en **no olvide completar la conexión con Stripe antes de utilizar este método de pago.**

![Formulario de creación de método de pago](../../../../../_images/create-
method-stripe.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Haga clic en <b>identificar cliente</b> para permitir este método de pago <b>únicamente</b> a clientes identificados. Deje la casilla <b>identificar cliente</b> sin seleccionar para que los clientes sin identificar puedan pagar con Stripe.</p></li>
<li><p>Los campos <b>cuenta pendiente</b> y <b>cuenta intermediaria</b> se pueden dejar vacíos para utilizar las cuentas predeterminadas.</p></li>
<li><p>Puede encontrar el número de serie de su terminal de pago en la parte inferior del dispositivo o en el <a href="https://dashboard.stripe.com">tablero de Stripe</a>.</p></li>
</ul>
</div>

### Conectar Stripe con Konvergo ERP

Haga clic en **conectar a Stripe**. Esto lo redirige de forma automática a la
página de configuración. Complete toda la información para crear su cuenta de
Stripe y vincúlela con Konvergo ERP. Una vez que complete los formularios, puede
obtener las claves API (**clave pública** y **clave secreta**) en el sitio web
de **Stripe**. Para hacerlo, haga clic en **obtenga sus claves secreta y
pública** , haga clic en las claves para copiarlas y péguelas en los campos
correspondientes en Konvergo ERP. Ahora puede configurar su terminal en un PdV.

![Formulario de conexión con Stripe](../../../../../_images/stripe-
connect.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cuando usa <b>Stripe</b> únicamente en Punto de venta, solo necesita la <b>clave secreta</b> para usar su terminal.</p></li>
<li><p>Cuando utiliza Stripe <b>como proveedor de pago</b>, el <b>estado</b> se puede establecer como <b>deshabilitado</b>.</p></li>
<li><p>El botón <b>conectar a Stripe</b> no funciona en las bases de datos con alojamiento <b>local</b>. Para obtener las claves API de forma manual, inicie sesión en su <a href="https://dashboard.stripe.com">tablero de Stripe</a>, escriba <code>API</code> en la barra de búsqueda y haga clic en <b>Desarrolladores &gt; API</b>.</p></li>
</ul>
</div>

### Configurar la terminal de pago

Deslice a la derecha en su terminal de pago, haga clic en **ajustes** ,
introduzca el código NIP de administrador, valide y seleccione su red.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>El dispositivo debe estar conectado a una red de Wi-Fi segura.</p></li>
<li><p>Su base de datos de Konvergo ERP y su terminal de pago deben compartir la misma red.</p></li>
<li><p>Debe ingresar el código NIP de administrador para acceder a los ajustes de su terminal de pago. De forma predeterminada, este código es <code>07139</code>.</p></li>
</ul>
</div>

### Vincular el método de pago con un PdV

Para agregar un **método de pago** a su punto de venta, vaya a Punto de venta
‣ Configuración ‣ Ajustes. Seleccione el PdV, baje a la sección **pagos** y
agregue el método de pago que utilizará para **Stripe** en el campo **métodos
de pago**.

## Pagar con una terminal de pago

Al procesar un pago, seleccione **Stripe** como el método de pago. Revise el
importe y haga clic en **Enviar**. En cuanto se realiza el pago, el estado
cambia a **pago exitoso**. Haga clic en **cancelar** para cancelar la
solicitud de pago.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><div class="line-block">
<div class="line">En caso de que haya problemas de conexión entre Konvergo ERP y la terminal de pago, puede forzar el pago al hacer clic en <b>forzar hecho</b>, lo que le permite validar la orden.</div>
<div class="line">Esta opción solo está disponible después de recibir un mensaje de error que le informa que la conexión falló.</div>
</div>
</li>
<li><p>El nivel de la batería de la terminal debe ser por lo menos del 10% para poder usarla.</p></li>
<li><p>El dispositivo no acepta pagos menores a €0.50.</p></li>
</ul>
</div>

## Solución de problemas

### La terminal de pago no está disponible en su cuenta de Stripe

Debe agregar la terminal de pago de forma manual si no está disponible en su
cuenta de Stripe:

  1. Inicie sesión en su [cuenta de Stripe](https://dashboard.stripe.com) y vaya a su tablero de Stripe ‣ Pagos ‣ Lectores ‣ Ubicaciones.

  2. Agregue una ubicación mediante el botón **\+ Nuevo** o seleccione una ubicación existente.

  3. Haga clic en el botón **\+ Nuevo** en la sección **lectores** y complete la información necesaria.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Debe proporcionar un <b>código de registro</b>. Para obtener este código, deslice la pantalla de su dispositivo a la derecha, ingrese el código NIP de administrador (es <code>07139</code> de forma predeterminada), valide y haga clic en <b>Generar código de registro</b>.</p>
</div>

