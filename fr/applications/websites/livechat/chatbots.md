# Chatbots

Un _Chatbot_ est un programme conçu pour imiter une conversation avec un être
humain. Les chatbots se voient attribuer un script d’étapes rédigées
préalablement à suivre. Les scripts sont conçus pour anticiper la réponse
potentielle d’un visiteur et le guider à travers une série de questions et de
réponses, comme le ferait un membre de l’équipe en chair et en os.

Les chatbots peuvent être personnalisés pour remplir différents rôles, de
l’assistance à la clientèle, à la création de pistes, en passant par la
collecte d’informations. L’objectif du chatbot dépend de la page du site web
qui lui est assignée et des messages inclus dans le script, parmi d’autres
critères.

![Vue de la fenêtre de chat avec un ticket d'assistance créé dans Konvergo ERP Live
Chat.](../../../_images/chatbot-visitor-view.png)

## Créer un chatbot

Avant de créer un nouveau chatbot, l’application _Live Chat_ doit être
installée sur la base de données. Vous pouvez le faire directement dans le
menu Apps en recherchant `Live Chat` dans la **barre de recherche** et en
cliquant sur **Installer**.

Vous pouvez également installer et activer _Live Chat_ en allant à
l’application Site Web ‣ Configuration ‣ Paramètres et en cochant la case
intitulée **Live Chat**. Une fois l’application _Live Chat_ activée, la base
de données est rafraîchie et l’application est accessible.

Une fois que l’application _Live Chat_ est installée sur la base de données,
ouvrez-la et allez à Configuration ‣ Chatbots.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsque l’application <em>Live Chat</em> est installée, un exemple de chatbot est créé, intitulé <em>Bot de bienvenue</em>. Ce chatbot a un script préconfiguré qui passe par quelques étapes de base, y compris demander une adresse email d’un visiteur et transférer la conversation à un opérateur.</p>
<p>Le <em>Bot de bienvenue</em> peut être utilisé comme point de départ. Les étapes existantes peuvent être modifiées ou supprimées et de nouvelles étapes peuvent être ajoutées pour personnaliser le script, le cas échéant.</p>
<p>Le <em>Bot de bienvenue</em> peut être supprimé (ou archivé).</p>
<img alt="Vue du script du Bot de bienvenue dans Konvergo ERP Live Chat." class="align-center" src="../../../_images/chatbot-welcome-bot.png"/>
</div>

Pour créer un nouveau chatbot, allez à la page **Chatbot** (Live Chat ‣
Configuration ‣ Chatbots) et cliquez sur **Nouveau**. Une page détaillée
vierge d’un chatbot s’affiche.

Sur la page détaillée vierge du chatbot, saisissez un nom dans le champ **Nom
du chatbot** et cliquez sur l’icône **Modifier l’image** dans le coin
supérieur droit du formulaire pour ajouter une photo.

### Scripts du chatbot

Une fois que le nouveau chatbot a été créé et nommé, l’étape suivante consiste
à créer un script. Les conversations du chatbot suivent un script
d’accompagnement. Ces scripts sont constitués de lignes de dialogue, chacune
étant conçue pour donner ou saisir des informations.

Pour créer un script de chatbot, allez à l’onglet **Script** de la page
détaillée du chatbot et cliquez sur **Ajouter une ligne** pour ouvrir le
formulaire contextuel **Créer des étapes du script**.

Ce formulaire doit être complété pour chaque ligne de texte (dialogue) que le
chatbot pourrait potentiellement délivrer au cours de la conversation.

Saisissez d’abord le contenu du message dans le champ **Message**. Puis,
sélectionnez une option dans le menu déroulant **Types d’étape**.

#### Types d’étape

Le **type d’étape** sélectionné dépend de l’objectif du message. Les options
disponibles dans le menu déroulant **Type d’étape** sont énumérées ci-dessous,
ainsi que leur utilisation et toute information complémentaire :

##### Texte

Cette étape est utilisée pour les messages pour lesquels aucune réponse n’est
attendue (ou nécessaire). Les étapes de type texte peuvent être utilisées pour
les messages d’accueil et/ou pour donner des informations.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les types d’étape de type texte visent uniquement à donner des informations et ne permettent pas au visiteur de s’exprimer. Ils doivent donc être suivis d’autres étapes pour poursuivre la conversation.</p>
</div>

##### Question

Cette étape permet de poser une question et de fournir une série de réponses.
Le visiteur clique sur une réponse, ce qui le conduit à une nouvelle étape de
la conversation ou à un lien facultatif vers une nouvelle page web.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est utile d’ajouter une réponse globale aux questions (par ex. « Autre chose »). Cela aide les visiteurs à poursuivre la conversation, même si leurs besoins ne correspondent pas exactement à l’une des autres réponses.</p>
</div>

##### Email

Cette étape invite les visiteurs à fournir leur adresse email, qui est
enregistrée et qui peut être utilisée ultérieurement par des membres de
l’équipe pour obtenir plus d’informations.

Les seules entrées acceptées pour ce type d’étape sont des adresses email dont
le format est valide. Si un visiteur tente de saisir autre chose qu’une
adresse email valide, le chatbot répond par un message indiquant qu’il ne
reconnaît pas l’information saisie.

![Vue d'un chatbot répondant à un email invalide.](../../../_images/chatbot-
invalid-email.png)

##### Téléphone

Comme pour l’email, ce type d’étape invite le visiteur à saisir son numéro de
téléphone, qui peut être utilisé ultérieurement pour obtenir plus
d’informations, planifier des démonstrations, etc.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>En raison du grand nombre de formats utilisés pour les numéros de téléphone dans le monde, les réponses à ce type d’étape ne sont <b>pas</b> validées en termes de formatage.</p>
</div>

##### Transférer à un opérateur

Cette étape permet de transmettre la conversation à un opérateur de live chat
actif, pour qu’il puisse continuer à aider le visiteur. La transcription de la
conversation étant envoyée à l’opérateur, celui-ci peut reprendre la
conversation là ou le chatbot l’a laissée. Cela permet non seulement de gagner
du temps, mais aussi de qualifier les conversations avant qu’elles
n’atteignent les opérateurs humains.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si aucun opérateur actif n’est disponible sur le canal, le chatbot poursuit la conversation avec le visiteur. Par conséquent, des étapes supplémentaires doivent être ajoutées après celle-ci pour s’assurer que la conversation ne s’arrête pas brusquement.</p>
<img alt="Vue des messages de suivi d'un chatbot lorsqu'aucun opérateur live chat n'est disponible." class="align-center" src="../../../_images/chatbot-no-operator.png"/>
</div>

##### Saisie libre/multi-lignes

L’étape de saisie libre permet aux visiteurs de répondre aux questions sans
fournir de réponses écrites préalablement. Les informations fournies dans ces
réponses sont stockées dans les transcriptions du chat.

Choisissez entre **Saisie libre** et **Saisie libre (multi-lignes)** en
fonction du type et de la quantité d’informations demandées au visiteur.

##### Créer une piste

Cette étape permet de créer une piste dans l’application _CRM_. Sélectionnez
une option dans la liste déroulante de l”**Équipe commerciale** pour assigner
la piste créée à une équipe spécifique.

##### Créer un ticket

Cette étape permet de créer un
[ticket](../../services/helpdesk/overview/receiving_tickets) dans
l’application _Assistance_. Sélectionnez une option dans la liste déroulante
**Équipe d’assistance** pour assigner le ticket créé à une équipe spécifique.

#### Seulement si

Les scripts de chatbot fonctionnent sur le principe du si/alors, ce qui
signifie que la prochaine question posée au visiteur est déterminée par la
réponse qu’il donne à la question précédente.

Pour poursuivre la progression de la conversation, le formulaire d’une
nouvelle étape contient un champ intitulé **Seulement si**. C’est dans ce
champ que la progression des questions est définie.

Si une étape est destinée à suivre tous les messages précédents, ce champ peut
être laissé vide. En revanche, si un message doit **uniquement** être envoyé
sous certaines conditions, en fonction d’une réponse précédente (ou de
plusieurs réponses précédentes), ces réponses doivent être ajoutées à ce
champ.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si des sélections sont faites dans le champ <b>Seulement si</b>, l’étape ne sera <b>pas</b> affichée dans une conversation si <b>toutes</b> les réponses n’ont pas été sélectionnées. N’incluez des sélections dans ce champ que si elles sont nécessaires à l’affichage de l’étape.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Dans le script <em>Bot de bienvenue</em>, un visiteur peut demander des informations sur les tarifs. Si le visiteur sélectionne cette réponse, une étape est prévue pour transférer la conversation à un opérateur. Le chatbot envoie d’abord un message informant le visiteur qu’il vérifie si un opérateur est disponible pour discuter.</p>
<p>Cependant, ce message doit <b>uniquement</b> être envoyé si le visiteur demande des informations sur les tarifs. Dans ce cas, la conversation se déroule comme suit :</p>
<ul>
<li><p>Bot de bienvenue : « <em>Que cherchez-vous ?</em> »</p></li>
<li><p>Visiteur : « <b>J’ai une question sur les tarifs.</b> »</p></li>
<li><p>Bot de bienvenu : « <em>Hmmm, laissez-moi vérifier si je peux trouver quelqu’un qui pourrait vous aider…</em> »</p></li>
</ul>
<p>Dans le formulaire détaillé de l’étape <b>Texte</b>, la réponse <em>J’ai une question sur les tarifs</em> a été sélectionnée dans le champ <b>Seulement si</b>. Ainsi, cette étape s’affiche <b>uniquement</b> dans les conversations où cette réponse a été sélectionnée.</p>
<img alt="Vue du formulaire du nouveau message mettant en évidence le champ Seulement si." class="align-center" src="../../../_images/chatbot-only-if.png"/>
</div>

### Test des scripts

Afin de s’assurer que tous les visiteurs ont une expérience satisfaisante avec
le chatbot, chaque message doit mener à une conclusion naturelle. Les scripts
du chatbot doivent être testés pour confirmer qu’il n’y a pas d’impasses et
pour comprendre ce que le visiteur voit lorsqu’il interagit avec le chatbot.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si une réponse ou une entrée fournie par le visiteur n’est <b>pas</b> associée à une réponse de suivi correspondante, la conversation s’arrête (<em>impasse</em>). Étant donné que le visiteur ne peut pas réengager le chatbot, il devra recommencer la conversation en rafraîchissant la fenêtre de chat ou son navigateur.</p>
</div>

Pour tester les performances d’un chatbot, cliquez d’abord sur le bouton
**Tester** dans le coin supérieur gauche de la page du script du chatbot.
Ensuite, après avoir été redirigé vers l’écran de test, répondez aux questions
du chatbot comme le ferait un visiteur potentiel du site web.

Lorsque le script a atteint un point final, le message _Conversation terminée…
Redémarrer_ apparaît en bas de la fenêtre de chat. Pour reprendre la
conversation au débit du script, cliquez sur **Redémarrer**. Pour retourner à
la page du script, cliquez sur **Retour au mode édition** en haut de la page.

## Ajouter un chatbot à un canal

Après qu’un chatbot a été créé et testé, il doit être ajouté à un canal de
live chat.

Tout d’abord, ouvrez l’application Live Chat et sélectionnez la carte kanban
d’un **Canal** ou créez-en un [nouveau](../livechat). Cliquez sur
l’onglet **Règles de canal**. Ensuite, ouvrez une règle existante ou créez-en
une nouvelle en cliquant sur **Ajouter une ligne**.

Sur le formulaire détaillé **Créer des règles** qui s’affiche, choisissez le
bon chatbot dans le champ **Chatbot**.

Si le chatbot doit **uniquement** être actif si aucun opérateur de live chat
n’est disponible, cochez la case intitulée **Activé uniquement s’il n’y a
aucun opérateur**.

![Vue des règles de canal mettant en évidence le champ
chatbot.](../../../_images/chatbot-add-to-channel.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../livechat">Règles de canal de live chat</a></p>
</div>

