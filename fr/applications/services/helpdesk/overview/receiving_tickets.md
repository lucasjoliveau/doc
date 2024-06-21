# Commencer à recevoir des tickets

Konvergo ERP _Assistance_ propose de multiples canaux par lesquels les clients peuvent
demander de l’aide, tels que l’email, le live chat et le formulaire de contact
sur le site web. Les clients disposent ainsi de multiples possibilités de
recevoir une assistance rapidement, tout en donnant à l’équipe d’assistance la
possibilité de gérer les tickets d’assistance multicanaux à partir d’un
emplacement central.

## Activer les options de canal pour soumettre des tickets

Allez à Assistance ‣ Configuration ‣ Équipes et choisissez une équipe
existante ou cliquez sur **Nouveau** pour [créer une nouvelle
équipe](getting_started).

Sur la page des paramètres de l’équipe, descendez jusqu’à la section
**Canaux**. Sélectionnez un ou plusieurs canaux à activer en cochant la ou les
cases respectives.

  * **Alias de messagerie**

  * **Formulaire de site web**

  * **Live Chat**

### Alias de messagerie

Le paramètre _Alias de messagerie_ crée automatiquement des tickets à partir
des messages envoyés à l’alias de messagerie de l’équipe.

Pour modifier l’alias de messagerie d’une équipe d” _Assistance_ , allez à la
page des paramètres des **Équipes**. Repérez **Alias de messagerie** sous le
titre **Canaux** et saisissez l’alias souhaité pour l’équipe dans le champ.

Lors de la création d’une nouvelle équipe d” _Assistance_ , un **alias de
messagerie** est également créé. Cet alias peut être modifié dans le champ
**Alias**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si aucun domaine personnalisé n’est encore configuré pour la base de données, cliquez sur <b>Configurer un domaine personnalisé</b> pour être redirigé vers la page des <b>Paramètres</b>. De là, activez <b>Serveurs de messagerie personnalisés</b>.</p>
</div> ![Vue de la page des paramètres d'une équipe d'assistance
mettant en évidence la fonctionnalité de l'alias de messagerie dans Konvergo ERP
Assistance.](../../../../_images/receiving-tickets-email-alias.png)

À la réception d’un email, la ligne d’objet de l’email devient le titre d’un
nouveau ticket d” _Assistance_. Le corps de l’email est également ajouté au
ticket dans l’onglet **Description** et dans le **Chatter** du ticket.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les étapes de configuration susmentionnées s’appliquent aux bases de données <b>Konvergo ERP Online</b> et <b>Konvergo ERP.sh</b>. Pour les bases de données <b>On-premise</b>, il est possible qu’une configuration supplémentaire des serveurs de messagerie personnalisés et des alias de messagerie soit demandée.</p>
</div>

### Formulaire de site web

L’activation du paramètre _Formulaire de site web_ ajoute une nouvelle page au
site web contenant un formulaire personnalisable. Un nouveau ticket est créé
dès que les champs obligatoires du formulaires sont complétés et soumis.

Pour activer le formulaire de site web, allez à la page de paramètres d’une
équipe via Configuration ‣ Équipes. Repérez la fonctionnalité **Formulaire de
site web** dans la section **Canaux** et cochez la case.

Une fois la fonctionnalité activée, cliquez sur le bouton intelligent **Allez
au site web** en haut de la page des paramètres des **Équipes** pour
visualiser et modifier le nouveau formulaire de site web créé automatiquement
par Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Après avoir activé le formulaire de site web, il se peut que la page des paramètres des <em>Équipes</em> doive être actualisée avant que le bouton intelligent <em>Allez au site web</em> n’apparaisse.</p>
<p>De même, si un <em>Centre d’assistance</em> est publié, le bouton intelligent y redirigera en premier. Cliquez simplement sur le bouton <b>Contactez-nous</b> en bas du forum pour aller au formulaire de soumission de ticket.</p>
</div> ![Vue de la page des paramètres d'une équipe d'assistance
mettant en évidence le bouton Allez au site web dans Konvergo ERP
Assistance.](../../../../_images/receiving-tickets-go-to-website.png)

#### Personnaliser le formulaire de ticket du site web

Pour personnaliser le formulaire de soumission de ticket par défaut, cliquez
sur le bouton **Modifier** dans le coin supérieur droit de la page. Ensuite,
cliquez sur un des champs du formulaire.

Ajoutez, enlevez ou mettez à jour les champs si nécessaire pour modifier les
informations soumises par les clients. Les champs peuvent être marqués comme
**Requis** , en passant du gris au bleu dans la fenêtre de l’éditeur du
constructeur de site web, situé sous la section **Champ**. Il est également
possible d’modifier d’autres informations pertinentes, telles que :

  * **Type** : qui fait correspondre une valeur du modèle Konvergo ERP au champ (par ex. `Nom du client`).

  * **Type d’entrée** : pour déterminer le type d’entrée du champ, comme `Texte`, `Email`, `Téléphone` ou `URL`.

  * **Libellé** : pour donner un libellé au champ du formulaire (par ex. `Nom complet`, `Adresse email`, etc.). Vous pouvez également contrôler la position du libellé sur le formulaire en utilisant les options imbriquées de **Position**.

  * **Description** : permet d’ajouter une ligne éditable sous le champ de saisie afin de fournir des informations contextuelles supplémentaires sur le champ.

  * **Placeholder** : pour ajouter un exemple de valeur de saisie.

  * **Valeur par défaut** : pour ajouter des valeurs de cas d’utilisation courants que la plupart des clients trouveront utiles.

  * **Requis** : permet de rendre le champ obligatoire pour que le formulaire puisse être soumis.

  * **Visibilité** : pour permettre une visibilité absolue ou conditionnelle du champ. Les options imbriquées, telles que la visibilité d’un périphérique, apparaissent lorsque certaines options sont cochées.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est possible d’ajouter des blocs de texte dans la colonne de droite de la page du formulaire, à côté du formulaire de ticket. C’est l’endroit idéal pour inclure des informations sur l’équipe, telles que des coordonnées supplémentaires, des heures d’ouverture ou des articles utiles qui renvoient au <b>Forum</b>.</p>
</div> ![Vue du formulaire de site web non publié pour soumettre
un ticket à l'assistance d'Konvergo ERP.](../../../../_images/receiving-tickets-web-
form.png)

Une fois le formulaire optimisé et prêt à être utilisé par le public,
**enregistrez** les changements et publiez le formulaire en cliquant sur le
bouton **Non publié**.

### Live Chat

La fonctionnalité de _Live Chat_ permet aux visiteurs du site web d’être
directement en contact avec un agent d’assistance ou un chatbot. Au cours de
ces conversations, des tickets d” _Assistance_ peuvent être créés
instantanément en utilisant la [commande de
réponse](../../../websites/livechat/responses) `/assistance`.

Pour activer le _Live Chat_ , allez à la vue de liste dans Configuration ‣
Équipes, sélectionnez une équipe et sur la page des paramètres des **Équipes**
, cochez la case à côté de **Live Chat** , sous le titre **Canaux**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si c’est la première fois que le <em>Live Chat</em> est activé dans la base de données, il se peut que la page doive être enregistrée manuellement et actualisée avant toute autre étape.</p>
</div>

Lorsque le paramètre **Live Chat** est activé, cliquez sur **Voir les
canaux**. Ensuite, sur le tableau de bord des **Canaux de live chat du site
web** , sélectionnez la carte kanban du canal qui a été créé pour l’équipe d”
_Assistance_ ou créez-en un **Nouveau** si nécessaire. Lorsqu’une carte kanban
est sélectionnée, d’autres options apparaissent sur le formulaire du canal.

#### Personnaliser le canal de live chat

Lorsque vous cliquez sur un canal individuel sur le tableau de bord des
**Canaux de live chat du site web** , Konvergo ERP redirige la page vers le formulaire
du canal. Vous pouvez y modifier le **Nom du canal** , mais Konvergo ERP le nomme par
défaut pour qu’il corresponde au pipeline de l’équipe d” _Assistance_.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si une équipe d”<em>Assistance</em> s’appelle <code>Service clientèle</code>, un canal de <em>Live Chat</em> sera créé avec le même nom.</p>
<img alt="Vue des cartes kanban pour les canaux de live chat disponibles." class="align-center" src="../../../../_images/receiving-tickets-live-chat-join-channel.png"/>
</div>

Sur le formulaire du canal, naviguez à travers les onglets pour compléter la
configuration.

##### Ajouter des opérateurs

Les _opérateurs_ sont les utilisateurs qui agiront en tant qu’agents et qui
répondront aux demandes de live chat des clients. L’utilisateur qui a
initialement créé le canal de live chat sera ajouté par défaut.

Pour ajouter d’autres utilisateurs, cliquez sur le canal de live chat sur le
tableau de bord des **Canaux de live chat du site web** et dans l’onglet
**Opérateurs** , cliquez sur **AJOUTER**.

Cochez ensuite la case à côté des utilisateurs que vous voulez ajouter et
cliquez sur **SÉLECTIONNER**. Cliquez sur **Nouveau** pour créer et ajouter
des opérateurs à la liste en complétant le formulaire **Créer Opérateurs** et
en cliquant sur **ENREGISTRER & FERMER** (ou sur **ENREGISTRER & NOUVEAU**
pour créer de multiples enregistrements).

De même, les opérateurs actuels peuvent être édités ou supprimés en cliquant
sur les cases respectives dans l’onglet **Opérateurs** et en ajustant leurs
valeurs de formulaire ou en utilisant l’un des boutons situés au bas du
formulaire, tels que **SUPPRIMER**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les utilisateurs peuvent s’ajouter en tant qu’opérateur en cliquant sur le bouton <b>Rejoindre</b> sur un canal de <em>Live Chat</em>.</p>
</div>

##### Modifier les options du canal

L’onglet **Options** contient les paramètres visuels et textuels de la fenêtre
de live chat.

Modifiez le texte dans le champ **Texte du bouton** pour mettre à jour le
message d’accueil affiché dans la bulle de texte lorsque le bouton de live
chat apparaît sur le site web.

Modifiez le **Message d’accueil** pour modifier le message qu’un visiteur voit
lorsqu’il ouvre la fenêtre de discussion. Ce message donnera l’impression
d’être envoyé par un opérateur de live chat et devrait encourager le visiteur
à poursuivre la conversation.

Modifiez le **Placeholder de l’entrée de conversation** pour changer le texte
qui apparaît dans la case où les visiteurs saisiront leurs réponses.

Modifiez la **Couleur du bouton de Live Chat** et la **Couleur de l’en-tête du
canal** en cliquant sur une bulle de couleur pour ouvrir la fenêtre de
sélection des couleurs. Cliquez sur l’icône de réinitialisation à droite des
bulles de couleur pour rétablir les couleurs par défaut.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les couleurs du bouton ou de l’en-tête peuvent être sélectionnées manuellement ou par les valeurs RGB, HSL ou HEX. Différents options sont disponibles, en fonction de votre système d’exploitation.</p>
</div>

##### Créer des règles de canal

L’onglet **Règles de canal** détermine quand la fenêtre de live chat s’ouvre
sur le site web en fonction de la logique de déclenchement d’une action **URL
Regex** (par ex. la visite d’une page).

Modifiez des règles existantes ou créez-en une nouvelle en cliquant sur
**Ajouter une ligne** et complétez les détails du formulaire qui apparaît en
fonction de la manière dont la règle doit s’appliquer.

Si un **Chatbot** est prévu sur ce canal, sélectionnez-le dans le menu
déroulant. Si le chatbot sera uniquement actif lorsqu’aucun opérateur n’est
disponible, cochez la case intitulée **Activé uniquement s’il n’y a aucun
opérateur**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un chatbot est ajouté au canal de live chat, 3 nouveaux boutons intelligents apparaissent sur le formulaire des paramètres du canal : <b>Chatbots</b>, <b>Sessions</b>, et <b>% content</b>.</p>
<ul>
<li><p>Le bouton intelligent <b>Chatbots</b> permet de programmer le chatbot avec un <b>Script</b>. Chaque ligne du <b>Script</b> contient un <b>Message</b>, un <b>Type d’étape</b>, des <b>Réponses</b> et une logique conditionnelle <b>Seulement si</b> qui s’applique lorsque certaines réponses prédéfinies sont choisies. Pour créer d’autres étapes dans le <b>Script</b>, cliquez sur <b>Ajouter une ligne</b> et complétez les étapes du script en fonction de la logique souhaitée.</p></li>
<li><p><b>Sessions</b> vous permet d’enregistrement les sessions de live chat par ordre décroissant de la <b>Date de la sesssion</b> par défaut. Chaque enregistrement contient les <b>Participants</b> impliqués dans la session de live chat, le <b># de messages</b> et l”<b>Évaluation</b> reçue à la fin de la session.</p></li>
<li><p>Le bouton intelligent <b>% contient</b> comprend un journal d’évaluations laissées par les participants au live chat et libellées par date, heure et l’agent d’assistance responsable de la session de live chat.</p></li>
</ul>
</div>

Ajoutez l’URL des pages auxquelles ce canal sera appliqué dans le champ **URL
Regex**. Si ce canal n’est accessible qu’aux utilisateurs d’un pays
spécifique, ajoutez-les dans le champ **Pays**. Si ce champ est vide, le canal
sera accessible à tous les visiteurs du site web.

![Vue des cartes kanban pour les canaux de live chat
disponibles.](../../../../_images/receiving-tickets-channel-rules.png)

##### Utiliser le widget de live chat

L’onglet **Widget** sur le formulaire du canal de live chat offre un widget de
site web incorporable ou un code court pour donner directement accès au
client/fournisseur à la fenêtre de live chat.

Le **Widget** de live chat peut s’appliquer aux sites web créés par Konvergo ERP en
allant à Site web ‣ Configuration ‣ Paramètres. Descendez jusqu’à la section
**Live Chat** et sélectionnez le canal à ajouter au site. Cliquez sur
**Saugarder** pour appliquer.

Pour ajouter le widget à un site web créé sur une plateforme externe, cliquez
sur **COPIER** et collez le code la balise `<head>` sur le site.

De même, pour envoyer une session de live chat à un client ou un fournisseur,
cliquez sur le deuxième bouton **COPIER** qui contient un lien permettant de
participer directement.

#### Créer un ticket d’assistance à partir d’une session de live chat

Une fois le live chat activé, les opérations pourront communiquer en temps
réel avec les visiteurs du site web.

Pendant la conversation, un opérateur peut demander le raccourci
[commande](../../../websites/livechat/responses) `/assistance` pour créer
un ticket sans quitter la fenêtre de discussion. La transcription de la
conversation sera ajoutée au nouveau ticket dans l’onglet **Description**.

## Prioriser les tickets

Tous les tickets contiennent un champ **Priorité**. Les tickets les plus
prioritaires apparaissent en haut des vues kanban et liste.

![Vue kanban d'une équipe et des tâches prioritaires dans Konvergo ERP
Assistance.](../../../../_images/receiving-tickets-priority.png)

Les niveaux de priorité sont représentés par des étoiles :

>   * 0 étoile = _Priorité faible_
>
>   * 1 étoile = _Priorité moyenne_
>
>   * 2 étoiles = _Priorité élevée_
>
>   * 3 étoiles = _Urgent_
>
>

Par défaut, les tickets ont un niveau de priorité faible (0 étoile). Pour
modifier le niveau de priorité, sélectionnez le nombre d’étoiles approprié sur
la carte kanban ou sur le ticket.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Comme les niveaux de priorité peuvent être utilisés comme critères d’attribution des <a href="sla">Accords de niveau d’assistance</a>, le fait de modifier le niveau de priorité d’un ticket peut modifier le délai de <abbr title="Accord de niveau de service">SLA</abbr>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les étapes de configuration susmentionnées s’appliquent aux bases de données <b>Konvergo ERP Online</b> et <b>Konvergo ERP.sh</b>. Pour les bases de données <b>On-premise</b>, il est possible qu’une configuration supplémentaire des serveurs de messagerie personnalisés et des alias de messagerie soit demandée.</p>
</div>0

