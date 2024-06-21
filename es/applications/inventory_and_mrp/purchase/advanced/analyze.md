# Analice el rendimiento de sus compras

Si su empresa suele comprar productos, tiene varias razones para analizar su
rendimiento. Realizar este análisis le servirá para mejorar sus pronósticos y
planeación de sus futuras órdenes. Por ejemplo, puede evaluar si su empresa
depende de ciertos proveedores y esta información puede ayudarle a negociar
descuentos en los precios.

## Generar reportes personalizados

Vaya a _Reportes_ para acceder al análisis de compras. Con solo acceder al
tablero de reportes, usted puede obtener una idea general de su rendimiento
real. De forma predeterminada, el tablero de reportes muestra un gráfico de
líneas que presenta la cantidad sin impuestos de sus órdenes de compra por
día, y en la parte inferior, las métricas principales y una tabla dinámica.

![Tablero de reportes en Compras de Konvergo ERP ](../../../../_images/analyze-
reporting-dashboard.png)

Aunque los datos presentados al principio son útiles, hay varias herramientas
y funciones que puede utilizar para obtener aún más información sobre sus
compras.

### Uso de filtros para seleccionar los datos necesarios

Konvergo ERP cuenta con varios filtros predeterminados que puede usar y combinar al
hacer clic en _Filtros_. Cuando se selecciona algún filtro, Konvergo ERP busca todas
las órdenes que coincidan con al menos un filtro seleccionado y completa el
gráfico, las métricas principales y la tabla dinámica con los datos. Los
filtros preconfigurados son:

  1. Todas las _solicitudes de cotización_

  2. Todas las _órdenes de compra_ , con excepción de las canceladas

  3. La _fecha de confirmación el año pasado_ incluye todas las órdenes que se confirmaron el año anterior, incluyendo las órdenes canceladas

  4. La _fecha de la orden_ incluye todas las órdenes, solicitudes de cotización y órdenes de compra (incluyendo las canceladas), dependiendo de su fecha de creación.

  5. La _fecha de confirmación_ incluye todas las órdenes confirmadas, incluso las canceladas, dependiendo de su fecha de confirmación

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando tenga que seleccionar un periodo, puede elegir varios años y, si selecciona al menos un año, también puede elegir varios trimestres y los últimos tres meses del periodo.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si utiliza los filtros <em>Fecha de la orden</em> o <em>Fecha de confirmación</em>, la función <em>Comparación</em> aparece junto a <em>Filtros</em>. Le permite comparar el periodo filtrado con el anterior.</p>
</div> ![Filtros de reporte en Compras de
Konvergo ERP ](../../../../_images/analyze-filters.png)

#### Añadir filtros personalizados

Gracias a las 31 opciones de filtros entre las que puede elegir, las
posibilidades de personalización de sus datos son casi ilimitadas. Vaya a
Filtros ‣ Añadir filtro personalizado, especifique la condición que debe
cumplir la opción de filtrado (por ejemplo, _es igual a_ , _contiene_ , etc.)
y haga clic en _Aplicar_. Si desea seleccionar órdenes que cumplan varias
condiciones a la vez (operador _y_), repita el proceso para añadir otro filtro
personalizado. Si desea utilizar el operador _o_ , no haga clic en _Aplicar_ ,
y en su lugar haga clic en _Añadir una condición_. Una vez que haya incluido
todas las opciones de filtrado deseadas, haga clic en _Aplicar_.

![Filtros de reportes personalizados en Compras de Konvergo ERP
](../../../../_images/analyze-custom-filter.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para evitar tener que volver a crear los filtros personalizados en cada ocasión, guárdelos haciendo clic en Favoritos ‣ Guardar la búsqueda actual ‣ Guardar. A continuación, se puede acceder al filtro de búsqueda personalizado haciendo clic en <em>Favoritos</em> o incluso se puede establecer como filtro predeterminado al acceder al tablero de reportes.</p>
</div>

### Seleccionar las medidas deseadas

Antes de seleccionar las medidas que desea implementar, debe decidir si
prefiere utilizar la vista de gráfico o la vista de tabla dinámica. El tablero
se presenta de forma predeterminada en ambas vistas. Sin embargo, no se
aplicarán las medidas que seleccione a ambas vistas. Puede acceder a cada
vista por separado haciendo clic en los iconos de la parte superior derecha
del tablero.

![Cambiar la vista de reportes en Compras de Konvergo ERP
](../../../../_images/analyze-switch-view.png)

#### Visualizar datos

Puede transformar el gráfico principal con un solo clic al seleccionar uno de
los tres gráficos: barra, línea o circular. Aunque existan catorce medidas
diferentes, solo puede utilizar una a la vez. En cambio, puede agrupar la
medida utilizando uno o varios de los 19 _Grupos_.

![Vista de gráfico de reportes en la aplicación Compras de
Konvergo ERP.](../../../../_images/analyze-graph-view.png)

En el caso de los gráficos de barras y líneas, la medida seleccionada es el
eje Y, y el primer grupo que seleccione se utilizará para crear el eje X. Si
se añaden más grupos, se añaden líneas adicionales (gráfico de líneas) o el
gráfico de barras se transforma en un gráfico de barras apiladas. En el caso
de los gráficos circulares, mientras más grupos se seleccionen, se mostrarán
más secciones.

#### Analizar datos

La vista de tabla dinámica le permite analizar sus datos con gran detalle. Al
contrario de la vista de gráfico, la vista de tabla dinámica permite añadir
varias medidas al mismo tiempo. Si hace clic en los botones de _Medidas_ o _+_
ubicados en la columna de _Total_ , podrá agregar todas las medidas que desee,
cada una en una nueva columna. Si hace clic en el botón _+_ ubicado en la fila
de _Total_ , podrá agregar _Grupos_. Si hace clic en el botón _+_ de un grupo,
podrá añadir un subgrupo y así sucesivamente.

![Vista de tabla dinámica en Compras de Konvergo ERP ](../../../../_images/analyze-
pivot-view.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede insertar su tabla dinámica directamente en la aplicación Hoja de cálculo o exportarla como archivo de Excel.</p>
</div>

