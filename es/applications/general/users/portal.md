# Acceso al portal

Se le brinda acceso al portal a los usuarios que necesitan poder ver
documentos o información en específico en una base de datos de Odoo.

Algunos de los casos de uso más comunes en los que se necesita brindar acceso
al portal incluyen permitir a los clientes ver o leer alguno de los siguientes
elementos en Odoo:

  * leads/oportunidades

  * cotizaciones/órdenes de venta

  * órdenes de compra

  * facturas de cliente o de proveedor

  * proyectos

  * tareas

  * hojas de horas

  * tickets

  * firmas

  * suscripciones

Nota

Los usuarios del portal solo tienen derechos de acceso de lectura/vista y no
pueden editar ningún documento en la base de datos.

## Otorgar acceso al portal a sus clientes

En el tablero principal de Ododo seleccione la aplicación Contactos. Si aún no
se ha creado el contacto en la base de datos, haga clic en el botón Crear,
ingrese la información del contacto y luego haga clic en guardar. De lo
contrario, elija un contacto existente y haga clic en el menú desplegable
acción que se encuentra en la parte superior central de la interfaz.

![La aplicación Contactos muestra cómo otorgar acceso al portal a los
usuarios.](../../../_images/grant-portal-access.png)

Luego seleccione la opción otorgar acceso al portal. Aparecerá una ventana
emergente con tres campos:

  * Contacto: el nombre del contacto registrado en la base de datos de Odoo

  * Correo electrónico: la dirección de correo electrónico que el contacto utilizará para iniciar sesión en el portal

  * En el portal: si el usuario tiene acceso al portal o no

Para otorgar acceso al portal primero debe introducir el correo electrónico
que el contacto utilizará para iniciar sesión en el portal. Después,
seleccione la casilla en la columna en el portal. Si lo desea, puede agregar
texto al mensaje de invitación que el contacto recibirá. Haga clic en aplicar
para terminar.

![Se debe completar la dirección de correo electrónico del contacto y su
casilla correspondiente antes de enviar una invitación al
portal.](../../../_images/add-contact-to-portal.png)

Se enviará un correo electrónico a la dirección especificada, la cual indica
que el contacto ahora es un usuario del portal de esa base de datos de Odoo.

Truco

Para otorgar acceso al portal a varios usuarios a la vez vaya a un contacto de
empresa y haga clic en Acción ‣ Otorgar acceso al portal para ver una lista de
todos los contactos relacionados con la empresa. Seleccione la casilla en la
columna en el portal para todos los contactos que necesitan acceso al portal y
luego haga clic en aplicar.

Nota

Puede revocar el acceso al portal en cualquier momento. Para hacerlo debe ir
al contacto, hacer clic en Acción ‣ Otorgar acceso al portal y anular la
selección de la casilla en la columna en el portal y hacer clic en aplicar.

## Cambiar el nombre de usuario del portal

Es probable que un usuario del portal quiera modificar su forma de iniciar
sesión en algún momento, esto es posible y lo puede realizar cualquier usuario
de la base de datos con permisos de acceso de administrador. El siguiente
proceso describe las instrucciones necesarias para cambiar la manera de
iniciar sesión.

Ver también

[Consulte la documentación sobre la configuración de los permisos de
acceso](access_rights.html).

Primero vaya a Ajustes ‣ Usuarios. Después, en Filtros, seleccione Usuarios
del portal, o seleccione Agregar filtro personalizado y realice la siguiente
configuración Grupos > contiene > `portal`. Después de hacer esta selección,
busque (y abra) el usuario de portal que tiene que editar.

Después, haga clic en Editar (si es necesario), haga clic en el campo
Dirección de correo y después haga los cambios necesarios a este campo. El
campo dirección de correo se usa para ingresar al portal de Odoo.

Nota

Cambiar la dirección de correo (o inicio de sesión) solo cambia el _nombre de
usuario_ de inicio de sesión en el portal del cliente.

Para cambiar el correo de contacto debe hacerlo desde la plantilla en la
aplicación _Contactos_. También el cliente puede cambiar su correo
directamente desde el portal, pero los datos de inicio de sesión **no** se
pueden cambiar. vea cómo cambiar la información del cleinte.

## Cambios en el portal del cliente

El cliente puede querer realizar cambios a su información de contacto,
contraseña y seguridad o información de pago vinculada a su portal de
contacto. Estos cambios los puede realizar el cliente desde el portal y aquí
le explicaremos cómo.

### Cambiar la información del cliente

Primero ingrese el nombre de usuario y la contraseña en la página de inicio de
sesión de la base de datos de la cuenta de portal del usuario. Al iniciar
sesión aparecerá el tablero del portal y varios documentos de las aplicaciones
instaladas en Odoo.

Ver también

Documentación de acceso del portal.

Ahora, en la esquina superior derecha del portal, haga clic en el botón
Editar, a un lado de la sección Detalles. Después, cambie la información
pertinente y haga clic en Confirmar.

### Cambiar contraseña

Primero ingrese el nombre de usuario y la contraseña en la página de inicio de
sesión de la cuenta de portal del usuario. Cuando inicie sesión aparecerá el
tablero del portal.

Para modificar la contraseña de su cuenta de Odoo.com, haga clic en el enlace
Editar los ajustes de seguridad que se encuentra en la sección Seguridad de la
cuenta. Haga los cambios necesarios, escriba su contraseña actual, la nueva
contraseña y vuelva a escribirla en el campo de abajo para verificar la
contraseña nueva. Por último, haga clic en Cambiar la contraseña para
completar el cambio.

Nota

Si un cliente desea modificar los datos de inicio de sesión, como se mencionó
con anterioridad, contacte al punto de contacto de la base de datos de Odoo.
Consulte la documentación relacionada sobre cómo cambiar el nombre de usuario
del portal.

Nota

Las contraseñas para los usuarios del portal y los usuarios de Odoo.com siguen
siendo distintas, incluso si usan la misma dirección de correo electrónico.

### Agregar autenticación de dos factores

Primero ingrese el nombre de usuario y la contraseña en la página de inicio de
sesión de la cuenta de portal del usuario. Cuando inicie sesión aparecerá el
tablero del portal.

Si desea activar la autenticación de dos factores (A2F) para acceder al
portal, haga clic en el enlace Editar los ajustes de seguridad dentro de la
sección Seguridad de la cuenta.

Haga clic en Habilitar la autenticación de dos factores para activar la A2F.
Confirme la contraseña actual del portal en el campo Contraseña, luego haga
clic en Confirmar contraseña y después active la A2F en una aplicación para
A2F como Google Authenticator, Authy o alguna otra. Allí deberá escanear el
código QR o escribir el código de verificación.

Por último, haga clic en Habilitar la autenticación de dos factores para
completar la configuración.

### Cambiar información de pago

Primero ingrese el nombre de usuario y la contraseña en la página de inicio de
sesión de la cuenta de portal del usuario. Cuando inicie sesión aparecerá el
tablero del portal.

Si e cliente quiere gestionar las opciones de pago, vaya a gestionar métodos
de pago en el menú de la derecha. Después, agregue la nueva información de
pago y seleccione Agregar nueva tarjeta.

  *[A2F]: Autenticación de dos factores

