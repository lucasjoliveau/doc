# Colis

A _package_ is a physical container holding one or more products. Packages can
also be used to store items in bulk.

Packages are commonly used for the following purposes:

  1. Grouping products to move them in bulk.

  2. Shipping to customers: configure package types to align with shipping carriers” size and weight requirements, streamlining the packing process, and ensuring compliance with carrier shipping specifications.

  3. Storing items in bulk.

_Package use_ is a field on the package form in Odoo that is only visible by
enabling the _Batch Transfers_ and _Packages_ features (Inventory app ‣
Configuration ‣ Settings).

By default, the _Package Use_ field on a packages form is set to _Disposable
Box_. Change this field to _Reusable Box_ **only** when configuring packages
for cluster pickings.

_Package type_ is an optional feature used for [calculating shipping
cost](../../shipping_receiving/setup_configuration/delivery_method.html),
based on real shipping weight. Create package types to include the weight of
the package itself (e.g. boxes, pallets, other shipping containers) in
shipping cost calculations.

Note

While packages are commonly used in the [three-step delivery
route](../../shipping_receiving/daily_operations/delivery_three_steps.html),
they can be used in any workflow involving storable products.

## Configuration

To use packages, first go to Inventory app ‣ Configuration ‣ Settings. Under
the Operations heading, activate the Packages feature. Then, click Save.

![Activate the *Packages* setting in Inventory > Configuration >
Settings.](../../../../../_images/enable-pack.png)

## Pack items

Products can be added to packages in any transfer by:

  1. Clicking each Detailed Operations icon on the product line.

  2. Using the Put in Pack button to place everything in the transfer into a package.

### Detailed operations

On any warehouse transfer (e.g. receipt, delivery order), add a product to a
package by clicking the ⦙≣ (bulleted list) icon in the Operations tab.

![Show "Detailed Operations" icon in the product
line.](../../../../../_images/detailed-operations1.png)

Doing so opens the Detailed Operations pop-up window for the Product.

To put the Product in a package, click Add a line, and assign the product to a
Destination Package. Select an existing package, or create a new one by typing
the name of the new package, then select Create….

![Assign a package to "Destination Package"
field.](../../../../../_images/destination-package.png)

Twelve units of `Acoustic Bloc Screen` are placed in `PACK0000001`.

Then, specify the quantity of items to go into the package in the Done column.
Repeat the above steps to place the Product in different packages. Once
finished, click Confirm to close the window.

Pour plus d'infos

[Ship one order in multiple
packages](../../shipping_receiving/advanced_operations_shipping/multipack.html)

### Put in pack

Alternatively, click the Put in Pack button on **any** warehouse transfer to
create a new package, and place all the items in the transfer in that newly-
created package.

Important

The Put in Pack button appears on receipts, delivery orders, and other
transfer forms with the _Packages_ feature enabled in Inventory app ‣
Configuration ‣ Settings.

![Image of the "Put in Pack" button being
clicked.](../../../../../_images/put-in-pack.png)

In batch transfer `BATCH/00003`, the Put in Pack button was clicked to create
a new package, `PACK0000002`, and assign all items to it in the Destination
Package field.

## Type de colis

Create package types by navigating to Inventory app ‣ Configuration ‣ Package
Types, in order to set custom dimensions and weight limits. This feature is
mainly used to calculate package weights for shipping costs.

Pour plus d'infos

  * [Shipping carriers](../../shipping_receiving/setup_configuration/third_party_shipper.html)

  * [Delivery methods](../../shipping_receiving/setup_configuration/delivery_method.html)

On the Package Types list, clicking New opens a blank package type form. The
fields of the form are as follows:

  * Package Type (required): define the package type’s name.

  * Size: define the dimensions of the package in millimeters (mm). The fields, from left to right, define the Length, Width, and Height.

  * Weight: weight of an empty package (e.g. an empty box, pallet).

Note

Odoo calculates the package’s weight by adding the weight of the empty package
plus the weight of the item(s), which can be found in the Weight field, in the
Inventory tab, of each product form.

  * Max Weight: maximum shipping weight allowed in the package.

  * Barcode: define a barcode to identify the package type from a scan.

  * Company: specify a company to make the package type available **only** at the selected company. Leave the field blank if it is available at all companies.

  * Carrier: specify the intended shipping carrier for this package type.

  * Carrier Code: define a code that is linked to the package type.

![Package type for FedEx's 25 kilogram box.](../../../../../_images/package-
type.png)

## Cluster packages

To use _cluster packages_ , first navigate to Inventory app ‣ Configuration ‣
Settings, and activate the Batch Transfers feature, located in the Operations
section. Doing so makes the _Package Use_ field become visible on a package
form.

![Activate the *Batch Transfers* feature in Inventory > Configuration >
Settings.](../../../../../_images/enable-batch.png)

Add new packages by going to Inventory app ‣ Products ‣ Packages. Then, click
New, or select an existing package. Doing so opens the package form, which
contains the following fields:

  * Package Reference (required): name of the package.

  * Package Type: used for configuring shipping boxes to ship to the customer.

Note

Package Type is unnecessary for configuring packages for cluster pickings.

  * Shipping Weight: used to input the weight of the package after measuring it on a scale.

  * Company: specify a company to make the package available **only** at the selected company. Leave the field blank if the package is available at all companies.

  * Location: current location of the package.

  * Pack Date: the date the package was created.

  * Package Use: choose Reusable for packages used for moving products within the warehouse; Disposable for packages used to ship products to customers.

![Display package form to create a cluster
pack.](../../../../../_images/package.png)

Pour plus d'infos

[Using cluster
packages](../../warehouses_storage/advanced_operations_warehouse/cluster_picking.html)

