# Shipping methods

Depending on your shipping strategy, you have the choice to either use your
own shipping methods, or use an integration with an existing shipping
provider.

<div class="alert alert-secondary" id="ecommerce-own-shipping">
<p class="alert-title">
See also</p><p><a href="checkout">Checkout</a></p>
</div>

## Own shipping methods

You can create your own custom shipping methods and define rules to compute
shipping costs. To do so, go to Website ‣ Configuration ‣ Shipping Methods,
and either select an **existing** shipping method, or **Create** one. When
creating a shipping method, you can choose between [Fixed
Price](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method),
[Based on
Rules](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method),
and **Pickup in store**.

### Pickup in store

**Pickup in store** must first be **enabled** in the settings (Website ‣
Configuration ‣ Settings ‣ Shipping section) by checking **On Site Payments &
Picking**. Once enabled, you can select and **Customize Pickup Sites**.
**Picking sites** can be made **website-specific** , but are by default
available for _all_ websites.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method">Delivery methods</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing">Shipping cost invoicing</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack">Multi-package shipments</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel">How to cancel a shipping request to a shipper?</a></p></li>
</ul>
</div>

## Shipping providers

Another solution is to use one of the integrations with an existing shipping
provider. The advantage of using an integration is that delivery costs are
automatically computed based on each order as well as generating shipping
labels.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Third-party shipping carriers</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials">How to get UPS credentials for integration with Konvergo ERP?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials">How to get DHL credentials for integration with Konvergo ERP?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels">Print shipping labels</a></p></li>
</ul>
</div>

## Website availability

Shipping methods can be made available on **specific** websites _only_ , if
desired. To do so, go to Website ‣ Configuration ‣ Settings ‣ Shipping
Methods, and select the desired **shipping method**. In the **Website** field,
set the website you want the shipping method to be restrained to. Leave the
field **empty** for the method to be available on _all_ websites.

## Delivery method at checkout

Customers can choose the shipping method at the end of the checkout process,
at the **Confirm Order** step.

![Delivery method choice at checkout](../../../../_images/shipping-
checkout.png)

