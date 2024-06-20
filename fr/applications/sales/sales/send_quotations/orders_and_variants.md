# Variantes de produits sur les devis et les commandes

Avant d’entrer dans les détails de l’utilisation des variantes de produits sur
les devis et les commandes, il est recommandé d’apprendre ce que sont les
[Variantes de produit](../products_prices/products/variants.html) dans Odoo.

Une fois familiarisé avec les bases sur les variantes de produits, la section
suivante couvre la façon dont les variantes peuvent être ajoutées aux devis et
commandes à l’aide du _configurateur de produit_ ou la _grille des variantes_.

Note

Il convient de noter que le paramètre s’intitule _Grille d’entrée de
variantes_ dans les paramètres de l’application _Ventes_ et s’intitule _Grille
des variantes de produits_ dans les formulaires de produits. Gardez donc cela
à l’esprit.

## Paramètres

Lorsque vous travaillez avec des variantes de produits, Odoo utilise par
défaut le configurateur de produits. Pour ajouter l’option de la grille
d’entrée des variantes, cette fonctionnalité **doit** être activée dans
l’application Odoo _Ventes_. L’option de la grille d’entrée des variantes
fournit une fenêtre contextuelle sur le devis/la commande pour simplifier le
processus de sélection des variantes.

Pour activer ce paramètre, allez à l’application Ventes ‣ Configuration ‣
Paramètres et faites défiler jusqu’à la section Catalogue de produits.
Ensuite, cochez la case à côté de l’option Grille d’entrée des variantes et
cliquez sur Enregistrer.

![Le paramètre de la grille d'entrée des variantes dans l'application Odoo
Ventes.](../../../../_images/order-grid-entry-setting.png)

Note

Bien évidemment, la fonctionnalité Variantes **doit** également être activée
pour pouvoir utiliser des variantes de produits dans les devis et les
commandes.

## Configuration du produit

Une fois que le paramètre Grille d’entrée des variantes est activé, les deux
options (_Configurateur de produits_ et _Grille des variantes_) deviennent
disponibles sur chaque formulaire de produit.

Pour configurer un formulaire de produit afin d’utiliser un configurateur de
produits ou une grille d’entrée des variantes, allez à l’application Ventes ‣
Produits ‣ Produits pour voir tous les produits de la base de données.

Ensuite, sélectionnez le produit que vous voulez configurer ou cliquez sur
Nouveau pour créer un nouveau produit à partir de zéro. Sur le formulaire de
produit, cliquez sur l’onglet Attributs & Variantes où vous pouvez afficher,
modifier et ajouter des variantes de produits.

Au bas de l’onglet Attributs & Variantes se trouve une section Sélection des
variantes de vente avec deux options : Configurateur de produits et Grille des
variantes du produit.

Note

Il convient de noter que ces deux options apparaissent **uniquement** si au
moins deux valeurs d’un attribut ont été ajoutées à l’enregistrement.

![Options de sélection des variantes dans l'onglet Attributs et Variantes d'un
formulaire de produit.](../../../../_images/attributes-variants-tab-selection-
options.png)

Ces options déterminent la méthode utilisée pour ajouter des variantes de
produits aux devis ou aux commandes.

Le Configurateur de produits ouvre une fenêtre contextuelle qui affiche
clairement toutes les variantes disponibles de ce produit en particulier
lorsqu’il est ajouté à un devis. Toutefois, une seule variante peut être
sélectionnée/ajoutée à la fois.

La Grille des variantes fournit les mêmes informations que le Configurateur de
produits dans un tableau, ce qui permet aux utilisateurs de sélectionner un
plus grand nombre de variantes et de les ajouter à un devis/une commande, dans
une seule vue.

## Configurateur de produits

Le configurateur de produits apparaît sous forme de fenêtre contextuelle de
Configuration dès qu’un produit avec des variantes (au moins deux) est ajouté
au devis ou à la commande, mais **seulement si** l’option Configurateur de
produits est sélectionnée dans le formulaire.

![La fenêtre contextuelle du configurateur de produits qui apparaît sur un
devis ou une commande.](../../../../_images/product-configurator-window.png)

Note

Cette fenêtre contextuelle de Configuration apparaît aussi si le paramètre
Grille des variantes n’est **pas** activé, car il s’agit de l’option par
défaut qu’Odoo utilise lorsqu’il traite des variantes de produits sur les
devis et/ou les commandes.

Avec le Configurateur de produits, les vendeurs peuvent choisir exactement la
variante à ajouter au devis ou à la commande en utilisant un format similaire
à celui des achats en ligne.

## Grille des variantes du produit

La grille des variantes apparaît sous forme de fenêtre contextuelle Choisissez
des variantes de produit, dès qu’un produit avec variantes (au moins deux) est
ajouté à un devis ou une commande, mais **seulement si** l’option Grille des
variantes est sélectionnée dans le formulaire.

![La fenêtre contextuelle permettant de choisir des variante qui apparaît sur
un devis dans Odoo.](../../../../_images/choose-product-variants-popup.png)

La fenêtre contextuelle Choisissez des variantes de produit affiche toutes les
variantes de ce produit en particulier. Dans cette fenêtre, le vendeur peut
désigner la quantité de chaque variante qu’il souhaite ajouter au devis/à la
commande en une seule fois.

Lorsque toutes les quantités et variantes souhaitées ont été sélectionnées, le
vendeur n’a plus qu’à cliquer sur Confirmer, et ces commandes sont
immédiatement ajoutées au devis/à la commande dans l’onglet Lignes de
commande.

![L'onglet Lignes de commande rempli après avoir choisi la grille des
variantes pour sélectionner des produits.](../../../../_images/order-grid-
entry-order-lines-tab.png)

Pour plus d'infos

[Variantes de produit](../products_prices/products/variants.html)

