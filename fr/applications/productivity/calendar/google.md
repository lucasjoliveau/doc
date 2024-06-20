# Synchroniser Google Agenda avec Odoo

Synchronisez Google Agenda avec Odoo pour voir et gérer les réunions à partir
des deux plateformes (les mises à jour vont dans les deux sens). Cette
intégration permet d’organiser votre emploi du temps afin de ne jamais manquer
une réunion.

Pour plus d'infos

  * [Authentification de connexion Google](../../general/users/google.html)

  * [Connecter Gmail à Odoo en utilisant Google OAuth](../../general/email_communication/google_oauth.html)

## Configuration dans Google

### Sélectionner (ou créer) un projet

Créez un nouveau projet API Google et activez l’API Google Agenda. Allez
d’abord à la [Console API Google](https://console.developers.google.com) et
connectez-vous au compte Google.

Note

Si c’est la première fois que vous visitez cette page, Google invitera
l’utilisateur à saisir un pays et accepter les Conditions générales
d’utilisation. Sélectionnez un pays dans la liste déroulante et acceptez les
CGS.

Ensuite, cliquez sur Sélectionner un projet et sélectionnez (ou créez) un
projet API dans lequel vous allez configurer OAuth et enregistrer les
identifiants. Cliquez sur Nouveau projet.

![Créer un nouveau projet API pour enregistrer les
identifiants.](../../../_images/new-api-project.png)

Astuce

Donnez au projet API un nom évident, tel que « Odoo Sync » pour que vous
puissiez l’identifier facilement.

### Activer l’API Google Agenda

Cliquez à présent sur API et services activés dans le menu de gauche. Cliquez
de nouveau Activer les API et les services si la barre de recherche n’apparaît
pas.

![Activer les API et les services dans le Projet
API.](../../../_images/enable-apis-services.png)

Ensuite, recherchez `Google Calendar API` en utilisant la barre de recherche
et sélectionnez Google Calendar API dans les résultats de recherche. Cliquez
sur Activer.

![Activer l'API Google Agenda.](../../../_images/enable-google-cal-api.png)

### Écran de consentement OAuth

Maintenant que le projet API a été créé, OAuth devrait être configuré. Pour ce
faire, cliquez sur consentement OAuth dans le menu de gauche et sélectionnez
ensuite le Type d’utilisateur.

Avertissement

Les comptes Gmail _personnels_ ne peuvent être que du type d’utilisateur
**externe** , ce qui signifie que Google peut exiger une approbation ou
l’ajout de _Champs d’application_. Cependant, l’utilisation d’un compte
_Google WorkSpace_ permet d’utiliser le type d’utilisateur **interne**.

Notez également que lorsque la connexion API est en mode de test _externe_ ,
aucune approbation n’est nécessaire de la part de Google. Les limites
d’utilisateurs dans ce mode de test sont fixées à 100 utilisateurs.

Pour la deuxième étape, l”écran de consentement OAuth, saisissez `Odoo` dans
le champ Nom d’application, saisissez l’adresse email dans le champ Adresse
email d’assistance utilisateur et saisissez l’adresse email dans la section
Coordonnées du développeur. Cliquez ensuite sur Enregistrer et continuer.

Passez la troisième étape, Champs d’application, en cliquant sur Enregistrer
et continuer.

Ensuite, si vous continuez en mode de test (Externe), ajoutez les adresses
email en cours de configuration à l’étape Utilisateurs test, en cliquant sur
Ajouter des utilisateurs et ensuite sur le bouton Enregistrer et continuer. Un
résumé de l’inscription de l’application apparaît.

Enfin, faites défiler vers le bas et cliquez sur Revenir au tableau de bord.

Maintenant que le consentement OAuth a été configuré, il est temps de créer
des identifiants.

### Créer des identifiants

L” _ID client_ et le _Secret client_ sont tous deux nécessaires pour connecter
Google Agenda à Odoo. C’est la dernière étape dans la console Google.
Commencez par cliquer sur Identifiants dans le menu de gauche. Cliquez ensuite
sur Créer des identifiants et sélectionnez ID client OAuth, Google ouvrira un
guide pour créer des identifiants.

Sous Créer ID client OAuth, définissez le Type d’application sur Application
Web et saisissez `Ma base de données Odoo` dans le champ Nom.

  * Dans la section Origines JavaScript autorisées, cliquez sur \+ Ajouter un URl et saisissez l’adresse URL complète d’Odoo de la société.

  * Dans la section URl de redirection autorisés, cliquez sur \+ Ajouter un URl et saisissez l’adresse URL d’Odoo de la société, suivie par `/google_account/authentication`. Enfin, cliquez sur Créer.

![Ajouter les origines JavaScript autorisées et les URl de redirection
autorisés.](../../../_images/uri.png)

Un ID client et un Secret client s’afficheront, copiez-les dans un bloc-notes.

## Configuration dans Odoo

Une fois l” _ID client_ et le _Secret client_ localisés, ouvrez la base de
données Odoo et allez aux Paramètres ‣ Paramètres généraux ‣ Intégrations ‣
Google Agenda. Cochez la case à côté de Google Agenda.

![La case à cocher Google Agenda dans les Paramètres
généraux.](../../../_images/settings-google-cal.png)

Ensuite, copiez et collez l” _ID client_ et le _Secret client_ dans la page
des identifiants Google Calendar API dans les champs respectifs situés sous la
case à cocher Google Agenda. Cliquez ensuite sur Enregistrer.

## Synchroniser le calendrier dans Odoo

Enfin, ouvrez l’application Calendrier dans Odoo et cliquez sur le bouton de
synchronisation Google pour connecter Google Agenda avec Odoo.

![Cliquez sur le bouton de synchronisation Google dans Odoo Calendrier pour
synchroniser Odoo Calendrier avec Odoo.](../../../_images/sync-google.png)

Note

Lors de la synchronisation de Google Agenda avec Odoo pour la première fois,
la page redirigera vers le compte Google. De là, sélectionnez le compte
d’email qui devrait avoir accès, puis cliquez sur Continuer (si l’application
n’est pas vérifiée), et enfin cliquez sur Continuer (pour donner
l’autorisation de transférer des données)`.

![Autoriser Odoo à accéder à Google Agenda.](../../../_images/trust-odoo.png)

À présent, Odoo Calendrier est synchronisé avec succès avec Google Agenda !

Avertissement

Odoo recommande vivement de tester la synchronisation de l’agenda Google sur
une base de données de test et une adresse email de test (qui n’est pas
utilisée à d’autres fins) avant de tenter de synchroniser l’agenda Google
souhaité avec la base de données de production de l’utilisateur.

Une fois qu’un utilisateur synchronise son agenda Google avec le calendrier
d’Odoo :

  * La création d’un événement dans Odoo pousse Google à envoyer une invitation à tous les participants à l’événement.

  * La suppression d’un événement dans Odoo pousse Google à envoyer une annulation à tous les participants à l’événement.

  * L’ajout d’un contact à un événement pousse Google à envoyer une invitation à tous les participants à l’événement.

  * La suppression d’un contact d’un événement pousse Google à envoyer une annulation à tous les participants à l’événement.

Events can be created in _Google Calendar_ without sending a notification by
selecting Don’t Send when prompted to send invitation emails.

## Troubleshoot sync

There may be times when the _Google Calendar_ account does not sync correctly
with Odoo. Sync issues can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be performed
using the Reset Account button, which can be accessed by navigating to
Settings app ‣ Manage Users. Then, select the user to modify the calendar, and
click the Calendar tab.

![Reset buttons highlighted on the calendar tab of the
user.](../../../_images/google-reset.png)

Next, click Reset Account under the correct calendar.

### Reset options

The following reset options are available for troubleshooting Google calendar
sync with Odoo:

![Google calendar reset options in Odoo.](../../../_images/reset-calendar.png)

User’s Existing Events:

>   * Leave them untouched: no changes to the events.
>
>   * Delete from the current Google Calendar account: delete the events from
> _Google Calendar_.
>
>   * Delete from Odoo: delete the events from the Odoo calendar.
>
>   * Delete from both: delete the events from both _Google Calendar_ and Odoo
> calendar.
>
>

Next Synchronization:

>   * Synchronize only new events: sync new events on _Google Calendar_ and/or
> Odoo calendar.
>
>   * Synchronize all existing events: sync all events on _Google Calendar_
> and/or Odoo calendar.
>
>

Click Confirm after making the selection to modify the user’s events and the
calendar synchronization.

## FAQ Google OAuth

At times there can be misconfigurations that take place, and troubleshooting
is needed to resolve the issue. Below are the most common errors that may
occur when configuring the _Google Calendar_ for use with Odoo.

### Production vs. testing publishing status

Choosing Production as the Publishing Status (instead of Testing) displays the
following warning message:

`OAuth is limited to 100 sensitive scope logins until the OAuth consent screen
is verified. This may require a verification process that can take several
days.`

To correct this warning, navigate to the [Google API
Platform](https://console.cloud.google.com/apis/credentials/consent). If the
Publishing Status is In Production, click Back to Testing to correct the
issue.

### No test users added

If no test users are added to the OAuth consent screen, then an Error 403:
access_denied populates.

![Erreur 403 Accès Interdit.](../../../_images/403-error1.png)

To correct this error, return to the OAuth consent screen, under APIs &
Services, and add test users to the app. Add the email to be configured in
Odoo.

### Type d’application

When creating the credentials (OAuth _Client ID_ and _Client Secret_), if
Desktop App is selected for the Application Type, an Authorization Error
appears (Error 400:redirect_uri_mismatch).

![Erreur 400 URL de redirection incorrecte.](../../../_images/error-4001.png)

To correct this error, delete the existing credentials, and create new
credentials, by selecting Web Application for the Application Type.

Then, under Authorized redirect URIs, click ADD URI, and type:
`https://yourdbname.odoo.com/google_account/authentication` in the field,
being sure to replace _yourdbname_ in the URL with the **real** Odoo database
name.

Astuce

Ensure that the domain (used in the URI:
`https://yourdbname.odoo.com/google_account/authentication`) is the exact same
domain as configured in the `web.base.url` system parameter.

Access the `web.base.url` by activating [developer
mode](../../general/developer_mode.html#developer-mode), and navigating to
Settings app ‣ Technical header menu ‣ Parameters section ‣ System Parameters.

  *[CGS]: Conditions générales de service
  *[URL]: Uniform Resource Locator

