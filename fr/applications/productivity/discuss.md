# Discussion

Konvergo ERP _Discussion_ est une application de communication interne qui permet aux
utilisateurs de discuter par le biais de messages, de notes et de partage de
fichiers, soit par le biais d’une fenêtre de chat persistante qui fonctionne à
travers les applications, soit par le biais du tableau de bord de
_Discussion_.

## Choisir vos préférences de notification

Accédez aux préférences spécifiques aux utilisateurs de l’application
_Discussion_ en allant à l’application Paramètres ‣ Utilisateurs ‣ Utilisateur
‣ onglet Préférences.

![Vue de l'onglet des préférences pour Konvergo ERP
Discussion.](../../_images/preferences-user.png)

Le champ **Notification** est défini par défaut sur **Recevoir par email**. Si
ce paramètre est activé, un email de notification sera envoyé par Konvergo ERP chaque
fois qu’un message est envoyé depuis le chatter, qu’une note est envoyée avec
une mention `@` (depuis le chatter), ou qu’une notification est envoyée pour
un enregistrement suivi par l’utilisateur. Le changement d’étape (si un email
est configuré pour être envoyé, par exemple, lorsque la tâche est définie sur
**Fait**) déclenche l’envoi d’une notification.

Si vous choisissez **Recevoir dans Konvergo ERP** , les notifications susmentionnées
s’affichent dans la _boîte de messagerie_ de l’application _Discussion_. Les
messages peuvent faire l’objet des actions suivantes : répondre avec un émoji
en ciliquant sur **Ajouter une réaction** , ou répondre au message en cliquant
sur **Répondre**. D’autres actions sont possibles : marquer le message d’un
astérisque en cliquant sur **Marqué comme à faire** , ou épingler le message
en cliquant sur **Épingler** ou même marquer le message comme non lu en
cliquant sur **Marqué comme non lu**.

![Vue d'un message de la boîte de réception et ses options d'action dans Konvergo ERP
Discussion.](../../_images/reactions-discuss.png)

Le fait de cliquer sur **Marquer comme à faire** sur un message le fait
apparaître sur la page des **Favoris** , tandis que le fait de cliquer sur
**Marquer comme lu** déplace le message dans l”**Historique**.

![Vue des messages marqués comme à faire dans Konvergo ERP
Discussion.](../../_images/starred-messages.png)

## Commencer à discuter

La première fois qu’un utilisateur se connecte à son compte, Konvergo ERPBot envoie un
message demandant la permission d’envoyer des notifications de bureau pour les
chats. S’il accepte, l’utilisateur recevra des notifications push sur son
bureau pour les messages qu’il reçoit, quel que soit l’endroit où il se trouve
dans Konvergo ERP.

![Vue des messages sous le menu de messagerie soulignant la demande des
notifications push pour Konvergo ERP Discussion.](../../_images/odoobot-push.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour arrêter de recevoir des notifications sur le bureau, réinitialisez les paramètres des notifications du navigateur.</p>
</div>

Pour démarrer une discussion, allez à l’application Discussion et cliquez sur
l’icône **\+ (plus)** à côté de **Messages directs** ou **Canaux** dans le
menu gauche du tableau de bord.

![Vue du panneau de Discussion mettant en évidence les titres, les canaux et
les messages directs dans Konvergo ERP Discussion.](../../_images/channels-direct-
messages.png)

A company can also easily create [public and private
channels](discuss/team_communication).

### Mentions dans le chat et le chatter

Pour mentionner un utilisateur dans un chat ou le chatter, tapez `@nom-
utilisateur` ; pour faire référence à un canal, tapez `#nom-canal`.
L’utilisateur mentionné sera notifié dans sa _boîte de messagerie_ ou par
email, en fonction de ses paramètres de communication.

![Vue de quelques fenêtres de chat dans Konvergo ERP Discussion.](../../_images/chat-
windows.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Lorsqu’un utilisateur est mentionné, la liste de recherche (liste de noms) suggère des valeurs d’abord basées sur les abonnés de la tâche, puis sur employés. Si l’enregistrement recherché ne correspond ni à un abonné ni à un employé, l’étendue de la recherche passe à tous les partenaires.</p>
</div>

### Statut de l’utilisateur

Il est utile de savoir ce que font les collègues et dans quelle mesure ils
peuvent répondre aux messages en vérifiant leur _statut_. Le statut est
affiché à gauche du nom d’un contact dans la barre latérale de **Discussion**
, dans le _menu de messagerie_ et dans le _chatter_.

  * Vert = en ligne

  * Orange = absent

  * Blanc = hors ligne

  * Avion = hors du bureau

![Vue du statut des contacts dans Konvergo ERP Discussion.](../../_images/status.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="discuss/team_communication">Utiliser les canaux pour la communication d’équipe</a></p></li>
<li><p><a href="../essentials/activities">Activités</a></p></li>
</ul>
</div>

  * [Utiliser les canaux pour la communication d’équipe](discuss/team_communication)
  * [Configurer des serveurs ICE avec Twilio](discuss/ice_servers)

