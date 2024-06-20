# Version control

Use Odoo’s _Product Lifecycle Management (PLM)_ to manage previous versions of
bills of materials (BoMs). Store former assembly instructions, component
details, and past product design files while keeping the past details out of
the production BoM.

Easily revert to previous BoM versions, when needed. Additionally, use _PLM_
to trace which BoM version was active on specific dates for recalls or
customer complaints.

Every BoM version is stored in an _engineering change order_ (ECO) for
organized testing and improvements without disrupting normal manufacturing
operations.

Pour plus d'infos

[Engineering change order](engineering_change_orders.html#plm-eco)

## Current BoM version

To see the current version of the BoM used in production, go to PLM app ‣
Master Data ‣ Bill of Materials, and select the desired BoM from the list.
Then, switch to the Miscellaneous tab, where the currently live Version of the
BoM is displayed.

Note

BoMs can also be accessed from Manufacturing app ‣ Products ‣ Bill of
Materials.

![Show the current version BOM in the Misc tab.](../../../../_images/current-
version.png)

## Version history

To manage all former, current, and future versions of a BoM, begin by
navigating to Manufacturing app ‣ Products ‣ Bills of Materials and click the
desired BoM.

From the BoM page, click the ECO smart button, and switch to list view by
selecting the ≣ (four horizontal lines) icon on the top right corner.

Note

The ECO smart button is visible on the BoM **only** if the _PLM_ app is
installed.

![Show ECO smart button on a BoM.](../../../../_images/eco-smart-button.png)

In the list of ECOs for the product, navigate to the search bar at the top,
and click the ▼ (down arrow) icon on the right to access a drop-down menu of
Filters.

Next, filter by Done ECOs to view: the revision history of the BoM, the
Responsible user who applied the change, and the Effective Date of the BoM.

Click each ECO to view the past components, operations, and design files
associated with the BoM.

![Display ECO revision history for a BoM for a
product.](../../../../_images/eco-list.png)

Note

If the Effective Date field is empty, the Effective date of the ECO is
automatically set to As soon as possible and no dates are recorded in the
revision history of the BoM.

![List of BOM effective dates.](../../../../_images/no-effective-date.png)

Astuce

A workaround for checking when the BoM went live is by navigating to the
chatter, and hovering over the time the ECO was moved to the [closing
stage](eco_type.html#plm-eco-stage-config).

## Design files

Attach computer-aided design (CAD) files, PDFs, images, or other design
material to the BoM itself.

To do so, navigate to PLM app ‣ Master Data ‣ Bill of Materials, and select
the desired BoM. On the BoM, navigate to the _chatter_ , and click the 📎
(paperclip) icon.

The files associated with the BoM are displayed in the Files section. To add
more design files, select the Attach files button.

![Show paperclip icon in the chatter to attach files to a
BoM.](../../../../_images/attach-files.png)

### Manage design files in an ECO

Add, modify, and remove files in an ECO. Once the ECO is approved and applied,
the new files are automatically linked to the production BoM. Archived files
are removed from the BoM, but are still accessible in the ECO.

To manage the design files in the ECO, begin by navigating to PLM app ‣
Changes and choose the desired ECO. Next, open the Attachments page by
clicking the Documents smart button.

Hover over each attachment to reveal the ︙ (three vertical dots) icon. From
there, choose whether to Edit, Remove, or Download the file. Any changes made
to these files are contained within the ECO, and will only apply to the
production BoM once the [changes are
applied](engineering_change_orders.html#plm-eco-apply-changes).

Example

In the `Create 60% keyboard` ECO, the design files are from the original `100%
keyboard` BoM. To replace the keyboard PDF, begin by selecting the Documents
smart button.

![Show *Documents* smart button from an active
ECO.](../../../../_images/documents-smart-button.png)

On the Attachments page, hover over the `100% keyboard manual.pdf` design
file, and click the ︙ (three vertical dots) icon. Then, click the Remove
option to archive the file.

Next, on the same Attachments page, click the Upload button to upload the new
design file, named `60% keyboard manual`.

![View of *Attachments* page from the *Documents* smart button. Displays one
archived and one newly added attachment.](../../../../_images/attachments.png)

Note

Archived files are **not** permanently deleted — they can still be accessed in
the previous ECO, or as an archived file in the latest ECO, where the archival
occurred.

## Apply rebase

Odoo simplifies merge conflict resolution for concurrent ECOs on the same
product.

Conflicts can occur when the production BoM is updated while other ECOs are
modifying the previous version. Differences between the new and previous
production BoMs are displayed in the Previous Eco Bom Changes tab, visible
only in this scenario.

To resolve conflicts and retain ECO changes, click the Apply Rebase button.

Example

Two ECOs, `ECO0011` and `ECO0012`, are created when the current BoM version is
`5`. In `ECO0011`, a new component, `Space stabilizer`, is added, and the
changes are applied. This means the current BoM version has become `6`.

![Apply changes to an ECO to update the production
BOM.](../../../../_images/branch-change.png)

This means `ECO0012` is modifying an outdated BoM. As shown in the Previous
Eco Bom Changes tab, the BoM is missing the `Space stabilizer`.

To ensure the changes applied by `ECO0011` are kept when the changes occur in
`ECO0012`, click the Apply Rebase button to apply the previous ECO changes,
without affecting the changes already made to `ECO0012`.

![Click the *Apply Rebase* button to update the BOM to match the production
BOM.](../../../../_images/merge-change.png)

  *[BoM]: Bill of Materials
  *[BoMs]: Bills of Materials
  *[ECOs]: Engineering Change Orders
  *[ECO]: Engineering Change Order

