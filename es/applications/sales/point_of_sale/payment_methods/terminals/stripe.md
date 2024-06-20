# Stripe

Conectar una terminal de pago le permite ofrecerle a sus clientes un flujo de
pago ágil y facilitar el trabajo de sus cajeros.

Importante

  * Las terminales de pago Stripe no necesitan una [caja IoT](../../../../general/iot.html).

  * Las terminales de Stripe se pueden utilizar en muchos países, pero no en todo el mundo. Consulte la [disponibilidad global de la terminal Stripe](https://support.stripe.com/questions/global-availability-for-stripe-terminal).

  * La integración de Stripe funciona con los [lectores de Stripe Terminal](https://docs.stripe.com/terminal/smart-readers)

Ver también

  * [Stripe como proveedor de pagos](../../../../finance/payment_providers/stripe.html)

  * [Lista de métodos de pago compatibles con Stripe](https://stripe.com/payments/payment-methods)

## Configuración

### Configure el método de pago

Active **Stripe** en Punto de venta ‣ Configuración ‣ Ajustes ‣ Terminales de
pago y habilite Stripe.

Después, cree el método de pago:

  * Vaya a Punto de venta ‣ Configuración ‣ Métodos de pago, haga clic en crear y complete el campo método con el nombre de su método de pago.

  * Establezca el campo diario como banco y el campo usar una terminal de pago como Stripe.

  * Introduzca el número de serie de su terminal de pago en el campo número de serie de Stripe.

  * Haga clic en no olvide completar la conexión con Stripe antes de utilizar este método de pago.

![Formulario de creación de método de pago](../../../../../_images/create-
method-stripe.png)

Nota

  * Haga clic en identificar cliente para permitir este método de pago **únicamente** a clientes identificados. Deje la casilla identificar cliente sin seleccionar para que los clientes sin identificar puedan pagar con Stripe.

  * Los campos cuenta pendiente y cuenta intermediaria se pueden dejar vacíos para utilizar las cuentas predeterminadas.

  * Puede encontrar el número de serie de su terminal de pago en la parte inferior del dispositivo o en el [tablero de Stripe](https://dashboard.stripe.com).

### Conectar Stripe con Odoo

Haga clic en conectar a Stripe. Esto lo redirige de forma automática a la
página de configuración. Complete toda la información para crear su cuenta de
Stripe y vincúlela con Odoo. Una vez que complete los formularios, puede
obtener las claves API (clave pública y clave secreta) en el sitio web de
**Stripe**. Para hacerlo, haga clic en obtenga sus claves secreta y pública,
haga clic en las claves para copiarlas y péguelas en los campos
correspondientes en Odoo. Ahora puede configurar su terminal en un PdV.

![Formulario de conexión con Stripe](../../../../../_images/stripe-
connect.png)

Nota

  * Cuando usa **Stripe** únicamente en Punto de venta, solo necesita la **clave secreta** para usar su terminal.

  * Cuando utiliza Stripe **como proveedor de pago** , el estado se puede establecer como deshabilitado.

  * El botón conectar a Stripe no funciona en las bases de datos con alojamiento **local**. Para obtener las claves API de forma manual, inicie sesión en su [tablero de Stripe](https://dashboard.stripe.com), escriba `API` en la barra de búsqueda y haga clic en Desarrolladores > API.

### Configurar la terminal de pago

Deslice a la derecha en su terminal de pago, haga clic en ajustes, introduzca
el código NIP de administrador, valide y seleccione su red.

Nota

  * El dispositivo debe estar conectado a una red de Wi-Fi segura.

  * Su base de datos de Odoo y su terminal de pago deben compartir la misma red.

  * Debe ingresar el código NIP de administrador para acceder a los ajustes de su terminal de pago. De forma predeterminada, este código es `07139`.

### Vincular el método de pago con un PdV

Para agregar un **método de pago** a su punto de venta, vaya a Punto de venta
‣ Configuración ‣ Ajustes. Seleccione el PdV, baje a la sección pagos y
agregue el método de pago que utilizará para **Stripe** en el campo métodos de
pago.

## Pagar con una terminal de pago

Al procesar un pago, seleccione Stripe como el método de pago. Revise el
importe y haga clic en Enviar. En cuanto se realiza el pago, el estado cambia
a pago exitoso. Haga clic en cancelar para cancelar la solicitud de pago.

Nota

  * En caso de que haya problemas de conexión entre Odoo y la terminal de pago, puede forzar el pago al hacer clic en forzar hecho, lo que le permite validar la orden.

Esta opción solo está disponible después de recibir un mensaje de error que le
informa que la conexión falló.

  * El nivel de la batería de la terminal debe ser por lo menos del 10% para poder usarla.

  * El dispositivo no acepta pagos menores a €0.50.

## Solución de problemas

### La terminal de pago no está disponible en su cuenta de Stripe

Debe agregar la terminal de pago de forma manual si no está disponible en su
cuenta de Stripe:

  1. Inicie sesión en su [cuenta de Stripe](https://dashboard.stripe.com) y vaya a su tablero de Stripe ‣ Pagos ‣ Lectores ‣ Ubicaciones.

  2. Agregue una ubicación mediante el botón \+ Nuevo o seleccione una ubicación existente.

  3. Haga clic en el botón \+ Nuevo en la sección lectores y complete la información necesaria.

Nota

Debe proporcionar un **código de registro**. Para obtener este código, deslice
la pantalla de su dispositivo a la derecha, ingrese el código NIP de
administrador (es `07139` de forma predeterminada), valide y haga clic en
Generar código de registro.

