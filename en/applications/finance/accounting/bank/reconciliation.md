# Bank reconciliation

**Bank reconciliation** is the process of matching your [bank
transactions](transactions) with your business records, such as [customer
invoices](../customer_invoices), [vendor bills](../vendor_bills),
and [payments](../payments). Not only is this compulsory for most
businesses, but it also offers several benefits, such as reduced risk of
errors in financial reports, detection of fraudulent activities, and improved
cash flow management.

Thanks to the bank [reconciliation models](reconciliation_models), Konvergo ERP
pre-selects the matching entries automatically.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/bank-reconciliation-2724">Konvergo ERP Tutorials: Bank reconciliation</a></p></li>
<li><p><a href="bank_synchronization">Bank synchronization</a></p></li>
<li><p><a href="transactions">Transactions</a></p></li>
</ul>
</div>

## Bank reconciliation view

To access a bank journal’s **reconciliation view** , go to your **Accounting
Dashboard** and either:

  * click the journal name (e.g., **Bank**) to display all transactions, including those previously reconciled or

  * click the **Reconcile items** button to display all transactions Konvergo ERP pre-selected for reconciliation. You can remove the **Not Matched** filter from the search bar to include previously reconciled transactions.

![Reaching the bank reconciliation tool from your accounting
dashboard](../../../../_images/bank-card.png)

The bank reconciliation view is structured into three distinct sections:
transactions, counterpart entries, and resulting entry.

![The user interface of the reconciliation view of a bank
journal.](../../../../_images/user-interface.png)

Transactions

    

The transactions section on the left shows all bank transactions, with the
newest displayed first. Click a transaction to select it.

Counterpart entries

    

The counterpart entries section on the bottom right displays the options to
match the selected bank transaction. Multiple tabs are available, including
Match existing entries, Batch payments, Manual operations, and **Discuss** ,
which contains the chatter for the selected bank transaction.

Resulting entry

    

The resulting entry section on the top right displays the selected bank
transaction matched with the counterpart entries and includes any remaining
debits or credits. In this section, you can validate the reconciliation or
mark it as **To Check**. Any reconciliation model buttons are also available
in the resulting entry section.

## Reconcile transactions

Transactions can be matched automatically with the use of [reconciliation
models](reconciliation_models), or they can be matched with existing
entries, batch payments, manual operations, and reconciliation model buttons.

  1. Select a transaction among unmatched bank transactions.

  2. Define the counterpart. There are several options for defining a counterpart, including matching existing entries, manual operations, batch payments, and reconciliation model buttons.

  3. If the resulting entry isn’t fully balanced, balance it by adding another existing counterpart entry or writing it off with a manual operation.

  4. Click the **Validate** button to confirm the reconciliation and move to the next transaction.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you aren’t sure how to reconcile a particular transaction and would like to deal with it
later, use the <b>To Check</b> button instead. All transactions marked as <b>To
Check</b> can be displayed using the <b>To Check</b> filter.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Bank transactions are posted on the <b>journal’s suspense account</b> until reconciliation. At this
point, reconciliation modifies the transaction journal entry by replacing the bank suspense
account with the corresponding receivable, payable, or outstanding account.</p>
</div>

### Match existing entries

This tab contains matching entries Konvergo ERP automatically pre-selects according to
the reconciliation models. The entry order is based on [reconciliation
models](reconciliation_models), with suggested entries appearing first.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>The search bar within the <b>Match Existing Entries</b> tab allows you to search for
specific journal items.</p>
</div>

### Batch payments

[Batch payments](payments/batch-payments) allow you to group different
payments to ease reconciliation. Use the **Batch Payments** tab to find batch
payments for customers and vendors. Similarly to the **Match Existing
Entries** tab, the **Batch Payments** tab has a search bar that allows you to
search for specific batch payments.

### Manual operations

If there isn’t an existing entry to match the selected transaction, you may
instead wish to reconcile the transaction manually by choosing the correct
account and amount. Then, complete any of the relevant optional fields.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can use the <b>fully paid</b> option to reconcile a payment, even in cases where only a
partial payment is received. A new line appears in the resulting entry section to reflect the
open balance registered on the Account Receivable by default. You can choose another
account by clicking on the new line in the resulting entry section and selecting the
<b>Account</b> to record the open balance.</p>
<img alt="Click on fully paid to manually set an invoice as entirely paid." src="../../../../_images/fully-paid.png"/>
</div>

### Reconciliation model buttons

Use a [reconciliation model](reconciliation_models) button for manual
operations that are frequently used. These custom buttons allow you to quickly
reconcile bank transactions manually and can also be used in combination with
existing entries.

