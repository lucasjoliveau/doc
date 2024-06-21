# GS1 barcode usage

GS1 barcodes provide a standardized format that barcode scanners can
interpret. They encode information in a [specific structure recognized
globally](gs1_nomenclature#barcode-operations-gs1), allowing scanners to
understand and process supply chain data consistently.

Konvergo ERP _Barcode_ interprets and prints GS1 barcodes, automating product
identification and tracking in warehouse operations such as receiving,
picking, and shipping.

The following sections contain examples of how Konvergo ERP uses GS1 barcodes provided
by the business to identify common warehouse items and automate certain
warehouse workflows.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP <b>does not</b> create GS1 barcodes. Businesses must purchase a unique Global Trade Item Number
(GTIN) from GS1. Then, they can combine their existing GS1 barcodes with product and supply chain
information (also provided by GS1) to create barcodes in Konvergo ERP.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.gs1.org/standards/get-barcodes">Purchase GTINs</a></p></li>
<li><p><a href="gs1_nomenclature#barcode-operations-gs1"><span class="std std-ref">GS1 nomenclature</span></a></p></li>
</ul>
</div>

## Configure barcodes for product, quantity, and lots

To build a GS1 barcode that contains information about a product, its
quantities, and the lot number, the following barcode patterns and Application
Identifiers (A.I.) are used:

Name | Rule Name | A.I. | Barcode Pattern | Field in Konvergo ERP  
---|---|---|---|---  
Product | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | **Barcode** field on product form  
Quantity | Variable count of items | 30 | (30)(\d{0,8}) | **Units** field on transfer form  
Lot Number | Batch or lot number | 10 | (10)([!”%-/0-9:-?A-Z_a-z]{0,20}) | **Lot** on Detailed Operations pop-up  
  
### Configuration

First, [enable product tracking using
lots](../../inventory/product_management/product_tracking/lots#inventory-
management-track-products-by-lots) by navigating to Inventory app ‣
Configuration ‣ Settings, and checking the box for **Lots & Serial Numbers**
under the **Traceability** heading.

Then, set up the product barcode by navigating to the intended product form in
Inventory app ‣ Products ‣ Products and selecting the product. On the product
form, click **Edit**. Then, in the **General Information** tab, fill in the
**Barcode** field with the unique 14-digit [Global Trade Item Number
(GTIN)](https://www.gs1.org/standards/get-barcodes), which is a universally
recognized identifying number that is provided by GS1.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>On the product form, omit the <abbr title="Application Identifier">A.I.</abbr> <code>01</code> for <abbr title="Global Trade Item Number">GTIN</abbr> product barcode pattern, as it is only used to
encode multiple barcodes into a single barcode that contains detailed information about the
package contents.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>To record the GS1 barcode for the product, <code>Fuji Apple</code>, enter the 14-digit <abbr title="Global Trade Item Number">GTIN</abbr>
<code>20611628936004</code> in the <b>Barcode</b> field on the product form.</p>
<img alt="Enter 14-digit GTIN into the Barcode field on product form." class="align-center" src="../../../../_images/barcode-field.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To view a list of <em>all</em> products and their corresponding barcodes in the Konvergo ERP database, navigate
to Inventory app ‣ Configuration ‣ Settings. Under the <b>Barcode</b>
heading, click on the <b>Configure Product Barcodes</b> button under the <b>Barcode
Scanner</b> section. Enter the 14-digit <abbr title="Global Trade Item Number">GTIN</abbr> into the <b>Barcode</b> column, then click
<b>Save</b>.</p>
<img alt="View the Product Barcodes page from inventory settings." class="align-center" src="../../../../_images/product-barcodes-page.png"/>
</div>

After activating tracking by lots and serial numbers from the settings page,
specify that this feature is to be applied on each product by navigating to
the **Inventory** tab on the product form. Under **Tracking** , choose the
**By Lots** radio button.

![Enable product tracking by lots in the "Inventory" tab of the product
form.](../../../../_images/track-by-lots.png)

### Scan barcode on receipt

To ensure accurate lot interpretation in Konvergo ERP on product barcodes scanned
during a receipt operation, navigate to the Barcode app to manage the [receipt
picking process](receipts_deliveries#barcode-operations-scan-received-
products).

From the **Barcode Scanning** dashboard, click the **Operations** button, then
the **Receipts** button to view the list of vendor receipts to process.
Receipts generated from POs are listed, but new receipt operations can also be
created directly through the Barcode app using the **Create** button.

On the list of receipts, click on the warehouse operation (`WH/IN`) and scan
product barcodes and lot numbers with a barcode scanner. The scanned product
then appears on the list. Use the **✏️ (pencil)** button to open a window and
manually enter quantities for specific lot numbers.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>After placing a <abbr title="Purchase Order">PO</abbr> for fifty apples, navigate to the associated receipt
in the <em>Barcode</em> app.</p>
<p>Scan the barcode containing the <abbr title="Global Trade Item Number">GTIN</abbr>, quantity, and lot number. For testing with a barcode
scanner, below is an example barcode for the fifty Fuji apples in Lot 2.</p>
<table class="colwidths-given table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head stub"><p>50 Fuji apples in Lot0002</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><th class="stub"><p>2D Matrix</p></th>
<td><img alt="2D matrix of GS1 barcode of 50 fuji apples with an assigned lot number." src="../../../../_images/fuji-apples-barcode.png"/>
</td>
</tr>
<tr class="row-odd"><th class="stub"><p><abbr title="Application Identifier">A.I.</abbr> (product)</p></th>
<td><p>01</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>GS1 Barcode (product)</p></th>
<td><p>20611628936004</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p><abbr title="Application Identifier">A.I.</abbr> (quantity)</p></th>
<td><p>30</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>GS1 Barcode (quantity)</p></th>
<td><p>00000050</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p><abbr title="Application Identifier">A.I.</abbr> (lot)</p></th>
<td><p>10</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>GS1 Barcode (lot #)</p></th>
<td><p>LOT0002</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Full GS1 barcode</p></th>
<td><p>0120611628936004 3000000050 10LOT0002</p></td>
</tr>
</tbody>
</table>
<p><a href="gs1_nomenclature#barcode-operations-troubleshooting"><span class="std std-ref">If the configuration is correct</span></a>, <code>50/50</code>
<b>Units</b> processed will be displayed and the <b>Validate</b> button turns green.
Click the <b>Validate</b> button to complete the reception.</p>
<img alt="Scan the barcode for a product on the reception picking page in the *Barcode* app." class="align-center" src="../../../../_images/receive-50-apples.png"/>
</div>

## Configure barcode for product and non-unit quantity

To build a GS1 barcode that contains products measured in a non-unit quantity,
like kilograms, for example, the following barcode patterns are used:

Name | Rule Name | A.I. | Barcode Pattern | Field in Konvergo ERP  
---|---|---|---|---  
Product | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | **Barcode** field on product form  
Quantity in kilograms | Variable count of items | 310[0-5] | (310[0-5])(\d{6}) | **Units** field on transfer form  
  
### Scan barcode on receipt

To confirm that quantities are correctly interpreted in Konvergo ERP, place an order
in the _Purchase_ app using the appropriate unit of measure (**UoM**) for the
quantity of products to be purchased.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../inventory/product_management/product_replenishment/uom#inventory-product-replenishment-unit-conversion"><span class="std std-ref">Simplify vendor unit conversions with UoMs</span></a></p>
</div>

After the order is placed, navigate to the Barcode app to [receive the vendor
shipment](receipts_deliveries#barcode-operations-scan-received-products).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>On the receipt in the <em>Barcode</em> app, receive an order for <code>52.1 kg</code> of peaches by scanning the
barcode containing the <abbr title="Global Trade Item Number">GTIN</abbr> and quantity of peaches in kilograms.</p>
<table class="colwidths-given table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head stub"><p>52.1 kg of Peaches</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><th class="stub"><p>2D Matrix</p></th>
<td><img alt="2D matrix of GS1 barcode of 52.1 kg of peaches." src="../../../../_images/peaches-barcode.png"/>
</td>
</tr>
<tr class="row-odd"><th class="stub"><p><abbr title="Application Identifier">A.I.</abbr> (product)</p></th>
<td><p>01</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>GS1 Barcode (product)</p></th>
<td><p>00614141000012</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p><abbr title="Application Identifier">A.I.</abbr> (kg, 1 decimal point)</p></th>
<td><p>3101</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>GS1 Barcode (quantity)</p></th>
<td><p>000521</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Full GS1 barcode</p></th>
<td><p>0100614141000012 3101000521</p></td>
</tr>
</tbody>
</table>
<p><a href="gs1_nomenclature#barcode-operations-troubleshooting"><span class="std std-ref">If the configuration is correct</span></a>, <code>52.1 / 52.1</code>
<b>kg</b> will be displayed and the <b>Validate</b> button turns green. Finally, press
<b>Validate</b> to complete the validation.</p>
<img alt="Scan barcode screen for a reception operation in the Barcode app." class="align-center" src="../../../../_images/scan-barcode-peaches.png"/>
</div>

## Verify product moves

For additional verification, the quantities of received products are also
recorded on the **Product Moves** report, accessible by navigating to
Inventory app ‣ Reporting ‣ Product Moves.

The items on the **Product Moves** report are grouped by product by default.
To confirm the received quantities, click on a product line to open its
collapsible drop-down menu, which displays a list of _stock move lines_ for
the product. The latest stock move matches the warehouse reception reference
number (e.g. `WH/IN/00013`) and quantity processed in the barcode scan,
demonstrating that the records processed in the _Barcode_ app were properly
stored in _Inventory_.

![Reception stock move record for 52.1 kg of
peaches.](../../../../_images/stock-moves-peach.png)

  *[POs]: Purchase Orders

