# Unités de mesure

In some cases, handling products in different units of measure is necessary.
For example, a business can buy products from a country that uses the metric
system, and then sell those products in a country that uses the imperial
system. In that case, the business needs to convert the units.

Another case for unit conversion is when a business buys products in a big
pack from a supplier, and then sells those products in individual units.

Odoo can be set up to use different _units of measure (UoM)_ for one product.

## Configuration

To use different units of measure in Odoo, first go to Inventory app ‣
Configuration ‣ Settings, and under the Products section, activate the Units
of Measure setting. Then, click Save.

![Activer les unités de mesure dans les paramètres
d'Inventaire](../../../../../_images/uom-enable-setting.png)

## Catégories d’unités de mesure

After enabling the _Units of Measure_ setting, view the default units of
measure categories in Inventory app ‣ Configuration ‣ UoM Categories. The
category is important for unit conversion; Odoo can convert a product’s units
from one unit to another **only** if both units belong to the same category.

![Définir les catégories d'unités de
mesure](../../../../../_images/category.png)

Chaque catégorie d’unité de mesure a son unité de référence. L’unité de
référence est surlignée en bleu dans la colonne UdM de la page Catégories
d’unités de mesure. Odoo utilise l’unité de référence comme base pour toute
nouvelle unité.

To create a new unit, first select the correct category from the Units of
Measure Categories page. For example, to sell a product in a box of six units,
click the Unit category line. Then, on the category page that appears, click
Add a line in the Units of Measure tab. Then, in the Unit of Measure field,
title the new unit, such as `Box of 6`, then in the Type field, select the
appropriate size reference, such as Bigger than the reference Unit of Measure.

If applicable, enter a UNSPSC Category, which is a globally recognized [code
managed by GS1](https://www.unspsc.org/), that **must** be purchased in order
to use.

In the Ratio field, enter how many individual units are in the new UoM, such
as `6.00000` when using the example of the `6-Pack` (since a box of six is six
times _bigger_ than the reference unit, `1.00000`).

![Convertir des produits d'une unité à une autre tant qu'elles appartiennent à
la même catégorie.](../../../../../_images/convert-products-by-unit.png)

## Préciser les unités de mesure d’un produit

To set units of measure on a product, first go to Inventory app ‣ Products ‣
Products and select a product to open its product form page.

In the General Information tab, edit the Unit of Measure field to specify the
unit of measure that the product is sold in. The specified unit is also the
unit used to keep track of the product’s inventory and internal transfers.

Edit the Purchase UoM field to specify the unit of measure that the product is
purchased in.

## Conversion d’unités

Odoo automatically converts unit measurements when products have different
UoMs and purchase UoMs.

This occurs in various scenarios, including:

  1. Vendor orders: purchase UoM on purchase orders (POs) converts to UoM on internal warehouse documents

  2. Automatic replenishment: generates POs when the stock levels of a product (tracked in UoM) dips below a certain level. But, the POs are created using the purchase UoM

  3. Sell products: if a different UoM is used on the sales order (SO), the quantity is converted to the warehouse’s preferred UoM on the delivery order

### Buy products in the purchase UoM

When creating a new request for quotation (RFQ) in the _Purchase_ app, Odoo
automatically uses the product’s specified purchase unit of measure. If
needed, manually edit the UoM value on the RFQ.

After the RFQ is confirmed into a PO, click the Receipt smart button at the
top of the PO.

Odoo automatically converts the purchase unit of measure into the product’s
sales/inventory unit of measure, so the Demand column of the delivery receipt
shows the converted quantity.

Example

When the product’s purchase UoM is `Box of 6`, and its sales/inventory unit of
measure is `Units`, the PO shows the quantity in boxes of six, and the receipt
(and other internal warehouse documents) shows the quantity in units.

![Image of a purchase order that is using the purchase unit of
measure.](../../../../../_images/on-po.png)

An order of three quantities is placed using the purchase « UoM »: `Box of
6`.

![Image of receipt displaying the unit of measure.](../../../../../_images/on-
receipt.png)

Upon warehouse receipt, the recorded quantities are in the internal « Unit of
Measure »: `Units`.

### Réassort

A request for quotation for a product can also be generated directly from the
product form using the Replenish button.

After clicking Replenish, a replenish assistant box pops up. The purchase unit
of measure can be manually edited in the Quantity field, if needed. Then,
click Confirm to create the RFQ.

Important

A PO can **only** be automatically generated if at least **one** vendor is
listed in the product form’s Purchase tab.

![Click Replenish button to manually
replenish.](../../../../../_images/replenish.png)

Navigate to the created PO by clicking the Forecasted smart button on the
product form. Scroll down to the Forecasted Inventory section, and in the
Requests for quotation line, click the RFQ reference number to open the draft
RFQ. If necessary, the purchase UoM can be edited directly on the PO.

### Vendre dans une UdM différente

When creating a new quotation in the _Sales_ app, Odoo automatically uses the
product’s specified unit of measure. If needed, the UoM can be manually edited
on the quotation.

After the quotation is sent to the customer, and confirmed into a sales order
(SO), click the Delivery smart button at the top of the SO. Odoo automatically
converts the unit of measure into the product’s inventory unit of measure, so
the Demand column of the delivery shows the converted quantity.

For example, if the product’s UoM on the SO was changed to `Box of 6`, but its
inventory unit of measure is `Units`, the SO shows the quantity in boxes of
six, and the delivery shows the quantity in units.

  *[UoM]: Unit of Measure
  *[UoMs]: Units of Measure
  *[POs]: Purchase Orders
  *[RFQ]: Request for Quotation
  *[PO]: Purchase Order
  *[SO]: Sales Order

