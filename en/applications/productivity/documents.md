# Documents

**Konvergo ERP Documents** allows you to store, view and manage files within Konvergo ERP.

You can upload any type of file (max 64MB per file on Konvergo ERP Online), and
organize them in various workspaces.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/app/documents">Konvergo ERP Documents: product page</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/documents-basics-674">Konvergo ERP Tutorials: Documents basics</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/using-documents-with-your-accounting-app-675?fullscreen=1#">Konvergo ERP Tutorials: Using Documents with your Accounting App</a></p></li>
</ul>
</div>

## Configuration

By going to Documents ‣ Configuration ‣ Settings, you can enable the
centralization of files attached to a specific area of your activity. For
example, by ticking **Human Resources** , your HR documents are automatically
available in the HR workspace, while documents related to Payroll are
automatically available in the Payroll sub-workspace . You can change the
default workspace by using the dropdown menu and edit its properties by
clicking the internal link button (**➔**).

![Enable the centralization of files attached to a specific area of your
activity.](../../_images/files-centralization.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If you enable the centralization of your accounting files and documents, it is necessary to
click on <b>Journals</b> and define each journal independently to allow automatic
synchronization.</p>
<img alt="Enable the centralization of files attached to your accounting." class="align-center" src="../../_images/accounting-files-centralization.png"/>
</li>
<li><p>If you select a new workspace, existing documents aren’t moved. Only newly created documents
will be found under the new workspace.</p></li>
</ul>
</div>

## Workspaces

Workspaces are hierarchical folders having their own set of tags and actions.
Default workspaces exist, but you can create your own by going to Documents ‣
Configuration ‣ Workspaces and clicking on **Create**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Workspaces</b> and <b>Sub-workspaces</b> can be created, edited, or deleted by
clicking on the gear icon <b>⚙</b> on the left menu.</p>
</div> ![Create sub-workspaces from the left
menu](../../_images/sub-workspaces-creation.png)

## Tags

Tags are used within workspaces to add a level of differentiation between
documents. They are organized per category and filters can be used to sort
them.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The tags of a parent workspace apply to the child workspaces automatically.</p></li>
<li><p>Tags can be created and modified by going to Configuration ‣ Tags.</p></li>
<li><p>Tags can also be created, edited, or deleted, by clicking on the gear icon <b>⚙</b>, on
the left menu.</p></li>
</ul>
</div>

## Documents management

When clicking on a specific document, the right panel displays different
options. On the top, additional options might be available: **Download** ,
**Share** , **Replace** , **Lock** or **Split**. It is also possible to **Open
chatter** or **Archive** the document.

![right panel options](../../_images/right-panel-options.png)

Then, you can modify the name of your file by clicking on **Document**. A
**Contact** or an **Owner** can be assigned. The related **Workspace** can be
modified and it is possible to access the related **Journal Entry** or to add
**Tags**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The <b>Contact</b> is the person related to the document and assigned to it. He can only
view the document and not modify it. I.e.: an existing supplier in your database is the contact
for their bill.</p></li>
<li><p>The person who creates a document is, by default <b>Owner</b> of it and has complete
rights to the document. It is possible to replace the owner of a document. I.e.: an employee
must be owner of a document to be able to see it in “My Profile”.</p></li>
</ul>
</div>

Finally, different **Actions** are available at the bottom of the right panel,
depending on the workspace where your document is stored.

## Workflow actions

Workflow actions help you streamline the management of your documents and your
overall business operations. These are automated actions that can be created
and customized for each workspace. For example, create documents, process
bills, sign, organize files, add tags to a file or move it to another
workspace with a single click etc. These workflow actions appear on the right
panel when it meets the criteria you set.

### Create workflow actions

To create workflow actions, go to Documents ‣ Configuration ‣ Actions and then
click on **Create**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>An action applies to all <b>Child Workspaces</b> under the <b>Parent Workspace</b> you
selected.</p>
</div>

### Set the conditions

You can **Create** a new **Action** or edit an existing one. You can define
the **Action Name** and then set the conditions that trigger the appearance of
the action button (**▶**) on the right-side panel when selecting a file.

There are three basic types of conditions you can set:

  1. **Tags** : you can both use the **Contains** and **Does not contain** conditions, meaning the files _must have_ or _mustn’t have_ the tags set here.

  2. **Contact** : the files must be associated with the contact set here.

  3. **Owner** : the files must be associated with the owner set here.

![Example of a workflow action's basic condition in Konvergo ERP
Documents](../../_images/basic-condition-example.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you don’t set any conditions, the action button appears for all files located inside the
selected workspace.</p>
</div>

#### Advanced condition type: domain

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>It is recommended to have some knowledge of Konvergo ERP development to properly configure <em>Domain</em>
filters.</p>
</div>

To access the _Domain_ condition, the [developer
mode](../general/developer_mode#developer-mode) needs to be activated.
Once that’s done, select the **Domain** condition type, and click on **Add
Filter**.

![Activating the domain condition type in Konvergo ERP
Documents](../../_images/activate-domain-condition.png)

To create a rule, you typically select a **field** , an **operator** , and a
**value**. For example, if you want to add a workflow action to all the PDF
files inside a workspace, set the **field** to _Mime Type_ , the **operator**
to _contains_ , and the **value** to _pdf_.

![Example of a workflow action's domain condition in Konvergo ERP
Documents](../../_images/domain-condition-example.png)

Click on **Add node** (plus-circle icon) and **Add branch** (ellipsis icon) to
add conditions and sub-conditions. You can then specify if your rule should
match **ALL** or **ANY** conditions. You can also edit the rule directly using
the **Code editor**.

![Add a node or a branch to a workflow action's condition in Konvergo ERP
Documents](../../_images/use-domain-condition.png)

### Configure the actions

Select the **Actions** tab to set up your action. You can simultaneously:

  * **Set Contact** : add a contact to the file, or replace an existing contact with a new one.

  * **Set Owner** : add an owner to the file, or replace an existing owner with a new one.

  * **Move to Workspace** : move the file to any workspace.

  * **Create** : create one of the following items attached to the file in your database:

>     * **Product template** : create a product you can edit directly.
>
>     * **Task** : create a Project task you can edit directly.
>
>     * **Signature request** : create a new Sign template to send out.
>
>     * **Sign directly** : create a Sign template to sign directly.
>
>     * **Vendor bill** : create a vendor bill using OCR and AI to scrape
> information from the file content.
>
>     * **Customer invoice** : create a customer invoice using OCR and AI to
> scrape information from the file.
>
>     * **Vendor credit note** : create a vendor credit note using OCR and AI
> to scrape information from the file.
>
>     * **Credit note** : create a customer credit note using OCR and AI to
> scrape information from the file.
>
>     * **Applicant** : create a new HR application you can edit directly.

  * **Set Tags** : add, remove, and replace any number of tags.

  * **Activities - Mark all as Done** : mark all activities linked to the file as done.

  * **Activities - Schedule Activity** : create a new activity linked to the file as configured in the action. You can choose to set the activity on the document owner.

![Example of a workflow action Konvergo ERP Documents](../../_images/workflow-action-
example.png)

## Digitize documents with AI and optical character recognition (OCR)

Documents available in the Finance workspace can be digitized. Select the
document you want to digitize, click on **Create Bill** , **Create Customer
Invoice** or **Create credit note** , and then click on **Send for
Digitization**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../finance/accounting/vendor_bills/invoice_digitization">AI-powered document digitization</a></p>
</div>

