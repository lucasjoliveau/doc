# Évaluations

À la fin d’une conversation de _Live Chat_ , les clients ont la possibilité
d’évaluer la qualité de l’assistance qu’ils ont reçue de l” _opérateur_ de
Live Chat. Les clients fournissent des évaluations dès qu’ils mettent fin à la
conversation. Cela permet au opérateurs de recevoir un feedback immédiat sur
leurs performances. Les clients ont également la possibilité de faire part de
leurs derniers commentaires avant de quitter la fenêtre de discussion.

## Évaluer les conversations de Live Chat

Les clients mettent fin à une conversation de _live chat_ en cliquant sur le X
dans le coin supérieur droit de la fenêtre de discussion. Ils ont invités à
sélectionner une icône qui représente leur niveau de satisfaction. Les icônes
représentent les évaluations suivantes :

>   * **Satisfait** \- _visage souriant vert_
>
>   * **Bien** \- _visage neutre jaune_
>
>   * **Insatisfait** \- _visage mécontent rouge_
>
>

![Vue de la fenêtre de discussion du côté de l'utilisateur pour Odoo Live
Chat.](../../../_images/live-chat-ratings-faces.png)

Note

Lorsque les clients mettent fin à une conversation, un champ marqué Recevoir
une copie de cette conversation apparaît sous les icônes d” _évaluations_. Les
clients peuvent saisir leur adresse email avant ou après avoir soumis une
évaluation.

Si le client sélectionne l’icône Satisfait (visage souriant), un message de
remerciement s’affiche, ainsi qu’un lien pour Fermer la conversation.

![Vue de la fenêtre de live chat d'un client avec le message de
remerciement.](../../../_images/live-chat-thank-you.png)

Si le client sélectionne l’icône Bien (neutre) ou Insatisfait (visage
mécontent), une zone de texte apparaît. Les clients peuvent ajouter des
commentaires pour expliquer la raison pour laquelle ils ont choisi cette
évaluation. Ce message sera envoyé à l’opérateur de live chat avec l’icône
d’évaluation.

![Vue d'une fenêtre de discussion du côté d'un opérateur mettant en évidence
une évaluation pour Odoo Live Chat.](../../../_images/live-chat-ratings-
operator-window.png)

## Publier les évaluations des clients

Pour publier les évaluations d’un canal sur le site web, allez d’abord à
l’enregistrement d’un canal de live chat en allant à l’application Live Chat
et en cliquant sur la carte kanban de cette équipe. Cliquez ensuite sur le
bouton intelligent Aller au Site web. La page Statistiques du canal de live
chat s’ouvre alors.

Dans le coin supérieur droit de la page, cliquez sur le curseur rouge Non
publié. Le curseur passe de Non publié à Publié.

![Vue des évaluations publiées sur le portail pour Odoo Live
Chat.](../../../_images/live-chat-ratings-unpublished.png)

Note

Les notes du client qui accompagnent l’évaluation ne seront _pas_ publiées sur
le site web. Elles sont conservées en interne. Seul un aperçu statistique des
prestations des opérateurs pour le _canal_ apparaît sur le site web.

### Ajouter la page des évaluations au site

Une fois que la page des évaluations a été publiée, elle doit être ajoutée
manuellement au site web. Pour ce faire, allez au tableau de bord principal
d’Odoo et ouvrez l’application _Site Web_ : Site Web ‣ Site ‣ Contenu ‣ Pages,
puis cliquez sur Nouveau.

Une fenêtre contextuelle Nouvelle page s’affiche. Dans le champ Titre de la
page, saisissez `livechat`. Il s’agit de l’URL de la page publiée.

Important

L’URL _doit_ s’intituler `livechat` pour que la base de données reconnaisse et
connecte la page des évaluations. Après que la page a été publiée, le titre de
la page peut être modifiée avec l”Éditeur de menu.

Cliquez sur Créer, et la page nouvellement créée s’ouvrira. L”Éditeur de page
apparaît dans le panneau de droite.

La page répertorie les noms des Canaux de live chat dont les évaluations ont
été publiées. À gauche du nom du canal se trouve une icône de bulle de
dialogue sur laquelle les utilisateurs peuvent cliquer pour accéder à la page
des évaluations du canal concerné.

![Vue de la page des évaluations Live Chat mettant en évidence l'icône du
canal.](../../../_images/live-chat-published-icon.png)

Apportez les modifications ou les ajouts souhaités à cette page et cliquez sur
Enregistrer en haut à droite de l’éditeur. Le panneau latéral de l’éditeur se
ferme et la page web reste à l’écran.

Pour publier la page `livechat`, retournez à la liste des pages en allant à
Site ‣ Contenu ‣ Pages. Cliquez sur la case à gauche de `livechat` dans la
liste des pages pour sélectionner la page et surligner la ligne. Puis, cochez
la case sous la colonne intitulée Est publié. Le champ contenant la case à
cocher est surligné en blanc. Cliquez une seconde fois sur la case pour cocher
la case Est publié. La page web est maintenant publiée.

![Vue de la liste des pages d'un site web avec la case 'Est publié' mise en
évidence.](../../../_images/live-chat-is-published.png)

Une fois que la page a été ajoutée au site, les évaluations sont publiées par
défaut. Cependant, il est possible de sélectionner des évaluations
individuelles pour les cacher au public. L’évaluation sera toujours incluse
dans les rapports internes et pourra toujours être consultée par les équipes
internes. Toutefois, les visiteurs du site web publics et les utilisateurs du
portail n’y auront pas accès.

Consultez Masquer les évaluations individuelles pour plus d’informations.

## Rapport d’évaluation des clients

Le rapport Évaluations des clients (Live Chat ‣ Rapport ‣ Évaluations des
clients) montre une vue d’ensemble des évaluations reçues sur les tickets
d’assistance individuels, ainsi que tous les commentaires supplémentaires qui
accompagnent l’évaluation.

![Vue du rapport des évaluations des clients dans Odoo Live
Chat.](../../../_images/live-chat-ratings-report.png)

Le rapport se présente par défaut sous la forme d’une vue kanban, chaque
évaluation étant représentée par une carte différente. Pour passer à une vue
différente, cliquez sur l’une des icônes dans le coin supérieur droit de
l’écran. Le rapport est disponible en vue _liste_ , _tableau croisé dynamique_
et _graphique_.

Cliquez sur une évaluation individuelle pour voir plus de détails sur la
conversation et l’évaluation.

### Masquer les évaluations individuelles

Les évaluations sont publiées par défaut. Toutefois, les évaluations
individuelles peuvent être manuellement masquées au public. L’évaluation sera
toujours incluse dans les rapports internes et pourra toujours être consultée
par les équipes internes. Cependant, les visiteurs du site web publics et les
utilisateurs du portail n’y auront pas accès.

Pour masquer une évaluation, allez à l’application Live Chat ‣ Rapports ‣
Évaluations des clients. Cliquez sur la carte kanban de l’évaluation à
masquer. Sur la page détaillée de l’évaluation individuelle, cochez la case
intitulée Visible en interne uniquement.

![Vue de la page détaillée d'une évaluation individuelle avec le paramètre
visible en interne coché.](../../../_images/live-chat-ratings-visible-
internally.png)

Pour plus d'infos

  * [Live Chat](../livechat.html)

  * [Commandes et réponses enregistrées](responses.html)

  * [Site Web](../website.html)

