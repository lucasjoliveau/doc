# Utiliser des kits

Dans Odoo, un _kit_ est un type de nomenclature qui peut être fabriqué et
vendu. Les kits sont des ensembles de composants non assemblés vendus aux
clients. Ils peuvent être vendus en tant que produits autonomes, mais sont
également des outils utiles pour gérer des nomenclatures plus complexes.

Note

Pour utiliser, fabriquer et vendre des kits, les applications Fabrication et
Inventaire doivent être installées.

## Créer le kit en tant que produit

Pour utiliser un kit comme produit vendable ou simplement comme outil
d’organisation des composants, le kit doit d’abord être créé en tant que
produit.

Pour créer un kit, allez à l’application Inventaire ‣ Produits ‣ Produits, et
cliquez sur Créer.

Assignez ensuite un nom au nouveau kit. Ensuite, dans l’onglet Informations
générales, définissez le Type de produit sur Consommable. Les kits
fonctionnent mieux en tant que consommables, car le stock disponible pour les
kits ne fait généralement pas l’objet d’un suivi.

Note

Même si les kits doivent presque toujours être définis en tant que produit
consommable, les entreprises qui utilisent la comptabilité **anglo-saxonne**
peuvent avoir besoin de créer des kits en tant que Produit stockable. En
effet, lors du traitement des factures pour les kits, le coût des marchandises
vendues (COGS) sera enregistré dans les journaux comptables.

Contrairement aux produits stockables, la définition des Routes dans l’onglet
Inventaire n’a pas d’importance pour les kits, car Odoo utilise les routes des
composants individuels du kit à des fins de réassort. Tous les autres
paramètres du produit de kit peuvent être modifiés selon les préférences. Une
fois que vous avez terminé, cliquez sur Enregistrer pour enregistrer le
nouveau produit.

Les composants du kit doivent également être configurés en tant que produits
via l’application Inventaire ‣ Produits ‣ Produits. Ces composants ne
nécessitent aucune configuration spécifique.

## Configurer la nomenclature du kit

Après avoir entièrement configuré le kit et ses composants, une nouvelle
nomenclature peut être créée pour le kit.

Allez à l’application Fabrication ‣ Produits ‣ Nomenclatures, et cliquez sur
Créer. À côté du champ Produit, cliquez sur le menu déroulant pour afficher
une liste de produits et sélectionner le produit en kit précédemment
configuré.

Ensuite, dans le champ Type de nomenclature, sélectionnez l’option Kit. Enfin,
dans l’onglet Composants, cliquez sur Ajouter une ligne, ajoutez chaque
composant souhaité et précisez leurs quantités dans la colonne Quantité.

Une fois que vous avez terminé, cliquez sur Enregistrer pour enregistrer la
nomenclature nouvellement créée.

![Sélection de kit sur la nomenclature.](../../../../_images/bom-kit-
selection.png)

Si le kit est uniquement utilisé comme produit vendable, seuls les composants
doivent être ajoutés sous l’onglet Composants et la configuration des
opérations de fabrication n’est pas nécessaire.

Note

Lorsqu’un kit est vendu en tant que produit, il apparaît comme une seule ligne
sur le devis et la commande client. Cependant, sur les bons de livraison,
chaque composant du kit est répertorié.

## Utiliser des kits pour gérer des nomenclatures complexes

Les kits sont également utilisés pour gérer les nomenclatures à plusieurs
niveaux. Ce sont des produits qui contiennent d”**autres** nomenclatures en
tant que composants et qui nécessitent des nomenclatures **imbriquées**.
L’incorporation de kits préconfigurés dans les nomenclatures à plusieurs
niveaux permet de mieux organiser les produits groupés.

Pour configurer ce type de nomenclature avec un kit comme composant, allez à
l’application Fabrication ‣ Produits ‣ Nomenclatures et cliquez sur Créer.

À côté du champ Produit cliquez sur le menu déroulant pour afficher une liste
de produits et sélectionner la nomenclature souhaitée. Dans le champ Type de
nomenclature, sélectionnez l’option Fabriquer ce produit.

Dans l’onglet Composants, cliquez sur Ajouter une ligne et sélectionnez un kit
comme composant. L’ajout du kit en tant que composant évite d’avoir à ajouter
les composants du kit individuellement. N’importe quel Type de nomenclature
peut être utilisé pour la nomenclature du produit de niveau supérieur.

Une fois que vous avez terminé, cliquez sur Enregistrer pour enregistrer les
modifications.

![Kit en tant que composant d'une nomenclature à plusieurs
niveaux.](../../../../_images/multilevel-bom-kit.png)

### Structure & coût

Pour obtenir une vue d’ensemble des composants de la nomenclature à plusieurs
niveaux, cliquez sur le bouton intelligent Structure & Coût. Les nomenclatures
de sous-niveaux peuvent être développées et visualisées à partir de ce
rapport.

![Kit développé dans le rapport Structure &
Coût](../../../../_images/structure-and-cost-kit.png)

Lors de la création d’un ordre de fabrication pour un produit avec une
nomenclature à plusieurs niveaux, le kit se développe automatiquement pour
afficher tous les composants. Toutes les opérations figurant dans la
nomenclature du kit sont également ajoutées à la liste des ordres de travail
de l’ordre de fabrication.

Astuce

Les kits sont principalement utilisés pour regrouper des composants en vue de
leur organisation ou de leur vente. Pour gérer les produits à plusieurs
niveaux qui nécessitent des sous-composants fabriqués, consultez [cette
documentation](sub_assemblies.html) sur les sous-ensembles.

