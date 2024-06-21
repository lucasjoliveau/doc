# Authentification de connexion Google

L” _authentification de connexion Google_ est une fonctionnalité utile qui
permet aux utilisateurs d’Konvergo ERP de se connecter à leur base de données avec
leur compte Google.

Ceci est particulièrement utile si votre organisation utilise Google Workspace
et souhaite que ses employés se connectent à Konvergo ERP avec leurs comptes Google.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les bases de données hébergées sur Konvergo ERP.com ne doivent pas utiliser la connexion OAuth pour le propriétaire ou l’administrateur de la base de données, car cela dissocierait la base de données de leur compte Konvergo ERP.com. Si OAuth est configuré pour cet utilisateur, la base de données ne pourra plus être dupliquée, renommée ou autrement gérée à partir du portail Konvergo ERP.com.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../productivity/calendar/google">Synchroniser Google Agenda avec Konvergo ERP</a></p></li>
<li><p><a href="../email_communication/google_oauth">Connecter Gmail à Konvergo ERP en utilisant Google OAuth</a></p></li>
</ul>
</div>

## Configuration

L’intégration de la fonctionnalité de connexion Google nécessite une
configuration à la fois sur Google _et_ sur Konvergo ERP.

### Tableau de bord de l’API Google

  1. Allez au [Tableau de bord de l’API Google](https://console.developers.google.com/).

  2. Assurez-vous que le bon projet est ouvert. Si le projet n’existe pas encore, cliquez sur **Créer un projet** , complétez le nom du projet et les autres détails de la société et cliquez sur **Créer**.

![Compléter les détails d'un nouveau projet.](../../../_images/new-project-
details.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Choisissez le nom de la société dans le menu déroulant.</p>
</div>

#### Écran de consentement OAuth

  1. Dans le menu de gauche, cliquez sur Écran de consentement OAuth.

![Menu de sélection du consentement Google OAuth.](../../../_images/consent-
selection.png)

  2. Choisissez une des options (**Interne** / **Externe**), et cliquez sur **Créer**.

![Choix d'un utilisateur type dans le consentement
OAuth.](../../../_images/consent.png) <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les comptes Gmail <em>personnels</em> ne peuvent être que du type d’utilisateur <b>externe</b>, ce qui signifie que Google peut exiger une approbation ou l’ajout de <em>Champs d’application</em>. Cependant, l’utilisation d’un compte <em>Google WorkSpace</em> permet d’utiliser le type d’utilisateur <b>interne</b>.</p>
<p>Notez également que lorsque la connexion API est en mode de test <em>externe</em>, aucune approbation n’est nécessaire de la part de Google. Les limites d’utilisateurs dans ce mode de test sont fixées à 100 utilisateurs.</p>
</div>

  3. Complétez les coordonnées et les informations de domaine demandées, puis cliquez sur **Enregistrer et continuer**.

  4. Sur la page des Champs d’application, laissez tous les champs tels qu’ils sont et cliquez sur **Enregistrer et continuer**.

  5. Ensuite, si vous continuez en mode de test (_externe_), ajoutez les adresses email en cours de configuration à l’étape **Utilisateurs test** en cliquant sur **Ajouter des utilisateurs** , puis sur le bouton **Enregistrer et continuer**. Un résumé de l’inscription de l’application s’affiche.

  6. Enfin, faites défiler jusqu’en bas et cliquez sur **Revenir au tableau de bord**.

#### Identifiants

  1. Dans le menu de gauche, cliquez sur Identifiants.

![Bouton de menu des identifiants.](../../../_images/credentials-button.png)

  2. Cliquez sur **Créer des identifiants** et sélectionnez **ID client OAuth**.

![Sélection de l'ID client OAuth.](../../../_images/client-id.png)

  3. Sélectionnez **Application Web** comme **Type d’application**. Configurez à présent les pages autorisées vers lesquelles Konvergo ERP sera redirigé.

Pour ce faire, dans le champ **URl de redirection autorisés** , saisissez le
domaine de la base de données immédiatement suivi par `/auth_oauth/signin`.
Par exemple, `https://mydomain.odoo.com/auth_oauth/signin`, puis cliquez sur
**Créer**.

  4. Maintenant que le _Client OAuth_ a été créé, un écran avec l”**ID client** et le **code secret du Client** apparaîtra. Copiez l”**ID client** pour plus tard, puisqu’il sera nécessaire pour la configuration dans Konvergo ERP, qui sera couverte dans les étapes suivantes.

### Authentification Google sur Konvergo ERP

#### Récupérer l’ID client

Une fois que vous avez effectué les étapes précédentes, deux clés sont
générées sur le tableau de bord de l’API Google : **ID client** et **Code
secret du client**. Copiez l”**ID client**.

![L'ID client OAuth Google est généré.](../../../_images/secret-ids.png)

#### Activation sur Konvergo ERP

  1. Allez aux Paramètres généraux d’Konvergo ERP ‣ Intégrations et activez **Authentification OAuth**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP invitera peut-être l’utilisateur à se reconnecter après cette étape.</p>
</div>

  2. Retournez aux Paramètres généraux ‣ Intégrations ‣ Authentification OAuth, activez la sélection et cliquez sur **Enregistrer**. Ensuite, allez aux Paramètres généraux ‣ Intégrations ‣ Authentification Google et activez la sélection. Complétez ensuite l”**ID client** avec la clé enregistrée du tableau de bord de l’API Google et cliquez sur **Enregistrer**.

![Compléter l'ID client dans les paramètres d'Konvergo ERP.](../../../_images/odoo-
client-id.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration de Google OAuth2 est également accessible en cliquant sur <b>Fournisseurs OAuth</b> sous le titre <b>Authentification OAuth</b> dans la section Intégrations.</p>
</div>

## Se connecter à Konvergo ERP avec Google

Pour lier le compte Google au profil d’Konvergo ERP, cliquez sur **Se connecter avec
Google** lors de votre première connexion à Konvergo ERP.

> ![L'écran de réinitialisation du mot de passe avec le bouton *Se connecter
> avec Google*.](../../../_images/first-login.png)

Les utilisateurs existants doivent [réinitialiser leur mot de
passe](../users#users-reset-password) pour accéder à la page
Réinitialiser le mot de passe, tandis que les nouveaux utilisateurs peuvent
directement cliquer sur **Se connecter avec Google** , au lieu de choisir un
nouveau mot de passe.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://support.google.com/cloud/answer/6158849">Aide Google Cloud Platform Console - Configuration d’OAuth 2.0</a></p></li>
</ul>
</div>

