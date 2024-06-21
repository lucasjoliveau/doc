# Connecter Gmail à Konvergo ERP en utilisant Google OAuth

Konvergo ERP est compatible avec la solution Google OAuth pour Gmail. Afin d’envoyer
des emails sécurisés à partir d’un domaine personnalisé, il suffit de
configurer quelques paramètres sur la plateforme Google _Workspace_ et sur le
backend de la base de données Konvergo ERP. Cette configuration fonctionne avec soit
une adresse email personnelle, soit une adresse créée par un domaine
personnalisé.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour plus d’informations, consultez la <a href="https://support.google.com/cloud/answer/6158849">documentation de Google</a> sur la configuration d’OAuth.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../users/google">Authentification de connexion Google</a></p></li>
<li><p><a href="../../productivity/calendar/google">Synchroniser Google Agenda avec Konvergo ERP</a></p></li>
</ul>
</div>

## Configuration dans Google

### Créer un nouveau projet

Pour commencer, allez à la [Console Google
API](https://console.developers.google.com). Connectez-vous avec votre compte
_Google Workspace_ si vous en avez un, sinon connectez-vous avec votre compte
Gmail personnel (ceci devrait correspondre à l’adresse email que vous
souhaitez configurer dans Konvergo ERP).

Ensuite, cliquez sur **Créer un projet** situé à l’extrême droite de l”**écran
de consentement OAuth**. Si un projet a déjà été créé dans ce compte, l’option
**Nouveau projet** sera disponible en haut à droite sous le menu déroulant
**Sélectionner un projet**.

Sur la page Nouveau projet, saisissez `Konvergo ERP` dans le champ **Nom du projet**
et recherchez la **Zone**. Définissez la **Zone** sur l” _organisation Google
Workspace_. Si vous utilisez un compte Gmail personnel, laissez la **Zone**
sur **Aucune organisation**.

![Nom du projet et Zone pour Google OAuth.](../../../_images/new-project.png)

Cliquez sur **Créer** pour finaliser cette étape.

### Écran de consentement OAuth

Si la page ne redirige pas vers les options Type d’utilisateur, cliquez sur
l”**écran de consentement OAuth** dans le menu de gauche.

Sous les options de **Type d’utilisateur** , sélectionnez le **Type
d’utilisateur** approprié et cliquez de nouveau sur **Créer** , ce qui vous
amènera à la page permettant de Modifier l’inscription de l’application.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les comptes Gmail <em>personnels</em> ne peuvent être que du type d’utilisateur <b>externe</b>, ce qui signifie que Google peut exiger une approbation ou l’ajout de <em>Champs d’application</em>. Cependant, l’utilisation d’un compte <em>Google WorkSpace</em> permet d’utiliser le type d’utilisateur <b>interne</b>.</p>
<p>Notez également que lorsque la connexion API est en mode de test <em>externe</em>, aucune approbation n’est nécessaire de la part de Google. Les limites d’utilisateurs dans ce mode de test sont fixées à 100 utilisateurs.</p>
</div>

### Modifier l’enregistrement de l’application

Ensuite, nous configurerons l’inscription de l’application du projet.

À l’étape de l”**écran de consentement OAuth** , sous la section
**Informations sur l’application** , saisissez `Konvergo ERP` dans le champ **Nom de
l’application**. Sélectionnez l’adresse email de l’organisation dans le champ
d’adresse mail d”**assistance utilisateur**.

Ensuite, sous Domaine de l’application ‣ Domaines autorisés, cliquez sur
**Ajouter un domaine** et saisissez `odoo.com`.

Ensuite, dans la section **Coordonnées du développeur** , saisissez l’adresse
email de l’organisation. Google utilise cette adresse email pour notifier
l’organisation de toute modification apportée à votre projet.

Ensuite, cliquez sur le bouton **Enregistrer et continuer**. Passez la page
Champs d’application en défilant vers le bas et en cliquant sur **Enregistrer
et continuer**.

Si vous continuez en mode de test (Externe), ajoutez les adresses email en
cours de configuration à l’étape **utilisateurs test** , en cliquant sur
**Ajouter des utilisateurs** et ensuite sur le bouton **Enregistrer et
continuer**. Un résumé de l’inscription de l’application s’affiche.

Finalement, défilez vers le bas et cliquez sur **Revenir au tableau de bord**
pour finaliser la configuration du projet.

### Créer des identifiants

Maintenant que le projet est configuré, vous devez créer des identifiants, qui
comprennent l” _ID client_ et le _Code secret du client_. Cliquez d’abord sur
**Identifiants** dans le menu latéral de gauche.

Cliquez ensuite sur **Créer des identifiants** dans le menu supérieur et
sélectionnez **ID client OAuth** dans le menu déroulant.

  * Dans le menu déroulant, définissiez le **Type d’application** sur **Application Web**.

  * Saisissez `Konvergo ERP` dans le champ **Nom**.

  * Sous le libellé **URl de redirection autorisés** , cliquez sur le bouton **AJOUTER UN URl** et saisissez `https://yourdbname.odoo.com/google_gmail/confirm` dans le champ **URI 1**. Veillez à remplacer la partie _yourdbname_ de l’URL par le nom réel de votre base de données Konvergo ERP.

  * Ensuite, cliquez sur **Créer** pour générer un **ID client** et un **Secret client** OAuth. Finalement, copiez chaque valeur générée pour pouvoir les utiliser ultérieurement lors de la configuration dans Konvergo ERP et allez ensuite à la base de données Konvergo ERP.

![ID Client et Secret Client pour Google OAuth.](../../../_images/client-
credentials.png)

## Configuration dans Konvergo ERP

### Saisir des identifiants Google

Ouvrez d’abord Konvergo ERP et allez au module **Applications**. Supprimez le filtre
**Applications** de la barre de recherche et saisissez `Google`. Installez le
module intitulé **Google Gmail**.

Ensuite, allez aux Paramètres ‣ Paramètres généraux et dans la section
**Discussion** , assurez-vous que la case à cocher à côté de **Serveurs de
messagerie personnalisés** ou **Serveurs de messagerie externes** est cochée.
Une nouvelle option s’affiche alors pour les **Identifiants Gmail** ou
**Utiliser un serveur Gmail**. Ensuite, copiez et collez les valeurs
respectives dans les champs **ID client** et **Secret client** et
**enregistrez** les paramètres.

### Configurer le serveur de messagerie sortant

Pour configurer un compte Gmail externe, revenez en haut du paramètre
**Serveurs de messagerie personnalisés** et cliquez sur le lien **Serveurs de
messagerie sortants**.

![Configurer des serveurs de messagerie sortants dans
Konvergo ERP.](../../../_images/outgoing-servers.png)

Ensuite, cliquez sur **Nouveau** ou **Créer** pour créer un nouveau serveur de
messagerie et complétez le **Nom** , la **Description** , et le **Nom
d’utilisateur** de l’email (si requis).

Ensuite cliquez sur **Authentification OAuth Gmail** ou **Gmail** (dans la
section **S’authentifier avec** ou **Connexion**). Enfin, cliquez sur
**Connecter votre compte Gmail**.

Une nouvelle fenêtre de **Google** s’ouvre vous permettant de finaliser le
processus d’authentification. Sélectionnez l’adresse email appropriée en cours
de configuration dans Konvergo ERP.

Si l’adresse email est un compte personnel, une fenêtre contextuelle
comportant une étape additionnelle apparaît, cliquez sur **Continuer** pour
permettre la vérification et la connexion du compte Gmail à Konvergo ERP.

Ensuite, autorisez Konvergo ERP à accéder au compte Google en cliquant sur
**Continuer** ou **Autoriser**. Après cela, la page reviendra au serveur de
messagerie sortant nouvellement créé dans Konvergo ERP. La configuration charge
automatiquement le jeton dans Konvergo ERP et une étiquette indiquant **Jeton Gmail
valide** apparaît en vert.

![Configurer des serveurs de messagerie sortants dans
Konvergo ERP.](../../../_images/green-token.png)

Enfin, faites un **Test de connexion**. Un message de configuration devrait
apparaître. La base de données Konvergo ERP peut désormais envoyer des emails sûrs et
sécurisés par le biais de Google en utilisant l’authentification OAuth.

## FAQ Google OAuth

### Statut de publication Production VS Test

Si vous définissez l”**État de publication** sur **Production** (au lieu de
**Test**), le message d’avertissement suivant s’affichera :

![OAuth est limité à 100 connexions de champ d'application
sensible.](../../../_images/published-status.png)

Pour corriger cet avertissement, allez à la [Plateforme Google
API](https://console.cloud.google.com/apis/credentials/consent). Si l”**État
de publication** est **En production** , cliquez sur **Retour à l’état de
test** pour corriger le problème.

### Aucun utilisateur test ajouté

Si aucun utilisateur test n’est ajouté à l’écran de consentement OAuth, une
erreur 403 accès interdit s’affichera.

![Erreur 403 Accès Interdit.](../../../_images/403-error.png)

Pour corriger cette erreur, retournez à l”**écran de consentement OAuth** sous
**API & Services** et ajoutez des utilisateurs tests à l’application. Ajoutez
l’email que vous êtes en train de configurer dans Konvergo ERP.

### Module Gmail non mis à jour

Si le module _Google Gmail_ dans Konvergo ERP n’a pas été mis à jour vers la dernière
version, un message d’erreur **Interdit** s’affichera.

![Interdit. Vous n'avez pas l'autorisation d'accéder à la ressource
demandée.](../../../_images/forbidden-error.png)

Pour corriger cette erreur, allez au module Applications et effacez la
recherche. Recherchez ensuite `Gmail` ou `Google` et mettez à niveau le module
**Google Gmail**. Enfin, cliquez sur les trois points dans le coin supérieur
droit du module et sélectionnez **Mettre à niveau**.

### Type d’application

Lors de la création des identifiants (_ID client_ et _Secret client_ OAuth),
si le **Type d’application** est défini sur **Application de bureau** , une
**Erreur d’autorisation** apparaît.

![Erreur 400 URL de redirection incorrecte.](../../../_images/error-400.png)

Pour corriger cette erreur, supprimez les identifiants déjà créés et créez de
nouveaux identifiants en définissant le **Type d’application** sur
**Application Web**. Ensuite, sous **URl de redirection autorisés** , cliquez
sur **AJOUTER UN URl** et saisissez
`https://yourdbname.odoo.com/google_gmail/confirm` dans le champ, en veillant
à remplacer _yourdbname_ dans l’URL par le nom de la base de données Konvergo ERP.

