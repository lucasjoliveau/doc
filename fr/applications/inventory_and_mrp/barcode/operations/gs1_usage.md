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
Pour plus d'infos</p><ul>
<li><p><a href="https://www.gs1.org/standards/get-barcodes">Purchase GTINs</a></p></li>
<li><p><a href="gs1_nomenclature#barcode-operations-gs1"><span class="std std-ref">GS1 nomenclature</span></a></p></li>
</ul>
</div>

## Configure barcodes for product, quantity, and lots

To build a GS1 barcode that contains information about a product, its
quantities, and the lot number, the following barcode patterns and Application
Identifiers (A.I.) are used:

Nom | Nom de la règle | A.I. | Modèle de code-barres | Champ dans Konvergo ERP  
---|---|---|---|---  
Produit | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | Champ **Code-barres** sur un formulaire de produit  
Quantité | Nombre variable d’articles | 30 | (30)(\d{0,8}) | Champ **Unités** sur un formulaire de transfert  
Numéro de lot | Numéro de lot | 10 | (10)([! »%-/0-9:-?A-Z_a-z]{0,20}) | **Lot** sur la fenêtre contextuelle des Opérations détaillées  
  
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
<img alt="Saisissez le GTIN à 14 chiffres dans le champ Code-barres sur le formulaire du produit." class="align-center" src="../../../../_images/barcode-field.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>To view a list of <em>all</em> products and their corresponding barcodes in the Konvergo ERP database, navigate
to Inventory app ‣ Configuration ‣ Settings. Under the <b>Barcode</b>
heading, click on the <b>Configure Product Barcodes</b> button under the <b>Barcode
Scanner</b> section. Enter the 14-digit <abbr title="Global Trade Item Number">GTIN</abbr> into the <b>Barcode</b> column, then click
<b>Save</b>.</p>
<img alt="Vue de la page des codes-barres des produits dans les paramètres d'inventaire." class="align-center" src="../../../../_images/product-barcodes-page.png"/>
</div>

After activating tracking by lots and serial numbers from the settings page,
specify that this feature is to be applied on each product by navigating to
the **Inventory** tab on the product form. Under **Tracking** , choose the
**By Lots** radio button.

![Activez le suivi des produits par lots dans l'onglet "Inventaire" du
formulaire du produit.](../../../../_images/track-by-lots.png)

### Scanner le code-barres sur la réception

Pour garantir une interprétation précise des lots dans Konvergo ERP sur les codes-
barres des produits scannés lors d’une opération de réception, allez à
l’application Code-barres pour gérer le [processus de transfert des
réceptions](receipts_deliveries#barcode-operations-scan-received-
products).

From the **Barcode Scanning** dashboard, click the **Operations** button, then
the **Receipts** button to view the list of vendor receipts to process.
Receipts generated from POs are listed, but new receipt operations can also be
created directly through the Barcode app using the **Create** button.

Sur la liste des réceptions, cliquez sur l’opération d’entrepôt (`WH/IN`) et
scannez les codes-barres et les numéros de lot du produit à l’aide d’un
lecteur de codes-barres. Le produit scanné apparaît alors dans la liste.
Utilisez le bouton **✏️ (crayon)** pour ouvrir une fenêtre et saisir
manuellement les quantités pour des numéros de lot spécifiques.

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
<img alt="Scannez le code-barres d'un produit sur la page de transfert de réception dans l'application *Code-barres*." class="align-center" src="../../../../_images/receive-50-apples.png"/>
</div>

## Configure barcode for product and non-unit quantity

Pour créer un code-barres GS1 qui contient des produits mesurés dans une
quantité non unitaire, comme des kilogrammes, les modèles de code-barres
suivants sont utilisés :

Nom | Nom de la règle | A.I. | Modèle de code-barres | Champ dans Konvergo ERP  
---|---|---|---|---  
Produit | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | Champ **Code-barres** sur un formulaire de produit  
Quantité en kilogrammes | Nombre variable d’articles | 310[0-5] | (310[0-5])(\d{6}) | Champ **Unités** sur un formulaire de transfert  
  
### Scanner le code-barres sur la réception

Pour confirmer que les quantités sont correctement interprétées dans Konvergo ERP,
placez une commande dans l’application _Achats_ en utilisant l’unité de mesure
(**UdM**) appropriée pour la quantité de produits à acheter.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../inventory/product_management/product_replenishment/uom#inventory-product-replenishment-unit-conversion"><span class="std std-ref">Simplify vendor unit conversions with UoMs</span></a></p>
</div>

Une fois la commande placée, allez à l’application Code-barres pour [recevoir
l’envoi du fournisseur](receipts_deliveries#barcode-operations-scan-
received-products).

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
<img alt="Écran de scan du code-barres pour une opération de réception dans l'application Code-barres." class="align-center" src="../../../../_images/scan-barcode-peaches.png"/>
</div>

## Verify product moves

For additional verification, the quantities of received products are also
recorded on the **Product Moves** report, accessible by navigating to
Inventory app ‣ Reporting ‣ Product Moves.

Les articles sur le rapport des **Mouvements de stock** sont regroupés par
produit par défaut. Pour confirmer les quantités reçues, cliquez sur une ligne
de produit pour ouvrir son menu déroulant rétractable, qui affiche une liste
des _lignes de mouvement de stock_ pour le produit. Le dernier mouvement de
stock correspond au numéro de réception de l’entrepôt (par ex. `WH/IN/00013`)
et à la quantité traitée dans la lecture du code-barres, ce qui prouve que les
enregistrements traités dans l’application _Code-barres_ ont été correctement
stockés dans _Inventaire_.

![Enregistrement d'un mouvement de stock de réception pour 52,1 kg de
pêches.](../../../../_images/stock-moves-peach.png)

  *[POs]: Purchase Orders

