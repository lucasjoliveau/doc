# Impuestos

Hay varios tipos de **impuestos** , y su uso varía mucho, esto depende
principalmente de la ubicación de su empresa. Para asegurarse de que se
registran correctamente, el sistema de impuestos de Konvergo ERP es compatible con
todo tipo de usos y cálculos.

## Impuestos predeterminados

Los **Impuestos predeterminados** definen cuáles impuestos se seleccionan
automáticamente cuando no hay ninguna otra indicación sobre qué impuesto usar.
Por ejemplo, Konvergo ERP completa previamente el campo **Impuestos** con los
impuestos predeterminados cuando se crea un nuevo producto o se añade una
nueva línea en una factura.

![Konvergo ERP completa el campo "impuestos" de forma automática según los impuestos
predeterminados](../../../_images/default-invoice-line.png)

Si desea cambiar sus **impuestos predeterminados** , vaya a Contabilidad ‣
Configuración ‣ Ajustes ‣ Impuestos ‣ Impuestos predeterminados, seleccione
los impuestos apropiados para su **impuesto de venta** e **impuesto de
compra** , y haga clic en _Guardar_.

![Defina qué impuestos se utilizan de forma predeterminada en
Konvergo ERP](../../../_images/default-configuration.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los <b>impuestos predeterminados</b> se configuran de forma automática según el país seleccionado en la creación de su base de datos, o al configurar un <a href="../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">paquete de localización fiscal</span></a> para su empresa.</p>
</div>

## Activar los impuestos sobre la venta desde la vista de lista

Como parte de su [paquete de localización
fiscal](../fiscal_localizations#fiscal-localizations-packages), la
mayoría de los impuestos de ventas de su país ya están preconfigurados en su
base de datos. Sin embargo, solo algunos de ellos están activados de forma
predeterminada, de esta forma puede activar solo los que sean relevantes para
su empresa.

Para activar los impuestos de venta, vaya a Contabilidad ‣ Configuración ‣
Impuestos y utilice el botón _activar_ para activar o desactivar un impuesto.

![Impuestos preconfigurados activos en la aplicación Contabilidad de
Konvergo ERP](../../../_images/list.png)

## Configuración

Si desea editar o crear un **impuesto** , vaya a Contabilidad ‣ Configuración
‣ Impuestos, abra un impuesto o haga clic en _crear_.

![Modo de edición de un impuesto en la aplicación Contabilidad de
Konvergo ERP](../../../_images/edit.png) <div class="alert alert-warning" id="taxes-labels">
<p class="alert-title">
Importante</p><p>Los impuestos tienen tres etiquetas diferentes, cada una con un uso específico. Consulte la siguiente tabla para ver en qué lugar aparecen.</p>
<table class="table docutils">
<colgroup>
<col style="width: 26%"/>
<col style="width: 37%"/>
<col style="width: 37%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><a href="#taxes-name"><span class="std std-ref">Nombre del impuesto</span></a></p></th>
<th class="head"><p><a href="#taxes-label-invoices"><span class="std std-ref">Etiqueta en la factura</span></a></p></th>
<th class="head"><p><a href="#taxes-tax-group"><span class="std std-ref">Grupo de impuestos</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Backend</p></td>
<td><p>La columna <em>impuestos</em> en las facturas exportadas</p></td>
<td><p>Arriba de la línea <em>total</em> en las facturas exportadas</p></td>
</tr>
</tbody>
</table>
</div>

### Opciones principales

#### Nombre del impuesto

El **nombre del impuesto** tal y como lo quiere mostrar a los usuarios del
backend. Esta es la etiqueta que se ve mientras se editan las órdenes de
venta, facturas, productos, etc.

#### Cálculo de impuestos

  * **Grupos de impuestos**

El impuesto es una combinación de varios subimpuestos. Puede agregar tantos
impuestos como desee, en el orden en el que desee que se apliquen.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de que la secuencia de impuestos es correcta, ya su orden puede afectar al cálculo de los importes de los impuestos, en especial si uno de los impuestos <a href="#taxes-base-subsequent"><span class="std std-ref">afecta a la base de los siguientes</span></a>.</p>
</div>

  * **Fijo**

El impuesto tiene un importe fijo en la divisa predeterminada. El importe
sigue siendo el mismo, independientemente del precio de venta.

Por ejemplo, si un producto tiene un precio de venta de $1000, y aplicamos un
impuesto fijo de _$10_. El resultado es:

Precio de venta del producto | Precio sin impuestos | Impuesto | Total  
---|---|---|---  
1,000 | 1,000 | 10 | 1,010.00  
  * **Porcentaje del precio**

El _precio de venta_ es la base del impuesto: el importe del impuesto se
calcula multiplicando el precio de venta por el porcentaje del impuesto.

Por ejemplo, si un producto tiene un precio de venta de $1000, y aplicamos un
impuesto del _10% del precio_. Tendremos entonces:

Precio de venta del producto | Precio sin impuestos | Impuesto | Total  
---|---|---|---  
1,000 | 1,000 | 100 | 1,100.00  
  * **Porcentaje del precio con impuestos incluidos**

El _total_ es la base del impuesto: el importe del impuesto es un porcentaje
del total.

Por ejemplo, si un producto tiene un precio de venta de $1000 y aplicamos un
impuesto del _10% del precio incluido_. Tendremos:

Precio de venta del producto | Precio sin impuestos | Impuesto | Total  
---|---|---|---  
1,000 | 1,000 | 111.11 | 1,111.11  

#### Activo

Solo se pueden agregar impuestos **activos** a los nuevos documentos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>No es posible eliminar los impuestos que ya se han utilizado. En su lugar, puede desactivarlos para evitar su uso en el futuro.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Este campo se puede modificar desde la <em>vista de lista</em>. Consulte <a href="#taxes-list-activation"><span class="std std-ref">esta sección</span></a> para obtener más información.</p>
</div>

#### Ámbito del impuesto

El **ámbito del impuesto** determina el uso del impuesto, lo cual también
limita su visualización.

  * **Ventas** : facturas de clientes, impuestos de productos de clientes, etc.

  * **Compra** : facturas de proveedores, impuestos de proveedores de productos, etc.

  * **Ninguno**

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede utilizar la opción <b>ninguno</b> para los impuestos que desee incluir en un <a href="#taxes-computation"><span class="std std-ref">grupo de impuestos</span></a> pero que no desee incluir en la lista junto con los otros impuestos de venta o compra.</p>
</div>

### Pestaña de definición

Asigne el importe de la base del impuesto o los porcentajes del impuesto
calculado a varias cuentas y tablas de impuestos.

![Asignación de importes de impuestos en las cuentas y tablas de impuestos
correctas](../../../_images/definition.png)

  * **Basado en** :

    * Base: el precio en la línea de factura

    * % de impuesto: un porcentaje del impuesto calculado.

  * **Cuenta** : si está definida, se registra un apunte contable adicional.

  * **Tablas de impuestos** : se usan para generar [reportes de impuestos](reporting/tax_returns) de forma automática, de acuerdo a las normativas de su país.

### Pestaña de opciones avanzadas

#### Etiqueta en facturas

La etiqueta del impuesto, como se muestra en cada línea de la factura en la
columna **impuestos**. Esta es la etiqueta visible para los usuarios del
_frontend_.

![La etiqueta en las facturas se muestra en cada línea de la
factura](../../../_images/invoice-label.png)

#### Grupo de impuestos

Seleccione a qué **grupo de impuestos** pertenece el impuesto. El nombre del
grupo de impuestos es la etiqueta que se muestra encima de la línea _total_ en
las facturas exportadas y en los portales de clientes.

Los grupos de impuestos incluyen diferentes repeticiones del mismo impuesto.
Esto puede ser útil cuando se debe registrar de forma diferente el mismo
impuesto según las [posiciones fiscales](taxes/fiscal_positions).

![El nombre del grupo de impuestos es distinto al de la etiqueta en las
facturas](../../../_images/invoice-tax-group.png)

En el ejemplo anterior, vemos un impuesto del 0% para los clientes
intracomunitarios en Europa. Registra importes en cuentas específicas y con
tablas de impuestos específicas. Aun así, para el cliente, es un impuesto del
0%. Por eso la Etiqueta de la factura indica _0% EU_ , y el nombre del grupo
de impuestos, sobre la línea _Total_ , indica _0%_.

#### Incluir en el costo analítico

Si activa esta opción, el importe del impuesto se asigna a la misma **cuenta
analítica** que la línea de factura.

#### Incluido en el precio

Si activa esta opción, el total (con impuestos incluidos) es igual al **precio
de venta**.

Total = Precio de venta = Precio calculado sin impuestos incluidos + Impuesto

Por ejemplo, un producto tiene un precio de venta de $1000, y aplicamos un
impuesto del _10% del precio_ , que está _incluido en el precio_. Entonces
tenemos:

Precio de venta del producto | Precio sin impuestos | Impuesto | Total  
---|---|---|---  
1,000 | 900.10 | 90.9 | 1,000.00  
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si necesita definir los precios con precisión, tanto con o sin impuestos, consulte la siguiente documentación: <a href="taxes/B2B_B2C">Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p><b>Facturas</b>: de forma predeterminada, los subtotales de línea mostrados en sus facturas son <em>sin impuestos incluidos</em>. Para mostrar los subtotales de línea <em>con impuestos incluidos</em>, vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Facturas de clientes, y seleccione <em>con impuestos incluidos</em> en el campo <b>distribución de impuestos de los subtotales de línea</b>, luego haga clic en <em>guardar</em>.</p></li>
<li><p><b>Comercio electrónico</b>: de forma predeterminada, los precios mostrados en su sitio web de comercio electrónico son <em>sin impuestos incluidos</em>. Para mostrar los precios <em>con impuestos incluidos</em>, vaya a Sitio web ‣ Configuración ‣ Ajustes ‣ Precios, y seleccione <em>con impuestos incluidos</em> en el campo <b>precios de los productos</b>, luego haga clic en <em>guardar</em>.</p></li>
</ul>
</div>

#### Afectación a la base de los impuestos subsecuentes

Con esta opción, el total de impuestos incluidos se convierte en la base del
impuesto de los demás impuestos aplicados al mismo producto.

Puede configurar un nuevo grupo de impuestos que incluya este impuesto, o
agregarlo directamente a una línea de producto.

![El impuesto se considera como base del IVA del
21%](../../../_images/subsequent-line.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El orden en el que se añaden los impuestos en una línea de producto no tiene ningún efecto sobre el cálculo de los importes. Si añade los impuestos directamente en una línea de producto, solo la secuencia de impuestos determina el orden en que se aplican.</p>
<p>Para reorganizar la secuencia, vaya a Contabilidad ‣ Configuración ‣ Impuestos, y arrastre y suelte las líneas junto a los nombres de los impuestos.</p>
<img alt="La secuencia de los impuestos en Konvergo ERP determina qué impuestos se aplican primero" src="../../../_images/list-sequence.png"/>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="taxes/fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p></li>
<li><p><a href="taxes/B2B_B2C">Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)</a></p></li>
<li><p><a href="taxes/taxcloud">Integración con TaxCloud</a> (en Konvergo ERP 17 y posteriores la integración con TaxCloud quedará fuera de servicio)</p></li>
<li><p><a href="reporting/tax_returns">Declaración de impuestos</a></p></li>
</ul>
</div>

  * [Impuestos de base de efectivo](taxes/cash_basis)
  * [Retención fiscal](taxes/retention)
  * [Comprobar un número de IVA (sistema VIES)](taxes/vat_verification)
  * [Posiciones fiscales (mapeo de impuestos y cuentas)](taxes/fiscal_positions)
  * [Integración con AvaTax](taxes/avatax)
    * [Uso de AvaTax](taxes/avatax/avatax_use)
    * [Portal de Avalara (AvaTax)](taxes/avatax/avalara_portal)
  * [Integración con TaxCloud](taxes/taxcloud)
  * [Ventas a distancia intracomunitarias en la UE](taxes/eu_distance_selling)
  * [Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)](taxes/B2B_B2C)

