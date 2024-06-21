# Pro-forma invoices

A _pro-forma invoice_ is an abridged or estimated invoice sent in advance of a
delivery of goods. It notes the kind and quantity of goods, their value, and
other important information, such as weight and transportation charges.

Pro-forma invoices are commonly used as preliminary invoices with a quotation.
They are also used during importation for customs purposes. They differ from a
normal invoice, in that they are _not_ a demand (or request) for payment.

## Configuration

In order to utilize pro-forma invoices, the _Pro-Forma Invoice_ feature
**must** be activated.

To enable this feature, navigate to Sales app ‣ Configuration ‣ Settings, and
in the **Quotations & Orders** section, click the checkbox next to **Pro-Forma
Invoice**. Then, click **Save** to save all changes.

![The Pro-Forma Invoice feature setting in the Konvergo ERP Sales
application.](../../../../_images/pro-forma-setting.png)

## Send pro-forma invoice

With the **Pro-Forma Invoice** feature activated, the option to send a pro-
forma invoice is now available on any quotation or sales order, via the **Send
Pro-Forma Invoice** button.

![The Send Pro-Forma Invoice button on a typical sales order in Konvergo ERP
Sales.](../../../../_images/send-pro-forma-invoice-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pro-forma invoices can <b>not</b> be sent for a sales order or quotation if an invoice for a down
payment has already been sent, or for a recurring subscription.</p>
<p>In either case, the <b>Send Pro-Froma Invoice</b> button does <b>not</b> appear.</p>
<p>However, pro-forma invoices <b>can</b> be sent for services, event registrations, courses, and/or
new subscriptions. Pro-forma invoices are not limited to physical, consumable, or storable goods.</p>
</div>

When the **Send Pro-Forma Invoice** button is clicked, a pop-up window
appears, from which an email can be sent.

In the pop-up window, the **Recipients** field is auto-populated with the
customer from the sales order or quotation. The **Subject** field and the body
of the email can be modified, if necessary.

The pro-forma invoice is automatically added as an attachment to the email.

When ready, click **Send** , and Konvergo ERP instantly sends the email, with the
attached pro-forma invoice, to the customer.

![The email pop-up window that appears with pro-forma invoice attached in Konvergo ERP
Sales.](../../../../_images/pro-forma-email-message-pop-up.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To preview what the pro-forma invoice looks like, click on the PDF at the bottom of the email
pop-up window <em>before</em> clicking <b>Send</b>. When clicked, the pro-forma invoice is
downloaded instantly. Open that PDF to view (and review) the pro-forma invoice.</p>
<img alt="Sample pro-forma invoice PDF from Konvergo ERP Sales." class="align-center" src="../../../../_images/pro-forma-pdf.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="invoicing_policy">Invoice based on delivered or ordered quantities</a></p>
</div>

