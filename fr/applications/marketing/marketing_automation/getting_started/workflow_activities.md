# Activités du flux de travail de la campagne

Lors de la création d’une campagne de marketing dans l’application _Marketing
Automation_ , les utilisateurs peuvent planifier des activités de marketing
qui peuvent être déclenchées lorsque certaines actions ou inactions se
produisent. Il peut s’agit d’activités telles que des emails automatisés, des
SMS ou des actions sur le serveur interne.

## Ajouter des activités au flux de travail

Pour ajouter des activités au flux de travail d’une campagne de marketing,
allez jusqu’au bas d’un formulaire détaillé de campagne préexistant ou
nouveau, sous les champs de configuration de l’audience cible, et cliquez sur
Ajouter une nouvelle activité.

Cette opération fait apparaître une fenêtre contextuelle Créer des activités.
Il s’agit d’un modèle d’activité vierge, dans lequel des paramètres
spécifiques peuvent être définis pour cette activité spécifique.

![Une fenêtre contextuelle d'un modèle d'activité de flux de travail dans Odoo
Marketing Automation.](../../../../_images/activity-template.png)

Donnez d’abord un nom à l’activité dans le champ Nom de l’activité. Ensuite,
procédez à la configuration des options suivantes.

Lorsque vous êtes prêt, cliquez sur Enregistrer & Fermer pour enregistrer
l’activité et fermer le formulaire contextuel, Enregistrer & Nouveau pour
enregistrer l’activité et immédiatement créer une autre activité dans un
nouveau formulaire contextuel Créer des activités ou Ignorer pour supprimer
l’activité.

### Types d’activité

Sélectionnez ensuite le Type d’activité. Choisissez entre Email, Action de
serveur (une action interne dans la base de données) ou SMS.

Le champ sous le Type d’activité varie en fonction du Type d’activité choisi.

#### L’activité Email

Si vous choisissez Email comme Type d’activité, vous pouvez choisir un Modèle
d’email prédéfini/préconfiguré. Vous pouvez également créer un modèle d’email
à la volée.

Pour créer un nouveau modèle directement à partir du champ Modèle d’email,
commencez par taper le titre du nouveau modèle dans le champ vierge à côté du
Modèle d’email, et cliquez sur Créer et modifier… pour faire apparaître une
fenêtre contextuelle Créer un modèle de marketing.

![L'option Créer et modifier dans le menu déroulant Email dans la fenêtre
contextuelle Créer des activités.](../../../../_images/email-activity-create-
edit.png)

Dans cette fenêtre contextuelle, vous pouvez créer et configurer le nouveau
modèle d’email.

![La fenêtre contextuelle permettant de créer un modèle de marketing dans Odoo
Marketing Automation.](../../../../_images/create-marketing-template-popup-
window.png)

#### L’activité Action de serveur

Si vous choisissez Action de serveur comme Type d’activité, il est possible de
choisir une Action de serveur spécifique (par ex. Message pour un vendeur,
Créer des pistes lorsqu’elles cliquent sur le site web, etc.).

Il est également possible de créer une nouvelle action de serveur directement
à partir de l’option Action de serveur. Pour ce faire, donnez un nom à la
nouvelle action, puis cliquez sur Créer et modifier… dans le menu déroulant.

![L'option Créer et modifier dans le champ Action de serveur du formulaire de
campagne.](../../../../_images/server-action-create-edit-option.png)

Vous pouvez également cliquez sur le champ Action de serveur vide pour ouvrir
un menu déroulant et ainsi sélectionner Recherche avancée… pour faire
apparaître une fenêtre contextuelle Recherche : Action de serveur, contenant
toutes les actions de serveur préconfigurées disponibles.

Pour créer une nouvelle action de serveur à partir de cette fenêtre
contextuelle, cliquez sur Nouveau.

![Le bouton Nouveau sur la fenêtre contextuelle Action de serveur de
l'application Marketing Automation.](../../../../_images/search-server-action-
new-button.png)

Les deux options font apparaître une fenêtre contextuelle Créer une action de
serveur, dans laquelle vous pouvez créer et configurer une action de serveur
personnalisée.

#### L’activité SMS

Si vous choisissez SMS comme Type d’activité, il est possible de choisir un
Modèle SMS prédéfini et préconfiguré.

Pour créer un nouveau modèle directement à partir du champ Modèle SMS,
commencez par écrire le titre du nouveau modèle dans le champ vierge à côté de
Modèle SMS, et sélectionnez Créer et modifier… dans le menu déroulant.

![L'option Créer et modifier dans le menu déroulant Email dans la fenêtre
contextuelle Créer des activités.](../../../../_images/create-edit-sms-
option.png)

Cette opération fait apparaître une fenêtre contextuelle Créer un modèle de
marketing, dans laquelle vous pouvez créer et configurer le nouveau modèle
SMS.

![La fenêtre contextuelle permettant de créer un modèle SMS à la
volée.](../../../../_images/sms-marketing-template-popup.png)

### Déclencher

Le champ Déclencher dans la fenêtre contextuelle Créer des activités permet
aux utilisateurs de choisir quand l’activité désignée doit être déclenchée.

Commencez par sélectionner un chiffre dans le premier champ. Dans le champ
Déclencher suivant, indiquez s’il s’agit d”Heures, de Jours, de Semaines, ou
de Mois. Cliquez ensuite sur le dernier champ, qui lit par défaut le début du
flux de travail pour faire apparaître un menu déroulant avec d’autres options
de déclenchement.

![Une liste des déclencheurs disponibles sur le formulaire contextuel des
activités de flux de travail.](../../../../_images/trigger-options-drop-down-
menu.png)

Les options de déclenchement sont les suivantes :

  * le début du flux de travail : l’activité sera déclenchée au moment préalablement configuré après le début du flux de travail.

  * une autre activité : l’activité sera déclenchée au moment préalablement configuré après une autre activité spécifique du flux de travail.

  * Email : ouvert : l’activité sera déclenchée au moment préalablement configuré si le destinataire a ouvert l’email envoyé dans le flux de travail.

  * Email : pas ouvert : l’activité sera déclenchée au moment préalablement configuré si le destinataire n’a pas ouvert l’email envoyé dans le flux de travail.

  * Email : répondu : l’activité sera déclenchée au moment préalablement configuré si le destinataire a répondu à l’email envoyé dans le flux de travail.

  * Email : non répondu : l’activité sera déclenchée au moment préalablement configuré si le destinataire n’a pas répondu à l’email envoyé dans le flux de travail.

  * Email : cliqué : l’activité sera déclenchée au moment préalablement configuré si le destinataire a ouvert et cliqué sur l’email envoyé dans le flux de travail.

  * Email : non cliqué : l’activité sera déclenchée au moment préalablement configuré si le destinataire a ouvert, mais n’a pas cliqué sur l’email envoyé dans le flux de travail.

  * Email : rejeté : l’activité sera déclenchée au moment préalablement configuré si l’email envoyé dans le flux de travail a été rejeté pour une raison quelconque.

  * SMS : cliqué : l’activité sera déclenchée au moment préalablement configuré si le destinataire a ouvert et cliqué sur le SMS envoyé dans le flux de travail.

  * SMS : non cliqué : l’activité sera déclenchée au moment préalablement configuré si le destinataire a ouvert, mais n’a pas cliqué sur le SMS envoyé dans le flux de travail.

  * SMS : rejeté : l’activité sera déclenchée au moment préalablement configuré si le SMS envoyé dans le flux de travail a été rejeté pour une raison quelconque.

### Durée d’expiration

Ensuite, sur le formulaire contextuel Créer des activités se trouve l’option
Durée d’expiration.

L’option Durée d’expiration permet de configurer l’activité pour qu’elle
s’arrête au bout d’un certain temps (après la date prévue).

Lorsque la case est cochée, le champ Annuler après apparaître, dans lequel
vous pouvez configurer le nombre d”Heures, Jours, Semaines ou Mois pour que
les actions cessent après la date initiale.

![Liste des options de durée d'expiration disponibles dans le formulaire
contextuel des activités de flux de travail.](../../../../_images/expiry-
duration-field-options.png)

### Activité et filtres appliqués

Dans la section Domaine du formulaire contextuel Créer des activités, vous
trouverez les champs Filtre d’activité et Filtre appliqué.

Le champ Filtre d’activité permet de configurer un domaine de filtre des
destinataires qui s’applique à cette activité _et_ ses activités enfants. Il
fonctionne de la même manière qu’un filtre d’audience cible classique.

Pour ajouter un filtre d’activité, cliquez sur Ajouter une condition dans le
champ Filtre d’activité et configurez une ou plusieurs règles d’équation de
filtrage d’activité personnalisées.

![Comment ajouter un filtre d'activité à une activité du flux de travail dans
Odoo Marketing Automation.](../../../../_images/activity-filter-option.png)

Cette option n’est pas obligatoire. Si le champ est vide, l’activité
s’applique à tous les enregistrements liés à l’audience cible de la campagne
globale.

Pour plus d'infos

  * [Cibler un public](target_audience.html)

Le champ Filtre appliqué ne peut pas être configuré. Il résume simplement le
moment où l’activité sera déclenchée, _uniquement_ si elle satisfait au
domaine spécifique (par ex. les règles configurées dans le champ Filtre
d’activité).

Note

Après avoir configuré tous les paramètres de l’activité, cliquez sur
Enregistrer & Fermer pour enregistrer l’activité et retourner au formulaire de
campagne d’automatisation du marketing, cliquez sur Enregistrer & Nouveau pour
enregistrer l’activité et immédiatement en créer une autre dans une nouvelle
fenêtre contextuelle Créer des activités ou cliquez sur Ignorer pour supprimer
l’activité et retourner au formulaire de campagne d’automatisation du
marketing.

## Activité du flux de travail

Une fois qu’une activité est créée et enregistrée, elle apparaît sous forme de
carte dans la section Flux de travail, située au bas du formulaire de la
campagne de marketing automation. Les analyses liés à chaque activité
s’affichent sous la forme d’un graphique linéaire.

![Activité du flux de travail typique dans Odoo Marketing
Automation](../../../../_images/workflow-activity.png)

L’heure de déclenchement configurée pour cette activité se trouve à gauche de
la carte Activité du flux de travail dans la section Flux de travail.

Une fois que l’activité a été déclenchée, un chiffre représentant le nombre de
Réussites ou d”Échecs s’affiche à droite du graphique.

Astuce

Si le Type d’activité de l’activité est défini sur Email ou SMS, des analyses
plus détaillés sont disponibles sous les données du graphique d’activité,
présentant le nombre de messages envoyés, et le pourcentage de ceux qui ont
été cliqués, qui ont été répondus ou qui ont été rejetés.

## Activités enfants

Vous avez également la possibilité d’ajouter une _activité enfant_ en cliquant
sur Ajouter une activité enfant, situé en bas de chaque bloc d’activité dans
la section Flux de travail d’un formulaire de campagne de marketing.

Les activités enfants sont des sous-activités qui sont liées à l’activité
située au-dessus d’elles et déclenchées par elle, appelée _activité parent_.
Une activité enfant est facile à reconnaître, car elle est légèrement en
retrait par rapport à l’activité parent.

![Une activité enfant typique en retrait sous son activité
parent.](../../../../_images/indented-child-activity.png)

Odoo propose un certain nombre d’options de déclenchement pour lancer une
activité enfant - qui dépendent toutes des configurations de déclenchement de
l’activité parent. Sous l’activité parent souhaitée, survolez Ajouter une
activité enfant pour faire apparaître un menu avec les options de
déclenchement.

![Les différentes options de déclenchement de l'activité enfant dans la
section flux de travail d'une campagne.](../../../../_images/child-activity-
trigger-options.png)

Sélectionnez l’un des déclencheurs d’activité enfant suivants :

  * Ajouter une autre activité : ajoute immédiatement une autre activité.

  * Ouvert : la prochaine activité sera déclenchée si le destinataire ouvre le mailing.

  * Pas ouvert : la prochaine activité sera déclenchée si le destinataire n’ouvre pas le mailing.

  * Répondu : la prochaine activité sera déclenchée si le destinataire répond au mailing.

  * Pas répondu : la prochaine activité sera déclenchée si le destinataire ne répond pas au mailing.

  * Cliqué : la prochaine activité sera déclenchée si le destinataire clique sur un lien inclus dans le mailing.

  * Pas cliqué : la prochaine activité sera déclenchée si le destinataire ne clique pas sur un lien inclus dans le mailing.

  * Rejeté : la prochaine activité sera déclenchée si l’email est rejeté (pas envoyé).

Une fois que vous avez sélectionné un déclencheur, l’utilisateur peut
configurer l’activité enfant de la même manière qu’une activité normale du
flux de travail.

Pour plus d'infos

  * [Tester/lancer des campagnes](testing_running.html)

