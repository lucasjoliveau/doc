# Packaging

In Konvergo ERP _Inventory_ , _packaging_ refers to disposable containers holding
multiple units of a specific product. Each specific packaging **must** be
defined on the individual product form.

For example, different packages for cans of soda, such as a 6-pack, a 12-pack,
or a case of 36, need to be configured on the individual product form. This is
because packagings are product specific — **not** generic.

## Configuration

To use packagings, navigate to Inventory app ‣ Configuration ‣ Settings. Then,
under the **Products** heading, enable the **Product Packagings** feature, and
click **Save**.

![Enable packagings by selecting "Product
Packagings".](../../../../../_images/enable-packagings.png)

## Create packaging

Packagings can be created directly on the product form, or from the **Product
Packagings** page.

### From product form

Create packagings on a product form by going to Inventory app ‣ Products ‣
Products, and select the desired product.

Under the **Inventory** tab, scroll down to the **Packaging** section, and
click **Add a line**. In the table, fill out the following fields:

  * **Packaging** (required): name of packaging that appears on sales/purchase orders as a packaging option for the product.

  * **Contained quantity** (required): amount of product in the packaging.

  * **Unit of Measure** (required): measurement unit for quantifying the product.

  * **Sales** : check this option for packagings intended for use on sales orders.

  * **Purchase** : check this option for packagings intended for use on purchase orders.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Access additional fields in the <b>Packaging</b> table below by clicking the
<b>(sliders)</b> icon to the far-right of the column titles in the <b>Packaging</b>
section, and selecting the desired options from the drop-down menu that appears.</p>
<img alt="Show the additional options menu's icon: sliders." class="align-center" src="../../../../../_images/slide.png"/>
</div>

  * **Barcode** : identifier for tracing packaging in stock moves or pickings, using the [Barcode app](../../../barcode/operations/receipts_deliveries#barcode-operations-intro). Leave blank if not in use.

  * **Company** : indicates the packaging is only available at the selected company. Leave blank to make the packaging available across all companies.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To create a packaging type for six units of the product, <code>Grape Soda</code>, begin by clicking
<b>Add a line</b>. In the line, name the <b>Packaging</b> <code>6-pack</code>, and set the
<b>Contained quantity</b> to <code>6</code>. Repeat this process for additional packagings.</p>
<img alt="Create 6-pack case for product." class="align-center" src="../../../../../_images/create-product-packaging.png"/>
</div>

### From product packagings page

To view all packagings that have been created, go to Inventory app ‣
Configuration ‣ Product Packagings. Doing so reveals the **Product
Packagings** page with a complete list of all packagings that have been
created for all products. Create new packagings by clicking **New**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Two soda products, <code>Grape Soda</code> and <code>Diet Coke</code>, have three types of packagings configured. On
the <b>Product Packagings</b> page, each product can be sold as a <code>6-Pack</code> that contains 6
products, as a <code>12-Pack</code> of 12 products, or as a <code>Case</code> of 32 products.</p>
<img alt="List of different packagings for products." class="align-center" src="../../../../../_images/packagings.png"/>
</div>

## Apply packagings

When creating a sales order in the Sales app, specify the packagings that
should be used for the product. The chosen packaging is displayed on the SO
under the **Packaging** field.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>18 cans of the product, <code>Grape Soda</code>, is packed using three 6-pack packagings.</p>
<img alt="Assign packagings on the Sales Order Line." class="align-center" src="../../../../../_images/packagings-sales-order.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Packaging can be used in conjunction with Konvergo ERP <a href="../../../barcode/setup/software#inventory-barcode-software"><span class="std std-ref">Barcode</span></a>. When
receiving products from suppliers, scanning the packaging barcode automatically adds the number
of units in the packaging to the internal count of the product.</p>
</div>

  *[SO]: Sales Order

