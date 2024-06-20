# Uso de canales para la comunicación en equipo

Use los canales en la aplicación _Conversaciones_ de Odoo para organizar
conversaciones entre equipos, departamentos, proyectos o cualquier otro grupo
que necesite mantener una comunicación constante. Con los canales, los
empleados se podrán comunicar dentro de espacios especializados dentro de la
base de Odoo. Podrán hablar de temas específicos, actualizaciones y las
noticias más recientes sobre la organización.

## Canales públicos y privados

Un canal _público_ es un canal que todo el mundo puede ver, mientras que el
canal _privado_ solo es visible para los usuarios que recibieron una
invitación. Para crear un canal nuevo, vaya a la aplicación Conversaciones y
después haga clic en el icono ➕ (más) que se encuentra junto al encabezado
Canales en el menú del lado izquierdo. Después de escribir el nombre del canal
aparecerán dos opciones. La primera opción es un canal con un símbolo de
etiqueta (`#`) que indica que se trata de un canal público. La segunda opción
es un canal con un candado (`🔒`) que indica que es un canal privado.
Seleccione el canal que mejor se adapte a sus necesidades de comunicación.

![Vista de la barra lateral de la aplicación Conversaciones y la creación de
un canal en la misma.](../../../_images/public-private-channel.png)

Truco

Un canal público es mejor cuando muchos empleados necesitan acceder a
información (como anuncios de la empresa), mientras que un canal privado es
mejor cuando la información deba limitarse a grupos específicos (como un
departamento específico).

### Opciones de configuración

El Nombre del grupo, la Descripción y los ajustes de Privacidad del canal se
pueden modificar desde los ajustes del canal, a los que puede acceder si hace
clic en el icono ⚙️ (engranaje) en el menú lateral, junto al nombre del canal.

![Imagen del formulario de los ajustes del canal en la aplicación
Conversaciones.](../../../_images/channel-settings.png)

#### Pestañas de privacidad y miembros

Con la opción ¿Quién puede seguir las actividades del grupo? podemos controlar
qué grupos pueden acceder al canal.

Nota

Si permitimos que Todos sigan un canal privado, otros usuarios podrán ver el
canal y unirse a él, como lo harían con un canal público.

Si se elige Solo personas invitadas debe especificar en la pestaña Miembros
quiénes son los usuarios invitados. También puede invitar miembros desde el
tablero principal de la aplicación _Conversaciones_. Solo tiene que
seleccionar el canal, hacer clic en el símbolo _agregar usuario_ en la esquina
superior derecha del tablero y haga clic en Invitar a canal una vez que agregó
a todos los usuarios deseados.

![Imagen de la opción "invitar miembros" en la aplicación Conversaciones de
Odoo.](../../../_images/invite-channel.png)

Si se elige la opción Grupo de usuarios seleccionado aparecerá una opción para
agregar un Grupo autorizado, así como las opciones Grupos de suscripción
automática y Suscripción automática a departamentos.

La opción Grupos de suscripción automática agregará usuarios que sean miembros
de ese grupo específico como seguidores. En otras palabras, aunque la opción
Grupo autorizado limita qué usuarios pueden acceder al canal, en Grupos de
suscripción automática agrega a un usuario como miembro siempre y cuando sean
parte de un grupo de usuarios. Lo mismo pasa con Suscripción automática a
departamentos.

## Barra de búsqueda rápida

Una vez que haya fijado al menos 20 canales, mensajes directos, o
conversaciones de chat en vivo (si tiene instalado el módulo _Chat en vivo_ en
la base de datos) se mostrará una barra de Búsqueda rápida…. Esta función le
permitirá filtrar sus conversaciones y encontrar información relevante.

![Imagen de la barra lateral de la aplicación Conversaciones de Odoo donde se
resalta la barra de búsqueda rápida.](../../../_images/quick-search.png)

### Encontrar canales

Haga clic en el icono de configuración ⚙️ (engranaje), situado en la barra
lateral izquierda, a la derecha del elemento de menú desplegable CANALES. Al
hacerlo, aparecerá una vista en mosaico con todos los canales públicos
disponibles. Los usuarios pueden unirse o abandonar canales en esta pantalla
gracias a los botones UNIRSE o ABANDONAR que aparecen en las casillas de los
canales.

También existe la posibilidad de aplicar filtros y guardarlos para después. La
función Buscar… acepta caracteres comodín mediante el subrayado [ `_` ]. Puede
guardar búsquedas específicas utilizando el menú desplegable Favoritos ‣
Guardar búsqueda actual.

![Vista de un canal buscado a través de filtros en la aplicación
Conversaciones](../../../_images/filter.png)

## Vincular un canal en el chatter

Puede vincular los canales en el chatter (nota de registro) de Odoo. Si desea
hacerlo, escriba `#` seguido del nombre del canal. Haga clic o presione enter
en el nombre del _canal_. Al registrar la nota aparecerá un enlace al canal.
Después de hacer clic en el enlace aparecerá una ventana de chat en la esquina
inferior derecha con la conversación del canal.

Los usuarios pueden contribuir a este canal de grupo (ya sea público o
privado) escribiendo mensajes en la ventana y haciendo clic en _enter_.

![Canal vinculado en el chatter con el canal abierto en el cuadrante inferior
derecho.](../../../_images/chatter-channel.png)

Ver también

  * [Conversaciones](../discuss.html)

  * [Actividades](../../essentials/activities.html)

