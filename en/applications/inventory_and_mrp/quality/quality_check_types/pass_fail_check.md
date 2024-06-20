# Pass - Fail quality check

In Odoo _Quality_ , a _Pass - Fail_ check is one of the quality check types
that can be selected when creating a new quality check or quality control
point (QCP). _Pass - Fail_ checks consist of a text field that allows the
creator to specify a certain criteria that a product must meet to pass the
check.

## Create a Pass - Fail quality check

There are two distinct ways that _Pass - Fail_ quality checks can be created.
A single check can be manually created. Alternatively, a QCP can be configured
that automatically creates checks at a predetermined interval.

This documentation only details the configuration options that are unique to
_Pass - Fail_ quality checks and QCP. For a full overview of all the
configuration options available when creating a single check or a QCP, see the
documentation on [quality
checks](../quality_management/quality_checks.html#quality-quality-management-
quality-checks) and [quality control
points](../quality_management/quality_control_points.html#quality-quality-
management-quality-control-points).

### Quality check

To create a single _Pass - Fail_ quality check, navigate to Quality ‣ Quality
Control ‣ Quality Checks, and click New. Fill out the new quality check form
as follows:

  * In the Type drop-down field, select the Pass - Fail quality check type.

  * In the Team drop-down field, select the quality team responsible for managing the check.

  * In the Instructions text field of the Notes tab, enter instructions for how to complete the quality check and the criteria that must be met for the check to pass.

![A quality check form configured for a Pass - Fail quality
check.](../../../../_images/quality-check-form.png)

### Quality Control Point (QCP)

To create a QCP that generates _Pass - Fail_ quality checks automatically,
begin by navigating to Quality ‣ Quality Control ‣ Control Points, and click
New. Fill out the new QCP form as follows:

  * In the Type drop-down field, select the Pass - Fail quality check type.

  * In the Team drop-down field, select the quality team responsible for managing the checks created by the QCP.

  * In the Instructions text field, enter instructions for how to complete the quality check and the criteria that must be met for the check to pass.

![A Quality Control Point \(QCP\) form configured to create a Pass - Fail
quality check.](../../../../_images/qcp-form.png)

## Process a Pass - Fail quality check

Once created, there are multiple ways that _Measure_ quality checks can be
processed. If a quality check is assigned to a specific inventory,
manufacturing, or work order, the check can be processed on the order itself.
Alternatively, a check can be processed from the check’s page.

### From the check’s page

To process a _Measure_ quality check from the check’s page, begin by
navigating to Quality ‣ Quality Control ‣ Quality Checks, and select a quality
check. Follow the Instructions for how to complete the check.

If the criteria for the check is met, click the Pass button at the top-left
corner of the page. If the criteria is not met, click the Fail button.

### On an order

To process a _Pass - Fail_ quality check on an order, select a manufacturing
order or inventory order (receipt, delivery, return, etc.), for which a check
is required. Manufacturing orders can be selected by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders, and clicking on an order.
Inventory orders can be selected by navigating to Inventory, clicking the # To
Process button on an operation card, and selecting an order.

On the selected manufacturing or inventory order, a purple Quality Checks
button appears at the top of the order. Click the button to open the Quality
Check pop-up window, which shows all of the quality checks required for that
order.

To process a _Pass - Fail_ quality check, follow the instructions shown on the
Quality Check pop-up window. If the criteria for the check is met, click the
Pass button at the bottom of the window. If the criteria is not met, click the
Fail button.

![A Pass - Fail quality check pop-up window on a manufacturing or inventory
order.](../../../../_images/pass-fail-check-pop-up.png)

If a quality alert must be created, click the Quality Alert button that
appears at the top of the manufacturing or inventory order after the check
fails. Clicking Quality Alert opens a quality alert form on a new page. For a
complete guide on how to fill out quality alert forms, view the documentation
on [quality alerts](../quality_management/quality_alerts.html#quality-quality-
management-quality-alerts).

### On a work order

When configuring a QCP that is triggered during manufacturing, a specific work
order can also be specified in the Work Order Operation field on the QCP form.
If a work order is specified, a _Pass - Fail_ quality check is created for
that specific work order, rather than the manufacturing order as a whole.

_Pass - Fail_ quality checks configured for work orders must be processed from
the tablet view. To do so, begin by navigating to Manufacturing ‣ Operations ‣
Manufacturing Orders. Select a manufacturing order that includes a work order
for which a quality check is required. Open the tablet view for that work
order by selecting the Work Orders tab, and then clicking the 📱 (tablet)
button on the order’s line.

With tablet view open, complete the steps listed on the left side of the
screen until the _Pass - Fail_ quality check step is reached. Upon reaching
the check, follow the instructions that appear at the top of the screen. If
the criteria for the check is met, click the Pass button at the top-right of
the screen. If the criteria is not met, click the Fail button.

![A Pass - Fail check for a manufacturing work
order.](../../../../_images/work-order-pass-fail-check.png)

If a quality alert must be created, do so by clicking the ☰ (menu) button in
the tablet view, and selecting Quality Alert from the Menu pop-up window. A
Quality Alerts pop-up window appears, from which a quality alert can be
created. For a complete guide on how to fill out quality alert forms, view the
documentation on [quality
alerts](../quality_management/quality_alerts.html#quality-quality-management-
quality-alerts).

  *[QCP]: Quality Control Point

