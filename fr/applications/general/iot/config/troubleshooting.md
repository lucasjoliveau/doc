# Aide au dépannage

## Connexion à l’IoT box

### Je ne trouve pas le code d’appariement pour connecter l’IoT box

Le code d’appariement doit être imprimé sur les imprimantes de reçu connectées
à l”IoT box et doit également s’afficher sur les moniteurs connectés.

The pairing code does not show under the following circumstances:

  * L”IoT box est déjà connectée à une base de données Konvergo ERP.

  * L”IoT box n’est pas connectée à Internet.

  * The code is only valid for 5 minutes after the IoT box has started. It is automatically removed from connected displays when this time has expired.

  * The version of the IoT box image is too old. If the IoT box image is from an earlier version, then the SD card of the IoT box needs to be re-flashed to update the image (see [Flashing the SD Card](updating_iot#iot-config-flash)).

If none of the cases listed above correct the issue, then make sure the IoT
box has correctly started, by checking that a fixed green LED is showing next
to the power port.

### IoT box is connected but it is not showing in the database

When an IoT box connects to a database, it may restart. If so, it can take up
to five minutes before appearing in the database. If the IoT box is still not
showing after five minutes, make sure that the IoT box can reach the database
and that the server does not use a multi-database environment.

Pour accéder à la base de données à partir de l”:`IoT (Internet of Things)`
box, ouvrez un navigateur et tapez l’adresse de la base de données.

### L’IoT box est connectée à la base de données Konvergo ERP, mais n’est pas
accessible

Assurez-vous que l”IoT box et l’ordinateur exécutant le navigateur se trouvent
sur le même réseau, car l”IoT box n’est pas accessible en dehors du réseau
local.

### The HTTPS certificate does not generate

Afin de générer un certificat HTTPS, un abonnement IoT box est nécessaire pour
l”IoT box. La connexion de l”IoT box avant la configuration d’un abonnement
IoT pour la base de données et l”IoT box avec le gestionnaire de compte
entraînera un connexion non sécurisée.

De plus, un pare-feu peut également empêcher la génération correcte du
certificat HTTPS. Dans ce cas, désactivez le pare-feu jusqu’à ce que le
certificat est généré avec succès. Notez également que certains périphériques,
tels qu’un router avec un pare-feu intégré, peuvent empêcher la génération du
certificat HTTPS.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https_certificate_iot">certificat HTTPS (IoT)</a></p>
</div>

## Imprimante

### L’imprimante n’est pas détectée

If a printer does not appear in the devices list, go to the IoT box homepage
and make sure that it is listed under **Printers**.

![La page d'accueil de l'IoT box.](../../../../_images/printer-status.png)

If the printer is not present on the IoT box homepage, click **Printers
Server** , go to the **Administration** tab and click on **Add Printer**. If
the printer is not present in the list, it is likely not connected properly.

### L’imprimante produit un texte aléatoire

Pour la plupart des imprimantes, le bon pilote est automatiquement détecté et
sélectionné. Cependant, dans certains cas, il se peut que le mécanisme de
détection automatique ne soit pas suffisant et que, si aucun pilote n’est
trouvé, l’imprimante puisse imprimer des caractères aléatoires.

The solution is to manually select the corresponding driver. On the IoT box
homepage, click on **Printers Server** , go to the **Printers** tab and select
the printer in the list. In the **Administration** drop-down menu, click on
**Modify Printer**. Follow the steps and select the _make_ and _model_
corresponding to the printer.

![Modifiez l'imprimante connectée à l'IoT box.](../../../../_images/modify-
printer.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>

#### Cas particulier de la configuration Epson

La plupart des imprimantes Epson prennent en charge l’impression de reçus dans
Konvergo ERP PdV à l’aide de la commande `GS v 0`. Cependant, les modèles
d’imprimantes Epson suivants ne prennent pas en charge cette commande :

  * TM-U220

  * TM-U230

  * TM-P60

  * TMP-P60II

Contournez ce problème en configurant l’imprimante pour qu’elle utilise plutôt
la commande `ESC *`.

##### Processus pour forcer la commande ESC *

###### Compatibilité de l’imprimante Epson

La première étape consiste à vérifier si l’imprimante n’est pas incompatible
avec la commande `GS v 0`.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=94">Documentation Epson GS v 0</a> pour les imprimantes compatibles avec <code>GS v 0</code>.</p></li>
<li><p><a href="https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=88">Documentation Epson ESC *</a> pour les imprimantes compatibles avec <code>ESC *</code>.</p></li>
</ul>
</div>

Si l’imprimante n’est pas compatible avec la commande `ESC *`, le processus
suivant n’est pas possible. Si l’imprimante est compatible avec la commande
`ESC *` pour imprimer, suivez cette procédure pour configurer l’imprimante
avec l”IoT box.

###### Configuration de l’IoT box pour ESC *

Pour configurer l”IoT box pour qu’elle utilise la commande `ESC *` pour
imprimer, allez à la page d’accueil de l”IoT box en allant à l’application IoT
‣ IoT Box. Cliquez ensuite sur l”**adresse IP** et vous serez redirigé vers la
page d’accueil de l”IoT box.

**Choix de l’imprimante**

Cliquez maintenant sur le bouton **Serveur d’imprimantes**. Le navigateur sera
redirigé vers la page _CUPS_. Allez ensuite à Administration ‣ Imprimantes ‣
Ajouter une imprimante, choisissez l’imprimante qui doit être modifiée et
cliquez sur **Continuer**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le nom de l’imprimante n’est toujours pas connu, suivez les étapes suivantes :</p>
<ol class="arabic simple">
<li><p>Prenez note des imprimantes répertoriées sur la page <em>CUPS</em>.</p></li>
<li><p>Éteignez l’imprimante et actualisez la page.</p></li>
<li><p>Voyez maintenant s’il y a une différence avec la première liste pour voir quelle imprimante a disparu.</p></li>
<li><p>Remettez l’imprimante sous tension et actualisez à nouveau la page.</p></li>
<li><p>Vérifiez à nouveau la liste pour voir si l’imprimante réapparaît.</p></li>
<li><p>L’imprimante qui disparaît et qui réapparaît dans la liste des imprimantes est le nom de l’imprimante en question.</p></li>
</ol>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il peut s’agir d”<b>Inconnu</b> dans <b>Imprimantes locales</b>.</p>
</div>
</div>

**Convention d’appellation de CUPS**

`CUPS` will prompt the administrator for three pieces of information: the
**Name** , **Description** and the **Location**. The last two pieces of
information do not need to be specific, however, the **Name** should follow a
particular convention to work with the `ESC *` command.

Le **Nom** doit correspondre à cette convention :
`<printer_name>__IMC_<param_1>_<param_2>_..._<param_n>__`

Détail de la convention d’appellation :

  * `printer_name` : Il s’agit du nom de l’imprimante. Il peut être composé de n’importe quel caractère tant qu’il ne contient pas `_`, `/`, `#`, or ` ` (caractère espace).

  * `IMC` : C’est l’abréviation d” _Image Mode Column_ (nom simplifié de `ESC *`).

  * `param_1` : Il s’agit du paramètre spécifique :

    * `SCALE<X>` : Échelle de l’image (avec le même rapport d’aspect). `X` doit être un entier décrivant le pourcentage d’échelle à utiliser.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><code>100</code> est la taille originale, <code>50</code> est la moitié de la taille et <code>200</code> est le double de la taille.</p>
</div>

    * `LDV` : _Faible densité verticale_ (sera défini sur _Densité verticale élevée_ si ce n’est pas précisé).

    * `LDH` : _Faible densité horizontale_ (sera défini sur _Densité horizontale élevée_ si ce n’est pas précisé).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il se peut que les paramètres de <em>densité</em> doivent être configurés d’une manière particulière en fonction du modèle d’imprimante.</p>
</div>

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Consultez la <a href="https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=88">documentation d’Epson relative à ESC *</a> et cliquez sur le modèle d’imprimante dans le tableau ci-dessus pour voir si l’imprimante doit définir ces paramètres.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Voici des exemples de formatage de nom correct et incorrect :</p>
<p>Formatage de nom correct :</p>
<ul>
<li><p><code>EPSONTMm30II__IMC__</code></p></li>
<li><p><code>EPSON_TM_U220__IMC_LDV_LDH_SCALE80__</code></p></li>
</ul>
<p>Formatage de nom incorrect (cela n’empêche pas l’impression, mais le résultat risque de ne pas être celui attendu) :</p>
<ul>
<li><p><code>EPSON TMm 30II</code> -&gt; The name cannot have spaces.</p></li>
<li><p><code>EPSONTMm30II</code> -&gt; The name itself is correct, but it will not use <code>ESC *</code>.</p></li>
<li><p><code>EPSONTMm30II__IMC</code> -&gt; Il manque la fin <code>__</code> à ce nom.</p></li>
<li><p><code>EPSONTMm30II__IMC_XDV__</code> -&gt; Le paramètre <code>XDV</code> ne correspond à aucun paramètre existant.</p></li>
<li><p><code>EPSONTMm30II__IMC_SCALE__</code> -&gt; Il manque la valeur d’échelle du paramètre <code>SCALE</code>.</p></li>
</ul>
</div>

**Terminer l’ajout d’une imprimante**

Après avoir configuré le nom de l’imprimante avec la bonne convention
d’appellation, cliquez sur **Continuer**. Définissez ensuite la valeur
**Marque** sur **Raw** et la valeur **Modèle** sur **Raw Queue (en)**.

Après avoir complété ces étapes, cliquez sur **Ajouter une imprimante**. Si la
configuration a été faite correctement, la page devrait rediriger vers la page
_Bannières_.

À ce stade, l’imprimante doit être créée. Il suffit maintenant que l”IoT la
détecte et se synchronise avec le serveur Konvergo ERP (cela peut prendre quelques
minutes).

**Ajout de l’imprimante à Konvergo ERP PdV**

Once the printer is visible on the Konvergo ERP database, do not forget to choose it
in the PoS printer. Navigate to Pos App ‣ Settings ‣ Connected Devices ‣ IoT
Box ‣ Receipt Printer ‣ Save.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si l’imprimante a été mal configurée (elle imprime toujours un texte aléatoire ou le reçu imprimé est trop grand ou trop petit), elle ne peut pas être modifiée via le nom de l’imprimante avec <em>CUPS</em>. En revanche, vous pouvez répéter la procédure susmentionnée pour configurer une autre imprimante à partir de zéro et en créer une avec des paramètres modifiés.</p>
</div>

**Exemple de configuration de l’imprimante Epson TM-U220B à l’aide de ESC**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>0

### DYMO LabelWriter print issue

The DYMO LabelWriter has a known issue in printing with the IoT box. The
OpenPrinting CUPS server installs the printer using **Local RAW Printer**
drivers. In order to print anything, the correct **Make and Model** needs to
be set, so the correct driver is referenced when using the device.

Additionally, a new printer needs to be added to reduce a print delay that
occurs after updating the driver.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>1

#### DYMO LabelWriter not printing

In the case where the DYMO LabelWriter is not printing anything, a new driver
needs to be installed.

First, open the OpenPrinting CUPS console by clicking Printers server at the
bottom of the IoT box homepage. Next, click on Printers in the top menu. Click
into the printer in question, and select **Maintenance** in the first drop-
down menu. Then, select **Modify Printer** in the second drop-down menu.

![Modify the make and model of the DYMO LabelWriter. Maintenance and Modify
drop-down menus highlighted.](../../../../_images/main-modify.png)

Next, select the specific network connection/printer that the modification
should be made on. Click **Continue**.

![Printer selection screen with Continue
highlighted.](../../../../_images/modify-select-printer.png)

On the next page, click **Continue** to proceed to set the **Make** of the
printer.

![Printer modification screen with Continue
highlighted.](../../../../_images/modify-printer-dymo.png)

Under **Make** select **DYMO** from the menu. Click on **Continue** to set the
**Model**.

![Setting the make page, with DYMO and continue
highlighted.](../../../../_images/setting-make.png)

On the following page, set the **Model** to **DYMO LabelWriter 450 DUO Label
(en)** (or whichever DYMO printer model is being used). Click on **Modify
Printer** to complete setting the new driver, a confirmation page will appear.

![Setting the printer model page with DYMO LabelWriter 450 DUO Label \(en\)
highlighted.](../../../../_images/setting-model.png)

After being redirected to a confirmation page, acknowledging a successful
update, click on the Printers button in the top menu.

All the printers installed on the OpenPrinting CUPS server appear, including
the newly updated: **DYMO LabelWriter 450 DUO Label** (or whichever DYMO
printer model is being used). Click into the printer that was just updated.

To print a test label, click on the **Maintenance** drop-down menu to the left
of the **Administration** drop-down menu, and select **Print Test Page**. The
test label will print out with a ten-second delay if the driver update was
successful.

![Printing a test page from the administration drop-down menu in the
OpenPrinting CUPs server.](../../../../_images/print-test.png)

To reduce this delay a new printer will need to be added, follow the process
below.

#### DYMO LabelWriter print delay

To resolve the delay issue after modifying the driver, the printer **must** be
reinstalled. To reinstall the printer, open the OpenPrinting CUPS
administration page by clicking Printers server, at the bottom of the IoT box
homepage. Then, click on Administration in the top menu, then click **Add a
Printer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>2 ![Add a printer button highlighted on the Printer CUPS
management page.](../../../../_images/add-printer-dymo.png)

On the next screen, in the **Local Printers** section, select the **DYMO
LabelWriter 450 DUO Label (DYMO LabelWriter 450 DUO Label)** (or whichever
DYMO printer model is being used) pre-installed printer. Click **Continue**.

![Add a printer screen on OpenPrinting CUPS with DYMO LabelWriter 450 DUO
Label highlighted.](../../../../_images/local-printer.png)

On the following screen, modify the **Name** to something recognizable, as the
original printer will still be present. Click **Continue** to be taken to the
next screen.

![Rename printer page in the 'Add a Printer' flow, with the name field
highlighted.](../../../../_images/rename-printer.png)

Next, choose the **Model**. Select **DYMO LabelWriter 450 DUO Label (en)** (or
whichever DYMO printer model is being used), and finally, click **Add
Printer** to complete the installation.

![Choose model screen on the OpenPrinting CUPS console with model and add a
printer highlighted.](../../../../_images/choose-printer.png)

After being redirected to a confirmation page, acknowledging a successful
installation, click on the Printers button in the top menu.

All the printers installed on the OpenPrinting CUPS server appear, including
the newly installed: **DYMO LabelWriter 450 DUO Label** (or whichever DYMO
printer model is being used). Click into the printer that was just installed.

![Printer page with newly installed printer
highlighted.](../../../../_images/printer-page.png)

To print a test label, click on the **Maintenance** drop-down menu to the left
of the **Administration** drop-down menu, and select **Print Test Page**. The
test label should print out immediately (one-to-two seconds delay).

![Printing a test page from the administration drop-down menu in the
OpenPrinting CUPs server.](../../../../_images/print-test.png)

### The Zebra printer does not print anything

Les imprimantes Zebra sont très sensibles au format du code Zebra Programming
Language (ZPL) qui est imprimé. Si l’imprimante n’imprime rien ou des
étiquettes vierges, essayez de modifier le format du rapport qui est envoyé à
l’imprimante en accédant aux Paramètres ‣ Technique ‣ Interface utilisateur ‣
Vues en [mode développeur](../../developer_mode#developer-mode) et
recherchez le modèle correspondant.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>3

## Lecteur de codes-barres

### The characters read by the barcode scanner do not match the barcode

Par défaut, la plupart des lecteurs de codes-barres sont configurés au format
QWERTY américain. Si le lecteur de codes-barres utilise une disposition
différente, allez à la vue formulaire de l’appareil (IoT ‣ Périphériques ‣
Lecteur de codes-barres) et sélectionnez le bon format.

### Rien ne se passe lorsqu’un code-barres est scanné

Assurez-vous que vous avez sélectionné le bon périphérique dans la
configuration du Point de Vente et que le code-barres est configuré pour
envoyer un caractère `ENTER` (keycode 28) à la fin de chaque code-barres. Pour
ce faire, allez à l’application Point de Vente ‣ Menu trois points sur le PdV
‣ Section IoT Box ‣ Modifier.

### Le lecteur de codes-barres est détecté comme un clavier

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>4

Vous pouvez manuellement modifier le type de périphérique en allant à sa fiche
(IoT ‣ Périphériques ‣ Lecteur de codes-barres) et en activant l’option **Est
un lecteur**.

![Modifiez le formulaire du lecteur de codes-
barres](../../../../_images/barcode-scanner-settings.png)

### Barcode scanner processes barcode characters individually

When accessing the mobile version of Konvergo ERP from a mobile device, or tablet,
paired with a barcode scanner, via the IoT box, the scanner may process each
barcode character as an individual scan. In this case, the _Keyboard Layout_
option **must** be filled out with the appropriate language of the barcode
scanner on the _Barcode Scanner_ form page.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>5 ![Barcode scanner form page, with keyboard layout option
highlighted.](../../../../_images/keyboard-layout.png)

The **Keyboard Layout** is language based, and the options available vary,
depending on the device and the language of the database. For example:
**English (UK)** , **English (US)** , etc.

## Tiroir caisse

### Le tiroir caisse ne s’ouvre pas

Le tiroir caisse doit être connecté à l’imprimante et la case de **Tiroir
caisse** doit être cochée dans la configuration du PdV. Pour ce faire,
naviguez à l’application Point de Vente ‣ Menu trois points sur le PdV ‣
Section IoT Box ‣ Modifier ‣ Imprimante de reçu ‣ Case à cocher du tiroir
caisse.

## Balance

Scales play a crucial role in the checkout process, especially for products
sold by weight, rather than fixed pricing.

### Set up Ariva S scales

Konvergo ERP has determined that a specific setting in Ariva S series scales
(manufactured by Mettler-Toledo, LLC.) needs modification, and a dedicated
Mettler USB-to-proprietary RJ45 cable is required for the scale to function
with Konvergo ERP’s IoT box.

To correctly configure the scale for recognition by the IoT box, follow this
setup process for the Ariva S series scales.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>6

#### Cable

The Mettler part number is 72256236 - USB-to-POS cable. Contact Mettler, or a
partner, to purchase an authentic cable. Note that **no other** cable outside
of this Mettler cable works for this configuration. Using a serial-only cable
attached to a serial-to-USB adapter is **not** effective.

![Authentic Mettler USB to POS cable, part number
72256236.](../../../../_images/cable-mettler.png)

#### Configuration

Refer to Mettler’s Setup Guide for Ariva S series scales during the following
configuration: [Ariva Checkout Scale User’s
Guide](https://www.mt.com/dam/RET_DOCS/Ariv.pdf).

To begin, go to page 17 in the above manual for _Setup_. This guide lists
potential settings for the Ariva S series scales.

Follow the instructions, along with the following process, to set the scale to
setup mode. First, hold the **> T<** button for eight seconds, or until
**CONF** appears.

Next, press **> T<** until **GRP 3** appears, then press **> 0<** to confirm.

Under **3.1** , ensure the setting is set to **1** (USB Virtual COM ports).
Press **> T<** to cycle through the options under group 3.1.

Once **3.1** is set to **1** , press **> 0<** to confirm the selection.
Continue to press **> 0<** until **GRP 4** appears.

Now, press **> T<** until **EXIT** appears.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote n’est sélectionné pour ces imprimantes.</p>
</div>7

Once **EXIT** appears, press **> 0<**. Following this, press **> 0<** again to
**SAVE**. Now the scale restarts.

Finally, restart the IoT box to recognize the changes made on the scale’s
configuration. After restarting, the scale appears as `Toledo 8217`, as
opposed to the previous display, where it appeared as `Adam Equipment Serial`.

  *[IoT]: Internet of Things
  *[HTTPS]: Hypertext Transfer Protocol Secure
  *[PdV]: Point of Sale
  *[PoS]: Point of Sale)`configuration as the :abbr:`IoT (Internet of Things
  *[USB]: Universal Serial Bus
  *[POS]: Point of Sale

