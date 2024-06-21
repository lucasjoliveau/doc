# Bank and cash accounts

You can manage as many bank or cash accounts as needed on your database.
Configuring them well allows you to have all your banking data up-to-date and
ready for [reconciliation](bank/reconciliation) with your journal
entries.

In Konvergo ERP Accounting, each bank account has a dedicated journal set to post all
entries in a dedicated account. Both the journal and the account are
automatically created and configured whenever you add a bank account.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cash journals and accounts must be configured manually.</p>
</div>

Bank journals are displayed by default on the **Accounting Dashboard** in the
form of cards which include action buttons.

![Bank journals are displayed on the Accounting Dashboard and contain action
buttons](../../../_images/card.png)

## Manage your bank and cash accounts

### Connect your bank for automatic synchronization

To connect your bank account to your database, go to Accounting ‣
Configuration ‣ Banks: Add a Bank Account, select your bank in the list, click
on **Connect** , and follow the instructions.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="bank/bank_synchronization">Bank synchronization</a></p>
</div>

### Create a bank account

If your banking institution is not available in Konvergo ERP, or if you don’t want to
connect your bank account to your database, you can configure your bank
account manually.

To manually add a bank account, go to Accounting ‣ Configuration ‣ Banks: Add
a Bank Account, click on **Create it** (at the bottom right), and fill out the
form.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Konvergo ERP automatically detects the bank account type (e.g., IBAN) and enables some features
accordingly.</p></li>
<li><p>A default bank journal is available and can be used to configure your bank account by going to
Accounting ‣ Configuration ‣ Accounting: Journals ‣ Bank. Open it and
edit the different fields to match your bank account information.</p></li>
</ul>
</div>

### Create a cash journal

To create a new cash journal, go to Accounting ‣ Configuration ‣ Accounting:
Journals, click on **Create** and select **Cash** in the **Type** field.

For more information on the accounting information fields, read the
Configuration section of this page.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>A default cash journal is available and can be used straight away. You can review it by going to
Accounting ‣ Configuration ‣ Accounting: Journals ‣ Cash.</p>
</div>

### Edit an existing bank or cash journal

To edit an existing bank journal, go to Accounting ‣ Configuration ‣
Accounting: Journals and select the journal you want to modify.

## Configuration

You can edit the accounting information and bank account number according to
your needs.

![Manually configure your bank information](../../../_images/bank-journal-
config.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="get_started/multi_currency">Multi-currency system</a></p></li>
<li><p><a href="bank/transactions">Transactions</a></p></li>
</ul>
</div>

### Suspense account

Bank statement transactions are posted on the **Suspense Account** until the
final reconciliation allows finding the right account.

### Profit and loss accounts

The **Profit Account** is used to register a profit when the ending balance of
a cash register differs from what the system computes, while the **Loss
Account** is used to register a loss when the ending balance of a cash
register differs from what the system computes.

### Currency

You can edit the currency used to enter the statements.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="get_started/multi_currency">Multi-currency system</a></p>
</div>

### Account number

If you need to **edit your bank account details** , click on the external link
arrow next to your **Account Number**. On the new page, click on the external
link arrow next to your **Bank** and update your bank information accordingly.
These details are used when registering payments.

![Edit your bank information](../../../_images/bank-account-number.png)

### Bank feeds

**Bank Feeds** defines how the bank statements are registered. Three options
are available:

  * **Undefined yet** , which should be selected when you don’t know yet if you will synchronize your bank account with your database or not.

  * **Import (CAMT, CODA, CSV, OFX, QIF)** , which should be selected if you want to import your bank statement using a different format.

  * **Automated Bank Synchronization** , which should be selected if your bank is synchronized with your database.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="bank/bank_synchronization">Bank synchronization</a></p></li>
<li><p><a href="bank/transactions">Transactions</a></p></li>
</ul>
</div>

## Outstanding accounts

By default, payments are registered through transitory accounts named
**outstanding accounts** , before being recorded in your bank account.

  * An **outstanding payments account** is where outgoing payments are posted until they are linked with a withdrawal from your bank statement.

  * An **outstanding receipts account** is where incoming payments are posted until they are linked with a deposit from your bank statement.

These accounts should be of [type](get_started/chart_of_accounts#chart-
of-account-type) **Current Assets**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The movement from an outstanding account to a bank account is done automatically when you
reconcile the bank account with a bank statement.</p>
</div>

### Default accounts configuration

The outstanding accounts are defined by default. If necessary, you can update
them by going to Accounting ‣ Configuration ‣ Settings ‣ Default Accounts and
update your **Outstanding Receipts Account** and **Outstanding Payments
Account**.

### Bank and cash journals configuration

You can also set specific outstanding accounts for any journal with the
[type](get_started/chart_of_accounts#chart-of-account-type) **Bank** or
**Cash**.

From your **Accounting Dashboard** , click on the menu selection ⋮ of the
journal you want to configure, and click on **Configuration** , then open the
**Incoming/Outgoing Payments** tab. To display the outstanding accounts
column, click on the toggle button and check the **Outstanding
Receipts/Payments accounts** , then update the account.

![Select the toggle button and click on outstanding
Accounts](../../../_images/toggle-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If you do not specify an outstanding payments account or an outstanding receipts account for a
specific journal, Konvergo ERP uses the default outstanding accounts.</p></li>
<li><p>If your main bank account is added as an outstanding receipts account or outstanding payments
account, when a payment is registered, the invoice or bill’s status is directly set to
<b>Paid</b>.</p></li>
</ul>
</div>

  * [Bank synchronization](bank/bank_synchronization)
    * [Salt Edge](bank/bank_synchronization/saltedge)
    * [Ponto](bank/bank_synchronization/ponto)
    * [Enable Banking](bank/bank_synchronization/enablebanking)
  * [Transactions](bank/transactions)
  * [Bank reconciliation](bank/reconciliation)
  * [Reconciliation models](bank/reconciliation_models)
  * [Manage a bank account in a foreign currency](bank/foreign_currency)
  * [Cash register](bank/cash_register)

