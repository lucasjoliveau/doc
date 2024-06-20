# Fonctionnalités du Connecteur Amazon

Le _Connecteur Amazon_ synchronise les commandes entre Amazon et Odoo, ce qui
réduit considérablement le temps consacré à l’encodage manuel des commandes
Amazon (depuis le compte Amazon Seller) dans Odoo. Il permet également aux
utilisateurs de suivre avec précision les ventes Amazon dans Odoo.

## Fonctionnalités prises en charge

Le Connecteur Amazon est en mesure de :

  * Synchroniser (Amazon vers Odoo) toutes les commandes confirmées (FBA et FBM) et leurs articles de commande, qui comprennent :

    * le nom du produit, la description et la quantité

    * les frais d’expédition du produit

    * les frais d’emballage cadeau

  * Créer tout partenaire manquant lié à une commande dans Odoo (types de coordonnées pris en charge : contact et adresse de livraison).

  * Informer Amazon d’une expédition confirmée dans Odoo (FBM) afin d’être payé.

  * Prendre en charge plusieurs comptes vendeurs.

  * Prendre en charge plusieurs marketplaces par compte vendeur.

Le tableau suivant répertorie les capacités fournies par Odoo lors de
l’utilisation du Connecteur Amazon :

| Expédié par Amazon (FBA) | Expédié par le vendeur (FBM)  
---|---|---  
**Commandes** | Synchronisation des commandes expédiées et annulées. | Synchronisation des commandes non expédiées et annulées.  
**Expédition** | Les frais d’expédition sont calculés par Amazon et sont inclus dans la commande synchronisée. | Les frais d’expédition sont calculés par Amazon et sont inclus dans les commandes synchronisées.  
Expédition par Amazon. | Un bon de livraison est créé automatiquement dans Odoo pour chaque nouvelle commande. Une fois qu’il a été traité dans Odoo, le statut est synchronisé dans Amazon.  
**Emballage cadeau** | Géré par Amazon. | Les frais sont calculés par Amazon et sont inclus dans la commande synchronisée. Le message cadeau est ajouté sur une ligne de la commande et sur le bon de livraison. Ensuite, c’est à l’utilisateur de décider.  
**Gestion du stock** | Géré par Amazon et synchronisé avec un emplacement virtuel pour le suivre dans Odoo. | Géré dans l’application Inventaire d’Odoo et synchronisé avec Amazon.  
**Notifications de livraison** | Géré par Amazon. | Envoyé par Amazon, sur la base du statut de livraison synchronisé à partir d’Odoo.  
  
Note

Le Connecteur Amazon est conçu pour synchroniser les données des commandes.
D’autres actions, telles que le téléchargement des rapports de frais mensuels,
la gestion des litiges ou des remboursements, **doivent** être gérés à partir
d” _Amazon Seller Central_ , comme d’habitude.

Avertissement

As of February 19, 2024, in North American marketplaces, FBA orders created
with the _Amazon Connector_ , do not get the customer’s name passed onto the
sales/delivery order in Odoo. This is due to the fact that Amazon now
calculates, and remits, sales tax on behalf of sellers. In other words,
personally identifiable customer information is not transmitted to the seller
any longer, after a FBA order.

## Marketplaces prise en charge

Si une marketplace n’est pas répertoriée dans vos marketplaces Amazon, il est
possible d”[ajouter une nouvelle marketplace](setup.html#amazon-add-new-
marketplace).

**Région Amérique du Nord**  
---  
Canada | Amazon.ca  
Mexique | Amazon.com.mx  
USA. | Amazon.com  
**Région Europe**  
---  
Allemagne | Amazon.de  
Espagne | Amazon.es  
France | Amazon.fr  
UK | Amazon.co.uk  
Italie | Amazon.it  
Pays-Bas | Amazon.nl  
  
Pour plus d'infos

  * [Configuration du Connecteur Amazon](setup.html)

  * [Gestion des commandes Amazon](manage.html)

  *[FBA]: Fulfilled by Amazon

