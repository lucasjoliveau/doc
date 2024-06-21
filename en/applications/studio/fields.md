# Fields and widgets

Fields structure the models of a database. If you picture a model as a table
or spreadsheet, fields are the columns where data is stored in the records
(i.e., the rows). Fields also define the type of data that is stored within
them. How the data is presented and formatted on the UI is defined by their
widget.

From a technical point of view, there are 15 field types in Konvergo ERP. However, you
can choose from 20 fields in Studio, as some field types are available more
than once with a different default widget.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><b>New Fields</b> can only be added to the <a href="views#studio-views-general-form"><span class="std std-ref">Form</span></a> and
<a href="views#studio-views-multiple-records-list"><span class="std std-ref">List</span></a> views. On other views, you can only add
<b>Existing Fields</b> <span class="dfn"><span>(fields already on the model)</span></span>.</p>
</div>

## Simple fields

Simple fields contain basic values, such as text, numbers, files, etc.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>

### Text (`char`)

The **Text** field is used for short text containing any character. One text
line is displayed when filling out the field.

  * **Badge** : displays the value inside a rounded shape, similar to a tag. The value cannot be edited on the UI, but a default value can be set.

  * **Copy to Clipboard** : users can copy the value by clicking a button.

  * **E-mail** : the value becomes a clickable _mailto_ link.

  * **Image** : displays an image using a URL. The value cannot be edited manually, but a default value can be set.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>

  * **Phone** : the value becomes a clickable _tel_ link.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>

  * **URL** : the value becomes a clickable URL.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Examples of Text fields with different widgets" class="align-center" src="../../_images/text-examples.png"/>
</div>

### Multiline Text (`text`)

The **Multiline Text** field is used for longer text containing any type of
character. Two text lines are displayed on the UI when filling out the field.

  * **Copy to Clipboard** : users can copy the value by clicking a button.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Examples of Multiline Text fields with different widgets" class="align-center" src="../../_images/multiline-text-examples.png"/>
</div>

### Integer (`integer`)

The **Integer** field is used for all integer numbers (positive, negative, or
zero, without a decimal).

  * **Percentage Pie** : displays the value inside a percentage circle, usually for a computed value. The value cannot be edited on the UI, but a default value can be set.

  * **Progress Bar** : displays the value next to a percentage bar, usually for a computed value. The field cannot be edited manually, but a default value can be set.

  * **Handle** : displays a drag handle icon to order records manually in [List view](views#studio-views-multiple-records-list).

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Examples of Integer fields with different widgets" class="align-center" src="../../_images/integer-examples.png"/>
</div>

### Decimal (`float`)

The **Decimal** field is used for all decimal numbers (positive, negative, or
zero, with a decimal).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Decimal numbers are displayed with two decimals after the decimal point on the UI, but they are
stored in the database with more precision.</p>
</div>

  * **Monetary** : it is similar to using the Monetary field. It is recommended to use the later as it offers more functionalities.

  * **Percentage** : displays a percent character `%` after the value.

  * **Percentage Pie** : displays the value inside a percentage circle, usually for a computed value. The field cannot be edited manually, but a default value can be set.

  * **Progress Bar** : displays the value next to a percentage bar, usually for a computed value. The field cannot be edited manually, but a default value can be set.

  * **Time** : the value must follow the _hh:mm_ format, with a maximum of 59 minutes.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Examples of Decimal fields with different widgets" class="align-center" src="../../_images/decimal-examples.png"/>
</div>

### Monetary (`monetary`)

The **Monetary** field is used for all monetary values.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When you first add a <b>Monetary</b> field, you are prompted to add a <b>Currency</b>
field if none exists already on the model. Konvergo ERP offers to add the <b>Currency</b> field for
you. Once it is added, add the <b>Monetary</b> field again.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>0

### Html (`html`)

The **Html** field is used to add text that can be edited using the Konvergo ERP HTML
editor.

  * **Multiline Text** : disables the Konvergo ERP HTML editor to allow editing raw HTML.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>1

### Date (`date`)

The **Date** field is used to select a date on a calendar.

  * **Remaining Days** : the remaining number of days before the selected date is displayed (e.g., _In 5 days_), based on the current date.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>2

### Date & Time (`datetime`)

The **Date & Time** field is used to select a date on a calendar and a time on
a clock. The user’s current time is automatically used if no time is set.

  * **Date** : used to record the time without displaying it on the UI.

  * **Remaining days** : displays the remaining number of days before the selected date (e.g., _In 5 days_), based on the current date and time.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>3

### Checkbox (`boolean`)

The **Checkbox** field is used when a value should only be true or false,
indicated by checking or unchecking a checkbox.

  * **Button** : displays a radio button. The widget works without switching to the edit mode.

  * **Toggle** : displays a toggle button. The widget works without switching to the edit mode.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>4

### Selection (`selection`)

The **Selection** field is used when users should select a single value from a
group of predefined values.

  * **Badge** : displays the value inside a rounded shape, similar to a tag. The value cannot be edited on the UI, but a default value can be set.

  * **Badges** : displays all selectable values simultaneously inside rectangular shapes, organized horizontally.

  * **Priority** : displays star symbols instead of values, which can be used to indicate an importance or satisfaction level, for example. This has the same effect as selecting the Priority field, although, for the latter, four priority values are already predefined.

  * **Radio** : displays all selectable values at the same time as radio buttons.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>5

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>6

### Priority (`selection`)

The **Priority** field is used to display a three-star rating system, which
can be used to indicate importance or satisfaction level. This field type is a
Selection field with the **Priority** widget selected by default and four
priority values predefined. Consequently, the **Badge** , **Badges** ,
**Radio** , and **Selection** widgets have the same effects as described under
Selection.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>8

### File (`binary`)

The **File** field is used to upload any type of file, or sign a form
(**Sign** widget).

  * **Image** : users can upload an image file, which is then displayed in [Form view](views#studio-views-general-form). This has the same effect as using the Image field.

  * **PDF Viewer** : users can upload a PDF file, which can be then browsed from the [Form view](views#studio-views-general-form).

  * **Sign** : users can electronically sign the form. This has the same effect as selecting the Sign field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Non-default widgets, when available, are presented as bullet points below.</p>
</div>9

### Image (`binary`)

The **Image** field is used to upload an image and display it in [Form
view](views#studio-views-general-form). This field type is a File field
with the **Image** widget selected by default. Consequently, the **File** ,
**PDF Viewer** , and **Sign** widgets have the same effects as described under
File.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>0

### Sign (`binary`)

The **Sign** field is used to sign the form electronically. This field type is
a File field with the **Sign** widget selected by default. Consequently, the
**File** , **Image** , and **PDF Viewer** widgets have the same effects as
described under File.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>1

## Relational fields

Relational fields are used to link and display the data from records on
another model.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>2

### Many2One (`many2one`)

The **Many2One** field is used to link another record (from another model) to
the record being edited. The record’s name from the other model is then
displayed on the record being edited.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>3 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>4

  * **Badge** : displays the value inside a rounded shape, similar to a tag. The value cannot be edited on the UI.

  * **Radio** : displays all selectable values at the same time as radio buttons.

### One2Many (`one2many`)

The **One2Many** field is used to display the existing relations between a
record on the current model and multiple records from another model.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>6

### Lines (`one2many`)

The **Lines** field is used to create a table with rows and columns (e.g., the
lines of products on a sales order).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>8

### Many2Many (`many2many`)

The **Many2Many** field is used to link multiple records from another model to
multiple records on the current model. Many2Many fields can use **Disable
creation** , **Disable opening** , **Domain** , just like Many2One fields.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This works differently than selecting the <a href="#studio-fields-simple-fields-image"><span class="std std-ref">Image field</span></a> directly, as the image is not stored in Konvergo ERP when using a
<b>Text</b> field with the <b>Image</b> widget. For example, it can be useful if you
want to save disk space.</p>
</div>9

  * **Checkboxes** : users can select several values using checkboxes.

  * **Tags** : users can select several values appearing in rounded shapes, also known as _tags_. This has the same effect as selecting the Tags field.

### Tags (`many2many`)

The **Tags** field is used to display several values from another model
appearing in rounded shapes, also known as _tags_. This field type is a
Many2Many field with the **Tags** widget selected by default. Consequently,
the **Checkboxes** and **Many2Many** widgets have the same effects as
described under Many2Many.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>0 <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>1

### Related Field (`related`)

A **Related Field** is not a relational field per se; no relationship is
created between models. It uses an existing relationship to fetch and display
information from another record.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>2

## Properties

  * **Invisible** : When it is not necessary for users to view a field on the UI, tick **Invisible**. It helps clear the UI by only showing the essential fields depending on a specific situation.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>4

  * **Required** : If a field should always be completed by the user before being able to proceed, tick **Required**.

  * **Read only** : If users should not be able to modify a field, tick **Read only**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>5

  * **Label** : The **Label** is the field’s name on the UI.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Tick <b>Enable SMS</b> to add an option to send an SMS directly from Konvergo ERP next to the
field.</p>
</div>6

  * **Help Tooltip** : To explain the purpose of a field, write a description under **Help Tooltip**. It is displayed inside a tooltip box when hovering with your mouse over the field’s label.

  * **Placeholder** : To provide an example of how a field should be completed, write it under **Placeholder**. It is displayed in light gray in lieu of the field’s value.

  * **Widget** : To change the default appearance or functionality of a field, select one of the available widgets.

  * **Default value** : To add a default value to a field when a record is created, use **Default value**.

  * **Limit visibility to groups** : To limit which users can see the field, select a user access group.

  *[UI]: User Interface

