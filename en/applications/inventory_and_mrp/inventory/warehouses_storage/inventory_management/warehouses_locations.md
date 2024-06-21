# Manage Warehouses and Locations

## Terminology

### Warehouse

In Konvergo ERP, a **Warehouse** is the actual building/place in which a company’s
items are stocked. Multiple warehouses can be set up in Konvergo ERP and the user can
create moves between warehouses.

### Location

A **Location** is a specific space within the warehouse. It can be a
sublocation of the warehouse (a shelf, a floor, an aisle, and so on).
Therefore, a location is part of one warehouse only and it is not possible to
link one location to multiple warehouses. In Konvergo ERP, as many locations can be
configured as needed under one warehouse.

There are three types of locations:

  * The **Physical Locations** are internal locations that are part of the warehouses that the company owns. They can be the loading and unloading areas of the warehouse, a shelf, a department, etc.

  * The **Partner Locations** are spaces within a customer and/or vendor’s warehouse. They work the same way as physical locations, with the only difference being that they are not owned by the user’s company.

  * The **Virtual Locations** are places that do not exist, but in which products can be placed when they are not physically in an inventory yet (or anymore). They come in handy when recording lost products (**Inventory Loss**), or accounting for products that are on their way to the warehouse (**Procurements**).

In Konvergo ERP, locations are structured hierarchically. Locations can be structured
as a tree, dependent on a parent-child relationship. This gives more detailed
levels of analysis of the stock operations and the organization of the
warehouses.

## Configuration

To activate locations, go to Configuration ‣ Settings and enable **Storage
Locations**. Then, click **Save**.

![Enable the storage location feature in Konvergo ERP Inventory
settings.](../../../../../_images/storage-location-warehouse-setting.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To manage several routes within the warehouses, also enable <b>Multi-Step Routes</b> and
check <a href="use_routes">Routes and push/pull rules</a>.</p>
</div>

## Create a new warehouse

To create a warehouse, go to Configuration ‣ Warehouse Management ‣ Warehouses
and click on **Create**.

Then, fill out a **Warehouse Name** and a **Short Name**. The short name is
five characters maximum.

![Short name field of a warehouse on Konvergo ERP
Inventory.](../../../../../_images/create-new-warehouse.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>Short Name</b> appears on transfer orders and other warehouse documents. Konvergo ERP
recommends using an understandable one like “WH/[first letters of location]”.</p>
</div>

Now, go back to the **Inventory** dashboard. There, new operations related to
the newly created warehouse have been automatically generated.

![Inventory app dashboard displaying new transfer types for the recently
created warehouse.](../../../../../_images/new-transfer-types.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Adding a second warehouse will automatically activate the <b>Locations</b> setting.</p>
</div>

## Create a new location

To create a location, go to Configuration ‣ Warehouse Management ‣ Locations
and click on **Create**.

Then, fill out a **Location Name** and a **Parent Location** and click
**Save**.

![Create a new warehouse location in Konvergo ERP
Inventory.](../../../../../_images/create-new-location.png)

