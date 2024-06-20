# Crear hojas de horas después de la validación del tiempo personal

Odoo registra las horas dedicadas en proyectos/tareas de forma automática
cuando se solicita tiempo personal. Esto permite un mejor control general
sobre la validación de hojas de hora, ya que evita tener que preguntar acerca
de horas que el empleado olvidó registrar.

Active el :ref:` modo desarrollador <developer-mode>`, vaya a _Hojas de horas_
, y cambie el _Proyecto_ y la _Tarea_ establecidos de manera predeterminada,
si así lo desea.

![Vista de los ajustes de hojas de horas cuando se habilita la función de
registro de tiempo personal en la aplicación de Hoja de horas de
Odoo.](../../../../_images/record_time_off.png)

Vaya a Tiempo personal -> Configuración -> Tipos de tiempo personal.
Seleccione o cree el tipo necesario y decida si desea que las solicitudes se
validen o no.

![Vista del formulario de los tipos de tiempo personal en la que se destacan
la aprobación de solicitudes de tiempo personal y la sección de hojas de horas
en la aplicación de Tiempo personal de
Odoo.](../../../../_images/time_off_types.png)

Una vez que el empleado solicitó su tiempo personal y se validó la solicitud
(o no, según los ajustes elegidos), el tiempo se asigna de forma automática en
la aplicación de _Hojas de horas_ , en el respectivo proyecto y tarea.

En el siguiente ejemplo, el usuario solicitó _Tiempo personal pagado_ del 13
al 15 de julio.

![Vista del formulario de solicitud de tiempo personal en
Odoo.](../../../../_images/time_off_request.png)

Si no se necesita validación, el tiempo personal solicitado se mostrará
automáticamente en la aplicación de _Hojas de horas_. Si se necesita la
validación, el tiempo se asignará de forma automática en cuanto la persona
responsable lo valide.

![Video de la aplicación de Hoja de horas en el que se destaca el tiempo
personal solicitado del empleado.](../../../../_images/timesheets.png)

Haga clic en la lupa y coloque el cursor sobre la celda correspondiente para
acceder a todos los datos agregados en esa celda (día) y ver los detalles
sobre el proyecto/tarea.

![Vista de los detalles de un proyecto/tarea en la aplicación de Hoja de horas
de Odoo.](../../../../_images/timesheet_description.png)

