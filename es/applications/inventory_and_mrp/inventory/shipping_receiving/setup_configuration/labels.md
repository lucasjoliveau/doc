# Imprimir etiquetas de envío

Integrar Konvergo ERP con [transportistas de terceros](third_party_shipper) para
imprimir etiquetas de envío que incluyan precio, dirección de destino, números
de rastreo y códigos de barra.

## Configuración

Para generar etiquetas para transportistas de terceros, primero [instale el
conector del transportista externo](third_party_shipper). Después,
configure y active el [método de entrega](third_party_shipper#inventory-
shipping-receiving-configure-delivery-method), asegúrese de configurar el
**Nivel de integración** a **Obtener tarifas y crear envíos** para generar
etiquetas de envío. Finalmente, ingrese la [dirección de
origen](third_party_shipper#inventory-shipping-receiving-configure-
source-address) de la empresa y [el peso de los
productos](third_party_shipper#inventory-shipping-receiving-configure-
weight).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="third_party_shipper">Transportistas externos</a></p>
</div> ![Configure la opción "Obtener tarifas y crear
envíos".](../../../../../_images/integration-level.png)

## Imprimir etiquetas de rastreo

Las etiquetas de rastreo se generan después de que se valida la orden de
entrega.

Si tiene instaladas tanto las aplicación _Ventas_ como _Inventario_ , primero
vaya a Ventas y abra la cotización a la que desea agregar el costo de envío,
confirme la orden de venta y valide la |orden de envío|.

Si solo tiene la aplicación _Inventario_ instalada, cree **órdenes de envío**
directamente en la aplicación Inventario, agregue el transportista externo en
el campo **Transportista** y valide la |orden de envío|.

### Agregar un envío en la cotización.

Para generar una etiqueta de rastreo para una orden, primero cree una
cotización en Ventas ‣ Órdenes ‣ Cotizaciones, haga clic en **Nuevo** y llene
el formulario de cotización. Después, haga clic en **Agregar envío** en la
esquina inferior derecha de la cotización.

![Visualización el botón "Agregar envío" en la
cotización.](../../../../../_images/add-shipping-button.png)

En la ventana emergente resultante, seleccione el transportista deseado desde
el menú desplegable **Método de envío**. Al hacer clic en **Obtener tarifa**
se mostrará el costo de envío para el cliente, en el campo **Costo** del
transportista.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si al hacer clic en <b>Obtener tarifa</b> aparece un error, asegúrese de que la <a href="third_party_shipper#inventory-shipping-receiving-configure-source-address"><span class="std std-ref">dirección del almacén</span></a> y el <a href="third_party_shipper#inventory-shipping-receiving-configure-weight"><span class="std std-ref">peso de los productos de la orden</span></a> estén bien configurados.</p>
</div>

Haga clic en **Agregar** para agregar los costos a la cotización, que está
enlistada como [producto de entrega
configurado](delivery_method#inventory-shipping-receiving-delivery-
product). Finalmente, haga clic en **Confirmar** en la cotización y haga clic
en el botón inteligente **Entrega** para ingresar a la |orden de envío|.

![Visualización de la ventana emergente "Obtener
tarifa".](../../../../../_images/get-rate.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para usuarios que no tengan la aplicación <em>Ventas</em> instalada, el transportista se especifica en la orden de entrega del campo <b>Transportista</b> de la pestaña <b>Información adicional</b>.</p>
<img alt='Mostrar la pestaña "información adicional" de la orden de entrega.' class="align-center" src="../../../../../_images/additional-info-tab.png"/>
</div>

### Validar la orden de entrega

En un formulario de orden de entrega, vaya a la pestaña **Información
adicional** para asegurarse de que el transportista externo se agregó al campo
**Transportista**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si la aplicación <em>Ventas</em> no está instalada, el transportista se configura en el campo <b>Transportista</b>.</p>
</div>

Después de que los artículos en la orden se hayan empaquetado, haga clic en
**Validar** para obtener el número de rastreo y generar una etiqueta de envío.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cree o seleccione una orden de envío existente en la aplicación Inventario y seleccione la tarjeta <b>órdenes de envío</b>.</p>
</div>

El número **Referencia de rastreo** se genera en la pestaña **Información
adicional** de la orden de entrega. Haga clic en el botón inteligente
**Seguimiento** para acceder al enlace de seguimiento del sitio web del
transportista.

La etiqueta de rastreo se encuentra en formato PDF en el chatter.

![Visualización de la etiqueta de envío generada en el
chatter.](../../../../../_images/shipping-label.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para envío de múltiples paquetes, se genera una etiqueta por paquete. Cada etiqueta aparece en el chatter.</p>
</div>

![Etiqueta de ejemplo generada desde el conector de envío de Konvergo ERP con
FedEx.](../../../../../_images/sample-label.png)

Etiqueta de ejemplo generada desde el conector de envío de Konvergo ERP con FedEx.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../advanced_operations_shipping/invoicing">Facturación del costo de envío</a></p></li>
<li><p><a href="../advanced_operations_shipping/multipack">Envío en varios paquetes</a></p></li>
</ul>
</div>

