# Authentification de connexion Google

L” _authentification de connexion Google_ est une fonctionnalité utile qui
permet aux utilisateurs d’Odoo de se connecter à leur base de données avec
leur compte Google.

Ceci est particulièrement utile si votre organisation utilise Google Workspace
et souhaite que ses employés se connectent à Odoo avec leurs comptes Google.

Avertissement

Les bases de données hébergées sur Odoo.com ne doivent pas utiliser la
connexion OAuth pour le propriétaire ou l’administrateur de la base de
données, car cela dissocierait la base de données de leur compte Odoo.com. Si
OAuth est configuré pour cet utilisateur, la base de données ne pourra plus
être dupliquée, renommée ou autrement gérée à partir du portail Odoo.com.

Pour plus d'infos

  * [Synchroniser Google Agenda avec Odoo](../../productivity/calendar/google.html)

  * [Connecter Gmail à Odoo en utilisant Google OAuth](../email_communication/google_oauth.html)

## Configuration

L’intégration de la fonctionnalité de connexion Google nécessite une
configuration à la fois sur Google _et_ sur Odoo.

### Tableau de bord de l’API Google

  1. Allez au [Tableau de bord de l’API Google](https://console.developers.google.com/).

  2. Assurez-vous que le bon projet est ouvert. Si le projet n’existe pas encore, cliquez sur Créer un projet, complétez le nom du projet et les autres détails de la société et cliquez sur Créer.

![Compléter les détails d'un nouveau projet.](../../../_images/new-project-
details.png)

Astuce

Choisissez le nom de la société dans le menu déroulant.

#### Écran de consentement OAuth

  1. Dans le menu de gauche, cliquez sur Écran de consentement OAuth.

![Menu de sélection du consentement Google OAuth.](../../../_images/consent-
selection.png)

  2. Choisissez une des options (Interne / Externe), et cliquez sur Créer.

![Choix d'un utilisateur type dans le consentement
OAuth.](../../../_images/consent.png)

Avertissement

Les comptes Gmail _personnels_ ne peuvent être que du type d’utilisateur
**externe** , ce qui signifie que Google peut exiger une approbation ou
l’ajout de _Champs d’application_. Cependant, l’utilisation d’un compte
_Google WorkSpace_ permet d’utiliser le type d’utilisateur **interne**.

Notez également que lorsque la connexion API est en mode de test _externe_ ,
aucune approbation n’est nécessaire de la part de Google. Les limites
d’utilisateurs dans ce mode de test sont fixées à 100 utilisateurs.

  3. Complétez les coordonnées et les informations de domaine demandées, puis cliquez sur Enregistrer et continuer.

  4. Sur la page des Champs d’application, laissez tous les champs tels qu’ils sont et cliquez sur Enregistrer et continuer.

  5. Ensuite, si vous continuez en mode de test (_externe_), ajoutez les adresses email en cours de configuration à l’étape Utilisateurs test en cliquant sur Ajouter des utilisateurs, puis sur le bouton Enregistrer et continuer. Un résumé de l’inscription de l’application s’affiche.

  6. Enfin, faites défiler jusqu’en bas et cliquez sur Revenir au tableau de bord.

#### Identifiants

  1. Dans le menu de gauche, cliquez sur Identifiants.

![Bouton de menu des identifiants.](../../../_images/credentials-button.png)

  2. Cliquez sur Créer des identifiants et sélectionnez ID client OAuth.

![Sélection de l'ID client OAuth.](../../../_images/client-id.png)

  3. Sélectionnez Application Web comme Type d’application. Configurez à présent les pages autorisées vers lesquelles Odoo sera redirigé.

Pour ce faire, dans le champ URl de redirection autorisés, saisissez le
domaine de la base de données immédiatement suivi par `/auth_oauth/signin`.
Par exemple, `https://mydomain.odoo.com/auth_oauth/signin`, puis cliquez sur
Créer.

  4. Maintenant que le _Client OAuth_ a été créé, un écran avec l”ID client et le code secret du Client apparaîtra. Copiez l”ID client pour plus tard, puisqu’il sera nécessaire pour la configuration dans Odoo, qui sera couverte dans les étapes suivantes.

### Authentification Google sur Odoo

#### Récupérer l’ID client

Une fois que vous avez effectué les étapes précédentes, deux clés sont
générées sur le tableau de bord de l’API Google : ID client et Code secret du
client. Copiez l”ID client.

![L'ID client OAuth Google est généré.](../../../_images/secret-ids.png)

#### Activation sur Odoo

  1. Allez aux Paramètres généraux d’Odoo ‣ Intégrations et activez Authentification OAuth.

Note

Odoo invitera peut-être l’utilisateur à se reconnecter après cette étape.

  2. Retournez aux Paramètres généraux ‣ Intégrations ‣ Authentification OAuth, activez la sélection et cliquez sur Enregistrer. Ensuite, allez aux Paramètres généraux ‣ Intégrations ‣ Authentification Google et activez la sélection. Complétez ensuite l”ID client avec la clé enregistrée du tableau de bord de l’API Google et cliquez sur Enregistrer.

![Compléter l'ID client dans les paramètres d'Odoo.](../../../_images/odoo-
client-id.png)

Note

La configuration de Google OAuth2 est également accessible en cliquant sur
Fournisseurs OAuth sous le titre Authentification OAuth dans la section
Intégrations.

## Se connecter à Odoo avec Google

Pour lier le compte Google au profil d’Odoo, cliquez sur Se connecter avec
Google lors de votre première connexion à Odoo.

> ![L'écran de réinitialisation du mot de passe avec le bouton *Se connecter
> avec Google*.](../../../_images/first-login.png)

Les utilisateurs existants doivent [réinitialiser leur mot de
passe](../users.html#users-reset-password) pour accéder à la page
Réinitialiser le mot de passe, tandis que les nouveaux utilisateurs peuvent
directement cliquer sur Se connecter avec Google, au lieu de choisir un
nouveau mot de passe.

Pour plus d'infos

  * [Aide Google Cloud Platform Console - Configuration d’OAuth 2.0](https://support.google.com/cloud/answer/6158849)

