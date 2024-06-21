# Dispositivos e integraciones

La VoIP se puede utilizar en muchos dispositivos distintos, como computadoras,
tabletas, celulares y otros. Es muy útil, pues reduce los costos y permite que
los empleados trabajen desde cualquier lugar del mundo siempre y cuando
cuenten con una conexión de internet de banda ancha.

La _VoIP_ de Konvergo ERP es compatible con el SIP (también conocido como protocolo de
inicio de sesión), así que se puede utilizar con _cualquier_ aplicación
compatible con SIP.

Este documento incluye el proceso para configurar la _VoIP_ de Konvergo ERP en
diferentes dispositivos e integraciones.

Todas las aplicaciones de Konvergo ERP están integradas entre sí, lo que permite que
los usuarios hagan clic en cualquier aplicación y programen una llamada como
una actividad en el chatter.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Por ejemplo, en la aplicación <em>CRM</em>, un usuario puede hacer clic en una oportunidad y luego en <b>Actividades</b> en el chatter.</p>
<p>A continuación, el usuario puede elegir <b>Llamada</b> y seleccionar una fecha en el campo <b>Fecha de vencimiento</b>.</p>
<p>La actividad aparece en el chatter una vez que hace clic en <b>Guardar</b>.</p>
<p>Si la <b>fecha de vencimiento</b> es la fecha de hoy, la actividad aparecerá en el widget de <abbr title="Voz sobre protocolo de internet">VoIP</abbr>.</p>
<img alt="Vista de los leads en CRM y la opción para programar una actividad en la aplicación Conversaciones de Konvergo ERP." class="align-center" src="../../../_images/crm-voip-widget.png"/>
</div>

## VoIP de Konvergo ERP en computadoras portátiles o de escritorio

El módulo y el widget _VoIP_ (Voz sobre protocolo de internet) de Konvergo ERP se
pueden utilizar desde cualquier navegador en una computadora portátil o de
escritorio. Solo haga clic en el icono **☎️ (teléfono)** ubicado en la esquina
superior derecha mientras se encuentre en su base de datos de Konvergo ERP, así
aparecerá el widget.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Para obtener más información sobre el uso del widget de <abbr title="Voz sobre protocolo de internet">VoIP</abbr> en una computadora de escritorio o portátil, consulte la siguiente documentación: <a href="voip_widget">Widget de VoIP</a>.</p>
</div>

## VoIP de Konvergo ERP en dispositivos móviles y tabletas

La aplicación _VoIP_ de Konvergo ERP se puede utilizar en tabletas y teléfonos móviles
a través de las aplicaciones de Konvergo ERP para Android o Apple iOS. También se
puede utilizar un navegador web móvil para acceder a la base de datos.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La aplicación de Konvergo ERP para Android y Apple iOS ya no recibe mantenimiento por parte de Konvergo ERP en los portales de Android y Apple, lo que significa que nuestro equipo de soporte solo se encarga de un alcance limitado en los tickets que reciben sobre Konvergo ERP en Android o en Apple iOS.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Aunque se pueden realizar llamadas salientes con Konvergo ERP desde un dispositivo móvil, tenga en cuenta que Konvergo ERP <b>no</b> es una aplicación completa de <abbr title="Voz sobre protocolo de internet">VoIP</abbr> y <b>no</b> suena al recibir llamadas. Si el usuario necesita estar disponible desde un dispositivo móvil en todo momento, entonces debería usar una aplicación como Zoiper. Aplicaciones similares a esa permanecen conectadas en segundo plano en todo momento.</p>
<p>Consulte la documentación de <a href="#voip-zoiper"><span class="std std-ref">Zoiper Lite</span></a> para obtener más información.</p>
</div>

Para acceder al widget de _VoIP_ de Konvergo ERP desde un dispositivo móvil o tableta
debe tocar el icono **☎️ (teléfono)** ubicado en la esquina superior derecha.
El widget aparecerá en la esquina inferior izquierda.

Cuando un usuario realiza una llamada desde una tableta a través la aplicación
móvil, se le solicita **permiso** para que la base de datos utilice el
micrófono. Haga clic en **Permitir** para continuar con la llamada y poder
utilizar el micrófono.

Este paso es **necesario** , no importa si está utilizando la aplicación móvil
de Konvergo ERP o un navegador web.

![Permitir que la base de datos acceda al micrófono.](../../../_images/allow-
mic.png)

Después, Konvergo ERP le preguntará cómo realizar la llamada. Las dos opciones
disponibles son **VoIP** o **Teléfono** (en caso de que la tableta este
habilitada para realizar y recibir llamadas). Seleccione la casilla junto a
**Recordar** si desea que esta decisión sea la que se use de forma
predeterminada después.

![La ventana en donde se le pregunta si desea utilizar VoIP o el teléfono del
dispositivo para realizar la llamada.](../../../_images/voip-phone.png)

La aplicación _VoIP_ de Konvergo ERP se ve de la siguiente forma en un dispositivo
móvil:

![Diseño de la aplicación VoIP y su visualización en un dispositivo
móvil.](../../../_images/voip-odoo-dashboard.png)

## Zoiper Lite

_Zoiper Lite_ es un softphone gratuito de VoIP y SIP que cuenta con funciones
de voz y video.

Para comenzar a usar la aplicación _Zoiper_ deberá descargarla en el
dispositivo desde la [página de descarga de
Zoiper](https://www.zoiper.com/en/voip-softphone/download/current).

La instalación más común se realiza en dispositivos móviles y este documento
menciona cómo configurar la aplicación _Zoiper_ en iOS. Las capturas de
pantalla y los pasos pueden variar según las condiciones de configuración.

Después de instalar la aplicación _Zoiper_ en el celular, ábrala y presione
**Ajustes**. Vaya a Cuentas y toque el icono **\+ (más)** para agregar una.

Si la cuenta de VoIP ya está configurada, entonces haga clic en **Sí**. Esto
indica que ya cuenta con un nombre de usuario y una contraseña para la cuenta.

![Configuración de la cuenta de Zoiper. La vista que aparece corresponde a un
dispositivo móvil.](../../../_images/account-settings-zoiper-group.png)

Presione **Selecciona un proveedor** y en la pantalla que aparece toque
**País** , allí presione en la esquina superior derecha para reducir la lista
de proveedores a un país específico. Elija el país del **proveedor** que está
configurando, búsquelo y selecciónelo.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si el proveedor que está configurando es <em>Axivox</em>, seleccione <b>Bélgica</b> y luego elija <b>Axivox</b>.</p>
</div> ![Configuración de la cuenta de Zoiper y elección de un
proveedor.](../../../_images/provider-zoiper-odoo.png)

Ingrese el **nombre de la cuenta** , **dominio** , **nombre de usuario** y
**contraseña** en las opciones del SIP. Toda esta información varía según la
cuenta.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para acceder a esta información desde el portal de <em>Axivox</em>, vaya a Usuarios ‣ Elija el usuario ‣ Editar ‣ Pestaña Identificadores SIP. El <b>Nombre de usuario SIP</b>, <b>Dominio</b>, <b>Contraseña SIP</b> y <b>Dirección del servidor proxy</b> se encuentran en esta pestaña.</p>
</div>  Campo de Zoiper | Campo de Avivox  
---|---  
Nombre de cuenta | _Puede ser cualquiera_  
Dominio | Dominio  
Nombre de usuario | Nombre de usuario SIP  
Contraseña | Contraseña SIP  
  
Una vez que haya ingresado esta información de la cuenta, haga clic en el
botón verde **Registrar** ubicado en la parte superior de la pantalla. Una vez
que se verifique la información de registro, _Zoiper_ mostrará un mensaje que
indica **Estado de registro: OK**.

En este punto, _Zoiper_ está configurado para realizar llamadas telefónicas a
través del servicio de VoIP.

![Configuración de la cuenta de Zoiper y un registro
exitoso.](../../../_images/sip-options-zoiper.png)

## Linphone

_Linphone_ es un softphone de VoIP y SIP de código abierto. Se utiliza para
llamadas de voz y video, mensajería (grupal e individual), así como para
conferencias telefónicas.

Para comenzar a usar la aplicación _Linphone_ , descárguela en el dispositivo
desde la [página de descarga de Linphone](https://new.linphone.org/technical-
corner/linphone?qt-technical_corner=2#qt-technical_corner).

La instalación más común se realiza en dispositivos móviles y este documento
menciona cómo configurar la aplicación _Linphone_ en iOS. Las capturas de
pantalla y los pasos pueden variar según las circunstancias.

Para comenzar a configurar _Linphone_ para su uso con un proveedor de SIP
primero deberá abrir la aplicación, aparecerá una pantalla de asistente.

En esta pantalla seleccione **Usar cuenta SIP**. Luego, en la siguiente
pantalla, escriba el **nombre de usuario** , **contraseña** , **dominio** y
**nombre para mostrar**. Una vez que haya terminado, presione **Iniciar
sesión**.

En ese momento _Linphone_ está listo para realizar llamadas. Debe aparecer un
botón verde en la parte superior de la pantalla de la aplicación con el texto
**Conectado**.

![Configuración de la cuenta de Linphone y un registro
exitoso.](../../../_images/linphone-odoo-setup.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p><em>Linphone</em> ofrece una variedad de aplicaciones para dispositivos móviles y de escritorio en sistemas operativos como Windows, Linux, Apple y Android. Además, como <em>Linphone</em> es un proyecto de código abierto, con frecuencia hay nuevas actualizaciones.</p>
<p>Consulte la <a href="https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/">página de documentación wiki de Linphone</a>.</p>
</div>

  *[VoIP]: Voz sobre protocolo de internet
  *[SIP]: Protocolo de inicio de sesión

