# Product management

Konvergo ERP allows you to create, import, and manage your products’ pages all within
the **Website** app.

## Add products to the catalog

To add a product to your catalog, you can either do it in:

  * From anywhere on your website, click \+ New ‣ Product. Enter the name of your product, and **Save** ;

  * Website ‣ eCommerce ‣ Products ‣ Create;

  * or by [importing data](../../../essentials/export_import_data#import-data) using XLSX or CSV files. To do so, go to Website ‣ eCommerce ‣ Products. Click on **Favorites** and [Import records](../../../essentials/export_import_data#import-data).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="catalog">Catalog</a></p></li>
<li><p><a href="../../../sales/sales/products_prices/products/import">Import products</a></p></li>
<li><p><a href="../../../sales/sales">Product-related documentation</a></p></li>
</ul>
</div>

### Publish

Upon creation, products are defaulted as **Unpublished** in your eCommerce
catalog. To make a product visible to visitors, go to Website ‣ Site ‣
Homepage, click on your **main shop** page, select the product, and enable it
as **Published** in the top-right corner.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To publish <b>large batches</b> of products, the most convenient fashion is to go to
Website ‣ eCommerce ‣ Products. Here, remove the <b>Published</b>
filter by clicking on the <b>x</b> right to it, and then select the <b>List</b> view.
Next, click the <b>dropdown toggle</b> button (located right below the <b>List</b>
button) and enable <b>Is published</b>. Click the <b>Is Published</b> column to
re-order it either by <b>published</b> or <b>unpublished</b> products. Finally, select the products to
publish by ticking their box on the extreme-right, and tick any box of the selected products in
the <b>Is Published</b> column to publish them all.</p>
</div> ![List and dropdown toggle
buttons](../../../../_images/products-buttons.png)

## Product page design

Once a product is created, you can access its **product page** through the
**Shop** page by clicking on the product, and then clicking **Edit**. Here,
you can change the page’s **additional functions** , **layout** , **add
content** , etc. Note that **enabled functions** apply to _all_ product pages.

### Additional functions

In the **website builder** window, click **Customize** to enable additional
functions:

  * **Customers: Rating** allows customers to submit [product reviews](../ecommerce_management/customer_interaction#product-reviews); **Share** adds social media and email icon buttons to share the product via those channels;

  * **Select Quantity** : if enabled, allows to choose the quantity added to cart;

  * **Tax Indication** : notifies if the price is **VAT included** or **excluded** ;

  * **Variants** : shows all possible [variants](../../../sales/sales/products_prices/products/variants) of the product as a **Products List** ; **Options** as selectable options to compose the variant yourself;

  * **Cart** : **Buy Now** adds a [checkout button](../checkout_payment_shipping/cart#cart-buy-now) taking the customer directly to the checkout page; **Wishlist** allows to add the product to a wishlist;

  * **Specification** : allows you to select where the **Specifications** section is displayed. This option displays a list of all variant attributes and values of a product, but only works for products _with_ variants.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>To allow <b>wishlists</b>, the option must be enabled in Website ‣ Configuration
‣ Settings ‣ Shop - Products;</p></li>
<li><p>To access the <b>Variants</b> options, the <a href="../../../sales/sales/products_prices/products/variants">Product Variants</a> option must first be enabled under
Website ‣ Configuration ‣ Settings ‣ Shop - Products.</p></li>
</ul>
</div>

### Layout

Within the same **Customize** tab as the functions, the layout configuration
can be changed according to your needs.

  * **Images Width** : changes the width of the product images displayed on the page;

  * **Layout** : the **Carousel** layout displays a large, main image with smaller ones underneath; whereas the **Grid** displays four images in a square layout (see pictures below);

  * **Image Zoom** : choose which image zooms are available, either **Pop-up on Click** , when hovering over the image (**Magnifier on hover**), on **Both** , or **None** ;

  * **Thumbnails** : decide how the thumbnails should be aligned, either **vertically** (**Left**), or **horizontally** (**Right**);

  * **Main Image** : click **Replace** to change the product’s main image;

  * **Extra Images** : click **Add** or **Remove all** to add or remove extra product images. You can also add images and videos via **URL**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Images must either be in PNG or JPG format. To trigger the zoom, the image has to be bigger than
1024x1024.</p>
</div> ![Product images layout](../../../../_images/products-
layout.png)

### Add content

You can use **building blocks** (Edit ‣ Blocks) to add content to your product
page. These blocks can be used to add extra text and picture galleries,
features such as **Call to Actions** , **Comparisons** , etc.

Depending on _where_ you drop the **building block** , it may be available
either on the product page _only_ , or on the _whole_ website. **Building
blocks** dropped at the very top or very bottom of the page are available on
the _whole_ website, where **building blocks** put underneath the product
description are only displayed on the _product_ page _(see image below)_.

![Building blocks on product page](../../../../_images/products-blocks.png)

### Download link

To add a downloadable file (ex.: user’s manual, notice of use, etc.) on the
product page, drag and drop a **Text** block from Edit ‣ Blocks on the page.
Once placed, click within the **Text** block, and under the **Inline Text**
section, select either Insert Media ‣ Documents or **Insert or edit link** and
enter the URL in the **Your URL** field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The difference with <a href="#ecommerce-digital-file"><span class="std std-ref">digital files</span></a> is that digital files can only
be downloaded <em>after</em> checkout.</p>
</div> ![Media and link buttons](../../../../_images/products-
media.png)

### Digital files

Should your product be sold with a certificate, manual user, or any other
relevant document, it is possible to add a download link for customers at the
end of the checkout. To do that, first enable **Digital Content** under
Website ‣ Configuration ‣ Settings ‣ Shop - Checkout Process. Then, on the
**product’s template** , click on More ‣ Digital Files and **Create** a new
file.

![Digital Files menu](../../../../_images/products-digital-files.png)

For the configuration:

  * **Name** : the name of your file;

  * **Type:** select if it is either a **file** or a **URL**. Accordingly, you either have a **File Content (base64)** field to upload your file, or a **URL** field to enter your URL.

  * **Website** : the website on which that file is _available_. If you want it available for _all_ websites, leave it empty.

The file is then available after checkout in the **purchase order** section
found on the customer’s portal.

## Product configuration

### Multiple languages

If multiple languages are available on your website and you wish to have the
product’s information translated, it is necessary to encode this translated
information in the **product’s template**. Fields with multiple languages
available are identifiable by their abbreviation language (ex. EN) next to
their field.

![Field translation](../../../../_images/products-field-translation.png)

The **eCommerce-related** fields to translate are:

  * **Product name** ;

  * **Out-of-Stock Message** (under the **Sales** tab);

  * **Sales Description** (under the **Sales** tab);

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Having untranslated content on a web page may be detrimental to the user experience and
<a href="../../website/pages/seo">SEO</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To check the language(s) of your website, go to Website ‣ Configuration ‣
Settings ‣ Website Info section.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../website/pages/seo">Search Engine Optimization (SEO)</a></p></li>
</ul>
</div>

### Website availability

A product can be set available on either _one_ or _all_ websites, but it is
not possible to select _some_ websites and not others. To define a product’s
availability, go to Website ‣ eCommerce ‣ Products, select your product, and
in the **Sales** tab, click the **Website** you wish the product to be
available on. Leave the field empty for the products to be available on _all_
websites.

## Stock management

Under the Website ‣ Configuration ‣ Settings ‣ Shop - Products, you can enable
and configure inventory management options.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To display the stock level on the product page, the <b>Product Type</b> on the <b>product’s
form</b> must be set to <b>Storable</b> (only available when the <b>Inventory</b> app is
installed).</p>
</div>

### Inventory

In the **Inventory Defaults** sub-section, you can select the eCommerce
selling strategy of products:

  * **Warehouse** : if you have multiple warehouses, you can define the warehouse associated to your website. If you have multiple websites, you can select a different one per website;

  * **Out-of-Stock (Continue Selling)** : enabling it allows customers to continue placing orders even when the product is **out-of-stock**. Leave it unchecked to **prevent orders** ;

  * **Show Available Qty** : enabling it displays the available quantity left under a specified threshold on the product page. The available quantity is calculated based on the ‘On hand’ quantity minus the quantity already reserved for outgoing transfers.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../checkout_payment_shipping/cart#cart-prevent-sale"><span class="std std-ref">Allow only selected customers to buy</span></a></p>
</div>

### Selling as kit

If you are selling non-prepackaged kits (i.e., the kits are made of individual
products), we recommend you read the related documentation to keep track of
your stock.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To publish <b>large batches</b> of products, the most convenient fashion is to go to
Website ‣ eCommerce ‣ Products. Here, remove the <b>Published</b>
filter by clicking on the <b>x</b> right to it, and then select the <b>List</b> view.
Next, click the <b>dropdown toggle</b> button (located right below the <b>List</b>
button) and enable <b>Is published</b>. Click the <b>Is Published</b> column to
re-order it either by <b>published</b> or <b>unpublished</b> products. Finally, select the products to
publish by ticking their box on the extreme-right, and tick any box of the selected products in
the <b>Is Published</b> column to publish them all.</p>
</div>0

## Product comparison

You can enable a **product comparison tool** for your eCommerce by going to
Website ‣ Configuration ‣ Settings ‣ Shop - Products, and ticking **Product
Comparison Tool**. This tool allows to save products’ **specifications** and
compare them against each other on a single page.

On the product page, scroll down to the **Specifications** section and click
**Compare**. Repeat the same process for all products you wish to compare.
Then, click the **Compare** button of the pop-up window at the bottom of the
page to reach the comparison summary.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To publish <b>large batches</b> of products, the most convenient fashion is to go to
Website ‣ eCommerce ‣ Products. Here, remove the <b>Published</b>
filter by clicking on the <b>x</b> right to it, and then select the <b>List</b> view.
Next, click the <b>dropdown toggle</b> button (located right below the <b>List</b>
button) and enable <b>Is published</b>. Click the <b>Is Published</b> column to
re-order it either by <b>published</b> or <b>unpublished</b> products. Finally, select the products to
publish by ticking their box on the extreme-right, and tick any box of the selected products in
the <b>Is Published</b> column to publish them all.</p>
</div>1 ![Product comparison
window](../../../../_images/products-compare.png)

  *[EN]: English

