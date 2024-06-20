# Locations

A _location_ is a specific space within a warehouse. This can be a shelf,
room, aisle, etc. There are three types of locations in Odoo:

  * _Physical locations_ are spaces within a warehouse owned by the user’s company. These can be a an area where items are stored like an aisle or shelf, or an area where operations take place, like loading and unloading bays.

  * _Partner locations_ are the same as physical locations except that they exist within the warehouse of a customer or vendor.

  * _Virtual locations_ are locations that do not exist physically, but where items that are not in inventory can be placed. These can be items that have not yet entered inventory, like products that are on the way to a warehouse, or items that are no longer in inventory due to loss or other factors.

Important

In order to use locations, the Storage Locations setting must be enabled. To
do so, navigate to Inventory ‣ Configuration ‣ Settings, scroll down to the
Warehouse heading, and enable the Storage Locations checkbox.

## Create a new location inside a warehouse

Starting from the Inventory app, select Configuration ‣ Locations ‣ Create.
The new location form can then be configured as follows:

  * Location Name: the name that will be used to reference the location

  * Parent Location: the location or warehouse that the new location exists within

  * Location Type: choose the category that the location belongs to

  * Company: the company that owns the warehouse that the location is inside of

  * Is a Scrap Location?: check this box to allow for scrapped/damaged goods to be stored in this location

  * Is a Return Location?: check this box to allow products to be returned to this location

  * Barcode: the barcode number assigned to the location

  * Removal Strategy: the [strategy](../advanced_operations_warehouse/removal.html#inventory-routes-strategies-removal) for how items should be taken from inventory

![The form for creating a new location.](../../../../../_images/new-location-
form.png)

## Create location hierarchies

The _Parent Location_ setting on the new location form allows for a location
to exist within a warehouse or another location. Every location can serve as a
parent location, and every parent location can have multiple locations within
it, allowing for the creation of a virtually infinite hierarchical structure.

Example

Location hierarchy could be organized so that a shelf is located within an
aisle, which is located within a room, which is located within the overall
warehouse.

To create the location hierarchy in the example above, set the warehouse as
the parent of the room, the room as the parent of the aisle, and the aisle as
the parent of the shelf. This can be adapted to a hierarchy of any magnitude.

