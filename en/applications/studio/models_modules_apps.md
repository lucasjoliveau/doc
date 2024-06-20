# Models, modules, and apps

Models determine the logical structure of a database and how data is stored,
organized, and manipulated. In other words, a model is a table of information
that can be linked with other tables. A model usually represents a business
concept, such as a _sales order_ , _contact_ , or _product_.

Modules and apps contain various elements, such as models, views, data files,
web controllers, and static web data.

Note

All apps are modules. Larger, standalone modules are typically referred to as
apps, whereas other modules usually serve as add-ons to said apps.

## Suggested features

When you create a new model or app with Studio, you can choose to add up to 14
features to speed up the creation process. These features bundle fields,
default settings, and views that are usually used together to provide some
standard functionality. Most of these features can be added later on, but
adding them from the start makes the model creation process much easier.
Furthermore, these features interact together in some cases to increase their
usefulness.

Example

Creating a model with the Picture and Pipeline stages features enabled adds
the image in the card layout of the [Kanban view](views.html#studio-views-
multiple-records-kanban).

![Combination of the Picture and Pipeline stages features on the Kanban
view](../../_images/picture-pipeline-kanban.png)

### Contact details

Selecting Contact details adds to the [Form view](views.html#studio-views-
general-form) a [Many2One field](fields.html#studio-fields-relational-fields-
many2one) linked to the _Contact_ model and two of its [Related
Fields](fields.html#studio-fields-relational-fields-related-field): Phone and
Email. The Contact field is also added to the [List view](views.html#studio-
views-multiple-records-list), and the [Map view](views.html#studio-views-
multiple-records-map) is activated.

Example

![Contact details feature on the Form view](../../_images/contact1.png)

### User assignment

Selecting User assignment adds to the [Form view](views.html#studio-views-
general-form) a [Many2One field](fields.html#studio-fields-relational-fields-
many2one) linked to the _Contact_ model, with the following Domain: `Share
User is not set` to only allow the selection of _Internal Users_. In addition,
the many2one_avatar_user widget is used to display the user’s avatar. The
Responsible field is also added to the [List view](views.html#studio-views-
multiple-records-list).

Example

![User assignment feature on the Form view](../../_images/user-assignment.png)

### Date & Calendar

Selecting Date & Calendar adds to the [Form view](views.html#studio-views-
general-form) a [Date field](fields.html#studio-fields-simple-fields-date) and
activates the [Calendar view](views.html#studio-views-timeline-calendar).

### Date range & Gantt

Selecting Date range & Gantt adds to the [Form view](views.html#studio-views-
general-form) two [Date fields](fields.html#studio-fields-simple-fields-date)
next to each other: one to set a start date, the other to set an end date,
using the daterange widget, and activates the [Gantt view](views.html#studio-
views-timeline-gantt).

### Pipeline stages

Selecting Pipeline stages activates the [Kanban view](views.html#studio-views-
multiple-records-kanban), adds several fields such as
[Priority](fields.html#studio-fields-simple-fields-priority) and Kanban State,
and three stages: New, In Progress, and Done. The Pipeline status bar and the
Kanban State field are added to the [Form view](views.html#studio-views-
general-form). The Color field is added to the [List view](views.html#studio-
views-multiple-records-list).

Note

The Pipeline stages feature can be added at a later stage.

### Tags

Selecting Tags adds to the [Form](views.html#studio-views-general-form) and
[List](views.html#studio-views-multiple-records-list) views a [Tags
field](fields.html#studio-fields-relational-fields-tags), creating a _Tag_
model with preconfigured access rights in the process.

### Picture

Selecting Picture adds to the top-right of the [Form view](views.html#studio-
views-general-form) an [Image field](fields.html#studio-fields-simple-fields-
image).

Note

The Picture feature can be added at a later stage.

### Lines

Selecting Lines: adds to the [Form view](views.html#studio-views-general-form)
a [Lines field](fields.html#studio-fields-relational-fields-lines) inside a
Tab component.

### Notes

Selecting Notes adds to the [Form view](views.html#studio-views-general-form)
an [Html field](fields.html#studio-fields-simple-fields-html) using the full
width of the form.

### Monetary value

Selecting Monetary value adds to the [Form](views.html#studio-views-general-
form) and [List](views.html#studio-views-multiple-records-list) views a
[Monetary field](fields.html#studio-fields-simple-fields-monetary). The
[Graph](views.html#studio-views-reporting-graph) and
[Pivot](views.html#studio-views-reporting-pivot) views are also activated.

Note

A _Currency_ field is added and hidden from the view.

### Company

Selecting Company adds to the [Form](views.html#studio-views-general-form) and
[List](views.html#studio-views-multiple-records-list) views a [Many2One
field](fields.html#studio-fields-relational-fields-many2one) linked to the
_Company_ model.

Note

This is only useful if you work in a multi-company environment.

### Custom Sorting

Selecting Custom Sorting adds to the [List view](views.html#studio-views-
multiple-records-list) a drag handle icon to manually reorder records.

Example

![Custom Sorting feature on the List view](../../_images/list-drag-handle.png)

### Chatter

Selecting Chatter adds to the [Form view](views.html#studio-views-general-
form) Chatter functionalities (sending messages, logging notes, and scheduling
activities).

Note

The Chatter feature can be added at a later stage.

Example

![Chatter feature on the Form view](../../_images/chatter1.png)

### Archiving

Selecting Archiving adds to the [Form](views.html#studio-views-general-form)
and [List](views.html#studio-views-multiple-records-list) views the Archive
action and hides archived records from searches and views by default.

## Export and import customizations

When you do any customization with Studio, a new module named Studio
customizations is added to your database.

To export these customizations, go to Main dashboard ‣ Studio ‣ Customizations
‣ Export to download a ZIP file containing all customizations.

To import and install these customizations in another database, connect to the
destination database and go to Main dashboard ‣ Studio ‣ Customizations ‣
Import, then upload the exported ZIP file before clicking on the Import
button.

Warning

Before importing, make sure the destination database contains the same apps
and modules as the source database. Studio does not add the underlying modules
as dependencies of the exported module.

