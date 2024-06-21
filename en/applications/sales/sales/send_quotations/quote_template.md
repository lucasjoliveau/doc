# Quotation templates

In Konvergo ERP _Sales_ , salespeople have the ability to create reusable quotation
templates for common products or services that the business offers.

By using these templates, quotations can be tailored and sent to customers at
a much faster pace, without having to create new quotations from scratch every
time a sales negotiation occurs.

## Configuration

Begin by activating the setting in Sales app ‣ Configuration ‣ Settings, and
scroll to the **Quotations & Orders** heading.

In that section, check the box beside the **Quotation Templates** option.
Doing so reveals a new **Default Template** field, in which a default
quotation template can be chosen from a drop-down menu.

![How to enable quotation templates on Konvergo ERP
Sales.](../../../../_images/quotations-templates-setting.png)

Also, upon activating the **Quotation Template** feature, an internal **➡️
Quotation Templates** link appears beneath the **Default Template** field.

Clicking that link reveals the **Quotation Templates** page, from which
templates can be created, viewed, and edited.

Before leaving the **Settings** page, don’t forget to click the **Save**
button to save all changes made during the session.

## Create quotation templates

Click the **Quotation Templates** link on the **Settings** page, or navigate
to Sales app ‣ Configuration ‣ Quotation Templates. Both options reveal the
**Quotation Templates** page, where quotation templates can be created,
viewed, and edited.

![Quotation templates page in the Konvergo ERP Sales
application.](../../../../_images/quotation-templates-page.png)

To create a new quotation template, click the **New** button, located in the
upper-left corner. Doing so reveals a blank quotation template form that can
be customized in a number of ways.

![Create a new quotation template on Konvergo ERP Sales.](../../../../_images/blank-
quotation-form.png)

Start by entering a name for the template in the **Quotation Template** field.

Then, in the **Quotation expires after** field, designate how many days the
quotation template will remain valid for, or leave the field on the default
`0` to keep the template valid indefinitely.

If the **Online Signature** and/or **Online Payment** features are activated
in the **Settings** (Sales app ‣ Configuration ‣ Settings), those options are
available in the **Online confirmation** field.

In the **Online confirmation** field, check the box beside **Signature** to
request an online signature from the customer to confirm an order. Check the
box beside **Payment** to request an online payment from the customer to
confirm an order.

Both options can be enabled simultaneously, in which case the customer must
provide **both** a signature **and** a payment to confirm an order.

Next, in the **Confirmation Mail** field, click the blank field to reveal a
drop-down menu. From the drop-down menu, select a pre-configured email
template to be sent to customers upon confirmation of an order.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To create a new email template directly from the <b>Confirmation Mail</b> field, start
typing the name of the new email template in the field, and select either: <b>Create</b> or
<b>Create and edit…</b> from the drop-down menu that appears.</p>
<p>Selecting <b>Create</b> creates the email template, which can be edited later. Selecting
<b>Create and edit…</b> creates the email template, and a <b>Create Confirmation
Mail</b> pop-up window appears, in which the email template can be customized and configured right
away.</p>
<img alt="Create confirmation mail pop-up window from the quotation template form in Konvergo ERP Sales." class="align-center" src="../../../../_images/create-confirmation-mail-popup.png"/>
<p>When all modifications are complete, click <b>Save &amp; Close</b> to save the email template
and return to the quotation form.</p>
</div>

If working in a multi-company environment, use the **Company** field to
designate to which company this quotation template applies.

In the **Recurrence** field, choose from a variety of pre-configured amounts
of time (e.g. **Monthly** , **Quarterly**) to designate how often this
quotation template should occur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Recurrence</b> field <b>only</b> applies to subscription plans. For more information,
check out the documentation on <a href="../../subscriptions/plans">Subscription plans</a>.</p>
</div>

### Lines tab

In the **Lines** tab, products can be added to the quotation template by
clicking **Add a product** , organized by clicking **Add a section** (and
dragging/dropping section headers), and further explained with discretionary
information (such as warranty details, terms, etc.) by clicking **Add a
note**.

![Populated lines tab on a quotation template form in Konvergo ERP
Sales.](../../../../_images/lines-tab-quotation-template.png)

To add a product to a quotation template, click **Add a product** in the
**Lines** tab of a quotation template form. Doing so reveals a blank field in
the **Product** column.

When clicked, a drop-down menu with existing products in the database appear.
Select the desired product from the drop-down menu to add it to the quotation
template.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If the desired product isn’t readily visible, type the name of the desired product in the
<b>Product</b> field, and the option appears in the drop-down menu. Products can also be
found by clicking <b>Search More…</b> from the drop-down menu.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When a product is added to a quotation template, the default <b>Quantity</b> is <code>1</code>, but
that can be edited at any time.</p>
</div>

Then, drag-and-drop the product to the desired position, via the **six
squares** icon, located to the left of each line item.

To add a _section_ , which serves as a header to organize the lines of a sales
order, click **Add a section** in the **Lines** tab. When clicked, a blank
field appears, in which the desired name of the section can be typed. When the
name has been entered, click away to secure the section name.

Then, drag-and-drop the section name to the desired position, via the **six
squares** icon, located to the left of each line item.

To add a note, which would appear as a piece of text for the customer on the
quotation, click **Add a note** in the **Lines** tab. When clicked, a blank
field appears, in which the desired note can be typed. When the note has been
entered, click away to secure the note.

Then, drag-and-drop the note to the desired position, via the **six squares**
icon.

To delete any line item from the **Lines** tab (product, section, and/or
note), click the **🗑️ (trash can)** icon on the far-right side of the line.

### Optional Products tab

The use of _optional products_ is a marketing strategy that involves the
cross-selling of products along with a core product. The aim is to offer
useful and related products to customers, which may result in an increased
sale.

For instance, if a customer wants to buy a car, they have the choice to order
massaging seats, as well, or ignore the offer and simply buy the car.
Presenting the choice to purchase optional products enhances the customer
experience.

Optional products appear as a section on the bottom of sales orders and
eCommerce pages. Customers can immediately add them to their online sales
orders themselves, if desired.

![Optional products appearing on a typical sales order with Konvergo ERP
Sales.](../../../../_images/optional-products-on-sales-order.png)

In the **Optional Products** tab, **Add a line** for each cross-selling
product related to the original items in the **Lines** tab, if applicable. The
products added here ideally complement the original offering as added value
for the prospective buyer.

![Populated optional products tab on a quotation template in Konvergo ERP
Sales.](../../../../_images/optional-products-tab-quotation-template1.png)

Clicking **Add a line** reveals a blank field in the **Product** column.

When clicked, a drop-down menu with products from the database appear. Select
the desired product from the drop-down menu to add it as an optional product
to the quotation template.

To delete any line item from the **Optional Products** tab, click the **🗑️
(trash can)** icon.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Optional products are <b>not</b> required to create a quotation template.</p>
</div>

### Terms & Conditions tab

The **Terms & Conditions** tab provides the opportunity to add terms and
conditions to the quotation template. To add terms and conditions, simply type
(or copy/paste) the desired terms and conditions in this tab.

![Terms and conditions tab in a quotation template form in Konvergo ERP
Sales.](../../../../_images/terms-and-conditions-tab.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../finance/accounting/customer_invoices/terms_conditions">Default terms and conditions (T&amp;C)</a></p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Terms and conditions are <b>not</b> required to create a quotation template.</p>
</div>

## Design quotation templates

In the upper-left corner of the quotation template form, there’s a **Design
Template** button.

![Design template button in the upper-left corner of quotation template
form.](../../../../_images/design-template-button.png)

When clicked, Konvergo ERP reveals a preview of the quotation template, through the
Konvergo ERP _Website_ application, as it will appear on the front-end of the website
to the customer.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature is <b>only</b> available if the <em>Website</em> application is installed.</p>
</div>

Konvergo ERP uses numerous blue placeholder blocks to signify where certain elements
appear, and what they contain (e.g. **Template Header** , **Product**).

To edit the content, appearance, and overall design of the quotation template
via the _Website_ application, click the **Edit** button in the upper-right
corner.

![Design template edit button in the upper-right corner of quotation template
design.](../../../../_images/design-template-edit-button.png)

When **Edit** is clicked, Konvergo ERP reveals a sidebar filled with a variety of
design elements and feature-rich building blocks. These building blocks can be
dragged-and-dropped anywhere on the quotation template design.

![Design quotation template building blocks sidebar in Konvergo ERP
Website.](../../../../_images/design-quotation-building-blocks.png)

After a block has been dropped in the desired position, it can be customized
and configured to fit any unique need, look, or style.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Quotation template design uses the same methodology and functionality with design building blocks
as a typical web page design with Konvergo ERP <em>Website</em>. Be sure to check out the
<a href="../../../websites/website">Website</a> documentation to learn more.</p>
</div>

When all blocks and customizations are complete, click the **Save** button to
put those configurations into place.

There is also a blue banner at the top of the quotation template design with a
link to quickly return **Back to edit mode**. When clicked, Konvergo ERP returns to
the quotation template form in the back-end of the _Sales_ application.

## Use quotation templates

When creating a quotation (Sales app ‣ New), choose a pre-configured template
in the **Quotation Template** field.

![Quotation templates field on a standard quotation form in Konvergo ERP
Sales.](../../../../_images/quotation-templates-field.png)

To view what the customer will see, click the **Preview** button at the top of
the page to see how the quotation template appears on the front-end of the
website through Konvergo ERP’s customer portal.

![Customer preview of a quotation template in Konvergo ERP
Sales.](../../../../_images/quotations-templates-preview.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="get_signature_to_validate">Online signatures for order confirmations</a></p></li>
<li><p><a href="get_paid_to_validate">Online payment order confirmation</a></p></li>
</ul>
</div>

