# Configurer votre lecteur de codes-barres

Follow this guide to choose and set up a barcode scanner compatible with
Konvergo ERP’s _Inventory_ and _Barcode_ apps.

![An image of an example barcode scanner.](../../../../_images/barcode-
scanner.png)

An image of an example barcode scanner.

## Scanner types

Before setting up a barcode scanner, it is important to determine which
scanner type best meets the needs of the business. There are three main types,
each with their own benefits and use cases:

  * **USB scanners** are connected to a computer, and are suitable for businesses that scan products at a fixed location, like at the checkout in a grocery store. Ensure the chosen USB scanner is compatible with the keyboard layout of the computer.

  * **Bluetooth scanners** pair with a smartphone or tablet, making them an ideal cost-effective and portable barcode scanner option. In this scenario, Konvergo ERP is installed on the smartphone, allowing warehouse operators to handle operations, and check stock directly through their mobile devices.

  * **Mobile computer scanners** are mobile devices with a built-in barcode scanner. First, ensure the device can run the Konvergo ERP mobile app properly. Recent models that use Android OS with the Google Chrome browser, or Windows OS with Microsoft Edge, should work. However, testing is crucial due to the variety of available models and configurations.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odoo.com/app/inventory-hardware">Compatible hardware with Konvergo ERP Inventory</a></p>
</div>

## Configuration

When setting up the barcode scanner, make sure the following configurations
are correct so the scanner can properly interpret barcodes with Konvergo ERP.

### Disposition du clavier

When using a USB barcode scanner, match its keyboard layout with the operating
system’s layout for proper interpretation of characters. Generally, the
scanning mode should be set to accept a USB keyboard (HID), with the language
set based on the keyboard that is in use.

To configure the keyboard layout for a **Zebra** scanner, scan the keyboard
wedge barcode for the desired language in the scanner’s user manual.

![Example of a user manual for keyboard layout.](../../../../_images/keyboard-
barcode.png)

Examples of keyboard language settings in the Zebra scanner user manual.

### Retour à la ligne automatique

Konvergo ERP has a default 100-millisecond delay between scans to prevent accidental
double scanning. To synchronize with the barcode scanner, set it to include a
_carriage return_ (character like the « Enter » key on a keyboard) after each
scan. Konvergo ERP interprets the carriage return as the end of the barcode input; so
Konvergo ERP accepts the scan, and waits for the next one.

Typically, on the scanner, a carriage return is included by default. Ensure it
is set by scanning a specific barcode in the user manual, like `CR suffix ON`
or `Apply Enter for suffix`.

### Zebra scanner

When using Zebra scanners, ensure the following keystroke configurations are
set to prevent errors.

Begin on the Zebra scanner’s home screen, and select the **DataWedge** app
(the icon for the app is a light blue barcode). On the **DataWedge Profiles**
page, select the profile option to access the Zebra scanner’s settings.

Scroll down to the **Keyboard Output** option, and ensure the **Enable/disable
keystroke output** option is **Enabled**.

![Show keystroke option in the Zebra scanner's DataWedge
app.](../../../../_images/enable-keystroke.png)

Now, go back to the **Profile** options page, and select **Key event
options**. Here, ensure the **Send Characters as Events** option is checked.

