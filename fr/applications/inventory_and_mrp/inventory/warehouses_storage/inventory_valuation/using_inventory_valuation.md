# Utiliser la valorisation des stocks

La _valorisation des stocks_ est une procédure comptable essentielle qui
permet de calculer la valeur du stock disponible. Une fois déterminé, le
montant de la valorisation des stocks est ensuite compté dans la valeur
globale de l’entreprise.

Dans Odoo, ce processus peut être appliqué manuellement — par les employés de
l’entrepôt qui comptent physiquement les produits — ou automatiquement par le
biais de la base de données.

## Valorisation automatique des stocks

Pour qu’Odoo génère automatiquement une trace des entrées de valorisation des
stocks, allez d’abord à la liste des Catégories de produits en allant à
l’application Inventaire ‣ Configuration ‣ Catégories de produits et
sélectionnez la catégorie de produits souhaitée. Sur le formulaire, définissez
la Valorisation des stocks sur Automatisée et la Méthode de coût sur l’une des
trois options.

Pour plus d'infos

[Set up inventory valuation](inventory_valuation_config.html)

Pour comprendre comment les entrées et les sorties de produits en stock
impactent la valeur globale de l’entreprise, examinons le scénario suivant de
mouvements des produits et des stocks.

### Recevoir un produit

Pour garder une trace de la valeur des produits entrants, tels qu’une simple
_table_ , configurez la catégorie de produits sur le produit même. Pour ce
faire, allez à l’application Inventaire ‣ Produits ‣ Produits et cliquez sur
le produit souhaité. Sur la fiche du produit, cliquez sur l’icône ➡️ (flèche
droite) à côté du champ Catégorie de produits qui ouvre un lien interne
permettant de modifier la catégorie de produits. Ensuite, définissez la
Méthode de coût sur First In First Out (FIFO) et la Valorisation des stocks
sur Automatisée.

Astuce

Vous pouvez également accéder au tableau de bord des Catégories de produits en
allant à l’application Inventaire ‣ Configuration ‣ Catégories de produits et
sélectionnez la catégorie de produits souhaitée.

Ensuite, imaginons que 10 tables sont achetées à un prix de 10,00 $ chacune.
Le bon de commande de ces tables affichera le sous-total de l’achat de 100 $,
plus tous les frais ou taxes supplémentaires.

![Bon de commande avec 10 tables d'une valeur de 10,00 $
chacune.](../../../../../_images/purchase-order.png)

Après avoir cliqué sur Valider sur le bon de commande, le bouton intelligent
Valorisation s’affiche. Si vous cliquez sur ce bouton, un rapport s’affiche
montrant comment la valorisation des stocks de la table a été impactée par cet
achat.

Important

Le [mode développeur](../../../../general/developer_mode.html#developer-mode)
**doit** être activé pour voir le bouton intelligent Valorisation.

Astuce

The [consignment](../advanced_operations_warehouse/owned_stock.html) feature
allows ownership to items in stock. Thus, products owned by other companies
are not accounted for in the host company’s inventory valuation.

![Voir le bouton intelligent Valorisation sur une réception, avec le mode
développeur activé.](../../../../../_images/valuation-smart-button.png)

Pour obtenir un tableau de bord complet comprenant la valorisation des stocks
de toutes les expéditions de produits, les ajustements d’inventaire et les
opérations d’entrepôt, consultez le rapport de valorisation des stocks.

### Livrer un produit

Dans la même logique, lorsqu’une table est expédiée à un client et quitte
l’entrepôt, la valorisation des stocks diminue. De même, le bouton intelligent
Valorisation sur le bon de livraison affiche l’enregistrement de la
valorisation des stocks comme il le fait sur un bon de commande.

![Valorisation des stocks réduite après l'expédition d'un
produit.](../../../../../_images/decreased-stock-valuation.png)

## Rapport de valorisation des stocks

Pour afficher la valeur totale de tous les produits de l’entrepôt, activez
d’abord le [mode
développeur](../../../../general/developer_mode.html#developer-mode) et allez
à l’application Inventaire ‣ Analyse ‣ Valorisation. Le tableau de bord de la
Valorisation des stocks affiche des enregistrements détaillés des produits
avec la Date, la Quantité, la Valeur unitaire, et la Valeur totale de
l’inventaire.

Important

Le [mode développeur](../../../../general/developer_mode.html#developer-mode)
**doit** être activé pour voir l’option Valorisation dans la section Analyse.

![Le rapport de valorisation des stocks affichant de multiples
produits.](../../../../../_images/inventory-valuation-products.png)

Le bouton Valorisation à la date, situé dans le coin supérieur gauche de la
page Valorisation des stocks, fait apparaître une fenêtre contextuelle. Dans
cette fenêtre, vous pouvez sélectionner et voir la valorisation des stocks des
produits disponibles à une date antérieure précise.

Astuce

Vous pouvez voir un enregistrement détaillé de la valeur d’inventaire, des
mouvements de stock et du stock disponible d’un produit en sélectionnant le
bouton sarcelle ➡️ (flèche droite) à droite de la valeur de la colonne
Référence.

### Mettre à jour le prix unitaire d’un produit

Pour une entreprise, les délais, les défaillances de la chaîne
d’approvisionnement et d’autres facteurs de risque peuvent engendrer des coûts
invisibles. Même si Odoo tente de représenter fidèlement la valeur du stock,
la _valorisation manuelle_ est un outil supplémentaire pour mettre à jour le
prix unitaire des produits.

Important

La valorisation manuelle est destinée aux produits qui peuvent être achetés et
reçus pour un coût supérieur à 0 ou qui ont des catégories de produits dont la
Méthode de coût est définie sur Coût moyen (AVCO) ou First In First Out
(FIFO).

![Ajouter une valorisation manuelle de la valeur du stock à un
produit.](../../../../../_images/add-manual-valuation.png)

Créez des entrées de valorisation manuelle sur le tableau de bord de la
Valorisation des stocks en allant d’abord à l’application Inventaire ‣ Analyse
‣ Valorisation. Ensuite, pour activer la fonctionnalité _Revalorisation du
produit_ , sélectionnez Regrouper par ‣ Produit pour organiser tous les
enregistrements par produit. Cliquez sur l’icône grise ▶️ (triangle déroulant)
pour faire apparaître les lignes de valorisation des stocks, ainsi qu’un
bouton sarcelle ➕ (plus) à droite.

Cliquez sur le bouton sarcelle \+ (plus) pour ouvrir le formulaire de
revalorisation du produit. Ce formulaire permet de recalculer la valeur des
stocks d’un produit, en augmentant ou en diminuant le prix unitaire de chaque
produit.

Note

Les boutons ▶️ (triangle déroulant) et ➕ (plus) ne sont visibles qu’après
avoir regroupé les entrées par produit.

![Le formulaire de revalorisation du produit ajoutant un montant de 1,00 $ en
raison de l'inflation.](../../../../../_images/product-revaluation.png)

### Pièces comptables pour la valorisation des stocks

Dans Odoo, les enregistrements de valorisation automatique des stocks sont
également enregistrés dans l’application Comptabilité ‣ Comptabilité ‣ Pièces
comptables. Dans cette liste exhaustive des pièces comptables, les
enregistrements de valorisation des stocks sont identifiés en vérifiant les
valeurs dans la colonne Journal ou en recherchant la valeur de la colonne
Référence de l’opération d’entrepôt (par ex. `WH/IN/00014` pour les
réceptions).

Si vous cliquez sur une pièce comptable de valorisation des stocks, un
enregistrement de _comptabilité en partie double_. Ces enregistrements sont
générés par Odoo afin de suivre la variation de la valeur de l’inventaire au
fur et à mesure que les produits entrent et sortent de l’entrepôt.

Example

Pour voir la valorisation des stocks de 10 _tables_ , d’une valeur de 10,00 $
chacune, lors de la réception du fournisseur, allez à la page Pièces
comptables accessible via Comptabilité ‣ Comptabilité ‣ Pièces comptables.
Cliquez sur l’écriture comptable dont la valeur de la colonne Référence
correspond à la référence sur la réception, `WH/IN/00014`.

![La page de la valorisation des stocks décrivant les produits d'une
expédition.](../../../../../_images/stock-valuation-product.png)

`Stock provisoire` est un compte d’attente de l’argent destiné à payer le
produit aux fournisseurs. Le compte `valorisation des stocks` contient la
valeur de tout le stock disponible.

![Pièce comptable pour la valorisation des stocks de 10
tables.](../../../../../_images/inventory-valuation-entry.png)

Pour plus d'infos

[Tutoriels Odoo : Valorisation des
stocks](https://www.odoo.com/slides/slide/2795/share)

