# After-Sales services

_After-Sales_ services can be configured in the _Helpdesk_ application for
individual _teams_. Once enabled, users can issue refunds, process returns,
generate coupons, and/or schedule repair and field service interventions
directly from a ticket.

## Set up the after-sales services

Start by enabling the after-sales services on specific _Helpdesk_ team(s), by
going to Helpdesk ‣ Configuration ‣ Teams and selecting which teams(s) these
services should be active on. Then, scroll to the **After-Sales** section on
the team’s settings page, and choose which of the following options to enable:

  * **Refunds** : issues credit notes to refund a customer, or adjust the remaining amount due

  * **Coupons** : offers discounts and free products through an existing coupon program

  * **Returns** : initiates a product return from a customer through a reverse transfer

  * **Repairs** : creates repair orders for broken or faulty products

  * **Field Service** : plans onsite intervention through the _Field Service_ application

![../../../../_images/after-sales-enable.png](../../../../_images/after-sales-
enable.png)

The services that are enabled can vary based on the type of support a team
provides.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>As all of the after-sales services in Konvergo ERP require integration with other applications, enabling
any of them may result in the installation of additional modules or applications. <em>Installing a
new application on a One-App-Free database will trigger a 15-day trial. At the end of the trial,
if a paid subscription has not been added to the database, it will no longer be accessible.</em></p>
</div>

## Issue a refund with a credit note

A _credit note_ is a document issued to a customer informing them that they
have been credited a certain amount of money. They can be used to provide a
full refund to a customer, or to adjust any remaining amount due. While they
are usually created through the _Accounting_ or _Invoicing_ applications, they
can be created through a _Helpdesk_ ticket, as well.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Invoices must be posted before a credit note can be generated.</p>
</div>

To create a credit note, navigate to a ticket on the Helpdesk application, and
click the **Refund** button in the upper-left corner of the ticket dashboard.
Then, select the corresponding invoice from the **Invoices to Refund** drop-
down menu.

![View of a refund creation page.](../../../../_images/after-sales-refund-
details.png)

Choose a **Credit Method** from one of the following options:

  * **Partial Refund** : the credit note is created in draft and can be edited before being issued

  * **Full Refund** : the credit note is auto-validated and reconciled with the invoice. _This is the option to choose if a validated invoice needs to be canceled_

  * **Full refund and new draft invoice** : the credit note is auto-validated and reconciled with the invoice. The original invoice is duplicated as a new draft. _This is the option to choose if a validated invoice needs to be modified_

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>Credit Method</b> options will <b>not</b> be available for invoices that have already
been paid.</p>
</div>

Make any necessary changes to the details of the credit note and click
**Reverse.** Then click **Confirm** to post the credit note.

Once the credit note has been posted, a **Credit Notes** smart button will be
added to the _Helpdesk_ ticket.

![View of smart buttons on a ticket focusing on the credit note
button.](../../../../_images/after-sales-credit-note-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../finance/accounting/customer_invoices/credit_notes">Credit notes and refunds</a></p>
</div>

## Generate coupons from a ticket

Coupons can be used to alter the price of products or orders. The usage
constraints of a coupon are defined by conditional rules. _Coupon Programs_
are configured in the _Sales_ or _Website_ applications.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <em>eCommerce</em> module must be installed in order to create coupon codes from the <em>Website</em>.</p>
</div>

To generate a coupon, open a _Helpdesk_ ticket and click on the **Coupon**
button in the upper left corner. Select an option from the **Coupon Program**
drop-down menu, then click **Generate**.

![View of a coupon generation window.](../../../../_images/after-sales-
generate-coupon.png)

The **Coupon Code** can be copied directly from the pop-up window (by clicking
the **Copy** button), or sent in an email by clicking **Send**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When emailing a coupon code, all the followers of the ticket will be added as recipients to the
email. Additional recipients can be added to the email as well, in the <b>Recipients</b>
field of the <b>Compose Email</b> pop-up window.</p>
<img alt="View of an email draft window with coupon code." class="align-center" src="../../../../_images/after-sales-coupon-email.png"/>
</div>

Once a **Coupon Code** has been generated, a **Coupons** smart button will be
added to the top of the ticket; click the smart button to view the coupon
code, expiration date, and additional information.

![View of the smart buttons on a ticket focusing on the coupon
button.](../../../../_images/after-sales-coupon-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://www.odoo.com/slides/slide/coupon-programs-640?fullscreen=1">Coupons</a></p>
</div>

## Facilitate a product return with a reverse transfer

Returns are completed through _reverse transfers_ , which generate new
warehouse operations for the returning products. Click the **Return** button
in the top-left corner of a ticket to open the **Reverse Transfer** pop-up
window.

![View of a Helpdesk ticket with the return button
highlighted.](../../../../_images/after-sales-return-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Return</b> button only appears on a ticket if the customer has a recorded delivery in
the database.</p>
</div>

By default, the quantity will match the validated quantity from the delivery
order. Update the **Quantity** field if necessary.

![View of a reverse transfer creation page.](../../../../_images/after-sales-
reverse-transfer.png)

Click **Return** to confirm the return. This generates a new warehouse
operation for the incoming returned product(s). A **Return** smart button will
then be added to the top of the ticket.

![View of the return smart button on a helpdesk
ticket.](../../../../_images/after-sales-return-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../sales/sales/products_prices/returns">Returns and refunds</a></p>
</div>

## Send products for repair from a ticket

If the ticket is related to an issue with a faulty or broken product, a repair
order can be created from the _Helpdesk_ ticket, and managed through the
_Repairs_ application.

To create a new repair order, open a Helpdesk ticket and click on the
**Repair** button in the upper left corner.

Clicking the **Repair** button opens a blank **Repair Reference** form.

![View of a repair reference page.](../../../../_images/after-sales-repair-
reference.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If a product was specified in the <b>Product</b> field on the ticket, it will be added to
the <b>Product to Repair</b> field automatically. If not, click into the field to select a
product from the drop down.</p>
</div>

Fill out the **Repair Description** field with a brief explanation of the
issue. Click the **Sale Order** field and then select the originating SO from
which the product is being repaired from. If a return has been initiated for
the product, select the reference number from the drop-down in the **Return**
field.

Choose an **Invoice Method** from the drop-down. Select **Before Repair** or
**After Repair** to generate an invoice before or after the work is completed.
Selecting **No Invoice** means that an invoice cannot be generated for this
service.

If parts are required for the repair, they can be added in the **Parts** tab.
Services can be added as product lines on the **Operations** tab. Additional
information for the internal repair team can be added to the **Repair Notes**
tab. Information for the customer can be added to the **Quotation Notes** tab,
and will be automatically added to the PDF of the quotations generated from
this **Repair Reference**.

A **Repairs** smart button will be added to the ticket, linking to the repair
order.

![View of smart buttons focusing on repair button.](../../../../_images/after-
sales-repair-smart-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Invoices must be posted before a credit note can be generated.</p>
</div>0

## Create a field service task from a ticket

On-site interventions can be planned from a ticket and managed through the
_Field Service_ application. Customers with [portal
access](../../../general/users/portal) will be able to track the progress
of a **Field Service** task just as they would a _Helpdesk_ ticket.

To create a new task, navigate to a Helpdesk ticket. Click **Create Task** to
open the **Create a Field Service task** pop-up. Confirm or update the task
**Title**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Invoices must be posted before a credit note can be generated.</p>
</div>1

Click **Create Task** or **Create & View Task**.

![View of a Field Service task creation page.](../../../../_images/after-
sales-field-service-create.png)

After the task is created, a **Tasks** smart button will be added to the
ticket, linking the **Field Service** task to the ticket.

![View of ticket smart buttons focused on task.](../../../../_images/after-
sales-field-service-smart-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Invoices must be posted before a credit note can be generated.</p>
</div>2

  *[SO]: Sales Order

