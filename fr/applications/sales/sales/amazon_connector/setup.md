# Configuration du Connecteur Amazon

Odoo permet aux utilisateurs d’enregistrer un compte vendeur Amazon dans la
base de données, mais l’utilisateur **doit** avoir un compte Vendeur Amazon
avant de terminer la configuration.

Configurez un compte Vendeur payant sur Amazon en vous inscrivant d’abord sur
la plateforme Amazon et en allant à Comptes & Listes ‣ Créer un compte vendeur
dans le menu déroulant situé dans la section d’en-tête.

Ensuite, sur la page Vendre avec Amazon, suivez les étapes du processus
d’inscription et les instructions suivantes pour enregistrer et lier de compte
Vendeur Amazon dans Odoo.

Pour plus d'infos

[Vendre avec Amazon](https://www.amazon.com/b/?node=12766669011)

## Connecter le compte Vendeur Amazon à Odoo

Pour connecter un compte Vendeur Amazon, allez à l’application Ventes ‣
Configuration ‣ Paramètres ‣ Section des Connecteurs, activez la
fonctionnalité Synchronisation Amazon et cliquez sur Enregistrer.

Retournez ensuite à l’application Ventes ‣ Configuration ‣ Paramètres ‣
section des Connecteurs, et cliquez sur le lien Comptes Amazon en dessous du
paramètre Sychronisation Amazon.

![Le lien Comptes Amazon en dessous des paramètres de synchronisation Amazon
dans Odoo Ventes.](../../../../_images/amazon-accounts-link-setting.png)

Une page séparée Comptes Amazon s’ouvre alors. Cliquez ici sur Nouveau pour
créer et lier un nouveau compte Amazon.

Sur le formulaire Compte Amazon vierge, commencez par donner un nom au compte
(par ex. `Marketplace américaine`). Ensuite, dans l’onglet Identifiants,
sélectionnez la marketplace sur laquelle le compte vendeur a initialement été
créé dans le menu déroulant Marketplace initiale.

![Un formulaire Compte Amazon typique dans l'application Odoo
Ventes.](../../../../_images/amazon-accounts-form-page.png)

Après avoir enregistré, le champ dans l’onglet Identifiants est remplacé par
un bouton Associer à Amazon.

![Un formulaire Compte Amazon typique et le bouton Associer avec Amazon dans
Odoo Ventes.](../../../../_images/amazon-accounts-form-link-button.png)

En cliquant sur ce bouton, l’utilisateur est redirigé vers la page de
connexion d’Amazon ou directement vers la page de consentement requise, s’il
est déjà connecté à Amazon.

Sur la page de connexion, connectez-vous au compte vendeur Amazon.

Sur la page de consentement, confirmez qu’Amazon est autorisé à donner à Odoo
l’accès au compte et aux données connexes.

Après confirmation, Amazon renvoie l’utilisateur à Odoo et le compte a été
enregistré.

Une fois le compte Amazon enregistré avec succès, les marketplaces disponibles
à ce compte spécifique sont synchronisées avec Odoo et répertoriées dans
l’onglet Marketplaces.

Si vous le souhaitez, supprimez des éléments de la liste des marketplaces
synchronisées pour désactiver la synchronisation.

## Commandes Amazon dans Odoo

Lorsqu’une commande Amazon est synchronisée, Odoo crée jusqu’à trois lignes
sur la commande. Chaque ligne représente un produit vendu sur Amazon : une
pour le produit vendu sur la marketplace Amazon, une pour les frais
d’expédition (le cas échéant) et une pour les frais d’emballage cadeau (le cas
échéant).

La sélection d’un produit de base de données pour une commande se fait en
faisant correspondre sa Référence interne (un identifiant de référence de
produit personnalisable dans Odoo, comme `FURN001`) avec le _SKU_ Amazon pour
les articles de la marketplace, le _Code d’expédition_ d’Amazon pour les frais
de livraison et le code _Emballage cadeau_ d’Amazon pour les frais d’emballage
cadeau.

Pour les produits de la marketplace, les paires sont sauvegardées en tant qu”
_Offres Amazon_ , qui sont répertoriées sous le bouton intelligent Offres sur
le formulaire du compte.

![Le bouton intelligent Offres Amazon sur le formulaire de compte dans Odoo
Ventes.](../../../../_images/amazon-offers-button.png)

Les offres sont créées automatiquement lorsque les paires sont établies et
elles sont utilisées pour les commandes suivantes pour rechercher les SKU. Si
aucune offre avec une SKU correspondante n’est trouvée, la référence interne
est utilisée à la place.

Astuce

Il est possible de forcer l’appariement d’un article de marketplace avec un
produit spécifique, en modifiant soit le produit, soit la SKU d’une offre pour
garantir qu’ils correspondent. L’offre peut être créée manuellement si ce
n’est pas encore fait automatiquement.

Ceci est utile si la référence interne n’est pas utilisée en tant que SKU, ou
si le produit est vendu dans des conditions différentes.

Si aucun produit de base de données avec une référence interne correspondante
n’est trouvée pour une SKU Amazon ou un code d’emballage cadeau, un produit
standard de la base de données, _Vente Amazon_ , est utilisé. Il en va de même
pour le produit par défaut _Expédition Amazon_ si aucun produit de base de
données n’est trouvé pour un certain code d’expédition d’Amazon.

Note

Pour modifier les produits par défaut, activez le [mode
développeur](../../../general/developer_mode.html#developer-mode), et allez à
l’application Ventes ‣ Configuration ‣ Paramètres ‣ Connecteurs ‣
Synchronisation Amazon ‣ Produits par défaut.

## Configuration des taxes sur les produits

Pour permettre la déclaration fiscale des ventes Amazon dans Odoo, les taxes
appliquées aux articles de la commande sont celles définies sur le produit, ou
déterminées par la position fiscale.

Veillez à ce que les taxes soient correctement définies sur vos produits dans
Odoo ou à ce qu’elles soient déterminées par une position fiscale, pour éviter
des divergences dans les sous-totaux entre _Amazon Seller Central_ et Odoo.

Note

Comme Amazon n’applique pas nécessairement les mêmes taxes que celles
configurées dans Odoo, il se peut que les totaux de la commande diffèrent de
quelques centimes entre Odoo et _Amazon Seller Central_. Ces différences
peuvent être résolues par une écriture d’annulation lors du rapprochement des
paiements dans Odoo.

## Ajouter une nouvelle marketplace

Toutes les marketplaces sont prises en charge par le Connecteur Amazon. Pour
ajouter une nouvelle marketplace, suivez les étapes suivantes :

  1. Activez le [mode développeur](../../../general/developer_mode.html#developer-mode).

  2. Allez à l’application Ventes ‣ Configuration ‣ Paramètres ‣ Connecteurs ‣ Synchronisation Amazon ‣ Marketplaces Amazon.

  3. Cliquez sur Nouveau pour créer un nouvel enregistrement de marketplace.

  4. Enter the Marketplace ID in the API Idenifier field, and select the Amazon Region for your marketplace as described in the [Amazon Documentation for marketplace IDs and regions](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids), and the Seller Central URL as described in the [Amazon Documentation for seller central URLs](https://developer-docs.amazon.com/sp-api/docs/seller-central-urls).

  5. Définissez le Nom de l’enregistrement sur `Amazon.<country code>` pour le retrouver facilement (par ex. `Amazon.se`). Les champs Identifiant API, Région et URL Seller Central devraient respectivement contenir les valeurs _ID de la marketplace, la région d’Amazon sélectionnée et l”*URL Seller Central_ de la documentation d’Amazon.

  6. Une fois la marketplace enregistrée, mettez à jour la configuration du compte Amazon en allant à l’application Ventes ‣ Configuration ‣ Paramètres ‣ Connecteurs ‣ Synchronisation Amazon ‣ Comptes Amazon.

  7. Sélectionnez le compte sur lequel vous voulez utiliser la nouvelle marketplace, allez à l’onglet Marketplaces et cliquez sur Mettre à jour les marketplaces disponibles. Une animation devrait confirmer la réussite de l’opération. Les marketplaces nouvellement ajoutées sont automatiquement ajoutées à la liste des marketplaces synchronisées. Si la nouvelle marketplace n’est pas ajoutée à la liste, cela signifie qu’elle est incompatible ou indisponible pour le compte vendeur.

Pour plus d'infos

  * [Fonctionnalités du Connecteur Amazon](features.html)

  * [Gestion des commandes Amazon](manage.html)

