# ECO type

An _ECO type_ is assigned to _engineering change orders_ (ECOs) to organize
and track changes to products and bills of materials (BoMs). Each ECO type
separates ECOs into a project in Gantt view, ensuring collaborators and
stakeholders **only** view and assist with relevant BoM improvements.

For example, an electronic chip manufacturer might use “New Product
Introduction”, “Product Improvement”, “Component Change”, and “Firmware
Update” ECO types. Then, designers and engineers can focus on ECOs in the “New
Product Introduction” and “Product Improvement” projects, avoiding unrelated
supplier change or firmware update ECOs.

## Create ECO type

To access and manage ECO types, navigate to PLM app ‣ Configuration ‣ ECO
Types.

Create a new ECO type by clicking **New**. On the new **ECO Types** form, fill
in the following information:

  * **Name** : the name of the ECO type, which will organize all of the ECOs of this _type_ in a project.

  * **Email Alias** : if this optional field is filled, emails submitted to this email address automatically generate ECOs in the left-most stage of this ECO type.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The <code>Formulation change</code> <abbr title="Engineering Change Order">ECO</abbr> type is used to organize and track related <abbr title="Engineering Change Orders">ECOs</abbr> in a single
project. Configuring the <b>Email Alias</b> field generates <abbr title="Engineering Change Orders">ECOs</abbr> in the <code>Formulation
change</code> project sent to the email address, <code>pawlish-change@pawlished-glam.odoo.com</code>.</p>
<img alt="Example of an ECO type." class="align-center" src="../../../../_images/create-eco-type.png"/>
</div>

## Edit ECO type

Modify existing ECO type names and email aliases by navigating to the PLM app
‣ Configuration ‣ ECO Types page. There, click on the desired ECO type from
the list.

On the form for each ECO type, proceed to edit the **Name** and **Email
Alias** fields.

## Étapes

Within an ECO type project, _stages_ are like milestones and are used to
identify the progress of the ECO before the changes are ready to be applied.
(e.g. “Feedback”, “In Progress”, “Approved”, “Complete”)

Additionally, required approvers can be added to each stage, ensuring that
changes to the production BoM cannot proceed until the approver reviews and
approves the ECO. Doing so prevents errors on the production BoM by enforcing
at least one review of suggested changes before they’re applied on a
production BoM.

For best practice, there should be at least one _verification_ stage, which is
a stage with a required approver, and one _closing_ stage, which stores ECOs
that have been either canceled or approved for use as the next production BoM.

### Create stage

To add a stage, go to the PLM app and select the intended project for an ECO
type from the **PLM Overview** dashboard.

Then, on the **Engineering Change Orders** project pipeline for the ECO type,
click the **\+ Stage** button. Doing so reveals a text box to fill in the name
of the stage. After filling it in, click the **Add** button to finish adding
the stage.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A new <code>Assigned</code> stage separates assigned <abbr title="Engineering Change Orders">ECOs</abbr> from the unassigned ones in the <code>New</code> stage.
Adding another stage helps the product manager track unassigned tasks.</p>
<img alt="Create a new stage in a project for an ECO type." class="align-center" src="../../../../_images/create-stage.png"/>
</div>

### Verification stage

Click an ECO type from PLM app ‣ Overview to open a kanban view of ECOs of
this type.

To configure a verification stage, hover over the intended stage, and select
the **⚙️ (gear)** icon. Then, click **Edit** to open a pop-up window.

Configure the verification stage in the edit stage pop-up window, by checking
the box for **Allow to apply changes**.

Then, add an approver in the **Approvers** section, by clicking **Add a line**
, and specifying the **Role** of the reviewer, their **User** , and **Approval
Type**.

Make sure at least one approver is configured with the **Approval Type** :
**Is required to approve**.

The approver listed is automatically notified when ECOs are dropped in the
stage specified in the pop-up window. Once finished, click **Save & Close**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>In the <abbr title="Engineering Change Order">ECO</abbr> type <code>New Product Introduction</code>, the verification stage <code>Validated</code> is configured by
clicking the <b>⚙️ (gear)</b> icon, and selecting <b>Edit</b>. Doing so opens the
<b>Edit: Validated</b> pop-up window.</p>
<p>By adding the <code>Engineering manager</code> as an approver, only <abbr title="Engineering Change Orders">ECOs</abbr> approved by this user can proceed
to the next stage, and have the changes applied on the production <abbr title="Bill of Materials">BoM</abbr>.</p>
<p>Additionally, check the <b>Allow to apply changes</b> option to ensure proper behavior.</p>
<img alt='Show "Allow to apply changes" option is checked.' class="align-center" src="../../../../_images/verification-stage.png"/>
</div>

### Closing stage

Configure a closing stage by opening the **Edit: [stage]** pop-up window. To
do so, hover over the intended stage and click the **⚙️ (gear)** icon that
appears in the top-right corner. Then, click **Edit** from the drop-down menu.

On the **Edit: [stage]** pop-up window, select the check boxes for **Folded in
kanban view** , **Allow to apply changes** and **Final Stage**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The closing stage, <code>Effective</code> is configured by checking the <b>Folded in kanban view</b>,
<b>Allow to apply changes</b>, and <b>Final Stage</b> options</p>
</div> ![Show configurations of the closing
stage.](../../../../_images/closing-stage.png)

  *[ECO]: Engineering Change Order
  *[ECOs]: Engineering Change Orders
  *[BoM]: Bill of Materials

