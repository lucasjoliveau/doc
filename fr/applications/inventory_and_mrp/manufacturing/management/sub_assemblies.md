# Gérer des produits semi-finis

Un _produit semi-fini_ , également connu comme un _sous-ensemble_ , est un
produit fabriqué qui est utilisé comme composant dans la nomenclature d’un
autre produit. Les produits semi-finis sont utilisés pour simplifier les
nomenclatures plus complexes ou pour représenter plus précisément un flux de
fabrication. Une nomenclature qui contient des produits semi-finis est appelée
_nomenclature à plusieurs niveaux_ , où l’on distingue le _produit de niveau
supérieur_ et ses sous-ensembles.

## Configurer des produits semi-finis

Pour configurer une nomenclature à plusieurs niveaux, le produit de niveau
supérieur et les produits semi-finis doivent être configurés. La première
étape consiste donc à créer les produits semi-finis et leurs nomenclatures.

Pour plus d'infos

[Bill of materials](bill_configuration.html)

![Une nomenclature d'un produit semi-fini.](../../../../_images/semifinished-
product-bom.png)

## Créer la nomenclature de niveau supérieur

Une fois les produits semi-finis entièrement configurés, allez à Fabrication ‣
Produits ‣ Produits. Ensuite, créez le produit de niveau supérieur. Configurez
les spécifications du produit comme vous le souhaitez et assurez-vous de
Enregistrer.

Une fois le produit de niveau supérieur configuré, cliquez sur le bouton
intelligent Nomenclature sur la fiche produit et cliquez sur Créer pour créer
une nomenclature pour le produit de niveau supérieur. Il suffit ensuite
d’ajouter les produits semi-finis à cette nomenclature, ainsi que tout autre
composant nécessaire.

![Une nomenclature pour un produit de niveau supérieur, contenant un composant
de sous-ensemble.](../../../../_images/custom-computer-bom.png)

## Gérer la planification de la production

Il existe plusieurs méthodes pour gérer l’automatisation de l’ordre de
fabrication pour les produits ayant des nomenclatures à plusieurs niveaux.

Note

Les produits semi-finis sont généralement utilisés pour gérer des produits
pouvant être fabriqués avec des nomenclatures à plusieurs niveaux. Si une
nomenclature est créée simplement pour organiser des composants ou regrouper
des produits vendables, l’utilisation des [Kits](kit_shipping.html) est
l’option la plus appropriée.

Pour automatiquement déclencher des ordres de fabrication pour des produits
semi-finis après avoir confirmé un ordre de fabrication pour le produit
principal, il existe deux options :

  * **Option 1 (recommandée) :** Créez des _règles de réassort_ pour les produits semi-finis et fixez à la fois les quantités minimales et maximales de stock souhaitées à `0`.

Pour plus d'infos

[Configurer des règles de réassort](../../purchase/products/reordering.html)

  * **Option 2 :** Activez les routes Réapprovisionner sur commande (MTO) et Fabriquer sous l’onglet Inventaire de la fiche produit des produits semi-finis.

L’option 1 est plus souple que l’option 2 et est donc recommandée. Les règles
de réassort ne relient pas directement la demande au réassort et permettent
donc de ne pas réserver les stocks et de les réorienter vers d’autres
commandes si nécessaire. La route Réapprovisionnement sur commande (MTO) crée
un lien unique entre les produits semi-finis et les produits de niveau
supérieur, en réservant exclusivement les quantités pour l’ordre de
fabrication de niveau supérieur confirmé.

Quelle que soit la méthode choisie, les produits semi-finis doivent être
entièrement fabriqués avant que la fabrication du produit de niveau supérieur
puisse commencer.

![Un ordre de fabrication pour un produit de niveau
supérieur.](../../../../_images/semifinished-on-mo.png)

