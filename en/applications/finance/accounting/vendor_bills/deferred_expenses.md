# Deferred expenses and prepayments

**Deferred expenses** and **prepayments** (also known as **prepaid expense**),
are both costs that have already occurred for unconsumed products or services
yet to receive.

Such costs are **assets** for the company that pays them since it already paid
for products and services still to receive or that are yet to be used. The
company cannot report them on the current **Profit and Loss statement** , or
_Income Statement_ , since the payments will be effectively expensed in the
future.

These future expenses must be deferred on the company’s balance sheet until
the moment in time they can be **recognized** , at once or over a defined
period, on the Profit and Loss statement.

For example, let’s say we pay $ 1200 at once for one year of insurance. We
already pay the cost now but haven’t used the service yet. Therefore, we post
this new expense in a _prepayment account_ and decide to recognize it on a
monthly basis. Each month, for the next 12 months, $ 100 will be recognized as
an expense.

Konvergo ERP Accounting handles deferred expenses and prepayments by spreading them in
multiple entries that are automatically created in _draft mode_ and then
posted periodically.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The server checks once a day if an entry must be posted. It might then take up to 24 hours before
you see a change from <em>draft</em> to <em>posted</em>.</p>
</div>

## Prerequisites

Such transactions must be posted on a **Deferred Expense Account** rather than
on the default expense account.

### Configure a Deferred Expense Account

To configure your account in the **Chart of Accounts** , go to Accounting ‣
Configuration ‣ Chart of Accounts, click on _Create_ , and fill out the form.

![Configuration of a Deferred Expense Account in Konvergo ERP
Accounting](../../../../_images/deferred_expenses01.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This account’s type must be either <em>Current Assets</em> or <em>Prepayments</em></p>
</div>

### Post an expense to the right account

#### Select the account on a draft bill

On a draft bill, select the right account for all the products of which the
expenses must be deferred.

![Selection of a Deferred Expense Account on a draft bill in Konvergo ERP
Accounting](../../../../_images/deferred_expenses02.png)

#### Choose a different Expense Account for specific products

Start editing the product, go to the _Accounting_ tab, select the right
**Expense Account** , and save.

![Change of the Expense Account for a product in
Konvergo ERP](../../../../_images/deferred_expenses03.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It is possible to automate the creation of expense entries for these products (see:
<a href="#automate-the-deferred-expenses">Automate the Deferred Expenses</a>).</p>
</div>

#### Change the account of a posted journal item

To do so, open your Purchases Journal by going to Accounting ‣ Accounting ‣
Purchases, select the journal item you want to modify, click on the account,
and select the right one.

![Modification of a posted journal item's account in Konvergo ERP
Accounting](../../../../_images/deferred_expenses04.png)

## Deferred Expenses entries

### Create a new entry

A **Deferred Expense entry** automatically generates all journal entries in
_draft mode_. They are then posted one by one at the right time until the full
amount of the expense is recognized.

To create a new entry, go to Accounting ‣ Accounting ‣ Deferred Expense, click
on _Create_ , and fill out the form.

Click on **select related purchases** to link an existing journal item to this
new entry. Some fields are then automatically filled out, and the journal item
is now listed under the **Related Expenses** tab.

![Deferred Expense entry in Konvergo ERP
Accounting](../../../../_images/deferred_expenses05.png)

Once done, you can click on _Compute Deferral_ (next to the _Confirm_ button)
to generate all the values of the **Expense Board**. This board shows you all
the entries that Konvergo ERP will post to recognize your expense, and at which date.

![Expense Board in Konvergo ERP
Accounting](../../../../_images/deferred_expenses06.png)

#### What does “Prorata Temporis” mean?

The **Prorata Temporis** feature is useful to recognize your expense the most
accurately possible.

With this feature, the first entry on the Expense Board is computed based on
the time left between the _Prorata Date_ and the _First Recognition Date_
rather than the default amount of time between recognitions.

For example, the Expense Board above has its first expense with an amount of $
70.97 rather than $ 100.00. Consequently, the last entry is also lower and has
an amount of $ 29.03.

### Deferred Entry from the Purchases Journal

You can create a deferred entry from a specific journal item in your
**Purchases Journal**.

To do so, open your Purchases Journal by going to Accounting ‣ Accounting ‣
Purchases, and select the journal item you want to defer. Make sure that it is
posted in the right account (see: Change the account of a posted journal
item).

Then, click on _Action_ , select **Create Deferred Entry** , and fill out the
form the same way you would do to create a new entry.

![Create Deferred Entry from a journal item in Konvergo ERP
Accounting](../../../../_images/deferred_expenses07.png)

## Deferred Expense Models

You can create **Deferred Expense Models** to create your Deferred Expense
entries faster.

To create a model, go to Accounting ‣ Configuration ‣ Deferred Expense Models,
click on _Create_ , and fill out the form the same way you would do to create
a new entry.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can also convert a <em>confirmed Deferred Expense entry</em> into a model by opening it from
Accounting ‣ Accounting ‣ Deferred Expenses and then, by clicking on the
button <em>Save Model</em>.</p>
</div>

### Apply a Deferred Expense Model to a new entry

When you create a new Deferred Expense entry, fill out the **Deferred Expense
Account** with the right recognition account.

New buttons with all the models linked to that account appear at the top of
the form. Clicking on a model button fills out the form according to that
model.

![Deferred Expense model button in Konvergo ERP
Accounting](../../../../_images/deferred_expenses08.png)

## Automate the Deferred Expenses

When you create or edit an account of which the type is either _Current
Assets_ or _Prepayments_ , you can configure it to defer the expenses that are
credited on it automatically.

You have three choices for the **Automate Deferred Expense** field:

  1. **No:** this is the default value. Nothing happens.

  2. **Create in draft:** whenever a transaction is posted on the account, a draft _Deferred Expenses entry_ is created, but not validated. You must first fill out the form in Accounting ‣ Accounting ‣ Deferred Expenses.

  3. **Create and validate:** you must also select a Deferred Expense Model (see: Deferred Expense Models). Whenever a transaction is posted on the account, a _Deferred Expenses entry_ is created and immediately validated.

![Automate Deferred Expense on an account in Konvergo ERP
Accounting](../../../../_images/deferred_expenses09.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can, for example, select this account as the default <b>Expense Account</b> of a product to
fully automate its purchase. (see: <a href="#choose-a-different-expense-account-for-specific-products">Choose a different Expense Account for specific
products</a>).</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../get_started/chart_of_accounts">Chart of accounts</a></p></li>
</ul>
</div>

