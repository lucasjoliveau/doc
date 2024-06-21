# GS1 barcode nomenclature

[GS1 nomenclature](https://www.gs1us.org/) consolidates various product and
supply chain data into a single barcode. Konvergo ERP takes in [unique Global Trade
Item Numbers](https://www.gs1.org/standards/get-barcodes) (GTIN), purchased by
businesses, to enable global shipping, sales, and eCommerce product listing.

Configure GS1 nomenclature to scan barcodes of sealed boxes and identify
essential product information, such as GTIN, lot number, quantity information,
and more.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p><abbr title="Global Trade Item Numbers">GTINs</abbr> are unique product identification that <b>must</b> be <a href="https://www.gs1.org/standards/get-barcodes">purchased from GS1</a> to use GS1 barcodes.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.gs1.org/standards/barcodes/application-identifiers">All GS1 barcodes</a></p></li>
<li><p><a href="#barcode-operations-default-gs1-nomenclature-list"><span class="std std-ref">Konvergo ERP’s default GS1 rules</span></a></p></li>
<li><p><a href="#barcode-operations-troubleshooting"><span class="std std-ref">Why’s my barcode not working?</span></a></p></li>
</ul>
</div>

## Set up barcode nomenclature

To use GS1 nomenclature, navigate to the Inventory app ‣ Configuration ‣
Settings. Then under the **Barcode** section, check the **Barcode Scanner**
box. Next, select Barcode Nomenclature ‣ Default GS1 Nomenclature from the
default barcode nomenclature options.

![Choose GS1 from dropdown and click the external link to see the list of GS1
rules.](../../../../_images/setup-gs1-nomenclature.png)

The list of GS1 _rules_ and _barcode patterns_ Konvergo ERP supports by default is
accessible by clicking the **➡️ (arrow)** icon to the right of the **Barcode
Nomenclature** selection.

In the **Open: Nomenclature** pop-up table, view and edit the GS1 **Rule
Names** available in Konvergo ERP. The table contains all the information that can be
condensed with a GS1 barcode, along with the corresponding **Barcode
Pattern**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>After setting GS1 as the barcode nomenclature, the Barcode Nomenclatures
settings can also be accessed by a hidden menu that’s discoverable after enabling <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer
mode</span></a>. Once enabled, navigate to the Inventory app ‣
Configuration ‣ Barcode Nomenclatures menu and finally, select <b>Default GS1
Nomenclature</b>.</p>
</div>

## Use GS1 barcodes in Konvergo ERP

For product identification using GS1 barcodes in Konvergo ERP, businesses obtain a
[unique GTIN](https://www.gs1.org/standards/get-barcodes) as an
internationally distinct product identifier purchased from GS1. This GTIN is
combined with specific product details following GS1’s designated _barcode
pattern_. The barcode pattern’s arrangement of numbers and letters must adhere
to GS1 conventions for accurate interpretation by global systems along the
supply chain.

Every barcode starts with a 2-4 digit [application
identifier](https://www.gs1.org/standards/barcodes/application-identifiers)
(A.I.). This required prefix universally indicates what kind of information
the barcode contains. Konvergo ERP follows GS1 rules for identifying information, as
detailed in the default GS1 rules list. Including the relevant A.I. from the
list enables Konvergo ERP to correctly interpret GS1 barcodes. While most barcode
patterns have a fixed length requirement, certain ones, such as lots and
serial numbers, have flexible length.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>For flexible-length barcode patterns not placed at the end of the GS1 barcode, use the FNC1
separator (<code>\x1D</code>) to end the barcode.</p>
<p>Example: The barcode pattern for lot numbers is 20 characters long. Instead of creating a
20-character lot number barcode, like <code>LOT00000000000000001</code>, use the FNC1 separator to make it
shorter: <code>LOT001x1D</code>.</p>
</div>

Refer to the GS1 nomenclature list to see a comprehensive list of all barcode
patterns and rules to follow. Otherwise, refer to [this GS1 usage
doc](gs1_usage#barcode-operations-gs1-usage) for specific examples of
combining GTIN to product information and configuring the workflow.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Lots workflow</span></a></p></li>
<li><p><a href="gs1_usage#barcode-operations-quantity-ex"><span class="std std-ref">Non-unit quantities workflow</span></a></p></li>
</ul>
</div>

### Create rules

GS1 rules are a specific format of information contained in the barcode,
beginning with an A.I. and containing a defined length of characters. Scanning
GS1 barcodes from the default GS1 list auto-fills corresponding data in the
Konvergo ERP database.

Adding GS1 barcode rules in Konvergo ERP ensures accurate interpretation of unique,
non-standard GS1 formats.

To do so, begin by turning on [developer
mode](../../../general/developer_mode#developer-mode) and navigating to
the **Barcode Nomenclatures** list in Inventory app ‣ Configuration ‣ Barcode
Nomenclatures. Then, select the **Default GS1 Nomenclature** list item.

On the **Default GS1 Nomenclature** page, select **Add a line** at the bottom
of the table, which opens a window to create a new rule. The **Rule Name**
field is used internally to identify what the barcode represents. The barcode
**Types** are different classifications of information that can be understood
by the system (e.g. product, quantity, best before date, package, coupon). The
**Sequence** represents the priority of the rule; this means the smaller the
value, the higher the rule appears on the table. Konvergo ERP follows the sequential
order of this table and will use the first rule it matches based on the
sequence. The **Barcode Pattern** is how the sequence of letters or numbers is
recognized by the system to contain information about the product.

After filling in the information, click the **Save & New** button to make
another rule or click **Save & Close** to save and return to the table of
rules.

## Barcode troubleshooting

Since GS1 barcodes are challenging to work with, here are some checks to try
when the barcodes are not working as expected:

  1. Ensure that the **Barcode Nomenclature** setting is set as Default GS1 Nomenclature. Jump to the nomenclature setup section for more details.

  2. Ensure that the fields scanned in the barcode are enabled in Konvergo ERP. For example, to scan a barcode containing lots and serial numbers, make sure the **Lots & Serial Numbers** feature is enabled in [Konvergo ERP’s settings](gs1_usage#barcode-operations-lot-setup) and [on the product](gs1_usage#barcode-operations-lot-setup-on-product).

  3. Omit punctuation such as parentheses `()` or brackets `[]` between the A.I. and the barcode sequence. These are typically used in examples for ease of reading and should **not** be included in the final barcode. For more details on building GS1 barcodes, go to this section.

  4. When a single barcode contains multiple encoded fields, Konvergo ERP requires all rules to be listed in the barcode nomenclature for Konvergo ERP to read the barcode. This section details how to add new rules in the barcode nomenclature.

  5. Test barcodes containing multiple encoded fields, piece by piece, to figure out which field is causing the issue.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>When testing a barcode containing the <abbr title="Global Trade Item Number">GTIN</abbr>, lot number, and quantity, start by scanning the
<abbr title="Global Trade Item Number">GTIN</abbr> alone. Then, test the <abbr title="Global Trade Item Number">GTIN</abbr> with the lot number, and finally, try scanning the whole
barcode.</p>
</div>

  6. After diagnosing the encoded field is unknown, add new rules to Konvergo ERP’s default list to recognize GS1 barcodes with unique specifications.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>While the new field will be read, the information won’t link to an existing field in Konvergo ERP
without developer customizations. However, adding new rules is necessary to ensure the rest of
the fields in the barcode are interpreted correctly.</p>
</div>

## GS1 nomenclature list

The table below contains Konvergo ERP’s default list of GS1 rules. Barcode patterns
are written in regular expressions. Only the first three rules require a
[check digit](https://www.gs1.org/services/check-digit-calculator) as the
final character.

Rule Name | Type | Barcode Pattern | GS1 Content Type | Konvergo ERP field  
---|---|---|---|---  
Serial Shipping Container Code | Package | (00)(\d{18}) | Numeric identifier | Package name  
Global Trade Item Number (GTIN) | Unit Product | (01)(\d{14}) | Numeric identifier | **Barcode** field on product form  
GTIN of contained trade items | Unit Product | (02)(\d{14}) | Numeric identifier | Packaging  
Ship to / Deliver to global location | Destination location | (410)(\d{13}) | Numeric identifier | Destination location  
Ship / Deliver for forward | Destination location | (413)(\d{13}) | Numeric identifier | Source location  
I.D. of a physical location | Location | (414)(\d{13}) | Numeric identifier | Location  
Batch or lot number | Lot | (10) ([!”%-/0-9:-?A-Z_a-z]{0,20}) | Alpha-numeric name | Lot  
Serial number | Lot | (21) ([!”%-/0-9:-?A-Z_a-z]{0,20}) | Alpha-numeric name | Serial number  
Packaging date (YYMMDD) | Packaging Date | (13)(\d{6}) | Date | Pack date  
Best before date (YYMMDD) | Best before Date | (15)(\d{6}) | Date | Best before date  
Expiration date (YYMMDD) | Expiration Date | (17)(\d{6}) | Date | Expiry date  
Variable count of items | Quantity | (30)(\d{0,8}) | Measure | UoM: Units  
Count of trade items | Quantity | (37)(\d{0,8}) | Measure | Qty in units for containers (AI 02)  
Net weight: kilograms (kg) | Quantity | (310[0-5])(\d{6}) | Measure | Qty in kg  
Length in meters (m) | Quantity | (311[0-5])(\d{6}) | Measure | Qty in m  
Net volume: liters (L) | Quantity | (315[0-5])(\d{6}) | Measure | Qty in L  
Net volume: cubic meters (m3) | Quantity | (316[0-5])(\d{6}) | Measure | Qty in m3  
Length in inches (in) | Quantity | (321[0-5])(\d{6}) | Measure | Qty in inches  
Net weight/volume: ounces (oz) | Quantity | (357[0-5])(\d{6}) | Measure | Qty in oz  
Net volume: cubic feet (ft3) | Quantity | (365[0-5])(\d{6}) | Measure | Qty in ft3  
Packaging type | Packaging Type | (91) ([!”%-/0-9:-?A-Z_a-z]{0,90}) | Alpha-numeric name | Package type
  *[GTIN]: Global Trade Item Number
  *[A.I.]: Application Identifier

