# Worldline

Conectar una terminal de pago le permite ofrecerle a sus clientes un flujo de
pago ágil y facilitar el trabajo de sus cajeros.

Importante

  * Las terminales de pago Worldline necesitan una [caja IoT](../../../../general/iot.html).

  * En este momento Worldline solo está disponible en Bélgica, Países Bajos y Luxemburgo.

  * Odoo es compatible con las terminales de Worldline que utilizan el protocolo CTEP (por ejemplo, las terminales Yomani XR y Yoximo). Si tiene alguna duda, póngase en contacto con su proveedor de pagos para asegurarse de la compatibilidad de su terminal.

## Configuración

### Conectar una caja IoT

Conectar una terminal de pago Worldline a Odoo es una función que requiere una
caja IoT. Para más información sobre cómo conectar una caja IoT a su base de
datos, refiérase a [documentación
IoT](../../../../general/iot/config/connect.html).

### Configurar el protocolo

Desde su terminal, haga clic en «.» ‣ 3 ‣ Detener ‣ 3 ‣ 0 ‣ 9. Introduzca la
contraseña técnica **«1235789»** y haga clic en OK ‣ 4 ‣ 2. Después, haga clic
en Cambio ‣ CTEP (como protocolo ECR) ‣ OK. Haga clic en **OK** tres veces en
las siguientes pantallas (_ticket de ECR CTEP_ , _ancho del ticket de ECR_ y
_conjunto de caracteres_). Por último, haga clic en **detener** tres veces. La
terminal se reiniciará de forma automática.

### Establecer la dirección IP

Desde su terminal, haga clic en «.» ‣ 3 ‣ Detener ‣ 3 ‣ 0 ‣ 9. Introduzca la
contraseña técnica **«1235789»** y haga clic en OK ‣ 4 ‣ 9. Después haga clic
en Cambio ‣ TCP/IP (pantalla de _configuración física TCP_) ‣ OK ‣ OK
(pantalla de _configuración de cliente TCP_).

Por último, configure un nombre de alojamiento y un número de puerto.

#### Nombre de alojamiento

Para configurar el nombre de alojamiento, ingrese la secuencia de números de
la dirección IP de su Caja IoT y presione **OK** con cada «.» hasta que llegue
al signo de los dos puntos.

Después, presione **OK** dos veces.

Example

Esta es una secuencia de dirección IP: `10.30.19.4:8069`.

En la *pantalla del nombre del alojamiento¨, escriba 10 –> OK –> 30 –> OK –>
19 –> OK –> 4 –> OK –> OK`.

Nota

La dirección IP de su Caja IoT está disponible en la base de datos de la
aplicación de su caja IoT.

#### Número de puerto

En la pantalla de _número de puerto_ , ingrese **9001** (o **9050** en
Windows) y haga clic en OK (_ECR protocol SSL no_) ‣ OK. Haga clic en
**detener** tres veces, la terminal se reiniciará de forma automática.

Advertencia

Es necesario agregar una excepción en el firewall para los dispositivos IoT de
**Windows**. Siga las [instrucciones adicionales en la documentación de
Windows IoT](../../../../general/iot/config/windows_iot.html#iot-windows-
wordline) para agregar la excepción al firewall de Windows.

### Configure el método de pago

Habilite la terminal de pago en los [ajustes de la
aplicación](../../configuration.html#configuration-settings) y [cree el método
de pago relacionado](../../payment_methods.html). Establezca el tipo de diario
como Banco y seleccione Worldline en el campo Usar una terminal de pago.
Luego, seleccione el dispositivo correspondiente en el campo Dispositivo de
terminal de pago.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Ya que haya creado el método de pago, puede seleccionarlo en sus ajustes del
Punto de venta. Para hacerlo, vaya a los [ajustes del punto de
venta](../../configuration.html#configuration-settings), haga clic en Editar y
agregue el método de pago en la sección de Pagos.

Truco

  * Contraseña técnica: `1235789`

  * Para contactar al soporte técnico de Worldline, llame al `02 727 61 11` y seleccione «comerciante». Su llamada se transferirá al servicio deseado.

  * Configure la terminal de cajero si tiene tanto una terminal de cliente como una de cajero.

  * Para evitar bloquear la terminal, primero revise la configuración inicial.

  * Configure una dirección IP fija en el router de su Caja IoT para evitar perder la conexión.

## Pagar con una terminal de pago

Al procesar un pago, seleccione _Worldline_ como método de pago. Compruebe el
importe y haga clic en _Enviar_. Una vez que el pago tenga éxito, el estado
cambia a _Pago exitoso_.

Una vez que se procese el pago, el tipo de tarjeta que se utilizó y el ID de
la transacción aparece en el registro del pago.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png)

Nota

  * En caso de que haya problemas de conexión entre Odoo y la terminal de pago, fuerce el pago al hacer clic en _Forzar terminación_ , lo cual le permite validar la orden. Esta opción solo está disponible después de recibir un mensaje de error que indique que la conexión falló.

  * Para cancelar la solicitud de pago, haga clic en **Cancelar**.

