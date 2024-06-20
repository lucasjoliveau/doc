# Gérer les ordres de travail en utilisant les postes de travail

Odoo Fabrication permet d’exécuter des ordres de travail à des postes de
travail spécifiques. Lorsqu’un ordre de fabrication est créé pour un produit,
tout ordre de travail répertorié dans l’onglet Opérations de la nomenclature
du produit sera automatiquement créé et assigné au poste de travail précisé.
Les ordres de travail peuvent être gérés dans le module Fabrication en
sélectionnant Opérations ‣ Ordres de travail.

Pour utiliser les postes de travail, la fonctionnalité des Ordres de travail
doit d’abord être activée. Pour ce faire, allez au module Fabrication,
sélectionnez Configuration ‣ Paramètres et cochez la case à côté d”ordres de
travail. Les postes de travail peuvent ensuite être créés et gérés en
sélectionnant Configuration ‣ Postes de travail.

## Créer un poste de travail

Dans le module Fabrication, sélectionnez Configuration ‣ Postes de travail ‣
Créer. Le formulaire du poste de travail peut ensuite être complété comme suit
:

  * Nom du poste de travail : donnez un nom court au poste de travail qui décrit le type d’opérations pour lesquelles il sera utilisé

  * Postes de travail alternatifs : précisez un poste de travail alternatif où les opérations peuvent être réalisées si le poste de travail principal n’est pas disponible

  * Code : assignez un code de référence au poste de travail

  * Heures de travail : définissez le nombre d’heures pendant lesquelles le poste de travail peut être utilisé chaque semaine

  * Société : sélectionnez la société à laquelle le poste de travail appartient

![Un exemple d'un formulaire de poste de travail entièrement
configuré](../../../../_images/work-center-form.png)

### Définir des normes de productivité pour les postes de travail

L’onglet Informations générales du formulaire du poste de travail permet
d’assigner des objectifs de productivité à un poste de travail :

  * Efficacité temporelle : utilisée pour calculer la durée prévue d’un ordre de travail au poste de travail ; par exemple, si un ordre de travail prend normalement une heure et l’efficacité est de 200 %, l’ordre de travail prendra 30 minutes

  * Capacité : le nombre d’opérations qui peuvent être effectuées en même temps au poste de travail

  * Objectif TRS : l’objectif d’efficacité du poste de travail

  * Temps avant prod. : temps de préparation requis avant que le travail puisse commencer

  * Temps après prod. : temps d’arrêt ou de nettoyage nécessaire après la fin du travail

  * Coût par heure : le coût de fonctionnement du poste de travail pendant une heure

  * Compte analytique : le compte où le coût du poste de travail doit être enregistré

![L'onglet des informations générales du formulaire du poste de
travail.](../../../../_images/work-center-general-information.png)

### Affecter un équipement à un poste de travail

L’onglet Équipement permet d’affecter des équipements spécifiques à un poste
de travail. Les informations suivantes seront affichées pour chaque équipement
ajouté :

  * Nom de l’équipement : le nom de l’équipement

  * Technicien : le technicien responsable de la maintenance de l’équipement

  * Catégorie d’équipement : la catégorie à laquelle l’équipement appartient

  * MTBF : temps moyen entre défaillances ; le temps moyen pendant lequel l’équipement fonctionnera avant de tomber en panne

  * MTTR : temps moyen de réparation ; le temps moyen nécessaire pour que l’équipement soit à nouveau opérationnel

  * Estimation de la prochaine défaillance : une estimation de la date de la prochaine défaillance de l’équipement

![L'onglet équipement du formulaire du poste de
travail.](../../../../_images/work-center-equipment.png)

Note

Le MTBF, le MTTR, et l”Estimation de la prochaine défaillance sont calculés
automatiquement en fonction de la date de la dernière défaillance, s’il y en a
eu une.

### Intégrer des appareils IoT

L’onglet des Déclencheurs IoT permet d’intégrer des appareils IoT à un poste
de travail :

  * Appareil : précise l’appareil IoT à déclencher

  * Clé : la clé de sécurité de l’appareil

  * Action : l’action de l’appareil IoT déclenchée

![L'onglet des déclencheurs IoT du formulaire du poste de
travail.](../../../../_images/work-center-iot.png)

## Cas d’utilisation : configurer un poste de travail alternatif

Lorsqu’un poste de travail est à pleine capacité, il ne peut pas accepter de
nouveaux ordres de travail. Au lieu d’attendre que le poste de travail se
libère, il est possible de déterminer un poste de travail alternatif où les
ordres de travail excédentaires doivent être exécutés.

Commencez par créer un nouveau poste de travail. Configurez l’onglet
Équipement de manière à ce qu’il dispose des mêmes équipements du poste de
travail principal. Cela permettra de s’assurer que les mêmes tâches peuvent
être réalisées dans les deux postes de travail. Allez au poste de travail
principal et incluez le nouveau poste de travail dans le champ de sélection
Postes de travail alternatifs

Créez maintenant un nouvel ordre de fabrication qui utilise le poste de
travail principal pour l’une de ses opérations. Le poste de travail principal
sera automatiquement sélectionné pour l’opération dans l’onglet Postes de
travail. Après avoir confirmé l’ordre de fabrication, cliquez sur le bouton
Programmer qui apparaît en haut à gauche du formulaire.

![Cliquez sur le bouton programmer pour sélectionner automatiquement un poste
de travail disponible.](../../../../_images/manufacturing-order-plan-
button.png)

Si le poste de travail principal est à pleine capacité, le poste de travail
sélectionné pour l’opération est automatiquement remplacé par le poste de
travail alternatif.

![Le poste de travail alternatif est sélectionné
automatiquement.](../../../../_images/automatic-work-center-selection.png)

## Contrôler les performances d’un poste de travail

Les performances d’un poste de travail individuel peuvent être visualisées en
sélectionnant Configuration ‣ Postes de travail et en cliquant sur un poste de
travail. Diverses mesures indiquant les performances d’un poste de travail
peuvent être affichées en haut à droite du formulaire :

  * TRS : taux de rendement synthétique, le pourcentage de temps pendant lequel le poste de travail a été pleinement productif

  * Perdu : le temps perdu en raison des arrêts de travail

  * Charge : le temps nécessaire à l’exécution de la charge de travail actuelle

  * Performances : la durée réelle du temps de travail, exprimée en pourcentage de la durée prévue

  *[IoT]: Internet of Things

