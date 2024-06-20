# Buscar y filtrar registros

Odoo utiliza filtros para incluir solo los registros más relevantes en función
del propósito de la vista en la que se encuentre. Sin embargo, puede editar el
filtro predeterminado o buscar valores específicos.

## Filtros preconfigurados

Puede modificar la selección predeterminada de registros al hacer clic en
Filtros, luego seleccione uno o varios **filtros preconfigurados**.

Example

En el reporte de análisis de ventas, se seleccionan de forma predeterminada
solo los registros en la etapa de orden de venta. Sin embargo, _también_
podría incluir registros en la etapa de cotización si selecciona Cotizaciones.
Además, podría incluir registros _únicamente_ de un año en específico, por
ejemplo _2022_ , al seleccionar Fecha de orden ‣ 2022.

![Uso de filtros preconfigurados en el reporte de análisis de
ventas](../../_images/preconfigured-filters.png)

Nota

Si selecciona filtros preconfigurados del mismo grupo (es decir, que _no_
están separados por una línea horizontal), los registros pueden coincidir con
_cualquier_ condición que se incluya. Sin embargo, si selecciona filtros de
diferentes grupos, los registros deben coincidir con _todas_ las condiciones.

## Filtros personalizados

Puede crear filtros personalizados con la mayoría de los campos presentes en
el modelo. Haga clic en Filtros ‣ Agregar filtro personalizado, seleccione un
campo, un operador, un valor y haga clic en Aplicar.

Example

Podría incluir registros _únicamente_ de un solo vendedor en el reporte de
Análisis de ventas, por ejemplo _Mitchell Admin_ , al seleccionar Vendedor
como campo, es igual a como operador, y escribir `Mitchell Admin` como valor.

![Uso de un filtro personalizado en el reporte de análisis de
ventas](../../_images/custom-filter.png)

Nota

Si los registros deben coincidir _solo_ con una de varias condiciones, haga
clic en Agregar una condición antes de aplicar un filtro personalizado. Si los
registros deben coincidir con _todas_ las condiciones, agregue nuevos filtros
personalizados.

## Buscar valores

Puede usar el campo de búsqueda para buscar valores específicos con rapidez y
agregarlos como filtro. Escriba el valor a buscar completo y seleccione el
campo deseado, o escriba parte del valor, haga clic en el botón desplegable
(⏵) antes del campo elegido y seleccione el valor exacto que está buscando.

Example

En lugar de agregar un filtro personalizado para seleccionar los registros
donde _Mitchell Admin_ es el vendedor en el reporte de análisis de ventas,
puede buscar `Mitch`, hacer clic en el botón desplegable (⏵) junto a Buscar
vendedor: Mitch, y seleccionar Mitchell Admin.

![Búsqueda de un valor específico en el reporte de análisis de
ventas](../../_images/search-values.png)

Nota

Usar el campo de búsqueda es equivalente a usar el operador _contiene_ al
agregar un filtro personalizado. Si introduce un valor parcial y selecciona el
campo deseado directamente entonces se incluirán _todos_ los registros que
contengan los caracteres que escribió para el campo seleccionado.

## Agrupar registros

Puede hacer clic en Agrupar por debajo del campo de búsqueda para agrupar los
registros según uno de los **grupos preconfigurados**.

Example

Puede agrupar los registros por vendedor en el reporte de análisis de ventas
haciendo clic en Agrupar y seleccionando Vendedor. No se filtra ningún
registro.

![Agrupar registros en el reporte de análisis de
ventas](../../_images/group.png)

Puede **personalizar grupos** utilizando una amplia gama de campos presentes
en el modelo. Haga clic en Agrupar por ‣ Agregar grupo personalizado,
seleccione un campo y luego haga clic en Aplicar.

Nota

Puede usar varios grupos al mismo tiempo. El primer grupo que selecciona es la
agrupación principal, el siguiente divide aún más las categorías del grupo
principal, y así sucesivamente.

