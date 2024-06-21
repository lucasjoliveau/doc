# Reportes

La aplicación _Servicio de asistencia_ de Konvergo ERP incluye varios reportes que
proporcionan la oportunidad de realizar un seguimiento de las tendencias de
los tickets de soporte al cliente, identificar áreas de mejora, gestionar las
cargas de trabajo de los empleados y confirmar cuando se cumplen las
expectativas del cliente.

## Reportes disponibles

A continuación se detallan los reportes disponibles en el _Servicio de
asistencia_ de Konvergo ERP. Para ver los distintos reportes, vaya a Servicio de
asistencia ‣ Reportes.

### Analisis de tickets

El reporte de _Análisis de tickets_ (Servicio de asistencia ‣ Reportes ‣
Análisis de tickets) proporciona una vista general de cada ticket de soporte
al cliente en la base de datos. Esto incluye el número de tickets asignados
entre equipos y usuarios individuales.

Este reporte es útil para identificar dónde invierten más tiempo los equipos y
ayuda a determinar si hay una distribución desequilibrada de la carga de
trabajo entre el personal de soporte. El reporte predeterminado cuenta el
número de tickets por equipo y los agrupa por etapas.

![Vista predeterminada del reporte de Análisis de
tickets.](../../../../_images/tickets-default.png)

Puede seleccionar medidas alternativas para consultar dónde utilizan más
tiempo en diferentes puntos del flujo de trabajo. Para cambiar las medidas
utilizadas del reporte presentado, o para agregar más, haga clic en el botón
**Medidas** y seleccione una o más opciones del menú desplegable:

  * **Horas promedio en responder** : promedio de horas laborables entre un mensaje enviado por el cliente y la respuesta del equipo de soporte. _No incluye los mensajes enviados cuando el ticket se encontraba en una etapa plegada_

  * **Horas abiertas** : número de horas entre la fecha de creación del ticket y la fecha de cierre. Si no hay fecha de cierre en el ticket, se utiliza la fecha actual. **Esta medida no es específica a las horas laborables**.

  * **Horas utilizadas** : número de horas registradas en _Hojas de horas_ de un ticket. _Esta medida solo está disponible si las Hojas de horas están habilitadas en un equipo y el usuario actual tiene los permisos de acceso para verlas_.

  * **Horas para asignar** : número de horas laborables entre la fecha de creación del ticket y cuando se asignó a un miembro del equipo.

  * **Horas para cerrar** : número de horas laborables entre la fecha de creación del ticket y la fecha de su cierre.

  * **Horas para la primera respuesta** : número de horas laborables entre la fecha de recepción del ticket y la fecha de envío del primer mensaje. _No incluye el correo electrónico que se envía de forma automática cuando un ticket llega a una etapa_.

  * **Horas para la fecha límite de SLA** : número de horas laborables para llegar a la última fecha límite de SLA en un ticket.

  * **Valoración /5** : número asignado a la valoración recibida de un cliente (Inconforme = 1, Bien o neutral = 3, Satisfecho = 5)

  * **Número** : número de tickets en total.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las <em>horas laborables</em> se calculan según el calendario de trabajo predeterminado. Para ver o cambiar el calendario de trabajo, vaya a la aplicación Ajustes y seleccione Empleados ‣ Horas laborables de la empresa.</p>
</div>

### Análisis del estado de SLA

El reporte de _Análisis del estado del SLA_ (Servicio de asistencia ‣ Reportes
‣ Análisis del estado del SLA) registra la rapidez con la que se cumple un
acuerdo de nivel de servicio (SLA), así como la tasa de éxito de cada
política.

Este reporte se filtra de forma predeterminada para mostrar el número de
acuerdos de nivel de servicio fallidos, así como la tasa de fallas en los
últimos 30 días, agrupados por equipo.

![Vista de las opciones de "Agrupar por" del reporte de Análisis de
tickets.](../../../../_images/sla-status.png)

Para cambiar las medidas utilizadas para el reporte presentado, o para agregar
más, haga clic en el botón **Medidas** y seleccione una o más opciones del
menú desplegable:

  * **% de SLA fallidos** : porcentaje de tickets que han fallado al menos un acuerdo de nivel de servicio.

  * **% de SLA en progreso** : porcentaje de tickets que aún tienen al menos un acuerdo de nivel de servicio en progreso y no han fallado ninguno.

  * **% de SLA exitosos** : porcentaje de tickets donde todos los acuerdos de nivel de servicio han sido exitosos.

  * **Número de SLA fallidos** : número de tickets que han fallado al menos un acuerdo de nivel de servicio.

  * **Número de SLA exitosos** : número de tickets donde todos los acuerdos de nivel de servicio han tenido éxito.

  * **Número de SLA en progreso** : número de tickets que aún tienen al menos un acuerdo de nivel de servicio en progreso y no han fallado ninguno.

  * **Horas laborables para asignar** : número de horas laborables entre la fecha de creación del ticket y cuando se asignó a un miembro del equipo.

  * **Horas laborables para cerrar** : número de horas laborables entre la fecha de creación del ticket y la fecha de su cierre.

  * **Horas laborables para llegar al SLA** : número de horas laborables entre la fecha de creación del ticket y la fecha en que se cumplió el acuerdo de nivel de servicio.

  * **Número** : número de tickets en total.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para ver el número de tickets que pudieron alcanzar los objetivos del <abbr title="Acuerdo de nivel de servicio">SLA</abbr> y hacer un seguimiento de la cantidad de tiempo que tomó lograrlos, haga clic en Medidas ‣ Número de SLA exitosos y Medidas ‣ Horas laborables para llegar al SLA.</p>
<p>Para ordenar estos resultados por los miembros del equipo asignados a los tickets, seleccione Total ‣ Asignado a.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="sla">Acuerdos de nivel de servicio (SLA)</a></p>
</div>

### Calificación de clientes

El reporte de _Calificación de clientes_ (Servicio de asistencia ‣ Reportes ‣
Calificación de clientes) muestra un resumen de las calificaciones recibidas
en los tickets de soporte individuales, así como cualquier comentario
adicional enviado con la calificación.

![Vista de la pantalla de kanban en el reporte de calificación de
clientes.](../../../../_images/customer-ratings.png)

Haga clic en una calificación individual para ver los detalles adicionales de
la calificación que envió el cliente, incluye un enlace al ticket original.

![Vista de los detalles de una calificación de cliente
individual.](../../../../_images/ratings-details.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>En la página de detalles de la calificación, seleccione la opción <b>Visible solo de forma interna</b> para ocultar la calificación en el portal de clientes.</p>
</div>

El reporte _Calificación de clientes_ se muestra en la vista kanban de forma
predeterminada, pero también se puede mostrar en la vista de gráfico, lista o
tabla dinámica.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="ratings">Calificaciones</a></p>
</div>

## Visualizar y filtrar opciones

En cualquier reporte de Konvergo ERP, las opciones de visualización y filtrado varían
según los datos que se están analizando, midiendo y agrupando. A continuación
encontrará más información sobre las vistas disponibles para los reportes del
_Servicio de asistencia_.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo puede seleccionar una medida a la vez para los gráficos, pero las tablas dinámicas pueden incluir varias.</p>
</div>

### Vista de tabla dinámica

La vista de _tabla dinámica_ presenta los datos de forma interactiva y los
tres reportes de _Servicio de asistencia_ están disponibles en ella.

Puede acceder a la vista de tabla dinámica en cualquier reporte, haga clic en
el **icono de tabla** en la parte superior derecha de la pantalla.

![Vista del reporte de análisis de estado del SLA en el Servicio de asistencia
de Konvergo ERP.](../../../../_images/pivot-view1.png)

Para agregar un grupo a una fila o columna a la vista de tabla dinámica, haga
clic en el **➕ (signo más)** junto a **Total** y luego seleccione uno de los
grupos. Para eliminar uno, haga clic en **➖ (signo menos)** y desmarque la
opción apropiada.

### Vista de gráfico

La vista de _gráfico_ presenta datos en un gráfico de _barras_ , _líneas_ o
_circular_.

Cambie a la vista de gráfico seleccionando el **icono de gráfico de líneas**
en la parte superior derecha de la pantalla. Para cambiar entre los diferentes
gráficos, seleccione el _icono relacionado_ en la parte superior izquierda del
gráfico mientras se encuentra en esta vista.

Bar chartLine chartPie chart

![Vista del reporte de análisis de estado del SLA en vista de
barras.](../../../../_images/bar-chart2.png)

![Vista del reporte de valoraciones de clientes en la vista de
líneas.](../../../../_images/line-chart1.png)

![Vista del reporte de Análisis de tickets en la vista de gráfico
circular.](../../../../_images/pie-chart1.png)

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Tanto el <em>gráfico de barras</em> como el <em>gráfico de líneas</em> pueden utilizar la opción de <em>vista apilada</em>, esta presenta dos (o más) grupos de datos uno encima del otro, en lugar de uno junto al otro, facilitando así la comparación de datos.</p>
</div>

### Guardar y compartir una búsqueda de favoritos

La función de _Favoritos_ en los reportes del _Servicio de asistencia_ permite
que los usuarios guarden sus filtros más utilizados sin tener que
reconstruirlos cada vez que los necesitan.

Siga los pasos a continuación para crear y guardar nuevos _Favoritos_ en un
reporte:

  1. Establezca los parámetros necesarios usando las opciones de **Filtros** , **Agrupar por** y **Medidas** .

  2. Haga clic en Favoritos ‣ Guardar búsqueda actual.

  3. Renombre la búsqueda.

  4. Seleccione **Utilizar de forma predeterminada** para que estos ajustes de filtro se muestren de forma automática cuando se abra el reporte. De lo contrario, no seleccione la casilla.

  5. Seleccione **Compartir con todos los usuarios** para que este filtro esté disponible para los demás usuarios de la base de datos. Si esta casilla no está seleccionada, solo estará disponible para el usuario que la creó.

  6. Haga clic en **Guardar** para conservar la configuración para su uso posterior.

![Vista de la opción guardar favoritos en la aplicación Servicio de asistencia
de Konvergo ERP.](../../../../_images/save-filters.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="receiving_tickets">Empezar a recibir tickets</a></p></li>
<li><p><a href="../../../essentials/reporting">Reportes de Konvergo ERP</a></p></li>
</ul>
</div>

  *[SLA]: Acuerdo de nivel de servicio

