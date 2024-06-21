# Online payments

  * Install the patch to disable online invoice payment
    * [Update Konvergo ERP to the latest release](online/install_portal_patch#update-odoo-to-the-latest-release)
    * [Update the list of available modules](online/install_portal_patch#update-the-list-of-available-modules)
    * [Install the module Invoice Online Payment Patch](online/install_portal_patch#install-the-module-invoice-online-payment-patch)

To make it more convenient for your customers to pay the invoices you issue,
you can activate the **Invoice Online Payment** feature, which adds a _Pay
Now_ button on their **Customer Portal**. This allows your customers to see
their invoices online and pay directly with their favorite payment method,
making the payment process much easier.

![Payment provider choice after having clicked on "Pay
Now"](../../../../_images/online-payment-providers.png)

## Configuration

Make sure your [payment providers are correctly
configured](../../payment_providers).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, “<a href="../../payment_providers/wire_transfer">Wire Transfer</a>” is the
only payment provider activated, but you still have to fill out the payment details.</p>
</div>

To activate the Invoice Online Payment, go to Accounting ‣ Configuration ‣
Settings ‣ Customer Payments, enable **Invoice Online Payment** , and click on
_Save_.

## Customer Portal

After issuing the invoice, click on _Send & Print_ and send the invoice by
email to the customer. They will receive an email with a link that redirects
them to the invoice on their **Customer Portal**.

![Email with a link to view the invoice online on the Customer
Portal.](../../../../_images/view-invoice.png)

They can choose which Payment Provider to use by clicking on _Pay Now_.

!["Pay now" button on an invoice in the Customer
Portal.](../../../../_images/pay-now.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../payment_providers">Online payments</a></p></li>
</ul>
</div>

