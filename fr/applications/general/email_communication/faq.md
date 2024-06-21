# Problèmes d’email

Ce document vise à expliquer les problèmes d’email les plus récurrents dans
Konvergo ERP.

## Emails sortants

### L’email n’est pas envoyé

Le premier indicateur montrant qu’un email n’a pas été envoyé est la présence
d’une enveloppe rouge **✉️** dans le chatter à côté de la date et de l’heure
du message.

![Icône d'enveloppe rouge affichée dans le chatter.](../../../_images/red-
envelop.png)

Les emails non envoyés apparaissent également dans la file d’attente des
emails d’Konvergo ERP. Avec le [mode développeur](../developer_mode#developer-
mode) activé, la file d’attente des emails est accessible en allant à
l’application Paramètres ‣ menu Technique ‣ Email ‣ Emails. Les emails non
envoyés apparaissent en turquoise, tandis que les emails envoyés apparaissent
en gris.

#### Messages d’erreur fréquents

##### Limite journalière atteinte

![Avertissement dans Konvergo ERP lorsque la limite d'emails est
atteinte.](../../../_images/email-limit.png)

Chaque fournisseur de services de messagerie a ses propres limites d’envoi
d’emails. Les limites peuvent être fixées par jour, par heure ou parfois par
minute. C’est la même chose pour Konvergo ERP. Nous devons limiter le nombre d’emails
envoyés par nos clients pour éviter que les serveurs de messagerie d’Konvergo ERP ne
soient mis sur liste noire.

Voici les limites par défaut des nouvelles bases de données :

  * **200 emails par jour** pour les bases de données Konvergo ERP Online et Konvergo ERP.sh avec un abonnement actif.

  * **20 emails par jour** pour les bases de données à Une application gratuite.

  * **50 emails par jour** pour les bases de données d’essai.

  * Dans le cas d’une migration, la limite journalière peut être réinitialisée à 50 emails par jour.

Si la limite journalière est atteinte :

  * Contactez l’équipe d’assistance d’Konvergo ERP, qui peut augmenter la limite journalière en fonction des critères suivants :

    1. Combien d’utilisateurs y a-t-il dans la base de données ?

    2. Quelles sont les applications installées ?

    3. Le taux de rebond : le pourcentage d’adresses email qui n’ont pas reçu les emails parce qu’ils ont été renvoyés par un serveur de messagerie lors de son acheminement vers le destinataire final.

  * Utilisez un serveur de messagerie sortant externe pour ne pas dépendre de la limite journalière d’Konvergo ERP (référez-vous à la [documentation relative aux emails](email_servers)).

  * Attendez jusqu’à 23:00 PM (UTC) pour que la limite journalière soit réinitialisée et essayez de renvoyer l’email. Avec le [mode développeur](../developer_mode#developer-mode) activé, allez à l’application Paramètres ‣ menu Technique ‣ Email ‣ Emails et cliquez sur le bouton **Réessayer** à côté d’un email non envoyé.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>La limite journalière des emails est exhaustive pour la base de données. Par défaut, tout message interne, notification, note, etc. compte comme un email dans la limite journalière si une personne est notifiée par email. Vous pouvez changer cela en choisissant de recevoir des <a href="../../productivity/discuss#discuss-app-notification-preferences"><span class="std std-ref">notifications dans Konvergo ERP</span></a>, au lieu d’emails.</p>
</div>

##### Erreur SMTP

Les messages d’erreur Simple Mail Transport Protocol (SMTP) expliquent
pourquoi un email n’a pas été envoyé avec succès. SMTP est un protocole
permettant de décrire la structure de l’email et transmet les données des
messages sur Internet. Les messages d’erreur générés par les services de
messagerie sont utiles pour diagnostiquer et dépanner les problèmes d’email.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Voici un exemple d’erreur de livraison permanente SMTP 554 : <code>554 : erreur de livraison : Désolé, votre message à ------@yahoo.com ne peut pas être délivré. Cette boîte de messagerie est désactivée (554.30). - mta4471.mail.bf1.yahoo.com --- Sous cette ligne se trouve une copie du message.</code></p>
</div>

Le menu de débogage peut être utilisé pour étudier les problèmes d’envoi SMTP
à partir d’une base de données. Pour accéder au menu, le [mode
développeur](../developer_mode#developer-mode) doit être activé. Une fois
activé, allez au Menu de débogage dans le coin supérieur droit de la barre de
menu (l’icône **🐞 (insecte)**), Menu de débogage ‣ Gérer les messages

Le menu **Gérer les messages** ouvre une liste de tous les messages envoyés
dans un enregistrement en particulier. Chaque message contient des
informations relatives à l’envoi, y compris le type et le sous-type du
message.

Vous y trouvez aussi à qui le message a été envoyé et si Konvergo ERP a reçu un
message de rebond de la part d’un serveur de messagerie.

![Option de menu Gérer les messages dans le menu de
débogage.](../../../_images/manage-messages.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Un utilisateur doit être sur une vue dans Konvergo ERP qui a un chatter pour que l’option <b>Gérer les messages</b> apparaisse.</p>
</div>

###### Pas d’informations sur l’erreur

Konvergo ERP n’est pas toujours en mesure de fournir des informations sur la raison de
l’échec de l’envoi. Les différents fournisseurs de messagerie mettent en œuvre
une politique personnalisée des emails de rebond et il n’est pas toujours
possible pour Konvergo ERP de l’interpréter correctement.

S’il s’agit d’un problème récurrent avec le même client ou le même domaine,
n’hésitez pas à contacter l”[assistance d’Konvergo ERP](https://www.odoo.com/help) qui
pourra vous aider à trouver une solution.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’une des raisons les plus courantes pour lesquelles il n’y a aucun message d’erreur lors de l’échec d’envoi d’un email est liée à la configuration de <a href="email_domain#email-communication-spf-compliant"><span class="std std-ref">SPF</span></a> et/ou de <a href="email_domain#email-communication-dkim-compliant"><span class="std std-ref">DKIM</span></a>. Vérifiez également que l’alias <code>mail.bounce.alias</code> est défini dans les <em>paramètres système</em>. Accédez aux paramètres système avec le <a href="../developer_mode#developer-mode"><span class="std std-ref">:mode développeur</span></a> activé en allant à l’application Paramètres ‣ menu Technique ‣ Paramètres ‣ Paramètres système.</p>
</div>

### L’email est envoyé en retard

Les campagnes d’email sont envoyées à une heure programmée, en utilisant un
délai préprogrammé dans la base de données. Konvergo ERP utilise une tâche retardée
pour envoyer des emails qui sont considérés comme « non urgents » (formats de
newsletter, tels que : mass mailing, marketing automation, et événements). Le
programme utilisateur **cron** peut être utilisé pour prévoir des programmes à
exécuter automatiquement à des intervalles prédéterminés. Konvergo ERP utilise cette
politique pour ne pas encombrer les serveurs de messagerie et de donner la
priorité à la communication individuelle. Ce **cron** s’intitule **Email :
Gestionnaire de la file d’attente des emails** et est accessible en allant à
l’application Paramètres ‣ menu Technique ‣ Automatisation ‣ Actions
planifiées avec le [mode développeur](../developer_mode#developer-mode)
activé.

![Email planifié pour être envoyé plus tard. ](../../../_images/email-
scheduled-later.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Qu’est-ce qu’un <b>cron</b> ? Un cron est une action qu’Konvergo ERP exécute en arrière-plan pour exécuter un code particulier et exécuter une tâche.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Par défaut, le <em>cron d’envoi en masse</em> s’exécute toutes les 60 minutes. Il est possible de le modifier pour qu’il s’exécute au minimum toutes les 5 minutes. Toutefois, l’exécution de l’action toutes les 5 minutes risque d’alourdir la base de données Konvergo ERP (charger le système), ce qui n’est pas recommandé. Pour modifier le cron d’envoi en masse, sélectionnez l’action planifiée <b>Email : Gestionnaire de la file d’attente des emails</b> et procédez aux ajustements nécessaires.</p>
</div>

Les emails considérés comme urgents (communication d’une personne à une autre,
telle que les commandes clients, les factures, les bons d’achat, etc.) sont
envoyés immédiatement.

## Emails entrants

Lorsque vous rencontrez un problème avec les emails entrants, il n’y a pas
forcément une indication dans Konvergo ERP. C’est le client qui tente de contacter une
base de données qui recevra un message de rebond (la plupart du temps un
message d’erreur **550 : boîte de messagerie indisponible**).

### L’email n’est pas reçu

Les mesures à prendre dépendent de la plateforme d’Konvergo ERP qui héberge la base de
données.

Les utilisateurs **Konvergo ERP.sh** peuvent trouver leurs journaux en direct dans le
dossier `~/logs/`.

Les journaux sont une collection stockée de toutes les tâches effectuées dans
une base de données. Il s’agit d’une représentation en texte seul, avec
l’horodatage de chaque action effectuée sur la base de données Konvergo ERP. Cela peut
être utile pour suivre les emails qui quittent la base de données. Vous pouvez
également observer les échecs d’envoi dans les journaux qui indiquent qu’on a
essayé d’envoyer le message à plusieurs reprises. Les journaux indiquent
toutes les actions effectuées sur les serveurs de messagerie à partir de la
base de données.

Le dossier `~/logs/` (accessible par la ligne de commande ou sur le tableau de
bord Konvergo ERP.sh) d’une base de données Konvergo ERP.sh contient une liste de fichiers
contenant les journaux de la base de données. Les fichiers de journaux sont
créés tous les jours à 05:00 (UTC).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les deux jours les plus récents (aujourd’hui et hier) ne sont pas comprimés, tandis que les plus anciens le sont afin d’économiser de l’espace. Les fichiers d’aujourd’hui et d’hier s’intitulent respectivement : <code>odoo.log</code> et <code>odoo.log.1</code>.</p>
<p>Pour les jours suivants, ils sont nommés avec leurs dates et ensuite comprimés. Utilisez les commandes <b class="command o_code">grep</b> et <b class="command o_code">zgrep</b> (pour les fichiers comprimés) pour parcourir les fichiers.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour plus d’informations sur les journaux et la façon d’y accéder via le tableau de bord Konvergo ERP.sh, consultez <a href="../../../administration/odoo_sh/getting_started/branches#odoosh-logs"><span class="std std-ref">cette documentation d’administration</span></a>.</p>
<p>Pour plus d’informations sur la façon d’accéder aux journaux via la ligne de commande, consultez <a href="../../../developer/reference/cli#reference-cmdline-server-logging"><span class="std std-ref">cette documentation développeur</span></a>.</p>
</div>

Les utilisateurs d”**Konvergo ERP Online** n’ont pas accès aux journaux. Toutefois,
vous pouvez contacter l”[Assistance d’Konvergo ERP](https://www.odoo.com/help) si vous
avez un problème récurrent avec le même client ou le même domaine.

## Obtenir de l’aide de l’assistance Konvergo ERP

Afin d’être aidé efficacement, veuillez fournir autant d’informations que
possible. Voici une liste de ce qui peut être utile lorsque vous contactez
l’équipe d’assistance Konvergo ERP à propos d’un problème :

  1. Envoyez une copie des en-têtes de l’email. Le fichier `.EML` file (ou **en-têtes**) de l’email est le format de fichier qui contient toutes les informations techniques requises pour une enquête. La documentation du fournisseur de messagerie vous expliquera comment accéder au fichier EML/aux fichiers d’en-tête. Une fois les en-têtes de l’email obtenus, ajoutez-les au ticket d’assistance Konvergo ERP pour que l’équipe d’assistance Konvergo ERP puisse enquêter de manière efficace.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://support.google.com/mail/answer/29436">Documentation de Gmail sur les en-têtes</a></p></li>
<li><p><a href="https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c#tab=Web">Documentation d’Outlook sur les en-têtes</a></p></li>
</ul>
</div>

  2. Expliquez le flux exact que vous suivez pour normalement recevoir ces emails dans Konvergo ERP. Voici des exemples de questions dont les réponses peuvent être utiles :

     * S’agit-il d’une notification d’une réponse reçue dans Konvergo ERP ?

     * S’agit-il d’un message envoyé depuis la base de données Konvergo ERP ?

     * Un serveur de messagerie entrant est-il utilisé ou l’email est-il redirigé d’une manière ou d’une autre ?

     * Avez-vous un exemple d’un email qui a été transféré correctement ?

  3. Répondez aux questions suivantes :

     * S’agit-il d’un problème générique ou est-il spécifique à un cas d’utilisation ? Si oui, lequel exactement ?

     * Est-ce que cela fonctionne comme prévu ? Si l’email est envoyé par le biais d’Konvergo ERP, l’email de rebond devrait atteindre la base de données Konvergo ERP et afficher l”enveloppe rouge.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le paramètre système de rebond doit être défini dans les paramètres techniques pour que la base de données reçoive correctement les messages de rebond. Pour accéder à ce paramètre, allez à l’application Paramètres ‣ menu Technique ‣ Paramètres ‣ Paramètres système. Sélectionnez ensuite le nom de paramètre <b>mail.bounce.alias</b> et définissez la valeur sur <code>bounce</code> si elle n’est pas encore définie.</p>
</div>

  *[SMTP]: Simple Mail Transport Protocol

