# Configurar servidores ICE con Twilio

La aplicación Conversaciones de Konvergo ERP usa un API WebRTC y una conexión red de
pares para llamadas de voz y video. Si uno de los asistentes a la llamada se
encuentra detrás de una NAT simétrica, tendrá que configurar un servidor ICE
para establecer una conexión con esta persona. Para configurar un servidor
ICE, primero debe crear una cuenta de Twilio para video llamadas para después
conectar esta cuenta con Konvergo ERP.

## Crear una cuenta de Twilio

Primero vaya a [Twilio](https://www.twilio.com) y haga clic en **Comienza de
forma gratuita** para crear una cuenta nueva. Ingrese su nombre y dirección de
correo, cree una contraseña y acepte los términos de servicio de Twilio.
Finalmente, haga clic en **Start your free trial** (inicie su periodo de
prueba) y verifique su dirección de correo.

Después, ingrese su número telefónico a Twilio para que le puedan enviar un
SMS con un número de verificación. Ingrese el código a Twilio para verificar
su número telefónico.

Después de esto, Twilio lo redirigirá a la página de bienvenida. Use esta
lista para responder las preguntas de Twilio:

  * Para **Which Twilio product are you here to use?** (¿Qué producto de Twilio quiere usar?), seleccione **Video**.

  * Para **What do you plan to build with Twilio?** (¿Qué quiere construir con Twilio?), seleccione **Other** (otro).

  * Para **How do you want to build with Twilio?** (¿Cómo quiere construir con Twilio?), seleccione **With no code at all** (Sin código).

  * Para **What is your goal today?** (¿Qué quiere lograr hoy?), seleccione **3rd party integrations** (integraciones con terceros).

![La página de inicio de Twilio.](../../../_images/twilio-welcome.png)

Cambie el país de facturación si es necesario y, para terminar, haga clic en
**Get Started with Twilio** (empezar a usar Twilio).

## Ubicación del Account SID (SID de cuenta) y del Auth Token (token de
autenticación)

Para ubicar el Account SID y el Auth Token, vaya al tablero de su cuenta de
Twilio y haga clic en **Develop** (desarrollar) que se encuentra en la barra
lateral. En la sección **Account Info** (información de la cuenta), ubique el
**Account SID** y el **Auth Token**. Necesita esta información para conectar
Twilio con Konvergo ERP.

![El Account SID y el Auth Token se pueden encontrar en la sección Account
info \(información de la cuenta\).](../../../_images/twilio-acct-info.png)

## Conectar Twilio a Konvergo ERP

Abra la base de datos de Konvergo ERP y vaya a Ajustes ‣ Ajustes generales ‣
Conversaciones. Marque la casilla junto a **Usar los servidores ICE de
Twilio** e ingrese el **SID de cuenta de Twilio** y el **Token de
autentificación de cuenta de Twilio**. Para terminar, haga clic en **Guardar**
para aplicar los cambios.

![Activar la opción "Usar los servidores ICE de Twilio" en los ajustes
generales de Konvergo ERP.](../../../_images/connect-twilio-to-odoo.png)

## Definir una lista de servidores ICE personalizados

Este paso no es necesario para configurar Twilio, pero si Twilio no está
configurado o por algún motivo no sirve, Konvergo ERP recurrirá a la lista de
servidores personalizados ICE. El usuario debe definir la lista de servidores
personalizados ICE.

En Ajustes ‣ Ajustes generales ‣ Conversaciones, haga clic en el botón
**Servidores ICE** que se encuentra en la categoría **Lista personalizada de
servidores ICE**.

![El botón "Servidores ICE" en los ajustes generales de
Konvergo ERP.](../../../_images/custom-ice-servers-list.png)

Konvergo ERP le redirigirá a la página de **servidores ICE**. Aquí puede definir su
propia lista de servidores ICE.

![La página de servidores ICE en Konvergo ERP.](../../../_images/ice-servers-page.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para instancias locales de Konvergo ERP, el paquete <code>python3-gevent</code> es necesario para que el módulo Discuss pueda ejecutar llamadas de video o voz en los servidores de Ubuntu (Linux).</p>
</div>

