# Scrap inventory

In some cases, a product in inventory may be damaged or found to be defective.
If it is not possible to repair or return the product, Konvergo ERP _Inventory_ allows
users to scrap it, ensuring that usable inventory counts remain accurate.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les ordres de mise au rebut peuvent être consultés en allant à Inventaire ‣ Opérations ‣ Rebut. Chaque ordre de mise au rebut indique la date et l’heure de création de l’ordre, ainsi que le produit et la quantité mis au rebut.</p>
<p>To view the total quantity of each item scrapped, navigate to Inventory ‣
Configuration ‣ Locations. Remove the <b>Internal</b> filter from the
<b>Search…</b> bar to display virtual locations. Finally, select the <b>Virtual
Locations/Scrap</b> location.</p>
</div>

By default, scrapping a product removes it from physical inventory, and places
it in a virtual location titled _Virtual Locations/Scrap_. A virtual location
is **not** a physical space, but rather a designation in Konvergo ERP that is used to
track items that are no longer in physical inventory.

<div class="admonition-learn-more alert">
<p class="alert-title">
En savoir plus</p><p>For more information about virtual locations, see the documentation about the different types of
<a href="warehouses_locations#inventory-management-difference-warehouse-location"><span class="std std-ref">locations</span></a>.</p>
</div>

## Scrap from stock

To scrap a product located in inventory, begin by navigating to Inventory ‣
Operations ‣ Scrap. On the **Scrap Orders** page, click **Create** to
configure a new scrap order.

On the scrap order, select the product being scrapped from the **Product**
drop-down menu, then enter the quantity in the **Quantity** field. The
**Source Location** defaults to the location where the product is stored, and
the **Scrap Location** defaults to **Virtual Locations/Scrap** , but either of
these can be changed by selecting a different location from their respective
drop-down menus.

![A new scrap order.](../../../../../_images/scrap-order.png)

Finally, click **Validate** to scrap the product. The on-hand inventory count
for the scrapped product updates to subtract the scrapped quantity.

## Scrap from a receipt, transfer, or delivery

It is also possible to scrap products during the receipt, transfer, and
delivery operations. This can be necessary if any products are found to be
defective when receiving them into inventory, transferring them from one
location to another, or preparing them for delivery.

To scrap a product during the receipt, transfer, or delivery operations, begin
by navigating to the Inventory app. On the **Overview** page, select the **#
TO PROCESS** button on the **Receipts** , **Internal Transfers** , or
**Delivery Orders** card, depending on the type of operation the product is
being scrapped from.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For the <b>Internal Transfers</b> card to appear on the Overview page of
the Inventory app, the <b>Storage Locations</b> setting must be enabled. To
do so, navigate to Configuration ‣ Settings, then enable the checkbox next to
<b>Storage Locations</b> under the <b>Warehouse</b> heading.</p>
</div>

Alternatively, a list of all delivery orders, receipts, and transfers can be
viewed by navigating to Inventory ‣ Operations ‣ Transfers.

Next, open a delivery order, receipt, or transfer from the corresponding page
by clicking on it. A **Scrap** button appears at the top of the page. Click it
to open the **Scrap** pop-up window.

![The scrap pop-up in the Inventory app.](../../../../../_images/scrap-pop-
up.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>Scrap</b> button will only appear on a receipt that has been validated. This is
because Konvergo ERP only allows products to be scrapped once they have been entered into inventory.</p>
</div>

On the **Scrap** pop-up window, select the product being scrapped from the
**Product** drop-down menu. Then, enter the quantity in the **Quantity**
field.

The **Source Location** defaults to the location where the product is stored,
and the **Scrap Location** defaults to **Virtual Locations/Scrap** , but
either of these can be changed by selecting a different location from their
respective drop-down menus.

Finally, click **Done** to scrap the product. After doing so, the **Scrap**
pop-up window disappears and a **Scraps** smart button appears in the top
right of the page. Click it to view all of the scrap orders created from that
operation.

![The Scraps smart button.](../../../../../_images/scraps-smart-button.png)

