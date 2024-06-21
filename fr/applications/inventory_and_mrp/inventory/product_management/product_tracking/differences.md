# Difference between lots and serial numbers

_Lots_ and _serial numbers_ are the two ways to identify and track products in
Konvergo ERP. While there are similarities between the two traceability methods, there
are also notable differences that affect receipts, deliveries, and inventory
reports.

A _lot_ usually indicates a specific batch of an item that was received, is
currently stored, or was shipped from a warehouse. However, it can also
pertain to a batch of products manufactured in-house, as well.

A _serial number_ is a unique identifier assigned incrementally (or
sequentially) to an item or product, used to distinguish it from other items
or products.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="lots">Lot numbers</a></p></li>
<li><p><a href="serial_numbers">Utiliser des numéros de série pour suivre des produits</a></p></li>
</ul>
</div>

## Activer les lots et les numéros de série

To track products using lots and serial numbers, the _Lots & Serial Numbers_
feature must be enabled.

To do that, go to the Inventory app ‣ Configuration ‣ Settings, scroll down to
the **Traceability** section, and click the box next to **Lots & Serial
Numbers**. Then, click the **Save** button to save changes.

![La fonctionnalité Lots et numéros de série activée dans les paramètres
d'inventaire.](../../../../../_images/differences-enabled-setting.png)

## When to use lots

Lots are useful for products that are manufactured or received in large
quantities, such as clothes or food. Lots and can be used to trace a product
back to a group, which is especially useful when managing product recalls or
expiration dates.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Created lot with quantity of products in it." class="align-center" src="../../../../../_images/differences-lot.png"/>
</div>

Manufacturers assign lot numbers to groups of products that have common
properties; this can lead to multiple goods sharing the same lot number. This
helps identify a number of products in a single group, and allows for end-to-
end traceability of these products through each step in their life cycles.

## When to use serial numbers

The goal of assigning serial numbers to individual products is to make sure
every item’s history is identifiable when it travels through the supply chain.
This can be especially useful for manufacturers that provide after-sales
services related to products they sell and deliver.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="List of serial numbers for product." class="align-center" src="../../../../../_images/differences-serial-numbers.png"/>
</div>

Serial numbers can contain many different types of characters: numbers,
letters, typographical symbols, or a mixture of all three types.

## Traçabilité

Manufacturers and companies can refer to traceability reports to see the
entire life cycle of a product. These reports include vital information, like
where it came from (and when), where it was stored, and to whom it was sent.

To see the full traceability of a product, or group products by lots and/or
serial numbers, go to Inventory app ‣ Products ‣ Lots/Serial Numbers. Doing so
reveals the **Lots/Serial Numbers** dashboard.

From here, products with lots or serial numbers assigned to them are listed by
default. They can also be expanded to show what lots or serial numbers have
been specifically assigned to them.

To group by lots or serial numbers, first remove any default filters from the
search bar in the upper-right corner. Then, click **Group By** , and select
**Add Custom Group** , which reveals a mini drop-down menu. From this mini
drop-down menu, select **Lot/Serial Number** , and click **Apply**.

Doing so reveals all existing lots and serial numbers, and each can be
expanded to show all product quantities with that assigned number. For unique
serial numbers that are _not_ reused, there should _only_ be one product per
serial number.

![Reporting page with drop-down lists of lots and serial
numbers.](../../../../../_images/differences-tracking.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>For additional information regarding an individual lot number or serial number, click the line
item for the lot or serial number to reveal that specific number’s <b>Lot</b> or
<b>Serial Number</b> form. From this form, click the <b>Location</b> and
<b>Traceability</b> smart buttons to see all stock on-hand using that serial number. Any
operations made using that lot or serial number can be found here, as well.</p>
</div>

