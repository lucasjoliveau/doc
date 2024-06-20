# Gestionar listas de materiales para variantes de productos

Odoo le permite utilizar una lista de materiales (LdM) para múltiples
variantes del mismo producto. Tener una LdM consolidada para un producto con
variantes ahorra tiempo, pues no es necesario gestionar varias listas de
materiales.

## Activar variantes de producto

Para activar esta función, vaya a Inventario ‣ Configuración ‣ Ajustes y baje
a la sección Productos. Haga clic en la casilla junto a Variantes y haga clic
en Guardar.

Para obtener más información sobre la configuración de variantes de productos,
consulte la documentación de [variantes de
productos](../../../sales/sales/products_prices/products/variants.html).

![Seleccionar "Variantes" desde los ajustes de la aplicación
Inventario.](../../../../_images/product-variants-variants-settings.png)

## Crear atributos personalizados para productos

Una vez que haya activado la función de variantes de productos podrá crear y
editar los atributos de los productos en la página Atributos.

Puede acceder a la página Atributos desde la aplicación Inventario ‣
Configuración ‣ Ajustes, luego deberá hacer clic en el botón Atributos.
También puede acceder desde Inventario ‣ Configuración ‣ Atributos.

Una vez que se encuentre en la página de Atributos podrá hacer clic en un
atributo existente o en Nuevo para crear uno nuevo. Al hacer clic en Nuevo se
abrirá un formulario vacío para personalizar un atributo. En caso de que el
atributo ya exista, solo haga clic en Editar en su formulario para realizar
cambios.

Asigne el Nombre del atributo y elija una Categoría en el menú desplegable
correspondiente. Seleccione las opciones deseadas junto a los campos Tipo de
visualización y Modo de creación de las variantes, después haga clic en
Agregar una línea en la pestaña Valores de atributo para agregar un nuevo
valor.

Truco

En la fila Valor hay una casilla denominada Es valor personalizado. Si está
seleccionada, este valor se reconocerá como un valor personalizado y los
clientes podrán escribir sus solicitudes especiales de personalización al
ordenar esta variante de un producto.

Example

![Pantalla de configuración de atributos de una variante de
producto.](../../../../_images/product-variants-attribute.png)

Haga clic en Guardar una vez que haya agregado todos los valores necesarios.

## Agregar las variantes de producto al formulario

Puede aplicar los atributos creados a variantes específicas en determinados
productos. Para agregar variantes de productos a un producto, vaya al
formulario del producto desde Inventario ‣ Productos ‣ Productos. Para
realizar cambios en el producto, selecciónelo y luego haga clic en la pestaña
Atributos y variantes.

En la sección Atributo, haga clic en Agregar una línea para agregar un nuevo
atributo y selecciónelo de la lista desplegable.

A continuación, en la sección Valores, haga clic en el menú desplegable para
elegir de la lista de valores existentes. Haga clic en cada valor para
agregarlos y repita este proceso para cualquier atributo adicional que deba
agregar al producto.

Una vez que haya terminado, haga clic en Guardar.

![El formulario del producto en la pestaña de Atributos y variantes con los
valores correspondientes.](../../../../_images/product-variants-product-
form.png)

Truco

Los productos de la LdM con distintas variantes que se fabrican de forma
interna deben tener configurada una **regla de reordenamiento de 0,0** , o
tener sus rutas de reabastecimiento configuradas como _Reabastecer sobre
pedido (MTO)_.

## Aplicar componentes de LdM a las variantes de producto

A continuación, cree una nueva LdM o edite una desde Fabricación ‣ Productos ‣
Listas de materiales. Luego, haga clic en Nuevo para abrir un formulario de
lista de materiales y configurar una.

Para agregar un producto a la lista de materiales haga clic en el menú
desplegable del campo Producto y seleccione uno.

Luego agregue los componentes necesarios, haga clic en Agregar una línea en la
sección Componente de la pestaña Componentes y elíjalos con el menú
desplegable.

Elija los valores necesarios en las columnas Cantidad y Unidad de medida del
producto, después seleccione los valores deseados en la columna Aplicar en
variantes.

Nota

La opción Aplicar en variantes para asignar componentes a variantes
específicas del producto en la lista de materiales estará disponible una vez
que haya habilitado la función Variantes desde la aplicación Inventario. Si el
campo Aplicar en variantes no es visible de inmediato, actívelo desde el menú
de opciones adicionales (es el icono de tres puntos ubicado a la derecha de la
fila del encabezado).

![Opción "Aplicar en variantes" en el menú de opciones
adicionales.](../../../../_images/product-variants-apply-on-variants.png)

Cada componente puede asignarse a multiples variantes y en cada variante del
producto se utilizan componentes sin variantes especificadas. El mismo
principio aplica cuando se configuran operaciones y subproductos.

Al definir listas de materiales de variantes por asignación de componentes
debe dejar vacío el campo Variante del producto en la sección principal de la
LdM. Este campo se utiliza _solo_ cuando se crea una LdM específicamente para
una variante del producto.

Haga clic en Guardar en la parte superior del formulario cuando haya realizado
todas las configuraciones necesarias a la lista de materiales.

Truco

Elija en qué operaciones deben consumirse los componentes si solo se aplican a
variantes específicas. Si la columna Consumido en la operación _no_ es visible
de inmediato, actívela desde el menú de opciones adicionales (es el icono de
tres puntos ubicado a la derecha de la fila del encabezado).

## Vender y fabricar variantes de productos de la lista de materiales

Para vender y fabricar variantes de productos de la lista de materiales para
una orden, vaya a Ventas ‣ Nuevo para crear una cotización.

### Vender variantes de productos de la lista de materiales

Una vez que se encuentre en el formulario de cotización, haga clic en el menú
desplegable junto al campo Cliente para agregar uno.

Después, en la pestaña Líneas de la orden, haga clic en Agregar un producto y
seleccione el producto con la LdM del menú desplegable, aparecerá la ventana
emergente para configurar el producto.

Desde la ventana emergente, haga clic en las opciones de atributos deseadas
para configurar la variante correcta a fabricar. Luego, haga clic en los
iconos verdes + o - junto al `1` para cambiar la cantidad a vender y fabricar
en caso de que sea necesario.

![Ventana emergente para configurar un producto, selección de variantes de
atributo.](../../../../_images/product-variants-variant-popup.png)

Haga clic en Agregar una vez que haya elegido todas las especificaciones, esto
cambiará la ventana emergente a otra, la ventana Configurar. Allí aparecerán
los productos opcionales disponibles, en caso de que los haya creado con
anterioridad.

Al terminar, haga clic en Confirmar para cerrar la ventana emergente.

A continuación, haga clic en Guardar y luego en Confirmar en la parte superior
del formulario de cotización para crear y confirmar una nueva orden de venta.

### Fabricar variantes de productos de la lista de materiales

Una vez que haya confirmado la orden de venta aparece el botón inteligente
Fabricación en la parte superior de su formulario. Haga clic en el botón
inteligente Fabricación para abrir el formulario de Orden de fabricación.

En la pestaña Componentes de este formulario se enumeran los componentes
apropiados para la variante elegida y los componentes aparecerán según la
variante que seleccione. Para ver los pasos de operación obligatorios u
opcionales haga clic en la pestaña Órdenes de trabajo.

Para acceder a la vista de la pantalla de órdenes de trabajo en formato
tableta haga clic en el icono de tableta ubicado a la derecha de la fila de la
operación a completar.

Desde la vista de tableta haga clic en Marcar como hecho a medida que la
operación avanza para completar los pasos correspondientes.

También puede hacer clic en el botón Marcar como hecho ubicado en la parte
superior del formulario de la orden de fabricación para completar la orden.

![Orden de fabricación para una variante de producto de lista de
materiales.](../../../../_images/product-variants-manufacturing-order.png)

Luego, regrese a la orden de venta a través de las migas de pan ubicadas en la
parte superior de la página.

Una vez que el producto esté fabricado haga clic en el botón inteligente
Entrega para entregar el producto al cliente. En el formulario de la orden de
entrega, haga clic en Validar y luego en Aplicar para entregar el producto.

Para finalizar la venta, regrese a la orden de venta a través de las migas de
pan ubicadas en la parte superior de la página. Haga clic en Crear factura y
luego otra vez en Crear Factura para facturar la orden al cliente.

  *[LdM]: Lista de materiales

