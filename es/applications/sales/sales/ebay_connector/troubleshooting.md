# Solución de problemas del Conector de eBay

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Para obtener más información relacionada al Conector de eBay puede visitar las siguientes páginas:</p>
<ul>
<li><p><a href="setup">Configuración del Conector de eBay</a></p></li>
<li><p><a href="manage">¿Cómo anunciar un producto?</a></p></li>
<li><p><a href="linking_listings">Vincular anuncios existentes</a></p></li>
</ul>
</div>

## Aceptar notificaciones de eliminación de cuenta

Desde septiembre de 2021, **eBay exige compatibilidad con las notificaciones
de eliminación o cierre de cuentas de clientes**. Por lo tanto, cuando eBay
recibe una solicitud de eliminación, todos los miembros de eBay deben
confirmar la recepción de la solicitud y tomar medidas adicionales si es
necesario.

Konvergo ERP tiene un punto de conexión de notificaciones para recibirlas, confirmar
la recepción de la solicitud y gestionar el primer conjunto de acciones para
anonimizar los detalles de la cuenta en _Contactos_ y eliminar el acceso del
cliente al portal.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de <a href="#ebay-subscribe-account-deletion-notifications"><span class="std std-ref">configurar de forma adecuada la suscripción a las notificaciones de eliminación de cuenta del mercado</span></a>, ya que tal vez eBay deshabilite la cuenta de eBay relacionada de forma temporal hasta completar la suscripción.</p>
</div>

### Verifique que su instalación de Konvergo ERP está actualizada

Es necesario que instale el módulo _Conector de eBay - Eliminación de cuenta_
para poder activar el punto de conexión. Si su base de datos de Konvergo ERP se creó
después de septiembre del 2021, el módulo se instala de forma automática y el
administrador puede continuar con el siguiente paso.

#### Actualizar Konvergo ERP a la versión más reciente

El punto de conexión de la notificación está disponible a través de un nuevo
módulo de Konvergo ERP. Para instalarlo, el administrador debe asegurarse de que su
código fuente de Konvergo ERP esté actualizado.

  * Si la empresa utiliza Konvergo ERP en Konvergo ERP.com o en una plataforma de Konvergo ERP.sh, su código ya está actualizado y puede continuar con el siguiente paso.

  * Si la empresa utiliza Konvergo ERP en una configuración local o a través de un partner, entonces el administrador debe actualizar la instalación tal como se describe en [esta página de la documentación](../../../../administration/on_premise/update), también puede contactar a un partner de integración.

#### Actualizar la lista de módulos disponibles

La instancia de Konvergo ERP debe _descubrir_ los nuevos módulos para que estén
disponibles en el menú de Aplicaciones.

Para hacerlo, active el [modo de
desarrollador](../../../general/developer_mode#developer-mode), y vaya a
Aplicaciones -> Actualizar lista de aplicaciones. Un asistente le solicitará
confirmar.

#### Instalar la actualización de «Conector de eBay - Eliminación de cuenta»

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p><b>Nunca</b> instale nuevos módulos en la base de datos de producción sin antes probarlos en un entorno duplicado o de prueba. Los clientes de Konvergo ERP.com pueden crear una base duplicada desde la página de gestión de bases de datos; si son usuarios de Konvergo ERP.sh, entonces los administradores deben usar una base de datos de prueba o una duplicada. En caso de que se trate de usuarios locales, el administrador debe usar un entorno de prueba. Contacte a su partner de integración para obtener más información sobre cómo probar un nuevo módulo en su configuración específica.</p>
</div>

Para instalar el módulo, vaya a Aplicaciones, elimine el filtro de
`Aplicaciones` y busque `eBay`. Si el módulo _Conector de eBay - Eliminación
de cuenta_ está disponible y aparece como «Instalado», su base de datos de
Konvergo ERP ya está actualizada y puede realizar el siguiente paso. Si aún no está
instalado, hágalo ahora.

### Recuperar los detalles de los puntos finales de comunicación de Konvergo ERP

Los detalles del punto de conexión están disponibles en Ventas ‣ Configuración
‣ Ajustes ‣ eBay. Primero ingrese valores de texto aleatorios en la **clave de
aplicación de producción** y la **clave de certificación de producción**. Haga
clic en **Generar token** para obtener el **token de verificación**.

![Generar un token de verificación en Konvergo ERP.](../../../../_images/generate-
token1.png)

### Recibir las notificaciones de eliminación de cuenta

vaya al [portal de desarrolladores de eBay](https://go.developer.ebay.com/).
Configure la eliminación de cuenta o los ajustes de notificaciones en eBay
desde `Hola, [nombre de usuario]` ubicado en la parte superior derecha de la
pantalla, luego vaya a **Alertas y notificaciones**.

![Vista general del tablero de Alertas y notificaciones de
eBay](../../../../_images/ebay-your-account.png)

Para recibir las notificaciones de eliminación o cierre, eBay necesita algunos
detalles:

  * Una **dirección de correo electrónico** para enviar notificaciones si no puede conectarse al punto de conexión.

  * Los _detalles del punto de conexión_ :

    * La URL del punto final de comunicación de la notificación de eliminación de la cuenta.

    * Un token de verificación

![Campos específicos para ingresar los detalles del punto final de
comunicación.](../../../../_images/ebay-notification-endpoint.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El administrador puede editar los dos últimos campos una vez que el campo de dirección de correo electrónico esté completo.</p>
</div>

### Verificar la conectividad con el punto final de comunicación

Después de configurar los detalles del punto de conexión obtenidos en el
tablero de eBay, considere realizar pruebas de conectividad con el botón
**Enviar notificación de prueba**.

> Debe recibir el siguiente mensaje de confirmación: «¡Se envió con éxito una
> notificación de prueba!»

![Botón para enviar notificaciones de prueba](../../../../_images/test-
notification.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="manage">¿Cómo anunciar un producto?</a></p></li>
<li><p><a href="linking_listings">Vincular anuncios existentes</a></p></li>
<li><p><a href="setup">Configuración del Conector de eBay</a></p></li>
</ul>
</div>

