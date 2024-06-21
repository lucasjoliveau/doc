# Checks

There are two ways to handle payments received by checks in Konvergo ERP, either by
using outstanding accounts or by bypassing the reconciliation process.

**Using outstanding accounts is recommended** , as your bank account balance
stays accurate by taking into account checks yet to be cashed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Both methods produce the same data in your accounting at the end of the process. But if you
have checks that have not been cashed in, the <b>Outstanding Account</b> method reports these
checks in the <b>Outstanding Receipts</b> account. However, funds appear in your bank account
whether or not they are reconciled, as the bank value is reflected at the moment of the bank
statement.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../bank#bank-outstanding-accounts"><span class="std std-ref">Outstanding accounts</span></a></p></li>
<li><p><a href="../get_started/cheat_sheet#accounting-reconciliation"><span class="std std-ref">Bank reconciliation</span></a></p></li>
</ul>
</div>

## Method 1: Outstanding account

When you receive a check, you [record a payment](../bank/reconciliation)
by check on the invoice. Then, when your bank account is credited with the
check’s amount, you reconcile the payment and statement to move the amount
from the **Outstanding Receipt** account to the **Bank** account.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can create a new payment method named <em>Checks</em> if you would like to identify such payments
quickly. To do so, go to Accounting ‣ Configuration ‣ Journals ‣ Bank,
click the <b>Incoming Payments</b> tab, and <b>Add a line</b>. As <b>Payment
Method</b>, select <b>Manual</b>, enter <code>Checks</code> as name, and <b>Save</b>.</p>
</div>

## Method 2: Reconciliation bypass

When you receive a check, you [record a payment](../bank/reconciliation)
on the related invoice. The amount is then moved from the **Account
Receivable** to the **Bank** account, bypassing the reconciliation and
creating only **one journal entry**.

To do so, you _must_ follow the following setup. Go to Accounting ‣
Configuration ‣ Journals ‣ Bank. Click the **Incoming Payments** tab and then
**Add a line** , select **Manual** as **Payment Method** , and enter `Checks`
as **Name**. Click the toggle menu button, tick **Outstanding Receipts
accounts** , and in the **Outstanding Receipts accounts** column, and set the
**Bank** account for the **Checks** payment method.

![Bypass the Outstanding Receipts account using the Bank
account.](../../../../_images/outstanding-payment-accounts.png)

## Payment registration

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, there are two ways to register payments made by check:</p>
<ul>
<li><p><b>Manual</b>: for single checks;</p></li>
<li><p><b>Batch</b>: for multiple checks at once.</p></li>
</ul>
<p>This documentation focuses on <b>single-check</b> payments. For <b>batch deposits</b>, see <a href="batch">the
batch payments documentation</a>.</p>
</div>

Once you receive a customer check, go to the related invoice (Accounting ‣
Customer ‣ Invoices), and click **Register Payment**. Fill in the payment
information:

  * **Journal: Bank** ;

  * **Payment method** : **Manual** (or **Checks** if you have created a specific payment method);

  * **Memo** : enter the check number;

  * Click **Create Payment**.

![Check payment info](../../../../_images/payment-checks.png)

The generated journal entries are different depending on the payment
registration method chosen.

## Journal entries

### Outstanding account

The invoice is marked as **In Payment** as soon as you record the payment.
This operation produces the following **journal entry** :

Account | Statement Match | Debit | Credit  
---|---|---|---  
Account Receivable |  |  | 100.00  
Outstanding Receipts |  | 100.00 |   
  
Then, once you receive the bank statements, match this statement with the
check of the **Outstanding Receipts** account. This produces the following
**journal entry** :

Account | Statement Match | Debit | Credit  
---|---|---|---  
Outstanding Receipts | X |  | 100.00  
Bank |  | 100.00 |   
  
If you use this approach to manage received checks, you get the list of checks
that have not been cashed in the **Outstanding Receipt** account (accessible,
for example, from the general ledger).

### Reconciliation bypass

The invoice is marked as **Paid** as soon as you record the check.

With this approach, you bypass the use of **outstanding accounts** ,
effectively getting only one journal entry in your books and bypassing the
reconciliation:

Account | Statement Match | Debit | Credit  
---|---|---|---  
Account Receivable | X |  | 100.00  
Bank |  | 100.00 | 

