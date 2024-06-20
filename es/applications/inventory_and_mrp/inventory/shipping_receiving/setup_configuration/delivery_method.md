# Métodos de envío

La configuración de _Métodos de envío_ , si está activa en Odoo, agrega una
opción para calcular el costo de envío de las órdenes de venta y de los
carritos de un comercio electrónico

Cuando se integra con un [transportista
externo](third_party_shipper.html#inventory-shipping-third-party), los precios
de envío se calculan según la información de tarifas y embalaje del
transportista.

Ver también

  * [Configurar un transportista externo](third_party_shipper.html#inventory-shipping-third-party)

  * [Tutoriales de Odoo: precios de envío](https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1)

## Configuración

Instale el módulo _Costos de envío_ para calcular el costo de envío de las
órdenes de venta y comercio electrónico. Para ello, vaya a la aplicación
Aplicaciones desde el tablero principal de Odoo.

Luego, elimine el filtro Aplicaciones y escriba `Costos de envío` en la barra
Buscar… . Después de encontrar el módulo, haga clic en Activar para
instalarlo.

![Instalar el módulo *Costos de envío*.](../../../../../_images/install-
module.png)

## Agregar métodos de envío

Para configurar los métodos de envío, vaya a la aplicación Inventario ‣
Configuración ‣ Métodos de envío.

Nota

Si la opción Métodos de envío no está disponible en el menú desplegable
Configuración, siga estos pasos para verificar que la función está habilitada:

  1. Vaya a la aplicación Inventario ‣ Configuración ‣ Ajustes.

  2. Vaya a la sección Envío y marque la casilla Métodos de envío para activar esta función.

![Habilitar la función *Métodos de envío*, se marca la casilla desde
Configuración > Ajustes.](../../../../../_images/enable-delivery1.png)

En la página Métodos de envío puede agregar un método si hace clic en Nuevo.
Esta acción abre un formulario para que proporcione algunos detalles sobre el
proveedor de envío, como:

  * Método de envío (_campo obligatorio_): el nombre del método de envío (por ejemplo, `tarifa plana de envío`, `entrega el mismo día`, etc.).

  * Proveedor (_campo obligatorio_): seleccione un servicio de entrega (por ejemplo, FedEx) si utiliza un [transportista externo](third_party_shipper.html#inventory-shipping-third-party). Asegúrese de que la integración con el transportista está instalada de manera correcta y seleccione el proveedor en el menú desplegable.

Para obtener más información sobre la configuración de métodos de envío
personalizados como el precio fijo, con reglas o las opciones para recoger en
la tienda, consulte las secciones que se encuentran a continuación.

  * Sitio web: configure métodos de envío para una página de comercio electrónico. Seleccione el sitio web aplicable en el menú desplegable o déjelo vacío para aplicar el método a todas las páginas web.

  * Empresa: si el método de envío debe aplicarse a una empresa en específico, selecciónela en el menú desplegable. Deje el campo vacío para aplicar ese método a todas las empresas.

  * Producto de envío (_campo obligatorio_): el producto que aparece en la línea de la orden de venta como el cargo por el envío.

  * Gratis si el importe de la orden es superior a: al seleccionar esta casilla, el cliente no pagará por el envío si el importe total de su orden es mayor al importe especificado.

Para consultar algunos ejemplos sobre cómo configurar métodos de envío
específicos, consulte las secciones que se encuentran a continuación.

### Precio fijo

Para configurar el mismo precio de envío para todas las órdenes, vaya a la
aplicación Inventario ‣ Configuración ‣ Métodos de envío. Haga clic en Nuevo
y, en el formulario de método de envío, establezca el proveedor como la opción
precio fijo. Al seleccionar esta opción, el campo Precio fijo estará
disponible, allí puede definir el importe de la tarifa fija de envío.

Para habilitar el envío gratuito si el importe de la orden es mayor al
especificado, marque la casilla Gratis si el importe de la orden es superior a
y escriba el importe necesario.

Example

Complete los siguientes campos para configurar una tarifa plana de envío con
un costo de `$20` que pasa a ser gratis si el cliente gasta más de `$100`:

  * Método de envío: `Tarifa plana de envío`.

  * Proveedor: Precio fijo.

  * Precio fijo: `$20.00`.

  * Gratis si el importe de la orden es superior a: `$100.00`.

  * Producto de envío: `[ENVÍO] Tarifa plana`.

![Ejemplo de cómo completar un formulario para un método de
envío.](../../../../../_images/new-shipping-method.png)

### Por reglas

Para calcular el precio del envío con las reglas de precios, establezca el
campo Proveedor en la opción Según las reglas. De forma opcional, puede
ajustar el margen en la tarifa y el margen adicional para incluir costos
adicionales de envío.

#### Crear reglas de precios

Vaya a la pestaña Precios y haga clic en Agregar una línea, esta acción abrirá
la ventana Crear reglas de precios. Aquí la condición relacionada con el peso,
volumen, precio o cantidad del producto se compara con una cantidad definida
para calcular el costo de envío.

Una vez que haya terminado, haga clic en Guardar y crear nuevo para agregar
otra regla o en Guardar y cerrar.

Example

Para que los clientes paguen $20 por el envío de sus órdenes con cinco o menos
productos, establezca la condición como `Cantidad <= 5.00` y el costo de envío
en `$20`.

![La ventana para mostrar una regla de precios. Aquí se establece la condición
y el costo del envío.](../../../../../_images/pricing-rule.png)

Para restringir el envío a ciertos destinos en el sitio web de comercio
electrónico, vaya a la pestaña Disponibilidad de destino en el formulario del
método de envío y defina los países, estados y prefijos de código postal. Deje
estos campos vacíos si puede hacer envíos a cualquier lugar.

#### Calcular costos de envío

El costo de envío es el costo de envío especificado en la regla que cumple con
la condición, sumado a cualquier cargo adicional del margen en la tarifa y el
margen adicional.

\\[Total = costo~de~envío~de~la~regla + (margen~en~la~tarifa \times
costo~de~envío~de~la~regla) + margen~adicional\\]

Example

Con las siguientes dos reglas configuradas:

  1. Si la orden incluye cinco o menos productos, el envío cuesta $20.

  2. Si la orden incluye más de cinco productos, el envío cuesta $50.

El margen en la tarifa es `10%` y el margen adicional es `$9.00`.

![Ejemplo con el método de envío "según las reglas" con los márgenes
configurados.](../../../../../_images/delivery-cost-example.png)

Cuando se aplica la primera regla, el costo de envío es de $31 (20 + (0.1 *
20) + 9) y cuando se aplica la segunda regla, el costo de envío es de $64 (50
+ (0.1 * 50) + 9).

### Recoger en tienda

Para que el cliente pueda ir por su orden a la tienda, seleccione Recoger en
tienda en el campo Proveedor y especifique la ubicación de recolección en
Almacén.

Para facturar al cliente por el costo de envío a la ubicación de recolección,
seleccione la opción Obtener tarifa y crear el envío en el campo Nivel de
integración. Luego, elija la opción Costo estimado o Costo real en el campo
Política de facturación para decidir si el cargo adicional de envío en la
orden de venta es el costo exacto del transportista.

Ver también

[Invoice cost of shipping](../advanced_operations_shipping/invoicing.html)

## Agregar un envío

Las órdenes de venta pueden incluir métodos de envío como si fueran productos
de entrega y aparecen como artículos de línea individuales. Vaya a la orden de
ventas deseada desde la aplicación Ventas ‣ Órdenes ‣ Órdenes.

Haga clic en el botón Agregar envío en la orden de venta. Esto abrirá la
ventana emergente Agregar un método de envío para que elija un método de envío
de la lista.

El peso total del pedido se completa de forma automática con el peso (que debe
definir en la pestaña Inventario de cada formulario de producto) de los
productos. Edite el campo para especificar el peso exacto y después haga clic
en Agregar para establecer el método de envío.

Nota

La cantidad que definió en peso total del pedido sustituye el peso total que
definió en los formularios de cada producto.

El costo de envío aparece en una _línea de la orden de venta_ como el producto
de envío detallado en el formulario del método de envío.

Example

La orden de venta `S00088` incluye `Entrega de muebles`, un producto de envío
con una tarifa fija de `$200`.

> ![La orden de envío en una línea de la orden de
> venta.](../../../../../_images/delivery-product1.png)

### Orden de envío

El método de envío que agregó a la orden de venta está vinculado a los
detalles del transportista en la orden de envío. Para agregar o cambiar el
método de envío desde allí, vaya a la pestaña Información adicional y
modifique el campo Transportista.

![Información del transportista en el formulario de
envío.](../../../../../_images/delivery-order.png)

