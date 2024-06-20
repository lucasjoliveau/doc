# Accords de niveau de service (SLA)

Le Service Level Agreement (SLA) ou Accord de niveau de service définit le
niveau de service qu’un client peut attendre d’un fournisseur. Les SLA
fournissent un calendrier qui indique aux clients quand ils peuvent s’attendre
à des résultats et qui permet à l’équipe d’assistance de ne pas perdre de vue
ses objectifs.

## Créer une nouvelle politique SLA

Pour créer une nouvelle politique SLA, allez à la page de l’équipe via
Assistance ‣ Configuration ‣ Équipes. Sélectionnez une équipe, descendez
jusqu’à la section Performances et cochez la case à côté de Politiques SLA
pour les activer pour cette équipe en particulier.

![Vue d'une page d'équipe dans Assistance mettant en évidence le paramètres
des Politiques SLA](../../../../_images/sla-enable.png)

Note

La valeur indiquée à côté du champ Heures de travail est utilisée pour
déterminer le délai des politiques SLA. Par défaut, elle est déterminée par la
valeur définie dans le champ Horaire de l’entreprise dans l’application
Paramètres ‣ Employés ‣ Organisation du travail.

Pour créer une nouvelle politique, cliquez sur le bouton intelligent sur la
page des paramètres de l’équipe ou allez à Assistance ‣ Configuration ‣
Politiques SLA et cliquez sur Nouveau. Commencez par saisir un Titre et une
Description pour la nouvelle politique et complétez le formulaire en suivant
les étapes ci-dessous.

### Définir les critères d’une politique SLA

La section Critères permet d’identifier les tickets auxquels cette politique
sera appliquée. Complétez les champs suivants pour modifier les critères de
sélection :

  * Équipe : une politique peut uniquement s’appliquer à une équipe. _Ce champ est obligatoire._

  * Priorité : le niveau de priorité d’un ticket est identifié en sélectionnant le nombre d’étoiles représentant le niveau de priorité sur la carte kanban ou sur le ticket lui-même. La politique SLA ne sera appliquée que lorsque le niveau de priorité du ticket aura été mis à jour pour correspondre aux critères du SLA. Si aucune sélection n’est faite dans ce champ, cette politique ne s’appliquera qu’aux tickets marqués comme étant de `faible priorité` (zéro étoiles).

  * Types : les types de tickets peuvent être utilisés pour indiquer s’il s’agit d’une question d’un client qui peut être résolue avec une réponse rapide, ou un problème qui peut nécessiter des recherches supplémentaires. Plusieurs types de tickets peuvent être sélectionnés dans ce champ. Si aucune sélection n’est faite, cette politique s’appliquera à tous les types de tickets.

  * Étiquettes : les étiquettes sont appliquées pour indiquer brièvement le sujet du ticket. Plusieurs étiquettes peuvent être appliquées à un seul ticket.

  * Clients : ce champ permet de sélectionner des contacts individuels ou des entreprises.

  * Articles du bon de commande : ce champ n’est disponible que si l’application _Feuilles de temps_ est activée pour l’équipe. Cela permet au ticket d’être lié directement à une ligne spécifique d’une commande, qui doit être indiquée sur le ticket dans le champ Articles du bon de commande.

Note

Sauf indication contraire, il est possible de faire plusieurs sélections pour
chaque champ (c’est-à-dire plusieurs Étiquettes peuvent être comprises dans
une politique, mais un seul niveau de Priorité)

![Vue d'un enregistrement de politique SLA vierge](../../../../_images/sla-
create-new.png)

### Établir une cible pour une politique SLA

La Cible est l’étape qu’un ticket doit atteindre et le temps alloué pour
atteindre cette étape, afin de satisfaire la politique SLA. Toute étape
assignée à une équipe peut être sélectionnée dans le champ Étape cible. Le
temps passé dans les étapes sélectionnées dans Étapes exclues ne sera pas pris
en compte dans le calcul du délai du SLA.

Example

Un SLA intitulé `8 heures pour clôturer` suit le temps de travail avant qu’un
ticket ne soit terminé et aurait `Résolu` comme Étape cible. Cependant, si le
SLA était intitulé `2 jours pour commencer`, il suit le temps de travail avant
que le travail sur un ticket ne commence et aurait `En cours` comme Étape
cible.

## Respecter les délais SLA

Une fois qu’il est déterminé qu’un ticket correspond aux critères d’une
politique SLA, un délai est calculé. Le délai est basé sur la date de création
du ticket et les heures de travail ciblées. Le délai est ensuite ajouté au
ticket, ainsi qu’un drapeau blanc indiquant le nom du SLA appliqué.

![Vue d'un formulaire de ticket mettant en évidence un délai SLA ouvert sur un
ticket dans Odoo Assistance](../../../../_images/sla-open-deadline.png)

Important

Si un ticket répond aux critères de plus d’un SLA, le délai qui vient à
échéance en premier sera affiché sur le ticket. Une fois ce délai passé, le
délai suivant sera affiché.

Lorsqu’un ticket répond à une politique SLA, le drapeau SLA devient vert et le
champ Délai disparaît de la vue du ticket.

![Vue d'un formulaire de ticket mettant en évidence un SLA satisfait dans Odoo
Assistance](../../../../_images/sla-deadline.png)

Si le délai SLA est passé et le ticket n’est pas passé à l”Étape cible, le
drapeau SLA deviendra rouge. Une fois que le SLA a échoué, le drapeau rouge
restera sur le ticket, même après que le ticket est déplacé vers l”Étape
cible.

![Vue d'un formulaire de ticket avec un SLA réussi et en échec dans Odoo
Assistance](../../../../_images/sla-passing-failing.png)

## Analyser les performances du SLA

Le rapport Analyse du statut SLA suit la rapidité avec laquelle un SLA est
respecté, ainsi que le taux de réussite des politiques individuelles.
Consultez le rapport et le tableau croisé dynamique correspondent en allant à
Assistance ‣ Analyse ‣ Analyse du statut SLA.

### En utilisant le tableau croisé dynamique

Par défaut, le rapport est affiché dans une vue Tableau croisé dynamique et
est filtré pour montrer le nombre de SLA en échec et le taux d’échec sur les
30 derniers jours, regroupés par équipe.

![Vue du rapport d'analyse du statut SLA dans Odoo
Assistance](../../../../_images/sla-status-analysis.png)

Pour ajouter le nombre de SLA réussis ou en cours, cliquez sur le bouton
Mesures pour afficher un menu déroulant de critères de rapport et choisissez
parmi les options disponibles en fonction des mesures préférées. Chaque fois
qu’une mesure est sélectionnée, elle est cochée dans le menu déroulant pour
indiquer que cette mesure est comprise et une nouvelle colonne correspondante
apparaît dans le tableau croisé dynamique pour montrer les calculs pertinents.

Pour ajouter un groupe à une ligne ou colonne, cliquez sur le bouton plus
:guilabel:` + ` à côté de Total, et sélectionnez l’un des groupes. Pour en
supprimer un, cliquez sur le bouton moins :guilabel:` - ` et désélectionnez-
le.

### En utilisant la vue graphique

Le rapport Analyse du statut peut également être affiché sous forme de
graphique à barres, linéaire ou circulaire. Basculez entre ces deux vues en
sélectionnant l’icône appropriée en haut du graphique.

Bar ChartLine ChartPie Chart

![Vue du rapport d'analyse du statut SLA dans la vue graphique à
barres](../../../../_images/sla-report-bar.png)

![Vue d'un rapport d'analyse du statut SLA dans la vue graphique
linéaire](../../../../_images/sla-report-line.png)

![Vue du rapport d'analyse du statut SLA dans la vue graphique
circulaire](../../../../_images/sla-report-pie.png)

Astuce

Les graphiques à barres et les graphiques linéaires peuvent être affichés en
mode empilé. Cela permet de faire apparaître deux groupes ou plus l’un au-
dessus de l’autre plutôt que l’un à côté de l’autre, facilitant ainsi la
comparaison des données.

### En utilisant la vue cohorte

La vue Cohorte est utilisée pour suivre l’évolution des données sur une
période donnée. Pour afficher le rapport Analyse du statut dans une vue
Cohorte, cliquez sur l’icône dans le coin supérieur droit au-dessus du
graphique.

![Vue du rapport d'analyse du statut SLA dans la vue
cohorte](../../../../_images/sla-report-cohort.png)

Pour plus d'infos

  * [Vues d’analyse](../../../essentials/reporting.html#reporting-views)

  * [Permettre aux clients de clôturer leurs tickets](../advanced/close_tickets.html)

  *[SLA]: Accord de niveau de service

