# Organize a cross-dock in a warehouse

Cross-docking is the process of sending products that are received directly to
the customers, without making them enter the stock. The trucks are simply
unloaded in a _Cross-Dock_ area in order to reorganize products and load
another truck.

![../../../../../_images/cross1.png](../../../../../_images/cross1.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For more information on how to organize your warehouse, read our blog: <a href="https://www.odoo.com/blog/business-hacks-1/post/what-is-cross-docking-and-is-it-for-me-270">What is cross-docking and
is it for me?</a></p>
</div>

## Configuration

In the _Inventory_ app, open Configuration ‣ Settings and activate the _Multi-
Step Routes_.

![../../../../../_images/cross2.png](../../../../../_images/cross2.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Doing so will also enable the <em>Storage Locations</em> feature.</p>
</div>

Now, both _Incoming_ and _Outgoing_ shipments should be configured to work
with 2 steps. To adapt the configuration, go to Inventory ‣ Configuration ‣
Warehouses and edit your warehouse.

![../../../../../_images/cross3.png](../../../../../_images/cross3.png)

This modification will lead to the creation of a _Cross-Docking_ route that
can be found in Inventory ‣ Configuration ‣ Routes.

![../../../../../_images/cross4.png](../../../../../_images/cross4.png)

## Configure products with Cross-Dock Route

Create the product that uses the _Cross-Dock Route_ and then, in the inventory
tab, select the routes _Buy_ and _Cross-Dock_. Now, in the purchase tab,
specify the vendor to who you buy the product and set a price for it.

![../../../../../_images/cross5.png](../../../../../_images/cross5.png)
![../../../../../_images/cross6.png](../../../../../_images/cross6.png)

Once done, create a sale order for the product and confirm it. Konvergo ERP will
automatically create two transfers which will be linked to the sale order. The
first one is the transfer from the _Input Location_ to the _Output Location_ ,
corresponding to the move of the product in the _Cross-Dock_ area. The second
one is the delivery order from the _Output Location_ to your _Customer
Location. Both are in state *Waiting Another Operation_ because we still need
to order the product to our supplier.

![../../../../../_images/cross7.png](../../../../../_images/cross7.png)
![../../../../../_images/cross8.png](../../../../../_images/cross8.png)

Now, go to the _Purchase_ app. There, you will find the purchase order that
has been automatically triggered by the system. Validate it and receive the
products in the _Input Location_.

![../../../../../_images/cross9.png](../../../../../_images/cross9.png)
![../../../../../_images/cross10.png](../../../../../_images/cross10.png)

When the products have been received from the supplier, you can go back to
your initial sale order and validate the internal transfer from _Input_ to
_Output_.

![../../../../../_images/cross11.png](../../../../../_images/cross11.png)
![../../../../../_images/cross12.png](../../../../../_images/cross12.png)

The delivery order is now ready to be processed and can be validated too.

![../../../../../_images/cross13.png](../../../../../_images/cross13.png)
![../../../../../_images/cross14.png](../../../../../_images/cross14.png)

