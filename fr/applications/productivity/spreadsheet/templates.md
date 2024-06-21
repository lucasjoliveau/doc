# Modèles

Les modèles de feuilles de calcul vous permettent de créer rapidement des
feuilles de calcul sans partir de zéro.

Plusieurs modèles prédéfinis sont disponibles lors de la création d’une
nouvelle feuille de calcul à partir de l’application **Documents** , tels que
:

  * les rapports budgétaires,

  * les rapports sur les revenus du pipeline, ou

  * le rapport de commission de vente.

![Vue de tous les modèles par défaut](../../../_images/report-templates.png)

Vous pouvez également enregistrer n’importe quelle feuille de calcul en tant
que modèle et gérer et modifier des modèles existants.

## Modèles par défaut

### Comptabilité : rapports budgétaires

Les rapports budgétaires comparent les dépenses réelles d’une entreprise à son
budget sur une période définie. Deux modèles sont disponibles : l’un utilise
des intervalles trimestriels (**Rapport budgétaire (Trimestriel)**), tandis
que l’autre utilise des intervalles mensuels (**Rapport budgétaire
(Mensuel)**).

![Extrait d'un rapport budgétaire](../../../_images/budget-report.png)

Les cellules de la colonne **Réalisations** sont remplies automatiquement avec
les montants réalisés et dépensés au cours de la période correspondante (mois
ou trimestre). Les données sont extraites des écritures comptables dans les
[comptes de charges et de
produits](../../finance/accounting/get_started/chart_of_accounts#chart-
of-account-type).

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les écritures comptables dans le type de compte <b>Autres revenus</b> ne sont pas pris en compte lors de la collecte des données.</p>
</div>

Pour analyser la performance du budget, indiquez dans les cellules de la
colonne **Budget** le montant des recettes (lignes **Produits**) et des
dépenses (lignes **Charges**) que vous prévoyez de réaliser sur la période
concernée et par compte. Ensuite, la colonne performance (**Perf.**) compare
les **Réalisations** au budget correspondant, exprimé en pourcentage.

Enfin, la ligne **Bénéfice net** représente les **Produits** totaux moins les
**Charges** totales pour les colonnes **Réalisations** et **Budget**.

### CRM : rapports sur les revenus du pipeline

Deux rapports sur les revenus du pipeline sont disponibles. Le **rapport sur
les revenus du pipeline (mensuel)** est consacré aux revenus uniques (NRR),
alors que le **rapport sur les revenus du pipeline MRR/NRR (mensuel)**
concerne les revenus récurrents et non récurrents (MRR).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Activez les <b>Revenus récurrents</b> en allant à CRM ‣ Configuration ‣ Paramètres.</p>
</div> ![Extrait d'un rapport sur les revenus du
pipeline](../../../_images/pipeline-revenue.png)

Les cellules dans la colonne **Réalisations** sont complétées automatiquement
avec le montant des revenus mensuels des opportunités **gagnées**.

Pour calculer la performance des revenus, complétez les objectifs de revenus
mensuels.

  * Pour la feuille **Revenus par Équipe** , complétez les cellules dans les colonnes **Objectif** pour chaque équipe commerciale.

  * Pour la feuille **Revenus par Vendeur** , ouvrez la feuille **Objectifs** et remplissez les cellules à côté de chaque vendeur. Utilisez le tableau **Facteur mensuel** ci-dessous pour adapter les objectifs principaux en fonction du mois de l’année.

Ensuite la colonne performance (**Perf.**) compare les **Réalisations** à leur
budget correspondant, exprimé en pourcentage.

Enfin, la colonne **Prévisions** regroupe les revenus mensuels des pistes
multipliés par leur pourcentage de **Probabilité**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour les réalisations et les prévisions :</p>
<ul>
<li><p>La date de <b>Clôture prévue</b> figurant sur les pistes est utilisée pour les assigner à un mois.</p></li>
<li><p>Le revenu mensuel récurrent est utilisé même si le nombre de mois du plan récurrent est défini sur une valeur différente de 1 mois. Par exemple, le revenu d’un plan annuel est divisé par 12 mois.</p></li>
</ul>
</div>

### Ventes : commission de vente

Ce rapport présente la commission mensuelle gagnée ou due à chaque vendeur.

![Extrait d'un rapport de commission de vente](../../../_images/sales-
commission.png)

La colonne **Taux** est préremplie avec le pourcentage de l’onglet **Taux** ,
qui peut être personnalisé pour chaque catégorie de produits en fonction de la
politique de la société. L’ajustement du taux pour une catégorie de produits
spécifique met automatiquement à jour le montant de la commission pour cette
catégorie.

La colonne **Facturé** indique le montant total des factures non taxées,
regroupées par vendeur et par mois.

Enfin, la colonne **Comm.** est calculée en multipliant le montant facturé par
le pourcentage du taux.

## Enregistrer une feuille de calcul en tant que modèle

N’importe quelle feuille de calcul peut être enregistrée en tant que modèle. À
partir de la barre de menu, cliquez sur Fichier ‣ Enregistrer en tant que
modèle. Modifiez le **Nom du modèle** par défaut si nécessaire et cliquez sur
**Confirmer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les modèles sont accessibles à tous les utilisateurs sur la base de données.</p>
</div>

## Gérer et modifier les modèles

Gérez les modèles en allant aux Documents ‣ Configuration ‣ Modèles de feuille
de calcul. Supprimez le [filtre](../../essentials/search#search-
preconfigured-filters) **Mes modèles** pour afficher tous les modèles dans la
base de données.

Pour modifier un modèle existant, cliquez sur `✎ Modifier` à côté du modèle
souhaité. Les modifications sont enregistrées automatiquement.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Utilisez le bouton de téléchargement sous la colonne <b>Données</b> pour exporter un modèle au format JSON. Le fichier peut être importé dans une autre base de données.</p>
</div>

  *[NRR]: Revenu non récurrent
  *[MRR]: Revenu mensuel récurrent

