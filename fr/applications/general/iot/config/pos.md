# Utiliser une IoT box avec un Point de Vente

## Conditions préalables

Avant de commencer, assurez-vous que l’équipement suivant est disponible :

  * Une IoT box, avec son adaptateur d’alimentation.

  * Un ordinateur ou une tablette avec un navigateur web à jour.

  * Une instance Odoo Online ou une instance Odoo sur laquelle les applications _Point de Vente_ et _IoT_ sont installées.

  * Un réseau local configuré avec DHCP (il s’agit du paramètre par défaut).

  * Un câble Ethernet RJ45 (facultatif, mais préféré au WiFi qui est déjà intégré).

  * N’importe quel matériel pris en charge (imprimante de reçu, lecteur de codes-barres, tiroir caisse, terminal de paiement, balance, écran client, etc.). Vous trouverez la liste du matériel pris en charge sur la [page du matériel PdV](https://www.odoo.com/page/point-of-sale-hardware).

## Configuration

![../../../../_images/pos-connections.png](../../../../_images/pos-
connections.png)

Une proposition de configuration d’un système de point de vente.

Pour connecter le matériel au PdV, la première étape consiste à connecter une
IoT box à la base de données. Pour ce faire, suivez ces instructions :
[Connecter une Internet of Things (IoT) box à la base de données
Odoo](connect.html).

Connectez ensuite les périphériques à l”IoT box.

Nom du périphérique | Instructions  
---|---  
Imprimante | Connectez une imprimante de reçu prise en charge à un port USB ou au réseau et mettez-la sous tension. Consultez [Imprimer des commandes](../../../sales/point_of_sale/restaurant/kitchen_printing.html).  
Tiroir caisse | Le tiroir caisse doit être connecté à l’imprimante via un câble RJ25.  
Lecteur de codes-barres | Pour que le lecteur de codes-barres soit compatible, il doit terminer les codes-barres par un caractère `ENTER` (keycode 28). Il s’agit probablement de la configuration par défaut du lecteur de codes-barres.  
Balance | Connect the scale and power it on. Refer to [Connecter une balance](../devices/scale.html).  
Écran client | Connect a screen to the IoT box to display the PoS order. Refer to [Connecter un écran](../devices/screen.html).  
Terminal de paiement | Le processus de connexion dépend du terminal. Consultez la [documentation relative aux terminaux de paiement](../../../sales/point_of_sale/payment_methods.html).  
  
Une fois cette opération terminée, connectez l”IoT box à l’application PdV.
Pour ce faire, allez à Point de Vente ‣ Configuration ‣ Paramètres, cochez la
case à côté de l’option IoT Box et sélectionnez les périphériques à utiliser
dans ce PdV. Enregistrez les changements.

![Configuration des périphériques connectés dans l'application Point de
Vente.](../../../../_images/iot-connected-devices.png)

Une fois la configuration effectuée, vous pouvez lancer une nouvelle session
PdV

  *[IoT]: Internet of Things
  *[DHCP]: Dynamic Host Configuration Protocol
  *[PdV]: Point de Vente
  *[USB]: Universal Serial Bus
  *[PoS]: Point of Sale

