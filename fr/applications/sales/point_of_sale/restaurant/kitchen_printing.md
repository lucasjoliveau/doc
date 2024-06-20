# Imprimer des commandes

L’intégration des imprimantes dans les flux de travail d’un restaurant ou d’un
bar peut améliorer la communication et la collaboration entre les équipes en
salle et en cuisine, rendant le service plus structuré et efficace.

## Configuration

### Activer et créer des imprimantes

Pour activer l’envoi de commandes à l’imprimante de la cuisine ou du bar,
allez à Point de Vente ‣ Configuration ‣ Paramètres, descendez jusqu’à la
section Restaurant & Bar et activez les Imprimantes de cuisine. Donnez un nom
à l’imprimante dans le champ Imprimantes et cliquez sur Créer et modifier…
pour ouvrir un formulaire de configuration.

Pour obtenir une liste de toutes les imprimantes déjà créées ou pour modifier
une imprimante déjà créée, cliquez sur –> Imprimantes et sélectionnez
l’imprimante souhaitée pour ouvrir le formulaire de configuration.

![paramètres pour activer les imprimantes de
cuisine](../../../../_images/printers-settings.png)

### Formulaire de configuration

À partir du formulaire de configuration, sélectionnez le Type d’imprimante en
fonction de votre installation :

  * Si votre imprimante est connectée à une IoT Box, sélectionnez Utiliser une imprimante connectée à l’IoT Box et sélectionnez le périphérique dans le champ Appareil IoT.

  * Si vous utilisez une imprimante Epson qui n’a pas besoin d’IoT Box, sélectionnez Utiliser une imprimante Epson et saisissez l’adresse IP de l’imprimante dans le champ Adresse IP imprimante Epson.

Pour plus d'infos

  * [Connecter une IoT box à Odoo](../../../general/iot/config/connect.html)

  * [Connecter une imprimante](../../../general/iot/devices/printer.html)

  * [Certificat auto-signé pour les imprimantes ePOS](../configuration/epos_ssc.html)

Configurez votre imprimante pour qu’elle imprime des produits spécifiques en
fonction de leur catégorie PdV. Pour ce faire, cliquez sur Ajouter une ligne
dans le champ Catégories de produit imprimées. Si vous laissez ce champ vide,
tous les produit sont envoyés à l’imprimante quelle que soit leur catégorie
PdV.

![formulaire de configuration d'une imprimante de
cuisine](../../../../_images/printer-setup.png)

## Imprimer des commandes

À partir d’une session ouverte, prenez une commande et cliquez sur Commande
pour l’envoyer au bar ou en cuisine.

![bouton de commande dans l'interface utilisateur du point de vente pour
envoyer des commandes en cuisine ou au bar](../../../../_images/order-
button.png)

Note

Lorsque des produits peuvent être imprimés, ils apparaissent en vert dans le
panier et le bouton de la commande devient vert.

