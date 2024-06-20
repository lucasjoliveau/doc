# Expédition de plusieurs colis

Dans certains cas, une livraison comportant plusieurs articles doit être
expédiée dans plusieurs colis. Cela peut s’avérer nécessaire si les articles
sont trop volumineux pour être expédiés dans un seul colis ou si certains
articles ne peuvent pas être emballés ensemble. L’expédition d’une seule
livraison en plusieurs colis offre une certaine flexibilité quant à
l’emballage de chaque article, sans qu’il ne soit nécessaire de créer
plusieurs livraisons.

## Configuration

Pour diviser une livraison en plusieurs colis, le paramètres _Colis_ doit être
activé. Pour ce faire, allez à Inventaire ‣ Configuration ‣ Paramètres, puis
cochez la case à côté de Colis. Cliquez sur Enregistrer pour confirmer la
modification.

![Le paramètre Colis sur la page des paramètres de l'application
Inventaire.](../../../../../_images/packages-setting.png)

## Expédier des articles dans plusieurs colis

Pour répartir les articles d’une même livraison dans plusieurs colis, allez à
Inventaire ‣ Bons de livraison, puis sélectionnez un bon de livraison qui a
plusieurs articles, une quantité multiple du même article, ou les deux.

Dans l’onglet Opérations, sélectionnez l’icône ⁞≣ (menu) sur la ligne du
produit qui sera expédié dans le premier colis.

![L'icône de menu pour un produit dans un bon de
livraison.](../../../../../_images/product-menu-icon.png)

Cela fait apparaître une fenêtre contextuelle Opérations détaillées. Dans le
tableau au bas de la fenêtre contextuelle, la colonne Réservé montre la
quantité totale du produit inclus dans le bon de livraison.

Si la totalité de la quantité sera expédiée dans le premier colis, saisissez
le nombre de la colonne Fait dans la colonne Réservé. Si la quantité expédiée
dans le premier colis est inférieure à la quantité totale, saisissez un nombre
inférieur à celui qui apparaît dans la colonne Réservé. Cliquez sur Confirmer
pour confirmer les quantités de la colonne Fait et fermer la fenêtre
contextuelle.

![La fenêtre contextuelle des opérations détaillées pour un produit d'un bon
de livraison.](../../../../../_images/detailed-operations2.png)

Répétez les mêmes étapes pour chaque quantité d’article incluse dans le
premier colis. Cliquez ensuite sur Mettre en colis pour créer un colis avec
tous les articles sélectionnés.

![Le bouton Mettre en colis sur un bon de
livraison.](../../../../../_images/put-in-pack1.png)

Pour le colis suivant, suivez les mêmes étapes que celles décrites ci-dessus,
en marquant la quantité de chaque article à inclure dans le premier colis
comme étant Fait avant de cliquer sur Mettre en colis sur le bon de livraison.
Continuez ainsi jusqu’à ce que la quantité totale de tous les articles soit
ajoutée à un colis.

Enfin, lorsque tous les colis ont été expédiés, cliquez sur Valider pour
confirmer que le bon de livraison a bien été exécuté.

Astuce

Après la création d’un ou de plusieurs colis, un bouton intelligent Colis
apparaît dans le coin supérieur droit du bon de livraison. Cliquez sur le
bouton intelligent Colis pour accéder à la page Colis du bon de livraison, où
vous pouvez sélectionner chaque colis pour afficher tous les articles qu’il
contient.

![Le bouton intelligent Colis sur un bon de
livraison.](../../../../../_images/packages-smart-button.png)

## Créer un reliquat pour les articles à expédier plus tard

Si certains articles seront expédiés plus tard que d’autres, il n’est pas
nécessaire de les mettre dans un colis jusqu’à ce qu’ils soient prêts à être
expédiés. Créez plutôt un reliquat pour les articles qui seront expédiés plus
tard.

Commencez par expédier les articles qui seront expédiés immédiatement. S’ils
doivent être envoyés en plusieurs colis, suivez les étapes susmentionnées pour
les emballer comme il se doit. S’ils sont expédiés en un seul colis, notez
simplement la quantité de chaque article expédié dans la colonne Fait, mais ne
cliquez **pas** sur le bouton Mettre en colis.

Une fois que toutes les quantités expédiées immédiatement sont marquées comme
Fait, cliquez sur le bouton Valider et une fenêtre contextuelle Créer un
reliquat ? s’affiche. Cliquez ensuite sur le bouton Créer un reliquat. Cette
opération confirme les articles expédiés immédiatement et crée un nouveau bon
de livraison pour les articles qui seront expédiés plus tard.

![La fenêtre contextuelle Créer un reliquat
?](../../../../../_images/backorder-pop-up.png)

Le reliquat sera répertorié dans le chatter du bon de livraison d’origine dans
un message disant Le reliquat WH/OUT/XXXXX a été créé.. Cliquez sur
WH/OUT/XXXXX dans le message pour afficher le reliquat.

![Le reliquat répertorié dans le chatter du bon de livraison
d'origine.](../../../../../_images/backorder-chatter.png)

Vous pouvez accéder au reliquat en allant à Inventaire, en cliquant sur le
bouton # Reliquats sur la carte des Bons de livraison et en sélectionnant le
bon de livraison.

![Le bouton Reliquats sur la carte des bons de
livraison.](../../../../../_images/back-orders-button.png)

Lorsque les articles restants sont prêts à être expédiés, allez au reliquat.
Les articles peuvent être envoyés en un seul colis en cliquant sur Valider et
en sélectionnant Appliquer dans la fenêtre contextuelle Transfert immédiat ?
qui s’affiche, ou envoyés dans plusieurs colis en suivant les étapes
détaillées dans la section ci-dessus.

Il est également possible d’expédier une partie des articles tout en créant un
autre reliquat pour le reste. Pour ce faire, suivez simplement les mêmes
étapes que celles utilisées pour créer le premier reliquat.

