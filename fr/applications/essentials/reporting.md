# Analyse

Vous trouverez plusieurs rapports dans le menu **Analyse** de la plupart des
applications, qui vous permettent d’analyser et de visualiser les données de
vos enregistrements.

## Sélectionner une vue

En fonction du rapport, Konvergo ERP peut afficher les données de différentes
manières. Parfois, une vue unique entièrement adaptée au rapport est
disponible, tandis que plusieurs vues sont disponibles pour d’autres.
Cependant, deux vues génériques sont dédiées aux rapports : la vue graphique
et la vue tableau croisé dynamique.

### Vue graphique

La vue graphique est utilisée pour visualiser les données de vos
enregistrements et vous aider à identifier les modèles et les tendances. La
vue se trouve souvent dans le menu **Analyse** des applications, mais elle
peut aussi se trouver ailleurs. Cliquez sur le **bouton de la vue graphique**
situé en haut à droite pour y accéder.

![Sélectionner la vue graphique](../../_images/graph-button.png)

### Vue tableau croisé dynamique

La vue tableau croisé dynamique est utilisée pour agréger les données de vos
enregistrements et les décomposer à des fins d’analyse. Cette vue se trouve
souvent dans le menu **Analyse** des applications, mais elle peut aussi se
trouver ailleurs. Cliquez sur le **bouton de la vue tableau croisé dynamique**
situé en haut à droite pour y accéder.

![Sélectionner la vue tableau croisé dynamique](../../_images/pivot-
button.png)

## Choisir les mesures

Après avoir sélectionné une vue, vous devez vous assurer que seuls les
enregistrements pertinents sont [filtrés](search). Ensuite, vous devez
choisir ce qui est mesuré. Par défaut, une mesure est toujours sélectionnée.
Si vous voulez la modifier, cliquez sur **Mesures** et choisissez une mesure
ou, pour les tableaux croisés dynamiques, plusieurs mesures.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsque vous sélectionnez une mesure, Konvergo ERP agrège les valeurs enregistrées sur ce champs pour les enregistrements filtrés. Seuls les champs numériques (<a href="../studio/fields#studio-fields-simple-fields-integer"><span class="std std-ref">entiers</span></a>, <a href="../studio/fields#studio-fields-simple-fields-decimal"><span class="std std-ref">décimaux</span></a>, <a href="../studio/fields#studio-fields-simple-fields-monetary"><span class="std std-ref">monétaires</span></a>) peuvent être mesurés. De plus, l’option <b>Comptage</b> permet de compter le nombre total d’enregistrements filtrés.</p>
</div>

Après avoir choisi ce que vous voulez mesurer, vous pouvez définir comment les
données doivent être [regroupées](search#search-group) en fonction de la
dimension que vous voulez analyser. Par défaut, les données sont souvent
regroupées par _Date > Mois_, ce qui permet d’analyser l’évolution d’une
mesure au fil des mois.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Lorsque vous filtrez une période unique, l’option de comparaison avec une autre période apparaît.</p>
<img alt="Utiliser l'option de comparaison" src="../../_images/comparison.png"/>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Select measures</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">Group measures</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><p>Parmi d’autres mesures, vous pouvez ajouter les mesures <b>Marge</b> et <b>Comptage</b> au rapport d’analyse des ventes. Par défaut, la mesure <b>Montant hors taxes</b> est sélectionnée.</p>
<img alt="Sélectionner différentes mesures sur le rapport d'analyse des ventes" src="../../_images/measures.png"/>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><p>Vous pouvez regrouper des mesures par <b>Catégorie de produit</b> au niveau des lignes sur l’exemple du rapport d’analyse des ventes précédent.</p>
<img alt="Ajouter un groupe au rapport d'analyse des ventes" src="../../_images/single-group.png"/>
</div></div>
</div>

## Utiliser la vue tableau croisé dynamique

Le regroupement des données est un élément essentiel du tableau croisé
dynamique. Il permet d’approfondir les données afin d’obtenir des informations
plus détaillées. Vous pouvez utiliser l’option **Regrouper par** pour ajouter
rapidement un groupe au niveau des lignes, comme le montre l’exemple ci-
dessus, mais vous pouvez également cliquer sur le bouton plus (**➕**) à côté
de l’en-tête **Total** au niveau des lignes _et_ des colonnes, puis
sélectionner un des **groupes préconfigurés**. Pour en enlever un, cliquez sur
le bouton moins (**➖**).

Une fois que vous avez ajouté un groupe, vous pouvez en ajouter de nouveaux
sur l’axe opposé ou sur les sous-groupes nouvellement créés.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Vous pouvez davantage diviser les mesures sur le rapport d’analyse des ventes précédent par le groupe <b>Vendeur</b> au niveau des colonnes et par le groupe <b>Date de la commande &gt; Mois</b> sur la catégorie de produit <b>All / Saleable / Office Furniture</b>.</p>
<img alt="Ajouter plusieurs groupes au rapport d'analyse des ventes" src="../../_images/multiple-groups.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Changez les groupes de lignes et de colonnes en cliquant sur le bouton d’inversion des axes (<b>⇄</b>).</p></li>
<li><p>Cliquez sur le libellé d’une mesure pour trier les valeurs par ordre croissant (⏶) ou décroissant (⏷).</p></li>
<li><p>Téléchargez une version <code>.xlsx</code> du tableau croisé dynamique en cliquant sur le bouton de téléchargement (<b>⭳</b>).</p></li>
</ul>
</div>

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

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour les graphiques à <b>barres</b> et <b>linéaires</b>, vous pouvez utiliser l’option Empilé lorsque vous analysez au moins deux groupes, qui apparaissent alors l’un au-dessus de l’autre au lieu de se trouver l’un à côté de l’autre.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-2-2-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-2-2-0" name="2-0" role="tab" tabindex="0">Stacked bar chart</button><button aria-controls="panel-2-2-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-1" name="2-1" role="tab" tabindex="-1">Regular bar chart</button><button aria-controls="panel-2-2-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-2" name="2-2" role="tab" tabindex="-1">Stacked line chart</button><button aria-controls="panel-2-2-3" aria-selected="false" class="sphinx-tabs-tab" id="tab-2-2-3" name="2-3" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-2-2-0" class="sphinx-tabs-panel" id="panel-2-2-0" name="2-0" role="tabpanel" tabindex="0"><img alt="Exemple de graphique à barres empilées" src="../../_images/stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-1" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-1" name="2-1" role="tabpanel" tabindex="0"><img alt="Exemple de graphique à barres non empilées" src="../../_images/non-stacked-bar.png"/>
</div><div aria-labelledby="tab-2-2-2" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-2" name="2-2" role="tabpanel" tabindex="0"><img alt="Exemple de graphique linéaire empilé" src="../../_images/stacked-line.png"/>
</div><div aria-labelledby="tab-2-2-3" class="sphinx-tabs-panel" hidden="true" id="panel-2-2-3" name="2-3" role="tabpanel" tabindex="0"><img alt="Exemple de graphique linéaire non empilé" src="../../_images/non-stacked-line.png"/>
</div></div>
<p>Pour les graphiques <b>linéaires</b>, vous pouvez utiliser l’option Cumulatif pour additionner les valeurs, ce qui est particulièrement utile pour montrer l’évolution de la croissance sur une période donnée.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-3-3-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-3-3-0" name="3-0" role="tab" tabindex="0">Cumulative line chart</button><button aria-controls="panel-3-3-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-3-3-1" name="3-1" role="tab" tabindex="-1">Regular line chart</button></div><div aria-labelledby="tab-3-3-0" class="sphinx-tabs-panel" id="panel-3-3-0" name="3-0" role="tabpanel" tabindex="0"><img alt="Exemple de graphique linéaire cumulatif" src="../../_images/cumulative.png"/>
</div><div aria-labelledby="tab-3-3-1" class="sphinx-tabs-panel" hidden="true" id="panel-3-3-1" name="3-1" role="tabpanel" tabindex="0"><img alt="Exemple de graphique linéaire normal" src="../../_images/non-cumulative.png"/>
</div></div>
</div>

