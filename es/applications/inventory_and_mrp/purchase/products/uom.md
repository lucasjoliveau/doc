# Compre en unidades de medida diferentes a las de venta

Puede que su proveedor use una unidad de medida diferente a la que usted
quiera usar cuando venda su producto. Esto puede causar confusión entre los
representantes de ventas y de compras. Además, es una pérdida de tiempo
convertir las medidas manualmente cada vez. Con Odoo, puede configurar su
producto una vez y dejar que Odoo se encargue de la conversión.

Considere los siguientes ejemplos:

  1. Compra jugo de naranja a un vendedor estadounidense en **galones**. Sin embargo, sus clientes son europeos y utilizan **litros**.

  2. Compra cortinas a un proveedor en **rollos** y vende partes de los rollos a sus clientes en **metros cuadrados**.

## Habilitar las unidades de medida

Abra la aplicación Ventas y vaya a Configuración ‣ Ajustes. Abajo del catálogo
del producto, habilite _Unidades de medida_.

![Habilite la opción de unidades de medida en Ventas de
Odoo](../../../../_images/uom-enable-option.png)

## Especificar las unidades de medida de compra y venta

### Unidades de medida estándar

Cuenta con una variedad de unidades de medida disponibles de forma
predeterminada en su base de datos. Cada una pertenece a una de las cinco
categorías de unidades de medida: _Longitud/Distancia_ , _Unidad_ , _Volumen_
, _Peso_ y _Tiempo de trabajo_.

Truco

Puede crear sus nuevas unidades de medida y categorías de unidades de medida
(consulte la siguiente sección).

Para especificar las diferentes unidades de medida para las compras y las
ventas, abra su aplicación de Compra y vaya a Productos ‣ Productos. Cree un
producto o seleccione uno existente. Primero seleccione la _Unidad de medida_
a usar para Ventas (al igual que para otras aplicaciones como Inventario)
debajo de la pestaña _Información general_. Después seleccione la _Unidad de
medida para Compra_ que se va a utilizar para las compras.

Regresando al primer ejemplo, si compra jugo de naranja en **galones** y lo
vende en **litros** , debe seleccionar _L_ (litros) como _Unidad de medida_ y
_gal (US)_ (galones) como _Unidad de medida para compra_ y hacer clic en
_Guardar_.

![Configure las unidades de medida de un producto en Odoo
](../../../../_images/uom-product-configuration.png)

### Crear nuevas unidades y categorías de medida.

A veces necesita crear sus propias unidades y categorías, ya sea porque no
está preconfigurada la medida en Odoo o porque las unidades no están
relacionadas entre ellas (por ejemplo, kilos y centímetros).

En el segundo ejemplo, se compran cortinas en **rollos** y se venden pedazos
de rollos en **metros cuadrados** , por lo que es necesario crear una nueva
categoría de unidades de medida para relacionarlas.

Para hacerlo, vaya a Configuración ‣ Categorías de unidades medida. y nombre
la nueva categoría.

![Cree una nueva categorría de unidades de medida en Compras de
Odoo](../../../../_images/uom-new-category.png)

El siguiente paso es crear dos unidades de medida. Para hacerlo, vaya a
Configuración ‣ Unidades de medida.

Primero, cree la unidad de medida usada como punto de referencia para
convertir las demás unidades de medida dentro de la categoría que acaba de
crear. Seleccione _Referencia de unidad de medida para el tipo de categoría_
como _Tipo_. Establezca la _Precisión de redondeo_ que le gustaría usar. La
cantidad calculada por Odoo siempre será un múltiplo de este valor.

En este ejemplo, como no puede comprar menos de 1 rollo y no usará fracciones
de rollo como unidad de medida, puede ingresar 1.

![Cree una nueva unidad de medida de referencia en Compras de
Odoo](../../../../_images/uom-new-reference-unit.png)

Nota

Si utiliza una _precisión de redondeo_ inferior a 0.01 es posible que aparezca
un mensaje de advertencia indicando que es mayor que la _precisión decimal_ y
que podría causar inconsistencias. Si desea utilizar una _precisión de
redondeo_ menor a 0.01, primero active el [modo de
desarrollador](../../../general/developer_mode.html#developer-mode) y vaya a
Ajustes ‣ Técnico ‣ Estructura de la base de datos ‣ Precisión decimal,
seleccione _Unidad de medida del producto_ y edite los _dígitos_ según
corresponda. Por ejemplo, establezca los _dígitos_ en 5 si desea usar una
precisión de redondeo de 0.00001.

Después cree una segunda unidad de medida, póngale nombre y seleccione la
misma categoría de unidad de medida que su unidad de referencia. Seleccione
_Menor_ o _Mayor que la referencia de unidad de medida_ como _Tipo_ , según su
situación.

Como el rollo de cortina equivale a 100 metros cuadrados, debería seleccionar
_Menor_.

Ahora, debe introducir el _Ratio_ entre su unidad de referencia y la segunda.
Si la segunda unidad es más pequeña, el _Ratio_ debe ser mayor que 1. Si la
segunda unidad es mayor, el ratio debe ser menor que 1.

Para el rollo de cortina, debe establecer un ratio de 100.

![Cree una segunda unidad de medida en Compras de
Odoo](../../../../_images/uom-second-unit.png)

Ahora puede establecer su producto como lo haría con las unidades de medida
estándar de Odoo.

![Establezca una unidad de medida en un producto usando sus propias unidades
en Compras de Odoo](../../../../_images/uom-product-configuration-new-
units.png)

