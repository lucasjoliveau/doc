# Posiciones fiscales (mapeo de impuestos y cuentas)

Se establecen los impuestos y cuentas predeterminadas en los productos y
clientes para crear nuevas transacciones al instante. Sin embargo, según la
ubicación y el tipo de negocio de los clientes y proveedores, podría ser
necesario utilizar diferentes impuestos y cuentas para una transacción.

Las **posiciones fiscales** permiten crear reglas que permitan adaptar
automáticamente los impuestos y las cuentas utilizadas para una transacción.

Pueden aplicarse de forma automática, manual, o se pueden asignar a un
contacto.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Existen varias posiciones fiscales predeterminadas que forman parte de su paquete de localización <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">fiscal</span></a>.</p>
</div>

## Configuración

> ### Mapeo de impuestos y cuentas

Si desea editar o crear una posición fiscal, vaya a Contabilidad ‣
Configuración ‣ Posiciones fiscales, y abra el dato a modificar o haga clic en
**Nuevo**.

El mapeo de impuestos y cuentas depende de los impuestos y cuentas
predeterminadas definidas en el formulario del producto.

  * Para asignar a otro impuesto o cuenta, complete la columna de la derecha (**impuesto a aplicar** / **cuenta alternativa**).

![Ejemplo de mapeo de impuestos de una posición
fiscal](../../../../_images/fiscal-positions-tax-mapping.png) ![Ejemplo de
mapeo de cuenta de una posición fiscal](../../../../_images/fiscal-positions-
account-mapping.png)

  * Para eliminar un impuesto, deje vacío el campo **Impuesto a aplicar**.

  * Para sustituir un impuesto por otros, añada varias líneas con el mismo **impuesto sobre el producto**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El mapeo solo funciona con impuestos <em>activos</em>. Por lo tanto, asegúrese de que estén activos en Contabilidad ‣ Configuración ‣ Impuestos.</p>
</div>

## Uso

### Uso automático

Si desea utilizar automáticamente una posición fiscal de acuerdo con una serie
de condiciones, vaya a Contabilidad ‣ Configuración ‣ Posiciones fiscales,
abra la posición fiscal que desea modificar y seleccione **detectar de forma
automática**.

Desde ahí, se pueden activar varias condiciones:

  * **RFC obligatorio** : se debe indicar el RFC del cliente en el formulario de contacto.

  * **Grupo de países** y **País** : la posición fiscal solo se aplicará al país o grupo de países seleccionado.

![Ejemplo de configuración del uso automático de una posición
fiscal](../../../../_images/fiscal-positions-automatic.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los impuestos de las <b>órdenes de comercio electrónico</b> se actualizarán de forma automática una vez que el cliente haya iniciado sesión o completado sus datos de facturación.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La <b>secuencia</b> de las posiciones fiscales define qué posición fiscal se usará si se cumplen todas las condiciones establecidas en varias posiciones fiscales al mismo tiempo.</p>
<p>Por ejemplo, supongamos que la primera posición fiscal de una secuencia afecta al <em>país A</em> mientras que la segunda afecta a un <em>grupo de países</em> que incluye al <em>país A</em>. En ese caso, solo se aplicará la primera posición fiscal a los clientes del <em>país A</em>.</p>
</div>

### Uso manual

Si desea seleccionar una posición fiscal de forma manual, abra una orden de
venta, factura o recibo, vaya a la pestaña **más información** y seleccione la
**posición fiscal** deseada antes de añadir líneas de producto.

![Selección de una posición fiscal en una orden de venta o
factura](../../../../_images/fiscal-positions-manual.png)

### Asignar a un contacto

Para definir qué posición fiscal debe utilizarse de forma predeterminada para
un contacto específico, vaya a Contabilidad ‣ Clientes ‣ Clientes, seleccione
el contacto, abra la pestaña **ventas y compras** y seleccione la **posición
fiscal**.

![Selección de una posición fiscal para un
cliente](../../../../_images/fiscal-positions-customer.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../taxes">Impuestos</a></p></li>
<li><p><a href="taxcloud">Integración con TaxCloud</a> (en Konvergo ERP 17 y posteriores la integración con TaxCloud quedará fuera de servicio)</p></li>
<li><p><a href="B2B_B2C">Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)</a></p></li>
</ul>
</div>

