# Clôturer des tickets

Une fois que le travail est terminé sur un ticket d” _Assistance_ dans Odoo,
il y a plusieurs façons de le clôturer. La fermeture manuelle des tickets
résolus permet de maintenir le pipeline à jour, tandis que la clôture
automatique des tickets inactifs permet d’éviter les problèmes de blocage
inutiles. Permettre aux clients de clôturer leurs propres tickets minimise la
confusion autour de la question de savoir si un problème est considéré comme
résolu ou non. Il en résulte une augmentation de la capacité opérationnelle
des équipes d’assistance et une plus grande satisfaction des clients.

## Clôturer manuellement les tickets résolus

Au fur et à mesure que le travail sur un ticket progresse, il passe à l’étape
suivante du pipeline. Une fois le problème résolu, le ticket est déplacé vers
une étape _repliée_. Cela marque la _clôture_ du ticket.

Pour replier une étape, allez au tableau de bord d”Assistance et cliquez sur
une équipe pour ouvrir le pipeline. Survolez l’en-tête d’une étape et cliquez
ensuite sur l’icône d’engrenage qui apparaît dans le coin supérieur droit de
la colonne Kanban de cette étape.

![Vue d'une étape dans le pipeline d'Assistance mettant en évidence l'icône
d'engrenage et l'option de modification de
l'étape.](../../../../_images/closing-edit-stage-gear.png)

Avertissement

En cliquant sur l’icône d’engrenage, vous avez également l’option de Replier
l’étape. Cette option permet de _temporairement_ replier l’étape pour
simplifier la vue kanban. Ceci ne clôture _pas_ le ticket dans cette étape.
Cela ne replie pas non plus l’étape de façon permanente. Si une étape doit
être repliée pour que les tickets puissent être marqués comme clôturés, suivez
les étapes ci-dessous.

Dans le menu qui apparaît, sélectionnez Modifier l’étape. Les paramètres de
l’étape s’ouvrent alors. Cochez la case à côté de Repliée dans la vue Kanban
en haut de la fenêtre et cliquez ensuite sur Enregistrer & Fermer pour
confirmer les changements. Les tickets qui atteignent cette étape seront
désormais considérés comme _clôturés_.

> ![Page des paramètres d'une étape.](../../../../_images/closing-folded-
> setting.png)

## Clôturer automatiquement des tickets inactifs

Les tickets inactifs pendant une période donnée peuvent être automatiquement
fermés. À ce moment-là, ils seront déplacés vers une étape repliée.

Allez à la page des paramètres de l’équipe en allant à Assistance ‣
Configuration ‣ Équipes. Dans la section Self-Service, activez la
fonctionnalité Clôture automatique.

Si l’une des étapes de l’équipe est configurée pour être repliée dans la vue
kanban, elle sera la sélection par défaut dans le champ Déplacer à l’étape. Si
l’équipe a plus d’une étape repliée, l’étape qui apparaît en premier dans le
pipeline sera la sélection par défaut. Si aucune étape n’est repliée, la
sélection par défaut sera la dernière étape du pipeline.

Le champ Après jours d’inactivité est fixé par défaut à `7`, mais peut être
modifié si nécessaire.

Avertissement

Le champ Après jours d’inactivité ne prend **pas** en compte le calendrier de
travail dans le suivi de la durée d’inactivité d’un ticket.

Si certaines étapes seulement doivent être utilisées pour suivre les jours
d’inactivité, elles peuvent être ajoutée au champ Pour les étapes.

Example

Le pipeline d’une équipe est créé avec les étapes suivantes :

  * `Nouveau`

  * `En cours`

  * `Retour client`

  * `Clôturé`

Les tickets peuvent s’attarder dans l’étape Retour client, car une fois le
problème résolu, les clients peuvent ne pas répondre immédiatement. À ce
moment-là, les tickets peuvent être clôturés automatiquement. Cependant, les
tickets dans les étapes Nouveau et En cours peuvent rester inactifs en raison
de problèmes d’assignation ou de charge de travail. La clôture automatique de
ces tickets aura pour effet de laisser des problèmes non résolus.

Par conséquent, les paramètres de Clôture automatique doivent être configurés
comme suit:

  * Clôture automatique : _coché_

  * Déplacer vers l’étape : `Résolu`

  * Après``7jours d’inactivité

  * Pour les étapes : `Retour client`

![Exemple de paramètres de clôture automatique.](../../../../_images/closing-
automatic-settings-example.png)

## Permettre aux clients de clôturer leurs propres tickets

L’activation du paramètre Clôture par les clients permet aux clients de
clôturer leur(s) propre(s) ticket(s) lorsqu’ils estiment que leur problème a
été résolu.

Allez à Assistance ‣ Configuration ‣ Équipes et sélectionnez une équipe. Sur
la page des paramètres de l’équipe, descendez jusqu’à la section Self-Service
et cochez la case à côté de Clôture par les clients.

![Paramètre de clôture par les clients dans Odoo
Assistance.](../../../../_images/closing-by-customer-setting.png)

Une fois les paramètres de clôture de ticket activés, un bouton Clôturer le
ticket sera disponible pour les clients lorsqu’ils consultent leur ticket sur
le portail client.

![Vue client d'une clôture de ticket dans Odoo
Assistance.](../../../../_images/closing-customer-view.png)

Note

Les clients peuvent consulter leurs tickets en cliquant sur le lien Afficher
le ticket qu’ils reçoivent par email. Le lien figure dans le modèle d”Accusé
de réception de la demande, qui est ajouté par défaut à la première étape
d’une équipe. Ce client n’exige pas que le client ait accès au portail pour
afficher ou répondre à son ticket.

Les clients ayant accès au portail pourront consulter leurs tickets sous Mon
compte ‣ Tickets.

