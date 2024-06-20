# Activités

Les _Activités_ sont des tâches de suivi liées à un enregistrement dans une
base de données Odoo. Les activités peuvent être planifiées sur n’importe
quelle page de la base de données qui contient un chatter, une vue kanban, une
vue de liste ou une vue des activités d’une application.

## Planifier des activités

Les activités peuvent être créées en cliquant sur le bouton Planifier une
activité, situé en haut du _chatter_ de chaque enregistrement. Dans la fenêtre
contextuelle qui s’affiche, sélectionnez un Type d’activité dans le menu
déroulant.

Astuce

Les applications individuelles ont une liste de _Types d’activité_ dédiés à
cette application. Par exemple, pour voir et modifier les activités
disponibles pour l’application _CRM_ , allez à l’app CRM ‣ Configuration ‣
Types d’activité.

Saisissez un titre pour l’activité dans le champ Résumé, situé dans la fenêtre
contextuelle Planifier une activité.

Pour assigner l’activité à un utilisateur différent, sélectionnez un nom dans
le menu déroulant Assigné à. Sinon, l’utilisateur qui crée l’activité est
automatiquement assigné.

Enfin, ajoutez des informations supplémentaires dans le champ facultatif
Enregistrer une note….

Note

Le champ Date d’échéance dans la fenêtre contextuelle Planifier une activité
se remplit automatiquement en fonction des paramètres de configuration du Type
d’activité sélectionné. Cependant, vous pouvez modifier cette date en
sélectionnant une date dans le calendrier dans le champ Date d’échéance.

Finalement, cliquez sur l’un des boutons suivants :

  * Planifier : ajoute l’activité au chatter dans l’onglet Activités planifiées.

  * Marquer comme fait : ajoute les détails de l’activité au chatter sous Aujourd’hui. L’activité n’est pas planifiée, mais elle est automatiquement marquée comme complétée.

  * Fait & Planifier suivant : ajoute la tâche sous Aujourd’hui marquée comme faite et ouvre une nouvelle fenêtre d’activité.

  * Ignorer : ignore tous les changements apportés dans la fenêtre contextuelle.

![Vue des pistes CRM et l'option de planifier une
activité.](../../_images/schedule-pop-up.png)

Note

En fonction du type d’activité, le bouton Planifier peut être remplacé par un
bouton Enregistrer ou un bouton Ouvrir le calendrier.

Les activités planifiées sont ajoutées au chatter pour l’enregistrement sous
Activités planifiées.

![Vue des pistes CRM et l'option de planifier une
activité.](../../_images/chatter-activities.png)

Les activités peuvent également être planifiées à partir de la vue kanban,
liste ou activités d’une application.

Kanban viewList viewActivity view

Sélectionnez un enregistrement pour lequel vous voulez planifier une activité.
Cliquez sur l’icône 🕘 (horloge), puis Planifier une activité et remplissez le
formulaire contextuel.

![La vue kanban du pipeline CRM et l'option de planifier une
activité.](../../_images/schedule-kanban-activity.png)

Sélectionnez un enregistrement pour lequel vous voulez planifier une activité.
Cliquez sur l’icône 🕘 (horloge), puis sur Planifier une activité. Si une autre
activité est déjà planifiée pour l’enregistrement, il se peut que l’icône
d’horloge soit remplacée par une icône de 📞 (téléphone) ou de ✉️ (enveloppe).

![La vue liste du pipeline CRM et l'option de planifier une
activité.](../../_images/schedule-list-activity.png)

Pour ouvrir la vue activité d’une application, sélectionnez l’icône 🕘
(horloge) dans la barre de menu n’importe où dans la base de données.
Sélectionnez n’importe quelle application dans le menu déroulant et cliquez
sur l’icône 🕘 (horloge) de l’application souhaitée.

![Le menu déroulant des activités avec l'endroit où ouvrir la vue activité
pour le CRM mis en évidence.](../../_images/schedule-activity-view-menu.png)

Sélectionnez un enregistrement pour lequel vous voulez planifier une activité.
Déplacez-vous sur la ligne pour trouver le type d’activité souhaité, puis
cliquez sur ＋ (signe plus).

![La vue activité du pipeline CRM et l'option de planifier une
activité.](../../_images/schedule-activity-view.png)

Note

Les couleurs de l’activité et leur relation à la date d’échéance d’une
activité sont cohérentes dans Odoo, indépendamment du type d’activité ou de la
vue.

  * Les activités qui apparaissent en **vert** indiquent une date d’échéance dans le futur.

  * **Jaune** indique que la date d’échéance de l’activité est aujourd’hui.

  * **Rouge** indique que l’activité est en retard et que la date d’échéance est dépassée.

Par exemple, si une activité est créée pour un appel téléphonique et que la
date d’échéance est dépassée, l’activité apparaît avec un téléphone rouge dans
la vue de liste et un horloge rouge dans la vue kanban.

## Voir les activités planifiées

Pour voir les activités planifiées, ouvrez l’application Ventes ou
l’application CRM et cliquez sur l’icône 🕘 (horloge), située à l’extrême
droite des autres options de vue.

Le menu des activités s’ouvre et affiche par défaut toutes les activités
planifiées pour l’utilisateur. Pour afficher toutes les activités de tous les
utilisateurs, supprimez le filtre Mon pipeline dans la barre Rechercher….

Pour voir une liste consolidée des activités séparée par l’application où
elles ont été créées, et par date d’échéance, cliquez sur l’icône 🕘 (horloge)
dans le menu d’en-tête pour voir les activités de cette application spécifique
dans un menu déroulant.

La possibilité d”Ajouter une nouvelle note et de Demander un document apparaît
au bas de ce menu déroulant, lorsque vous cliquez sur l’icône 🕘 (horloge) du
menu d’en-tête.

![Vue d'une page des pistes CRM mettant en évidence le menu des
activités.](../../_images/activities-menu.png)

## Configurer des types d’activité

Pour configurer les types d’activités dans la base de données, allez à
l’application Paramètres ‣ Discussion ‣ Activités ‣ Types d’activité.

![Vue de la page des paramètres mettant en évidence le menu des types
d'activité.](../../_images/settings-activities-types.png)

La page des Types d’activité s’ouvre et affiche les types d’activité
existants.

Pour modifier un type d’activité existant, sélectionnez-le dans la liste, puis
cliquez sur Modifier. Pour créer un nouveau type d’activité, cliquez sur
Créer.

En haut du formulaire vierge du type d’activité, commencez par choisir un Nom
pour ce nouveau type d’activité.

![Formulaire d'un nouveau type d'activité.](../../_images/new-activity-
type.png)

### Paramètres des activités

#### Action

Le champ _Action_ précise l’intention de l’activité. Certaines actions
déclenchent des comportements spécifiques après avoir planifié une activité.

  * Si vous sélectionnez Charger un document, un lien pour charger un document s’ajoute directement à l’activité planifiée dans le chatter.

  * Si vous sélectionnez Appel téléphonique ou Réunion, les utilisateurs ont l’option d’ouvrir leur calendrier pour programmer une heure pour cette activité.

  * Si vous sélectionnez Demander une signature, un lien est ajouté à l’activité planifiée dans le chatter permettant d’ouvrir une fenêtre contextuelle de demande de signature.

Note

Les actions disponibles pour sélectionner un type d’activité varient en
fonction des applications actuellement installées dans la base de données.

#### Utilisateur par défaut

Pour assigner cette activité automatiquement à un utilisateur spécifique
lorsque ce type d’activité est planifié, choisissez un nom dans le menu
déroulant Utilisateur par défaut. Si ce champ est laissé vierge, l’activité
est assignée à l’utilisateur qui a créé l’activité.

#### Résumé par défaut

Pour inclure des notes chaque fois que ce type d’activité est créé, saisissez-
les dans le champ Résumé par défaut.

Note

Les informations dans les champs Utilisateur par défaut et Résumé par défaut
sont incluses lors de la création d’une activité. Toutefois, elles peuvent
être modifiées avant que l’activité ne soit planifiée ou enregistrée.

### Activité suivante

Pour suggérer ou déclencher automatiquement une nouvelle activité après qu’une
activité a été marquée comme faite, vous devez définir le Type de chaînage.

#### Suggérer l’activité suivante

Dans le champ Type de chaînage, sélectionnez Suggérer l’activité suivante. Le
champ situé en dessous devient alors Suggérer. Cliquez sur le menu déroulant
Suggérer pour sélectionner les activités à recommander comme tâches de suivi
pour ce type d’activité.

Dans le champ Planifier, choisissez un délai par défaut pour ces activités.
Pour ce faire, configurez un nombre souhaité de Jours, Semaines, ou Mois. Puis
décidez si elle doit avoir lieu après la date d’achèvement ou après la date de
fin de l’activité précédente.

Vous pouvez modifier ce champ Planifier avant que l’activité ne soit
planifiée.

Lorsque toutes les configurations sont terminées, cliquez sur Enregistrer.

![Fenêtre contextuelle Planifier une activité mettant en évidence les
activités recommandées.](../../_images/schedule-recommended-activity.png)

Note

Si le Type de chaînage de l’activité est défini sur Suggérer l’activité
suivante et des activités sont répertoriées dans le champ Suggérer, les
utilisateurs reçoivent des recommandations d’activités pour les étapes
suivantes.

#### Déclencher l’activité suivante

Le fait de définir le Type de chaînage sur Déclencher l’activité suivante
permet de lancer immédiatement l’activité suivante une fois que la précédente
est terminée.

Si vous sélectionnez Déclencher l’activité suivante dans le champ Type de
chaînage, le champ situé en dessous devient Déclencher. Dans le menu déroulant
du champ Déclencher, sélectionnez l’activité qui doit être lancée une fois que
cette activité est terminée.

Dans le champ Planifier, choisissez un délai par défaut pour ces activités.
Pour ce faire, configurez un nombre souhaité de Jours, Semaines, ou Mois. Puis
décidez si elle doit avoir lieu après la date d’achèvement ou après la date de
fin de l’activité précédente.

Vous pouvez modifier ce champ Planifier avant que l’activité ne soit
planifiée.

Lorsque toutes les configurations sont terminées, cliquez sur Enregistrer.

![Fenêtre contextuelle Planifier une activité mettant en évidence le bouton
Fait et lancer suivant.](../../_images/triggered-activities.png)

Note

Lorsque le Type de chaînage est défini sur Déclencher l’activité suivante, le
fait de marquer l’activité comme `Fait` lance immédiatement l’activité
suivante répertoriée dans le champ Déclencher.

Pour plus d'infos

  * [Discussion](../productivity/discuss.html)

  * [Utiliser les canaux pour la communication d’équipe](../productivity/discuss/team_communication.html)

