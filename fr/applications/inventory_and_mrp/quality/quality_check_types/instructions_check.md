# Instructions quality check

In Konvergo ERP _Quality_ , an _Instructions_ check is one of the quality check types
that can be selected when creating a new quality check or quality control
point (QCP). _Instructions_ checks consist of a text entry field that allows
the creator to provide instructions for how to complete the check.

For a full overview of how to configure a quality check or a QCP, see the
documentation on [quality
checks](../quality_management/quality_checks#quality-quality-management-
quality-checks) and [quality control
points](../quality_management/quality_control_points#quality-quality-
management-quality-control-points).

## Process an Instructions quality check

There are multiple ways that _Instructions_ quality checks can be processed.
If a quality check is assigned to a specific manufacturing, inventory, or work
order, the check can be processed on the order itself. Alternatively, a check
can be processed from the check’s page.

### Process from the quality check’s page

To process an _Instructions_ quality check from the check’s page, begin by
navigating to Quality ‣ Quality Control ‣ Quality Checks, and select a quality
check. Follow the **Instructions** for how to complete the check.

If the product passes the check, click the **Pass** button above the quality
check form. If the product does not pass the check, click the **Fail** button,
instead.

### Process quality check on an order

To process an _Instructions_ quality check on an order, select a manufacturing
order or inventory order (receipt, delivery, return, etc.) for which a check
is required. Manufacturing orders can be selected by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders, and clicking on an order.
Inventory orders can be selected by navigating to Inventory, clicking the **#
To Process** button on an operation card, and selecting an order.

On the selected manufacturing or inventory order, a purple **Quality Checks**
button appears above the order. Click the button to open the **Quality Check**
pop-up window, from which any quality checks created for the order can be
processed.

![The Quality Check pop-up window on a manufacturing or inventory
order.](../../../../_images/quality-check-pop-up.png)

To complete an _Instructions_ quality check, follow the instructions detailed
in the **Quality Check** pop-up window. Finally, click **Validate** to confirm
that the check has been completed.

If an issue or defect is found during the quality check, a quality alert may
need to be created to notify a quality team. To do so, click the **Quality
Alert** button that appears at the top of the manufacturing or inventory order
after the check is validated.

Clicking **Quality Alert** opens a quality alert form on a new page. For a
complete guide on how to fill out quality alert forms, view the documentation
on [quality alerts](../quality_management/quality_alerts#quality-quality-
management-quality-alerts).

### Process work order quality check

When configuring a QCP that is triggered by a manufacturing order, a specific
work order can also be specified in the **Work Order Operation** field on the
QCP form. If a work order is specified, an _Instructions_ quality check is
created for that specific work order, rather than the manufacturing order as a
whole.

Quality checks configured for work orders must be completed from the tablet
view. To do so, begin by navigating to Manufacturing ‣ Operations ‣
Manufacturing Orders. Select a manufacturing order that includes a work order
for which a quality check is required. Open the tablet view for that work
order by clicking the **📱 (tablet)** button on the order’s line.

With tablet view open, complete the steps listed on the left side of the
screen until the _Instructions_ quality check step is reached. Upon reaching
the check, the instructions for how to complete it will appear at the top of
the screen. Follow the instructions, then click **Next** to move on to the
next step.

![An Instructions check for a work order.](../../../../_images/work-order-
instructions-check.png)

If an issue or defect is found during the quality check, a quality alert may
need to be created to notify a quality team. To do so, click the **☰ (menu)**
button in the tablet view, and then select **Quality Alert** from the **Menu**
pop-up window.

Clicking **Quality Alert** opens a **Quality Alerts** pop-up window, from
which a quality alert can be created. For a complete guide to quality alert
creation, view the documentation on [quality
alerts](../quality_management/quality_alerts#quality-quality-management-
quality-alerts).

  *[QCP]: Quality Control Point

