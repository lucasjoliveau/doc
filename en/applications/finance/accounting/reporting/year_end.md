# Year-end closing

Year-end closing is vital for maintaining financial accuracy, complying with
regulations, making informed decisions, and ensuring transparency in
reporting.

## Fiscal years

By default, the fiscal year is set to last 12 months and end on December 31st.
However, its duration and end date can vary due to cultural, administrative,
and economic considerations.

To modify these values, go to Accounting ‣ Configuration ‣ Settings. Under the
**Fiscal Periods** section, change the **Last Day** field if necessary.

If the period lasts _more_ than or _less_ than 12 months, enable **Fiscal
Years** and **Save**. Go back to the **Fiscal Periods** section and click **➜
Fiscal Years**. From there, click **Create** , give it a **Name** , and both a
**Start Date** and **End Date**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Once the set fiscal period is over, Konvergo ERP automatically reverts to the default periodicity, taking
into account the value specified in the <b>Last Day</b> field.</p>
</div>

## Year-end checklist

### Before closure

Before closing a fiscal year, ensure first everything is accurate and up-to-
date:

  * Make sure all bank accounts are fully [reconciled](../bank/reconciliation) up to year-end, and confirm that the ending book balances match the bank statement balances.

  * Verify that all [customer invoices](../customer_invoices) have been entered and approved and that there are no draft invoices.

  * Confirm that all [vendor bills](../vendor_bills) have been entered and agreed upon.

  * Validate all [expenses](../../expenses), ensuring their accuracy.

  * Corroborate that all [received payments](../payments) have been encoded and recorded accurately.

  * Close all [suspense accounts](../bank#bank-accounts-suspense).

  * Book all [depreciation](../vendor_bills/assets) and [deferred revenue](../customer_invoices/deferred_revenues) entries.

### Closing a fiscal year

Then, to close the fiscal year:

  * Run a [tax report](../reporting#reporting-tax-report), and verify that all tax information is correct.

  * Reconcile all accounts on the [balance sheet](../reporting#reporting-balance-sheet):

    * Update the bank balances in Konvergo ERP according to the actual balances found on the bank statements.

    * Reconcile all transactions in the cash and bank accounts by running the [aged receivables](../reporting#reporting-aged-receivable) and [aged payables](../reporting#reporting-aged-payable) reports.

    * Audit all accounts, being sure to fully understand all transactions and their nature, making sure to include loans and fixed assets.

    * Optionally, run [payments matching](../payments#payments-matching) to validate any open vendor bills and customer invoices with their payments. While this step is optional, it could assist the year-end closing process if all outstanding payments and invoices are reconciled, potentially finding errors or mistakes in the system.

Next, the accountant likely verifies balance sheet items and book entries for:

>   * year-end manual adjustments,
>
>   * work in progress,
>
>   * depreciation journal entries,
>
>   * loans,
>
>   * tax adjustments,
>
>   * etc.
>
>

If the accountant is going through the year-end audit, they may want to have
paper copies of all balance sheet items (such as loans, bank accounts,
prepayments, sales tax statements, etc.) to compare these with the balances in
Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>During this process, it is good practice to set a <b>Journal Entries Lock Date</b> to the
last day (inclusive) of the preceding fiscal year by going to Accounting ‣
Accounting ‣ Lock Dates. This way, the accountant can be confident that nobody changes the
transactions while auditing the books. Users from the <em>accountant</em> access group can still create
and modify entries.</p>
</div>

#### Current year’s earnings

Konvergo ERP uses a unique account type called **current year’s earnings** to display
the amount difference between the **income** and **expenses** accounts.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The chart of accounts can only contain one account of this type. By default, it is a 999999
account named <b>Undistributed Profits/Losses</b>.</p>
</div>

To allocate the current year’s earnings, create a miscellaneous entry to book
them to any equity account. Once done, confirm whether or not the current
year’s earnings in the **balance sheet** is correctly reporting a balance of
zero. If that is the case, set an **All Users Lock Date** to the last day of
the fiscal year by going to Accounting ‣ Accounting ‣ Lock Dates.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Install the <b>Irreversible Lock Date</b> (<code>account_lock</code>) module to make the <b>All
Users Lock Date</b> <em>irreversible</em> once set.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>A specific year-end closing entry is <b>optional</b> in order to close out the <b>profit and loss
statement</b>. The reports are created in real-time, meaning that the profit and loss statement
corresponds directly with the year-end date specified in Konvergo ERP. Therefore, any time the <b>income
statement</b> is generated, the beginning date corresponds with the beginning of the <b>fiscal
year</b> and all account balances should equal zero.</p>
</div>

