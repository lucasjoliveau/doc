# Servicios de VoIP en Konvergo ERP con Axivox

## Introducción

Puede configurar el VoIP (Voz sobre protocolo de internet) de Konvergo ERP para que
funcione junto con [Axivox](https://www.axivox.com/). En ese caso, no se
necesita un servidor Asterisk ya que la infraestructura se aloja y se gestiona
en Axivox.

Para usar este servicio [contacte a Axivox](https://www.axivox.com/contact/)
para abrir una cuenta. Antes de hacerlo, compruebe que Axivox tenga cobertura
en su área y en las zonas a las que desea llamar.

## Configuración

Para configurar Axivox en Konvergo ERP, vaya a Aplicaciones y busque `VoIP` e instale
el módulo.

Después, vaya a Ajustes ‣ Ajustes generales ‣ Sección de integraciones y
complete el campo **Asterisk (VoIP)** :

  * **Dominio OnSIP** : configure el dominio que creó Axivox para la cuenta (por ejemplo, `yourcompany.axivox.com`)

  * **WebSocket** : escriba `wss://pabx.axivox.com:3443`.

  * **Entorno VoIP** : configurado como **Producción**

![Integración de Axivox como un proveedor de VoIP en la base de datos de
Konvergo ERP.](../../../../_images/voip-configuration.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Ingrese al dominio desde el panel administrativo de Axivox desde <a href="https://manage.axivox.com/">https://manage.axivox.com/</a>. Después de iniciar sesión en el portal, vaya a Usuarios ‣ Editar (a un lado de cualquier usuario) ‣ pestaña de identificadores SIP ‣ Dominio.</p>
</div>

### Configurar el usuario VoIP en Konvergo ERP

Después, el usuario estará configurado en Konvergo ERP, lo cual se debe hacer para
cada usuario de Axivox/Konvergo ERP que use VoIP.

En Konvergo ERP, vaya a Ajustes ‣ Usuarios y empresas ‣ Usuarios, después abra el
formulario del usuario que quiera y configure el VoIP (Voz sobre protocolo de
internet. En la pestaña de **Preferencias** llene la sección **Configuración
VOIP** :

  * **Nombre de usuario VoIP** / **Extensión del navegador** = **Nombre de usuario** OnSIP.

  * **Secreto VoIP** : (Axivox) **Contraseña SIP**.

  * **Número de dispositivo externo** : extensión de teléfono externo SIP

  * **Cómo realizar llamadas desde el móvil** : método para hacer llamadas en un dispositivo móvil

  * **Usuario de autorización OnSIP** : (Axivox) **nombre de usuario SIP**

  * **Llamadas de otro dispositivo** : opción para siempre transferir las llamadas telefónicas a un dispositivo auricular.

  * **Rechazar todas las llamadas entrantes** : opción para rechazar todas las llamadas entrantes

![Integración del usuario Axivox en las preferencias de usuario de
Konvergo ERP.](../../../../_images/odoo-user.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Ingrese al dominio desde el panel administrativo de Axivox desde <a href="https://manage.axivox.com/">https://manage.axivox.com/</a>. Después de iniciar sesión en el portal, vaya a Usuarios ‣ Editar (a un lado del usuario) ‣ pestaña de identificadores SIP ‣ Nombre de usuario SIP / contraseña SIP.</p>
<img alt="Credenciales SIP en el gestor Axivox." class="align-center" src="../../../../_images/manager-sip.png"/>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Al ingresar la <b>contraseña SIP</b> en la pestaña de <b>preferencias</b> del usuario <b>debe</b> escribir el valor, <b>no</b> puede copiar y pegarlo, si lo hace causará un <code>error 401 de rechazo del servidor</code>.</p>
</div>

