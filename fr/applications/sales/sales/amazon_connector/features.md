# Fonctionnalités du Connecteur Amazon

Le _Connecteur Amazon_ synchronise les commandes entre Amazon et Konvergo ERP, ce qui
réduit considérablement le temps consacré à l’encodage manuel des commandes
Amazon (depuis le compte Amazon Seller) dans Konvergo ERP. Il permet également aux
utilisateurs de suivre avec précision les ventes Amazon dans Konvergo ERP.

## Fonctionnalités prises en charge

Le Connecteur Amazon est en mesure de :

  * Synchroniser (Amazon vers Konvergo ERP) toutes les commandes confirmées (FBA et FBM) et leurs articles de commande, qui comprennent :

    * le nom du produit, la description et la quantité

    * les frais d’expédition du produit

    * les frais d’emballage cadeau

  * Créer tout partenaire manquant lié à une commande dans Konvergo ERP (types de coordonnées pris en charge : contact et adresse de livraison).

  * Informer Amazon d’une expédition confirmée dans Konvergo ERP (FBM) afin d’être payé.

  * Prendre en charge plusieurs comptes vendeurs.

  * Prendre en charge plusieurs marketplaces par compte vendeur.

Le tableau suivant répertorie les capacités fournies par Konvergo ERP lors de
l’utilisation du Connecteur Amazon :

| Expédié par Amazon (FBA) | Expédié par le vendeur (FBM)  
---|---|---  
**Commandes** | Synchronisation des commandes expédiées et annulées. | Synchronisation des commandes non expédiées et annulées.  
**Expédition** | Les frais d’expédition sont calculés par Amazon et sont inclus dans la commande synchronisée. | Les frais d’expédition sont calculés par Amazon et sont inclus dans les commandes synchronisées.  
Expédition par Amazon. | Un bon de livraison est créé automatiquement dans Konvergo ERP pour chaque nouvelle commande. Une fois qu’il a été traité dans Konvergo ERP, le statut est synchronisé dans Amazon.  
**Emballage cadeau** | Géré par Amazon. | Les frais sont calculés par Amazon et sont inclus dans la commande synchronisée. Le message cadeau est ajouté sur une ligne de la commande et sur le bon de livraison. Ensuite, c’est à l’utilisateur de décider.  
**Gestion du stock** | Géré par Amazon et synchronisé avec un emplacement virtuel pour le suivre dans Konvergo ERP. | Géré dans l’application Inventaire d’Konvergo ERP et synchronisé avec Amazon.  
**Notifications de livraison** | Géré par Amazon. | Envoyé par Amazon, sur la base du statut de livraison synchronisé à partir d’Konvergo ERP.  
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le Connecteur Amazon est conçu pour synchroniser les données des commandes. D’autres actions, telles que le téléchargement des rapports de frais mensuels, la gestion des litiges ou des remboursements, <b>doivent</b> être gérés à partir d”<em>Amazon Seller Central</em>, comme d’habitude.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>As of February 19, 2024, in North American marketplaces, <abbr title="Fulfilled by Amazon">FBA</abbr> orders
created with the <em>Amazon Connector</em>, do not get the customer’s name passed onto the
sales/delivery order in Konvergo ERP. This is due to the fact that Amazon now calculates, and remits,
sales tax on behalf of sellers. In other words, personally identifiable customer information is
not transmitted to the seller any longer, after a <abbr title="Fulfilled by Amazon">FBA</abbr> order.</p>
</div>

## Marketplaces prise en charge

Si une marketplace n’est pas répertoriée dans vos marketplaces Amazon, il est
possible d”[ajouter une nouvelle marketplace](setup#amazon-add-new-
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
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="setup">Configuration du Connecteur Amazon</a></p></li>
<li><p><a href="manage">Gestion des commandes Amazon</a></p></li>
</ul>
</div>

