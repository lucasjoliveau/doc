# Search and filter records

Konvergo ERP uses filters to include only the most relevant records depending on the
purpose of the view you are on. However, you can edit the default filter or
search for specific values.

## Preconfigured filters

You can modify the default selection of records by clicking **Filters** and
selecting one or several **preconfigured filters**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>On the Sales Analysis report, only records at the sales order stage are selected by default.
However, you could <em>also</em> include records at the quotation stage by selecting
<b>Quotations</b>. Furthermore, you could <em>only</em> include records from a specific year, for
example <em>2022</em>, by selecting Order Date ‣ 2022.</p>
<img alt="Using preconfigured filters on the Sales Analysis report" class="align-center" src="../../_images/preconfigured-filters.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you select preconfigured filters from the same group (i.e., that are <em>not</em> separated by an
horizontal line), the records can match <em>any</em> condition to be included. However, if you select
filters from different groups, the records have to match <em>all</em> condition to be included.</p>
</div>

## Custom filters

You can create custom filters using most fields present on the model by
clicking Filters ‣ Add Custom Filter, selecting a field, an operator, a value,
and clicking **Apply**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>You could <em>only</em> include records from a single salesperson on the Sales Analysis report, for
example <em>Mitchell Admin</em>, by selecting <b>Salesperson</b> as the field, <b>is equal
to</b> as the operator, and typing <code>Mitchell Admin</code> as the value.</p>
<img alt="Using a custom filter on the Sales Analysis report" class="align-center" src="../../_images/custom-filter.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the records should <em>only</em> match one of several conditions, click <b>Add a condition</b>
before applying a custom filter. If the records should match <em>all</em> conditions, add new custom
filters instead.</p>
</div>

## Search for values

You can use the search field to quickly look for specific values and add them
as a filter. Either type the full value you are searching for and select the
desired field, or type a part of the value, click the dropdown button (**⏵**)
before the chosen field, and select the exact value you are looking for.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Instead of adding a custom filter to select records where <em>Mitchell Admin</em> is the salesperson on
the Sales Analysis report, you could search for <code>Mitch</code>, click the dropdown button
(<b>⏵</b>) next to <b>Search Salesperson for: Mitch</b>, and select
<b>Mitchell Admin</b>.</p>
<img alt="Searching for a specific value on the Sales Analysis report" class="align-center" src="../../_images/search-values.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Using the search field is equivalent to using the <em>contains</em> operator when adding a custom
filter. If you enter a partial value and directly select the desired field, <em>all</em> records
containing the characters you typed for the selected field will be included.</p>
</div>

## Group records

You can click **Group By** below the search field to cluster records together
according to one of the **preconfigured groups**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>You could group the records by salesperson on the Sales Analysis report by clicking
<b>Group By</b> and selecting <b>Salesperson</b>. No records are filtered out.</p>
<img alt="Grouping records on the Sales Analysis report" class="align-center" src="../../_images/group.png"/>
</div>

You can **customize groups** by using a wide selection of fields present on
the model. To do so, click Group By ‣ Add Custom Group, select a field, and
click **Apply**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can use several groups at the same time. The first group you select is the main cluster, the
next one you add further divides the main group’s categories, and so on.</p>
</div>

