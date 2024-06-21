# Follow-up on invoices

A follow-up message can be sent to customers when a payment is overdue. Konvergo ERP
helps you identify late payments and allows you to schedule and send the
appropriate reminders using **follow-up actions** that automatically trigger
one or more actions according to the number of overdue days. You can send your
follow-ups via different means, such as email, post, or SMS.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/payment-follow-up-1682">Konvergo ERP Tutorials: Payment Follow-up</a></p></li>
</ul>
</div>

## Configuration

To configure a **Follow-Up Action** , go to Accounting ‣ Configuration ‣
Follow-up Levels, and select or create (a) new follow-up level(s). Several
follow-up actions are available by default under the **Notification** tab, and
the **name** as well as the **number of days** can be changed. The follow-up
**Actions** available are:

  * **Send Email** ;

  * [Send a Letter](../customer_invoices/snailmail#customer-invoices-snailmail);

  * [Send an SMS message](../../../marketing/sms_marketing/pricing/pricing_and_faq#pricing-pricing-and-faq).

You can use a pre-filled template for your messages by selecting a **Content
Template**. To change the template used, hover over the field and click the
**– >**. If enabled, SMS messages have a specific **Sms Template** field.

It is possible to automatically send a reminder by enabling the **Automatic**
option, and attaching the _open_ invoice(s) by enabling **Attach Invoices** ,
within a specific follow-up action.

By clicking on the **Activity** tab, scheduling activities (tasks) is
possible. That way, an activity is automatically scheduled when the follow-up
is triggered. To do so, enable **Schedule Activity** , and select a
**Responsible** person for the task. Choose an **Activity Type** , and enter a
**Summary** on how to handle the activity, if desired.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Set a negative number of days to send a reminder before the actual due date.</p>
</div>

## Follow-up reports

Overdue invoices you need to follow up on are available in Accounting ‣
Customers ‣ Follow-up Reports. By default, Konvergo ERP filters by **Overdue
Invoices** , but you can also filter by **In need of action** in the
**Filters** menu.

When selecting an invoice, you can see all of the customer’s unpaid invoices
(overdue or not), with the due dates of late invoices appearing in red. You
can exclude invoices from a reminder by clicking **Exclude from Follow-ups**.
You can set either **Automatic** or **Manual** reminders as well as a
**Responsible** person for that customer.

To send reminders, click on **Follow up** , and select the action(s) you want
to perform from:

  * **Print** ;

  * **Email** ;

  * **Sms** ;

  * **By post**.

You can **Attach Invoices** and change the content templates from this view.
When done, click **Send** or **Send & Print**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The contact information on the invoice or the contact form is used to send the reminder.</p></li>
<li><p>When the reminder is sent, it is documented in the chatter of the invoice.</p></li>
<li><p>If it is not the right time for a reminder, you can specify the <b>Next Reminder</b> date.
You will get the next report according to the next reminder date set.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Reconcile all bank statements right before launching the follow-up process to avoid sending a
reminder to a customer that has already paid.</p>
</div>

### Debtor’s trust level

To know whether a customer usually pays late or not, you can set a trust level
by marking them as **Good Debtor** , **Normal Debtor** , or **Bad Debtor** on
their follow-up report. To do so, click on the bullet next to the customer’s
name and select a trust level.

![Set debtor's trust level](../../../../_images/debtor-level.png)

### Send reminders in batches

You can send reminder emails in batches from the **Follow-up Reports** page.
To do so, select all the reports you would like to process, click on the
**Action** gear icon, and select **Process follow-ups**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
<li><p><a href="../../../marketing/sms_marketing/pricing/pricing_and_faq">SMS Pricing and FAQ</a></p></li>
<li><p><a href="../customer_invoices/snailmail">Snailmail</a></p></li>
</ul>
</div>

