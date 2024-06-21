# Cycle counts

For most companies, warehouse stock only needs to be counted once a year. This
is why, by default, after making an _inventory adjustment_ in Konvergo ERP, the
scheduled date for the next inventory count is set for the 31st of December of
the current year.

However, for some businesses, it’s crucial to have an accurate inventory count
at all times. These companies use _cycle counts_ to keep critical stock levels
accurate. Cycle counting is a method by which companies count their inventory
more often in certain _locations_ , to ensure that their physical inventory
counts match their inventory records.

## Activate storage locations

In Konvergo ERP, cycle counts are location-based. Therefore, the _storage locations_
feature needs to be enabled before performing a cycle count.

To enable this feature, navigate to Inventory app ‣ Configuration ‣ Settings,
and scroll down to the **Warehouse** section. Then, click the checkbox next to
**Storage Locations**. Click **Save** to save all changes.

![Enabled storage locations setting in inventory
settings.](../../../../../_images/cycle-counts-enabled-setting.png)

## Change inventory count frequency by location

Now that the storage locations setting is enabled, the inventory count
frequency can be changed for specific locations created in the warehouse.

To view and edit locations, navigate to Inventory app ‣ Configuration ‣
Locations. This reveals a **Locations** page containing every location
currently created and listed in the warehouse.

From this page, click into a location to reveal the settings and configuration
page for that location. Click **Edit** to edit the location settings.

Under the **Cyclic Inventory** section, locate the **Inventory Frequency
(Days)** field, which should be set to `0` (if this location has not been
edited previously). In this field, change the value to whichever number of
days is desired.

![Location frequency setting on location.](../../../../../_images/cycle-
counts-location-frequency.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>A location that needs an inventory count every 30 days should have the <b>Inventory
Frequency (Days)</b> value set to <code>30</code>.</p>
</div>

Once the frequency has been changed to the desired number of days, click
**Save** to save changes. Now, once an inventory adjustment is applied to this
location, the next scheduled count date is automatically set, based on the
value entered into the **Inventory Frequency (Days)** field.

## Count inventory by location

To perform a cycle count for a specific location in the warehouse, navigate to
Inventory app ‣ Operations ‣ Inventory Adjustments. This reveals an
**Inventory Adjustments** page containing all products currently in stock,
with each product listed on its own line.

From this page, the **Filters** and **Group By** buttons (at the top of the
page, under the **Search…** bar), can be used to select specific locations and
perform inventory counts.

![Inventory adjustments page.](../../../../../_images/cycle-counts-inventory-
adjustments-page.png)

To select a specific location and view all products within that location,
click **Group By** , then click **Add Custom Group** to reveal a new drop-down
menu to the right.

Click **Location** from the drop-down menu, then click **Apply**. The page now
displays condensed drop-down menus of each location in the warehouse that has
products in stock, and a cycle count can be performed for all products in that
location.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>In large warehouses with multiple locations and a high volume of products, it might be easier to
search for the specific location desired. To do this, from the <b>Inventory Adjustments</b>
page, click <b>Filters</b>. Then, click <b>Add Custom Filter</b> to reveal a new menu
to the right. Click this menu to reveal three drop-downs.</p>
<p>For the first field, click and select <b>Location</b> from the drop-down. For the second
field, leave the <b>contains</b> value as is. For the third field, type in the name of the
location that is being searched for. Click <b>Apply</b> for that location to appear on the
page.</p>
</div> ![Applied filters and group by on inventory adjustments
page.](../../../../../_images/cycle-counts-filters.png)

## Change full inventory count frequency

While cycle counts are typically performed per location, the scheduled date
for full inventory counts of everything in-stock in the warehouse can also be
manually changed to push the date up sooner than the date listed.

To modify the default scheduled date, go to Inventory app ‣ Configuration ‣
Settings. Then, in the **Operations** section, locate the **Annual Inventory
Day and Month** setting field, which includes a drop-down that is set to `31`
**December** by default.

![Frequency field in inventory app settings.](../../../../../_images/cycle-
counts-frequency-settings.png)

To change the day, click the `31`, and change it to a day within the range
`1-31`, depending on the desired month of the year.

Then, to change the month, click **December** to reveal the drop-down menu,
and select the desired month.

Once all changes have been made, click **Save** to save all changes.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="count_products">Inventory adjustments</a></p>
</div>

