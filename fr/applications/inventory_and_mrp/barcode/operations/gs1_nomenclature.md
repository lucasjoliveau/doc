# Nomenclature des codes-barres GS1

[GS1 nomenclature](https://www.gs1us.org/) consolidates various product and
supply chain data into a single barcode. Odoo takes in [unique Global Trade
Item Numbers](https://www.gs1.org/standards/get-barcodes) (GTIN), purchased by
businesses, to enable global shipping, sales, and eCommerce product listing.

Configure GS1 nomenclature to scan barcodes of sealed boxes and identify
essential product information, such as GTIN, lot number, quantity information,
and more.

Important

GTINs are unique product identification that **must** be [purchased from
GS1](https://www.gs1.org/standards/get-barcodes) to use GS1 barcodes.

Pour plus d'infos

  * [Tous les codes-barres GS1](https://www.gs1.org/standards/barcodes/application-identifiers)

  * Règles GS1 par défaut d’Odoo

  * Pourquoi mon code-barres ne fonctionne-t-il pas ?

## Configurer la nomenclature de code-barres

Pour utiliser la nomenclature GS1 nomenclature, allez à l’application
Inventaire ‣ Configuration ‣ Paramètres. Dans la section Code-barres, cochez
la case à côté de Lecteur de codes-barres. Ensuite, sélectionnez Nomenclature
des code-barres ‣ Nomenclature GS1 par défaut dans les options de nomenclature
des codes-barres par défaut.

![Choose GS1 from dropdown and click the external link to see the list of GS1
rules.](../../../../_images/setup-gs1-nomenclature.png)

The list of GS1 _rules_ and _barcode patterns_ Odoo supports by default is
accessible by clicking the ➡️ (arrow) icon to the right of the Barcode
Nomenclature selection.

In the Open: Nomenclature pop-up table, view and edit the GS1 Rule Names
available in Odoo. The table contains all the information that can be
condensed with a GS1 barcode, along with the corresponding Barcode Pattern.

Astuce

After setting GS1 as the barcode nomenclature, the Barcode Nomenclatures
settings can also be accessed by a hidden menu that’s discoverable after
enabling [developer mode](../../../general/developer_mode.html#developer-
mode). Once enabled, navigate to the Inventory app ‣ Configuration ‣ Barcode
Nomenclatures menu and finally, select Default GS1 Nomenclature.

## Use GS1 barcodes in Odoo

For product identification using GS1 barcodes in Odoo, businesses obtain a
[unique GTIN](https://www.gs1.org/standards/get-barcodes) as an
internationally distinct product identifier purchased from GS1. This GTIN is
combined with specific product details following GS1’s designated _barcode
pattern_. The barcode pattern’s arrangement of numbers and letters must adhere
to GS1 conventions for accurate interpretation by global systems along the
supply chain.

Every barcode starts with a 2-4 digit [application
identifier](https://www.gs1.org/standards/barcodes/application-identifiers)
(A.I.). This required prefix universally indicates what kind of information
the barcode contains. Odoo follows GS1 rules for identifying information, as
detailed in the default GS1 rules list. Including the relevant A.I. from the
list enables Odoo to correctly interpret GS1 barcodes. While most barcode
patterns have a fixed length requirement, certain ones, such as lots and
serial numbers, have flexible length.

Astuce

For flexible-length barcode patterns not placed at the end of the GS1 barcode,
use the FNC1 separator (`\x1D`) to end the barcode.

Example: The barcode pattern for lot numbers is 20 characters long. Instead of
creating a 20-character lot number barcode, like `LOT00000000000000001`, use
the FNC1 separator to make it shorter: `LOT001x1D`.

Refer to the GS1 nomenclature list to see a comprehensive list of all barcode
patterns and rules to follow. Otherwise, refer to [this GS1 usage
doc](gs1_usage.html#barcode-operations-gs1-usage) for specific examples of
combining GTIN to product information and configuring the workflow.

Pour plus d'infos

  * [Lots workflow](gs1_usage.html#barcode-operations-gs1-lots)

  * [Non-unit quantities workflow](gs1_usage.html#barcode-operations-quantity-ex)

### Créer des règles

GS1 rules are a specific format of information contained in the barcode,
beginning with an A.I. and containing a defined length of characters. Scanning
GS1 barcodes from the default GS1 list auto-fills corresponding data in the
Odoo database.

Adding GS1 barcode rules in Odoo ensures accurate interpretation of unique,
non-standard GS1 formats.

To do so, begin by turning on [developer
mode](../../../general/developer_mode.html#developer-mode) and navigating to
the Barcode Nomenclatures list in Inventory app ‣ Configuration ‣ Barcode
Nomenclatures. Then, select the Default GS1 Nomenclature list item.

Sur la page Nomenclature GS1 par défaut, cliquez sur Ajouter une ligne en bas
du tableau, ce qui ouvre une fenêtre permettant de créer une nouvelle règle.
Le champ Nom de la règle est utilisé en interne pour identifier ce que le
code-barres représente. Les Types de codes-barres sont des classifications
différentes d’informations qui peuvent être comprises par le système (par ex.
produit, quantité, date limite d’utilisation optimale, colis, bon de
réduction). La Séquence représente la priorité de la règle : plus la valeur
est petite, plus la règle apparaît en haut du tableau. Odoo suit l’ordre
séquentiel de ce tableau et utilise la première règle qui correspond à la
séquence. Le Modèle de code-barres est la façon dont la séquence de lettres ou
de chiffres est reconnue par le système pour contenir des informations sur le
produit.

Après avoir complété les informations, cliquez sur le bouton Enregistrer &
Nouveau pour créer une autre règle ou cliquez sur Enregistrer & Fermer pour
enregistrer et revenir au tableau des règles.

## Dépannage des codes-barres

Les codes-barres GS1 étant difficiles à utiliser, voici quelques vérifications
à effectuer lorsque les codes-barres ne fonctionnent pas comme prévu :

  1. Assurez-vous que le paramètre Nomenclature des codes-barres est défini sur Nomenclature GS1 par défaut. Consultez la section sur la configuration de la nomenclature pour plus de détails.

  2. Assurez-vous que les champs scannés dans le code-barres sont activés dans Odoo. Par exemple, pour scanner un code-barres contenant des lots et des numéros de série, assurez-vous que la fonctionnalité Lots & Numéros de série est activée dans les [paramètres d’Odoo](gs1_usage.html#barcode-operations-lot-setup) et [sur le produit](gs1_usage.html#barcode-operations-lot-setup-on-product).

  3. Supprimez la ponctuation comme les parenthèses `()` ou les crochets `[]` entre l”A.I. et la séquence du code-barres. Ils sont généralement utilisés dans les exemples pour faciliter la lecture et ne doivent **pas** être inclus dans le code-barres final. Pour plus de détails sur la création des codes-barres GS1, consultez cette section.

  4. Lorsqu’un seul code-barres contient plusieurs champs encodés, Odoo exige que toutes les règles soient répertoriées dans la nomenclature des codes-barres pour qu’Odoo puisse lire le code-barres. Cette section détaille comment ajouter de nouvelles règles dans la nomenclature des codes-barres.

  5. Test barcodes containing multiple encoded fields, piece by piece, to figure out which field is causing the issue.

Example

When testing a barcode containing the GTIN, lot number, and quantity, start by
scanning the GTIN alone. Then, test the GTIN with the lot number, and finally,
try scanning the whole barcode.

  6. After diagnosing the encoded field is unknown, add new rules to Odoo’s default list to recognize GS1 barcodes with unique specifications.

Important

While the new field will be read, the information won’t link to an existing
field in Odoo without developer customizations. However, adding new rules is
necessary to ensure the rest of the fields in the barcode are interpreted
correctly.

## Liste de la nomenclature GS1

Le tableau suivant contient la liste par défaut des règles GS1 d’Odoo. Les
modèles de code-barres sont écrits sous forme d’expressions régulières. Seules
les trois premières règles requièrent un [chiffre de
contrôle](https://www.gs1.org/services/check-digit-calculator) comme caractère
final.

Nom de la règle | Type | Modèle de code-barres | Type de contenu GS1 | Champ Odoo  
---|---|---|---|---  
Serial Shipping Container Code | Package | (00)(\d{18}) | Identifiant numérique | Nom de colis  
Global Trade Item Number (GTIN) | Unité de produit | (01)(\d{14}) | Identifiant numérique | Champ Code-barres sur un formulaire de produit  
GTIN of contained trade items | Unité de produit | (02)(\d{14}) | Identifiant numérique | Conditionnement  
Ship to / Deliver to global location | Emplacement de destination | (410)(\d{13}) | Identifiant numérique | Emplacement de destination  
Ship / Deliver for forward | Emplacement de destination | (413)(\d{13}) | Identifiant numérique | Emplacement d’origine  
I.D. of a physical location | Emplacement | (414)(\d{13}) | Identifiant numérique | Emplacement  
Numéro de lot | Lot | (10) ([! »%-/0-9:-?A-Z_a-z]{0,20}) | Nom alphanumérique | Lot  
Numéro de série | Lot | (21) ([! »%-/0-9:-?A-Z_a-z]{0,20}) | Nom alphanumérique | Numéro de série  
Packaging date (YYMMDD) | Date de colisage | (13)(\d{6}) | Date | Date de colisage  
Best before date (YYMMDD) | Date limite d’utilisation optimale | (15)(\d{6}) | Date | Date limite d’utilisation optimale  
Expiration date (YYMMDD) | Date d’expiration | (17)(\d{6}) | Date | Date d’expiration  
Nombre variable d’articles | Quantité | (30)(\d{0,8}) | Mesure | UdM : Unités  
Count of trade items | Quantité | (37)(\d{0,8}) | Mesure | Qté en unités pour les conteneurs (AI 02)  
Net weight: kilograms (kg) | Quantité | (310[0-5])(\d{6}) | Mesure | Qté en kg  
Length in meters (m) | Quantité | (311[0-5])(\d{6}) | Mesure | Qté en m  
Net volume: liters (L) | Quantité | (315[0-5])(\d{6}) | Mesure | Qté en L  
Net volume: cubic meters (m3) | Quantité | (316[0-5])(\d{6}) | Mesure | Qté en m3  
Length in inches (in) | Quantité | (321[0-5])(\d{6}) | Mesure | Qté en pouces  
Net weight/volume: ounces (oz) | Quantité | (357[0-5])(\d{6}) | Mesure | Qté en oz  
Net volume: cubic feet (ft3) | Quantité | (365[0-5])(\d{6}) | Mesure | Qté en ft3  
Packaging type | Type de conditionnement | (91) ([! »%-/0-9:-?A-Z_a-z]{0,90}) | Nom alphanumérique | Type de colis
  *[GTIN]: Global Trade Item Number
  *[GTINs]: Global Trade Item Numbers
  *[A.I.]: Identificateur de données

