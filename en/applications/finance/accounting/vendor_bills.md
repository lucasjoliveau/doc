# Vendor bills

In Konvergo ERP, we can register vendor bills **manually** or **automatically** ,
while the **Aged Payable report** provides an overview of all outstanding
bills to help us pay the correct amounts on time.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p>Tutorial <a href="https://www.odoo.com/slides/slide/registering-a-vendor-bill-1683?fullscreen=1">Registering a vendor bill</a></p></li>
<li><p><a href="../../inventory_and_mrp/purchase/manage_deals/manage">Manage vendor bills</a></p></li>
</ul>
</div>

## Bill creation

### Manually

Create a vendor bill manually by going to Accounting ‣ Vendors ‣ Bills and
clicking **Create**.

### Automatically

Vendor bills can be automatically created by **sending an email** to an [email
alias](vendor_bills/invoice_digitization#invoice-digitization-email-
alias) associated with the purchase journal, or by **uploading a PDF** in
Accounting ‣ Vendors ‣ Bills and then clicking **Upload**.

## Bill completion

Whether the bill is created manually or automatically, make sure the following
fields are appropriately completed:

  * **Vendor** : Konvergo ERP automatically fills some information based on the vendor’s registered information, previous purchase orders, or bills.

  * **Bill Reference** : add the sales order reference provided by the vendor and is used to do the [matching](payments#payments-matching) when you receive the products.

  * **Auto-Complete** : select a past bill/purchase order to automatically complete the document. The **Vendor** field should be completed prior to completing this field.

  * **Bill Date** : is the issuance date of the document.

  * **Accounting Date** : is the date on which the document is registered in your accounting.

  * **Payment Reference** : when registering the payment, it is automatically indicated in the **Memo** field.

  * **Recipient Bank** : to indicate to which account number the payment has to be made.

  * **Due Date** or **Terms** to pay the bill.

  * **Journal** : select in which journal the bill should be recorded and the [Currency](get_started/multi_currency).

![filling the vendor bill](../../../_images/bill-completion.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Bills can be <a href="vendor_bills/invoice_digitization">digitized</a> for
automatic completion by clicking <b>Send for Digitization</b>.</p></li>
<li><p>If you upload the bill, the PDF document is displayed on the right of the screen, allowing you
to easily fill in the bill information.</p></li>
</ul>
</div>

## Bill confirmation

Click **Confirm** when the document is completed. The status of your document
changes to **Posted** and a journal entry is generated based on the
configuration on the invoice.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Once confirmed, it is no longer possible to update it. Click <b>Reset to draft</b> if
changes are required.</p>
</div>

## Bill Payment

Upon payment of the vendor bill, click on **Register Payment**. A new window
pops up.

Select the **Journal** , the **Payment Method** , the **Amount** you wish to
pay (full or partial payment), and the **Currency**. Konvergo ERP fills the **Memo**
field automatically if the **Payment Reference** has been set correctly in the
vendor bill. If the field is empty, we recommend you select the vendor invoice
number as a reference.

Once confirmed, an **In Payment** banner appears on the bill until it is
[reconciled](bank/reconciliation).

## Aged payable report

To get an overview of your open vendor bills and their related due dates, you
can use the **Aged Payable report**. Go to Accounting ‣ Reporting ‣ Partner
Reports: Aged payable.

Click on a vendor’s name to open up the details of all outstanding bills, the
amounts due, the due dates, etc.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>By clicking the <b>Save</b> button, you can export the information available on the screen
as a PDF or XLSX file and save it in the folder of your choice.</p></li>
<li><p>You might receive several bills for the same purchase order if your vendor is in back-order and
is sending you invoices as they ship the products, or if your vendor is sending you a partial
bill or asking for a deposit.</p></li>
</ul>
</div>

  * [AI-powered document digitization](vendor_bills/invoice_digitization)
  * [Non-current assets and fixed assets](vendor_bills/assets)
  * [Deferred expenses and prepayments](vendor_bills/deferred_expenses)

