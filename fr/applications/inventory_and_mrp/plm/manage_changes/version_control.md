# Version control

Use Konvergo ERP’s _Product Lifecycle Management (PLM)_ to manage previous versions of
bills of materials (BoMs). Store former assembly instructions, component
details, and past product design files while keeping the past details out of
the production BoM.

Easily revert to previous BoM versions, when needed. Additionally, use _PLM_
to trace which BoM version was active on specific dates for recalls or
customer complaints.

Every BoM version is stored in an _engineering change order_ (ECO) for
organized testing and improvements without disrupting normal manufacturing
operations.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="engineering_change_orders#plm-eco"><span class="std std-ref">Engineering change order</span></a></p>
</div>

## Current BoM version

To see the current version of the BoM used in production, go to PLM app ‣
Master Data ‣ Bill of Materials, and select the desired BoM from the list.
Then, switch to the **Miscellaneous** tab, where the currently live
**Version** of the BoM is displayed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><abbr title="Bills of Materials">BoMs</abbr> can also be accessed from Manufacturing app ‣ Products ‣ Bill of
Materials.</p>
</div> ![Show the current version BOM in the Misc
tab.](../../../../_images/current-version.png)

## Version history

To manage all former, current, and future versions of a BoM, begin by
navigating to Manufacturing app ‣ Products ‣ Bills of Materials and click the
desired BoM.

From the BoM page, click the **ECO** smart button, and switch to list view by
selecting the **≣ (four horizontal lines)** icon on the top right corner.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>ECO</b> smart button is visible on the <abbr title="Bill of Materials">BoM</abbr> <b>only</b> if the <em>PLM</em> app is installed.</p>
</div> ![Show ECO smart button on a
BoM.](../../../../_images/eco-smart-button.png)

In the list of ECOs for the product, navigate to the search bar at the top,
and click the **▼ (down arrow)** icon on the right to access a drop-down menu
of **Filters**.

Next, filter by **Done** ECOs to view: the revision history of the BoM, the
**Responsible** user who applied the change, and the **Effective Date** of the
BoM.

Click each ECO to view the past components, operations, and design files
associated with the BoM.

![Display ECO revision history for a BoM for a
product.](../../../../_images/eco-list.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the <b>Effective Date</b> field is empty, the <b>Effective</b> date of the <abbr title="Engineering Change Order">ECO</abbr> is
automatically set to <b>As soon as possible</b> and no dates are recorded in the revision
history of the <abbr title="Bill of Materials">BoM</abbr>.</p>
<img alt="List of BOM effective dates." class="align-center" src="../../../../_images/no-effective-date.png"/>
</div>
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>A workaround for checking when the <abbr title="Bill of Materials">BoM</abbr> went live is by navigating to the chatter, and hovering
over the time the <abbr title="Engineering Change Order">ECO</abbr> was moved to the <a href="eco_type#plm-eco-stage-config"><span class="std std-ref">closing stage</span></a>.</p>
</div>

## Design files

Attach computer-aided design (CAD) files, PDFs, images, or other design
material to the BoM itself.

To do so, navigate to PLM app ‣ Master Data ‣ Bill of Materials, and select
the desired BoM. On the BoM, navigate to the _chatter_ , and click the **📎
(paperclip)** icon.

The files associated with the BoM are displayed in the **Files** section. To
add more design files, select the **Attach files** button.

![Show paperclip icon in the chatter to attach files to a
BoM.](../../../../_images/attach-files.png)

### Manage design files in an ECO

Add, modify, and remove files in an ECO. Once the ECO is approved and applied,
the new files are automatically linked to the production BoM. Archived files
are removed from the BoM, but are still accessible in the ECO.

To manage the design files in the ECO, begin by navigating to PLM app ‣
Changes and choose the desired ECO. Next, open the **Attachments** page by
clicking the **Documents** smart button.

Hover over each attachment to reveal the **︙ (three vertical dots)** icon.
From there, choose whether to **Edit** , **Remove** , or **Download** the
file. Any changes made to these files are contained within the ECO, and will
only apply to the production BoM once the [changes are
applied](engineering_change_orders#plm-eco-apply-changes).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>In the <code>Create 60% keyboard</code> <abbr title="Engineering Change Order">ECO</abbr>, the design files are from the original <code>100% keyboard</code> <abbr title="Bill of Materials">BoM</abbr>.
To replace the keyboard PDF, begin by selecting the <b>Documents</b> smart button.</p>
<img alt="Show *Documents* smart button from an active ECO." class="align-center" src="../../../../_images/documents-smart-button.png"/>
<p>On the <b>Attachments</b> page, hover over the <code>100% keyboard manual.pdf</code> design file, and
click the <b>︙ (three vertical dots)</b> icon. Then, click the <b>Remove</b> option to
archive the file.</p>
<p>Next, on the same <b>Attachments</b> page, click the <b>Upload</b> button to upload the
new design file, named <code>60% keyboard manual</code>.</p>
<img alt="View of *Attachments* page from the *Documents* smart button. Displays one archived and one newly added attachment." class="align-center" src="../../../../_images/attachments.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Archived files are <b>not</b> permanently deleted — they can still be accessed in the previous
<abbr title="Engineering Change Order">ECO</abbr>, or as an archived file in the latest <abbr title="Engineering Change Order">ECO</abbr>, where the archival occurred.</p>
</div>

## Apply rebase

Konvergo ERP simplifies merge conflict resolution for concurrent ECOs on the same
product.

Conflicts can occur when the production BoM is updated while other ECOs are
modifying the previous version. Differences between the new and previous
production BoMs are displayed in the **Previous Eco Bom Changes** tab, visible
only in this scenario.

To resolve conflicts and retain ECO changes, click the **Apply Rebase**
button.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Two <abbr title="Engineering Change Orders">ECOs</abbr>, <code>ECO0011</code> and <code>ECO0012</code>, are created when the current <abbr title="Bill of Materials">BoM</abbr> version is <code>5</code>. In
<code>ECO0011</code>, a new component, <code>Space stabilizer</code>, is added, and the changes are applied. This means
the current <abbr title="Bill of Materials">BoM</abbr> version has become <code>6</code>.</p>
<img alt="Apply changes to an ECO to update the production BOM." class="align-center" src="../../../../_images/branch-change.png"/>
<p>This means <code>ECO0012</code> is modifying an outdated <abbr title="Bill of Materials">BoM</abbr>. As shown in the <b>Previous Eco Bom
Changes</b> tab, the <abbr title="Bill of Materials">BoM</abbr> is missing the <code>Space stabilizer</code>.</p>
<p>To ensure the changes applied by <code>ECO0011</code> are kept when the changes occur in <code>ECO0012</code>, click
the <b>Apply Rebase</b> button to apply the previous <abbr title="Engineering Change Order">ECO</abbr> changes, without affecting the
changes already made to <code>ECO0012</code>.</p>
<img alt="Click the *Apply Rebase* button to update the BOM to match the production BOM." class="align-center" src="../../../../_images/merge-change.png"/>
</div>

  *[BoM]: Bill of Materials
  *[ECOs]: Engineering Change Orders
  *[ECO]: Engineering Change Order
  *[BoMs]: Bills of Materials

