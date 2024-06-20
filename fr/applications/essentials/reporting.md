# Analyse

Vous trouverez plusieurs rapports dans le menu Analyse de la plupart des
applications, qui vous permettent d’analyser et de visualiser les données de
vos enregistrements.

## Sélectionner une vue

En fonction du rapport, Odoo peut afficher les données de différentes
manières. Parfois, une vue unique entièrement adaptée au rapport est
disponible, tandis que plusieurs vues sont disponibles pour d’autres.
Cependant, deux vues génériques sont dédiées aux rapports : la vue graphique
et la vue tableau croisé dynamique.

### Vue graphique

La vue graphique est utilisée pour visualiser les données de vos
enregistrements et vous aider à identifier les modèles et les tendances. La
vue se trouve souvent dans le menu Analyse des applications, mais elle peut
aussi se trouver ailleurs. Cliquez sur le **bouton de la vue graphique** situé
en haut à droite pour y accéder.

![Sélectionner la vue graphique](../../_images/graph-button.png)

### Vue tableau croisé dynamique

La vue tableau croisé dynamique est utilisée pour agréger les données de vos
enregistrements et les décomposer à des fins d’analyse. Cette vue se trouve
souvent dans le menu Analyse des applications, mais elle peut aussi se trouver
ailleurs. Cliquez sur le **bouton de la vue tableau croisé dynamique** situé
en haut à droite pour y accéder.

![Sélectionner la vue tableau croisé dynamique](../../_images/pivot-
button.png)

## Choisir les mesures

Après avoir sélectionné une vue, vous devez vous assurer que seuls les
enregistrements pertinents sont [filtrés](search.html). Ensuite, vous devez
choisir ce qui est mesuré. Par défaut, une mesure est toujours sélectionnée.
Si vous voulez la modifier, cliquez sur Mesures et choisissez une mesure ou,
pour les tableaux croisés dynamiques, plusieurs mesures.

Note

Lorsque vous sélectionnez une mesure, Odoo agrège les valeurs enregistrées sur
ce champs pour les enregistrements filtrés. Seuls les champs numériques
([entiers](../studio/fields.html#studio-fields-simple-fields-integer),
[décimaux](../studio/fields.html#studio-fields-simple-fields-decimal),
[monétaires](../studio/fields.html#studio-fields-simple-fields-monetary))
peuvent être mesurés. De plus, l’option Comptage permet de compter le nombre
total d’enregistrements filtrés.

Après avoir choisi ce que vous voulez mesurer, vous pouvez définir comment les
données doivent être [regroupées](search.html#search-group) en fonction de la
dimension que vous voulez analyser. Par défaut, les données sont souvent
regroupées par _Date > Mois_, ce qui permet d’analyser l’évolution d’une
mesure au fil des mois.

Astuce

Lorsque vous filtrez une période unique, l’option de comparaison avec une
autre période apparaît.

![Utiliser l'option de comparaison](../../_images/comparison.png)

Example

Select measuresGroup measures

Parmi d’autres mesures, vous pouvez ajouter les mesures Marge et Comptage au
rapport d’analyse des ventes. Par défaut, la mesure Montant hors taxes est
sélectionnée.

![Sélectionner différentes mesures sur le rapport d'analyse des
ventes](../../_images/measures.png)

Vous pouvez regrouper des mesures par Catégorie de produit au niveau des
lignes sur l’exemple du rapport d’analyse des ventes précédent.

![Ajouter un groupe au rapport d'analyse des ventes](../../_images/single-
group.png)

## Utiliser la vue tableau croisé dynamique

Le regroupement des données est un élément essentiel du tableau croisé
dynamique. Il permet d’approfondir les données afin d’obtenir des informations
plus détaillées. Vous pouvez utiliser l’option Regrouper par pour ajouter
rapidement un groupe au niveau des lignes, comme le montre l’exemple ci-
dessus, mais vous pouvez également cliquer sur le bouton plus (➕) à côté de
l’en-tête Total au niveau des lignes _et_ des colonnes, puis sélectionner un
des **groupes préconfigurés**. Pour en enlever un, cliquez sur le bouton moins
(➖).

Une fois que vous avez ajouté un groupe, vous pouvez en ajouter de nouveaux
sur l’axe opposé ou sur les sous-groupes nouvellement créés.

Example

Vous pouvez davantage diviser les mesures sur le rapport d’analyse des ventes
précédent par le groupe Vendeur au niveau des colonnes et par le groupe Date
de la commande > Mois sur la catégorie de produit All / Saleable / Office
Furniture.

![Ajouter plusieurs groupes au rapport d'analyse des
ventes](../../_images/multiple-groups.png)

Astuce

  * Changez les groupes de lignes et de colonnes en cliquant sur le bouton d’inversion des axes (⇄).

  * Cliquez sur le libellé d’une mesure pour trier les valeurs par ordre croissant (⏶) ou décroissant (⏷).

  * Téléchargez une version `.xlsx` du tableau croisé dynamique en cliquant sur le bouton de téléchargement (⭳).

## Utiliser la vue graphique

Trois graphiques sont disponibles : le graphique à barres, le graphique
linéaire et le graphique circulaire.

Les **graphiques à barres** sont utilisés pour afficher la distribution ou la
comparaison de plusieurs catégories. Ils sont particulièrement utiles, car ils
permettent de traiter des ensembles de données plus importants.

Les **graphiques linéaires** sont utiles pour afficher des séries temporelles
changeantes et des tendances dans le temps.

Les **graphiques circulaires** sont utilisés pour afficher la distribution ou
la comparaison d’un petit nombre de catégories lorsqu’elles forment un
ensemble significatif.

Bar chartLine chartPie chart

![Visualiser le rapport d'analyse des ventes sous forme de graphique à
barres](../../_images/bar.png)

![Visualiser le rapport d'analyse des ventes sous forme de graphique
linéaire](../../_images/line.png)

![Visualiser le rapport d'analyse des ventes sous forme de graphique
circulaire](../../_images/pie.png)

Astuce

Pour les graphiques à **barres** et **linéaires** , vous pouvez utiliser
l’option Empilé lorsque vous analysez au moins deux groupes, qui apparaissent
alors l’un au-dessus de l’autre au lieu de se trouver l’un à côté de l’autre.

Stacked bar chartRegular bar chartStacked line chartRegular line chart

![Exemple de graphique à barres empilées](../../_images/stacked-bar.png)

![Exemple de graphique à barres non empilées](../../_images/non-stacked-
bar.png)

![Exemple de graphique linéaire empilé](../../_images/stacked-line.png)

![Exemple de graphique linéaire non empilé](../../_images/non-stacked-
line.png)

Pour les graphiques **linéaires** , vous pouvez utiliser l’option Cumulatif
pour additionner les valeurs, ce qui est particulièrement utile pour montrer
l’évolution de la croissance sur une période donnée.

Cumulative line chartRegular line chart

![Exemple de graphique linéaire cumulatif](../../_images/cumulative.png)

![Exemple de graphique linéaire normal](../../_images/non-cumulative.png)

