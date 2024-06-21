# Pricelists

Pricelists allow you to adjust product prices depending on various criteria
automatically. For example, you can set POS-specific prices, create temporary
discount periods, reward specific customers, or offer discounts when set
quantities are ordered.

## Configuration

Navigate to the [general POS app
settings](../configuration#configuration-settings) and ensure **Flexible
Pricelists** are enabled under the **Pricing** section.

Multiple prices per product is the default pricelist option for setting simple
fixed price rules per product. Select Advanced price rules (discounts,
formulas) to apply price rules to multiple products at once and to compute
prices dynamically using percentage discounts or more complex formulas in
addition to setting fixed prices.

![Enabling pricelists in the general P0S
settings](../../../../_images/settings1.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The selected pricelist type applies to the entire database, including the <a href="../../sales/products_prices/prices/pricing">Sales</a> and <a href="../../../websites/ecommerce/managing_products/price_management#ecommerce-pricelists"><span class="std std-ref">eCommerce</span></a>
apps.</p>
</div>

### Create pricelists

Go to Point of Sale ‣ Products ‣ Pricelists and click **New** or select an
existing pricelist. The pricelist setup differs depending on the selected
pricelist option.

#### Multiple prices per product

When pricelists are configured to use the **Multiple prices per product**
option, it is possible to use multiple fixed prices for different products or
their variants depending, if necessary, on one or several conditions. To add a
new price rule to a pricelist:

  1. Click **Add a line** , and select a **product** and its **variant** if needed.

  2. Add the condition(s):

     * a product quantity to be reached by using the **Min. Quantity** column;

     * a determined period during which the pricelist is applied by using the **Start Date** and **End Date** columns.

  3. Add the **Price** to be applied when the conditions are met (if any).

![Setup form of a multiple prices pricelist](../../../../_images/multiple-
prices.png)

#### Advanced price rules

When pricelists are configured to use the **Advanced price rules (discounts,
formulas)** option, it is possible to use percentage discounts/mark-ups and
formulas in addition to using fixed prices. To add a new price rule to a
pricelist, click **Add a line**. In the pop-up windows:

  1. Select a **Computation** method:

     * **Fixed Price** to set a new fixed price (similarly to the **Multiple prices per product** option).

     * **Discount** to compute a percentage discount (e.g., `10.00` %) or mark-up (e.g., `-10.00` %).

     * **Formula** to compute the price according to a formula. It is required to define what the calculation is **based on** (**Sales Price** , **Cost** , or **Other Pricelist**). You can then:

       * Apply a percentage **Discount** or mark-up.

       * Add an **Extra Fee** (e.g., $ `5.00`) or subtract a fixed amount (e.g., $ `-5.00`).

       * Define a [Rounding Method](cash_rounding) by forcing the price after **Discount** to be a multiple of the value set. The **Extra Fee** is applied afterward.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To have the final price end with <code>.99</code>, set the <b>Rounding Method</b> to <code>1.00</code> and
the <b>Extra Fee</b> to <code>-0.01</code>.</p>
</div>

       * Specify the minimum (e.g., $ `20.00` ) and maximum (e.g., $ `50.00` ) profit **Margins** for computations based on **Cost**.

  2. Select on which product(s) the price rule should be **applied** :

     * **All Products**

     * a **Product Category**

     * a **Product**

     * a **Product Variant**

  3. Add conditions, such as a specific quantity to reach for the price to change by using the **Min. Quantity** field or a specific period during which the pricelist should be applied by using the **Validity** fields.

![Setup form to configure an advanced pricelist](../../../../_images/price-
rules.png)

### Select pricelists

Go to the [specific POS settings](../configuration#configuration-
settings) and add all the available pricelists in the **Available** field.
Then, set its **default pricelist** in the **Default** field.

When you [open a POS session](../../point_of_sale#pos-session-start),
click the **pricelists** button, and select the desired pricelist from the
list.

![Button to select a pricelist on the POS
frontend](../../../../_images/pricelist-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Multiple pricelists must be selected for the <b>pricelist button</b> to be displayed.</p></li>
<li><p>If a pricelist is selected on a POS order while its conditions are <b>not</b> met, the price will
<b>not</b> be adjusted.</p></li>
</ul>
</div>
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can also set a pricelist to be selected automatically once a specific <a href="../../point_of_sale#pos-customers"><span class="std std-ref">customer is set</span></a>. To do so, go to the customer form and switch to the preferred pricelist in the
<b>Pricelist</b> field of the <b>Sales &amp; Purchase</b> tab.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../sales/products_prices/prices/pricing">Pricelists, discounts, and formulas</a></p></li>
<li><p><a href="../../../websites/ecommerce/managing_products/price_management#ecommerce-pricelists"><span class="std std-ref">How to use pricelists in an ecommerce environment</span></a></p></li>
</ul>
</div>

