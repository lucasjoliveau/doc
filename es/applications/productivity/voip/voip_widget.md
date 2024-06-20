# Widget de VoIP

El widget _VoIP_ es un complemento al que los usuarios de Odoo pueden acceder
mediante el módulo _VoIP_. Se utiliza para incorporar la telefonía virtual en
la base de datos y es el centro de control para hacer y gestionar llamadas en
Odoo.

## Llamadas telefónicas

Para realizar llamadas telefónicas mientras se encuentra en la base de datos
de Odoo, haga clic en el icono ☎️ (teléfono) ubicado en la barra superior de
navegación.

Al hacer clic, el widget emergente VoIP aparece en la esquina inferior derecha
de la base de datos de Odoo. Este widget permite que los usuarios naveguen por
la base de datos y que al mismo tiempo puedan hacer y recibir llamadas.

El widget VoIP suena y muestra una notificación cuando recibe llamadas en
Odoo. Para cerrar el widget, haga clic en el icono X (cerrar) ubicado en la
parte superior derecha de la pantalla del widget.

Nota

El número VoIP es el que le proporcionó Axivox. Inicie sesión en
<https://manage.axivox.com/> y después vaya a Usuarios ‣ Número saliente
(columna) para consultarlo.

![Llamada VoIP en Odoo.](../../../_images/call.png)

## Solución de problemas

Truco

Si aparece el mensaje de error relacionado a _parámetros faltantes_ en el
widget _VoIP_ de Odoo, asegúrese de actualizar la ventana correspondiente e
inténtelo de nuevo.

![El mensaje de error relacionado a un parámetro faltante en el softphone de
Odoo.](../../../_images/missing-parameter.png)

Truco

Si aparece el mensaje de error relacionado a un _número incorrecto_ en el
widget _VoIP_ de Odoo, asegúrese de utilizar el formato internacional. Debe
comenzar con el signo \+ (más), seguido del código internacional del país.

Por ejemplo, en el número +16506913277, el `+1` corresponde al prefijo
internacional para Estados Unidos.

![Mensaje de error relacionado a un número incorrecto en el softphone de
Odoo.](../../../_images/incorrect-number.png)

## Pestañas

Hay tres pestañas disponibles en el widget _VoIP_ que corresponden a Reciente,
Siguientes actividades y Contactos y se usan para gestionar las llamadas y las
actividades diarias en Odoo.

### Reciente

En la pestaña Reciente del widget _VoIP_ se encuentra el historial de llamadas
del usuario e incluye las llamadas entrantes y salientes. Haga clic en
cualquier número para iniciar una llamada.

### Siguientes actividades

En la pestaña Siguientes actividades del widget _VoIP_ , un usuario puede
visualizar cualquier actividad que tenga asignada,, además de cuales se deben
completar ese día.

Haga clic en una actividad de esta pestaña para realizar cualquier acción,
como enviar un correo electrónico, acceder a algún contacto, programar otra
actividad o acceder a un registro vinculado (puede ser una orden de venta,
lead, oportunidad o tarea de un proyecto).

El usuario también puede marcar la actividad como completa, editar los
detalles relacionados a ella o cancelarla.

Haga clic en el icono 📞 (teléfono) para llamar al cliente relacionado a una
actividad programada o en el icono ⌨️ (teclado) para marcar a otro número
relacionado al cliente.

![Centro de control de actividades en el widget
VoIP.](../../../_images/activity-widget.png)

En el widget _VoIP_ aparecen otros iconos categorizados en dos secciones:
Documento y Actividad.

En la sección Documento aparecen los siguientes de derecha a izquierda:

  * Icono ✉️ (sobre): envía un correo electrónico.

  * Icono 👤 (persona): redirecciona a la tarjeta del contacto.

  * Icono 📄 (documento): redirecciona al registro adjunto en Odoo.

  * Icono 🕓 (reloj): programa una actividad.

En la sección Actividad aparecen los siguientes de izquierda a derecha:

  * Icono ✔️ (marca de verificación): marca la actividad como hecha.

  * Icono ✏️ (lápiz): edita la actividad.

  * Icono ✖️ (cancelar) icon: cancela la actividad.

### Contactos

Un usuario puede acceder a un contacto de la aplicación _Contactos_ desde la
pestaña Contactos del widget _VoIP_.

Es muy fácil llamar a un contacto, solo es necesario que haga clic en él desde
la pestaña Contactos del widget _VoIP_.

La función de búsqueda también está disponible en la parte superior derecha
del widget, está representada con el icono 🔍 (lupa).

  *[VoIP]: Voz sobre protocolo de internet

