# Closing tickets

Once work has been completed on a _Helpdesk_ ticket in Konvergo ERP, there are several
ways it can be closed. Manually closing solved tickets keeps the pipeline up
to date, while automatically closing inactive tickets prevents unnecessary
blocking issues. Allowing customers to close their own tickets minimizes
confusion around whether an issue is considered solved or not. This results in
increased operational capacity for support teams, and higher customer
satisfaction.

## Manually close solved tickets

As work on a ticket progresses, it is moved along to the next stage in the
pipeline. Once the issue is solved, the ticket is moved to a _folded_ stage.
This marks the ticket as _closed_.

To fold a stage, navigate to the Helpdesk dashboard and click on a team to
open the pipeline. Hover over a stage’s heading, and then click the gear icon
that appears in the top-right corner of that stage’s kanban column.

![View of stage on Helpdesk pipeline with emphasis on gear icon and edit stage
option.](../../../../_images/closing-edit-stage-gear.png) <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Clicking the gear icon also displays the option to <b>Fold</b> the stage. This setting folds
the stage <em>temporarily</em> to simplify the kanban view. This does <em>not</em> close the tickets in this
stage. It also does not permanently fold the stage. If a stage needs to be folded so the tickets
can be marked as closed, continue following the steps below.</p>
</div>

From the menu that appears, select **Edit Stage**. This will open the stage’s
settings. Check the box labeled **Folded in Kanban** towards the top of the
window, and then **Save & Close** to confirm the changes. Now, tickets that
reach this stage will be considered as _closed_.

> ![Stage settings page.](../../../../_images/closing-folded-setting.png)

## Automatically close inactive tickets

Tickets that are inactive for a set period of time can be automatically
closed. At that point, they will be moved to a folded stage.

Go to the team’s settings page by going to Helpdesk ‣ Configuration ‣ Teams.
Under the **Self-Service** section, enable **Automatic Closing**.

If one of the team’s stages is set to be folded in the kanban view, it will be
the default selection in the **Move to Stage** field. If the team has more
than one folded stage, the stage that occurs first in the pipeline will be the
default. If no stage is folded, the default selection will be the last stage
in the pipeline.

The **After days of inactivity** field defaults to `7`, but can be adjusted if
necessary.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The <b>After days of inactivity</b> field does <b>not</b> take the working calendar into
account when tracking the amount of time a ticket has been inactive.</p>
</div>

If only certain stages should be used to track days of inactivity, they can be
added to the **In Stages** field.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A team’s pipeline is created with the following stages:</p>
<ul>
<li><p><code>New</code></p></li>
<li><p><code>In Progress</code></p></li>
<li><p><code>Customer Feedback</code></p></li>
<li><p><code>Closed</code></p></li>
</ul>
<p>Tickets can linger in the <b>Customer Feedback stage</b>, because once an issue is solved,
customers may not respond immediately. At that point, the tickets can be closed automatically.
However, tickets in the <b>New</b> and <b>In Progress</b> stages may remain inactive
due to assignment or workload issues. Closing these tickets automatically would result in issues
going unsolved.</p>
<p>Therefore, the <b>Automatic Closing</b> settings would be configured as below:</p>
<ul>
<li><p><b>Automatic Closing</b>: <em>checked</em></p></li>
<li><p><b>Move to Stage</b>: <code>Solved</code></p></li>
<li><p><b>After``7</b><b>days of inactivity</b></p></li>
<li><p><b>In Stages</b>: <code>Customer Feedback</code></p></li>
</ul>
<img alt="Example of Automatic Closing settings." class="align-center" src="../../../../_images/closing-automatic-settings-example.png"/>
</div>

## Allow customers to close their own tickets

Enabling the **Closure by Customers** setting allows customers to close their
own ticket(s) when they determine that their issue has been resolved.

Start by navigating to Helpdesk ‣ Configuration ‣ Teams and select a team. On
the team’s settings page, scroll to the **Self-Service** section and check the
box for **Closure by Customers**.

![Customer closing setting in Konvergo ERP Helpdesk.](../../../../_images/closing-by-
customer-setting.png)

Once the ticket closing settings are enabled, a **Close Ticket** button will
be available for customers when they view their ticket through the customer
portal.

![Customer view of ticket closing in Konvergo ERP
Helpdesk.](../../../../_images/closing-customer-view.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Customers are able to view their tickets by clicking the <b>View the ticket</b> link they
receive by email. The link is included in the <b>Request Acknowledgment</b> template, which
is added to the first stage of a team by default. This link does not require a customer to have
access to the portal to view or respond to their ticket.</p>
<p>Customers with access to the portal will be able to view their tickets under My
Account ‣ Tickets.</p>
</div>

