# Worldline

Conectar una terminal de pago le permite ofrecerle a sus clientes un flujo de
pago ágil y facilitar el trabajo de sus cajeros.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Las terminales de pago Worldline necesitan una <a href="../../../../general/iot">caja IoT</a>.</p></li>
<li><p>En este momento Worldline solo está disponible en Bélgica, Países Bajos y Luxemburgo.</p></li>
<li><p>Konvergo ERP es compatible con las terminales de Worldline que utilizan el protocolo CTEP (por ejemplo, las terminales Yomani XR y Yoximo). Si tiene alguna duda, póngase en contacto con su proveedor de pagos para asegurarse de la compatibilidad de su terminal.</p></li>
</ul>
</div>

## Configuración

### Conectar una caja IoT

Conectar una terminal de pago Worldline a Konvergo ERP es una función que requiere una
caja IoT. Para más información sobre cómo conectar una caja IoT a su base de
datos, refiérase a [documentación
IoT](../../../../general/iot/config/connect).

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

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line">Esta es una secuencia de dirección IP: <code>10.30.19.4:8069</code>.</div>
<div class="line">En la <a href="#id1"><span class="problematic" id="id2">*</span></a>pantalla del nombre del alojamiento¨, escriba 10 –&gt; OK –&gt; 30 –&gt; OK –&gt; 19 –&gt; OK –&gt; 4 –&gt; OK –&gt; OK`.</div>
</div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La dirección IP de su Caja IoT está disponible en la base de datos de la aplicación de su caja IoT.</p>
</div>

#### Número de puerto

En la pantalla de _número de puerto_ , ingrese **9001** (o **9050** en
Windows) y haga clic en OK (_ECR protocol SSL no_) ‣ OK. Haga clic en
**detener** tres veces, la terminal se reiniciará de forma automática.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Es necesario agregar una excepción en el firewall para los dispositivos IoT de <b>Windows</b>. Siga las <a href="../../../../general/iot/config/windows_iot#iot-windows-wordline"><span class="std std-ref">instrucciones adicionales en la documentación de Windows IoT</span></a> para agregar la excepción al firewall de Windows.</p>
</div>

### Configure el método de pago

Habilite la terminal de pago en los [ajustes de la
aplicación](../../configuration#configuration-settings) y [cree el método
de pago relacionado](../../payment_methods). Establezca el tipo de diario
como **Banco** y seleccione **Worldline** en el campo **Usar una terminal de
pago**. Luego, seleccione el dispositivo correspondiente en el campo
**Dispositivo de terminal de pago**.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Ya que haya creado el método de pago, puede seleccionarlo en sus ajustes del
Punto de venta. Para hacerlo, vaya a los [ajustes del punto de
venta](../../configuration#configuration-settings), haga clic en
**Editar** y agregue el método de pago en la sección de **Pagos**.

<div class="alert alert-info" id="worldline-yomani-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Contraseña técnica: <code>1235789</code></p></li>
<li><p>Para contactar al soporte técnico de Worldline, llame al <code>02 727 61 11</code> y seleccione «comerciante». Su llamada se transferirá al servicio deseado.</p></li>
<li><p>Configure la terminal de cajero si tiene tanto una terminal de cliente como una de cajero.</p></li>
<li><p>Para evitar bloquear la terminal, primero revise la configuración inicial.</p></li>
<li><p>Configure una dirección IP fija en el router de su Caja IoT para evitar perder la conexión.</p></li>
</ul>
</div>

## Pagar con una terminal de pago

Al procesar un pago, seleccione _Worldline_ como método de pago. Compruebe el
importe y haga clic en _Enviar_. Una vez que el pago tenga éxito, el estado
cambia a _Pago exitoso_.

Una vez que se procese el pago, el tipo de tarjeta que se utilizó y el ID de
la transacción aparece en el registro del pago.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>En caso de que haya problemas de conexión entre Konvergo ERP y la terminal de pago, fuerce el pago al hacer clic en <em>Forzar terminación</em>, lo cual le permite validar la orden. Esta opción solo está disponible después de recibir un mensaje de error que indique que la conexión falló.</p></li>
<li><p>Para cancelar la solicitud de pago, haga clic en <b>Cancelar</b>.</p></li>
</ul>
</div>

