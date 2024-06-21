# Authorize.Net

[Authorize.Net](https://www.authorize.net) is a United States-based online
payment solution provider, allowing businesses to accept **credit cards**.

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Credentials tab

Konvergo ERP needs your **API Credentials & Keys** to connect with your Authorize.Net
account, which comprise:

  * **API Login ID** : The ID solely used to identify the account with Authorize.Net.

  * **API Transaction Key**

  * **API Signature Key**

  * **API Client Key**

To retrieve them, log into your Authorize.Net account, go to Account ‣
Settings ‣ Security Settings ‣ API Credentials & Keys, generate your
**Transaction Key** and **Signature Key** , and paste them on the related
fields in Konvergo ERP. Then, click on **Generate Client Key**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To test Authorize.Net with a <em>sandbox</em> account, change the <b>State</b> to <b>Test
Mode</b>. We recommend doing this on a test Konvergo ERP database, rather than on your main database.</p>
<p>If you use the <b>Test Mode</b> with a regular account, it results in the following error:
<em>The merchant login ID or password is invalid or the account is inactive</em>.</p>
</div>

### Configuration tab

#### Place a hold on a card

With Authorize.Net, you can enable the [manual
capture](../payment_providers#payment-providers-manual-capture). If
enabled, the funds are reserved for 30 days on the customer’s card, but not
charged yet.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>After <b>30 days</b>, the transaction is <b>voided automatically</b> by Authorize.Net.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers">Online payments</a></p></li>
</ul>
</div>

## ACH payments (USA only)

ACH is an electronic funds transfer system used between bank accounts in the
United States.

### Configuration

To give customers the possibility to pay using ACH, [sign up for Authorize.Net
eCheck’s service](https://www.authorize.net/payments/echeck). Once eCheck
is activated, duplicate the previously configured Authorize.Net payment
provider on Konvergo ERP by going to Accounting ‣ Configuration ‣ Payment Providers ‣
Authorize.net ‣ ⛭ Action ‣ Duplicate. Then, change the provider’s name to
differentiate both versions (e.g., `Authorize.net - Banks`).

Open the **Configuration** tab, set the **Allow Payments From** field to
**Bank Account (USA only)**.

When ready, change the provider’s **State** to **Enabled** for a regular
account or **Test Mode** for a sandbox account.

## Import an Authorize.Net statement

### Export from Authorize.Net

<div class="admonition-template alert" id="authorize-import-template">
<p class="alert-title">
Template</p><p><a href="https://docs.google.com/spreadsheets/d/1CMVtBWLLVIrUpYA92paw-cL7-WdKLbaa/edit?usp=share_link&amp;ouid=105295722917050444558&amp;rtpof=true&amp;sd=true">Download the Excel import template</a></p>
</div>

To export a statement:

  * Log in to Authorize.Net.

  * Go to Account ‣ Statements ‣ eCheck.Net Settlement Statement.

  * Define an export range using an _opening_ and _closing_ batch settlement. All transactions within the two batch settlements will be exported to Konvergo ERP.

  * Select all transactions within the desired range, copy them, and paste them into the **Report 1 Download** sheet of the Excel import template.

![Selecting Authorize.Net transactions to import](../../../_images/authorize-
report1.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Settlement batch of an Authorize.Net statement" class="align-center" src="../../../_images/authorize-settlement-batch.png"/>
<p>In this case, the first batch (01/01/2021) of the year belongs to the settlement of 12/31/2020,
so the <b>opening</b> settlement is from 12/31/2020.</p>
</div>

Once the data is in the **Report 1 Download** sheet:

  * Go to the **Transaction Search** tab on Authorize.Net.

  * Under the **Settlement Date** section, select the previously used range of batch settlement dates in the **From:** and **To:** fields and click **Search**.

  * When the list has been generated, click **Download to File**.

  * In the pop-up window, select **Expanded Fields with CAVV Response/Comma Separated** , enable **Include Column Headings** , and click **Submit**.

  * Open the text file, select **All** , copy the data, and paste it into the **Report 2 Download** sheet of the Excel import template.

  * Transit lines are automatically filled in and updated in the **transit for report 1** and **transit for report 2** sheets of the Excel import template. Make sure all entries are present, and **if not** , copy the formula from previously filled-in lines of the **transit for report 1** or **2** sheets and paste it into the empty lines.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To get the correct closing balance, <b>do not remove</b> any line from the Excel sheets.</p>
</div>

### Import into Konvergo ERP

To import the data into Konvergo ERP:

  * Open the Excel import template.

  * Copy the data from the **transit for report 2** sheet and use _paste special_ to only paste the values in the **Konvergo ERP Import to CSV** sheet.

  * Look for _blue_ cells in the **Konvergo ERP Import to CSV** sheet. These are chargeback entries without any reference number. As they cannot be imported as such, go to Authorize.Net ‣ Account ‣ Statements ‣ eCheck.Net Settlement Statement.

  * Look for **Charge Transaction/Chargeback** , and click it.

  * Copy the invoice description, paste it into the **Label** cell of the **Konvergo ERP Import to CSV** sheet, and add `Chargeback /` before the description.

  * If there are multiple invoices, add a line into the Excel import template for each invoice and copy/paste the description into each respective **Label** line.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For <b>combined chargeback/returns</b> in the payouts, create a new line in the <a href="#authorize-import-template"><span class="std std-ref">Excel import
template</span></a> for each invoice.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Chargeback description" src="../../../_images/authorize-chargeback-desc.png"/>
</div>

  * Next, delete _zero transaction_ and _void transaction_ line items, and change the format of the **Amount** column in the **Konvergo ERP Import to CSV** sheet to _Number_.

  * Go back to eCheck.Net Settlement Statement ‣ Search for a Transaction and search again for the previously used batch settlements dates.

  * Verify that the batch settlement dates on eCheck.Net match the related payments’ dates found in the **Date** column of the **Konvergo ERP Import to CSV**.

  * If it does not match, replace the date with the one from eCheck.Net. Sort the column by _date_ , and make sure the format is `MM/DD/YYYY`.

  * Copy the data - column headings included - from the **Konvergo ERP Import to CSV** sheet, paste it into a new Excel file, and save it using the CSV format.

  * Open the Accounting app, go to Configuration ‣ Journals, tick the **Authorize.Net** box, and click Favorites ‣ Import records ‣ Load file. Select the CSV file and upload it into Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>List of <a href="https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293">eCheck.Net return codes</a></p>
</div>

  *[ACH]: automated clearing house

