# Delivery methods

When activated in Konvergo ERP, the _Delivery Methods_ setting adds the option of
calculating the cost of shipping on sales orders and e-commerce shopping
carts.

When integrated with a [third-party
carrier](third_party_shipper#inventory-shipping-third-party), shipping
prices are calculated based on the carrier’s pricing and packaging
information.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="third_party_shipper#inventory-shipping-third-party"><span class="std std-ref">Third-party shipping carrier setup</span></a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1">Konvergo ERP Tutorials: Delivery Prices</a></p></li>
</ul>
</div>

## Configuration

To calculate shipping on sales orders and e-commerce, the _Delivery Costs_
module must be installed. To do so, navigate to the Apps application from the
main Konvergo ERP dashboard.

Then, remove the **Apps** filter, and type in `Delivery Costs` in the
**Search…** bar. After finding the **Delivery Costs** module, click
**Activate** to install it.

![Install the *Delivery Costs* module.](../../../../../_images/install-
module.png)

## Add shipping method

To configure delivery methods, go to Inventory app ‣ Configuration ‣ Shipping
Methods.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the <b>Shipping Methods</b> option is not available from the <b>Configuration</b>
drop-down menu, verify whether the feature is enabled by following these steps:</p>
<ol class="arabic simple">
<li><p>Go to Inventory app ‣ Configuration ‣ Settings.</p></li>
<li><p>Scroll to the <b>Shipping</b> section and enable the <b>Delivery Methods</b> feature
by checking the corresponding checkbox.</p></li>
</ol>
<img alt="Enable the *Delivery Methods* feature by checking the box in Configuration &gt; Settings." class="align-center" src="../../../../../_images/enable-delivery1.png"/>
</div>

On the **Shipping Methods** page, add a method by clicking **New**. Doing so
opens a form to provide details about the shipping provider, including:

  * **Shipping Method** (_Required field_): the name of the delivery method (e.g. `flat-rate shipping`, `same day delivery`, etc.).

  * **Provider** (_Required field_): choose the delivery service, like Fedex, if using a [third-party carrier](third_party_shipper#inventory-shipping-third-party). Ensure the integration with the shipping carrier is properly installed and select the provider from the drop-down menu.

For more details on configuring custom shipping methods, such as fixed price,
based on rules, or pickup in store options, refer to their respective sections
below.

  * **Website** : configure shipping methods for an e-commerce page. Select the applicable website from the drop-down menu, or leave it blank to apply the method to all web pages.

  * **Company** : if the shipping method should apply to a specific company, select it from the drop-down menu. Leave the field blank to apply the method to all companies.

  * **Delivery Product** (_Required field_): the product listed on the sales order line as the delivery charge.

  * **Free if order amount is above** : checking this box enables free shipping if the customer spends above the specified amount.

For examples on how to configure specific shipping methods, refer to the
sections below.

### Fixed price

To configure a shipping price that is the same for all orders, go to Inventory
app ‣ Configuration ‣ Shipping Methods. Then, click **New** , and on the
shipping method form, set the **Provider** to the **Fixed Price** option.
Selecting this option makes the **Fixed Price** field become available, which
is where the fixed rate shipping amount is defined.

To enable free shipping if the amount of the order exceeds a specified amount,
check the box **Free if order amount is above** and fill in the amount.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To set up <code>$20</code> flat-rate shipping that becomes free if the customer spends over <code>$100</code>, fill in
the following fields:</p>
<ul>
<li><p><b>Shipping Method</b>: <code>Flat-rate shipping</code></p></li>
<li><p><b>Provider</b>: <b>Fixed Price</b></p></li>
<li><p><b>Fixed Price</b>: <code>$20.00</code></p></li>
<li><p><b>Free if order amount is above</b>: <code>$100.00</code></p></li>
<li><p><b>Delivery Product</b>: <code>[SHIP] Flat</code></p></li>
</ul>
<img alt="Example of filling out a shipping method." class="align-center" src="../../../../../_images/new-shipping-method.png"/>
</div>

### Based on rules

To calculate the price of shipping based on pricing rules, set the
**Provider** field to the **Based on Rules** option. Optionally, adjust
**Margin on Rate** and **Additional margin** to include additional shipping
costs.

#### Create pricing rules

Navigate to the **Pricing** tab and click **Add a line**. Doing so opens the
**Create Pricing Rules** window, where the **Condition** related to the
product weight, volume, price, or quantity is compared to a defined amount to
calculate the **Delivery Cost**.

Once finished, click either **Save & New** to add another rule, or **Save &
Close**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To charge customers $20 in shipping for orders with five or fewer products, set the
<b>Condition</b> to <code>Quantity &lt;= 5.00</code>, and the <b>Delivery Cost</b> to <code>$20</code>.</p>
<img alt="Display window to add a pricing rule. Set a condition and delivery cost." class="align-center" src="../../../../../_images/pricing-rule.png"/>
</div>

To restrict shipping to specific destinations on the eCommerce website, in the
shipping method form, navigate to the **Destination Availability** tab and
define the **Countries** , **States** , and **Zip Prefixes**. Leave these
fields empty if all locations apply.

#### Calculate delivery cost

Shipping cost is the **Delivery cost** specified in the rule that satisfies
the **Condition** , plus any extra charges from the **Margin on rate** and
**Additional margin**.

\\[Total = Rule's~Delivery~Cost + (Margin~on~rate \times Rule's~Delivery~Cost)
+ Additional~margin\\]

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>With the two following rules set up:</p>
<ol class="arabic simple">
<li><p>If the order contains five or fewer products, shipping is $20</p></li>
<li><p>If the order contains more than five products, shipping is $50.</p></li>
</ol>
<p><b>Margin on Rate</b> is <code>10%</code> and <b>Additional margin</b> is <code>$9.00</code>.</p>
<img alt='Show example of "Based on rules" shipping method with margins configured.' class="align-center" src="../../../../../_images/delivery-cost-example.png"/>
<p>When the first rule is applied, the delivery cost is $31 (20 + (0.1 * 20) + 9). When the second
rule is applied, the delivery cost is $64 (50 + (0.1 * 50) + 9).</p>
</div>

### Pickup in store

To configure in-store pickup, select **Pickup in store** in the **Provider**
field and specify the pickup location in **Warehouse**.

To invoice the customer for the shipping cost to the pickup location, choose
the **Get Rate and Create Shipment** option in the **Integration Level**
field. Then, pick either the **Estimated cost** or **Real cost** radio options
in the **Invoicing Policy** field to decide whether the added shipping charge
on the sales order is the precise cost from the shipping carrier.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../advanced_operations_shipping/invoicing">Invoice cost of shipping</a></p>
</div>

## Add shipping

Shipping methods can be added to sales orders in the form of delivery
products, which appear as individual line items. First, navigate to the
desired sales order by going to Sales app ‣ Orders ‣ Orders.

On the sales order, click the **Add shipping** button, which opens the **Add a
shipping method** pop-up window. Then, choose a **Shipping Method** from the
list.

The **Total Order Weight** is pre-filled based on product weights (that are
defined in the **Inventory** tab for each product form). Edit the field to
specify the exact weight, and then click **Add** to add the shipping method.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The amount defined in <b>Total Order Weight</b> overwrites the total product weights defined
on the product form.</p>
</div>

The shipping cost is added to the _sales order line_ as the **Delivery
Product** detailed on the shipping method form.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><code>Furniture Delivery</code>, a delivery product with a fixed rate of <code>$200</code>, is added to sales order
<code>S00088</code>.</p>
<blockquote>
<div><img alt="Show delivery order on the sales order line." class="align-center" src="../../../../../_images/delivery-product1.png"/>
</div></blockquote>
</div>

### Delivery order

The shipping method added to the sales order is linked to the shipping carrier
details on the delivery order. To add or change the delivery method on the
delivery itself, go to the **Additional Info** tab and modify the **Carrier**
field.

![Shipping carrier information on the delivery
form.](../../../../../_images/delivery-order.png)

