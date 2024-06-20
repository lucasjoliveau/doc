# Associer des annonces existantes

Une fois que le compte est associé, les annonces existantes du compte vendeur
d’eBay doivent être ajoutées manuellement aux listes de produits Odoo.

Le processus est le suivant : - Désactiver les actions programmées d’eBay -
Ajouter des produits et associer des annonces - Activer les actions
programmées d’eBay

Pour plus d'infos

Pour en apprendre plus sur le connecteur eBay, consultez également ces pages :

  * [Configuration du connecteur eBay](setup.html)

  * [Comment répertorier un produit ?](manage.html)

  * [Dépannage du connecteur eBay](troubleshooting.html)

## Désactiver les actions planifiées d’eBay

Pour commencer à associer les annonces existantes dans eBay, désactivez
d’abord les notifications d’eBay dans les actions planifiées dans Odoo. La
raison en est qu’aucune commande ou donnée eBay n’est synchronisée pendant ce
processus. Vous pouvez accéder aux Actions planifiées en activant d’abord le
[mode développeur](../../../general/developer_mode.html#developer-mode).
Ensuite, allez aux Paramètres ‣ Technique ‣ Automatisation ‣ Actions
planifiées.

Avertissement

Le [Developer mode (debug mode)](../../../general/developer_mode.html) doit
être activé pour que le menu technique soit visible pour l’utilisateur.

La désactivation des actions planifiées permet aux utilisateurs de
synchroniser et de valider les données d’eBay avant de recevoir les commandes.
Les actions planifiées qui doivent être temporairement désactivées sont
décrites ci-dessous :

  * eBay : obtenez de nouvelles commandes : eBay pousse les nouvelles commandes qui ne se trouvent pas encore dans Odoo (basées sur les champs client_order_reference, ou sales order reference). Cette commande met également à jour les commandes existantes, pour lesquelles les changements ont été effectués dans eBay. Les nouvelles commandes et les commandes mises à jour sont ensuite placées en mode brouillon. Les clients seront créés s’ils n’existent pas encore dans Odoo.

  * eBay : synchronisez les stocks : eBay affiche le stock disponible d’Odoo.

  * eBay : mise à jour des catégories : eBay envoie des catégories mensuelles mises à jour (uniquement jusqu’à la quatrième couche ; une mise à jour manuelle est nécessaire pour le reste).

Pour désactiver la notification eBay, sélectionnez l’entrée dans la liste des
Actions planifiées. Ensuite, sur la page, cliquez sur le bouton Actif pour la
désactiver.

### Synchroniser les catégories d’eBay

Pour s’assurer que les produits eBay d’Odoo ont toutes les catégories
disponibles sur eBay, les catégories d’eBay doivent ensuite être synchronisées
avec Odoo.

Navigate to Settings ‣ Technical ‣ Automation ‣ Scheduled Actions. Click into
the scheduled action labeled: Ebay: update categories and then click Run
Manually.

Important

Odoo ne reconnaît les chemins de catégories d’eBay que jusqu’à quatre couches
de profondeur. Si un produit a une annonce de plus de quatre couches, le champ
catégorie ne sera rempli que jusqu’à la quatrième couche.

Si des catégories de produits de plus de quatre chemins sont nécessaires, les
utilisateurs doivent ajouter ces chemins manuellement. Historiquement, cela a
été fait en obtenant une liste de toutes les catégories de produits de plus de
4 chemins, en les important dans le modèle de Catégorie de produits dans Odoo
et en les liant individuellement au produit.

Les utilisateurs peuvent importer les autres catégories de produits dans les
catégories de produits d’eBay manuellement à l’aide du menu Action et de la
fonctionnalité Importer.

## Associer les annonces eBay

Pour ajouter des annonces eBay dans Odoo, ajoutez les produits manuellement à
l’aide d’une ID d’annonce ou établissez un lien de liste automatique entre
Odoo et eBay.

Astuce

Pour plus d’informations sur l’association d’un produit à partir de zéro,
consulter la page [Comment répertorier un produit ?](manage.html#ebay-
connector-listing)

### Lien de liste manuel

Pour ajouter une annonce eBay aux produits dans Odoo, allez à l’application
Ventes ‣ Produits ‣ Produits et sélectionnez le produit souhaité. Cliquez sur
Vendre sur eBay (soit dans l’onglet eBay, soit sous le Nom du produit).
Cliquez sur Enregistrer si nécessaire.

Toujours sur le formulaire du produit, cliquez sur lien vers l’annonce dans le
menu supérieur et saisissez l’ID de l’annonce sur eBay dans la fenêtre
contextuelle (l’ID de l’annonce se trouve dans l’URL du produit eBay).

Example

Un exemple d’URL serait :
`www.ebay.com/itm/272222656444?hash=item3f61bc17bb:g:vJ0AAOSwslJizv8u`. L’ID
de l’annonce est `272222656444` dans ce cas. Une fois l’ID de l’annonce saisi,
les informations relatives à l’annonce eBay seront synchronisées vers Odoo.

## Activer les actions planifiées d’eBay

La prochaine étape consiste à activer les notifications eBay dans les actions
planifiées dans Odoo pour pouvoir échanger les commandes et les données. Vous
pouvez accéder aux Actions planifiées en activant le [mode
développeur](../../../general/developer_mode.html#developer-mode) et en allant
aux Paramètres ‣ Technique ‣ Automatisation ‣ Actions planifiées.

L’activation des actions planifiées suivantes permet aux utilisateurs de
synchroniser et de valider les données eBay automatiquement.

  * eBay : Obtenez de nouvelles commandes : eBay envoie toutes les nouvelles commandes qui ne se trouvent pas encore dans Odoo (basées sur les champs client_order_reference, ou sales_order_reference), et met à jour les commandes s’il y a eu un changement sur eBay. Les commandes seront placées en mode brouillon. Les clients seront créés s’ils n’existent pas encore dans Odoo.

  * eBay : synchronisez les stocks : eBay affiche le stock disponible dans Odoo.

  * eBay : mise à jour des catégories : eBay envoie des catégories mensuelles mises à jour (uniquement jusqu’à la quatrième couche, une mise à jour manuelle est nécessaire pour le reste).

Note

Lorsqu’une commande est placée et l’annonce de la commande n’est pas associée
à un produit, eBay créera un produit consommable. Ces consommables doivent
être modifiés sur la _commande_ en brouillon afin de représenter un produit
stockable et l’utilisateur peut ensuite l’associer à l’annonce.

Pour plus d'infos

  * [Comment répertorier un produit ?](manage.html)

  * [Dépannage du connecteur eBay](troubleshooting.html)

  * [Configuration du connecteur eBay](setup.html)

