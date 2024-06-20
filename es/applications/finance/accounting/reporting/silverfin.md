# Integración con Silverfin

[Silverfin](https://www.silverfin.com) es un proveedor de servicios de
terceros que ofrece una plataforma en la nube para contadores.

Odoo y Silverfin se pueden integrar para automatizar la sincronización de
datos.

## Configuración

Para configurar esta integración, debe introducir los siguientes datos en su
cuenta de Silverfin:

  * Dirección de correo electrónico del usuario.

  * Clave API de Odoo.

  * URL de la base de datos de Odoo.

  * Nombre de su base de datos de Odoo.

### Clave API de Odoo

Puede crear claves API externas de Odoo ya sea para una sola base de datos
(para los alojamientos de Odoo en línea, local y Odoo.sh) o para todas las
bases de datos gestionadas por un solo usuario (para el alojamiento en Odoo en
línea).

Importante

  * Estas claves API son personales y brindan acceso completo a su cuenta de usuario. Guárdela con seguridad.

  * Puede copiar la clave API solo en el momento de la creación y no es posible recuperarla después.

  * Si la necesita otra vez, cree una nueva clave API (y elimine la anterior).

Ver también

[External API](../../../../developer/reference/external_api.html)

#### Para una sola base de datos

Para agregar una clave API a **una sola** base de datos, acceda a la base de
datos, habilite el [modo de
desarrollador](../../../general/developer_mode.html#developer-mode), haga clic
en el menú de usuario y luego en Mi perfil / Preferencias. En la pestaña
Seguridad de la cuenta, haga clic en Nueva clave API, confirme su contraseña,
proporciónele un nombre descriptivo a su nueva clave y cópiela.

![Creación de una clave API externa de Odoo para una base de
datos](../../../../_images/api-key-db.png)

Ver también

[API Keys](../../../../developer/reference/external_api.html#api-external-api-
keys)

#### Para todas las bases de datos (fiduciarias)

Para agregar una clave API a **todas** las bases de datos que un solo usuario
gestiona al mismo tiempo **(el método más fácil para fiduciarias)** , vaya al
[sitio web de Odoo](https://www.odoo.com) e inicie sesión con su cuenta de
administrador. Después, abra [los ajustes de seguridad de su cuenta en modo de
desarrollador](https://www.odoo.com/my/security?debug=1), haga clic en Nueva
clave API, confirme su contraseña, proporciónele un nombre descriptivo a su
nueva clave y cópiela.

Truco

Abra el [gestor de bases de datos](https://www.odoo.com/my/databases) para ver
todas las bases de datos que estarán vinculadas a una sola clave API.

![Creación de una clave API externa para un usuario de
Odoo](../../../../_images/api-key-user.png)

