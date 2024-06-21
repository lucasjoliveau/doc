# Permisos de acceso

Los _permisos de acceso_ son permisos que determinan el contenido y las
aplicaciones a las que los usuarios pueden acceder y editar. En Konvergo ERP, estos
permisos se pueden configurar para usuarios individuales o para grupos de
usuarios. Limitar los permisos a solo aquellos usuarios que los necesitan
asegura que los usuarios no modificarán ni eliminarán nada a lo que no tengan
acceso.

**Solo** los _administradores_ pueden cambiar los permisos de acceso.

<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Los cambios a los permisos de acceso pueden afectar de forma perjudicial la base de datos. Esto incluye <em>admin impotente</em>, lo que significa que ningún usuario en la base de datos podrá cambiar los permisos de acceso. Le recomendamos que se ponga en contacto con un consultor de Konvergo ERP o con nuestro equipo de soporte antes de realizar cambios.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Un usuario <b>debe</b> tener permisos de acceso específicos de <em>Administración</em> configurados en su perfil de usuario para poder hacer cambios en los ajustes de otro usuario para derechos de acceso.</p>
<p>Para acceder a este función, vaya a  Ajustes ‣ Gestionar usuarios ‣ seleccione un usuario ‣ vaya a la pestaña Permisos de acceso ‣ vaya a la sección de Administración ‣ campo de Administración.</p>
<p>Una vez en este ajuste, un administrador existente <b>debe</b> cambiar el ajuste en el campo <b>Administración</b> a <b>Derechos de acceso</b></p>
<p>Una vez que termine, haga clic en <b>Guardar</b> para guardar los cambios e implementar al usuario como administrador.</p>
</div>

## Usuarios

Los derechos de acceso para [usuarios individuales](../users#users-add-
individual) se configuran cuando el usuario se agrega a la base de datos, pero
se pueden ajustar en cualquier momento en el perfil del usuario.

Para hacer cambios en los permisos de acceso del usuario, haga clic en el
usuario deseado para editar su perfil.

![Menú de los usuarios en la sección Usuarios y empresas de los Ajustes de
Konvergo ERP.](../../../_images/navigate-to-users-menu.png)

En la página de perfil del usuario, en la pestaña **Permisos de acceso**
deslícese hacia abajo para ver los permisos actuales.

Para cada aplicación, use el menú desplegable para seleccionar qué nivel de
permisos debería de tener un usuario. Las opciones varían por cada sección,
pero las más comunes son: **Vacío o ninguno** , **Usuario: solo mostrar
documentos propios** , **Usuario: todos los documentos** , o
**Administrador**.

El campo **Administración** en la pestaña **Permisos de acceso** tiene las
siguientes opciones: **Ajustes** o **Permisos de acceso**.

![El menú desplegable de la aplicación Venta para configurar el nivel de
permisos de un usuario.](../../../_images/user-permissions-dropdown-menu.png)

## Crear y modificar grupos

_Grupos_ son permisos específicos que se usan para gestionar los permisos de
acceso comunes para una gran cantidad de usuarios. Los administradores pueden
modificar los grupos existentes en Konvergo ERP, o crear nuevos para definir las
reglas para modelos dentro de una aplicación.

Para acceder a grupos, primero active el [modo de
desarrollador](../developer_mode#developer-mode) de Konvergo ERP, después valla a
Ajustes ‣ Usuarios y empresas ‣ Grupos.

![Menú de los grupos en la sección Usuarios y empresas de los Ajustes de
Konvergo ERP.](../../../_images/click-users-and-companies.png)

Para crear un nuevo grupo, haga clic en **Crear** en la página **Grupos**.
Después, en el formulario en blanco de grupo, seleccione una **Aplicación** y
complete el formulario del grupo (como se detalla más adelante).

Para modificar grupos existentes, haga clic en un grupo existente de la lista
que se muestra en la página **Grupos** y edite los contenidos del formulario.

Ingrese un **Nombre** para el grupo y marque la casilla de verificación a un
lado de **Compartir grupo** , si este grupo se creó para configurar permisos
de acceso para compartir datos con otros usuarios.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Siempre pruebe los ajustes que se están cambiando para asegurarse de que se están aplicando a los usuarios correctos.</p>
</div>

El formulario de grupo contiene varias pestañas para gestionar todos los
elementos del grupo. En cada pestaña, haga clic en **Agregar una línea** para
agregar una nueva hilera para usuarios o reglas y haga clic en el icono **❌
(eliminar)** para eliminar una hilera.

![Las pestañas en el formulario de grupos para modificar los ajustes del
grupo.](../../../_images/groups-form.png)

  * La pestaña **Usuarios** : enlista los usuarios que actualmente están en el grupo. Los usuarios que aparezcan en negro son aquellos que tienen permisos de administrador, mientras que los usuarios sin permisos de administrador aparecerán en azul. Haga clic en **Agregar una línea** para agregar usuarios a este grupo.

  * La pestaña **heredado** : heredado significa que los usuarios que se agreguen a este grupo se agregan también de forma automática a los grupos que se enlistan en esta pestaña. Haga clic en **Agregar una línea** para agregar grupos heredados.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Por ejemplo, si el grupo <em>Ventas/Administrador</em> tiene al grupo <em>Sitio web/Editor restringido</em> en su pestaña <b>Heredado</b>, entonces cualquier usuario que se agregue al grupo  <em>Ventas/Administrador</em> también recibirá acceso al grupo <em>Sitio web/Editor restringido</em> en automático.</p>
</div>

  * La pestaña **Menús** : define a qué menús o modelos puede acceder el grupo. Haga clic en **Agregar una línea** para agregar un menú en específico.

  * La pestaña **Vistas** : define a qué vistas en Konvergo ERP puede acceder el grupo. Haga clic en **Agregar una línea** para agregar una vista al grupo.

  * La pestaña **Permisos de acceso** : enlista el primer nivel de permisos (modelos) a los que este grupo tiene permisos de acceso. Haga clic en **Agregar una línea** para vincular permisos de acceso a este grupo. En esta pestaña la columna **Modelo** representa el nombre común del menú o modelo y la columna **Nombre** representa el nombre técnico que se le da a dicho modelo. Para cada modelo, active las siguientes opciones como lo crea necesario:

    * **Lectura** : los usuarios pueden ver los valores existentes del objeto.

    * **Editar** : los usuarios pueden editar los valores existentes del objeto.

    * **Crear** : los usuarios pueden crear nuevos valores para el objeto.

    * **Eliminar** : los usuarios pueden borrar borrar los valores para el objeto.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Primero intente buscar el nombre común del modelo en el menú desplegable de la columna <b>Modelo</b>. El nombre técnico del <b>Modelo</b> puede encontrarse al expandir el nombre común del modelo, lo cual se hace al hacer clic en el icono <b>(enlace externo)</b>.</p>
<p>También puede acceder al nombre técnico del modelo en <a href="../developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a>.</p>
<p>En un formulario, vaya a cualquier campo y pase el cursor por encima del nombre del campo. Al hacer esto, aparecerá una caja con información de backend con el nombre específico del <b>Objeto</b> en el backend. Este es el nombre técnico del modelo que se debe agregar.</p>
<img alt="Información técnica que se muestra en el campo de un modelo, con el objeto resaltado." class="align-center" src="../../../_images/technical-info.png"/>
</div>

  * **Reglas de registro** : enlista la segunda capa de edición y permisos de visualización. Las **reglas de registro** sobreescriben, o hacen más precisos, los permisos de acceso del grupo. Haga clic en **Agregar una línea** para agregar una regla de registro a este grupo. Por cada regla, seleccione los valores para las siguientes opciones:

    * **Postúlate para lectura**.

    * **Aplicar para edición**.

    * **Aplicar para crear**.

    * **Aplicar para borrar**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las reglas de registro se escriben usando un <em>dominio</em> o condiciones que filtran la información. Una expresión de dominio es una lista de estas condiciones, por ejemplo:</p>
<p><code>[('mrp_production_ids', 'in', user.partner_id.commercial_partner_id.production_ids.ids)]</code></p>
<p>Esta regla de registro existe ara activar las advertencias de consumo de MRP para subcontratistas.</p>
<p>Konvergo ERP tiene una librería de reglas de registro preconfiguradas para facilitar el uso. Los usuarios que no sepan de dominos (o expresiones de dominos) deben ponerse en contacto con un consultor de Konvergo ERP o con el equipo de soporte de Konvergo ERP antes de hacer estos cambios.</p>
</div>

## Modo de superusuario

_El modo de superusuario_ permite que el usuario omita las reglas de registro
y los permisos de acceso. Para activar el _modo de superusuario_ primero debe
activar el [modo de desarrollador](../developer_mode#developer-mode).
Después, navegue al menú de _depuración_ , el cual se representa con el icono
**🪲 (bug)** , que se ubica en la parte superior.

Finalmente, en la parte inferior del menú, haga clic en **Convertirse en
superusuario**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Solo los usuarios que tengan el permiso de acceso <em>Ajustes</em> en la sección <em>Administración</em> de los <em>Permisos de acceso</em> (en su perfil de usuario) tienen permitido ingresar al <em>modo de superusuario</em>.</p>
</div> <div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p><em>El modo de superusuario</em> permite saltarse las reglas de registro y los derechos de acceso, por lo que debe usarse con mucha precaución.</p>
<p>Es probable que al salir del <em>modo de superusuario</em> los usuarios no puedan ingresar a la base de datos debido a los cambios realizados. Esto puede causar un <em>admin impotente</em>, o un admin que no puede cambiar los permisos de acceso o los ajustes.</p>
<p>En este caso, se debe poner en contacto con el soporte de Konvergo ERP mediante un <a href="https://www.odoo.com/help">nuevo ticket de ayuda</a>. El equipo de soporte puede restaurar el acceso con un inicio de sesión de soporte.</p>
</div>

Para salir del _modo de superusuario_ cierre a sesión de la cuenta haciendo
clic en el nombre de usuario **Konvergo ERPBot** que se encuentra en la esquina
superior derecha. Después, seleccione la opción **Cerrar sesión**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Otra forma de activar el <em>modo superusuario</em> es iniciar sesión como un superusuario. Para hacerlo, vaya a la pantalla de inicio de sesión e ingrese el <b>correo electrónicol</b> y la <b>contraseña</b> adecuados.</p>
<p>En lugar de hacer clic en <b>iniciar sesión</b>, haga clic en <b>iniciar sesión como superusuario</b>.</p>
</div>

