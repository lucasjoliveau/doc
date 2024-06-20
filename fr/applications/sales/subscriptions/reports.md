# Rapports

Comme nous le savons, comprendre comment vont nos affaires et comment ils se
développent, est la clé du succès. Et c’est particulièrement vrai lorsqu’on
offre des services ou des produits par abonnement.

Avant d’entrer dans le vif du sujet, il est très important de se rappeler
certaines notions essentielles à la bonne compréhension des rapports suivants
:

  * **Revenu mensuel récurrent (MRR)** : Le MRR est sans doute la mesure la plus importante pour les entreprises qui vendent des abonnements. Il indique les revenus mensuels générés par les produits ou les services par abonnement. Il s’agit d’un chiffre cohérent utilisé pour suivre tous les revenus récurrents dans le temps, par incréments mensuels.

  * **Revenu annuel récurrent (ARR)** : L’ARR est la version annuelle du MRR, qui se base sur le MRR actuel pour estimer les performances de l’année à venir. Cependant, cette estimation ne prend pas en compte les variations et la croissance.

![Différence entre le MRR et l'ARR dans Odoo
Abonnements](../../../_images/difference-between-MRR-and-ARR.png)

  * **Revenu non récurrent (NRR)** : Le NRR montre les revenus générés pour tout ce qui n’est pas produits ou services par abonnement. Il inclut les recettes rares ou uniques qui ne sont pas susceptibles de se produire dans le cours normal des affaires.

  * **Rétention des clients** : Les pratiques visant à inciter les clients existants à continuer d’acheter des produits ou des services à votre entreprise. La rétention des clients peut être un défi, parce que vous devez prouver que vous êtes digne de la confiance de vos clients.

  * **Taux d’attrition** : Également appelé taux de désabonnement, le taux d’attrition peut être défini, dans ce cas, comme le pourcentage d’abonnés qui ont interrompu leurs abonnements au cours d’une période donnée. Nous pouvons distinguer deux types d’attrition :

    * **Perte de clients** : Il correspond au taux d’annulation des abonnements.

    * **Perte de revenus** : Il correspond au taux de perte de revenus mensuels récurrents.

Example

Imaginons une augmentation de 2$ dans un service d’abonnement.

      * Nous avons perdu 3 clients sur un total initial de 20 clients, ce qui entraîne une **perte de clients** de 15%.

      * Par conséquent, les 56$ de différence de MRR sur les 600$ initiaux entraînent une **perte de revenus**

de 9,33%.

![Différence entre la perte de clients et la perte de revenus dans Odoo
Abonnements](../../../_images/difference-between-logo-churn-and-revenue-
churn.png)

Rappel : même s’ils semblent évoluer dans la même direction la plupart du
temps, ce n’est pas toujours le cas.

  * **Valeur vie client (CLV)** : Indique le montant des revenus que l’on peut attendre d’un client pendant toute la durée de son contrat. Cette approche met l’accent sur l’importance de la rétention des clients, en passant d’une approche trimestrielle ou annuelle à une approche à long terme.

Découvrez les différents types de rapports auxquels vous pouvez accéder depuis
l’application **Odoo Abonnements**.

## Rapport d’analyse des abonnements

Allez à Abonnements ‣ Analyse ‣ Abonnements. De là, vous pouvez changer les
_Mesures_. Par défaut, Odoo utilise le _Revenu mensuel récurrent_. En plus,
vous pouvez choisir la _Quantité_ , le _Prix récurrent_ , le _Revenu annuel
récurrent_ et le _Nombre_. Dans cet exemple, la _Quantité_ est ajoutée. Vous
pouvez ainsi afficher ces deux mesures en même temps. Vous pouvez même
_Regrouper par date de début_ et, plus précisément, par _Semaine_ pour obtenir
une vue d’ensemble de votre rapport.

![Rapport d'analyse des abonnements dans Odoo
Abonnements](../../../_images/subscriptions-analysis-report.png)

## Rapport d’analyse de la rétention

Allez à Abonnements ‣ Analyse ‣ Rétention. La mesure appliquée par défaut est
_Nombre_ , mais vous pouvez la changer pour celle qui vous convient. Dans
l’exemple suivant, le _Revenu mensuel récurrent_ est sélectionné et la
périodicité _Par mois_ reste inchangée. En utilisant ces critères, vous pouvez
voir l’évolution de la rétention depuis le début.

![Rapport d'analyse de la rétention dans Odoo
Abonnements](../../../_images/retention-analysis-report.png)

## Rapport des KPIs des revenus

Allez à Abonnements ‣ Analyse ‣ KPIs des revenus. De là, vous pouvez voir
différents KPIs : _Revenu mensuel récurrent_ , _Revenu net_ , _Revenu non
récurrent_ , _Revenu par abonnement_ , _Revenu annuel récurrent_ , _Valeur
vie_ , et plus encore. Vous pouvez aussi filtrer ces informations sur les
abonnements, les sociétés et les équipes commerciales. Ceci est utile si vous
recherchez des informations spécifiques.

![Rapport des KPIs des revenus dans Odoo
Abonnements](../../../_images/revenue-KPIs-report.png)

L’exemple suivant montre le rapport détaillé du _Revenu mensuel récurrent_. À
ce moment, il n’y aucune donnée, ce qui est le scénario typique pour une
nouvelle entreprise. Mais, au fur et à mesure que votre entreprise se
développe au fil des mois, ce graphique se remplit de plus en plus de données.
Une fois encore, vous pouvez filtrer ces KPIs spécifiques sur les abonnements,
les entreprises et les équipes commerciales.

![Rapport détaillé sur le MRR dans Odoo
Abonnements](../../../_images/detailed-MRR-report.png)

## Rapport sur le tableau de bord d’un vendeur

Allez à Abonnements ‣ Analyse ‣ Tableau de bord vendeur. Cette page vous
fournit un résumé du _Revenu mensuel récurrent_ , du _Revenu non récurrent_ ,
des _Modifications d’abonnement_ et des _Factures non récurrentes_ pour chacun
de vos vendeurs. Vous pouvez choisir la période que vous voulez appliquer et
le vendeur que vous voulez analyser.

![Rapport sur le tableau de bord d'un vendeur dans Odoo
Abonnements](../../../_images/salesperson-dashboard-report.png)

Pour plus d'infos

  * [Abonnements](../subscriptions.html)

  * [Plans d’abonnement](plans.html)

  * [Produits d’abonnement](products.html)

