# Buscar y filtrar registros

Konvergo ERP utiliza filtros para incluir solo los registros más relevantes en función
del propósito de la vista en la que se encuentre. Sin embargo, puede editar el
filtro predeterminado o buscar valores específicos.

## Filtros preconfigurados

Puede modificar la selección predeterminada de registros al hacer clic en
**Filtros** , luego seleccione uno o varios **filtros preconfigurados**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En el reporte de análisis de ventas, se seleccionan de forma predeterminada solo los registros en la etapa de orden de venta. Sin embargo, <em>también</em> podría incluir registros en la etapa de cotización si selecciona <b>Cotizaciones</b>. Además, podría incluir registros <em>únicamente</em> de un año en específico, por ejemplo <em>2022</em>, al seleccionar Fecha de orden ‣ 2022.</p>
<img alt="Uso de filtros preconfigurados en el reporte de análisis de ventas" class="align-center" src="../../_images/preconfigured-filters.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si selecciona filtros preconfigurados del mismo grupo (es decir, que <em>no</em> están separados por una línea horizontal), los registros pueden coincidir con <em>cualquier</em> condición que se incluya. Sin embargo, si selecciona filtros de diferentes grupos, los registros deben coincidir con <em>todas</em> las condiciones.</p>
</div>

## Filtros personalizados

Puede crear filtros personalizados con la mayoría de los campos presentes en
el modelo. Haga clic en Filtros ‣ Agregar filtro personalizado, seleccione un
campo, un operador, un valor y haga clic en **Aplicar**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Podría incluir registros <em>únicamente</em> de un solo vendedor en el reporte de Análisis de ventas, por ejemplo <em>Mitchell Admin</em>, al seleccionar <b>Vendedor</b> como campo, <b>es igual a</b> como operador, y escribir <code>Mitchell Admin</code> como valor.</p>
<img alt="Uso de un filtro personalizado en el reporte de análisis de ventas" class="align-center" src="../../_images/custom-filter.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si los registros deben coincidir <em>solo</em> con una de varias condiciones, haga clic en <b>Agregar una condición</b> antes de aplicar un filtro personalizado. Si los registros deben coincidir con <em>todas</em> las condiciones, agregue nuevos filtros personalizados.</p>
</div>

## Buscar valores

Puede usar el campo de búsqueda para buscar valores específicos con rapidez y
agregarlos como filtro. Escriba el valor a buscar completo y seleccione el
campo deseado, o escriba parte del valor, haga clic en el botón desplegable
(**⏵**) antes del campo elegido y seleccione el valor exacto que está
buscando.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En lugar de agregar un filtro personalizado para seleccionar los registros donde <em>Mitchell Admin</em> es el vendedor en el reporte de análisis de ventas, puede buscar <code>Mitch</code>, hacer clic en el botón desplegable (<b>⏵</b>) junto a <b>Buscar vendedor: Mitch</b>, y seleccionar <b>Mitchell Admin</b>.</p>
<img alt="Búsqueda de un valor específico en el reporte de análisis de ventas" class="align-center" src="../../_images/search-values.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Usar el campo de búsqueda es equivalente a usar el operador <em>contiene</em> al agregar un filtro personalizado. Si introduce un valor parcial y selecciona el campo deseado directamente entonces se incluirán <em>todos</em> los registros que contengan los caracteres que escribió para el campo seleccionado.</p>
</div>

## Agrupar registros

Puede hacer clic en **Agrupar por** debajo del campo de búsqueda para agrupar
los registros según uno de los **grupos preconfigurados**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Puede agrupar los registros por vendedor en el reporte de análisis de ventas haciendo clic en <b>Agrupar</b> y seleccionando <b>Vendedor</b>. No se filtra ningún registro.</p>
<img alt="Agrupar registros en el reporte de análisis de ventas" class="align-center" src="../../_images/group.png"/>
</div>

Puede **personalizar grupos** utilizando una amplia gama de campos presentes
en el modelo. Haga clic en Agrupar por ‣ Agregar grupo personalizado,
seleccione un campo y luego haga clic en **Aplicar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede usar varios grupos al mismo tiempo. El primer grupo que selecciona es la agrupación principal, el siguiente divide aún más las categorías del grupo principal, y así sucesivamente.</p>
</div>

