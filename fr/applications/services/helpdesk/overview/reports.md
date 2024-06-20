# Analyse

Odoo _Assistance_ fournit plusieurs rapports qui vous donnent la possibilité
de suivre les tendances des tickets d’assistance, d’identifier les points à
améliorer, de gérer la charge de travail de l’employé et de confirmer lorsque
les attentes du client sont satisfaites.

## Rapports disponibles

Vous pouvez trouver les détails sur les rapports disponibles dans Odoo
_Assistance_ ci-dessous. Pour afficher les différents rapports, allez à
Assistance ‣ Analyse.

### Analyse des tickets

Le rapport _Analyse des tickets_ (Assistance ‣ Analyse ‣ Analyse des tickets)
permet de fournir une vue d’ensemble de chaque ticket d’assistance client dans
la base de données. Elle comprend le nombre de tickets assignés aux équipes et
aux utilisateurs individuels.

Ce rapport vous permet d’identifier où les équipes passent le plus de temps et
de déterminer si la charge de travail est distribuée de manière inégale parmi
les membres des équipes d’assistance. Le rapport par défaut compte le nombre
de tickets par équipe et les regroupe par étape.

![Vue de la vue par défaut du rapport Analyse des
tickets.](../../../../_images/tickets-default.png)

Il est possible de sélectionner des mesures alternatives pour suivre où le
plus de temps est passé à des moments différents du flux de travail. Pour
modifier les mesures utilisées dans le rapport qui s’affiche actuellement ou
pour en ajouter d’autres, cliquez sur le bouton Mesures et sélectionnez une
des options dans le menu déroulant :

  * Temps moyen pour répondre : nombre moyen d’heures de travail entre l’envoi d’un message par le client et la réponse de l’équipe d’assistance. _Ceci n’inclut pas les messages envoyés quand le ticket était dans une étape repliée_

  * Heures ouvertes : nombre d’heures entre la date à laquelle le ticket a été créé et la date à laquelle le ticket a été clôturé. Si aucune date de clôture ne figure sur le ticket, la date actuelle est utilisée. **Cette mesure n’est pas spécifique aux heures de travail**

  * Heures passées : le nombre d’heures de _Feuille de temps_ enregistrées sur un ticket. _Cette mesure n’est disponible que si les Feuilles de temps sont activées sur une équipe et l’utilisateur actuel dispose des droits d’accès pour les voir_

  * Heures pour assigner : nombre d’heures de travail entre la date à laquelle le ticket a été créé et la date à laquelle il a été assigné à un membre de l’équipe

  * Heures pour clôturer : nombre d’heures de travail entre la date à laquelle le ticket a été créé et la date à laquelle il a été clôturé

  * Heures avant la première réponse : nombre d’heures de travail entre la date à laquelle le ticket a été reçu et la date à laquelle le premier message a été envoyé. _Ceci n’inclut pas l’email envoyé automatiquement lorsqu’un ticket atteint une étape_

  * Heures jusqu’à la date limite SLA : nombre d’heures de travail restantes avant d’atteindre la dernière date limite du SLA sur un ticket

  * Évaluation /5 : valeur assignée à l’évaluation reçue de la part d’un client (Insatisfait = 1, Bien/Neutre = 3, Satisfait = 5)

  * Nombre : nombre total de tickets

Note

Les _Heures de travail_ sont calculées sur la base de l’horaire par défaut.
Pour afficher ou modifier l’horaire, allez à l’application Paramètres et
sélectionnez Employés ‣ Horaire de l’entreprise.

### Analyse du statut SLA

Le rapport _Analyse du statut SLA_ (Assistance ‣ Analyse ‣ Analyse du statut
SLA) permet de suivre la rapidité avec laquelle un SLA (Accord de niveau de
service) est respecté, ainsi que le taux de réussite des politiques
individuelles.

Par défaut, les filtres de ce rapport sont définis pour afficher le nombre de
SLA échoués, ainsi que le taux d’échec sur les 30 derniers jours, regroupés
par équipe.

![Vue des options Regrouper par sur le rapport d'analyse des
tickets.](../../../../_images/sla-status.png)

Pour modifier les mesures utilisées pour le rapport actuellement affiché ou
pour en ajouter d’autres, cliquez sur le bouton Mesures et sélectionnez une ou
plusieurs options dans le menu déroulant :

  * % de SLA en échec : pourcentage de tickets qui ont échoué à au moins un SLA

  * % de SLA en cours : pourcentage de tickets qui ont au moins un SLA toujours en cours et dont aucun SLA n’a échoué

  * % de SLA réussis : pourcentage de tickets pour lesquels tous les SLA ont été réussis

  * Nombre de SLA en échec : nombre de tickets qui ont échoué à un SLA au moins

  * Nombre de SLA réussis : nombre de tickets pour lesquels tous les SLA ont été réussis

  * Nombre de SLA en cours : nombre de tickets qui ont au moins un SLA toujours en cours et qui n’ont aucun SLA en échec

  * Heures de travail pour assigner : le nombre d’heures de travail entre la date à laquelle le ticket a été créé et la date à laquelle il a été assigné à un membre de l’équipe

  * Heures de travail pour clôturer : nombre d’heures de travail entre la date à laquelle le ticket a été créé et la date à laquelle il a été clôturé

  * Heures de travail pour atteindre le SLA : nombre d’heures de travail entre la date à laquelle le ticket a été créé et la date à laquelle le SLA a été atteint

  * Nombre : nombre total de tickets

Example

Pour voir le nombre de tickets qui ont atteint les objectifs SLA définis et
suivre le temps qu’il a fallu pour atteindre ces objectifs, cliquez sur
Mesures ‣ Nombre de SLA réussis et Mesures ‣ Heures de travail pour atteindre
le SLA.

Pour trier ces résultats en fonction des membres de l’équipe assignés aux
tickets, sélectionnez Total ‣ Assigné à.

Pour plus d'infos

[Accords de niveau de service (SLA)](sla.html)

### Évaluations des clients

Le rapport _Évaluations des clients_ (Assistance ‣ Analyse – Évaluations des
clients) montre une vue d’ensemble des évaluations reçues sur les tickets
d’assistance individuels, ainsi que tous les commentaires supplémentaires
laissés avec l’évaluation.

![Vue de l'affichage kanban du rapport des Évaluations des
clients.](../../../../_images/customer-ratings.png)

Cliquez sur une évaluation individuelle pour voir plus de détails sur
l’évaluation soumise par le client, y compris un lien vers le ticket original.

![Vue des détails d'une évaluation client
individuelle.](../../../../_images/ratings-details.png)

Astuce

Sur la page des détails de l’évaluation, sélectionnez l’option Visible en
interne uniquement pour masquer l’évaluation du portail client.

Le rapport _Évaluations des clients_ s’affiche dans une vue kanban par défaut,
mais peut également s’afficher dans une vue graphique, liste ou tableau croisé
dynamique.

Pour plus d'infos

[Évaluations](ratings.html)

## Options d’affichage et de filtrage

Sur n’importe quel rapport d’Odoo, les options d’affichage et de filtrage
varient, en fonction des données qui sont analysées, mesurées et regroupées.
Vous trouverez ci-dessous des informations supplémentaires sur les vues
disponibles pour les rapports d” _Assistance_.

Note

Les graphiques ne peuvent afficher qu’une seule mesure à la fois, tandis que
les tableaux croisés dynamiques peuvent contenir plusieurs mesures.

### Vue tableau croisé dynamique

La vue _tableau croisé dynamique_ présente les données de manière interactive.
Les trois rapports _Assistance_ sont disponibles dans la vue tableau croisé
dynamique.

La vue tableau croisé dynamique est accessible depuis n’importe quel rapport
en sélectionnant l”icône de grille dans le coin supérieur droit de l’écran.

![Vue du rapport d'analyse du statut SLA dans Odoo
Assistance.](../../../../_images/pivot-view1.png)

Pour ajouter un groupe à une ligne ou colonne dans la vue tableau croisé
dynamique, cliquez sur ➕ (signe plus) à côté du Total et sélectionnez un des
groupes. Pour en supprimer un, cliquez sur ➖ (signe moins) et désactivez
l’option appropriée.

### Vue graphique

La vue _graphique_ présente les données dans un graphique _à barres_ ,
_linéaire_ ou _circulaire_.

Basculez vers la vue graphique en cliquant sur l”icône du graphique linéaire
dans le coin supérieur droit dans l’écran. Pour passer d’un graphique à un
autre, sélectionnez l” _icône appropriée_ dans le coin supérieur gauche du
graphique, tout cela dans la vue graphique.

Bar chartLine chartPie chart

![Vue du rapport d'analyse du statut SLA dans la vue graphique à
barres.](../../../../_images/bar-chart2.png)

![Vue du rapport Évaluations des clients dans la vue graphique
linéaire.](../../../../_images/line-chart1.png)

![Vue du rapport d'analyse des tickets dans la vue graphique
circulaire.](../../../../_images/pie-chart1.png)

Astuce

Les _graphiques à barres_ et les _graphiques linéaires_ peuvent être affichés
en mode _empilé_. Cela permet de faire apparaître deux groupes de données (ou
plus) l’un au-dessus de l’autre, plutôt que l’un à côté de l’autre, facilitant
ainsi la comparaison des données.

### Enregistrer et partager une recherche favorite

La fonctionnalité _Favoris_ trouvée sur les rapports d” _Assistance_ permet
aux utilisateurs de enregistrer les filtres qu’ils utilisent souvent sans
avoir à les redéfinir chaque fois.

Pour créer et enregistrer de nouveaux _Favoris_ sur un rapport, suivez les
étapes suivantes :

  1. Définissez les paramètres nécessaires en utilisant les options Filtres, Regrouper par et Mesures.

  2. Cliquez sur Favoris ‣ Enregistrer la recherche actuelle.

  3. Donnez un nouveau nom à la recherche.

  4. Sélectionnez Utiliser par défaut pour que ces paramètres de filtrages s’affichent automatiquement à l’ouverture du rapport. Sinon, ne cochez pas cette case.

  5. Sélectionnez Partager avec tous les utilisateurs pour rendre ce filtre accessible à tous les autres utilisateurs de la base de données. Si cette case n’est pas cochée, ce filtre ne sera accessible qu’à l’utilisateur qui l’a créé.

  6. Cliquez sur Enregistrer pour conserver la configuration pour plus tard.

![Vue de l'option d'enregistrement des favoris dans Odoo
Assistance.](../../../../_images/save-filters.png)

Pour plus d'infos

  * [Commencer à recevoir des tickets](receiving_tickets.html)

  * [Odoo reporting](../../../essentials/reporting.html)

  *[SLA]: Accord de niveau de service

