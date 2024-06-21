# Views

Views are the interface that allows displaying the data contained in a model.
One model can have several views, which are simply different ways to show the
same data. In Studio, views are organized into four categories: general,
multiple records, timeline, and reporting.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To change the default view of a model, go to Studio ‣ Views ‣ Dropdown menu
(⋮) ‣ Set as Default.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>

## General views

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The settings described below are found under the view’s <b>View</b> tab unless specified
otherwise.</p>
</div>

### Form

The **Form** view is used when creating and editing records, such as contacts,
sales orders, products, etc.

  * To structure a form, drag-and-drop the **Tabs and Columns** element found under the **\+ Add** tab.

  * To prevent users from creating, editing, or deleting records, untick **Can Create** , **Can Edit** , or **Can Delete**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Sales order model's Form view" class="align-center" src="../../_images/form-sales-order.png"/>
</div>

### Activity

The **Activity** view is used to schedule and have an overview of activities
(emails, calls, etc.) linked to records.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This view can only be modified within Studio by editing the XML code.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Lead/Opportunity model's Activity view" class="align-center" src="../../_images/activity-lead-opportunity.png"/>
</div>

### Search

The **Search** view is added on top of other views to filter, group, and
search records.

  * To add custom **Filters** and structure them using **Separators** , go to the **\+ Add** tab and drag and drop them under **Filters**.

  * To add an existing field under the search dropdown menu, go to the **\+ Add** tab and drag-and-drop it under **Autocompletion Fields**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Project model's Search view on the Kanban view" class="align-center" src="../../_images/search-project-kanban.png"/>
</div>

## Multiple records views

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The settings described below are found under the view’s <b>View</b> tab unless specified
otherwise.</p>
</div>

### Kanban

The **Kanban** view is often used to support business flows by moving records
across stages or as an alternative way to display records inside _cards_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the <b>Kanban</b> view exists, it is used by default to display data on mobile devices
instead of the <a href="#studio-views-multiple-records-list"><span class="std std-ref">List view</span></a>.</p>
</div>

  * To prevent users from creating new records, untick **Can Create**.

  * To create records directly within the view, in a minimalistic form, enable **Quick Create**.

  * To change the way records are grouped by default, select a new group under **Default Group by**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>0

### List

The **List** view is used to overview many records at once, look for records,
and edit simple records.

  * To prevent users from creating, editing, or deleting records, untick **Can Create** , **Can Edit** , or **Can Delete**.

  * To create and edit records directly within the view, select either **New record on top** or **New record at the bottom** under **Editable**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>1

  * To edit several records at once, tick **Enable Mass Editing**.

  * To change the way records are sorted by default, select a field under **Sort By**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>3

### Map

The **Map** view is used to display records on a map. For example, it is used
in the Field Service app to plan an itinerary between different tasks.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>4

  * To select which kind of contact should be used on the map, select it under **Contact Field**.

  * To hide the name or the address of the record, tick **Hide name** or **Hide Address**.

  * To add information from other fields, select them under **Additional Fields**.

  * To have a route suggested between the different records, tick **Enable Routing** and select which field should be used to sort records for the routing.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>5

## Timeline views

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>6

### Calendar

The **Calendar** view is used to overview and manage records inside a
calendar.

  * To create records directly within the view instead of opening the Form view, enable **Quick Create**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>7

  * To color records on the calendar, select a field under **Color**. All the records sharing the same value for that field are displayed using the same color.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>8

  * To display events lasting the whole day at the top of the calendar, select a [Checkbox field](fields#studio-fields-simple-fields-checkbox) that specifies if the event lasts the whole day.

  * To choose the default time scale used to display events, select **Day** , **Week** , **Month** , or **Year** under **Default Display Mode**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can modify views by using the built-in XML editor. To do so, activate <a href="../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode</span></a>, go to the view you want to edit, select the <b>View</b> tab and then
click on <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>
</div>9 <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>0

### Cohort

The **Cohort** view is used to examine the life cycle of records over a time
period. For example, it is used in the Subscriptions app to view the
subscriptions’ retention rate.

  * To display a measure (i.e., the aggregated value of a given field) by default on the view, select a **Measure Field**.

  * To choose which time interval is used by default to group results, select **Day** , **Week** , **Month** , or **Year** under **Interval**.

  * To change the cohort **Mode** , select either **Retention** the percentage of records staying over a period of time, it starts at 100% and decreases with time or **Churn** the percentage of records moving out over a period of time - it starts at 0% and increases with time.

  * To change the way the **Timeline** (i.e., the columns) progresses, select either **Forward** (from 0 to +15) or **Backward** (from -15 to 0). For most purposes, the **Forward** timeline is used.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>1

### Gantt

The **Gantt** view is used to forecast and examine the overall progress of
records. Records are represented by a bar under a time scale.

  * To prevent users from creating or editing records, untick **Can Create** or **Can Edit**.

  * To fill cells in gray whenever a record should not be created there (e.g., on weekends for employees), tick **Display Unavailability**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>2

  * To show a total row at the bottom, tick **Display Total row**.

  * To collapse multiple records in a single row, tick **Collapse First Level**.

  * To choose which way records are grouped by default on rows (e.g., per employee or project), select a field under **Default Group by**.

  * To define a default time scale to view records, select **Day** , **Week** , **Month** , or **Year** under **Default Scale**.

  * To color records on the view, select a field under **Color**. All the records sharing the same value for that field are displayed using the same color.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>3

  * To specify with which degree of precision each time scale should be divided by, select **Quarter Hour** , **Half Hour** , or **Hour** under **Day Precision** , **Half Day** or **Day** under **Week Precision** , and **Month Precision**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>4

## Reporting views

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>5

### Pivot

The **Pivot** view is used to explore and analyze the data contained in
records in an interactive manner. It is especially useful to aggregate numeric
data, create categories, and drill down the data by expanding and collapsing
different levels of data.

  * To access all records whose data is aggregated under a cell, tick **Access records from cell**.

  * To divide the data into different categories, select field(s) under **Column grouping** , **Row grouping - First level** , or **Row grouping - Second level**.

  * To add different types of data to be measured using the view, select a field under **Measures**.

  * To display a count of records that made up the aggregated data in a cell, tick **Display count**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>6

### Graph

The **Graph** view is used to showcase data from records in a bar, line, or
pie chart.

  * To change the default chart, select **Bar** , **Line** , or **Pie** under **Type**.

  * To choose a default data dimension (category), select a field under **First dimension** and, if needed, another under **Second dimension**.

  * To select a default type of data to be measured using the view, select a field under **Measure**.

  * _For Bar and Line charts only_ : To sort the different data categories by their value, select **Ascending** (from lowest to highest value) or **Descending** (from highest to lowest) under **Sorting**.

  * _For Bar and Pie charts only_ : To access all records whose data is aggregated under a data category on the chart, tick **Access records from graph**.

  * _For Bar charts only_ : When using two data dimensions (categories), display the two columns on top of each other by default by ticking **Stacked graph**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>7

### Dashboard

The **Dashboard** view is used to display multiple reporting views and key
performance indicators. Which elements are displayed on the view depends on
the configuration of the other reporting views.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are editing a view using the XML editor, avoid making changes directly to standard
views and inherited views, as those would be reset and would not be kept in case of an update
or module upgrade. Always make sure you select the right Studio inherited views. Indeed, when
you modify a view in Studio by drag-and-dropping a new field, a specific Studio inherited view
and its XPath, the latter which defines which part of the view is modified, are automatically
generated.</p>
</div>8

