# EPC QR codes

European Payments Council quick response codes, or **EPC QR codes** , are two-
dimensional barcodes that customers can scan with their **mobile banking
applications** to initiate a **SEPA credit transfer (SCT)** and pay their
invoices instantly.

In addition to bringing ease of use and speed, it greatly reduces typing
errors that would potentially make for payment issues.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature is only available for companies in several European countries such as Austria,
Belgium, Finland, Germany, and the Netherlands.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../bank">Bank and cash accounts</a></p></li>
<li><p><a href="https://www.odoo.com/r/VuU">Konvergo ERP Academy: QR Code on Invoices for European Customers</a></p></li>
</ul>
</div>

## Configuration

Go to Accounting ‣ Configuration ‣ Settings and activate the **QR Codes**
feature in the **Customer Payments** section.

### Configure your bank account’s journal

Make sure that your **Bank Account** is correctly configured in Konvergo ERP with your
IBAN and BIC.

To do so, go to Accounting ‣ Configuration ‣ Journals, open your bank journal,
then fill out the **Account Number** and **Bank** under the **Bank Account
Number** column.

![Bank account number column in the bank journal](../../../../_images/bank-
journal.png)

## Issue invoices with EPC QR codes

EPC QR codes are added automatically to your invoices. Customers whose bank
supports making payments via EPC QR codes will be able to scan the code and
pay the invoice.

Go to Accounting ‣ Customers ‣ Invoices, and create a new invoice.

Before posting it, open the **Other Info** tab. Konvergo ERP automatically fills out
the **Recipient Bank** field with your IBAN.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In the <b>Other Info</b> tab, the account indicated in the <b>Recipient Bank</b> field
is used to receive your customer’s payment. Konvergo ERP automatically populates this field with your
IBAN by default and uses it to generate the EPC QR code.</p>
</div>

When the invoice is printed or previewed, the QR code is included at the
bottom.

![QR code on a customer invoice](../../../../_images/invoice-qr-code.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to issue an invoice without an EPC QR code, remove the IBAN indicated in the
<b>Recipient Bank</b> field, under the <b>Other Info</b> tab of the invoice.</p>
</div>

