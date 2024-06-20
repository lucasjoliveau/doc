# Packaging

In Odoo _Inventory_ , _packaging_ refers to disposable containers holding
multiple units of a specific product. Each specific packaging **must** be
defined on the individual product form.

For example, different packages for cans of soda, such as a 6-pack, a 12-pack,
or a case of 36, need to be configured on the individual product form. This is
because packagings are product specific — **not** generic.

## Configuration

To use packagings, navigate to Inventory app ‣ Configuration ‣ Settings. Then,
under the Products heading, enable the Product Packagings feature, and click
Save.

![Enable packagings by selecting "Product
Packagings".](../../../../../_images/enable-packagings.png)

## Create packaging

Packagings can be created directly on the product form, or from the Product
Packagings page.

### From product form

Create packagings on a product form by going to Inventory app ‣ Products ‣
Products, and select the desired product.

Under the Inventory tab, scroll down to the Packaging section, and click Add a
line. In the table, fill out the following fields:

  * Packaging (required): name of packaging that appears on sales/purchase orders as a packaging option for the product.

  * Contained quantity (required): amount of product in the packaging.

  * Unit of Measure (required): measurement unit for quantifying the product.

  * Sales: check this option for packagings intended for use on sales orders.

  * Purchase: check this option for packagings intended for use on purchase orders.

Note

Access additional fields in the Packaging table below by clicking the
(sliders) icon to the far-right of the column titles in the Packaging section,
and selecting the desired options from the drop-down menu that appears.

![Show the additional options menu's icon:
sliders.](../../../../../_images/slide.png)

  * Barcode: identifier for tracing packaging in stock moves or pickings, using the [Barcode app](../../../barcode/operations/receipts_deliveries.html#barcode-operations-intro). Leave blank if not in use.

  * Company: indicates the packaging is only available at the selected company. Leave blank to make the packaging available across all companies.

Example

To create a packaging type for six units of the product, `Grape Soda`, begin
by clicking Add a line. In the line, name the Packaging `6-pack`, and set the
Contained quantity to `6`. Repeat this process for additional packagings.

![Create 6-pack case for product.](../../../../../_images/create-product-
packaging.png)

### From product packagings page

To view all packagings that have been created, go to Inventory app ‣
Configuration ‣ Product Packagings. Doing so reveals the Product Packagings
page with a complete list of all packagings that have been created for all
products. Create new packagings by clicking New.

Example

Two soda products, `Grape Soda` and `Diet Coke`, have three types of
packagings configured. On the Product Packagings page, each product can be
sold as a `6-Pack` that contains 6 products, as a `12-Pack` of 12 products, or
as a `Case` of 32 products.

![List of different packagings for
products.](../../../../../_images/packagings.png)

## Apply packagings

When creating a sales order in the Sales app, specify the packagings that
should be used for the product. The chosen packaging is displayed on the SO
under the Packaging field.

Example

18 cans of the product, `Grape Soda`, is packed using three 6-pack packagings.

![Assign packagings on the Sales Order
Line.](../../../../../_images/packagings-sales-order.png)

Tip

Packaging can be used in conjunction with Odoo
[Barcode](../../../barcode/setup/software.html#inventory-barcode-software).
When receiving products from suppliers, scanning the packaging barcode
automatically adds the number of units in the packaging to the internal count
of the product.

  *[SO]: Sales Order

