# Acciones automatizadas (automatizaciones)

Las acciones automatizadas se utilizan para activar cambios automáticos según
las acciones de usuario (por ejemplo, aplicar una modificación cuando se
establece un valor específico en un campo) o las condiciones de tiempo (por
ejemplo, archivar un registro 7 días después de su última actualización).

Para crear una acción automatizada con Studio, vaya a Automatizaciones en
cualquier parte dentro de esta aplicación.

Por cada acción automatizada que cree, debe definir los elementos Modelo,
Activador, Aplicar sobre y Acción.

Example

![Ejemplo de una acción automatizada en el modelo de
suscripción](../../_images/automated-action-example.png)

## Modelo

Seleccione el modelo en el que se aplicará la acción automatizada.

Nota

El modelo en el que se encuentra al hacer clic en Automatizaciones se
preselecciona de forma predeterminada.

## Activador

Defina cuándo se deben aplicar las acciones automatizadas. Hay seis
activadores disponibles.

### Al crear

La acción se activa cuando crea y guarda un registro.

### Al actualizar

La acción se activa cuando edita y guarda un registro que ya estaba guardado.

  * Utilice los campos activadores para especificar qué campos, y solo esos campos, activan la acción a su actualización.

  * Para detectar cuando un registro cambia de un estado a otro, defina un filtro de Antes de la actualización del dominio, el cual comprueba si se cumplió la condición antes de actualizarlo. Después, establezca un filtro Aplicar sobre, que verifica si se cumplió la condición después de actualizar el registro.

Example

Si desea que la acción automatizada ocurra al establecer una dirección de
correo electrónico en el contacto, defina el filtro Antes de la actualización
del dominio como `Correo electrónico sin establecer` y el dominio Aplicar en
como `Correo electrónico establecido`.

![Ejemplo de un activador Al actualizar](../../_images/on-update-trigger-
example.png)

### Al crear y actualizar

La acción se activa cuando crea y guarda un registro o lo edita después y lo
guarda.

### Al eliminar

La acción se activa cuando elimina un registro.

Nota

Este activador no se utiliza con frecuencia, ya que por lo general los
registros se archivan en lugar de eliminarlos.

### Al modificar un formulario

La acción se activa cuando realiza cualquier cambio al valor de un campo
activador en la [Vista de formulario](views.html#studio-views-general-form),
incluso antes de guardar el registro. Este activador solo funciona en la
interfaz de usuario cuando un usuario realiza una modificación. La acción no
se ejecutará si el campo se modifica debido a otra acción y no por el usuario.

Nota

Este activador solo se puede utilizar con la acción Ejecutar código Python,
por lo que requiere desarrollo.

### Según una condición de tiempo

Esta acción se activa cuando se llega a la fecha o fecha y hora de un campo
activador.

  * Para activar la acción después de la fecha de activación, agregue un número de minutos, horas, días o meses en Retraso después de fecha de activador. Para activar la acción antes, agregue un número negativo.

Example

Si desea enviar un recordatorio por correo electrónico 30 minutos antes del
inicio de un evento en el calendario, seleccione Inicio (evento de calendario)
en Fecha de activación y establezca el Retraso después de la fecha de
activador en **-30** minutos.

![Ejemplo de un activador con base en una condición de
tiempo](../../_images/timed-condition-trigger-example.png)

Nota

De forma predeterminada, el planificador busca fechas de activación cada 4
horas.

## Aplicar sobre

Defina en qué registros del modelo se aplicará la acción automatizada.
Funciona de la misma forma que cuando se aplican filtros en un modelo.

## Acción

Determina qué debe hacer la acción automatizada (acción de servidor). Hay ocho
tipos de acciones para elegir.

### Ejecutar el código Python

La acción se utiliza para ejecutar código Python. Las variables disponibles se
describen en la pestaña de Código Python, la cual también se utiliza para
escribir su código o en la pestaña de Ayuda.

  * Para permitir que la acción se ejecute en el sitio web, seleccione Disponible en el sitio web y agregue una Ruta de sitio web.

### Crear un nuevo registro

La acción se utiliza para crear un nuevo registro en cualquier modelo.

Nota

Solo es necesario seleccionar un modelo objetivo si desea que otro modelo que
no sea el que está utilizando sea el objetivo.

  * Para vincular el registro que activó la creación del nuevo registro, seleccione un campo en Vincular campo. Por ejemplo, puede crear un contacto de forma automática cuando un lead se convierte en una oportunidad.

  * Pestaña de Datos por escribir: la pestaña se utiliza para especificar los nuevos valores del registro. Después de seleccionar un Campo, seleccione su Tipo de evaluación:

    * Valor: se utiliza para indicar directamente el valor sin procesar del campo en la columna de Valor.

    * Referencia: se utiliza para seleccionar el registro en la columna de Registro y permite que Studio agregue el ID interno a la columna de Valor.

Example

Si una acción automatizada crea una nueva tarea en un proyecto, puede
asignarla a un usuario específico al establecer el Campo como Usuario
responsable (proyecto), el Tipo de evaluación como Referencia y el Registro a
un usuario específico.

![Ejemplo de una acción de Crear un nuevo registro](../../_images/new-record-
example.png)

    * Expresión de Python: se utiliza para definir de forma dinámica el valor recién creado del registro para un campo mediante el código Python en la columna de Valor.

### Actualizar el registro

La acción se utiliza para establecer los valores de los campos de cualquier
registro en el modelo actual.

Nota

El proceso para completar la pestaña de Datos por escribir es el mismo que se
describe en Crear un nuevo registro.

### Ejecutar varias acciones

La acción se utiliza para activar varias acciones al mismo tiempo. Para
hacerlo, haga clic en Agregar una línea en la pestaña de Acciones. En la
ventana emergente de Acciones subordinadas, haga clic en Crear y configure la
acción.

### Enviar correo electrónico

La acción se utiliza para enviar un correo electrónico a un contacto vinculado
a un registro en específico. Para hacerlo, seleccione o cree una plantilla de
correo electrónico.

### Añadir seguidores

La acción se utiliza para suscribir contactos existentes al registro.

### Crear nueva actividad

La acción se utiliza para programar una nueva actividad vinculada a un
registro. Utilice la pestaña de Actividad para configurarla con normalidad,
pero en lugar de Asignado a un campo, seleccione un Tipo de usuario de
actividad. Seleccione Usuario específico y agregue el usuario en Responsable
si la actividad siempre se debe asignar al mismo usuario. Para seleccionar de
forma dinámica un usuario vinculado al registro, seleccione Usuario genérico
del registro y cambie el nombre de campo de usuario si es necesario.

Example

Después de que un lead se convierte en una oportunidad, desea que su acción
automatizada programe una llamada para el usuario responsable del lead. Para
hacer esto, establezca la Actividad en Llamada y el Tipo de actividad de
usuario como Usuario genérico del registro.

![Ejemplo de una acción de Crear siguiente actividad](../../_images/next-
activity-example.png)

### Manda Mensaje de Texto SMS

La acción se utiliza para enviar un SMS al contacto vinculado al registro.
Para hacerlo, seleccione o cree una plantilla de SMS.

Truco

Si desea que los mensajes enviados se registren en el chatter, seleccione
Registrar como nota.

