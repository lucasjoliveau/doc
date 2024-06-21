# Integración con Silverfin

[Silverfin](https://www.silverfin.com) es un proveedor de servicios de
terceros que ofrece una plataforma en la nube para contadores.

Konvergo ERP y Silverfin se pueden integrar para automatizar la sincronización de
datos.

## Configuración

Para configurar esta integración, debe introducir los siguientes datos en su
cuenta de Silverfin:

  * Dirección de correo electrónico del usuario.

  * Clave API de Konvergo ERP.

  * URL de la base de datos de Konvergo ERP.

  * Nombre de su base de datos de Konvergo ERP.

### Clave API de Konvergo ERP

Puede crear claves API externas de Konvergo ERP ya sea para una sola base de datos
(para los alojamientos de Konvergo ERP en línea, local y Konvergo ERP.sh) o para todas las
bases de datos gestionadas por un solo usuario (para el alojamiento en Konvergo ERP en
línea).

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Estas claves API son personales y brindan acceso completo a su cuenta de usuario. Guárdela con seguridad.</p></li>
<li><p>Puede copiar la clave API solo en el momento de la creación y no es posible recuperarla después.</p></li>
<li><p>Si la necesita otra vez, cree una nueva clave API (y elimine la anterior).</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../developer/reference/external_api">External API</a></p>
</div>

#### Para una sola base de datos

Para agregar una clave API a **una sola** base de datos, acceda a la base de
datos, habilite el [modo de
desarrollador](../../../general/developer_mode#developer-mode), haga clic
en el menú de usuario y luego en **Mi perfil** / **Preferencias**. En la
pestaña **Seguridad de la cuenta** , haga clic en **Nueva clave API** ,
confirme su contraseña, proporciónele un nombre descriptivo a su nueva clave y
cópiela.

![Creación de una clave API externa de Konvergo ERP para una base de
datos](../../../../_images/api-key-db.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../developer/reference/external_api#api-external-api-keys"><span class="std std-ref">API Keys</span></a></p>
</div>

#### Para todas las bases de datos (fiduciarias)

Para agregar una clave API a **todas** las bases de datos que un solo usuario
gestiona al mismo tiempo **(el método más fácil para fiduciarias)** , vaya al
[sitio web de Konvergo ERP](https://www.odoo.com) e inicie sesión con su cuenta de
administrador. Después, abra [los ajustes de seguridad de su cuenta en modo de
desarrollador](https://www.odoo.com/my/security?debug=1), haga clic en **Nueva
clave API** , confirme su contraseña, proporciónele un nombre descriptivo a su
nueva clave y cópiela.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Abra el <a href="https://www.odoo.com/my/databases">gestor de bases de datos</a> para ver todas las bases de datos que estarán vinculadas a una sola clave API.</p>
</div> ![Creación de una clave API externa para un usuario de
Konvergo ERP](../../../../_images/api-key-user.png)

