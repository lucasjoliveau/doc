# Rebuts pendant la fabrication

Au cours du processus de fabrication, il peut s’avérer nécessaire de mettre au
rebut des composants de fabrication ou des produits finis, par exemple si un
composant ou un produit est endommagé ou inutilisable pour toute autre raison.

Par défaut, la mise au rebut d’un composant ou d’un produit fini le retire de
l’inventaire physique et le place dans un emplacement virtuel intitulé
_Emplacements virtuels/Rebut_. Un emplacement virtuel n’est **pas** un espace
physique, mais plutôt une désignation dans Odoo qui est utilisée pour suivre
les articles qui ne se trouvent plus dans l’inventaire physique.

Odoo _Fabrication_ permet de mettre au rebut à la fois des composants et des
produits finis dans le cadre d’un ordre de fabrication. Le type spécifique
d’article qui peut être mis au rebut au cours d’un ordre de fabrication dépend
de l’étape du processus de fabrication.

Astuce

Les ordres de mise au rebut peuvent être consultés en allant à Inventaire ‣
Opérations ‣ Rebut. Chaque ordre de mise au rebut indique la date et l’heure
de création de l’ordre, ainsi que le produit et la quantité mis au rebut.

Pour afficher la quantité totale de chaque article mis au rebut, allez à
Inventaire ‣ Configuration ‣ Emplacements, puis supprimez le filtre Interne de
la barre Rechercher… pour afficher tous les emplacements virtuels. Dans la
liste, sélectionnez l’emplacement Emplacements virtuels/Rebut.

## Mise au rebut des composants de fabrication

Pour mettre au rebut des composants au cours du processus de fabrication,
allez à Fabrication ‣ Ordres de fabrication, puis sélectionnez un ordre de
fabrication ou cliquez sur Créer pour en configurer un nouveau. Si un nouvel
ordre de fabrication est créé, sélectionnez un produit dans le menu déroulant
Produit, puis cliquez sur Confirmer.

Une fois l’ordre de fabrication confirmé, un bouton Rebut apparaît en haut de
la page. Cliquez sur le bouton et une fenêtre contextuelle Rebut apparaît.

![Le bouton rebut sur un ordre de fabrication.](../../../../_images/scrap-
button.png)

Dans le menu déroulant Produit dans la fenêtre contextuelle Rebut,
sélectionnez le composant mis au rebut, puis saisissez la quantité dans le
champ Quantité. Enfin, cliquez sur Valider pour mettre au rebut le composant.

![La fenêtre contextuelle de rebut.](../../../../_images/scrap-pop-up1.png)

Important

Avant de cliquer sur Marquer comme fait sur un ordre de fabrication, seuls les
composants du produit fini peuvent être mis au rebut, **pas** le produit fini
lui-même. C’est parce qu’Odoo reconnaît que le produit fini ne peut pas être
mis au rebut avant d’avoir été fabriqué.

Après avoir mis au rebut un composant, continuez le processus de fabrication
en utilisant la quantité requise du composant mis au rebut. Le stock
disponible pour le composant mis au rebut est mis à jour pour refléter à la
fois la quantité mise au rebut et la quantité consommée pendant la
fabrication.

Example

Si la fabrication d’une table nécessite quatre unités d’un pied de table et
que deux unités d’un pied de table ont été mises au rebut au cours du
processus de fabrication, la quantité totale de pieds de table consommée sera
de six : quatre unités utilisées pour fabriquer la table, plus deux unités
mises au rebut.

## Mise au rebut de composants à partir de la vue de tablette

Les composants peuvent également être mis au rebut à partir de la vue de
tablette de fabrication. Pour ce faire, sélectionnez l’onglet Ordres de
travail sur un ordre de fabrication, puis cliquez sur l’icône 📱 (vue tablette)
d’un ordre de travail.

![L'icône de la vue tablette d'un ordre de
travail.](../../../../_images/tablet-view-icon.png)

Lorsque la vue tablette est ouverte, cliquez sur le bouton ☰ (menu) en haut à
gauche de l’écran, puis sélectionnez le bouton Rebut dans la fenêtre
contextuelle Menu. La fenêtre contextuelle Rebut s’ouvre alors.

![Le bouton Rebut dans la fenêtre contextuelle Menu de la vue de tablette de
fabrication.](../../../../_images/tablet-scrap-button.png)

Enfin, sélectionnez un composant dans le menu déroulant Produit et saisissez
la quantité mise au rebut dans le champ Quantité. Cliquez sur Valider pour
mettre au rebut le composant.

## Mise au rebut des produits finis

Odoo vous permet également de mettre au rebut des produits finis d’un ordre de
fabrication une fois que l’ordre est terminé. Après avoir cliqué sur Marquer
comme fait, cliquez sur le bouton Rebut pour faire apparaître la fenêtre
contextuelle Rebut.

Étant donné que les composants ont été consommés pour créer le produit fini,
ils n’apparaissent plus dans le menu déroulant Produit. Le produit fini sera
disponible en tant qu’option. Sélectionnez le produit fini et saisissez la
quantité à mettre au rebut dans le champ Quantité. Cliquez sur Valider pour
mettre au rebut le produit fini.

Le stock disponible pour le produit mis au rebut sera mis à jour pour refléter
à la fois la quantité mise à rebut et la quantité produite au cours de la
fabrication.

Example

Si cinq unités d’une chaise ont été fabriquées, mais deux unités ont été mises
au rebut après la fabrication, le stock disponible de la chaise augmentera de
trois unités : cinq unités fabriquées moins deux unités mises au rebut.

