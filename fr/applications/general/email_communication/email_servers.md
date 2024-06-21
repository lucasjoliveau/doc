# Envoyer et recevoir des emails dans Konvergo ERP avec un serveur de messagerie

## Utilisateurs d’Konvergo ERP Online ou d’Konvergo ERP.sh

Puisque **Konvergo ERP configure ses propres serveurs de messagerie pour la base de
données** , les emails entrants et sortants fonctionnent déjà d’emblée. Donc,
pour les clients de **Konvergo ERP Online** et **Konvergo ERP.sh** , il n’y a rien à faire !

À moins qu’un serveur de messagerie externe ne soit nécessaire pour effectuer
des envois de masse, il suffit d’utiliser normalement la base de données Konvergo ERP
Online standard puisqu’elle a déjà été préconfigurée pour envoyer des emails.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le serveur Konvergo ERP est soumis à une limite quotidienne d’emails pour prévenir les abus. La limite par défaut est de 200 emails envoyés par jour avec un abonnement <b>Enterprise</b>. Cette limite peut être augmentée sous certaines conditions. Consultez notre <a href="faq">FAQ</a> ou contactez l’assistance pour plus d’informations.</p>
</div>

## Le but de cette documentation

This document is **mainly dedicated to Konvergo ERP on-premise databases** that do not
benefit from an out-of-the-box solution to send and receive emails in Konvergo ERP,
unlike [Konvergo ERP Online](https://www.odoo.com/trial) and
[Konvergo ERP.sh](https://www.odoo.sh). Incoming and outgoing servers must be
configured for on-premise databases.

Les sections suivantes contiennent des informations sur comment intégrer un
serveur de messagerie externe à Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si personne dans l’entreprise n’est engagée pour gérer les serveurs de messagerie, nous vous recommandons fortement de choisir Konvergo ERP Online et Konvergo ERP.sh. L’envoi d’emails de ces types d’hébergement d’Konvergo ERP fonctionne instantanément et est surveillé par des professionnels. Néanmoins, si une société souhaite gérer elle-même la réparation du serveur de messagerie, elle peut utiliser son propre serveur de messagerie. Pour plus d’informations, consultez <a href="email_domain">Configurer des enregistrements DNS pour envoyer des emails dans Konvergo ERP</a></p>
</div>

## Notifications par défaut

Les documents dans Konvergo ERP (comme une opportunité CRM, un bon de commande, une
facture, etc.) ont un fil de discussion, appelé _chatter_.

Lorsqu’un utilisateur de la base de données publie un message dans le chatter,
ce message est envoyé par email aux abonnés du document en tant que
notification (à l’exception de l’expéditeur). Si un abonné répond au message,
la réponse met le chatter à jour et Konvergo ERP relaie une autre réponse aux abonnés
en tant que notification. Les messages renvoyés au chatter par des
utilisateurs ou des utilisateurs externes apparaîtront dans le chatter à
partir de leur adresse email respective ou sous le nom enregistré dans leur
fiche _Contacts_.

Ces notifications sont envoyées à l’aide d’une adresse d’origine par défaut.
Pour plus d’informations, consultez Utiliser une adresse email par défaut.

## Comment gérer les messages sortants

As a system administrator, go to Settings ‣ General Settings ‣ Discuss in
Konvergo ERP, and enable the **Custom Email Servers** option. Then, click **Save**.
Next, click **Outgoing Email Servers** and click **Create** to create a new
outgoing mail server record in Konvergo ERP. Reference the SMTP data of the external
email server. Once all the information has been filled out, click **Test
Connection**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="google_oauth">Connecter Gmail à Konvergo ERP en utilisant Google OAuth</a></p></li>
<li><p><a href="azure_oauth">Connecter Microsoft Outlook 365 à Konvergo ERP avec Azure OAuth</a></p></li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>S’assurer que le domaine sortant a un <abbr title="Sender Policy Framework">SPF</abbr>, <abbr title="DomainKeys Identified Mail">DKIM</abbr> et <abbr title="Domain-based Message Authentication, Reporting, &amp; Conformance">DMARC</abbr> configurés sur le <abbr title="Domain Name System">DNS</abbr> améliorera la délivrabilité. Pour plus d’informations, consultez <a href="email_domain">Configurer les enregistrements DNS pour envoyer des emails dans Konvergo ERP</a>.</p>
</div>

### Restriction de port

Notez que le port 25 est bloqué pour des raisons de sécurité sur les
plateformes Konvergo ERP Online et Konvergo ERP.sh. Essayez plutôt d’utiliser les ports 465,
587 ou 2525.

### Utiliser une adresse email « De » par défaut

Parfois, l’adresse (sortante) « De » d’un email peut appartenir à un domaine
différent, ce qui peut poser problème.

Par exemple, si un client avec l’adresse email `mary@customer.example.com`
répond à un message, Konvergo ERP tentera de redistribuer le même email aux autres
abonnés du fil. Cependant, si le domaine `customer.example.com` interdit ce
type d’utilisation pour des raisons de sécurité, l’email que Konvergo ERP tente de
redistribuer sera rejeté par les serveurs de messagerie de certains
destinataires.

Pour éviter ce genre de problèmes, Konvergo ERP envoie tous les emails en utilisant
une adresse « De » du même domaine autorisé.

Accédez aux **Paramètres système** en activant le [mode
développeur](../developer_mode#developer-mode) et allez au menu
Paramètres ‣ Technique ‣ Paramètres ‣ Paramètres système.

Pour forcer l’adresse email à partir de laquelle les emails sont envoyés, vous
devez définir une combinaison des clés suivantes dans les paramètres système
de la base de données :

  * `mail.default.from`: accepte la partie locale ou une adresse email complète comme valeur

  * `mail.default.from_filter`: accepte un nom de domaine ou une adresse email complète comme valeur

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le <code>mail.default.from_filter</code> fonctionne uniquement pour des configurations <code>odoo-bin</code> ou le serveur de messagerie d’Konvergo ERP par défaut, sinon ce paramètre peut être défini en utilisant le champ <code>from_filter</code> sur <code>ir.mail_server</code>.</p>
</div>

Le champ peut être un nom de domaine ou une adresse email complète ou il peut
rester vide. Si l’adresse email de l’expéditeur ne correspond pas à ce filtre
défini, l’email sera encapsulé par les deux paramètres système :
`mail.default.from` et `mail.catchall.domain`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Dans l’exemple suivant, l’adresse email d’origine est remplacée par la combinaison des deux paramètres système (<code>mail.default.from</code> et <code>mail.catchall.domain</code>). Il s’agit de la configuration de notification par défaut dans Konvergo ERP : <code>“Admin” &lt;admin@example.com&gt;</code> =&gt; <code>“Admin” &lt;notifications@mycompany.com&gt;</code>.</p>
</div>

En d’autres termes, si l’adresse email de l’auteur ne correspond pas à
`mail.default.from_filter`, l’adresse email est remplacée par
`mail.default.from` (si elle contient une adresse email complète) ou une
combinaison de `mail.default.from` et `mail.catchall.domain`.

Si le `from_filter` contient une adresse email complète et si le
`mail.default.from` est identique à cette adresse, toutes les adresses email
différentes de `mail.default.from` seront encapsulées dans
`mail.default.from`.

### Utiliser le filtre « De » sur un serveur de messagerie sortant

Le champ **Filtrage DE** permet d’utiliser un serveur de messagerie sortant
spécifique en fonction de l’adresse email **De** ou du domaine pour lequel
Konvergo ERP effectue l’envoi. Ce paramètre peut être utilisé pour améliorer la
délivrabilité ou le taux de réussite de l’envoi des emails à partir de la base
de données. Le paramétrage du champ **Filtrage DE** peut également être
utilisé pour envoyer à partir de domaines différents dans un environnement
multi-sociétés. Accédez à ce champ dans Konvergo ERP en allant aux Paramètres ‣
Discussion ‣ Serveurs de messagerie personnalisés ‣ Serveurs de messagerie
sortants ‣ Nouveau.

![Paramètres du serveur de messagerie sortant et les paramètres du filtrage
DE.](../../../_images/from-filter-setting.png)

Lorsqu’un email est envoyé depuis Konvergo ERP lorsque le champ **Filtrage DE** est
défini, un serveur de messagerie est sélectionné dans l’ordre suivant :

  1. Tout d’abord, Konvergo ERP recherche un serveur de messagerie qui a la même valeur du **Filtrage DE** que la valeur **De** (adresse mail) définie dans l’email sortant. Par exemple, si la valeur **De** (adresse mail) est `test@example.com`, seuls les serveurs de messagerie dont la valeur **Filtrage DE** est égale à `test@example.com` sont renvoyés.

  2. Toutefois, si aucun serveur de messagerie n’utilise la valeur **De** , Konvergo ERP recherche un serveur de messagerie qui a le même _domaine_ que la valeur **De** (adresse mail) définie dans l’email sortant. Par exemple, si l’adresse email **De** est `test@example.com`, seuls les serveurs de messagerie dont la valeur **Filtrage DE** est égale à `example.com` sont renvoyés.

Si aucun serveur de messagerie n’est trouvé après avoir vérifié le domaine,
Konvergo ERP renvoie tous les serveurs de messagerie qui n’ont aucune valeur
**Filtrage DE** définie.

Si cette requête ne renvoie aucun résultat, Konvergo ERP effectue une recherche de
serveur de messagerie à l’aide du paramètre système: `mail.default.from`. Tout
d’abord, l’adresse email indiquée tente de trouver un serveur de messagerie,
puis le domaine tente de trouver une correspondance. Si aucun serveur de
messagerie n’est trouvé, Konvergo ERP renvoie le premier serveur de messagerie sortant
(trié par priorité).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si Konvergo ERP trouve plusieurs serveurs de messagerie, il utilise le premier en fonction de sa priorité. S’il trouve deux serveurs de messagerie, l’un avec une priorité de <code>10</code> et l’autre avec une priorité de <code>20</code>, le serveur de messagerie avec une priorité de <code>10</code> est utilisé en premier.</p>
</div>

### Configurer différents serveurs dédiés pour les emails transactionnels et
les envois de masse

In Konvergo ERP a separate email server can be used for transactional emails and mass
mailings. Example: Use Postmark or SendinBlue for transactional emails, and
Amazon SES, Mailgun, Sendgrid or [Mailjet](mailjet_api) for mass
mailings.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Un serveur de messagerie sortant par défaut est déjà configuré. Vous ne devez pas créer une alternative, sauf si un serveur de messagerie sortant externe spécifique est requis pour des raisons techniques.</p>
</div>

Pour ce faire, activez d’abord le mode développeur `, et allez ensuite aux
:menuselection:`Paramètres –> Technique –> Serveurs de messagerie sortants.
Créez-y deux paramètres de serveur de messagerie sortant ; un pour les emails
transactionnels et un autre pour le serveur d’envois de massa. Assurez-vous de
donner la priorité au serveur transactionnel par rapport au serveur d’envois
de masse en donnant une priorité plus faible au serveur des emails
transactionnels.

À présent, allez à Email Marketing ‣ Paramètres et activez **Serveur dédié**.
Choisissez le serveur de messagerie approprié. Avec ces paramètres, Konvergo ERP
utilise le serveur avec la plus faible priorité pour les emails
transactionnels et le serveur sélectionné ici pour les envois de masse. Notez
que dans ce cas, les enregistrements Sender Policy Framework (SPF) du domaine
doivent être configurés pour inclure les serveurs d’emails transactionnels et
d’envois de masse.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="email_domain">Configurer les enregistrements DNS pour envoyer des emails dans Konvergo ERP</a></p></li>
</ul>
</div>

## Comment gérer les messages entrants

Konvergo ERP s’appuie sur des alias email pour récupérer des messages entrants.

  * **Reply messages** of messages sent from Konvergo ERP are routed to their original discussion thread (and to the inbox of all its followers) by the alias of the model if there is any or by the catchall alias (**catchall@**). Replies to messages of models that do not have a custom alias will use the catchall alias (`catchall@mycompany.odoo.com`). The catchall address, however, does not have another action attached to it like other aliases might, it is only used to collect replies.

  * Les **messages rejetés** sont utilisés comme Return-Path. Un exemple particulièrement utile est celui d”[Konvergo ERP Email Marketing](https://www.odoo.com/page/email-marketing). Dans ce cas, la désinscription est basée sur le fait que l’email a été rejeté trop de fois (5) au cours du dernier mois et que les rejets sont espacés d’une semaine. Cela permet d’éviter de mettre quelqu’un sur liste noire à cause d’une erreur du serveur de messagerie. Si ces circonstances sont réunies, l’email est considéré comme invalide et est inscrit sur liste noire. Une note est ajoutée sur le contact sous **Adresses email sur liste noire** dans le **menu de configuration d’Email Marketing**.

Les messages qui sont rejetés dans le chatter (en dehors d’Email Marketing)
sont accompagnés d’une enveloppe rouge indiquant l’échec de la livraison. Cela
peut être utile pour savoir qu’un bon de commande ou une facture n’a pas
atteint sa destination finale.

  * **Messages originaux** : plusieurs objets professionnels ont leur propre alias pour créer de nouveaux enregistrements dans Konvergo ERP à partir des emails entrants :

>     * Canal de ventes (pour créer des _pistes_ ou des _opportunités_ dans
> [Konvergo ERP CRM](https://www.odoo.com/page/crm))
>
>     * Canal d’assistance (pour créer des _tickets_ dans [Konvergo ERP
> Assistance](https://www.odoo.com/page/helpdesk))
>
>     * Projets (pour créer de nouvelles _tâches_ dans [Konvergo ERP
> Projet](https://www.odoo.com/page/project-management))
>
>     * Vacatures (pour créer des _candidats_ dans [Konvergo ERP
> Recrutement](https://www.odoo.com/page/recruitment))

Selon votre serveur de messagerie, il peut y avoir plusieurs façons de
récupérer des emails. La méthode la plus facile et la plus recommandée
consiste à gérer une adresse email par alias Konvergo ERP dans le serveur de
messagerie.

  * Créez les adresses email correspondantes dans le serveur de messagerie (**catchall@** , **bounce@** , **sales@** , etc.).

  * Définissez le nom de l”**Alias de domaine** dans Paramètres ‣ Paramètres généraux ‣ Discussion. Le fait de modifier l”**Alias de domaine** modifiera le domaine de catchall pour la base de données.

  * Si vous utilisez Konvergo ERP sur serveur, créez un **Serveur de messagerie entrant** dans Konvergo ERP pour chaque alias. Pour créer un nouveau serveur entrant, allez à : Paramètres ‣ Discussion ‣ Serveurs de messagerie personnalisés ‣ Serveurs de messagerie entrants ‣ Nouveau. Complétez le formulaire selon les paramètres de votre fournisseur de messagerie. Laissez le champ **Actions à effectuer à l’arrivée des emails** vide. Une fois toutes les informations complétées, cliquez sur **TESTER & CONFIRMER**.

![Configuration du serveur de messagerie entrant dans
Konvergo ERP.](../../../_images/incoming-server.png)

  * Si vous utilisez Konvergo ERP Online ou Konvergo ERP.sh, nous vous recommandons de rediriger les messages entrants vers le nom de domaine d’Konvergo ERP plutôt que d’utiliser un serveur de messagerie externe. Vous recevrez ainsi tous les messages entrants sans délai. Les redirections pour toutes les adresses email doivent être configurées vers le nom de domaine d’Konvergo ERP dans le serveur de messagerie (par ex. `catchall@mydomain.ext` vers `catchall@mycompany.odoo.com`).

Tous les alias sont personnalisés dans Konvergo ERP. Les alias d’objets peuvent être
modifiés à partir de leurs configurations respectives en allant à Paramètres ‣
Menu technique ‣ Email ‣ Alias.

To edit catchall and bounce aliases, first activate the [developer
mode](../developer_mode#developer-mode). Then, go to Settings ‣ Technical
‣ Parameters ‣ System Parameters to customize the aliases
(`mail.catchall.alias` & `mail.bounce.alias`). These types of changes should
be completed prior to the database going live. If a customer replies after a
change is made then the system will not recognize the old alias, and the reply
will not be received.

Par défaut, les messages entrants sont récupérés toutes les 5 minutes pour les
bases de données sur serveur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier cette valeur dans le <a href="../developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>. Allez aux Paramètres ‣ Technique ‣ Automatisation ‣ Actions planfiiées et recherchez <b>Mail: Service Fetchmail</b>.</p>
</div>

### Paramètres système qui préviennent les boucles de rétraction

Deux paramètres système vous aident à prévenir des boucles de rétroaction dans
Konvergo ERP. Ces paramètres ont été introduits dans Konvergo ERP 16 pour empêcher les alias
de créer trop d’enregistrements et pour prévenir les boucles de rétroaction
sur l’adresse email de réponse catchall. Ils se trouvent dans la base de
données, mais pas dans les _Paramètres système_. Pour remplacer les valeurs
par défaut suivantes, ils doivent être ajoutés.

Les deux paramètres système sont les suivants :

  * `mail.gateway.loop.minutes` (120 minutes by default)

  * `mail.gateway.loop.threshold` (20 by default)

Ajoutez ces champs dans Konvergo ERP en activant d’abord le [mode
développeur](../developer_mode#developer-mode), et en allant ensuite à
Paramètres ‣ Menu technique ‣ Paramètres ‣ Paramètres système. Modifiez la
valeur de ces paramètres le cas échéant.

When an email is received in the Konvergo ERP database on the catchall email address
or on any alias, Konvergo ERP looks at the mail received for the given period of time
defined in the system parameter `mail.gateway.loop.minutes`. If the received
email was sent to an alias then Konvergo ERP will reference the
`mail.gateway.loop.threshold` system parameter and determine the value as the
number of records this alias is allowed to create in the given period of time
(value of `mail.gateway.loop.minutes`).

In addition, when email is received to the catchall email address, Konvergo ERP will
reference the emails received to the database during the set period of time
(as stated by the value in the system parameter: `mail.gateway.loop.minutes`).
Konvergo ERP will then determine whether any of the emails received match that of the
email(s) being received during the specified time-frame, and will prevent a
feedback loop from occurring if a duplicate email is detected.

### Allow alias domain system parameter

Incoming aliases are set in the Konvergo ERP database to create records by receiving
incoming emails. To view aliases set in the Konvergo ERP database, first activate the
[developer mode](../developer_mode#developer-mode). Then, go to Settings
app ‣ Technical ‣ Email section ‣ Aliases.

The following system parameter, `mail.catchall.domain.allowed`, set with
allowed alias domain values, separated by commas, filters out correctly
addressed emails to aliases. Setting the domain(s) for which the alias can
create a ticket, lead, opportunity, etc., eliminates false positives where
email addresses with only the prefix alias (not the domain) are present.

In some instances, matches have been made in the Konvergo ERP database when an email
is received with the same alias prefix and a different domain on the incoming
email address. This is true in the sender, recipient, and CC email addresses
of an incoming email.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si personne dans l’entreprise n’est engagée pour gérer les serveurs de messagerie, nous vous recommandons fortement de choisir Konvergo ERP Online et Konvergo ERP.sh. L’envoi d’emails de ces types d’hébergement d’Konvergo ERP fonctionne instantanément et est surveillé par des professionnels. Néanmoins, si une société souhaite gérer elle-même la réparation du serveur de messagerie, elle peut utiliser son propre serveur de messagerie. Pour plus d’informations, consultez <a href="email_domain">Configurer des enregistrements DNS pour envoyer des emails dans Konvergo ERP</a></p>
</div>0

To add the `mail.catchall.domain.allowed` system parameter, first, activate
the [developer mode](../developer_mode#developer-mode). Then, go to
Settings app ‣ Technical ‣ Parameters section ‣ System Parameters. Click
**Create**. Then, type in `mail.catchall.domain.allowed` for the **Key**
field.

Next, for the **Value** field, add the domain(s) separated by comma(s) (if
plural domains). Manually **Save** , and the system parameter takes immediate
effect.

![mail.catchall.domain.allowed system parameter set with key and value
highlighted.](../../../_images/allowed-domain.png)

  *[CC]: Carbon Copy

