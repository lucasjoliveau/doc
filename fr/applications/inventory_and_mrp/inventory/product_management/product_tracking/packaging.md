# Conditionnement

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

  * Société : indique que le conditionnement n’est disponible que dans la société sélectionnée. Laissez vide pour rendre le conditionnement disponible dans toutes les sociétés.

Example

To create a packaging type for six units of the product, `Grape Soda`, begin
by clicking Add a line. In the line, name the Packaging `6-pack`, and set the
Contained quantity to `6`. Repeat this process for additional packagings.

![Créez un conditionnement Pack de 6 pour le
produit.](../../../../../_images/create-product-packaging.png)

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

![Liste de différents conditionnements pour les
produits.](../../../../../_images/packagings.png)

## Appliquer les conditionnements

When creating a sales order in the Sales app, specify the packagings that
should be used for the product. The chosen packaging is displayed on the SO
under the Packaging field.

Example

Les 18 canettes du produit `Grape Soda` sont emballées dans 3 packs de 6.

![Assignez des conditionnements sur la ligne de
commande.](../../../../../_images/packagings-sales-order.png)

Astuce

Le conditionnement peut être utilisé avec l’application [Code-
barres](../../../barcode/setup/software.html#inventory-barcode-software)
d’Odoo. Lorsque vous recevez des produits de vos fournisseurs, en scannant le
code-barres du conditionnement, vous ajoutez automatiquement le nombre
d’unités contenues dans le conditionnement à l’inventaire interne du produit.

  *[SO]: Sales Order

