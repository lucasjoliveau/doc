# Ogone

[Ogone](https://www.ingenico.com/), también conocido como **Servicios de pago
Ingenico** es una empresa con sede en Francia que proporciona la tecnología
involucrada en transacciones electrónicas seguras.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
<li><p><a href="https://epayments-support.ingenico.com/get-started/">Documentación de Ogone</a>.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El proveedor Ogone ya es obsoleto. En su lugar, se le recomienda usar <a href="stripe">Stripe</a>.</p>
</div>

## Coonfiguración en Ogone

### Cree un usuario API

Inicie sesión en su cuenta de Ogone y vaya a la pestaña **Configuración**.

Necesita crear un **Usuario API** para usarlo al momento de realizar
transacciones en Konvergo ERP. Si bien puede usar su cuenta principal para hacerlo,
usar un **Usuario API** le garantiza que si las credenciales utilizadas en
Konvergo ERP se filtran, no se podrá acceder a las configuraciones de Ogone. Además,
las contraseñas para los **Usuarios API ** no necesitan actualizarse
constantemente, a diferencia de los usuarios normales.

Para crear un **Usuario API** , vaya a Configuración ‣ Usuarios y haga clic en
**Usuario nuevo**. Se deben configurar los siguientes campos:

  * **ID de ususario** : puede escoger el que quiera.

  * **Nombre del usuario, correo electrónico y zona horaria** : puede ingresar la información que desee.

  * El **Perfil** : debe estar establecido como **Administrador**.

  * La casilla **Usuario especial para API** : debe estar seleccionada.

Después de crear su usuario, debe generar una contraseña. Guardela junto con
el **ID del usuario** pues los necesitara después durante la configuración.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si ya tiene un usuario configurado, asegúrese de que esté activado sin errores. Si no es el caso, simplemente haga clic en el botón de  <b>Activar(Errores)</b> para resetear el usuario.</p>
</div>

### Configure Ogone para Konvergo ERP

Ogone debe estar configruado para aceptar pagos desde Konvergo ERP. Vaya a
Configuración ‣ Información técnica ‣ Parámetros de seguridad globales,
seleccione **SHA-512** como **Algoritmo hash** y **UTF-8** como **codificación
de caracter**. Luego, vaya a la pestaña **Datos y verificación de origen** en
la misma página y deje el campo de la URL sección **Comercio electrónico y
entrada de alias** vacía.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si necesita usar otro algoritmo, como <code>sha-1</code> o <code>sha-256</code>, dentro de Konvergo ERP, active el <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">modo desarrollador</span></a> y vaya a la página de <b>Proveedores de pago</b> en Contabilidad ‣ Configuración ‣ Proveedores de pago. Haga clic en <b>Ogone</b>, y en la pestaña <b>Credenciales</b>, seleccione el algoritmo que desea utilizar en el campo <b>Función hash</b>.</p>
</div>

Ahora debe generar farses de contraseña **SHA-IN**. Las frases de contraseña
**SHA-IN** y **SHA-OUT** se usan para firmar digitalmente las solicitudes de
transacciones y las respuestas entre Konvergo ERP y Ogone. Al usar estas frases de
contraseña secretas y el algoritmo `sha-1`, ambos sistemas pueden garantizar
que la información que reciben del otro no fue alterada o tocada.

Ingrese la misma frase de contraseña **SHA-IN** tanto en **Cheques para
comercio electrónico y entrada de alias** como en **Cheques para DirectLink y
Lote (Automático)**. Puede dejar el campo de la dirección IP vacío.

Sus frases de contraseña **SHA-IN** y **SHA-OUT** deben ser diferentes y deben
contener entre 16 y 32 caracteres. Asegúrese de usar las mismas frases de
contraseña **SHA-IN** y **SHA-OUT** durante toda la configuración de Ogone,
pues Konvergo ERP solo permite una sola frase de contraseña para **SHA-IN** y otra
para **SHA-OUT**.

Para obtener la clave **SHA-OUT** , inicie sesión en su cuenta de Ogone, vaya
a Configuración ‣ Información técnica ‣ Retroalimentación de la transacción ‣
Todos los modos de envío de transacción, y ibtenga o vuelva a generar su
**Clave API** y **Clave de cliente**. Ponga atención y copie su clave API pues
no se le permitirá obtenerla después sin generar una nueva.

Al terminar, vaya a Configuración ‣ Información técnica ‣ Retroalimentación de
transacción y seleccione las siguientes opciones:

  * Los campos **URL** para **Redireccionar HTTP en el navegador** pueden quedarse vacíos, pues Konvergo ERP especificará estas URL para cada solicitud de transacción.

  * **Me gustaría recibir los parámetros de retroalimentación de las transacciones en las URL de redirección** : debe estar seleccionado.

  * **Solicitud servidor a servidor HTTP directa** : debe estar establecido en `En línea pero cambiar a solicitud diferida cuando la solicitud en línea falle`.

  * Ambos campos **URL** deben contener esta misma URL, reemplazando `<example>` por su base de datos: `https://<example>/payment/ogone/return`.

  * Los **Parámetros dinámicos de comercio electrónico** deben contener los siguientes valores: `ALIAS`, `AMOUNT`, `CARDNO`, `CN`, `CURRENCY`, `IP`, `NCERROR` `ORDERID`, `PAYID`, `PM`, `STATUS`, `TRXDATE`. Se pueden incluir otros parámetros (si tiene otra integración con Ongone que lo requiera), pero no se recomienda.

  * En la sección **Todos los modos de envío de transacciones** , llene el campo de frase de contraseña **SHA-OUT** y desactive `Solicitud HTTP para cambio de estado`.

Para permitir que sus clientes guarden las credenciales de sus tarjetas de
crédito para usarlas en el futuro, vaya a Configuración ‣ Alias ‣ Mi
información de alias. Desde esta pestaña, puede configurar cómo es que el
usuario puede guardar los detalles de su tarjeta, por cuánto timpo se guarda
dicha información, si debe aparecer una casilla para guaradar la información
de la tarjeta, etc.

## Ajustes en Konvergo ERP

Para configurar Ogone en Konvergo ERP, vaya a Contabilidad ‣ Configuración ‣
Proveedores de pago y abra el proveedor Ogone. En la pestaña **Credenciales**
, ingrese el **PSPID** de su cuenta de Ogone, y llene los otros campos como
están configurados en su Portal de Ogone.

