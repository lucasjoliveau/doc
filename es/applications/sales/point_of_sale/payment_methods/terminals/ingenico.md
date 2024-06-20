# Ingenico

Conectar una terminal de pago le permite ofrecerle a sus clientes un flujo de
pago ágil y facilitar el trabajo de sus cajeros.

Importante

  * Las terminales de pago Ingenico necesitan una [caja IoT](../../../../general/iot.html).

  * En este momento Ingenico solo está disponible en Bélgica, Países Bajos y Luxemburgo.

  * Odoo funciona con las terminales de pago Lane, Desk y Move de Ingenico que son compatibles con el protocolo de comunicación TLV a través de TCP/IP.

## Configuración

### Conectar una caja IoT

Conectar una terminal de pago Ingenico a Odoo es una función que requiere una
caja IoT. Para más información sobre cómo conectar una caja IoT a su base de
datos, refiérase a [documentación
IoT](../../../../general/iot/config/connect.html).

### Configure las terminales de pago Lane/Desk/Move 5000 de Ingenico para
BENELUX

  1. Presione el botón de función (F en Lane/5000, ⦿ en Desk/5000 y Move/5000).

  2. Vaya a menú Kassa ‣ menú de Ajustes e ingrese la contraseña de los ajustes.

  3. Seleccione Change Connection (cambiar conexión) y presione OK en la siguiente pantalla.

  4. Seleccione TCP/IP y IP-address.

  5. En la siguiente pantalla ingrese la dirección IP de su caja IoT.

  6. Escriba `9000` como número de puerto y presione OK en la siguiente pantalla.

En este momento, la terminal se reiniciará y se debería de ver en su caja IoT
de Odoo.

![../../../../../_images/payment_terminal_02.png](../../../../../_images/payment_terminal_02.png)

### Configure el método de pago

Habilite la terminal de pago en los [ajustes de la
aplicación](../../configuration.html#configuration-settings) y [cree el método
de pago relacionado](../../payment_methods.html). Establezca el tipo de diario
como Banco y seleccione Ingenico en el campo Usar una terminal de pago. Luego,
seleccione el dispositivo correspondiente en el campo Dispositivo de terminal
de pago.

![../../../../../_images/payment-method2.png](../../../../../_images/payment-
method2.png)

Ya que haya creado el método de pago, puede seleccionarlo en sus ajustes del
Punto de venta. Para hacerlo, vaya a los [ajustes del punto de
venta](../../configuration.html#configuration-settings), haga clic en Editar y
agregue el método de pago en la sección de Pagos.

## Pagar con una terminal de pago

Al procesar un pago en la _interfaz de PdV_ seleccione un _método de pago_ con
una terminal. Revise la cantidad en la columna emitida sea la misma que tiene
que enviarse a la terminal de pago y haga clic en _Enviar_. Cuando se realice
el pago, el estado cambiará a _Pago realizado_.

![../../../../../_images/payment_terminal_05.png](../../../../../_images/payment_terminal_05.png)

Si quiere cancelar la petición de pago, haga clic en cancelar. Puede intentar
enviar la petición de pago de nuevo.

Si hay un problema con la terminal de pago, puede forzar el pago si usa
_Forzar terminación_. Esto le permitirá validar la orden en Odoo incluso si la
conexión entre la terminal y Odoo tiene problemas.

Nota

La opción solo estará disponible si recibe un mensaje de error en el que diga
que la conexión falló.

Una vez que se haya procesado su pago, verá el tipo de tarjeta que se usó y el
ID de la transacción en el registro del pago.

![../../../../../_images/payment_terminal_06.png](../../../../../_images/payment_terminal_06.png)

