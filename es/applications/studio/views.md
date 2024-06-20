# Vistas

Las vistas son la interfaz que permite mostrar los datos contenidos en un
modelo. Un modelo puede tener varias vistas, que simplemente son diferentes
formas de mostrar los mismos datos. En Studio, las vistas se dividen en cuatro
categorías: general, varios registros, línea de tiempo y reportes.

Truco

Para cambiar la vista predeterminada de un modelo, vaya a Studio ‣ Vistas ‣
Menú desplegable (⋮) ‣ Establecer como predeterminada.

Nota

Puede modificar las vistas con ayuda de un editor xml integrado. Para hacerlo,
active el [Modo de desarrollador](../general/developer_mode.html#developer-
mode), vaya a la vista que desea editar, seleccione la pestaña de View y haga
clic en </> XML.

Importante

Si está editando una vista por medio del editor XML, evite hacer cambios
directamente en las vistas estándar y en las vistas heredadas, ya que podrían
reiniciarse y no se conservarían en el caso de una actualización. Asegúrese de
seleccionar siempre las vistas heredadas correspondientes en Studio. De hecho,
cuando se modifica una vista en Studio arrastrando y soltando un nuevo campo,
automáticamente se genera una vista heredada de Studio con su XPath
correspondiente, el cual define qué parte de la vista se modifica.

## Vistas generales

Nota

Los siguientes ajustes se encuentran en la pestaña Vista de la vista, a menos
que se especifique lo contrario.

### Formulario

Se usa la vista Formulario al crear y editar registros, por ejemplo,
contactos, órdenes de venta, productos, etc.

  * Con el fin de darle estructura a un formulario, contamos con la función de arrastrar y soltar, la cual puede utilizar con los elementos Pestañas y columnas, ubicados en la pestaña \+ Añadir.

  * Si desea evitar que los usuarios creen, editen o eliminen registros, desmarque Puede crear, Puede editar, o Puede eliminar.

Example

![Vista de formulario del modelo de la orden de venta](../../_images/form-
sales-order.png)

### Actividad

Se usa la vista Actividad para organizar y tener una vista general de las
actividades (correos electrónicos, llamadas, etc.) vinculadas a los registros.

Nota

Solo se puede modificar esta vista en Studio al editar el código XML.

Example

![Vista de actividad de los leads/oportunidades](../../_images/activity-lead-
opportunity.png)

### Buscar

Se añade la vista de Búsqueda por encima de otras vistas para filtrar, agrupar
y buscar registros.

  * Para añadir Filtros personalizados y darles estructura con Separadores, vaya a la pestaña \+ Añadir y, con la función arrastrar y soltar, colóquelos en Filtros.

  * Si desea añadir un campo existente al menú despegable de búsqueda, vaya a la pestaña \+ Añadir y, con la función arrastrar y soltar, colóquelo en Campos de autocompletado.

Example

![Vista de búsqueda del proyecto en kanban](../../_images/search-project-
kanban.png)

## Vistas para varios registros

Nota

Los siguientes ajustes se encuentran en la pestaña Vista de la vista, a menos
que se especifique lo contrario.

### Kanban

Normalmente se usa la vista de Kanban en los flujos empresariales, esto hace
más fácil el proceso de cambio de etapas y además, organiza los registros en
_tarjetas_.

Nota

Si se encuentra habilitada la vista Kanban, se usará de forma predeterminada
en los dispositivos móviles en lugar de la Vista de lista.

  * Para evitar que los usuarios creen un nuevo registro, desmarque Puede crear.

  * Para crear registros desde la vista, en un formulario minimalista, habilite Creación rápida.

  * Si desea cambiar la forma en la que se agrupan los registros, seleccione un nuevo grupo en Automáticamente agrupar por.

Example

![Vista kanban del proyecto](../../_images/kanban-project.png)

### Lista

Se usa la vista de Lista para ver varios registros al mismo tiempo y para
buscar y editar registros.

  * Si desea evitar que los usuarios creen, editen o eliminen registros, desmarque Puede crear, Puede editar, o Puede eliminar.

  * Si desea crear y editar registros desde la vista, seleccione Nuevo registro en la parte superior o Nuevo registro en la parte inferior en Editable.

Nota

Esto evita que los usuarios abran registros en la Vista de formulario de la
vista de Lista.

  * Si desea editar varios registros al mismo tiempo, marque Habilitar edición masiva.

  * Si desea cambiar la forma en la que se organizan los registros, seleccione un campo en Ordenar por.

Truco

Si desea añadir un icono de manija que le ayude a ordenar los registros de
forma manual, debe añadir un [Campo integer](fields.html#studio-fields-simple-
fields-integer) con el widget Manija.

![Mueva el icono de manija para organizar los registros de manera manual en la
vista de lista](../../_images/list-drag-handle.png)

Example

![Vista de lista de la orden de venta](../../_images/list-sales-order.png)

### Mapa

Se usa la vista de Mapa para mostrar registros en un mapa. Por ejemplo, se
puede usar en la aplicación de Servicio externo con el objetivo de organizar
un itinerario entre diferentes tareas.

Nota

Para activar esta vista, es necesario contar con un campo
[Many2One](fields.html#studio-fields-relational-fields-many2one) vinculado a
un _Contacto_ , ya que se usa la dirección del contacto para marcar la
ubicación de los registros en el mapa.

  * Para seleccionar qué tipo de contacto se debe usar en el mapa, selecciónelo en el Campo de contacto.

  * Si desea ocultar el nombre o la dirección del registro, seleccione Ocultar nombre u Ocultar dirección.

  * Si desea añadir información de otros campos, selecciónelos en Campos adicionales.

  * Si desea que se le muestren rutas sugeridas entre diferentes registros, seleccione Habilitar enrutamiento y el campo que se deberá usar para ordenar los registros.

Example

![Vista de mapa en la tarea](../../_images/map-task.png)

## Vistas de línea de tiempo

Nota

  * Al activar una vista de línea de tiempo, necesita seleccionar qué campos de [Fecha](fields.html#studio-fields-simple-fields-date) o [Fecha y hora](fields.html#studio-fields-simple-fields-date-time) se deben usar para definir el inicio y final de los registros, con el fin de mostrarlos en la vista. Puede modificar los campos Fecha de inicio y Fecha de finalización después de activar la vista.

  * Los siguientes ajustes se encuentran en la pestaña Vista de la vista, a menos que se especifique lo contrario.

### Calendario

Se usa la vista de Calendario para administrar y obtener una vista general de
los registros dentro de un calendario.

  * Para crear registros desde la vista sin necesidad de abrir la Vista de formulario, habilite la Creación rápida.

Nota

Esta función solo está disponible en modelos específicos que se pueden _crear
rápido_ con tan solo un _nombre_. Sin embargo, la mayoría de modelos no
cuentan con esta función, por lo que tendrá que abrir la vista de Formulario
para completar los campos necesarios.

  * Si desea añadir colores a los registros en el calendario, seleccione un campo en Color. De esta manera, todos los registros que compartan el mismo valor de ese campo mostrarán el mismo color.

Nota

Hay pocos colores disponibles, por lo que se podría asignar el mismo color a
diferentes valores.

  * Para mostrar los eventos que duran todo un día en la parte superior del calendario, seleccione la [Casilla de verificación](fields.html#studio-fields-simple-fields-checkbox) que especifica que el evento dura todo el día.

  * Para seleccionar la medida de tiempo predeterminada para mostrar los eventos, seleccione Día, Semana, Mes, o Año en Modo de visualización predeterminado.

Nota

También puede usar el Campo de retraso para mostrar la duración del evento en
horas al seleccionar un campo [Decimal](fields.html#studio-fields-simple-
fields-decimal) o [Integer](fields.html#studio-fields-simple-fields-integer)
en el modelo que especifica la duración del evento. Sin embargo, si establece
un campo de Fecha de finalización, no se tomará en cuenta el Campo de retraso.

Example

![Vista de calendario en el calendario de eventos](../../_images/calendar-
event.png)

### Cohorte

Se usa la vista Cohorte para examinar el ciclo de vida de los registros
durante un periodo de tiempo. Por ejemplo, se usa en la aplicación de
Suscripciones para ver la tasa de retención.

  * Para mostrar una medida (por ejemplo, el valor agregado de algún campo) de manera predeterminada en la vista, seleccione un Campo de medida.

  * Para elegir el intervalo de tiempo a usar de forma predeterminada al agrupar los resultados, seleccione Día, Semana, Mes o Año en Intervalo.

  * Si desea activar el Modo cohorte, seleccione Retención el porcentaje de registros que permanecen durante un periodo de tiempo, comienza en el 100% y disminuye con el tiempo o Rotación el porcentaje de registros que se desplazan a lo largo de un periodo de tiempo: comienza en el 0% y aumenta con el tiempo.

  * Para cambiar el progreso de la Línea de tiempo (por ejemplo, las columnas), seleccione Avanzar (de 0 a +15) o Retroceder (de -15 a 0). La mayoría de las veces se usa la línea de tiempo Avanzar.

Example

![Vista cohorte de una suscripción](../../_images/cohort-subscription.png)

### Gantt

Se usa la vista Gantt para prever y examinar el progreso de los registros, los
cuales se representan por una barra debajo de la medida de tiempo.

  * Si desea evitar que los usuarios creen o editen registros, desmarque Puede crear y Puede editar.

  * Si desea que se rellenen las celdas de color gris cuando no se deba crear un registro (por ejemplo, los fines de semana para los empleados), seleccione Mostrar indisponibilidad.

Nota

Esta función debe ser compatible con el modelo sin ayuda de Studio. Es
compatible con las aplicaciones Proyecto, Tiempo personal, Planeación y
Fabricación.

  * Para que se muestre una fila con el total en la parte inferior, seleccione Mostrar fila con el total.

  * Para combinar varios registros en una sola fila, seleccione Combinar primer nivel.

  * Para elegir la forma de agrupar los registros en las filas de forma predeterminada (por ejemplo, por empleado o proyecto), seleccione un campo en Automáticamente agrupar por.

  * Para definir la medida de tiempo predeterminada para mostrar los registros, seleccione Día, Semana, Mes, or Año en Medida predeterminada.

  * Si desea añadir colores a los registros en la vista, seleccione un campo en Color. De esta manera, todos los registros que compartan el mismo valor de ese campo mostrarán el mismo color.

Nota

Hay pocos colores disponibles, por lo que se podría asignar el mismo color a
diferentes valores.

  * Para especificar con qué grado de precisión debe dividirse cada medida de tiempo, seleccione Cuarto de hora, Media hora u Hora en Precisión del día, Medio día o Día en Precisión de la semana y Precisión del mes.

Example

![Vista gantt en la planeación de turnos](../../_images/gantt-planning.png)

## Vistas de informes

Nota

Los siguientes ajustes se encuentran en la pestaña Vista de la vista, a menos
que se especifique lo contrario.

### Pivote

Se utiliza la vista de Tabla dinámica para explorar y analizar los datos de
los registros de forma interactiva. Es de gran utilidad a la hora de agregar
datos numéricos, crear categorías y organizar los datos al expandir y colapsar
diferentes niveles de datos.

  * Para acceder a todos los registros cuyos datos se encuentran en una celda, seleccione Acceder a los registros de la celda.

  * Para dividir los datos en diferentes categorías, seleccione los campos en Agrupación de columnas, Agrupar filas - primer nivel, o Agrupar filas - segundo nivel.

  * Para añadir diferentes tipos medidas en la vista, seleccione un campo en Medidas.

  * Para mostrar el número de registros que conforman los datos totales de una celda, seleccione Mostrar recuento.

Example

![Vista de tabla dinámica del reporte de compra](../../_images/pivot-purchase-
report.png)

### Gráfico

Se utiliza la vista de Gráfico para mostrar los datos de los registros en un
gráfico de barras, líneas o circular.

  * Para cambiar el gráfico predeterminado, seleccione Barra, Línea, o Circular en Tipo.

  * Para elegir un atributo (categoría) de datos predeterminado, seleccione un campo en Primer atributo y, en caso de ser necesario, otro en Segundo atributo.

  * Seleccione uno de los campos en Medida para elegir un tipo predeterminado de datos a medir con la vista.

  * _Solo para gráficos de barras o líneas_ : si desea ordenar las diferentes categorías de datos por su valor, seleccione Ascendente (de menor a mayor valor) o Descendente (de mayor a menor valor) en orden.

  * _Solo para gráficos de barras y circulares_ : Si desea acceder a todos los registros cuyos datos se encuentran en una categoría de datos del gráfico, marque Acceso a los registros desde el gráfico.

  * _Solo para gráficos de barras_ : Si se utilizan dos atributos (categorías) de datos y se marca la opción Gráfico de barras apilado, se mostrarán dos columnas, una encima de la otra.

Example

![Vista de gráfico de barras del reporte de análisis de
ventas](../../_images/graph-sales-report.png)

### Tablero

Se utiliza la vista de Tablero para mostrar varias vistas de reportes e
indicadores clave de rendimiento. Los elementos que se muestran en la vista
dependen de la configuración de las otras vistas de reporte.

Example

![Vista de tablero del modelo para el reporte de análisis de
ventas](../../_images/dashboard-sales-report.png)

