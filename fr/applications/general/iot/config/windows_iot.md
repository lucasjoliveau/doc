# Connecter Windows pour l’IoT à Odoo

Une IoT Box Virtuelle est un logiciel qui doit être téléchargé et installé sur
un ordinateur Windows et requiert un système d’exploitation Windows avec une
base de données Odoo 16 ou ultérieure.

L”IoT box virtuelle de Windows fonctionne de la même manière qu’une IoT box
physique, avec la capacité de faire fonctionner la plupart des mêmes
appareils. Tous les appareils de PdV fonctionnent avec elle, comme une balance
ou une imprimante. Les terminaux de paiement fonctionnent également, mais il
convient de noter que les appareils MRP ne sont pas compatibles. _Il s’agit
notamment de caméras ou d’outils de mesure._

## Prérequis

Les éléments suivants sont nécessaires pour compléter l’installation de
Windows pour l”IoT.

  * Base de données Odoo 16 ou toute version ultérieure.

  * Appareils compatibles avec l”IoT (à l’exception de ceux mentionnés ci-dessus). Consultez [Appareils IoT compatibles avec Odoo](https://www.odoo.com/app/iot-hardware).

  * Pilotes de périphériques pour Windows.

Note

Odoo recommande d’utiliser une version récente et mise à jour de Windows
(Windows 10/11), car certains systèmes d’exploitation plus anciens peuvent
empêcher le fonctionnement de l”IoT virtuelle de Windows.

  * Ordinateur Windows (portable, ordinateur de bureau ou serveur).

  * Abonnement à Odoo IoT. Consultez [Éligibilité à l’Internet des objets (IoT)](https_certificate_iot.html#iot-iot-eligibility).

## Connect the Windows virtual IoT box to an Odoo database

L’IoT Box virtuelle de Windows est facile à configurer en quelques étapes
faciles. Suivez cette procédure lors de l’installation du logiciel virtuel
Windows pour l’IoT pour la première fois.

### Téléchargement et installation initiale

To begin the installation, navigate to the Odoo 16 or higher installation
package for Community - Windows edition at [Odoo’s download
page](https://odoo.com/download). Next, install and setup the Odoo `.exe`
file. After the instructions screen, click Next to start the installation and
agree to the TOS.

During the next step of the installation, select Odoo IoT from the Select the
type of install drop-down menu.

Example

Pour référence, les éléments suivants doivent être installés :

  * **Serveur Odoo**

  * **Odoo IoT**

  * **Nginx WebServer**

  * **Interpréteur Ghostscript**

Assurez-vous qu’il y a suffisamment d’espace sur l’ordinateur pour
l’installation et cliquez sur Suivant.

### Définir la destination et finaliser l’installation

Pour terminer l’installation, sélectionnez le dossier de destination et
cliquez sur Installer.

Astuce

Choisir `C:\odoo` comme emplacement d’installation permettra au serveur Nginx
de démarrer. Si le dossier n’existe pas, créez-le. Sinon, les fichiers
d’installation seront dispersés sur le disque dur.

Avertissement

Odoo’s Windows virtual IoT software should not be installed inside any of the
Window’s User’s directories. Doing so will not allow for Nginx to initialize.

L’installation peut prendre quelques minutes. Une fois l’installation
terminée, cliquez sur Suivant pour continuer.

Ensure that the Start Odoo box is checked and click Finish. After
installation, the Odoo server will run and automatically open
`http://localhost:8069` on a web browser. The webpage should display the IoT
box homepage.

Pour plus d'infos

Un redémarrage du programme Windows IoT peut être nécessaire si le navigateur
web n’affiche rien. Redémarrer l’IoT box de Windows

### Connecter des appareils

Ensuite, connectez les appareils IoT à l’ordinateur Windows. Windows devrait
détecter automatiquement l’appareil, car le pilote est préinstallé sur
l’ordinateur. Si ce n’est pas le cas, recherchez et installez le pilote
Windows de l’appareil.

Important

Most devices connect to the Windows Machine for Windows IoT automatically
through Windows Plug-N-Play (PnP). However, if Windows does not automatically
recognize the device after connecting, then the administrator may need to
install the corresponding drivers manually.

Devices automatically recognized:

  * Regular ink/toner based printers

  * Receipt printers (Epson/Star)

  * Lecteurs de codes-barres

  * Measurement devices (although some configuration of the measurement device settings is required) See this documentation: [Connecter un outil de mesure](../devices/measurement_tool.html)

Devices not automatically recognized (requires manual driver download):

  * Label printers (Zebra)

  * Balances

Reference the manufacturer’s website for the equipment in question. Then,
download the drivers and install them on the Windows machine. Reconnect the
device in question and Windows will find the device.

Après avoir connecté les appareils à l’ordinateur, actualisez la page
d’accueil de l”IoT box et vérifiez que l’appareil est visible. Si ce n’est pas
le cas, rechargez les gestionnaires via la page d’accueil de l”IoT box.

Finalement, connectez Windows pour l”IoT à une base de données en suivant les
instructions existantes (manuellement à l’aide du jeton).

Pour plus d'infos

[Connecter une IoT box à Odoo](connect.html)

Maintenant que l’installation est terminée, les appareils connectés à l”IoT
peuvent être utilisés pour exécuter des processus/actions.

## Aide au dépannage

### Redémarrer l’IoT box de Windows

Dans certains cas, un redémarrage manuel de l”IoT box physique peut résoudre
le problème d’une IoT box qui n’apparaît pas dans la base de données. Pour
l”IoT box virtuelle de Windows, un redémarrage manuel du serveur Odoo peut
résoudre les problèmes de connexion à la base de données.

Pour redémarrer le serveur IoT virtuel de Windows :

  1. Tapez `Services` dans la barre de recherche dans Windows.

  2. Sélectionnez l’application Services et faites défiler jusqu’au service Odoo.

  3. Cliquez droit sur Odoo et sélectionnez Démarrer ou Redémarrer. Cette action redémarrera manuellement le serveur IoT d’Odoo.

### Pare-feu

Les pare-feu assurent la sécurité des appareils. Parfois, ils peuvent bloquer
des connexions qui devraient pourtant être établies. Le logiciel de l”IoT box
virtuelle de Windows peut ne pas être accessible au LAN en raison d’un pare-
feu empêchant la connexion. Consultez votre équipe d’assistance technique
locale pour créer des exceptions (découverte du réseau) dans le système
d’exploitation ou le programme de pare-feu. Windows a son propre pare-feu,
tout comme d’autres programmes de protection contre le virus.

Example

Il peut arriver qu’un client soit en mesure d’accéder à la page d’accueil de
l”IoT box, mais qu’il ne puisse pas y accéder à partir d’un autre ordinateur,
d’un autre appareil mobile, d’une tablette sur le même réseau.

#### Créer une exception dans Windows Defender

It is possible to allow other devices to access the Windows virtual IoT box
while keeping the firewall on. This is done by creating a rule on _Windows
Defender_ and allowing communication through port `8069`. The following
process describes the steps to take in order to make this exception.

##### Créer une règle dans Windows Defender

Ouvrez d’abord le _pare-feu Windows_ en allant au menu Démarrer et en tapant
`Pare-feu`. Ensuite, ouvrez le programme Pare-feu Windows Defender. Dans le
menu de gauche, cliquez sur Paramètres avancés.

Une fois les paramètres avancés sélectionnés, cliquez sur Règles de trafic
entrant dans le menu de gauche. Ensuite, dans la colonne de droite du menu
(sous Règles de trafic entrant), cliquez sur Nouvelle règle pour créer une
nouvelle règle.

##### Configurer une nouvelle règle

On the Rule Type screen, select Port. Then click Next. From the Protocol and
Ports page leave the rule application to TCP. Then, select Specific Local
Ports for the ports option. In the text box, type in `8069, 443`. Finally,
click Next to continue to the next step.

Sur la page Actions, sélectionnez Autoriser la connexion et cliquez sur
Suivant. La page suivante de l’assistant de Configuration de la règle est la
page de Profil. Sur cette page, sélectionnez le type de connexion qui
s’applique au réseau sur lequel la machine Windows fonctionne. Dans l’idéal,
sélectionnez Connexions privées uniquement. Le type de connexion _Privée_ est
la connexion la plus sûre tout en permettant au port sélectionné de
communiquer. Cliquez sur Suivant pour continuer.

Enfin, attribuez un nouveau nom unique à la règle. Par exemple, ce nom peut
être `Odoo`. Vous pouvez également ajouter une brève description dans le champ
Description. Cliquez sur Terminer pour finaliser l’assistant de Configuration
de la règle. La nouvelle règle est désormais active et des appareils peuvent
être connectés à l”IoT box virtuelle de Windows.

#### Worldline exception

_Worldline_ is a payment terminal that can be connected to Odoo’s _PoS_ (point
of sale) system. It allows for a comprehensive and fluid payment experience
for customers. Worldline is available in Belgium, the Netherlands, and
Luxembourg.

When using the Windows IoT server to connect the Worldline payment terminal,
it is necessary to create an exception in the Windows firewall so that a
connection can be made between the Odoo database/IoT box and Worldline.

Pour plus d'infos

[Worldline](../../../sales/point_of_sale/payment_methods/terminals/worldline.html)

To create the exception, first, open the _Windows Defender Firewall_ app on
the Windows machine. This can be accomplished by typing `windows defender` in
the Search bar.

Next, click Advanced settings in the left menu.

![Advanced settings option highlighted in the left pane of the Windows
Defender Firewall app.](../../../../_images/advanced-settings.png)

In the left menu, choose Inbound Rules.

![Windows Defender left window pane with inbound rules menu item
highlighted.](../../../../_images/inbound-rules.png)

After selecting Inbound Rules, select New Rule in the far right menu.

![New rule dropdown shown with new rule option
highlighted.](../../../../_images/new-rule.png)

Then, for the Rule Type, select the radio button for Port. Click Next to
continue to the rest of the configuration.

![Rule Type window open, with the radio button next to port
highlighted.](../../../../_images/radio-port.png)

On the Protocols and Ports page, choose the radio button for TCP, under Does
this rule apply to TCP or UDP?.

Next, under Does this rule apply to all local ports or specific ports?, select
the radio button for Specific local ports. Then, enter `9050`, and click Next
to continue.

![Protocol/port configuration window with TCP, specific port \(9050\) and Next
highlighted.](../../../../_images/protocol-port.png)

The next screen is the Action page. Under What action should be taken when a
connection matches the specified conditions?, choose the radio button for
Allow the connection. Then, click Next to continue.

A Profile page appears. Under When does this rule apply?, leave the three
boxes checked for: Domain, Private, and Public. Click Next to continue to the
naming convention page.

On the Name page, enter `Odoo Worldline`, under the Name field. Enter a
Description (optional). Finally, once ready, click Finish.

The final Inbound rule should appear as follows:

| Odoo Worldline  
---|---  
Profil | Tous  
Activé | Oui  
Action | Autoriser  
Override | Non  
Programme | Au moins un  
Local Address | Au moins un  
Remote Address | Au moins un  
Protocol | TCP  
Local Port | 9050  
Remote Port | Au moins un  
Utilisateurs autorisés | Au moins un  
Authorized Computers | Au moins un  
Authorized Local Principals | Au moins un  
Local User Owner | Au moins un  
PolicyAppld | Aucun  
Application Package | Au moins un  
  
### Désinstaller Windows pour l’IoT

La désinstallation de l”IoT box virtuelle de Windows s’effectue via le
gestionnaire de programmes Windows. Quelle que soit la version de Windows,
recherchez `programme`. Sélectionnez ensuite Ajouter ou supprimer des
programmes dans le panneau de configuration. Recherchez `Odoo` et cliquez sur
le menu à trois points pour désinstaller.

Confirmez la désinstallation et suivez les étapes de désinstallation à travers
le guide de désinstallation d’Odoo.

  *[IoT]: Internet des Objets
  *[PdV]: Point de Vente
  *[MRP]: Planification des besoins en matériaux
  *[TOS]: Terms of Service
  *[LAN]: Réseau local

