# Métriques de campagne

Les _métriques de campagne_ sont des statistiques et des analyses détaillées
d’une campagne de marketing, qui en mesurent le succès et l’efficacité. Les
activités de marketing déclenchées remplissent les blocs d’activité avec des
métriques en temps réel, dans le formulaire de détail de la campagne.

## Analyse des activités

Dans la section **Flux de travail** d’un formulaire de marketing dans l”
_application Marketing Automation_ , où se trouvent les différentes activités
de la campagne, vous trouverez une série de données utiles sur chaque bloc
d’activité individuel, comme le nombre de communications **Envoyées** , le
pourcentage de messages qui ont été **Cliqués** , et bien plus encore.

![Un bloc d'activité dans la section Flux de de travail avec des données
analytiques intéressantes dans Konvergo ERP.](../../../../_images/activity-analytics-
block-sample.png)

À gauche du bloc d’activité est affiché le [temps de
déclenchement](../getting_started/workflow_activities) configuré sous
forme de durée (soit **Heures** , **Jours** , **Semaines** , ou **Mois**) s’il
correspond à la période après le début du flux de travail.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le temps de déclenchement dépend d’une autre activité ou d’une action de déclenchement (par ex. <b>Email : Répondu</b>, etc.) le temps est affiché, ainsi que l’action nécessaire pour que cette activité soit activée (par ex. <code>Répondu après 2 Heures</code>).</p>
<img alt="L'affichage des déclencheurs de temps dépend d'une autre activité dans Konvergo ERP Marketing Automation." class="align-center" src="../../../../_images/replied-after-activity-time-trigger.png"/>
</div>

Dans le bloc d’activité, une icône représente chaque type d’activité. Une
icône d’enveloppe **✉️** signifie que l’activité est un email. Ces trois
petites icônes d’engrenage **⚙️** signifient que l’activité est une action
interne. Et une petite icône basique de téléphone portable **📱** signifie que
l’activité est un SMS.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Le nom du type d’activité est également affiché en plus petits caractères sous le titre de l’activité.</p>
</div>

À côté de l’icône de l’activité, en haut du bloc d’activité, se trouve le
titre de l’activité. À droite du titre de l’activité, se trouvent les boutons
**Modifier** et **Supprimer**.

Cliquez sur **Modifier** pour ouvrir le formulaire contextuel **Ouvrir :
Activités** pour modifier cette activité spécifique. Cliquez sur le bouton
**Supprimer** pour supprimer complètement cette activité spécifique du flux de
travail.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../getting_started/workflow_activities">Activités du flux de travail de la campagne</a></p>
</div>

### Onglet du graphique d’activité

Dans chaque bloc d’activité, l’onglet **Graphique (icône du graphique
circulaire)** est ouvert par défaut, affichant les métriques connexes sous la
forme d’un simple graphique linéaire. Les métriques de réussite sont affichées
en `vert` et les métriques de rejet sont affichées en `rouge`.

Les représentations numériques des **Réussites** et des **Échecs** sont
affichées à droite du graphique linéaire.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Survolez n’importe quel point du graphique linéaire du bloc d’activité pour faire apparaître une explication détaillée des données pour cette date spécifique.</p>
<img alt="Le fait de survoler n'importe quel point du graphique linéaire permet d'afficher une explication détaillée dans Konvergo ERP." class="align-center" src="../../../../_images/graph-breakdown-data.png"/>
</div>

Sous le graphique du bloc d’activité, pour les types d’activité _Email_ ou
_SMS_ , une ligne de données accessibles fournit une vue d’ensemble de
l’activité de la campagne, y compris : **Envoyé** (valeur numérique),
**Cliqué** (pourcentage), **Répondu** (pourcentage), et **Rejeté**
(pourcentage).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>En cliquant sur l’une de ces statistiques sur la ligne <b>DÉTAILS</b>, sous le graphique linéaire, vous accédez à une page séparée contenant chaque enregistrement spécifique pour ce point de données particulier.</p>
</div>

### Onglet du filtre de l’activité

À côté de l’onglet **Graphique** du bloc d’activité, vous avez l’option
d’ouvrir un onglet **Filtre** (représenté par une icône de
**filtre/entonnoir**).

![Représentation d'un onglet de filtre d'une activité de campagne dans Konvergo ERP
Marketing Automation.](../../../../_images/activity-filter-tab.png)

En cliquant sur l’onglet **Filtre** sur un bloc d’activité, vous pouvez voir
les filtres spécifiques de cette activité de campagne spécifique et combien
d’enregistrements dans la base de données correspondent à ces critères
spécifiques.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>En cliquant sur le lien des <b>enregistrements</b> sous le filtre affiché, une fenêtre contextuelle séparée s’ouvre et contient une liste de tous les enregistrements qui correspondent aux règles de cette activité de campagne spécifique.</p>
</div>

## Tracker de liens

Konvergo ERP suit toutes les URL utilisées dans les campagnes de marketing. Pour
accéder à ces URL et les analyser, allez à l’application Marketing Automation
‣ Analyse ‣ Tracker de liens. Cette option fait apparaître la page des
**Statistiques des liens** , qui permet d’analyser toutes les URL liées à une
campagne.

![Représentation d'un onglet de filtre d'une activité de campagne dans Konvergo ERP
Marketing Automation.](../../../../_images/campaign-link-tracker.png)

L’affichage par défaut de la page **Statistiques des liens** est la vue
**Graphique à barres** , mais il existe d’autres options d’affichage,
accessibles dans le coin supérieur gauche. Vous avez la possibilité d’afficher
les statistiques sous la forme d’un **Graphique linéaire** ou d’un **Graphique
circulaire**.

En outre, il est également possible d’afficher les statistiques sous forme
d”**Empilement** , et les données peuvent être classées par ordre
**croissant** ou **décroissant**.

À l’extrême gauche des options d’affichage, vous trouverez le menu déroulant
**Mesures**. Lorsque vous cliquez dessus, vous avez les options d’afficher le
**Nombre de clics** ou le **Comptage** total. À droite du menu déroulant
**Mesures** , il est possible d’ajouter des données à une feuille de calcul en
cliquant sur le bouton **Insérer dans une feuille de calcul**.

De plus, dans le coin supérieur droit de la page **Statistiques des liens** ,
à l’extrême droite de la barre de recherche, des options d’affichage
supplémentaires sont disponibles : la vue **Graphique** par défaut, la vue
**Tableau croisé dynamique** et la vue **Liste**.

## Suivis

Konvergo ERP suit toutes les activités utilisées dans chaque campagne de marketing.
Les données liées à ces activités sont accessibles et analysées sur la page
**Suivis** , disponible en allant à l’application Marketing Automation ‣
Analyse ‣ Suivis.

![La page des suivis dans l'application Konvergo ERP Marketing
Automation.](../../../../_images/traces-page-marketing-automation.png)

L’affichage par défaut sur la page des **Suivis** est la vue **Graphique à
barres** , mais d’autres options d’affichage sont disponibles dans le coin
supérieur gauche. Il est possible d’afficher les statistiques sous forme de
**Graphique linéaire** ou **Graphique circulaire**.

En haut du graphique, il y a une légende des couleurs, informant l’utilisateur
quelles activités ont été **Traitées** , **Planifiées** , et **Refusées**. Il
y a également un indicateur de contour pour informer les utilisateurs de la
**Somme** de certaines activités.

Outre les différentes options d’affichage dans le coin supérieur gauche de la
page **Suivis** , il est également possible d’afficher les statistiques sous
forme d”**Empilement** , et les données peuvent être classées dans un ordre
**croissant** ou **descendant**.

À l’extrême gauche des options d’affichage, se trouve le menu déroulant
**Mesures**. Lorsque vous cliquez dessus, vous avez la possibilité d’afficher
l”**ID Document** ou le **Comptage** total. De plus, à droite du menu
déroulant **Mesures** , il est possible d’ajouter toutes les données dans une
feuille de calcul en cliquant sur le bouton **Insérer dans une feuille de
calcul**.

De plus, dans le coin supérieur droit de la page **Statistiques des liens** ,
à l’extrême droite de la barre de recherche, des options d’affichage
supplémentaires sont disponibles : la vue **Graphique** par défaut, la vue
**Tableau croisé dynamique** et la vue **Liste**.

## Participants

Konvergo ERP suit tous les participants liés à chaque campagne de marketing. Les
données relatives à ces participants peuvent être consultés et analyses sur la
page **Participants** , accessible dans l’application Marketing Automation ‣
Analyse ‣ Participants.

![La page des Participants dans l'application Konvergo ERP Marketing
Automation.](../../../../_images/participants-page-marketing-automation.png)

L’affichage par défaut de la page **Participants** est le **Graphique
circulaire** , mais d’autres options d’affichage sont disponibles dans le coin
supérieur gauche. Il est possible d’afficher les statistiques sous forme de
**Graphique linéaire** ou de **Graphique à barres**.

En haut du graphique, il y a une légende des couleurs qui indique le type de
participants que vous trouverez dans le graphique.

À l’extrême gauche des options d’affichage, vous avez le menu déroulant
**Mesures**. Lorsque vous cliquez dessus, vous pouvez afficher l”**ID de
l’enregistrement** ou le **Comptage**. À droite du menu déroulant **Mesures**
, il est possible d’ajouter toutes les données dans une feuille de calcul en
cliquant sur le bouton **Insérer dans une feuille de calcul**.

De plus, dans le coin supérieur droit de la page **Statistiques des liens** ,
à l’extrême droite de la barre de recherche, des options d’affichage
supplémentaires sont disponibles : la vue **Graphique** par défaut, la vue
**Tableau croisé dynamique** et la vue **Liste**.

