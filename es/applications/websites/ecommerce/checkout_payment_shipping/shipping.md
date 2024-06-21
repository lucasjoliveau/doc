# Métodos de envío

Según su estrategia de envío, puede elegir entre métodos de envío propios, o
puede usar une integración con un proveedor de envíos existente.

<div class="alert alert-secondary" id="ecommerce-own-shipping">
<p class="alert-title">
Ver también</p><p><a href="checkout">Proceso de pago</a></p>
</div>

## Métodos de envío propios

Puede crear sus propios métodos de envío personalizados y definir reglas para
calcular los costos de envío. Para hacerlo, vaya a Sitio web ‣ Configuración
‣Métodos de envío, donde puede seleccionar un método de envío **existente** ,
o **crear** uno. Si decide crear un método de envío, podrá elegir entre un
[precio
fijo](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method),
con base en reglas, o **recoger en tienda**.

### Recoger en tienda

Primero debe **activar** la opción **Recoger en tienda** en los ajustes (Sitio
web ‣ Configuración ‣ Ajustes ‣ Envío), solo tiene que hacer clic en **Pagos y
recolección en tienda física**. Una vez que lo haya activado, puede
seleccionar y **personalizar sitios de recolección**. **Los sitios de
recolección** pueden ser **específicos para el sitio web** , pero de manera
predeterminada están disponibles en _todos_ los sitios web.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method">Métodos de envío</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing">Facturación del costo de envío</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack">Envío en varios paquetes</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel">¿Cómo cancelar una solicitud de envío a un transportista?</a></p></li>
</ul>
</div>

## Proveedores de envío

Otra solución es utilizar alguna de las integraciones con un proveedor de
envío existente. La ventaja de utilizar una integración es que los costos de
envío se calculan de forma automática según cada orden y también se generan
sus etiquetas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Transportistas externos</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials">¿Cómo obtener las credenciales de UPS para la integración con Konvergo ERP?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials">¿Cómo obtener las credenciales de DHL para la integración con Konvergo ERP?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels">Imprimir etiquetas de envío</a></p></li>
</ul>
</div>

## Disponibilidad para sitio web

Los métodos de envío se pueden habilitar _solo_ en sitios web **específicos**
si así lo quiere. Para hacerlo, debe ir a Sitio web ‣ Configuración ‣ Ajustes
‣ Envío, y seleccione el **método de envío** deseado. En el campo **Sitio
web** seleccione el sitio web al cual quiere que se limite este método de
envío. Si lo deja **vacío** el método de envío estará disponible en **todos**
los sitios web.

## Método de entrega al finalizar la compra

Los clientes puede elegir el método de envío al final del proceso de pago, al
llegar al paso **Confirmar orden**.

![Elección del método de entrega al finalizar la
compra](../../../../_images/shipping-checkout.png)

