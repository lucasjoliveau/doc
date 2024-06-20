# Transferts par lot

Le _transfert par lot_ permet à un seul préparateur de commandes de traiter
plusieurs commandes à la fois, réduisant ainsi le temps nécessaire pour se
rendre au même emplacement dans un entrepôt.

Pour les transferts par lot, les ordres sont regroupés et consolidés dans une
liste de transferts. Après le transfert, le lot est acheminé vers un
emplacement de sortie, où les produits sont triés dans leurs emballages de
livraison respectifs.

Pour plus d'infos

Utiliser l’application Code-barres pour les transferts

Puisque les ordres _doivent_ être triés à l’emplacement de sortie après avoir
été transférés, cette méthode de transfert convient aux entreprises qui
commandent peut de produits. Le stockage des articles très demandés dans des
emplacements facilement accessibles permet d’augmenter le nombre d’ordres
satisfaits de manière efficace.

## Configuration

Pour activer l’option de transfert par lot, allez à l’application Inventaire ‣
Configuration ‣ Paramètres. Dans la section Opérations, cochez la case
Transferts par lot.

![Activez la fonctionnalité *Transferts par lot* dans Inventaire >
Configuration > Paramètres.](../../../../../_images/batch-transfer-
checkbox.png)

Puisque le transfert par lot est une méthode permettant d’optimiser
l’opération de _transfert_ dans Odoo, les fonctionnalités Emplacements de
stockage et Routes en plusieurs étapes dans la section Entrepôt doivent
également être activées sur la page des paramètres. Lorsque vous avez terminé,
cliquez sur Enregistrer.

![Activez les fonctionnalités *Emplacements de stockage* et *Routes en
plusieurs étapes* dans Inventaire > Configuration >
Paramètres.](../../../../../_images/locations-routes-checkbox.png)

Enfin, activez la fonctionnalité du transfert dans l’entrepôt, en allant à la
page des paramètres de l’entrepôt, accessible à partir de l’application
Inventaire ‣ Configuration ‣ Entrepôts.

Sélectionnez ici l’entrepôt souhaité dans la liste. Ensuite, parmi les options
disponibles pour les Expéditions, sélectionnez soit Amener les marchandises à
l’emplacement de sortie et ensuite livrer (2 étape) ou Emballer les
marchandises, les envoyer à l’emplacement de sortie et ensuite livrer (3
étapes).

Pour plus d'infos

  * [Livraison en deux étapes](../../shipping_receiving/daily_operations/receipts_delivery_two_steps.html#inventory-receipts-delivery-two-steps)

  * [Livraison en trois étapes](../../shipping_receiving/daily_operations/delivery_three_steps.html#inventory-delivery-three-steps)

![Configurez des expéditions en 2 ou 3
étapes.](../../../../../_images/set-2-or-3-step-shipment.png)

## Créer des transferts par lot

Vous pouvez manuellement créer des transferts par lot à partir de
l’application Inventaire ‣ Opérations ‣ Transferts par lot. Cliquez sur le
bouton Nouveau pour créer un transfert par lot.

Sur le formulaire du transfert par lot, complétez les champs suivants en
conséquence :

  * Responsable : l’employé assigné au transfert. Laissez ce champ vide si _n’importe quel_ ouvrier peut effectuer ce transfert.

  * Type d’opération : sélectionnez dans le menu déroulant le type d’opération sous lequel le transfert est classé.

  * Date planifiée : précise la date à laquelle la personne Responsable doit effectuer le transfert vers l’emplacement de sortie.

Ensuite, dans la liste des Transferts, cliquez sur Ajouter une ligne pour
ouvrir la fenêtre Ajouter : Transferts.

Si vous avez complété le champ Type d’opération, la liste filtrera les
enregistrements de transfert correspondant au Type d’opération sélectionné.

Cliquez sur le bouton Nouveau pour créer un nouveau transfert.

Une fois les enregistrements de transfert sélectionnés, cliquez sur Confirmer
pour confirmer le transfert par lot.

Example

Un nouveau transfert par lot est assigné au Responsable, `Joel Willis`, pour
le type d’opération `Transfert`. La Date planifiée est définie sur `11 août`.

![Vue du formulaire *Transferts par lot*.](../../../../../_images/batch-
transfer-form.png)

En cliquant sur le bouton Ajouter une ligne, la fenêtre Ajouter : Transferts
s’ouvre et n’affiche que les transferts, étant donné que le Type d’opération
était défini sur `Transfert` sur le formulaire du transfert par lot.

Cochez la case à cocher à gauche des transferts, `WH/PICK/00001` et
`WH/PICK/00002`, pour les inclure dans le nouveau transfert. Cliquez ensuite
sur le bouton Sélectionner pour fermer la fenêtre Ajouter : Transferts.

![Sélectionnez plusieurs transferts dans la fenêtre *Ajouter :
Transferts*.](../../../../../_images/add-transfers-window.png)

### Ajouter un lot à partir de la liste des transferts

Il existe une autre méthode de créer des transferts par lot : l’option Ajouter
au lot dans la vue de liste. Allez à l’application Inventaire ‣ Opérations et
sélectionnez n’importe quel Transfert dans le menu déroulant pour ouvrir une
liste filtrée de transferts.

![Afficher tous les types de transfert dans un menu déroulant : Réceptions,
Livraisons, Transferts internes,  Fabrications, Transferts par lot,
Dropshippings.](../../../../../_images/transfers-drop-down.png)

Sur la liste des transferts, cochez la case à gauche des transferts
sélectionnés pour l’ajouter à un lot. Allez ensuite au bouton Actions ⚙️
(engrenage) et cliquez sur Ajouter au lot dans le menu déroulant qui s’ouvre.

![Utiliser le bouton *Ajouter au lot*, dans la liste du bouton
*Action*.](../../../../../_images/add-to-batch.png)

Cette action ouvre une fenêtre contextuelle Ajouter au lot, dans laquelle
l’employé Responsable du transfert peut être désigné.

Choisissez parmi les deux options radio d’ajouter à un transfert par lot
existant ou de créer un nouveau transfert par lot.

Pour commencer par un brouillon, cochez la case Brouillon.

Terminez le processus en cliquant sur Confirmer.

![Afficher la fenêtre *Ajouter au lot* pour créer un transfert par
lot.](../../../../../_images/add-to-batch-window.png)

## Traiter des transferts par lot

Traitez les transferts par lot dans l’application Inventaire ‣ Opérations ‣
Transferts par lot.

Sélectionnez le transfert souhaité dans la liste. Ensuite, sur le formulaire
du transfert par lot, saisissez les quantités faites pour chaque produit, dans
l’onglet Opérations détaillées. Cliquez enfin sur Valider pour terminer le
transfert.

Astuce

Assurez-vous que le transfert par lot est terminé lorsque le bouton Valider
est surligné en mauve. Si le bouton Vérifier la disponibilité est surligné à
la place, cela signifie qu’il y a des articles dans le lot qui ne sont
actuellement _pas_ disponibles en stock.

Example

Dans un transfert par lot impliquant des produits provenant des transferts,
`WH/PICK/00001` et `WH/PICK/00002`, l’onglet Opérations détaillées montre que
le produit, `Armoire avec portes`, a été transféré parce que la colonne Fait
correspond à la valeur de la colonne Réservé. Cependant, des quantités de
`0,00` ont été transférées pour l’autre produit, `Boîtier pour câbles`.

![Afficher le transfert par lot de produits provenant de deux transferts dans
l'onglet *Opérations détaillées*.](../../../../../_images/process-batch-
transfer.png)

Seuls les produits en stock sont visibles dans l’onglet Opérations détaillées.

Pour afficher la liste complète des produits, allez à l’onglet Opérations.
Dans cette liste, la colonne Demande indique la quantité souhaitée pour
l’ordre. La colonne Réservé indique le stock disponible pour honorer l’ordre.
Enfin, la colonne Fait précise les produits qui ont été transférés et qui sont
prêts pour l’étape suivante.

Example

Le produit, `Sous-main`, issu du même lot que l”exemple ci-dessus, n’est
visible que dans l’onglet Opérations, car il n’y a pas de quantités réservées
en stock pour honorer le transfert par lot.

Cliquez sur le bouton Vérifier la disponibilité pour rechercher à nouveau les
produits disponibles dans le stock.

![Afficher les quantités réservées non disponibles dans l'onglet
*Opérations*.](../../../../../_images/operations-tab.png)

### Créer un reliquat

Sur le formulaire de transfert par lot, si la quantité faite du produit est
_inférieure_ à la quantité réservée, une fenêtre contextuelle s’ouvre.

Cette fenêtre contextuelle propose l’option : Créer un reliquat ?.

Si vous cliquez sur le bouton Créer un reliquat, un nouveau lot est
automatiquement créé, contenant les produits restants.

Cliquez sur Aucun reliquat pour terminer le transfert _sans_ créer un autre
transfert par lot.

Cliquez sur Ignorer pour annuler la validation et revenir au formulaire de
transfert par lot.

![Afficher la fenêtre contextuelle *Créer un
reliquat*.](../../../../../_images/create-backorder.png)

## Traiter le transfert par lot : l’application Code-barres

Les transferts par lot créés sont également répertoriés dans l’application
Code-barres, accessible en cliquant sur le bouton Transferts par lot.

Par défaut, les transferts par lot confirmés apparaissent sur la page des
Transferts par lot. Sur cette page, cliquez sur le transfert par lot souhaité
pour ouvrir une liste détaillée des produits à transférer.

![Afficher la liste des transferts par lot à effectuer dans l'application
*Code-barres*.](../../../../../_images/barcode-batch-transfers.png)

Pour le transfert par lot choisi, suivez les instructions en haut de la page
sur fond noir. Commencez par scanner le code-barres du produit pour
enregistrer un seul produit à transférer. Pour enregistrer des quantités
multiples, cliquez sur l’icône ✏️ (crayon) et saisissez les quantités requises
pour le transfert.

Note

Les produits du même ordre sont libellés de la même couleur à gauche. Les
transferts complétés sont surlignés en vert.

Example

Dans un transfert par lot pour 2 `Armoires avec portes`, 3 `Écrans anti-
bruit`, et 4 `Bureaux de quatre personnes`, les Unités `3/3` et `4/4`
indiquent que les deux derniers transferts de produits sont terminés.

`1/2` unité de l”`Armoire avec portes` a déjà été transféré et après avoir
scanné le code-barres du produit pour la deuxième armoire, Odoo invite
l’utilisateur à `Scanner un numéro de série` pour enregistrer le numéro de
série unique à des fins de [suivi de
produits](../../product_management/product_tracking/serial_numbers.html#inventory-
serial-numbers-configure).

![Afficher les produits à transférer dans la vue Code-
barres.](../../../../../_images/barcode-products.png)

Une fois tous les produits transférés, cliquez sur Valider pour marquer le
transfert par lot comme Fait.

