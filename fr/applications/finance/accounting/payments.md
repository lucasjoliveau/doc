# Paiements

In Konvergo ERP, payments can either be automatically linked to an invoice or bill or
be stand-alone records for use at a later date:

  * If a payment is **linked to an invoice or bill** , it reduces/settles the amount due of the invoice. You can have multiple payments related to the same invoice.

  * If a payment is **not linked to an invoice or bill** , the customer has an outstanding credit with your company, or your company has an outstanding debit with a vendor. You can use those outstanding amounts to reduce/settle unpaid invoices/bills.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="payments/internal_transfers">Virements internes</a></p></li>
<li><p><a href="bank/reconciliation">Rapprochement bancaire</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/bank-configuration-1880">Tutoriels Konvergo ERP : Configuration bancaire</a></p></li>
</ul>
</div>

## Enregistrer un paiement à partir d’une facture client ou d’une facture
fournisseur

When clicking **Register payment** in a customer invoice or vendor bill, it
generates a new journal entry and changes the amount due according to the
payment amount. The counterpart is reflected in an
[outstanding](bank#bank-outstanding-accounts) **receipts** or
**payments** account. At this point, the customer invoice or vendor bill is
marked as **In payment**. Then, when the outstanding account is reconciled
with a bank statement line, the invoice or vendor bill changes to the **Paid**
status.

The information icon near the payment line displays more information about the
payment. You can access additional information, such as the related journal,
by clicking **View**.

![See detailed information of a payment.](../../../_images/information-
icon.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The customer invoice or vendor bill must be in the <b>Posted</b> status to register the
payment.</p></li>
<li><p>If you unreconcile a payment, it still appears in your books but is no longer linked to the
invoice.</p></li>
<li><p>Si vous lettrez (annulez le lettrage d”) un paiement dans une devise différente, une écriture comptable est automatiquement créée pour enregistrer le montant des gains/pertes de change (extourne).</p></li>
<li><p>Si vous lettrez (annulez le lettrage d”) un paiement et une facture comportant une TVA sur encaissements, une écriture comptable est automatiquement créée pour enregistrement le montant de la TVA sur encaissements (extourne).</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>If your main bank account is set as an <a href="bank#bank-outstanding-accounts"><span class="std std-ref">outstanding account</span></a>, and the payment is registered in Konvergo ERP (not through a related
bank statement), invoices and bills are directly registered as <b>Paid</b>.</p></li>
</ul>
</div>

## Enregistrer des paiements non associés à une facture client ou fournisseur

When a new payment is registered via Customers / Vendors ‣ Payments menu, it
is not directly linked to an invoice or bill. Instead, the account receivable
or the account payable is matched with the **outstanding account** until it is
manually matched with its related invoice or bill.

### Lettrer les factures clients et fournisseurs aux paiements

A blue banner appears when you validate a new invoice/bill and an
**outstanding payment** exists for this specific customer or vendor. It can
easily be matched from the invoice or bill by clicking **ADD** under
**Outstanding Credits** or **Outstanding Debits**.

![Shows the ADD option to reconcile an invoice or a bill with a
payment.](../../../_images/add-option.png)

The invoice or bill is now marked as **In payment** until it is reconciled
with its corresponding bank statement.

### Paiements par lot

Batch payments allow you to group different payments to ease
[reconciliation](bank/reconciliation). They are also useful when you
deposit [checks](payments/checks) to the bank or for [SEPA
payments](payments/pay_sepa). To do so, go to Accounting ‣ Customers ‣
Batch Payments or Accounting ‣ Vendors ‣ Batch Payments. In the list view of
payments, you can select and group several payments in a batch by clicking
Action ‣ Create Batch Payment.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="payments/batch">Paiements par lot par dépôt bancaire</a></p></li>
<li><p><a href="payments/batch_sdd">Paiements par lot : Prélèvement SEPA (SDD)</a></p></li>
</ul>
</div>

### Lettrage des paiements

The **Payments matching** tool opens all unreconciled customer invoices or
vendor bills and allows you to process them individually, matching all
payments and invoices in one place. You can reach this tool from the
Accounting Dashboard ‣ Customer Invoices / Vendor Bills, click the drop-down
menu button (**⋮**), and select **Payments Matching** , or go to Accounting ‣
Accounting ‣ Reconciliation.

![Payments matching menu in the drop-down menu.](../../../_images/payments-
journal.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Au cours du <a href="bank/reconciliation">rapprochement</a>, si la somme des débits et des crédits ne correspond pas, cela signifie qu’il y a un solde restant qui devra être lettré ultérieurement ou qui doit être annulé directement.</p>
</div>

### Lettrage des paiements par lot

You can use the batch reconciliation feature to reconcile several outstanding
payments or invoices simultaneously for a specific customer or vendor. Go to
Accounting ‣ Reporting ‣ Aged Receivable / Aged Payable. You can see all
transactions that have not been reconciled yet for that partner, and when you
select a customer or vendor, the **Reconcile** option is displayed.

![See the reconcile option.](../../../_images/reconcile-option.png)

## Registering a partial payment

To register a **partial payment** , click **Register payment** from the
related invoice or bill, and enter the amount received or paid. Upon entering
the amount, a prompt appears to decide whether to **Keep open** the invoice or
bill, or **Mark as fully paid**. Select **Keep open** and click **Create
payment**. The invoice or bill is now marked as **Partial**. Select **Mark as
fully paid** if you wish to settle the invoice or bill with a difference in
the amount.

![Partial payment of an invoice or bill.](../../../_images/payment-
difference.png)

## Rapprocher des paiements avec les relevés bancaires

Once a payment has been registered, the status of the invoice or bill is **In
payment**. The next step is [reconciling](bank/reconciliation) it with
the related bank statement line to have the transaction finalized and the
invoice or bill marked as **Paid**.

  * [Paiements en ligne](payments/online)
    * [Installer le patch pour désactiver le paiement des factures en ligne](payments/online/install_portal_patch)
  * [Chèques](payments/checks)
  * [Paiements par lot par dépôt bancaire](payments/batch)
  * [Paiements par lot : Prélèvement SEPA (SDD)](payments/batch_sdd)
  * [Suivi des factures](payments/follow_up)
  * [Virements internes](payments/internal_transfers)
  * [Payer avec SEPA](payments/pay_sepa)
  * [Payer par chèque](payments/pay_checks)
  * [Prévoir les futures factures à payer](payments/forecast)

