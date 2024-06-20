# GS1 barcode usage

GS1 barcodes provide a standardized format that barcode scanners can
interpret. They encode information in a [specific structure recognized
globally](gs1_nomenclature.html#barcode-operations-gs1), allowing scanners to
understand and process supply chain data consistently.

Odoo _Barcode_ interprets and prints GS1 barcodes, automating product
identification and tracking in warehouse operations such as receiving,
picking, and shipping.

The following sections contain examples of how Odoo uses GS1 barcodes provided
by the business to identify common warehouse items and automate certain
warehouse workflows.

Important

Odoo **does not** create GS1 barcodes. Businesses must purchase a unique
Global Trade Item Number (GTIN) from GS1. Then, they can combine their
existing GS1 barcodes with product and supply chain information (also provided
by GS1) to create barcodes in Odoo.

Pour plus d'infos

  * [Purchase GTINs](https://www.gs1.org/standards/get-barcodes)

  * [GS1 nomenclature](gs1_nomenclature.html#barcode-operations-gs1)

## Configure barcodes for product, quantity, and lots

To build a GS1 barcode that contains information about a product, its
quantities, and the lot number, the following barcode patterns and Application
Identifiers (A.I.) are used:

Nom | Nom de la règle | A.I. | Modèle de code-barres | Champ dans Odoo  
---|---|---|---|---  
Produit | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | Champ Code-barres sur un formulaire de produit  
Quantité | Nombre variable d’articles | 30 | (30)(\d{0,8}) | Champ Unités sur un formulaire de transfert  
Numéro de lot | Numéro de lot | 10 | (10)([! »%-/0-9:-?A-Z_a-z]{0,20}) | Lot sur la fenêtre contextuelle des Opérations détaillées  
  
### Configuration

First, [enable product tracking using
lots](../../inventory/product_management/product_tracking/lots.html#inventory-
management-track-products-by-lots) by navigating to Inventory app ‣
Configuration ‣ Settings, and checking the box for Lots & Serial Numbers under
the Traceability heading.

Then, set up the product barcode by navigating to the intended product form in
Inventory app ‣ Products ‣ Products and selecting the product. On the product
form, click Edit. Then, in the General Information tab, fill in the Barcode
field with the unique 14-digit [Global Trade Item Number
(GTIN)](https://www.gs1.org/standards/get-barcodes), which is a universally
recognized identifying number that is provided by GS1.

Important

On the product form, omit the A.I. `01` for GTIN product barcode pattern, as
it is only used to encode multiple barcodes into a single barcode that
contains detailed information about the package contents.

Example

To record the GS1 barcode for the product, `Fuji Apple`, enter the 14-digit
GTIN `20611628936004` in the Barcode field on the product form.

![Saisissez le GTIN à 14 chiffres dans le champ Code-barres sur le formulaire
du produit.](../../../../_images/barcode-field.png)

Astuce

To view a list of _all_ products and their corresponding barcodes in the Odoo
database, navigate to Inventory app ‣ Configuration ‣ Settings. Under the
Barcode heading, click on the Configure Product Barcodes button under the
Barcode Scanner section. Enter the 14-digit GTIN into the Barcode column, then
click Save.

![Vue de la page des codes-barres des produits dans les paramètres
d'inventaire.](../../../../_images/product-barcodes-page.png)

After activating tracking by lots and serial numbers from the settings page,
specify that this feature is to be applied on each product by navigating to
the Inventory tab on the product form. Under Tracking, choose the By Lots
radio button.

![Activez le suivi des produits par lots dans l'onglet "Inventaire" du
formulaire du produit.](../../../../_images/track-by-lots.png)

### Scanner le code-barres sur la réception

Pour garantir une interprétation précise des lots dans Odoo sur les codes-
barres des produits scannés lors d’une opération de réception, allez à
l’application Code-barres pour gérer le [processus de transfert des
réceptions](receipts_deliveries.html#barcode-operations-scan-received-
products).

From the Barcode Scanning dashboard, click the Operations button, then the
Receipts button to view the list of vendor receipts to process. Receipts
generated from POs are listed, but new receipt operations can also be created
directly through the Barcode app using the Create button.

Sur la liste des réceptions, cliquez sur l’opération d’entrepôt (`WH/IN`) et
scannez les codes-barres et les numéros de lot du produit à l’aide d’un
lecteur de codes-barres. Le produit scanné apparaît alors dans la liste.
Utilisez le bouton ✏️ (crayon) pour ouvrir une fenêtre et saisir manuellement
les quantités pour des numéros de lot spécifiques.

Example

After placing a PO for fifty apples, navigate to the associated receipt in the
_Barcode_ app.

Scan the barcode containing the GTIN, quantity, and lot number. For testing
with a barcode scanner, below is an example barcode for the fifty Fuji apples
in Lot 2.

50 Fuji apples in Lot0002 |   
---|---  
2D Matrix | ![2D matrix of GS1 barcode of 50 fuji apples with an assigned lot number.](../../../../_images/fuji-apples-barcode.png)  
A.I. (product) | 01  
GS1 Barcode (product) | 20611628936004  
A.I. (quantity) | 30  
GS1 Barcode (quantity) | 00000050  
A.I. (lot) | 10  
GS1 Barcode (lot #) | LOT0002  
Full GS1 barcode | 0120611628936004 3000000050 10LOT0002  
  
[If the configuration is correct](gs1_nomenclature.html#barcode-operations-
troubleshooting), `50/50` Units processed will be displayed and the Validate
button turns green. Click the Validate button to complete the reception.

![Scannez le code-barres d'un produit sur la page de transfert de réception
dans l'application *Code-barres*.](../../../../_images/receive-50-apples.png)

## Configure barcode for product and non-unit quantity

Pour créer un code-barres GS1 qui contient des produits mesurés dans une
quantité non unitaire, comme des kilogrammes, les modèles de code-barres
suivants sont utilisés :

Nom | Nom de la règle | A.I. | Modèle de code-barres | Champ dans Odoo  
---|---|---|---|---  
Produit | Global Trade Item Number (GTIN) | 01 | (01)(\d{14}) | Champ Code-barres sur un formulaire de produit  
Quantité en kilogrammes | Nombre variable d’articles | 310[0-5] | (310[0-5])(\d{6}) | Champ Unités sur un formulaire de transfert  
  
### Scanner le code-barres sur la réception

Pour confirmer que les quantités sont correctement interprétées dans Odoo,
placez une commande dans l’application _Achats_ en utilisant l’unité de mesure
(UdM) appropriée pour la quantité de produits à acheter.

Pour plus d'infos

[Simplify vendor unit conversions with
UoMs](../../inventory/product_management/product_replenishment/uom.html#inventory-
product-replenishment-unit-conversion)

Une fois la commande placée, allez à l’application Code-barres pour [recevoir
l’envoi du fournisseur](receipts_deliveries.html#barcode-operations-scan-
received-products).

Example

On the receipt in the _Barcode_ app, receive an order for `52.1 kg` of peaches
by scanning the barcode containing the GTIN and quantity of peaches in
kilograms.

52.1 kg of Peaches |   
---|---  
2D Matrix | ![2D matrix of GS1 barcode of 52.1 kg of peaches.](../../../../_images/peaches-barcode.png)  
A.I. (product) | 01  
GS1 Barcode (product) | 00614141000012  
A.I. (kg, 1 decimal point) | 3101  
GS1 Barcode (quantity) | 000521  
Full GS1 barcode | 0100614141000012 3101000521  
  
[If the configuration is correct](gs1_nomenclature.html#barcode-operations-
troubleshooting), `52.1 / 52.1` kg will be displayed and the Validate button
turns green. Finally, press Validate to complete the validation.

![Écran de scan du code-barres pour une opération de réception dans
l'application Code-barres.](../../../../_images/scan-barcode-peaches.png)

## Verify product moves

For additional verification, the quantities of received products are also
recorded on the Product Moves report, accessible by navigating to Inventory
app ‣ Reporting ‣ Product Moves.

Les articles sur le rapport des Mouvements de stock sont regroupés par produit
par défaut. Pour confirmer les quantités reçues, cliquez sur une ligne de
produit pour ouvrir son menu déroulant rétractable, qui affiche une liste des
_lignes de mouvement de stock_ pour le produit. Le dernier mouvement de stock
correspond au numéro de réception de l’entrepôt (par ex. `WH/IN/00013`) et à
la quantité traitée dans la lecture du code-barres, ce qui prouve que les
enregistrements traités dans l’application _Code-barres_ ont été correctement
stockés dans _Inventaire_.

![Enregistrement d'un mouvement de stock de réception pour 52,1 kg de
pêches.](../../../../_images/stock-moves-peach.png)

  *[A.I.]: Application Identifier
  *[GTIN]: Global Trade Item Number
  *[POs]: Purchase Orders
  *[PO]: Purchase Order

