# Adyen

Si conecta su **terminal de pago Adyen** podrá ofrecer a sus clientes un flujo
de pago eficaz y facilitar el trabajo a sus cajeros.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Las terminales de pago Adyen no necesitan una <a href="../../../../general/iot">caja IoT</a>.</p></li>
<li><p>Las terminales Adyen se pueden utilizar en muchos países, pero no en todo el mundo. Consulte la <a href="https://docs.adyen.com/point-of-sale/what-we-support/supported-languages/">lista de países compatibles con Adyen</a>.</p></li>
<li><p>Adyen funciona solo con empresas que procesan más de <b>10 millones anuales</b> o que facturan mínimo <b>1000 transacciones al mes</b>.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/">Lista de métodos de pago compatibles con Adyen</a></p></li>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals/">Lista de terminales Adyen</a></p></li>
</ul>
</div>

## Configuración

Primero cree su cuenta de Adyen en el [sitio web de
Adyen](https://www.adyen.com/). Después, siga los pasos que se muestran en la
pantalla de su terminal para activarla.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://docs.adyen.com/point-of-sale/user-manuals">Documentación de Adyen - Guías de inicio rápido para las terminales de pago</a></p>
</div>

### Generar una clave API de Adyen

La **clave API de Adyen** se utiliza para autenticar las solicitudes de su
terminal de Adyen. Para generar una clave API, vaya a su cuenta de Adyen ‣
Desarrolladores ‣ Credenciales de API y **cree** nuevas credenciales o
seleccione las que ya **existen**. Haga clic en **Generar una clave API** y
guarde la clave para pegarla en el campo **Clave API de Adyen** de Konvergo ERP al
crear el método de pago.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://docs.adyen.com/development-resources/api-credentials#generate-api-key">Documentos de Adyen - Credenciales API</a>.</p></li>
</ul>
</div>

### Ubicar el identificador de terminal Adyen

El **identificador de terminal de Adyen** es el número de serie de la terminal
y se utiliza para identificar el hardware.

Para encontrar este número, vaya a su cuenta de Adyen ‣ Punto de Venta ‣
Terminales, seleccione la terminal que vinculará y guarde su número de serie,
después lo pegará en el campo **Identificador de terminal de Adyen** de Konvergo ERP
al crear el método de pago.

### Configurar las URL del evento

Para que Konvergo ERP sepa cuándo se realizó un pago, debe configurar las **URL de
eventos** de la terminal. Para ello:

  1. Inicie sesión en el [sitio web de Adyen](https://www.adyen.com/).

  2. Vaya al tablero de Adyen ‣ Punto de venta ‣ Terminales y seleccione la terminal conectada.

  3. Desde los ajustes de la terminal, haga clic en **Integraciones**.

  4. Establezca el campo **Cambiar a modo descifrado para editar esta configuración** en **Descifrado**.

  5. Haga clic en el **icono de lápiz** y escriba la dirección de su servidor, seguida por `/pos_adyen/notification` en el campo **URL de eventos**.

  6. Haga clic en **Guardar** en la parte inferior de la pantalla para guardar los cambios.

### Configure el método de pago

Habilite la terminal de pago en los [ajustes de la
aplicación](../../configuration#configuration-settings) y [cree el método
de pago relacionado](../../payment_methods). Establezca el tipo de diario
como **Banco** y seleccione **Adyen** en el campo **Usar una terminal de
pago**.

Por último, complete los campos obligatorios con su clave API de Adyen,
identificador de terminal de Adyen y **cuenta de comerciante de Adyen**.

![../../../../../_images/payment-method1.png](../../../../../_images/payment-
method1.png)

Ya que haya creado el método de pago, puede seleccionarlo en sus ajustes del
Punto de venta. Para hacerlo, vaya a los [ajustes del punto de
venta](../../configuration#configuration-settings), haga clic en
**Editar** y agregue el método de pago en la sección de **Pagos**.

## Pagar con una terminal de pago

Al procesar un pago, seleccione **Adyen** como método de pago. Revise el
importe y haga clic en **Enviar**. En cuanto se realice el pago, el estado
cambia a **Pago exitoso**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><div class="line-block">
<div class="line">En caso de que haya problemas de conexión entre Konvergo ERP y la terminal de pago, puede forzar el pago al hacer clic en <b>forzar hecho</b>, lo que le permite validar la orden.</div>
<div class="line">Esta opción solo está disponible después de recibir un mensaje de error que le informa que la conexión falló.</div>
</div>
</li>
<li><p>Para cancelar la solicitud de pago, haga clic en <b>cancelar</b>.</p></li>
</ul>
</div>

