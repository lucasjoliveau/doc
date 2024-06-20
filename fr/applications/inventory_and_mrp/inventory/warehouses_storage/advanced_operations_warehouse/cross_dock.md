# Organiser une correspondance dans un entrepôt

La correspondance est le processus qui consiste à envoyer des produits reçus
directement aux clients, sans les faire entrer dans le stock. Les camions sont
simplement déchargés dans une zone de _correspondance_ afin de réorganiser les
produits et de charger un autre camion.

![../../../../../_images/cross1.png](../../../../../_images/cross1.png)

Note

Pour plus d’informations sur la façon d’organiser votre entrepôt, lisez notre
blog : [What is cross-docking and is it for
me?](https://www.odoo.com/blog/business-hacks-1/post/what-is-cross-docking-
and-is-it-for-me-270)

## Configuration

Dans l’application _Inventaire_ , ouvrez Configuration ‣ Paramètres et activez
les _Routes en plusieurs étapes_.

![../../../../../_images/cross2.png](../../../../../_images/cross2.png)

Note

Ceci activera également la fonctionnalité _Emplacements de stockage_.

À présent, il est possible de configurer les _Réceptions_ et les _Expéditions_
pour fonctionner avec 2 étapes. Pour adapter la configuration, allez à
Inventaire ‣ Configuration ‣ Entrepôts et modifiez votre entrepôt.

![../../../../../_images/cross3.png](../../../../../_images/cross3.png)

Cette modification entraînera la création d’une route de _Correspondance_ qui
se trouve dans Inventaire ‣ Configuration ‣ Routes.

![../../../../../_images/cross4.png](../../../../../_images/cross4.png)

## Configurer des produits avec la route de correspondance

Créez le produit qui utilise la _Route de correspondance_ et ensuite, dans
l’onglet inventaire, sélectionnez les routes _Acheter_ et _Correspondance_. À
présent, dans l’onglet achat, précisez le fournisseur auquel vous achetez le
produit et définissez un prix.

![../../../../../_images/cross5.png](../../../../../_images/cross5.png)
![../../../../../_images/cross6.png](../../../../../_images/cross6.png)

Une fois cela fait, créez une commande client pour le produit et confirmez-la.
Odoo créera automatiquement deux transferts qui seront liés à la commande
client. Le premier est le transfert depuis l” _Emplacement d’entrée_ vers l”
_Emplacement de sortie_ , correspondant au déplacement du produit vers la zone
de _Correspondance_. Le deuxième est le bon de livraison de l” _Emplacement de
sortie_ vers votre _Emplacement client_. Les deux transferts sont toujours _En
attente d’une autre opération_ parce que vous devez encore commander le
produit auprès du fournisseur.

![../../../../../_images/cross7.png](../../../../../_images/cross7.png)
![../../../../../_images/cross8.png](../../../../../_images/cross8.png)

Allez à présent à l’application _Achats_. Vous y trouverez le bon de commande
qui a été déclenché automatiquement par le système. Validez-le et recevez les
produits dans l” _Emplacement d’entrée_.

![../../../../../_images/cross9.png](../../../../../_images/cross9.png)
![../../../../../_images/cross10.png](../../../../../_images/cross10.png)

Quand vous avez reçu les produits de votre fournisseur, vous pouvez revenir à
votre commande client initiale et valider le transfert interne depuis _Entrée_
vers _Sortie_.

![../../../../../_images/cross11.png](../../../../../_images/cross11.png)
![../../../../../_images/cross12.png](../../../../../_images/cross12.png)

Le bon de livraison est à présent prêt à être traité et peut également être
validé.

![../../../../../_images/cross13.png](../../../../../_images/cross13.png)
![../../../../../_images/cross14.png](../../../../../_images/cross14.png)

