# Discount and loyalty programs

The Konvergo ERP _Sales_ , _eCommerce_ , and _Point of Sale_ applications allow users
to create discount and loyalty programs that customers can use for online and
in-store shopping. These programs offer more varied, public, and time-
sensitive pricing options than [pricelists](prices/pricing).

## Configure the settings

To begin using discount and loyalty programs, navigate to Sales ‣
Configuration ‣ Settings. Under the **Pricing** heading, activate the
**Discounts, Loyalty & Gift Card** setting by checking the box next to the
feature. Finally, click **Save** to save the changes.

## Configure discount and loyalty programs

To create discount and loyalty programs, go to Sales ‣ Products ‣ Discount &
Loyalty.

If no discount or loyalty programs have been created yet, Konvergo ERP provides a
choice of templates to help create the first program. Choose one of the
template cards, or click **New** to create a new program from scratch.

Or, if there are already existing programs, select an existing program to edit
it.

![Discount and loyalty program template cards.](../../../../_images/price-
discount-loyalty.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Templates only appear when no programs have been created, and they disappear once the first
program is created.</p>
</div>

Creating or editing a program opens the program form.

The program form contains the following options:

  * **Program Name** : Enter the name of the program. The program name is _not_ visible to the customer.

  * **Program Type** : Select the desired program type.

  * **Currency** : Select the currency used for the program.

  * **Points Unit** : Enter the name of the points used for the **Loyalty Cards** program (e.g. `Loyalty Points`). The points unit name _is_ visible to the customer. This field is only available when the **Program Type** is set to **Loyalty Cards**.

  * **Validity** : Select the date until which the program is valid. Leave this field blank for no end date, meaning the program is always valid and does not expire.

  * **Limit Usage** : Check this box and enter a number to limit the number of times the program can be used during the **Validity** period.

  * **Company** : In the case of multiple companies, choose the company for which the program is available.

  * **Available On** : Select the app(s) on which the program is available.

  * **Website** : Select the website(s) on which the program is available. Leave this field blank to make it available on all websites.

  * **Point of Sale** : Select the point(s) of sale at which the program is available. Leave this field blank to make it available at all PoS.

![Program options on the loyalty program form.](../../../../_images/price-
programs.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The options available on the program form vary depending on the <a href="#sales-pricing-management-program-types"><span class="std std-ref">Program Type</span></a> selected.</p>
</div>

All of the existing cards, codes, coupons, etc. that have been generated for
the program are accessible through the smart button located in the upper-right
corner of the form.

![Program items smart button on the loyalty program
form.](../../../../_images/price-programs-items.png)

### Program types

The different **Program Types** available on the program form are:

  * **Coupons** : Generate and share single-use coupon codes that grant immediate access to rewards.

  * **Next Order Coupons** : Generate and share single-use coupon codes that grant access to rewards on the customer’s next order.

  * **Loyalty Cards** : When making purchases, the customer accumulates points to exchange for rewards on current and/or future orders.

  * **Promotions** : Set conditional rules for ordering products, which, when fulfilled, grant access to rewards for the customer.

  * **Discount Code** : Set codes which, when entered upon checkout, grant discounts to the customer.

  * **Buy X Get Y** : For every X item bought, the customer is granted 1 credit. After accumulating a specified amount of credits, the customer can trade them in to receive Y item.

### Conditional rules

Next, configure the **Conditional rules** that determine when the program
applies to a customer’s order.

In the **Rules & Rewards** tab, click **Add** next to **Conditional rules** to
add _conditions_ to the program. This reveals a **Create Conditional rules**
pop-up window.

![Rules & Rewards tab of the loyalty program form.](../../../../_images/price-
conditional-rewards.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The options for <b>Conditional rules</b> vary depending on the selected <a href="#sales-pricing-management-program-types"><span class="std std-ref">Program Type</span></a>.</p>
</div>

The following options are available for configuring conditional rules:

  * **Discount Code** : Enter a custom code to be used for the **Discount Code** program, or use the default one generated by Konvergo ERP. This field is only available when the **Program Type** is set to **Discount Code**.

  * **Minimum Quantity** : Enter the minimum number of products that must be purchased in order to access the reward. Set the minimum quantity to at least `1` to ensure that the customer must make a purchase in order to access the reward.

  * **Minimum Purchase** : Enter the minimum amount (in currency), with **tax Included** or **tax Excluded** , that must be spent in order to access the reward. If both a minimum quantity _and_ minimum purchase amount are entered, then the customer’s order must meet both conditions.

  * **Products** : Select the specific product(s) for which the program applies. Leave this field blank to apply it to all products.

  * **Categories** : Select the category of products for which the program applies. Choose **All** to apply it to all product categories.

  * **Product Tag:** Select a tag to apply the program to products with that specific tag.

  * **Grant** : Enter the number of points the customer earns **per order** , **per currency spent** , or **per unit paid** (for the **Loyalty Cards** and **Buy X Get Y** programs).

![Conditional rules configuration window for a discount or loyalty
program.](../../../../_images/price-conditions.png)

Click **Save & Close** to save the rule and close the pop-up window, or click
**Save & New** to save the rule and immediately create a new one.

### Rewards

In the **Rules & Rewards** tab of the program form, click **Add** next to
**Rewards** to add _rewards_ to the program. This reveals a **Create Rewards**
pop-up window.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The options for <b>Rewards</b> vary depending on the selected <a href="#sales-pricing-management-program-types"><span class="std std-ref">Program Type</span></a>.</p>
</div>

The following options are available for configuring rewards:

  * **Reward Type** : Select the reward type among **Free Product** , **Discount** , and **Free Shipping**. The other options for reward configuration depend on the **Reward Type** selected.

    * **Free Product** :

      * **Quantity Rewarded** : Select the number of free products rewarded to the customer.

      * **Product** : Select the product given for free as a reward. Only one product can be selected.

      * **Product Tag** : Select a tag to further specify the free product eligible for the reward.

    * **Discount** :

      * **Discount** : Enter the discounted amount in either **percentage** , **currency per point** , or **currency per order**. Then, select whether the discount applies to the entire **Order** , only the **Cheapest Product** on the order, or only **Specific Products**.

      * **Max Discount** : Enter the maximum amount (in currency) that this reward may grant as a discount. Leave this field at `0` for no limit.

    * **Free Shipping** :

      * **Max Discount** : Enter the maximum amount (in currency) that this reward may grant as a discount. Leave this field at `0` for no limit.

  * **In exchange of** : Enter the number of points required to exchange for the reward (for the **Loyalty Cards** and **Buy X Get Y** programs).

  * **Description on order** : Enter the description of the reward, which is displayed to the customer upon checkout.

![Rewards configuration window for a discount or loyalty
program.](../../../../_images/price-rewards.png)

  *[PoS]: Point of Sale

