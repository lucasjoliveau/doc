# Reportes

En el menú **Reportes** de la mayoría de las aplicaciones puede encontrar
varios reportes que le permiten analizar y visualizar los datos de sus
registros.

## Seleccionar una vista

Dependiendo del reporte, Konvergo ERP puede mostrar los datos de varias formas.
Algunas veces está disponible una vista única personalizada por completo al
reporte, mientras que varias vistas están disponibles para otros. Sin embargo,
hay dos vistas genéricas específicas para los reportes: las vistas de gráfico
y tabla dinámica.

### Vista de gráfico

La vista de gráfico se utiliza para visualizar los datos de sus registros,
esta le ayudará a identificar patrones y tendencias. A menudo puede encontrar
esta vista en el menú **reportes** de las aplicaciones, pero también puede
encontrarla en otros lugares. Para acceder a ella, haga clic en el **botón de
vista de gráfico** que se ubica en la parte superior derecha de la página.

![Seleccionar la vista de gráfico](../../_images/graph-button.png)

### Vista de tabla dinámica

La vista de tabla dinámica se utiliza para agregar los datos de sus registros
y desglosarlos para su análisis. Puede encontrar esta vista en el menú
**reportes** de las aplicaciones, pero también puede encontrarla en otros
lugares. Para acceder a ella, haga clic en el **botón de vista de tabla
dinámica** que se ubica en la parte superior derecha de la página.

![Selección de la vista de tabla dinámica](../../_images/pivot-button.png)

## Elegir medidas

Tras seleccionar una vista, debe asegurarse de que solo se
[filtran](search) los registros relevantes. A continuación, debe elegir
lo que se medirá. Siempre hay una medida seleccionada de forma predeterminada,
si desea editarla haga clic en **medidas** y elija una, o varias en el caso de
las tablas dinámicas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando selecciona una medida, Konvergo ERP agrega los valores registrados en ese campo para los registros filtrados. Solo se pueden medir los campos numéricos <a href="../studio/fields#studio-fields-simple-fields-integer"><span class="std std-ref">enteros</span></a>, <a href="../studio/fields#studio-fields-simple-fields-decimal"><span class="std std-ref">decimales</span></a> y <a href="../studio/fields#studio-fields-simple-fields-monetary"><span class="std std-ref">monetarios</span></a>. Además, la opción «número» se utiliza para contar el número total de registros filtrados.</p>
</div>

Después de elegir qué desea medir, puede definir cómo se deben
[agrupar](search#search-group) los datos según la dimensión que desea
analizar. De forma predeterminada, los datos se agrupan por _Fecha > Mes_ para
analizar la evolución de las medidas a lo largo de los meses.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Cuando filtra un solo periodo de tiempo, se habilita la opción de compararlo con otro.</p>
<img alt="Uso de la opción de comparación" src="../../_images/comparison.png"/>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Select measures</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">Group measures</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><p>Entre otras medidas, puede agregar las medidas de <b>margen</b> y <b>número</b> al reporte de análisis de ventas. De forma predeterminada, se selecciona la medida <b>importe sin impuestos</b>.</p>
<img alt="Selección de distintas medidas en el reporte de análisis de ventas" src="../../_images/measures.png"/>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><p>Puede agrupar las medidas por <b>categoría de producto</b> en el nivel de filas del ejemplo anterior del reporte de análisis de ventas.</p>
<img alt="Agregar un grupo en el reporte de análisis de ventas" src="../../_images/single-group.png"/>
</div></div>
</div>

## Utilizar la vista de tabla dinámica

Agrupar datos es esencial para la vista de tabla dinámica pues le permite
desglosar los datos para obtener información más detallada. Aunque puede usar
la opción **Agrupar por** para agregar con rapidez un grupo en el nivel de las
filas, como se muestra en el ejemplo anterior. También puede hacer clic en el
botón con el signo de más (**➕**) junto al encabezado de **total** en el nivel
de las filas _y_ columnas, y luego seleccionar uno de los **grupos
preconfigurados**. Para eliminar uno, haga clic en el botón con el signo de
menos (**➖**).

Una vez que agregue un grupo, puede agregar nuevos en el eje opuesto o en los
subgrupos recién creados.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Puede dividir aún más las medidas en el ejemplo anterior del reporte de análisis de ventas mediante el grupo <b>vendedor</b> en el nivel de columnas y el grupo <b>Fecha de orden &gt; Mes</b> en la categoría de producto <b>Todos / Se pueden vender / Muebles de oficina</b>.</p>
<img alt="Agregar varios grupos a un reporte de análisis de ventas" src="../../_images/multiple-groups.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Puede cambiar los grupos de las filas y columnas al hacer clic en el botón «girar eje» (<b>⇄</b>).</p></li>
<li><p>Puede hacer clic en la etiqueta de una medida para ordenar los valores en orden ascendente (⏶) o descendente (⏷).</p></li>
<li><p>Puede descargar una versión <code>.xlsx</code> de la tabla dinámica al hacer clic en el botón de descarga (<b>⭳</b>).</p></li>
</ul>
</div>

## Utilizar la vista de gráfico

Hay tres gráficos disponibles: de barras, de líneas y circular.

Los **gráficos de barras** se utilizan para mostrar la distribución o una
comparación de varias categorías. Son bastante útiles, ya que pueden trabajar
con conjuntos grandes de datos.

Los **gráficos de líneas** son útiles para mostrar los cambios en series
temporales y tendencias a lo largo del tiempo.

Los **gráficos circulares** se utilizan para mostrar la distribución o
comparación de un pequeño número de categorías cuando son parte de un conjunto
significativo.

Bar chartLine chartPie chart

![Vista del reporte de análisis de ventas como gráfico de
barras](../../_images/bar.png)

![Vista del reporte de análisis de ventas como gráfico de
líneas](../../_images/line.png)

![Vista del reporte de análisis de ventas como gráfico
circular](../../_images/pie.png)

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para los gráficos de <b>barras</b> y <b>líneas</b> puede usar la opción de apilado cuando tiene al menos dos grupos, aparecerán uno encima del otro en lugar de uno junto al otro.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-2-2-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-2-2-0" name="2-0" role="tab" tabindex="0">Stacked bar chart</button><button aria-controls="panel-2-2-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-1" name="2-1" role="tab" tabindex="-1">Regular bar chart</button><button aria-controls="panel-2-2-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-2" name="2-2" role="tab" tabindex="-1">Stacked line chart</button><button aria-controls="panel-2-2-3" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-3" name="2-3" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-2-2-0" class="sphinx-tabs-panel" id="panel-2-2-0" name="2-0" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de barras apilado" src="../../_images/stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-1" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-1" name="2-1" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de barras sin apilar" src="../../_images/non-stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-2" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-2" name="2-2" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de líneas apiladas" src="../../_images/stacked-line.png"/>
</div><div aria-labelledby="tab-2-2-3" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-3" name="2-3" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de líneas sin apilar" src="../../_images/non-stacked-line.png"/>
</div></div>
<p>Para los gráficos de <b>líneas</b> puede usar la opción de acumulativo para sumar valores, resulta bastante útil para mostrar el cambio en el crecimiento durante un período de tiempo.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-3-3-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-3-3-0" name="3-0" role="tab" tabindex="0">Cumulative line chart</button><button aria-controls="panel-3-3-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-3-3-1" name="3-1" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-3-3-0" class="sphinx-tabs-panel" id="panel-3-3-0" name="3-0" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de líneas acumulativo" src="../../_images/cumulative.png"/>
</div><div aria-labelledby="tab-3-3-1" class="sphinx-tabs-panel" hidden="true" id="panel-3-3-1" name="3-1" role="tabpanel" tabindex="0"><img alt="Ejemplo de gráfico de líneas regular" src="../../_images/non-cumulative.png"/>
</div></div>
</div>

