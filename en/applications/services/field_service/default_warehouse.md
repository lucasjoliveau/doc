# User default warehouse

Setting up a **default warehouse** can be useful for field technicians who
keep a supply in their van or those who always resupply from the same
warehouse. It also allows field workers to switch between warehouses from
their profiles.

Products in sales orders created during field interventions are always pulled
from the default warehouse, keeping the inventory accurate.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../inventory_and_mrp/inventory">Inventory</a></p>
</div>

## Configuration

To set up a user default warehouse, the [storage
locations](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations)
feature needs to be activated in the **Inventory** app. It is also necessary
to have more than one warehouse in your database.

You can either set it up for your profile, or for all users.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations">Manage Warehouses and Locations</a></p>
</div>

### For your profile

To set up a default warehouse for yourself, click your **profile icon** in the
upper right corner of the screen, then, go to My Profile ‣ Preferences ‣
Default Warehouse. Select the default warehouse from the drop-down menu.

### For all users

To set up a default warehouse for a specific user, go to Settings ‣ Users ‣
Manage users, select a user, then go to the **Preferences** tab. Scroll down
to **Inventory** , and select the default warehouse from the drop-down menu.

![Selection of a default warehouse on a user profile.](../../../_images/user-
default.png)

## Use in field service tasks

Once a default warehouse has been configured for a user, the materials used
for a sales order related to a Field Service task are pulled from that
specific warehouse. Open the related sales order, go to the **Other Info**
tab, then scroll down to **Delivery**. The default warehouse is applied
correctly.

Once the Field Service task is marked as done, the stock of the default
warehouse is automatically updated.

