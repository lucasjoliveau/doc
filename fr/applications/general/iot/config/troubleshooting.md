# Aide au dépannage

## Connexion à l’IoT box

### Je ne trouve pas le code d’appariement pour connecter l’IoT box

Le code d’appariement doit être imprimé sur les imprimantes de reçu connectées
à l”IoT box et doit également s’afficher sur les moniteurs connectés.

The pairing code does not show under the following circumstances:

  * L”IoT box est déjà connectée à une base de données Odoo.

  * L”IoT box n’est pas connectée à Internet.

  * The code is only valid for 5 minutes after the IoT box has started. It is automatically removed from connected displays when this time has expired.

  * The version of the IoT box image is too old. If the IoT box image is from an earlier version, then the SD card of the IoT box needs to be re-flashed to update the image (see [Flashing the SD Card](updating_iot.html#iot-config-flash)).

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

### L’IoT box est connectée à la base de données Odoo, mais n’est pas
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

Pour plus d'infos

[certificat HTTPS (IoT)](https_certificate_iot.html)

## Imprimante

### L’imprimante n’est pas détectée

If a printer does not appear in the devices list, go to the IoT box homepage
and make sure that it is listed under Printers.

![La page d'accueil de l'IoT box.](../../../../_images/printer-status.png)

If the printer is not present on the IoT box homepage, click Printers Server,
go to the Administration tab and click on Add Printer. If the printer is not
present in the list, it is likely not connected properly.

### L’imprimante produit un texte aléatoire

Pour la plupart des imprimantes, le bon pilote est automatiquement détecté et
sélectionné. Cependant, dans certains cas, il se peut que le mécanisme de
détection automatique ne soit pas suffisant et que, si aucun pilote n’est
trouvé, l’imprimante puisse imprimer des caractères aléatoires.

The solution is to manually select the corresponding driver. On the IoT box
homepage, click on Printers Server, go to the Printers tab and select the
printer in the list. In the Administration drop-down menu, click on Modify
Printer. Follow the steps and select the _make_ and _model_ corresponding to
the printer.

![Modifiez l'imprimante connectée à l'IoT box.](../../../../_images/modify-
printer.png)

Note

Les imprimantes de reçu Epson et Star et les imprimantes d’étiquettes Zebra
n’ont pas besoin de pilote pour fonctionner. Assurez-vous qu’aucun pilote
n’est sélectionné pour ces imprimantes.

#### Cas particulier de la configuration Epson

La plupart des imprimantes Epson prennent en charge l’impression de reçus dans
Odoo PdV à l’aide de la commande `GS v 0`. Cependant, les modèles
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

Pour plus d'infos

  * [Documentation Epson GS v 0](https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=94) pour les imprimantes compatibles avec `GS v 0`.

  * [Documentation Epson ESC *](https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=88) pour les imprimantes compatibles avec `ESC *`.

Si l’imprimante n’est pas compatible avec la commande `ESC *`, le processus
suivant n’est pas possible. Si l’imprimante est compatible avec la commande
`ESC *` pour imprimer, suivez cette procédure pour configurer l’imprimante
avec l”IoT box.

###### Configuration de l’IoT box pour ESC *

Pour configurer l”IoT box pour qu’elle utilise la commande `ESC *` pour
imprimer, allez à la page d’accueil de l”IoT box en allant à l’application IoT
‣ IoT Box. Cliquez ensuite sur l”adresse IP et vous serez redirigé vers la
page d’accueil de l”IoT box.

**Choix de l’imprimante**

Cliquez maintenant sur le bouton Serveur d’imprimantes. Le navigateur sera
redirigé vers la page _CUPS_. Allez ensuite à Administration ‣ Imprimantes ‣
Ajouter une imprimante, choisissez l’imprimante qui doit être modifiée et
cliquez sur Continuer.

Astuce

Si le nom de l’imprimante n’est toujours pas connu, suivez les étapes
suivantes :

  1. Prenez note des imprimantes répertoriées sur la page _CUPS_.

  2. Éteignez l’imprimante et actualisez la page.

  3. Voyez maintenant s’il y a une différence avec la première liste pour voir quelle imprimante a disparu.

  4. Remettez l’imprimante sous tension et actualisez à nouveau la page.

  5. Vérifiez à nouveau la liste pour voir si l’imprimante réapparaît.

  6. L’imprimante qui disparaît et qui réapparaît dans la liste des imprimantes est le nom de l’imprimante en question.

Note

Il peut s’agir d”Inconnu dans Imprimantes locales.

**Convention d’appellation de CUPS**

`CUPS` will prompt the administrator for three pieces of information: the
Name, Description and the Location. The last two pieces of information do not
need to be specific, however, the Name should follow a particular convention
to work with the `ESC *` command.

Le Nom doit correspondre à cette convention :
`<printer_name>__IMC_<param_1>_<param_2>_..._<param_n>__`

Détail de la convention d’appellation :

  * `printer_name` : Il s’agit du nom de l’imprimante. Il peut être composé de n’importe quel caractère tant qu’il ne contient pas `_`, `/`, `#`, or ` ` (caractère espace).

  * `IMC` : C’est l’abréviation d” _Image Mode Column_ (nom simplifié de `ESC *`).

  * `param_1` : Il s’agit du paramètre spécifique :

    * `SCALE<X>` : Échelle de l’image (avec le même rapport d’aspect). `X` doit être un entier décrivant le pourcentage d’échelle à utiliser.

Example

`100` est la taille originale, `50` est la moitié de la taille et `200` est le
double de la taille.

    * `LDV` : _Faible densité verticale_ (sera défini sur _Densité verticale élevée_ si ce n’est pas précisé).

    * `LDH` : _Faible densité horizontale_ (sera défini sur _Densité horizontale élevée_ si ce n’est pas précisé).

Note

Il se peut que les paramètres de _densité_ doivent être configurés d’une
manière particulière en fonction du modèle d’imprimante.

Pour plus d'infos

Consultez la [documentation d’Epson relative à ESC *](https://reference.epson-
biz.com/modules/ref_escpos/index.php?content_id=88) et cliquez sur le modèle
d’imprimante dans le tableau ci-dessus pour voir si l’imprimante doit définir
ces paramètres.

Example

Voici des exemples de formatage de nom correct et incorrect :

Formatage de nom correct :

  * `EPSONTMm30II__IMC__`

  * `EPSON_TM_U220__IMC_LDV_LDH_SCALE80__`

Formatage de nom incorrect (cela n’empêche pas l’impression, mais le résultat
risque de ne pas être celui attendu) :

  * `EPSON TMm 30II` -> The name cannot have spaces.

  * `EPSONTMm30II` -> The name itself is correct, but it will not use `ESC *`.

  * `EPSONTMm30II__IMC` -> Il manque la fin `__` à ce nom.

  * `EPSONTMm30II__IMC_XDV__` -> Le paramètre `XDV` ne correspond à aucun paramètre existant.

  * `EPSONTMm30II__IMC_SCALE__` -> Il manque la valeur d’échelle du paramètre `SCALE`.

**Terminer l’ajout d’une imprimante**

Après avoir configuré le nom de l’imprimante avec la bonne convention
d’appellation, cliquez sur Continuer. Définissez ensuite la valeur Marque sur
Raw et la valeur Modèle sur Raw Queue (en).

Après avoir complété ces étapes, cliquez sur Ajouter une imprimante. Si la
configuration a été faite correctement, la page devrait rediriger vers la page
_Bannières_.

À ce stade, l’imprimante doit être créée. Il suffit maintenant que l”IoT la
détecte et se synchronise avec le serveur Odoo (cela peut prendre quelques
minutes).

**Ajout de l’imprimante à Odoo PdV**

Once the printer is visible on the Odoo database, do not forget to choose it
in the PoS printer. Navigate to Pos App ‣ Settings ‣ Connected Devices ‣ IoT
Box ‣ Receipt Printer ‣ Save.

Note

Si l’imprimante a été mal configurée (elle imprime toujours un texte aléatoire
ou le reçu imprimé est trop grand ou trop petit), elle ne peut pas être
modifiée via le nom de l’imprimante avec _CUPS_. En revanche, vous pouvez
répéter la procédure susmentionnée pour configurer une autre imprimante à
partir de zéro et en créer une avec des paramètres modifiés.

**Exemple de configuration de l’imprimante Epson TM-U220B à l’aide de ESC**

Click this text to reveal the example

Voici un exemple de processus de dépannage pour un modèle d’imprimante
TM-U220B à l’aide de la commande `ESC *`. Le reçu suivant est un exemple de
reçu qui s’imprime correctement grâce à un formatage adéquat (en théorie) :

![Image d'un reçu correctement formaté d'une base de données de
démonstration.](../../../../_images/receipt-example.png)

Essayer d’imprimer le reçu immédiatement avant le formatage correct ne
fonctionnera pas, car le modèle d’imprimante TM-U220B ne prend pas en charge
`GS v 0`. Il imprimera plutôt des caractères aléatoires :

![Papier d'impression avec des caractères apparemment
aléatoires.](../../../../_images/receipt-print-random-letters.png)

Pour correctement configurer le formatage pour le modèle Epson TM-U220B,
suivez les étapes suivantes :

Après avoir consulté le site web d’Epson pour vérifier la compatibilité des
deux commandes : [GS v 0](https://reference.epson-
biz.com/modules/ref_escpos/index.php?content_id=94) et [ESC
*](https://reference.epson-
biz.com/modules/ref_escpos/index.php?content_id=88), vous pouvez voir que le
modèle TM-U220B n’est pas compatible avec `GS v 0`, mais qu’il l’est avec `ESC
*`.

![Évaluation de la compatibilité d'Epson à partir du site web
d'Epson.](../../../../_images/epson-compatibility-compare.png)

Lors de l’ajout de l’imprimante, _CUPS_ demande quelle imprimante doit être
ajoutée :

![Menu Administration, sélection de l'imprimante à
ajouter.](../../../../_images/add-printer.png)

Dans ce cas, l’imprimante est connectée via USB et ne fait donc pas partie des
Imprimantes réseau découvertes. Elle fait probablement partie de la sélection
Inconnu dans Imprimantes locales. En débranchant le câble USB de l’imprimante
de l”IoT box et en actualisant la page, l’imprimante Inconnu disparaît. En la
rebranchant, l’imprimante réapparaît, donc on peut confirmer qu’il s’agit de
l’imprimante en question.

For the naming convention, since it needs to print using the `ESC *` command,
it is imperative to add `__IMC`. Reference the printer model on [Epson’s ESC *
site](https://reference.epson-
biz.com/modules/ref_escpos/index.php?content_id=88) to find out more about the
_density_ parameters.

![Spécifications de l'imprimante Epson TM-U220 sur le site web du
fabricant.](../../../../_images/epson-tm-u220-specification.png)

Pour ce modèle en particulier, TM-U220, `m` doit être égal à 0 ou 1. En se
référant à la Description sous l’encadré rose dans l’image ci-dessus, les
valeurs `m` doivent être 0, 1, 32 ou 33. Donc dans le cas de cette imprimante,
la valeur `m` ne peut PAS être 32 ou 33 (sinon, des caractères aléatoires
seront imprimés).

Le tableau comprend les valeurs numériques : 32 et 33, qui se produisent
toutes deux si le Nombre de bits pour les données verticales est défini sur
24. Ceci signifie que la _densité verticale est élevée_. Dans le cadre de la
configuration de l’imprimante Epson TM-U220, la _faible densité verticale_
doit être forcée, car ce modèle d’imprimante ne prend pas en charge la
_densité verticale élevée_ pour cette commande `ESC *`.

Pour ajouter une _Faible densité verticale_ , ajoutez le paramètre `LDV` à la
convention d’appellation.

![Ajoutez une *Faible densité verticale* \(le paramètre `LDV`\)  à la
convention d'appellation.](../../../../_images/add-printer-filled.png)

Cliquez sur Continuer pour continuer. Définissez ensuite la valeur Marque sur
Raw et la valeur Modèle sur Raw Queue (en).

![Spécifications de l'imprimante Epson TM-U220 sur le site web du
fabricant.](../../../../_images/add-printer-add.png)

However, when trying to print with the naming convention:
`EpsonTMU220B__IMC_LDV__`, it prints the receipt, but it is too big and
outside the margin. To resolve this, add a new printer (and naming convention)
with the `SCALE<X>` parameter to adapt to our receipt size.

Voici quelques exemples :

Convention d’appellation de l’imprimante | `EpsonTMU220B__IMC_LDV__` | `EpsonTMU220B__IMC_LDV_SCALE75__` | `EpsonTMU220B__IMC_LDV_LDH__` | `EpsonTMU220B__IMC_LDV_LDH_SCALE35__`  
---|---|---|---|---  
![Exemple de format de reçu.](../../../../_images/receipt-example.png) | ![Format de reçu utilisant la convention d'appellation : EpsonTMU220B__IMC_LDV__.](../../../../_images/tm-u220-ldv.png) | ![Format de reçu utilisant la convention d'appellation : EpsonTMU220B__IMC_LDV_SCALE75__.](../../../../_images/tm-u220-ldv-scale75.png) | ![Format de reçu utilisant la convention d'appellation : EpsonTMU220B__IMC_LDV_LDH__.](../../../../_images/tm-u220-ldv-hdv.png) | ![Format de reçu utilisant la convention d'appellation : EpsonTMU220B__IMC_LDV_LDH_SCALE35__.](../../../../_images/tm-u220-ldv-hdv-scale35.png)  
  
### DYMO LabelWriter print issue

The DYMO LabelWriter has a known issue in printing with the IoT box. The
OpenPrinting CUPS server installs the printer using Local RAW Printer drivers.
In order to print anything, the correct Make and Model needs to be set, so the
correct driver is referenced when using the device.

Additionally, a new printer needs to be added to reduce a print delay that
occurs after updating the driver.

Important

The DYMO LabelWriter 450 DUO printer is the recommended DYMO printer for use
with Odoo and the IoT box. It **must** already be connected to, and recognized
on, the IoT box.

The DYMO LabelWriter 450 DUO printer contains two printers in one: a label
printer and a tape printer. Choosing the correct model (either DYMO
LabelWriter 450 DUO Label (en) or DYMO LabelWriter 450 DUO Tape (en)) is
crucial when configuring the following processes.

To keep things consistent, both of the following processes detail the
configuration for the DYMO LabelWriter 450 DUO Label (en) model. Change the
model when needed.

#### DYMO LabelWriter not printing

In the case where the DYMO LabelWriter is not printing anything, a new driver
needs to be installed.

First, open the OpenPrinting CUPS console by clicking Printers server at the
bottom of the IoT box homepage. Next, click on Printers in the top menu. Click
into the printer in question, and select Maintenance in the first drop-down
menu. Then, select Modify Printer in the second drop-down menu.

![Modify the make and model of the DYMO LabelWriter. Maintenance and Modify
drop-down menus highlighted.](../../../../_images/main-modify.png)

Next, select the specific network connection/printer that the modification
should be made on. Click Continue.

![Printer selection screen with Continue
highlighted.](../../../../_images/modify-select-printer.png)

On the next page, click Continue to proceed to set the Make of the printer.

![Printer modification screen with Continue
highlighted.](../../../../_images/modify-printer-dymo.png)

Under Make select DYMO from the menu. Click on Continue to set the Model.

![Setting the make page, with DYMO and continue
highlighted.](../../../../_images/setting-make.png)

On the following page, set the Model to DYMO LabelWriter 450 DUO Label (en)
(or whichever DYMO printer model is being used). Click on Modify Printer to
complete setting the new driver, a confirmation page will appear.

![Setting the printer model page with DYMO LabelWriter 450 DUO Label \(en\)
highlighted.](../../../../_images/setting-model.png)

After being redirected to a confirmation page, acknowledging a successful
update, click on the Printers button in the top menu.

All the printers installed on the OpenPrinting CUPS server appear, including
the newly updated: DYMO LabelWriter 450 DUO Label (or whichever DYMO printer
model is being used). Click into the printer that was just updated.

To print a test label, click on the Maintenance drop-down menu to the left of
the Administration drop-down menu, and select Print Test Page. The test label
will print out with a ten-second delay if the driver update was successful.

![Printing a test page from the administration drop-down menu in the
OpenPrinting CUPs server.](../../../../_images/print-test.png)

To reduce this delay a new printer will need to be added, follow the process
below.

#### DYMO LabelWriter print delay

To resolve the delay issue after modifying the driver, the printer **must** be
reinstalled. To reinstall the printer, open the OpenPrinting CUPS
administration page by clicking Printers server, at the bottom of the IoT box
homepage. Then, click on Administration in the top menu, then click Add a
Printer.

Astuce

If the DYMO LabelWriter 450 DUO printer is not printing at all, or is not
recognizable (has a RAW driver type), then update the drivers on the device.
See DYMO LabelWriter not printing.

![Add a printer button highlighted on the Printer CUPS management
page.](../../../../_images/add-printer-dymo.png)

On the next screen, in the Local Printers section, select the DYMO LabelWriter
450 DUO Label (DYMO LabelWriter 450 DUO Label) (or whichever DYMO printer
model is being used) pre-installed printer. Click Continue.

![Add a printer screen on OpenPrinting CUPS with DYMO LabelWriter 450 DUO
Label highlighted.](../../../../_images/local-printer.png)

On the following screen, modify the Name to something recognizable, as the
original printer will still be present. Click Continue to be taken to the next
screen.

![Rename printer page in the 'Add a Printer' flow, with the name field
highlighted.](../../../../_images/rename-printer.png)

Next, choose the Model. Select DYMO LabelWriter 450 DUO Label (en) (or
whichever DYMO printer model is being used), and finally, click Add Printer to
complete the installation.

![Choose model screen on the OpenPrinting CUPS console with model and add a
printer highlighted.](../../../../_images/choose-printer.png)

After being redirected to a confirmation page, acknowledging a successful
installation, click on the Printers button in the top menu.

All the printers installed on the OpenPrinting CUPS server appear, including
the newly installed: DYMO LabelWriter 450 DUO Label (or whichever DYMO printer
model is being used). Click into the printer that was just installed.

![Printer page with newly installed printer
highlighted.](../../../../_images/printer-page.png)

To print a test label, click on the Maintenance drop-down menu to the left of
the Administration drop-down menu, and select Print Test Page. The test label
should print out immediately (one-to-two seconds delay).

![Printing a test page from the administration drop-down menu in the
OpenPrinting CUPs server.](../../../../_images/print-test.png)

### The Zebra printer does not print anything

Les imprimantes Zebra sont très sensibles au format du code Zebra Programming
Language (ZPL) qui est imprimé. Si l’imprimante n’imprime rien ou des
étiquettes vierges, essayez de modifier le format du rapport qui est envoyé à
l’imprimante en accédant aux Paramètres ‣ Technique ‣ Interface utilisateur ‣
Vues en [mode développeur](../../developer_mode.html#developer-mode) et
recherchez le modèle correspondant.

Pour plus d'infos

Consultez les instructions de Zebra relatives à l’impression des fichiers ZPL
[ici](https://supportcommunity.zebra.com/s/article/Print-a-zpl-file-using-the-
Generic-Text-Printer).

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

Important

Certains lecteurs de codes-barres ne s’affichent pas comme des lecteurs de
codes-barres, mais comme des claviers USB et ne seront pas reconnus par l”IoT
box.

Vous pouvez manuellement modifier le type de périphérique en allant à sa fiche
(IoT ‣ Périphériques ‣ Lecteur de codes-barres) et en activant l’option Est un
lecteur.

![Modifiez le formulaire du lecteur de codes-
barres](../../../../_images/barcode-scanner-settings.png)

### Barcode scanner processes barcode characters individually

When accessing the mobile version of Odoo from a mobile device, or tablet,
paired with a barcode scanner, via the IoT box, the scanner may process each
barcode character as an individual scan. In this case, the _Keyboard Layout_
option **must** be filled out with the appropriate language of the barcode
scanner on the _Barcode Scanner_ form page.

Astuce

Access the barcode scanner form page by navigating to IoT App ‣ Devices ‣
Barcode Scanner.

![Barcode scanner form page, with keyboard layout option
highlighted.](../../../../_images/keyboard-layout.png)

The Keyboard Layout is language based, and the options available vary,
depending on the device and the language of the database. For example: English
(UK), English (US), etc.

## Tiroir caisse

### Le tiroir caisse ne s’ouvre pas

Le tiroir caisse doit être connecté à l’imprimante et la case de Tiroir caisse
doit être cochée dans la configuration du PdV. Pour ce faire, naviguez à
l’application Point de Vente ‣ Menu trois points sur le PdV ‣ Section IoT Box
‣ Modifier ‣ Imprimante de reçu ‣ Case à cocher du tiroir caisse.

## Balance

Scales play a crucial role in the checkout process, especially for products
sold by weight, rather than fixed pricing.

### Set up Ariva S scales

Odoo has determined that a specific setting in Ariva S series scales
(manufactured by Mettler-Toledo, LLC.) needs modification, and a dedicated
Mettler USB-to-proprietary RJ45 cable is required for the scale to function
with Odoo’s IoT box.

To correctly configure the scale for recognition by the IoT box, follow this
setup process for the Ariva S series scales.

Important

It is crucial to use the official Mettler USB-to-RJ45 cable during this
process.

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
setup mode. First, hold the **> T<** button for eight seconds, or until CONF
appears.

Next, press **> T<** until GRP 3 appears, then press **> 0<** to confirm.

Under 3.1, ensure the setting is set to 1 (USB Virtual COM ports). Press **>
T<** to cycle through the options under group 3.1.

Once 3.1 is set to 1, press **> 0<** to confirm the selection. Continue to
press **> 0<** until GRP 4 appears.

Now, press **> T<** until EXIT appears.

Important

Do **not** make any other changes unless otherwise needed.

Once EXIT appears, press **> 0<**. Following this, press **> 0<** again to
SAVE. Now the scale restarts.

Finally, restart the IoT box to recognize the changes made on the scale’s
configuration. After restarting, the scale appears as `Toledo 8217`, as
opposed to the previous display, where it appeared as `Adam Equipment Serial`.

  *[IoT]: Internet of Things
  *[HTTPS]: Hypertext Transfer Protocol Secure
  *[PdV]: Point of Sale
  *[PoS]: Point of Sale)`configuration as the :abbr:`IoT (Internet of Things
  *[USB]: Universal Serial Bus
  *[ZPL]: Zebra Programming Language
  *[POS]: Point of Sale

