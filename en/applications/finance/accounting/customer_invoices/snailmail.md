# Snailmail

Sending direct mail can be an effective strategy for grabbing people’s
attention, especially when their email inboxes are overflowing. With Konvergo ERP, you
have the ability to send invoices and follow-up reports through postal mail
worldwide, all from within your database.

## Configuration

Go to Accounting ‣ Configuration ‣ Settings ‣ Customer invoices section to
activate **Snailmail**.

To make it a by-default feature, select **Send by Post** in the **Default
Sending Options** section.

![Under settings enable the snailmail feature in Konvergo ERP
Accounting](../../../../_images/setup-snailmail.png)

## Send invoices by post

Open your invoice, click on **Send & Print** and select **Send by Post**. Make
sure your customer’s address is set correctly, including the country, before
sending the letter.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Your document must respect the following rules to pass the validation before being sent:</p>
<ul>
<li><p>Margins must be <b>5 mm</b> on all sides. As Konvergo ERP forces the outer margins by filling them with
white before sending the snailmail, it can results in the user’s custom being cut off if it
protrudes into the margins. To check the margins, activate the <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, go to General Settings ‣ Technical ‣ Reporting
section: Paper Format.</p></li>
<li><p>A square of <b>15mm by 15mm</b> on the bottom left corner has to stay clear.</p></li>
<li><p>The postage area has to stay clear (<a download="" href="../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf"><code>download the snailmail PDF template</code></a> for more details).</p></li>
<li><p>Pingen (Konvergo ERP Snailmail service provider) scans the area to process the address, so if something
gets written outside the area, it is not counted as part of the address.</p></li>
</ul>
</div>

## Pricing

Snailmail is an [In-app purchases
(IAP)](../../../essentials/in_app_purchase) service that requires prepaid
stamps (=credits) to work. Sending one document consumes one stamp.

To buy stamps, go to Accounting ‣ Configuration ‣ Settings ‣ Customer
invoices: Snailmail, click on **Buy credits** , or go to Settings ‣ In-App
Purchases: Konvergo ERP IAP, and click on **View my Services**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://iap.odoo.com/privacy#header_4">Konvergo ERP’s IAP Privacy Policy</a></p>
</div>

