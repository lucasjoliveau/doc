# Impuestos flexibles (posiciones fiscales)

Al dirigir una empresa tal vez necesite aplicar distintos impuestos y
registrar transacciones en varias cuentas según la ubicación y el tipo de
negocio de sus clientes y proveedores.

La función **posiciones fiscales** le permite establecer reglas que
seleccionan de forma automática los impuestos y cuentas correctas que se
utilizarán en cada transacción.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../finance/accounting/taxes/fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p></li>
<li><p><a href="../../../finance/accounting/taxes">Impuestos</a></p></li>
</ul>
</div>

## Configuración

Para habilitar la función, vaya a Punto de venta ‣ Configuración ‣ Ajustes,
baje a la sección **Contabilidad** y habilite la función **impuestos
flexibles**.

Después, en el campo **predeterminado** establezca una posición fiscal
predeterminada que se debería aplicar a todas las ventas en el PdV
seleccionado. También puede agregar más posiciones fiscales para seleccionar
en el campo **permitido**.

![../../../../_images/flexible-taxes-
setting.png](../../../../_images/flexible-taxes-setting.png)

Según el [paquete de localización
fiscal](../../../finance/fiscal_localizations) que activó, hay varias
posiciones fiscales preconfiguradas que se pueden establecer y utilizar en
PdV. Sin embargo, también puede [crear nuevas posiciones
fiscales](../../../finance/accounting/taxes/fiscal_positions#fiscal-
positions-mapping).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no establece una posición fiscal, el impuesto permanece como se definió en el campo <b>impuestos de cliente</b> en el formulario del producto.</p>
</div>

## Usar posiciones fiscales

Abra una [sesión de PdV](../../point_of_sale#pos-session-start) para
utilizar una de las posiciones fiscales permitidas. Luego, haga clic en el
botón **impuesto** a lado del icono con forma de **libro** y seleccione una
posición fiscal de la lista. Hacer esto aplica las reglas definidas de forma
automática a todos los productos sometidos a las regulaciones de la posición
fiscal elegida.

![../../../../_images/set-tax.png](../../../../_images/set-tax.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si se establece una posición fiscal predeterminada, el botón «impuesto» muestra el nombre de la posición fiscal.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../finance/accounting/taxes/fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p>
</div>

