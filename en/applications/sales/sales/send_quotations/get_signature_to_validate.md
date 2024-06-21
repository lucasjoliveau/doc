# Online signatures for order confirmations

The Konvergo ERP _Sales_ application provides customers with the ability to confirm
orders, via an online signature, directly on the sales order. Once the sales
order is electronically signed by the customer, the salesperson attached to
the sales order is instantly notified that the order is confirmed.

## Activate online signatures

In order to have customers confirm orders with an online signature, the
_Online Signature_ feature **must** be activated.

To activate the _Online Signature_ feature, go to Sales app ‣ Configuration ‣
Settings, scroll to the **Quotations & Orders** heading, and activate the
**Online Signature** feature by checking the box beside it.

![The Online Signature feature option in the Settings of the Konvergo ERP Sales
application.](../../../../_images/signature-setting.png)

Then, click the **Save** button in the top-left corner.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When making a quotation template, the online signature feature is the <b>Signature</b>
option, located in the <b>Online confirmation</b> field of the quotation template form.</p>
<img alt="The Online confirmation signature option found on every quotation template in Konvergo ERP." class="align-center" src="../../../../_images/signature-feature-quotation-template.png"/>
<p>On standard quotations, the online signature feature is the <b>Signature</b> option, located
under the <b>Other Info</b> tab of the quotation form.</p>
<img alt="The online signature feature option in the Other Info tab of a quotation form in Konvergo ERP." class="align-center" src="../../../../_images/signature-other-info-tab.png"/>
</div>

## Order confirmations with online signatures

When clients access quotations online through their customer portal, there’s a
**Sign & Pay** button directly on the quotation.

![The Sign and Pay button present on online quotations in Konvergo ERP
Sales.](../../../../_images/sign-and-pay-button.png)

When clicked, a **Validate Order** pop-up window appears. In this pop-up
window, the **Full Name** field is auto-populated, based on the contact
information in the database.

![The Validate Order pop-up window for online signatures in Konvergo ERP
Sales.](../../../../_images/validate-order-popup.png)

Then, customers have the option to enter an online signature with any of the
following options: **Auto** , **Draw** , or **Load**.

**Auto** lets Konvergo ERP automatically generate an online signature based on the
information in the **Full Name** field. **Draw** lets the customer use the
cursor to create a custom signature directly on the pop-up window. And
**Load** lets the customer upload a previously-created signature file from
their computer.

After the customer has chosen any of the three previously mentioned signature
options (**Auto** , **Draw** , or **Load**), they will click the **Accept &
Sign** button.

When **Accept & Sign** is clicked, the various payment method options become
available for them to choose from (if the _online payment_ option applies to
this quotation).

Then, when the quotation is paid and confirmed, a delivery order is
automatically created (if the Konvergo ERP _Inventory_ app is installed).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="quote_template">Quotation templates</a></p></li>
<li><p><a href="get_paid_to_validate">Online payment order confirmation</a></p></li>
</ul>
</div>

