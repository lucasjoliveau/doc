# Shop Floor overview

The _Shop Floor_ module is a companion module to the _Manufacturing_ app.
_Shop Floor_ provides a visual interface for processing manufacturing orders
(MOs) and work orders. It also allows manufacturing employees to track the
amount of time spent working on manufacturing and work orders.

The _Shop Floor_ module is installed alongside the _Manufacturing_ app. It
cannot be installed by itself. To install the _Manufacturing_ app, navigate to
Apps, search for `manufacturing` in the **Search…** bar, and then click
**Install** on the **Manufacturing** app card.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <em>Shop Floor</em> module replaces the tablet view functionality of the <em>Manufacturing</em> app, and is
only available in Konvergo ERP versions 16.4 and later.</p>
<p>To check the version number of an Konvergo ERP database, navigate to Settings and scroll
down to the <b>About</b> section at the bottom of the page. The version number is displayed
there.</p>
<p>To switch to a newer version of Konvergo ERP, see the documentation on <a href="../../../../administration/upgrade">upgrading a database</a>.</p>
</div>

## Navigation

_Shop Floor_ is broken down into three main views, which can be selected from
the navigation bar at the top of the module:

  * The **All** page serves as the main dashboard for the module, and displays information cards for MOs.

  * Each work center also has a dedicated page, which shows information cards for work orders assigned to that work center. Work center pages can be toggled on or off by clicking the **\+ (plus)** button in the navigation bar, selecting or deselecting them on the pop-up window that appears, and then clicking **Confirm**.

  * The **My** page shows information cards for all work orders assigned to the employee whose profile is currently active in the operator panel on the left side of the module. Other than only showing work orders assigned to the active employee, this page functions the same as the pages for each work center.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To isolate an <abbr title="Manufacturing Order">MO</abbr> or work order, so that no other orders appear, simply search the reference
number of the <abbr title="Manufacturing Order">MO</abbr> in the <b>Search…</b> bar at the top of the module. This search filter
remains active while switching between the different module views.</p>
</div>

On the left side of the module is the operator panel, which shows all of the
employees currently signed in to _Shop Floor_ , and allows new employees to
sign in. The operator panel is always available in the module, regardless of
which view is selected. It can be toggled on or off by clicking the
**sidebar** button at the extreme left of the navigation bar.

![The "sidebar" button, which is used to toggle the operator panel on or
off.](../../../../_images/sidebar-button.png)

### All page

By default, the **All** page shows an information card for every MO that is
_ready to start_. An MO is considered ready to start once it has been
confirmed, and all required components are available.

To view every confirmed MO regardless of readiness, click the **x** button on
the **Ready to Start** filter to remove it from the **Search…** bar.

#### MO information card

An MO information card on the **All** page shows all of the relevant details
of the associated MO, and also provides employees with options for processing
the MO.

The header for an MO card shows the MO number, the product and number of units
being produced, and the status of the MO. If work has not yet begun on the MO,
the status appears as **Confirmed**. Once work has begun, the status updates
to **In Progress**. If all work orders for an MO have been completed and the
MO is ready to close, the status updates to **To Close**.

The main body of an MO card shows a line for each completed work order, if
any, followed by the current work order that needs to be completed. Completed
work orders are indicated by a green check mark to the right of title of the
work order. The current work order is indicated by a button that opens the
page for the work center to which the order is assigned.

Below the current work order is a line titled **Register Production** , which
is used to record the number of product units produced. To manually enter the
number of units produced, click on the **Register Production** line, enter a
value in the **Units** field of the resulting pop-up window, then click
**Validate**.

Alternatively, click the **# Units** button on the right side of the line,
which automatically records the number of units the MO was created for as the
number of units produced. For example, if an MO is created for 10 units of a
dining table, clicking the **10 units** button records that 10 units were
produced.

The footer of the MO card displays a **Close Production** button. This is used
to close the MO once production is completed. However, if there are any
quality checks required for the MO as a whole (not the work orders within it),
a **Quality Checks** button appears instead. Clicking **Quality Checks** opens
a pop-up window, from which any required quality checks can be completed.

After clicking **Close Production** , the MO card begins to fade away, and an
**Undo** button appears on the footer. Clicking **Undo** causes the MO to
remain open. Once the MO card disappears completely, the work order is closed.

On the right side of the footer is an **⋮ (options)** button, which opens a
pop-up window with additional options for the MO:

  * **Scrap** is used to send components to a scrap location when they are found to be defective.

  * **Add Work Order** is used to add an additional work order to the MO.

  * **Add Component** is used to add an additional component to the MO.

  * **Open Backend MO** opens the MO in the Manufacturing app.

![An information card for an MO on the "All" page of the Shop Floor
module.](../../../../_images/mo-card.png)

### Work center pages

By default, the page for each work center shows an information card for every
work order assigned to it that is _ready to start_. A work order is considered
ready to start once the MO it is a part of is ready to start, and any
preceding work orders have been completed.

To view every confirmed work order assigned to a work center regardless of
readiness, click the **x** button on the **Ready to Start** filter to remove
it from the **Search…** bar.

#### Work order information card

A work order information card on a work center’s page shows all of the
relevant details of the associated work order, and also provides employees
with options for processing the work order.

The header for a work order card shows the reference number of the MO that the
work order is a part of, the product and number of units being produced, and
the status of the work order. If work has not yet begun on the work order, the
status appears as **To Do**. Once work has begun, the status updates to
display a timer showing the total time the work order has been worked on.

The main body of a work order card shows a line for each step required to
complete the work order. Work order steps can be completed by clicking on the
line, then following the instructions on the pop-up window that appears.
Alternatively, clicking the checkbox on the right side of each line
automatically marks the step as completed.

Below the final step of the work order is a line titled **Register
Production** , which functions the same as the **Register Production** line on
an MO card. Registering the number of units produced using the **Register
Production** line on a work order card also completes the step for the
associated MO card.

If the work order being processed is the final work order for the MO, a
**Close Production** button appears on the footer of the work order card.
Clicking **Close Production** closes both the work order and the MO, unless a
quality check is required for the MO. In this case, the quality check must be
completed from the MO card before the MO can be closed.

Alternatively, if the MO requires the completion of additional work orders, a
**Mark as Done** button appears instead. Clicking **Mark as Done** marks the
current work order as completed, and causes the next work order to appear on
the page for the work center it is assigned to.

After clicking **Close Production** or **Mark as Done** , the work order card
begins to fade away, and an **Undo** button appears on the footer. Clicking
**Undo** causes the work order to remain open. Once the work order card
disappears completely, the work order is marked as **Finished** on the MO.

On the right side of the footer is an **⋮ (options)** button, which opens a
pop-up window with additional options for the work order:

  * **Scrap** is used to send components to a scrap location when they are found to be defective.

  * **Add Component** is used to add an additional component to the MO.

  * **Move to work center** is used to transfer the work order to a different work center.

  * **Suggest a Worksheet improvement** allows the user to propose a change to the work order’s instructions or steps.

  * **Create a Quality Alert** opens a quality alert form that can be filled out to alert a quality team about a potential issue.

![An information card for a work order in the Shop Floor
module.](../../../../_images/wo-card.png)

### Operator panel

The operator panel is used to manage the employees that are signed in to the
_Shop Floor_ module. The panel shows the name and profile picture of every
employee that is currently signed in across all instances of the database.

To interact with _Shop Floor_ as a specific employee, click the employee’s
name to activate their profile. Profiles that are not active appear with their
names and profile pictures greyed-out.

When an employee is selected in the operator panel, they can begin working on
a work order by clicking the work order’s heading. If an employee is working
on one or more work orders, the work order title(s) appear under their name,
along with a timer showing how long they’ve been working on each order.

To add a new employee to the operator panel, click the **\+ Add Operator**
button at the bottom of the panel. Then, select an employee from the **Select
Employee** pop-up window.

To remove an employee from the operator panel, simply click the **x** button
next to their name in the panel.

![The operator panel of the Shop Floor module, showing three employees signed
in.](../../../../_images/operator-panel.png)

  *[MOs]: Manufacturing Orders
  *[MO]: Manufacturing Order

