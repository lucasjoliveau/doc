# Validations

Notify stakeholders and managers automatically by assigning approvers to
stages of [engineering change
orders](../manage_changes/engineering_change_orders#plm-eco) (ECOs) under
review. Changes can only be applied after the assigned approver accepts them.
Approvals ensure reviews by team members, which prevents mistakes and
premature actions.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../manage_changes/eco_type#plm-eco-stage-config"><span class="std std-ref">Stage configuration</span></a></p>
</div>

## Add approver

To add an approver, first go to the PLM app, and click on the project card of
an ECO type to open the Gantt view of the ECOs.

On the **Engineering Change Orders** page, hover over the intended stage, and
select the **⚙️ (gear)** icon. Then, click **Edit** to open a pop-up window.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Approvers can be added to any stage, but it’s strongly recommended to assign them to the
<em>verification</em> stage, which comes before the <em>closing</em> stage, where <abbr title="Engineering Change Orders">ECOs</abbr> are applied, and the
<abbr title="Bill of Materials">BoM</abbr> version is updated.</p>
<p>See the documentation about <a href="../manage_changes/eco_type#plm-eco-stage-config"><span class="std std-ref">stage types</span></a> for more information.</p>
</div>

In the **Edit** stage pop-up window, click the **Add a line** button, located
under **Approvals**. Then, type in the approver’s position (or title) under
**Role** (e.g. `Engineering Manager`, `Quality Team`, etc.), and select the
relevant **User** from the drop-down menu.

Next, set the **Approval Type** to **Is required to approve** , **Approves,
but the approval is optional** , or **Comments only**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Assign the <code>CTO</code>, « Mitchell Admin, » as a required approver for <abbr title="Engineering Change Orders">ECOs</abbr> in the <code>Validated</code> stage in
the <code>New Product Introduction</code> ECO type.</p>
<p>Approvals from the quality and marketing teams are <b>not</b> required to apply changes to the <abbr title="Engineering Change Order">ECO</abbr>
because their <b>Approval Type</b> is set to <b>Approves, but the approval is
optional</b> and <b>Comments only</b>, respectively.</p>
<img alt='Set an approver that "Is required to approve" ECOs in the "Validated" stage.' class="align-center" src="../../../../_images/approvers.png"/>
</div>

## Manage approvals

Approvers can easily track their to-do approvals by navigating to the PLM app,
and looking at the card for an ECO type, which shows the count of open tasks
assigned to them.

Here’s what each button on an ECO project card does:

  1. The **# Engineering Changes** button displays a count of in-progress ECOs of this ECO type. Clicking the button opens the Gantt view of the **Engineering Change Orders** page.

  2. **My Validations** displays a count of ECOs the approver must accept or reject. Clicking on this button displays ECOs pending approval or rejected (marked with the red **Blocked** state).

  3. The **All Validations** button shows the count of ECOs awaiting approval or rejected by any approver. Clicking it reveals these pending ECOs.

  4. **To Apply** displays a count of ECOs to which the user needs to apply changes. Clicking on the button displays all the ECOs to approve, and apply changes to, in the verification stage.

ECOs marked with the green **Done** stage have already been approved, and the
user just needs to click on the ECO to enter the form view, and click the
**Apply Changes** button.

![Display count of validations to-do and buttons to open filtered list of
ECOs.](../../../../_images/validation-overview.png)

### Approve ECOs

Navigate to an ECO in a verification stage, while logged in as the assigned
approver, to see the **Approve** , **Reject** , and **Apply Changes** buttons.

To approve the ECO, and apply the changes onto the production BoM, click
**Approve** , and then **Apply Changes**.

Note that the **Apply Changes** button will **not** work unless the
**Approve** button was clicked first. Additionally, the chatter logs the
history of the clicked buttons.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>When the <b>Approval Type</b> is <b>not</b> set to <b>Is required to approve</b>, approval
from the associated user is not needed before applying changes with the <b>Apply Changes</b>
button. Thus, the <b>Apply Changes</b> button <b>will work</b> without requiring the
<b>Approve</b> button to be clicked first.</p>
</div>

### Automated activities

When an ECO is moved to a verification stage, a planned activity is
automatically created for assigned approvers to review the ECO. Approvers
receive a notification in their activities inbox, accessible through the **🕘
(clock)** icon at the top of the page.

In the to-do task list, the **Engineering Change Order (ECO)** notification
displays the number of activities marked **Late** , **Today** , and
**Future**. Clicking on each of these buttons shows a filtered Gantt view of
the respective ECOs.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Scheduled activities are shown as a number on the <b>🕘 (clock)</b> icon, with <code>5</code> <abbr title="Engineering Change Orders">ECOs</abbr>
pending approval <b>Today</b>. Currently, there are <code>0</code> <b>Late</b> or
<b>Future</b> <abbr title="Engineering Change Orders">ECOs</abbr>.</p>
<blockquote>
<div><img alt="Show scheduled approvals notifications for the user." class="align-center" src="../../../../_images/todo-list.png"/>
</div></blockquote>
</div>

By clicking a pending ECO, a _planned activity_ for **ECO Approval** is
recorded in the chatter. Click on the **i (Info)** icon to view additional
information, including the approval’s **Created** date, the approver
**Assigned to** it, and the due date.

![Show additional details of the planned ECO
approval.](../../../../_images/planned-activity.png)

#### Follow-up activities

When ECOs are rejected, tasks need to be assigned to project members for
required modifications before ECO approval. To create tasks with deadlines,
navigate to the rejected ECO form, and go to the chatter.

Select the **Mark Done** button in the **Planned Activities** section of the
chatter to close the activity, and open a pop-up window for creating tasks.

![Show *Mark Done* window to show *Done & Schedule Next*, *Done*, and
*Discard* buttons to close the planned activity.](../../../../_images/mark-as-
done.png)

In the **Mark Done** window, click **Done & Schedule Next** to open a new
**Schedule an Activity** window. Next, set the **Assigned to** team member and
the **Due Date** for completing the changes. Provide task details in the
**Summary** field and the text box. Click the **Schedule** button to close the
window.

After closing the window, on the ECO form, move the ECO back one stage. Doing
so ensures that when the team member completes the changes, and returns the
ECO to the verification stage, a new **ECO Approval** task is created for the
approver.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The approver creates an activity for the <b>Responsible</b> of the <abbr title="Engineering Change Order">ECO</abbr>, <code>Laurie Poiret</code>,
that details the changes required for the approver to <b>Accept</b> the <abbr title="Engineering Change Order">ECO</abbr>. Clicking the
<b>Schedule</b> button creates a planned activity for Laurie due on <code>08/15/2023</code>.</p>
<img alt="Create a scheduled activity for follow-up changes to a rejected ECO." class="align-center" src="../../../../_images/schedule-an-activity.png"/>
</div>

  *[ECOs]: Engineering Change Orders
  *[ECO]: Engineering Change Order
  *[BoM]: Bill of Materials

