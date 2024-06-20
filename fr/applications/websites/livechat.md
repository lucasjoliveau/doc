# Live Chat

Odoo _Live Chat_ permet aux utilisateurs de communiquer avec les visiteurs du
site web en temps réel. Avec _Live Chat_ , vous pouvez qualifier les pistes en
raison de leur potentiel de vente, vous pouvez rapidement répondre aux
questions d’assistance et vous pouvez rediriger les problèmes vers la bonne
équipe pour qu’elle les examine (ou suive) plus en détail. _Live Chat_ permet
également d’obtenir un feedback instantané de la part des clients.

## Activer le Live Chat

Afin d’activer le _Live Chat_ , l’application _Live Chat_ doit être installée.
Il y a deux façons de le faire.

  * Allez à Apps ‣ Live Chat et cliquez sur Installer.

  * Dans l’application Site Web, allez à Configuration ‣ Paramètres, faites défiler jusqu’à la section Email & Marketing, cochez la case à côté de Live Chat et cliquez sur Enregistrer.

![Vue de la page des paramètres et de la fonctionnalité de live chat pour Odoo
Live Chat.](../../_images/enable-setting.png)

Après l’installation de l’application Live Chat, un Canal de live chat est
créé par défaut et automatiquement sélectionné dans le menu déroulant.

## Créer un nouveau canal de live chat

Pour créer un nouveau _Canal_ de live chat, allez au Tableau de bord principal
d’Odoo ‣ Application Live Chat ‣ Nouveau. Un formulaire détaillé de canal
vierge s’affiche. Saisissez le nom du nouveau canal dans le champ Nom du
canal.

![Vue d'un formulaire de canal de live chat pour Odoo Live
Chat.](../../_images/open-channel.png)

Pour configurer les autres onglets du formulaire détaillé du canal
(Opérateurs, Options, Règles de canal et Widgets), suivez les étapes
suivantes.

### Opérateurs

Les _Opérateurs_ sont les utilisateurs qui répondront aux demandes de live
chat des clients. Lorsqu’un utilisateur est ajouté en tant qu’opérateur dans
un canal de live chat, ils pourront recevoir des messages des visiteurs du
site web où qu’ils se trouvent dans la base de données. Des fenêtres de chat
s’ouvriront dans le coin inférieur droit de l’écran.

![Vue d'une fenêtre contextuelle de live chat dans une base de données
Odoo.](../../_images/pop-up1.png)

L’utilisateur qui a initialement créé le canal de live chat sera par défaut
ajouté en tant qu’opérateur.

Pour ajouter des utilisateurs supplémentaires, retournez au tableau de bord
des Canaux de live chat du site web par le fil d’Ariane et cliquez sur le
Canal de live chat approprié. Ensuite, sur le formulaire détaillé du canal,
dans l’onglet Opérateurs, cliquez sur AJOUTER pour afficher une fenêtre
contextuelle Ajouter : Opérateurs.

Dans la fenêtre contextuelle, recherchez le ou les utilisateurs souhaités.
Cochez la case à coté du ou des utilisateurs à ajouter et cliquez sur
SÉLECTIONNER.

Il est possible de créer et d’ajouter de nouveaux opérateurs à la liste
directement dans cette fenêtre contextuelle en cliquant sur Nouveau et en
remplissant le formulaire Créer des opérateurs. Une fois le formulaire
complété, cliquez sur ENREGISTRER & FERMER (ou ENREGISTRER & NOUVEAU pour
créer plusieurs enregistrements).

Note

Il est possible de modifier (ou de supprimer) les opérateurs actuels en
cliquant sur leurs cases respectives dans l’onglet Opérateurs, qui fait
apparaître une fenêtre contextuelle séparée Ouvrir : Opérateurs. Dans cette
fenêtre contextuelle, faites tous les changements nécessaires et cliquez sur
Enregistrer, ou cliquez sur Supprimer pour supprimer cet opérateur du canal.

### Options

L’onglet Options sur le formulaire détaillé du canal de live chat contient les
paramètres visuels et textuels de la fenêtre de live chat.

#### Bouton Live Chat

Le _Bouton Live Chat_ est l’icône qui apparaît dans le coin inférieur du site
web.

![Vue d'un site web d'Odoo mettant en évidence le bouton Live
Chat.](../../_images/chat-button.png)

Modifiez le texte dans le champ Texte du bouton pour mettre à jour le message
d’accueil affiché dans la bulle de texte lorsque le bouton de live chat
apparaît sur le site web.

Modifiez la Couleur du bouton de live chat en cliquant sur une bulle de
couleur pour ouvrir la fenêtre de sélection des couleurs. Cliquez sur l’icône
🔄 (rafraîchir) à droite des bulles de couleur pour rétablir les couleurs par
défaut.

Astuce

La sélection des couleurs du bouton ou de l’en-tête peuvent être sélectionnés
manuellement à l’aide d’un curseur ou en entrant le code couleur RGB, HSL ou
HEX dans la fenêtre contextuelle de sélection des couleurs qui s’affiche
lorsque vous cliquez sur l’une des bulles de couleur. Différentes options sont
disponibles en fonction de votre système d’exploitation.

#### Fenêtre de live chat

La _Fenêtre de live chat_ est l’espace où se déroule la conversation en direct
avec les visiteurs du site web.

Modifiez le Message d’accueil pour changer le message qu’un visiteur voit
lorsqu’il ouvre une nouvelle session de chat. Ce message semblera avoir été
envoyé par un opérateur de live chat et servira à la fois de message d’accueil
et d’invitation à poursuivre la conversation.

Modifiez le Placeholder de l’entrée de conversation pour modifier le texte qui
apparaît qui apparaît dans la case où les visiteurs saisissent leur réponse.

L” _En-tête du canal_ est la barre colorée située en haut de la fenêtre de
chat. La Couleur de l’en-tête du canal peut être modifiée de la même manière
que la _Couleur du bouton de live chat_ ci-dessus.

![../../_images/chat-window.png](../../_images/chat-window.png)

La fenêtre de live chat avec un en-tête violet. Le placeholder de l’entrée de
conversation indique « Posez une question… »

### Règles de canal

L’onglet Règles de canal sur le formulaire détaillé du canal de live chat
détermine quand la _Fenêtre de live chat_ s’ouvre sur le site web, par la
configuration du déclenchement d’une action URL Regex (par ex. la visite d’une
page).

Pour créer une nouvelle règle de canal, cliquez sur Ajouter une ligne. Une
fenêtre contextuelle Ouvrir : Règles s’affiche.

![Vue d'un formulaire de règles de canal pour Odoo Live
Chat.](../../_images/create-rules.png)

#### Créer de nouvelles règles

Remplissez les champs de la fenêtre contextuelle Ouvrir : Règles comme il est
indiqué ci-dessus, puis cliquez sur Enregistrer.

Live Chat ButtonChatbotURL RegexOpen automatically timerCountry

Le _Bouton Live Chat_ est l’icône qui s’affiche dans le coin inférieur du site
web. Choisissez parmi les options d’affichage suivantes :

  * Afficher affiche le bouton de chat sur la ou les pages.

  * Afficher avec notification affiche le bouton de chat, ainsi qu’une bulle de texte flottant à côté du bouton.

  * Ouvrir automatiquement affiche le bouton et ouvre automatiquement la fenêtre de chat après un certain laps de temps (défini dans le champ Minuteur pour l’ouverture automatique).

  * Masquer masque le bouton de chat sur la ou les pages.

Si un _Chatbot_ est prévu sur ce canal, sélectionnez-le dans le menu
déroulant. Si le chatbot n’est actif que quand aucun opérateur n’est actif,
cochez la case intitulée Activé uniquement s’il n’y a aucun opérateur.

Dans le champ URL Regex, saisissez l’URL relative de la page où le bouton de
chat doit s’afficher.

Ce champ indique le laps de temps (en secondes) pendant lequel une page doit
être ouverte avant que la fenêtre de chat ne s’ouvre. Si le Bouton Live Chat
de cette règle n’est pas défini sur Ouvrir automatiquement, ce champ sera
ignoré.

Si ce canal ne doit être accessible qu’aux visiteurs de certains pays, ajoutez
ces pays dans le champ Pays. Si ce champ est laissé vide, le canal sera
accessible à tous les visiteurs du site web, quel que soit leur lieu de
résidence.

Note

In order to track the geographical location of visitors, GeoIP must be
installed on the database. While this feature is installed by default on _Odoo
Online_ , _On-Premise_ databases will require additional [setup
steps](../../administration/on_premise/geo_ip.html).

### Widget

L’onglet Widget sur le formulaire détaillé du canal de live chat fournit un
code court pour le widget de site web intégrable. Ce code peut être ajouté à
un site web pour donner accès à une fenêtre de live chat.

Le widget de live chat peut être ajouté aux sites web créés via Odoo en allant
à Site Web ‣ Configuration ‣ Paramètres. Ensuite, faites défiler jusqu’à la
section Live Chat et sélectionnez le canal à ajouter au site. Cliquez sur
Enregistrer pour l’appliquer.

Pour ajouter le widget à un site web créé sur une plateforme externe, cliquez
sur le premier bouton COPIER dans l’onglet Widget et collez le code dans
l’étiquette `<head>` sur le site.

De même, pour envoyer une session de live chat à un client, cliquez sur le
deuxième bouton COPIER dans l’onglet Widget. Ce lien peut être envoyé
directement à un client et une fois qu’il aura cliqué sur le lien, il ouvrira
une nouvelle session de chat.

![Vue de l'onglet widget pour Odoo Live Chat.](../../_images/widget-code.png)

## Participer à une conversation

Comme il est expliqué ci-dessus, les _opérateurs_ sont les utilisateurs qui
répondent aux demandes de live chat des clients. Les informations suivantes
décrivent les étapes nécessaires pour que les opérateurs participent à des
conversations de live chat dans une base de données Odoo.

### Définir un nom de chat en ligne

Avant de participer à un live chat, les opérateurs doivent mettre à jour leur
_Nom de chat en ligne_. C’est le nom qui sera affiché aux visiteurs du site
web dans la conversation de live chat.

Pour mettre à jour le Nom de chat en ligne, cliquez sur le nom d’utilisateur
dans le coin supérieur droit de n’importe quelle page sur la base de données.
Sélectionnez Mon profil pour ouvrir la page du profil. Dans la partie droite
de l’onglet Préférences, repérez le champ Nom de chat en ligne et saisissez le
nom que vous préférez.

![Vue de l'option Mon profil dans Odoo.](../../_images/my-profile.png)

Si un utilisateur n’a pas défini de Nom de chat en ligne, le nom affiché sera
par défaut le Nom d’utilisateur.

Example

Un utilisateur a son nom complet comme Nom d’utilisateur, mais il ne veut pas
inclure son nom de famille dans une conversation de live chat. Il doit alors
définir son Nom de chat en ligne de manière à ce qu’il ne contienne que son
prénom.

![Vue d'un profil utilisateur dans Odoo, mettant en évidence le champ de Nom
de chat en ligne.](../../_images/online-chat-name.png)

### Rejoindre ou quitter un canal

Pour rejoindre un canal de live chat, allez à l’application Live Chat et
cliquez sur le bouton REJOINDRE sur la carte kanban du canal approprié.

Tout canal où l’utilisateur est actuellement actif affichera un bouton
QUITTER. Cliquez sur ce bouton pour vous déconnecter du canal.

![Vue d'un formulaire de canal et de l'option de rejoindre un canal pour Odoo
Live Chat.](../../_images/leave-channel.png)

Important

Les _Opérateurs_ qui ne montrent aucune activité dans Odoo pendant plus de
trente minutes seront considérés comme déconnectés et ensuite supprimés du
canal.

### Gérer les demandes de live chat

Lorsqu’un opérateur est actif dans un canal, des fenêtres de chat s’ouvrent
dans le coin inférieur de l’écran, quel que soit l’endroit où il se trouve
dans la base de données. Il peut ainsi participer à des conversations sans
quitter sa page actuelle.

Astuce

Il est également possible d’accéder aux conversations en cliquant sur l’icône
Conversations dans la barre de menu.

![Vue de la barre de menu dans Odoo mettant en évidence l'icône des
conversations.](../../_images/menu-bar.png)

Les conversations de live chat peuvent également être visualisées en allant au
Tableau de bord ‣ Discussion. Les nouvelles conversations apparaîtront en gras
sous l’en-tête LIVE CHAT dans le panneau de gauche.

![Vue de l'application Discussion avec un message envoyé par le live chat
d'Odoo.](../../_images/managing-chat-responses.png)

Cliquez sur une conversation dans le panneau de gauche pour la sélectionner.
Cela ouvrira la conversation. À partir de cette vue, un opérateur peut
participer au chat comme il le ferait dans une fenêtre de chat normale.

Pour plus d'infos

  * [Get Started with Discuss](../productivity/discuss.html)

  * [Commandes et réponses enregistrées](livechat/responses.html)

  * [Évaluations](livechat/ratings.html)
  * [Commandes et réponses enregistrées](livechat/responses.html)
  * [Chatbots](livechat/chatbots.html)

