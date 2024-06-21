# Reporting

You can find several reports under the **Reporting** menu of most apps that
let you analyze and visualize the data of your records.

## Selecting a view

Depending on the report, Konvergo ERP can display the data in various ways. Sometimes,
a unique view fully tailored to the report is available, while several views
are available for others. However, two generic views are dedicated to
reporting: the graph and pivot views.

### Graph view

The graph view is used to visualize your records’ data, helping you identify
patterns and trends. The view is often found under the **Reporting** menu of
apps but can be found elsewhere. Click the **graph view button** located at
the top right to access it.

![Selecting the graph view](../../_images/graph-button.png)

### Pivot view

The pivot view is used to aggregate your records’ data and break it down for
analysis. The view is often found under the **Reporting** menu of apps but can
be found elsewhere. Click the **pivot view button** located at the top right
to access it.

![Selecting the pivot view](../../_images/pivot-button.png)

## Choosing measures

After selecting a view, you should ensure only the relevant records are
[filtered](search). Next, you should choose what is measured. By default,
a measure is always selected. If you wish to edit it, click **Measures** and
choose one or, only for pivots, multiple measures.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When you select a measure, Konvergo ERP aggregates the values recorded on that field for the filtered
records. Only numerical fields (<a href="../studio/fields#studio-fields-simple-fields-integer"><span class="std std-ref">integer</span></a>,
<a href="../studio/fields#studio-fields-simple-fields-decimal"><span class="std std-ref">decimal</span></a>, <a href="../studio/fields#studio-fields-simple-fields-monetary"><span class="std std-ref">monetary</span></a>) can be measured. In addition, the <b>Count</b>
option is used to count the total number of filtered records.</p>
</div>

After choosing what you want to measure, you can define how the data should be
[grouped](search#search-group) depending on the dimension you want to
analyze. By default, the data is often grouped by _Date > Month_, which is
used to analyze the evolution of a measure over the months.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>When you filter a single time period, the option to compare it against another one appears.</p>
<img alt="Using the comparison option" src="../../_images/comparison.png"/>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Select measures</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">Group measures</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><p>Among other measures, you could add the <b>Margin</b> and <b>Count</b> measures
to the Sales Analysis report. By default, the <b>Untaxed Amount</b> measure is
selected.</p>
<img alt="Selecting different measures on the Sales Analysis report" src="../../_images/measures.png"/>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><p>You could group the measures by <b>Product Category</b> at the level of rows on the
previous Sales Analysis report example.</p>
<img alt="Adding a group on the Sales Analysis report" src="../../_images/single-group.png"/>
</div></div>
</div>

## Using the pivot view

Grouping data is quintessential to the pivot view. It enables drilling down
the data to gain deeper insights. While you can use the **Group By** option to
quickly add a group at the level of rows, as shown in the example above, you
can also click the plus button (**➕**) next to the **Total** header at the
level of rows _and_ columns, and then select one of the **preconfigured
groups**. To remove one, click the minus button (**➖**).

Once you have added a group, you can add new ones on the opposite axis or the
newly created subgroups.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>You could further divide the measures on the previous Sales Analysis report example by the
<b>Salesperson</b> group at the level of columns and by the <b>Order Date &gt; Month</b>
group on the <b>All / Saleable / Office Furniture</b> product category.</p>
<img alt="Adding multiple groups on the Sales Analysis report" src="../../_images/multiple-groups.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>Switch the rows and columns’ groups by clicking the flip axis button (<b>⇄</b>).</p></li>
<li><p>Click on a measure’s label to sort the values by ascending (⏶) or descending (⏷) order.</p></li>
<li><p>Download a <code>.xlsx</code> version of the pivot by clicking the download button (<b>⭳</b>).</p></li>
</ul>
</div>

## Using the graph view

Three graphs are available: the bar, line, and pie charts.

**Bar charts** are used to show the distribution or a comparison of several
categories. They are especially useful as they can deal with larger data sets.

**Line charts** are useful to show changing time series and trends over time.

**Pie charts** are used to show the distribution or a comparison of a small
number of categories when they form a meaningful whole.

Bar chartLine chartPie chart

![Viewing the Sales Analysis report as a bar chart](../../_images/bar.png)

![Viewing the Sales Analysis report as a line chart](../../_images/line.png)

![Viewing the Sales Analysis report as a pie chart](../../_images/pie.png)

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>For <b>bar</b> and <b>line</b> charts, you can use the stacked option when you have at least two
groups, which then appear on top of each other instead of next to each other.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-2-2-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-2-2-0" name="2-0" role="tab" tabindex="0">Stacked bar chart</button><button aria-controls="panel-2-2-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-1" name="2-1" role="tab" tabindex="-1">Regular bar chart</button><button aria-controls="panel-2-2-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-2" name="2-2" role="tab" tabindex="-1">Stacked line chart</button><button aria-controls="panel-2-2-3" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-3" name="2-3" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-2-2-0" class="sphinx-tabs-panel" id="panel-2-2-0" name="2-0" role="tabpanel" tabindex="0"><img alt="Stacked bar chart example" src="../../_images/stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-1" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-1" name="2-1" role="tabpanel" tabindex="0"><img alt="Non-stacked bar chart example" src="../../_images/non-stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-2" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-2" name="2-2" role="tabpanel" tabindex="0"><img alt="Stacked line chart example" src="../../_images/stacked-line.png"/>
</div><div aria-labelledby="tab-2-2-3" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-3" name="2-3" role="tabpanel" tabindex="0"><img alt="Non-stacked line chart example" src="../../_images/non-stacked-line.png"/>
</div></div>
<p>For <b>line</b> charts, you can use the cumulative option to sum values, which is especially useful
to show the change in growth over a time period.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-3-3-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-3-3-0" name="3-0" role="tab" tabindex="0">Cumulative line chart</button><button aria-controls="panel-3-3-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-3-3-1" name="3-1" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-3-3-0" class="sphinx-tabs-panel" id="panel-3-3-0" name="3-0" role="tabpanel" tabindex="0"><img alt="Cumulative line chart example" src="../../_images/cumulative.png"/>
</div><div aria-labelledby="tab-3-3-1" class="sphinx-tabs-panel" hidden="true" id="panel-3-3-1" name="3-1" role="tabpanel" tabindex="0"><img alt="Regular line chart example" src="../../_images/non-cumulative.png"/>
</div></div>
</div>

