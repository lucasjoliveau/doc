# Commandes et réponses enregistrées

Dans l’application _Live Chat_ d’Odoo, les _commandes_ permettent à
l’utilisateur d’effectuer des actions spécifiques à la fois dans la fenêtre de
chat et à travers d’autres applications d’Odoo. L’application _Live Chat_
comprend également des _réponses enregistrées_. Il s’agit de substitutions
préconfigurées personnalisées qui permettent aux utilisateurs de remplacer les
raccourcis par des réponses plus longues et pertinentes aux questions et aux
commentaires les plus courants.

Les commandes et les réponses enregistrées font gagner du temps et permettent
aux utilisateurs de maintenir un niveau de cohérence tout au long de leurs
conversations.

## Exécuter une commande

Les _commandes_ de live chat sont des mots-clés qui déclenchent des actions
préconfigurées. Lorsqu’un _opérateur_ de live chat participe à une
conversation avec un client ou un visiteur du site web, il peut exécuter une
commande en tapant `/`, suivi de la commande.

Les commandes et les actions qui en résultent ne sont visibles que dans la
fenêtre de conversation de l’opérateur de live chat. Un client ne verra pas
les commandes qu’un opérateur utilise dans une conversation depuis sa vue du
chat.

![Vue de la fenêtre de chat avec un ticket d'assistance créé dans Odoo Live
Chat.](../../../_images/responses-ticket-link.png)

Vous trouverez plus d’informations sur chaque commande disponible ci-dessous.

### Aide

Si un opérateur tape `/help` dans la fenêtre de chat, un message informatif
qui inclut les types d’entrées potentielles s’affiche.

  * Tapez `@nomdutilisateur` pour mentionner un utilisateur dans la conversation. Une notification sera envoyée à la boîte de réception ou à l’adresse email de cet utilisateur, en fonction de ses paramètres de notification.

  * Tapez `#canal` pour mentionner un canal de _Discussion_.

  * Tapez `/commande` pour exécuter une commande.

  * Tapez `:raccourci` pour insérer une réponse enregistrée.

![Vue du message généré par l'utilisation de la commande /help dans Odoo Live
Chat.](../../../_images/responses-help.png)

Pour plus d'infos

  * [Discussion](../../productivity/discuss.html)

  * [Utiliser les canaux pour la communication d’équipe](../../productivity/discuss/team_communication.html)

### Assistance & Rechercher des tickets d’assistance

Les commandes `/helpdesk` et `/helpdesk_search` permettent aux opérateurs de
créer des tickets d’assistance directement dans une conversation et de
rechercher des tickets existants par mot-clé ou numéro de ticket.

Important

Les commandes `/helpdesk` et `/helpdesk_search` ne peuvent être utilisées que
si l’application _Assistance_ est installée, et la fonctionnalité _Live Chat_
a été activée sur l’équipe d” _Assistance_. Pour activer Live Chat, allez à
l’application Assistance ‣ Configuration ‣ Équipes et sélectionnez une équipe.
Faites défiler jusqu’à la section Canaux et cochez la case intitulée Live
Chat.

#### Créer un ticket à partir d’un live chat

Si un opérateur tape `/helpdesk` dans la fenêtre de chat, la conversation est
utilisée pour créer un ticket d” _Assistance_.

Important

Dans la version 16.3, la commande pour créer un nouveau ticket est `/ticket`.
Ceci ne s’applique qu’aux bases de données fonctionnant avec la version 16.3.

Après avoir saisi la commande `/helpdesk`, donnez un nom au ticket dans la
fenêtre de chat et appuyez sur `Enter`.

![Vue des résultats d'une recherche dans les tickets d’assistance dans une
conversation de live chat.](../../../_images/helpdesk.png)

Le ticket nouvellement créé sera ajouté à l’équipe d” _Assistance_ qui a
activé le live chat. Si plusieurs équipes ont activé le live chat, le ticket
sera automatiquement assigné en fonction de la priorité de l’équipe.

La transcription de la conversation sera ajoutée au nouveau ticket, dans
l’onglet Description.

Pour accéder au nouveau ticket, cliquez sur le lien dans la fenêtre de chat ou
allez à l’application Assistance et cliquez sur le bouton Tickets sur la carte
kanban de l’équipe appropriée.

#### Rechercher un ticket dans une fenêtre de live chat

Si un opérateur tape `/helpdesk_search` dans la fenêtre de chat, il peut
rechercher des tickets d” _Assistance_ par numéro de ticket ou par mot-clé.

Important

Dans la version 16.3, la commande pour rechercher des tickets d” _Assistance_
est `/search_tickets`. Ceci ne s’applique qu’aux bases de données fonctionnant
avec la version 16.3.

Après avoir saisi la commande `/helpdesk_search`, saisissez un mot-clé ou un
numéro de ticket et appuyez sur `Enter`. Si un ou plusieurs tickets associés
sont trouvés, une liste de liens sera générée dans la fenêtre de conversation.

![Vue des résultats d'une recherche dans les tickets d’assistance dans une
conversation de live chat.](../../../_images/helpdesk-search.png)

Note

Les résultats de la commande de recherche ne sont visibles que par
l’opérateur, et non par le client.

### Historique

Si un opérateur tape `/history` dans la fenêtre de chat, il obtient une liste
des pages les plus récentes que le visiteur a consultées sur le site web
(jusqu’à 15).

![Vue des résultats d'une commande /history dans une conversation de Live
Chat.](../../../_images/responses-history.png)

### Piste

En saisissant `/lead` dans la fenêtre de chat, un opérateur peut créer une
_piste_ dans l’application _CRM_.

![Vue des résultats d'une commande /lead dans une conversation de Live
Chat.](../../../_images/responses-lead.png)

Important

La commande `/lead` ne peut être utilisée que si l’application _CRM_ est
installée.

Après avoir saisi `/lead`, donnez à nom à cette nouvelle piste, puis appuyez
sur `Enter`. Un lien avec le nom de la piste s’affiche. Cliquez sur le lien ou
allez à l’application CRM pour afficher le Pipeline.

Note

Le lien vers la nouvelle piste ne peut être affichée et accédée que par
l’opérateur, pas par le client.

La transcription de cette conversation de live chat en particulier (dans
laquelle la piste a été créée) est ajoutée à l’onglet Notes internes du
formulaire de la piste.

Dans l’onglet Informations supplémentaires du formulaire de la piste, Live
Chat sera mentionné comme Source.

### Quitter

Si un opérateur tape `/leave` dans la fenêtre de chat, il peut automatiquement
quitter la conversation. Cette commande n’entraîne pas la suppression du
client de la conversation et ne met pas automatiquement fin à la conversation.

Pour plus d'infos

  * [Acquérir des pistes](../../sales/crm/acquire_leads.html)

  * [Démarrer avec Assistance](../../services/helpdesk/overview/getting_started.html)

## Réponses enregistrées

Les _réponses enregistrées_ sont des entrées personnalisables dans lesquelles
un _raccourci_ remplace une réponse plus longue. Un opérateur saisit le
raccourci, qui est automatiquement remplacé par la réponse de _substitution_
plus longue dans la conversation.

### Créer des réponses enregistrées

Pour créer une nouvelle réponse enregistrée, allez à l’application Live Chat ‣
Configuration ‣ Réponses enregistrées ‣ Nouveau.

À partir de là, tapez la commande de raccourci dans le champ Raccourci.

Ensuite, cliquez sur le champ Substitution et saisissez le message
personnalisé qui sera envoyé aux visiteurs à la place du raccourci. Cliquez
sur Enregistrer.

Astuce

Essayez d’associer le raccourci au sujet de la substitution. Plus les
opérateurs s’en souviennent facilement, plus il sera facile d’utiliser les
réponses enregistrées dans les conversations.

### Utiliser des réponses enregistrées dans une conversation de live chat.

Pour utiliser une réponse enregistrée dans une conversation de live chat,
tapez deux points (`:`) dans la fenêtre de chat, suivi du raccourci.

Example

Un opérateur est en train de discuter avec un visiteur. Dès qu’il saisit `:`,
il voit une liste des réponses disponibles. Il peut en sélectionner une
manuellement dans la liste ou continuer à écrire. S’il veut utiliser la
réponse enregistrée `'I am sorry to hear that.'`, il peut taper `:sorry`.

![Vue d'une fenêtre de chat et de l'utilisation d'une réponse enregistrée dans
Odoo Live Chat.](../../../_images/canned-responses.png)

Astuce

Le fait de taper `:` dans une fenêtre de chat génère une liste des réponses
enregistrées disponibles. Vous pouvez sélectionner les réponses manuellement
dans la liste ou utiliser le raccourci.

![Vue d'une fenêtre de chat et de la liste des réponses enregistrées
disponibles.](../../../_images/response-list.png)

