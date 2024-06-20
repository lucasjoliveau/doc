# Delivery methods

When activated in Odoo, the _Delivery Methods_ setting adds the option of
calculating the cost of shipping on sales orders and e-commerce shopping
carts.

When integrated with a [third-party
carrier](third_party_shipper.html#inventory-shipping-third-party), shipping
prices are calculated based on the carrier’s pricing and packaging
information.

See also

  * [Third-party shipping carrier setup](third_party_shipper.html#inventory-shipping-third-party)

  * [Odoo Tutorials: Delivery Prices](https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1)

## Configuration

To calculate shipping on sales orders and e-commerce, the _Delivery Costs_
module must be installed. To do so, navigate to the Apps application from the
main Odoo dashboard.

Then, remove the Apps filter, and type in `Delivery Costs` in the Search… bar.
After finding the Delivery Costs module, click Activate to install it.

![Install the *Delivery Costs* module.](../../../../../_images/install-
module.png)

## Add shipping method

To configure delivery methods, go to Inventory app ‣ Configuration ‣ Shipping
Methods.

Note

If the Shipping Methods option is not available from the Configuration drop-
down menu, verify whether the feature is enabled by following these steps:

  1. Go to Inventory app ‣ Configuration ‣ Settings.

  2. Scroll to the Shipping section and enable the Delivery Methods feature by checking the corresponding checkbox.

![Enable the *Delivery Methods* feature by checking the box in Configuration >
Settings.](../../../../../_images/enable-delivery1.png)

On the Shipping Methods page, add a method by clicking New. Doing so opens a
form to provide details about the shipping provider, including:

  * Shipping Method (_Required field_): the name of the delivery method (e.g. `flat-rate shipping`, `same day delivery`, etc.).

  * Provider (_Required field_): choose the delivery service, like Fedex, if using a [third-party carrier](third_party_shipper.html#inventory-shipping-third-party). Ensure the integration with the shipping carrier is properly installed and select the provider from the drop-down menu.

For more details on configuring custom shipping methods, such as fixed price,
based on rules, or pickup in store options, refer to their respective sections
below.

  * Website: configure shipping methods for an e-commerce page. Select the applicable website from the drop-down menu, or leave it blank to apply the method to all web pages.

  * Company: if the shipping method should apply to a specific company, select it from the drop-down menu. Leave the field blank to apply the method to all companies.

  * Delivery Product (_Required field_): the product listed on the sales order line as the delivery charge.

  * Free if order amount is above: checking this box enables free shipping if the customer spends above the specified amount.

For examples on how to configure specific shipping methods, refer to the
sections below.

### Fixed price

To configure a shipping price that is the same for all orders, go to Inventory
app ‣ Configuration ‣ Shipping Methods. Then, click New, and on the shipping
method form, set the Provider to the Fixed Price option. Selecting this option
makes the Fixed Price field become available, which is where the fixed rate
shipping amount is defined.

To enable free shipping if the amount of the order exceeds a specified amount,
check the box Free if order amount is above and fill in the amount.

Example

To set up `$20` flat-rate shipping that becomes free if the customer spends
over `$100`, fill in the following fields:

  * Shipping Method: `Flat-rate shipping`

  * Provider: Fixed Price

  * Fixed Price: `$20.00`

  * Free if order amount is above: `$100.00`

  * Delivery Product: `[SHIP] Flat`

![Example of filling out a shipping method.](../../../../../_images/new-
shipping-method.png)

### Based on rules

To calculate the price of shipping based on pricing rules, set the Provider
field to the Based on Rules option. Optionally, adjust Margin on Rate and
Additional margin to include additional shipping costs.

#### Create pricing rules

Navigate to the Pricing tab and click Add a line. Doing so opens the Create
Pricing Rules window, where the Condition related to the product weight,
volume, price, or quantity is compared to a defined amount to calculate the
Delivery Cost.

Once finished, click either Save & New to add another rule, or Save & Close.

Example

To charge customers $20 in shipping for orders with five or fewer products,
set the Condition to `Quantity <= 5.00`, and the Delivery Cost to `$20`.

![Display window to add a pricing rule. Set a condition and delivery
cost.](../../../../../_images/pricing-rule.png)

To restrict shipping to specific destinations on the eCommerce website, in the
shipping method form, navigate to the Destination Availability tab and define
the Countries, States, and Zip Prefixes. Leave these fields empty if all
locations apply.

#### Calculate delivery cost

Shipping cost is the Delivery cost specified in the rule that satisfies the
Condition, plus any extra charges from the Margin on rate and Additional
margin.

\\[Total = Rule's~Delivery~Cost + (Margin~on~rate \times Rule's~Delivery~Cost)
+ Additional~margin\\]

Example

With the two following rules set up:

  1. If the order contains five or fewer products, shipping is $20

  2. If the order contains more than five products, shipping is $50.

Margin on Rate is `10%` and Additional margin is `$9.00`.

![Show example of "Based on rules" shipping method with margins
configured.](../../../../../_images/delivery-cost-example.png)

When the first rule is applied, the delivery cost is $31 (20 + (0.1 * 20) +
9). When the second rule is applied, the delivery cost is $64 (50 + (0.1 * 50)
+ 9).

### Pickup in store

To configure in-store pickup, select Pickup in store in the Provider field and
specify the pickup location in Warehouse.

To invoice the customer for the shipping cost to the pickup location, choose
the Get Rate and Create Shipment option in the Integration Level field. Then,
pick either the Estimated cost or Real cost radio options in the Invoicing
Policy field to decide whether the added shipping charge on the sales order is
the precise cost from the shipping carrier.

See also

[Invoice cost of shipping](../advanced_operations_shipping/invoicing.html)

## Add shipping

Shipping methods can be added to sales orders in the form of delivery
products, which appear as individual line items. First, navigate to the
desired sales order by going to Sales app ‣ Orders ‣ Orders.

On the sales order, click the Add shipping button, which opens the Add a
shipping method pop-up window. Then, choose a Shipping Method from the list.

The Total Order Weight is pre-filled based on product weights (that are
defined in the Inventory tab for each product form). Edit the field to specify
the exact weight, and then click Add to add the shipping method.

Note

The amount defined in Total Order Weight overwrites the total product weights
defined on the product form.

The shipping cost is added to the _sales order line_ as the Delivery Product
detailed on the shipping method form.

Example

`Furniture Delivery`, a delivery product with a fixed rate of `$200`, is added
to sales order `S00088`.

> ![Show delivery order on the sales order
> line.](../../../../../_images/delivery-product1.png)

### Delivery order

The shipping method added to the sales order is linked to the shipping carrier
details on the delivery order. To add or change the delivery method on the
delivery itself, go to the Additional Info tab and modify the Carrier field.

![Shipping carrier information on the delivery
form.](../../../../../_images/delivery-order.png)

