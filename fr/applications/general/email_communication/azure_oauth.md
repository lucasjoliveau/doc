# Connecter Microsoft Outlook 365 à Konvergo ERP avec Azure OAuth

Konvergo ERP est compatible avec la solution Azure OAuth de Microsoft for Microsoft
365. Afin d’envoyer et de recevoir des emails sécurisés depuis un domaine
personnalisé, il suffit de configurer quelques paramètres sur la plateforme
Azure et sur le backend de la base de données Konvergo ERP. Cette configuration
fonctionne soit avec une adresse email personnelle, soit avec une adresse
créée par un domaine personnalisé.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app">Microsoft Learn : Enregistrer une application avec la plateforme d’identités Microsoft</a></p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../users/azure">Authentification de connexion Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Synchronisation du Calendrier Outlook</a></p></li>
</ul>
</div>

## Configuration dans le portail Microsoft Azure

### Créer une nouvelle application

Pour commencer, allez au [Portail de Microsoft
Azure](https://portal.azure.com/). Connectez-vous avec le compte **Microsoft
Outlook Office 365** s’il y en a un, sinon connectez-vous avec votre **compte
Microsoft** personnel. Un utilisateur disposant d’un accès administratif aux
paramètres d’Azure devra se connecter et effectuer la configuration suivante.
Ensuite, allez à la section intitulée **Gérer Microsoft Entra ID** (auparavant
_Azure Active Directory_).

Cliquez sur **Ajouter (+)** dans le menu supérieur et puis sélectionnez
**Inscription d’application**. Sur la page **Inscrire une application** ,
remplacez le **Nom** par `Konvergo ERP` ou un autre nom significatif. Dans la section
**Types de comptes pris en charge** , sélectionnez **Comptes dans un annuaire
d’organisation (Tout annuaire Microsoft Entra ID - Multilocataire) et comptes
Microsoft personnels (par exemple, Skype, Xbox)**.

Dans la section **URL de redirection** , sélectionnez **Web** en tant que
plateforme et ensuite saisissez `https://<odoo base
url>/microsoft_outlook/confirm` dans le champ **URL**. L’URL de base d’Konvergo ERP
est le domaine canonique auquel votre instance Konvergo ERP peut être atteinte dans le
champ URL.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><em>mydatabase.odoo.com</em>, où <em>mydatabase</em> est le préfixe actuel du sous-domaine de la base de données, en supposant qu’elle soit hébergée sur Konvergo ERP.com</p>
</div>

Après avoir ajouté l’URL au champ, cliquez sur **S’inscrire** pour inscrire
l’application.

### API autorisées

Il faut ensuite définir les **API autorisées**. Konvergo ERP aura besoin
d’autorisations API spécifiques pour pouvoir lire (IMAP) et envoyer (SMTP) des
emails dans la configuration Microsoft 365. Cliquez d’abord sur le lien **API
autorisées** situé dans la barre de menu à gauche. Cliquez ensuite sur le
bouton **(+) Ajouter une autorisation** et sélectionnez **Microsoft Graph**
sous **API Microsoft couramment utilisées**. Ensuite, sélectionnez l’option
**Autorisations déléguées**.

In the search bar, search for the following **Delegated permissions** and
click **Add permissions** for each one:

  * **SMTP.Send**

  * **IMAP.AccessAsUser.All**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’autorisation <b>User.Read</b> sera ajoutée par défaut.</p>
</div> ![Les API autorisées nécessaires pour l'intégration Konvergo ERP
sont énumérées sous Microsoft Graph.](../../../_images/permissions.png)

## Assigner des utilisateurs et des groupes

Après avoir ajouté les autorisations de l’API, revenez à la **Vue d’ensemble**
de l”**Application** en haut du menu latéral gauche.

À présent, ajoutez des utilisateurs à cette application. Sous le tableau
général **Bases** , cliquez sur le lien intitulé **Application gérée dans le
répertoire local** ou la dernière option en bas à droite du tableau.

![Ajoutez des utilisateurs/groupes en cliquant sur le lien Application gérée
dans le répertoire local pour  l'application créée.](../../../_images/managed-
application.png)

Dans le menu latéral de gauche, sélectionnez **Utilisateurs et Groupes**.
Ensuite, cliquez sur **(+) Ajouter un Utilisateur/Groupe**. En fonction du
compte, un **Groupe** , ou un **Utilisateur** sera ajouté, ou uniquement des
**Utilisateurs**. Les comptes personnels ne permettent d’ajouter que des
**Utilisateurs**.

Sous **Utilisateurs** ou **Groupes** , cliquez sur **Aucun sélectionné** et
ajoutez les utilisateurs ou le groupe d’utilisateurs qui enverront des emails
depuis le **compte Microsoft** dans Konvergo ERP. **Ajoutez** les
utilisateurs/groupes, cliquez sur **Sélectionner** , et ensuite **assignez**
-les à l’application.

### Créer des identifiants

Maintenant que l’application Microsoft Azure est configurée, des identifiants
doivent être créées pour la configuration d’Konvergo ERP. Il s’agit de l”**ID Client**
et du **Secret Client**. Pour commencer, l”**ID Client** peut être copié
depuis la page **Aperçu** de l’application. L”**ID Client** ou l”**ID
d’application** se situe en-dessous du **Nom d’affichage** dans l’aperçu
**Essentials** de l’application.

![ID d'application/client dans la Vue d'ensemble de
l'application.](../../../_images/application-id.png)

Ensuite, il faut récupérer la **Valeur du Secret Client**. Pour obtenir cette
valeur, cliquez sur **Certificats & Secrets** dans le menu latéral de gauche.
Ensuite, il faut produire un **Secret Client**. Pour ce faire, cliquez sur le
bouton **(+) Nouveau Secret Client**.

Une fenêtre sur la droite s’affiche avec un bouton intitulé **Ajouter un
secret client**. Sous **Description** , saisissez `Konvergo ERP Fetchmail` ou quelque
chose de reconnaissable, puis définissez la **date d’expiration**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Un nouveau <b>Secret Client</b> devra être produit et configuré si le premier expire. Dans ce cas, il pourrait y avoir une interruption de service, il faut donc noter la date d’expiration et la fixer à la date la plus éloignée possible.</p>
</div>

Cliquez ensuite sur **Ajouter** lorsque ces deux valeurs sont saisies. Une
**Valeur de Secret Client** et un **ID Secret** seront créés. Il est importer
de copier la **Valeur** ou la **Valeur du Secret Client** dans un bloc-notes,
car elle sera chiffrée après avoir quitté cette page. L”**ID Secret** n’est
pas nécessaire.

![Valeur du Secret Client ou Valeur dans les identifiants de
l'application.](../../../_images/secretvalue.png)

Après ces étapes, les éléments suivants doivent être prêts à être configurés
dans Konvergo ERP :

  * Un ID client (**ID Client** ou **ID d’application**)

  * Un secret client (**Valeur** ou **Valeur du Secret Client**)

Ceci complète la configuration du côté du **Portail de Microsoft Azure**

## Configuration dans Konvergo ERP

### Saisir des identifiants de Microsoft Outlook

Ouvrez d’abord la base de données Konvergo ERP et allez au module **Applications**.
Supprimez ensuite le filtre **Applications** de la barre de recherche et
saisissez `Outlook`. Ensuite, installez le module intitulé **Microsoft
Outlook**.

Allez ensuite à Paramètres ‣ Paramètres généraux et dans la section
**Discussion** , assurez-vous que la case à côté de **Serveurs de messagerie
personnalisés** est cochée. Une nouvelle option s’affiche alors pour les
**Identifiants Outlook**.

**Enregistrez** la progression.

Ensuite, copiez et collez l”**ID Client** (ID d’application) et le **Secret
Client (Valeur du Secret Client)** dans les champs respectifs et
**enregistrez** les paramètres.

![Identifiants Outlook dans les Paramètres généraux
d'Konvergo ERP.](../../../_images/outlookcreds.png)

### Configurer le serveur de messagerie sortant

Sur la page des **Paramètres généraux** , sous le paramètre **Serveurs de
messagerie personnalisés** , cliquez sur le lien **Serveurs de messagerie
sortants** pour configurer le compte Microsoft.

Créez ensuite un nouveau serveur de messagerie et cochez la case à côté
d”**Outlook**. Ensuite, complétez le **Nom** (il peut s’agir de n’importe
quoi) et le **Nom d’utilisateur** de la messagerie Microsoft Outlook.

Si le champ **Filtre expéditeur** est vide, saisissez un [domaine ou une
adresse email](email_servers#email-communication-default).

Cliquez ensuite sur **Connecter votre compte Outlook**.

Une nouvelle fenêtre de Microsoft s’ouvre pour finaliser le **processus
d’authentification**. Sélectionnez l’adresse email personnalisée en cours de
configuration dans Konvergo ERP.

![Page d'autorisation pour accorder l'accès entre une application nouvellement
créée et Konvergo ERP.](../../../_images/verify-outlook.png)

Ensuite, autorisez Konvergo ERP à accéder au compte Microsoft en cliquant sur **Oui**.
Après cela, la page reviendra au **Serveur de messagerie sortant**
nouvellement configuré dans Konvergo ERP. La configuration charge automatiquement le
**jeton** dans Konvergo ERP et une étiquette indiquant **Jeton Outlook valide**
apparaît en vert.

![Indicateur de jeton Outlook valide.](../../../_images/outlook-token.png)

Finalement, cliquez sur **Test de connexion**. Un message de confirmation
devrait apparaître. La base de données Konvergo ERP peut désormais envoyer des emails
sûrs et sécurisés par le biais de Microsoft Outlook en utilisant
l’authentification OAuth.

#### Configuration avec un seul serveur de messagerie sortant

La configuration d’un seul serveur de messagerie sortant est la configuration
la plus simple disponible pour Microsoft Azure et ne nécessite pas de droits
d’accès étendus pour les utilisateurs de la base de données.

Une adresse email générique est utilisée pour envoyer des emails à tous les
utilisateurs de la base de données. Par exemple, elle pourrait être structurée
avec un alias `notifications` (`notifications@example.com`) ou un alias
`contact` (`contact@example.com`). Cette adresse doit être définie comme le
**filtre expéditeur** sur le serveur. Cette adresse doit également
correspondre à la combinaison de clés
`{mail.default.from}@{mail.catchall.domain}` dans les paramètres système.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour plus d’informations sur le filtre expéditeur, consultez <a href="email_servers#email-communication-default"><span class="std std-ref">Utiliser une adresse email « De » par défaut</span></a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les <b>Paramètres système</b> sont accessibles en activant le <span class="xref std std-ref">mode développeur</span> dans les Paramètres ‣ Technique ‣ Paramètres ‣ Paramètres système.</p>
</div>

Avec cette configuration, chaque email envoyé à partir de la base de données
utilisera l’adresse de la boîte de messagerie `notification` configurée. Il
convient toutefois de noter que le nom de l’expéditeur apparaîtra, mais que
son adresse email changera :

![Nom de l'expéditeur réel avec adresse email
statique.](../../../_images/from-name-remain.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Configuration d’un seul serveur de messagerie sortant :</p>
<ul>
<li><p><b>Nom d’utilisateur</b> (login) du serveur de messagerie sortant = <code>notifications@example.com</code></p></li>
<li><p><b>Filtre expéditeur</b> du serveur de messagerie sortant = <code>notifications@example.com</code></p></li>
<li><p><code>mail.catchall.domain</code> dans les paramètres système = <code>example.com</code></p></li>
<li><p><code>mail.default.from</code> dans les paramètres système = <code>notifications</code></p></li>
</ul>
</div>

#### Configuration spécifique à l’utilisateur (plusieurs utilisateurs)

En plus d’un serveur de messagerie générique, vous pouvez configurer des
serveurs de messagerie individuels pour les utilisateurs d’une base de
données. Ces adresses email doivent être configurées en tant que **filtre
expéditeur** sur chaque serveur individuel pour que cette configuration
fonctionne.

Cette configuration est la plus compliquée des deux configurations Microsoft
Azure, car elle exige que tous les utilisateurs configurés avec des serveurs
de messagerie aient des droits d’accès aux paramètres afin d’établir une
connexion au serveur de messagerie.

##### Configuration

Chaque utilisateur doit avoir un serveur de messagerie séparé. Le **Filtre
expéditeur** doit être défini pour que seul l’email de l’utilisateur soit
envoyé à partir de ce serveur. En d’autres termes, seul un utilisateur avec
une adresse email qui correspond au **Filtre expéditeur** défini peut utiliser
ce serveur.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour plus d’informations sur le filtre expéditeur, consultez <a href="email_servers#email-communication-default"><span class="std std-ref">Utiliser une adresse email « De » par défaut</span></a>.</p>
</div>

Un serveur de repli doit être configuré pour autoriser l’envoi de
**notifications**. Le **filtre expéditeur** pour ce serveur doit avoir la
valeur de `{mail.default.from}@{mail.catchall.domain}`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les <b>Paramètres système</b> sont accessibles en activant le <span class="xref std std-ref">mode développeur</span> dans les Paramètres ‣ Technique ‣ Paramètres ‣ Paramètres système.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../users/azure">Authentification de connexion Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Synchronisation du Calendrier Outlook</a></p></li>
</ul>
</div>0 <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../users/azure">Authentification de connexion Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Synchronisation du Calendrier Outlook</a></p></li>
</ul>
</div>2

### Configurer le serveur de messagerie entrant

Le compte entrant doit être configuré de la même manière que le compte de
messagerie sortant. Allez aux **Serveurs de messagerie entrants** dans le
**Menu technique** et **créez** une nouvelle configuration. Cochez ou
sélectionnez le bouton à côté d”**Authentification OAuth Outlook** et
saisissez le **nom d’utilisateur de Microsoft Outlook**. Cliquez sur
**Connecter votre compte Outlook**. Konvergo ERP affichera : **Jeton Outlook valide**.
À présent, **testez et confirmez** le compte. Le compte devrait être prêt à
recevoir des emails de la base de données Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../users/azure">Authentification de connexion Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Synchronisation du Calendrier Outlook</a></p></li>
</ul>
</div>3

