# Authentification de connexion Microsoft Azure

L’authentification de connexion Microsoft Azure OAuth est une fonctionnalité
utile qui permet aux utilisateurs d’Konvergo ERP de se connecter à leur base de
données avec leur compte Microsoft Azure.

Ceci est particulièrement utile si l’organisation utilise Azure Workspace et
souhaite que ses employés se connectent à Konvergo ERP avec leurs comptes Microsoft.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les bases de données hébergées sur Konvergo ERP.com ne doivent pas utiliser la connexion OAuth pour le propriétaire ou l’administrateur de la base de données, car cela dissocierait la base de données de leur compte Konvergo ERP.com. Si OAuth est configuré pour cet utilisateur, la base de données ne pourra plus être dupliquée, renommée ou autrement gérée à partir du portail Konvergo ERP.com.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../productivity/calendar/outlook">Synchronisation du Calendrier Outlook</a></p></li>
<li><p><a href="../email_communication/azure_oauth">Connecter Microsoft Outlook 365 à Konvergo ERP avec Azure OAuth</a></p></li>
</ul>
</div>

## Configuration

L’intégration de la fonctionnalité de connexion Microsoft nécessite une
configuration sur Microsoft et sur Konvergo ERP.

### Paramètres système d’Konvergo ERP

Activez d’abord le [mode développeur](../developer_mode#developer-mode),
et allez ensuite aux Paramètres ‣ Technique ‣ Paramètres système.

Cliquez sur **Créer** et sur le nouveau formulaire vierge qui apparaît,
ajoutez le paramètre système suivant `auth_oauth.authorization_header` dans le
champ **Clé** et définissez la **Valeur** sur `1`. Cliquez ensuite sur
**Enregistrer** pour terminer.

### Tableau de bord Microsoft Azure

#### Créer une nouvelle application

Maintenant que les paramètres système ont été configurés dans Konvergo ERP, vous devez
créer une application correspondante dans Microsoft Azure. Pour commencer à
créer la nouvelle application, allez au [Portail de Microsoft
Azure](https://portal.azure.com/). Connectez-vous avec le compte **Microsoft
Outlook Office 365** s’il y en a un, sinon, connectez-vous avec un **compte
Microsoft** personnel.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Un utilisateur disposant d’accès d’administrateur aux <em>paramètres d’Azure</em> doit se connecter et effectuer les étapes de configuration suivantes.</p>
</div>

Ensuitez, allez à la section intitulée **Gérer Microsoft Entra ID**
(auparavant _Azure Active Directory_). Ce lien se trouve généralement au
milieu de la page.

Cliquez à présent sur l’icône **Ajouter (+)** dans le menu supérieur et
sélectionnez **Inscription d’application** dans le menu déroulant. Sur l’écran
**Inscrire une application** , remplacez le nom dans le champ **Nom** par
`OAuth connexion Konvergo ERP` ou un autre nom reconnaissable. Dans la section **Types
de comptes pris en charge** , sélectionnez l’option **Comptes dans cet
annuaire d’organisation uniquement (Annuaire par défaut uniquement - Un seul
locataire)**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les <b>Types de comptes pris en charge</b> peuvent varier par type de compte Microsoft et de l’utilisation finale de l’OAuth. Par exemple : La connexion est-elle destinée aux utilisateurs internes d’une organisation ou à l’accès au portail des clients ? La configuration ci-dessus est utilisée pour les utilisateurs internes d’une organisation.</p>
<p>Choisissez <b>Comptes Microsoft personnels uniquement</b> si les utilisateurs du portail sont ciblés. Choisissez <b>Comptes dans cet annuaire d’organisation uniquement (Annuaire par défaut uniquement - Un seul locataire)</b> si les utilisateurs d’une entreprise sont ciblés.</p>
</div>

Dans la section **URl de redirection** , sélectionnez la plateforme **Web** et
saisissez `https://<odoo base url>/auth_oauth/signin` dans le champ **URL**.
L”URL de base d’Konvergo ERP est le domaine canonique auquel votre instance Konvergo ERP peut
être atteinte (par ex. _mydatabase.odoo.com_ si vous êtes hébergé sur
Konvergo ERP.com). Cliquez ensuite sur **S’inscrire** , et l’application est créée.

#### Authentification

Modifiez l’authentification de la nouvelle application en cliquant sur
**Authentification** dans le menu de gauche après avoir été redirigé vers les
paramètres de l’application après l’étape précédente.

Ensuite, vous devez choisir le type de _jetons_ nécessaires pour
l’authentification OAuth. Il ne s’agit pas de jetons monétaires, mais plutôt
de jetons d’authentification qui sont transmis entre Microsoft et Konvergo ERP. Par
conséquent, il n’y a aucun coût pour ces jetons ; ils sont simplement utilisés
à des fins d’authentification entre deux APIs. Sélectionnez les jetons qui
doivent être émis par le point de terminaison d’autorisation en faisant
défiler l’écran vers le bas et cochez les cases : **Jetons d’accès (utilisés
pour les flux implicites)** et **Jetons d’ID (utilisés pour les flux
implicites et hybrides)**.

![Paramètres d'authentification et jetons de points de
terminaison.](../../../_images/authentication-tokens.png)

Cliquez sur **Enregistrer** pour que ces paramètres soient enregistrés.

#### Rassembler des identifiants

Une fois l’application créée et authentifiée dans la console Microsoft Azure,
les identifiants doivent être rassemblés. Pour ce faire, cliquez sur le menu
**Aperçu** dans la colonne de gauche. Sélectionnez et copiez l”**ID
d’application (client)** dans la fenêtre qui s’affiche. Collez ces
identifiants dans un presse-papiers / bloc-notes, car ces identifiants seront
utilisés ultérieurement dans la configuration Konvergo ERP.

Après avoir finalisé cette étape, cliquez sur **Points de terminaison** dans
le menu supérieur et cliquez sur _l’icône copier_ à côté du champ **Point de
terminaison d’autorisation OAuth 2.0 (v2)**. Collez cette valeur dans le
presse-papiers / bloc-notes.

![Identifiants de l'ID d'application et le point de terminaison d'autorisation
OAuth 2.0 \(v2\).](../../../_images/overview-azure-app.png)

### Configuration Konvergo ERP

Enfin, la dernière étape de la configuration Microsoft Azure OAuth consiste à
configurer certains paramètres dans Konvergo ERP. Allez aux Paramètres ‣ Intégrations
‣ Authentification OAuth et cochez la case pour activer la fonctionnalité de
connexion OAuth. Cliquez sur **Enregistrer** pour que la progression soit
enregistrée. Connectez-vous ensuite à la base de données une fois que l’écran
de connexion se charge.

Une fois de plus, allez aux Paramètres ‣ Intégrations ‣ Authentification OAuth
et cliquez sur **Fournisseurs OAuth**. Sélectionnez à présent **Nouveau** dans
le coin supérieur gauche et nommez le fournisseur `Azure`.

Collez l”**ID d’application (client)** de la section précédente dans le champ
**ID client**. Ensuite, collez la nouvelle valeur **Point de terminaison
d’authentification OAuth 2.0 (v2)** dans le champ **URL d’autorisation**.

Pour le champ **URL des UserInfo** , collez l”URL suivante :
`https://graph.microsoft.com/oidc/userinfo`

Dans le champ **Portée** , collez la valeur suivante : `openid profile email`.
Ensuite, le logo Windows peut être utilisé comme la classe CCS sur l’écran de
connexion en saisissant la valeur suivante : `fa fa-fw fa-windows` dans le
champ **classe CSS**.

Cochez la case à côté du champ **Autorisé** pour activer le fournisseur OAuth.
Enfin, ajoutez `Microsoft Azure` dans le champ **Libellé du bouton de
connexion**. Ce texte apparaîtra à côté du logo Windows sur la page de
connexion.

![Configuration du fournisseur dans l'application Paramètres
d'Konvergo ERP.](../../../_images/odoo-provider-settings.png)

**Enregistrez** les modifications pour finaliser la configuration de
l’authentification OAuth dans Konvergo ERP.

### Flux de l’expérience utilisateur

Pour qu’un utilisateur puisse se connecter à Konvergo ERP en utilisant Microsoft
Azure, l’utilisateur doit se trouver sur la page de réinitialisation du mot de
passe Konvergo ERP. C’est la seule façon pour Konvergo ERP de lier le compte Microsoft Azure
et de permettre à l’utilisateur de se connecter.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les utilisateurs existants doivent <a href="../users#users-reset-password"><span class="std std-ref">réinitialiser leur mot de passe</span></a> pour accéder à la page de réinitialisation du mot de passe Konvergo ERP. Les nouveaux utilisateurs d’Konvergo ERP doivent cliquer sur le lien d’invitation des nouveaux utilisateurs qui leur a été envoyé par mail, puis cliquer sur <b>Microsoft Azure</b>. Les utilisateurs ne doivent pas définir un nouveau mot de passe.</p>
</div>

Pour se connecter à Konvergo ERP pour la première fois en utilisant le fournisseur
OAuth de Microsoft Azure, allez à la page de réinitialisation du mot de passe
Konvergo ERP (en utilisant le lien d’invitation des nouveaux utilisateurs). Une page
de réinitialisation du mot de passe devrait apparaître. Cliquez ensuite sur
l’option intitulée **Microsoft Azure**. La page sera redirigée vers la page de
connexion Microsoft.

![Page de connexion Microsoft Outlook.](../../../_images/odoo-login.png)

Saisissez l”**adresse mail Microsoft** et cliquez sur **Suivant**. Suivez la
procédure pour vous connecter au compte. Si l’option 2FA est activée, une
étape supplémentaire peut être nécessaire.

![Saisissez les identifiants de connexion de
Microsoft.](../../../_images/login-next.png)

Enfin, après s’être connecté au compte, la page sera redirigée vers une page
d’autorisations où l’utilisateur sera invité à **Accepter** les conditions
d’accès de l’application Konvergo ERP à ses informations Microsoft.

![Acceptez les conditions de Microsoft pour autoriser l'accès aux informations
de votre compte.](../../../_images/accept-access.png)

  *[URL]: Uniform Resource Locator
  *[APIs]: application programming interfaces
  *[2FA]: Authentification à deux facteurs

