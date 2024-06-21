# Lot numbers

_Lots_ are one of the two ways to identify and track products in Konvergo ERP. They
typically represent a specific batch of products that were received, stored,
shipped, or manufactured in-house.

Manufacturers assign lot numbers to groups of products sharing common
properties, facilitating end-to-end traceability through their lifecycles.

Lots are useful for managing large quantities of manufactured or received
products, aiding in tracing items back to their group, particularly for
product recalls or [expiration dates](expiration_dates).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="serial_numbers">Utiliser des numéros de série pour suivre des produits</a></p>
</div>

## Configuration

To track products by lots, enable the _Lots & Serial Numbers_ feature. Then,
configure each product to be tracked by serial numbers on the product form.

### Activer les lots et les numéros de série

To track products using lots, enable the _Lots & Serial Numbers_ feature. Go
to the Inventory app ‣ Configuration ‣ Settings, scroll down to the
**Traceability** section, and tick the checkbox next to **Lots & Serial
Numbers**. Then, click **Save**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div> ![La fonctionnalité Lots et numéros de série activée dans
les paramètres d'inventaire.](../../../../../_images/enabled-lots-setting.png)

### Track by lots

Once the **Lots & Serial Numbers** feature is activated, configure individual
products to be tracked using lots. To do this, go to Inventory app ‣ Products
‣ Products, and choose a product to configure.

On the product form, go to the **Inventory** tab. In the **Traceability**
section, select the **By Lots** option in the **Tracking** field. Now, new or
existing lot numbers can be assigned to newly-received or manufactured batches
of this product.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If a product has stock on-hand prior to activating tracking by lots or serial numbers, use an
<a href="../../warehouses_storage/inventory_management/count_products">inventory adjustment</a> to
assign lot numbers to existing products in stock.</p>
</div> ![La fonctionnalité de Suivi par lots activée sur la fiche
du produit.](../../../../../_images/tracking-product-form.png)

## Assign lots for shipping and receiving

Assign new lot numbers to incoming goods on the receipt form. When shipping
outgoing goods, select products with specific lot numbers on the delivery
order form.

### On receipts

Assigning new or existing lot numbers to incoming goods can be done directly
on receipts.

To begin, go to the Purchase app to [create and
confirm](https://www.youtube.com/watch?v=o_uI718P1Dc) a PO for products
tracked by lot numbers. Then, click the **Receipt** smart button that appears
at the top of the page to navigate to the warehouse receipt form.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Alternatively, navigate to an existing receipt by going to the Inventory app,
clicking the <b>Receipts</b> Kanban card, and choosing the desired receipt.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Clicking <b>Validate</b> before assigning a lot number triggers a <b>User Error</b>,
indicating that a lot number <b>must</b> be assigned before validating the receipt.</p>
<img alt="Fenêtre contextuelle d'erreur d'utilisateur lors de l'ajout d'un lot/numéro de série." class="align-center" src="../../../../../_images/user-error.png"/>
</div>

On the receipt form, on the product line in the **Operations** tab, select the
**⦙≣ (bulleted list)** icon to the right of the product that is tracked by lot
numbers.

![Show the bulleted list icon on the product
line.](../../../../../_images/bulleted-list-icon.png)

The bulleted list icon on the product line.

Doing so opens the **Detailed Operations** pop-up window, where the
**Lot/Serial Number** and **Done** quantity are assigned.

The two ways to assign lot numbers are **manually** and **copy/paste**.

#### Manual assignment

To manually assign lot numbers, click **Add a line** , and choose the location
the products will be stored in under the **To** column. Then, type a new
**Lot/Serial Number** , and specify the **Done** quantity.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To assign multiple lot numbers, or store to multiple locations, click <b>Add a line</b>, and
type a new <b>Lot/Serial Number</b> for additional quantities. Repeat until the total in the
<b>Done</b> column matches the <b>Quantity Done</b> at the top.</p>
</div> ![Fenêtre contextuelle des opérations détaillées
d'assignation d'un numéro de lot.](../../../../../_images/assign-lot-number-
popup.png)

#### Copy and paste

From a spreadsheet with all of the lot numbers received from the supplier (or
manually chosen to assign upon receipt), click **Add a line** , and proceed to
copy and paste the lot numbers, in the **Lot/Serial Number** column.

![Liste des numéros de lot copiés dans la feuille de calcul
Excel.](../../../../../_images/lots-excel-spreadsheet.png)

![Lot numbers copied to the lot number line.](../../../../../_images/bulk-
sn.png)

Lot numbers copied to the lot number line, with each lot number on its own
line.

After clicking away from the text field, Konvergo ERP automatically generates the
necessary lot number lines. The quantities in the **Done** column match the
first entry. Manually adjust the **To** locations and **Done** quantities for
each lot number, as needed.

Once all product quantities have been assigned a lot number, click **Confirm**
to close the pop-up window. Then, click **Validate** on the receipt form.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="#inventory-product-management-lot-traceability"><span class="std std-ref">Traceability report for lot numbers</span></a></p>
</div>

### On delivery orders

Konvergo ERP makes it possible to specify which lot numbers for a product are chosen
for outgoing shipment on a delivery order form.

To begin, create or select an existing quotation from the Sales app. After
confirming the SO, the **Delivery** smart button becomes available. Click the
**Delivery** smart button to view the warehouse receipt form for that specific
SO.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Alternatively, navigate to delivery orders by going to the Inventory app, and
clicking the <b>Delivery Orders</b> Kanban card.</p>
</div>

Clicking the **Delivery** smart button opens the the delivery order form,
where lot numbers are picked for delivery. In the **Operations** tab, click
the **⦙≣ (bulleted list)** icon to the right of the product that is tracked by
lot numbers. Clicking that icon reveals a **Detailed Operations** pop-up
window.

In the **Detailed Operations** pop-up window, a **Lot/Serial Number** is
chosen, with the full **Reserved** quantity taken from that specific lot (if
there is enough stock in that particular lot).

Si le stock de ce lot est insuffisant ou si des quantités partielles de la
**Demande** doivent être prélevées sur plusieurs lots, changez la quantité
dans la colonne **Fait** pour uniquement inclure cette partie spécifique de la
quantité totale.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The lot automatically chosen for delivery orders varies, depending on the selected removal
strategy (<abbr title="First In, First Out">FIFO</abbr>, <abbr title="Last In, First Out">LIFO</abbr>, or <abbr title="First Expiry, First Out">FEFO</abbr>). It also depends on the ordered quantity, and whether the lot’s
on-hand quantity is enough to fulfill the order.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../warehouses_storage/advanced_operations_warehouse/removal">Removal strategies (FIFO, LIFO, FEFO)</a></p>
</div>

Next, click **Add a line** , select a different **Lot/Serial Number** , apply
the remaining **Done** quantities, and click **Confirm** to close the pop-up
window. Lastly, click the **Validate** button to deliver the products.

![Fenêtre contextuelle des opérations détaillées pour le numéro de lot source
sur la commande client.](../../../../../_images/detailed-operations.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>0

## Lot management

Manage and view existing lot numbers for products in the **Lot/Serial
Numbers** dashboard by going to Inventory app ‣ Products ‣ Lots/Serial
Numbers.

By default, lot numbers are grouped by product, and selecting the drop-down
menu for each product displays the existing lot numbers. Select a lot number
to modify or add details linked to the lot. Lot numbers can also be created
from this page, by clicking the **New** button.

![Show the "Lot/Serial Number" dashboard.](../../../../../_images/lot-
dashboard.png)

Display lot numbers, grouped by products, on the **Lot/Serial Number**
dashboard.

### Modify lot

Clicking a lot from the **Lot/Serial Number** dashboard reveals a separate
page where additional information can be provided about the lot.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>1

On the lot number form, the following fields can be modified:

  * **Lot/Serial Number** : Change the lot number linked to the **Product**

  * **Internal Reference** : Records an alternative lot/serial number used within the warehouse that differs from the one used by the supplier manufacturer.

  * **Company** : Specify the company where the lot number is available.

  * **Description** : Add extra details about the lot or serial number in this text field.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>2 ![Show the lot number form.](../../../../../_images/lot-
number.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>3

### Reserve lot number for a product

To create a lot number for a product, begin by going to Inventory app ‣
Products ‣ Lot/Serial Numbers, and click **New**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>4 <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>5

Une fois que le nouveau **Lot/Numéro de série** est généré, cliquez sur le
champ vierge à côté de **Produit** pour révéler un menu déroulant. Dans ce
menu, sélectionnez le produit auquel ce nouveau numéro sera assigné.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>6

After a new lot number has been created, saved, and assigned to the desired
product, the lot number is saved as an existing lot number linked to the
product, and can be selected when assigning lot numbers to products on a
receipt, or when making an inventory adjustment.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>7

## Gérer des lots pour différents types d’opérations

By default, new lots can only be created when receiving products, and existing
lot numbers cannot be used. For sales orders, only existing lot numbers can be
utilized, and new ones cannot be created on the delivery order.

To change the ability to use new (or existing) lot numbers on any operation
type, go to the Inventory app ‣ Configuration ‣ Operations Types, and select
the desired operation type.

On the operation type form, under the **Lots/Serial Numbers** section, tick
the **Create New** checkbox to enable new lot numbers to be created during
this operation type. Choose **Use Existing ones** if only existing lot numbers
can be selected.

![Le paramètre de traçabilité activé sur le formulaire des types
d'opérations.](../../../../../_images/operations-type-form.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>8

## Traçabilité

Manufacturers and companies can refer to traceability reports to see the
entire lifecycle of a product: where it came from, when it arrived, where it
was stored, who it went to (and when).

Pour voir la traçabilité complète d’un produit, ou regrouper des produits par
lots, allez à l’application Inventaire ‣ Produits ‣ Lots/Numéros de série.
Cette opération affiche le tableau de bord des Lots/Numéros de série.

À partir de là, les produits auxquels des numéros de lot ont été assignés sont
répertoriés par défaut, et il est possible de les développer pour afficher les
numéros de lot assignés à ces produits.

To group by lots, begin by removing any filters in the **Search…** bar. Then,
click the **Group By** drop-down menu, select **Add Custom Group** , and
select **Lot/Serial Number** from the drop-down menu. Then, click **Apply**.

Cette opération permet d’afficher tous les lots et numéros de série existants
et il est possible de les développer pour afficher toutes les quantités de
produits portant le numéro assigné.

![Rapport de traçabilité des lots et numéros de
série.](../../../../../_images/group-by-number.png)

### Traceability report

To view a full stock moves report for a lot number, select the lot number line
from the **Lots/Serial Number** dashboard. On the lot number form, click the
**Traceability** smart button.

![Show the Traceability Report for a lot, that displays the stock
moves.](../../../../../_images/traceability-report.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="expiration_dates">Tracking expiration dates</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Print GS1 barcodes for lots and serial numbers</span></a></p></li>
</ul>
</div>9

  *[PO]: Purchase Order
  *[SO]: Sales Order

