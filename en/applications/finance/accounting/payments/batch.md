# Batch payments by bank deposit

A **batch deposit** is a convenient way to group customer payments and deposit
them into your bank account. The feature lets you list multiple payments and
generate a detailed deposit slip with a batch reference. This reference can be
used when reconciling to match bank statement lines with transactions in the
batch deposit.

## Configuration

Go to Accounting ‣ Configuration ‣ Settings ‣ Customer Payments and tick
**Batch Payments** to activate the feature.

## Deposit multiple payments in batch

### Register payments

Before performing a batch deposit, it is necessary to register each
transaction’s payment. To do so, open the corresponding customer invoice and
click **Register Payment**. In the pop-up window, select the **Journal**
linked to your bank account and **Batch Deposit** as the **Payment Method** ,
and click **Create Payment**.

![Registering a customer payment as part of a batch
deposit](../../../../_images/batch-payments.png)

### Add payments to a batch deposit

To add payments to a batch deposit, go to Accounting ‣ Customers ‣ Batch
Payments, and click **New**. Next, select the **Bank** and choose **Batch
Deposit** as the **Payment Method**.

![Filling out a new inbound batch payment form](../../../../_images/batch-
customer-payment.png)

Click **Add a line**. In the pop-up window, tick all payments to include in
the batch deposit, then click **Select**.

![Selecting all payments to include in the batch
deposit](../../../../_images/batch-lines-selection.png)

Once done, click **Validate** to finalize the batch deposit.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Click <b>Print</b> to download a PDF file to include with the deposit slip.</p>
</div>

### Bank reconciliation

Once the bank transactions are on your database, you can reconcile bank
statement lines with the batch payment. To do so, go to the **Accounting
Dashboard** and click **Reconcile Items** on the related bank account. Go to
the **Batch Payments** tab to select a specific batch and click **Validate**
to finalize the process.

![Reconciling the batch payment with all its
transactions](../../../../_images/batch-reconciliation.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If a specific payment could not be processed by the bank or is missing, remove the related
payment before reconciling.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payments">Payments</a></p></li>
<li><p><a href="batch_sdd">Batch payments: SEPA Direct Debit (SDD)</a></p></li>
</ul>
</div>

