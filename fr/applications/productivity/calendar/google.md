# Synchroniser Google Agenda avec Konvergo ERP

Synchronisez Google Agenda avec Konvergo ERP pour voir et gérer les réunions à partir
des deux plateformes (les mises à jour vont dans les deux sens). Cette
intégration permet d’organiser votre emploi du temps afin de ne jamais manquer
une réunion.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../general/users/google">Authentification de connexion Google</a></p></li>
<li><p><a href="../../general/email_communication/google_oauth">Connecter Gmail à Konvergo ERP en utilisant Google OAuth</a></p></li>
</ul>
</div>

## Configuration dans Google

### Sélectionner (ou créer) un projet

Créez un nouveau projet API Google et activez l’API Google Agenda. Allez
d’abord à la [Console API Google](https://console.developers.google.com) et
connectez-vous au compte Google.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si c’est la première fois que vous visitez cette page, Google invitera l’utilisateur à saisir un pays et accepter les Conditions générales d’utilisation. Sélectionnez un pays dans la liste déroulante et acceptez les <abbr title="Conditions générales de service">CGS</abbr>.</p>
</div>

Ensuite, cliquez sur **Sélectionner un projet** et sélectionnez (ou créez) un
projet API dans lequel vous allez configurer OAuth et enregistrer les
identifiants. Cliquez sur **Nouveau projet**.

![Créer un nouveau projet API pour enregistrer les
identifiants.](../../../_images/new-api-project.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Donnez au projet API un nom évident, tel que « Konvergo ERP Sync » pour que vous puissiez l’identifier facilement.</p>
</div>

### Activer l’API Google Agenda

Cliquez à présent sur **API et services activés** dans le menu de gauche.
Cliquez de nouveau **Activer les API et les services** si la **barre de
recherche** n’apparaît pas.

![Activer les API et les services dans le Projet
API.](../../../_images/enable-apis-services.png)

Ensuite, recherchez `Google Calendar API` en utilisant la barre de recherche
et sélectionnez **Google Calendar API** dans les résultats de recherche.
Cliquez sur **Activer**.

![Activer l'API Google Agenda.](../../../_images/enable-google-cal-api.png)

### Écran de consentement OAuth

Maintenant que le projet API a été créé, OAuth devrait être configuré. Pour ce
faire, cliquez sur **consentement OAuth** dans le menu de gauche et
sélectionnez ensuite le **Type d’utilisateur**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les comptes Gmail <em>personnels</em> ne peuvent être que du type d’utilisateur <b>externe</b>, ce qui signifie que Google peut exiger une approbation ou l’ajout de <em>Champs d’application</em>. Cependant, l’utilisation d’un compte <em>Google WorkSpace</em> permet d’utiliser le type d’utilisateur <b>interne</b>.</p>
<p>Notez également que lorsque la connexion API est en mode de test <em>externe</em>, aucune approbation n’est nécessaire de la part de Google. Les limites d’utilisateurs dans ce mode de test sont fixées à 100 utilisateurs.</p>
</div>

Pour la deuxième étape, l”**écran de consentement OAuth** , saisissez `Konvergo ERP`
dans le champ **Nom d’application** , saisissez l’adresse email dans le champ
**Adresse email d’assistance utilisateur** et saisissez l’adresse email dans
la section **Coordonnées du développeur**. Cliquez ensuite sur **Enregistrer
et continuer**.

Passez la troisième étape, Champs d’application, en cliquant sur **Enregistrer
et continuer**.

Ensuite, si vous continuez en mode de test (Externe), ajoutez les adresses
email en cours de configuration à l’étape **Utilisateurs test** , en cliquant
sur **Ajouter des utilisateurs** et ensuite sur le bouton **Enregistrer et
continuer**. Un résumé de l’inscription de l’application apparaît.

Enfin, faites défiler vers le bas et cliquez sur **Revenir au tableau de
bord**.

Maintenant que le consentement OAuth a été configuré, il est temps de créer
des identifiants.

### Créer des identifiants

L” _ID client_ et le _Secret client_ sont tous deux nécessaires pour connecter
Google Agenda à Konvergo ERP. C’est la dernière étape dans la console Google.
Commencez par cliquer sur **Identifiants** dans le menu de gauche. Cliquez
ensuite sur **Créer des identifiants** et sélectionnez **ID client OAuth** ,
Google ouvrira un guide pour créer des identifiants.

Sous Créer ID client OAuth, définissez le **Type d’application** sur
**Application Web** et saisissez `Ma base de données Konvergo ERP` dans le champ
**Nom**.

  * Dans la section **Origines JavaScript autorisées** , cliquez sur **\+ Ajouter un URl** et saisissez l’adresse URL complète d’Konvergo ERP de la société.

  * Dans la section **URl de redirection autorisés** , cliquez sur **\+ Ajouter un URl** et saisissez l’adresse URL d’Konvergo ERP de la société, suivie par `/google_account/authentication`. Enfin, cliquez sur **Créer**.

![Ajouter les origines JavaScript autorisées et les URl de redirection
autorisés.](../../../_images/uri.png)

Un **ID client** et un **Secret client** s’afficheront, copiez-les dans un
bloc-notes.

## Configuration dans Konvergo ERP

Une fois l” _ID client_ et le _Secret client_ localisés, ouvrez la base de
données Konvergo ERP et allez aux Paramètres ‣ Paramètres généraux ‣ Intégrations ‣
Google Agenda. Cochez la case à côté de **Google Agenda**.

![La case à cocher Google Agenda dans les Paramètres
généraux.](../../../_images/settings-google-cal.png)

Ensuite, copiez et collez l” _ID client_ et le _Secret client_ dans la page
des identifiants Google Calendar API dans les champs respectifs situés sous la
case à cocher **Google Agenda**. Cliquez ensuite sur **Enregistrer**.

## Synchroniser le calendrier dans Konvergo ERP

Enfin, ouvrez l’application Calendrier dans Konvergo ERP et cliquez sur le bouton de
synchronisation **Google** pour connecter Google Agenda avec Konvergo ERP.

![Cliquez sur le bouton de synchronisation Google dans Konvergo ERP Calendrier pour
synchroniser Konvergo ERP Calendrier avec Konvergo ERP.](../../../_images/sync-google.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lors de la synchronisation de Google Agenda avec Konvergo ERP pour la première fois, la page redirigera vers le compte Google. De là, sélectionnez le <b>compte d’email</b> qui devrait avoir accès, puis cliquez sur <b>Continuer</b> (si l’application n’est pas vérifiée), et enfin cliquez sur <b>Continuer</b> (pour donner l’autorisation de transférer des données)`.</p>
</div> ![Autoriser Konvergo ERP à accéder à Google
Agenda.](../../../_images/trust-odoo.png)

À présent, Konvergo ERP Calendrier est synchronisé avec succès avec Google Agenda !

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Konvergo ERP recommande vivement de tester la synchronisation de l’agenda Google sur une base de données de test et une adresse email de test (qui n’est pas utilisée à d’autres fins) avant de tenter de synchroniser l’agenda Google souhaité avec la base de données de production de l’utilisateur.</p>
<p>Une fois qu’un utilisateur synchronise son agenda Google avec le calendrier d’Konvergo ERP :</p>
<ul>
<li><p>La création d’un événement dans Konvergo ERP pousse Google à envoyer une invitation à tous les participants à l’événement.</p></li>
<li><p>La suppression d’un événement dans Konvergo ERP pousse Google à envoyer une annulation à tous les participants à l’événement.</p></li>
<li><p>L’ajout d’un contact à un événement pousse Google à envoyer une invitation à tous les participants à l’événement.</p></li>
<li><p>La suppression d’un contact d’un événement pousse Google à envoyer une annulation à tous les participants à l’événement.</p></li>
</ul>
<p>Events can be created in <em>Google Calendar</em> without sending a notification by selecting
<b>Don’t Send</b> when prompted to send invitation emails.</p>
</div>

## Troubleshoot sync

There may be times when the _Google Calendar_ account does not sync correctly
with Konvergo ERP. Sync issues can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be performed
using the **Reset Account** button, which can be accessed by navigating to
Settings app ‣ Manage Users. Then, select the user to modify the calendar, and
click the **Calendar** tab.

![Reset buttons highlighted on the calendar tab of the
user.](../../../_images/google-reset.png)

Next, click **Reset Account** under the correct calendar.

### Reset options

The following reset options are available for troubleshooting Google calendar
sync with Konvergo ERP:

![Google calendar reset options in Konvergo ERP.](../../../_images/reset-calendar.png)

**User’s Existing Events** :

>   * **Leave them untouched** : no changes to the events.
>
>   * **Delete from the current Google Calendar account** : delete the events
> from _Google Calendar_.
>
>   * **Delete from Konvergo ERP** : delete the events from the Konvergo ERP calendar.
>
>   * **Delete from both** : delete the events from both _Google Calendar_ and
> Konvergo ERP calendar.
>
>

**Next Synchronization** :

>   * **Synchronize only new events** : sync new events on _Google Calendar_
> and/or Konvergo ERP calendar.
>
>   * **Synchronize all existing events** : sync all events on _Google
> Calendar_ and/or Konvergo ERP calendar.
>
>

Click **Confirm** after making the selection to modify the user’s events and
the calendar synchronization.

## FAQ Google OAuth

At times there can be misconfigurations that take place, and troubleshooting
is needed to resolve the issue. Below are the most common errors that may
occur when configuring the _Google Calendar_ for use with Konvergo ERP.

### Production vs. testing publishing status

Choosing **Production** as the **Publishing Status** (instead of **Testing**)
displays the following warning message:

`OAuth is limited to 100 sensitive scope logins until the OAuth consent screen
is verified. This may require a verification process that can take several
days.`

To correct this warning, navigate to the [Google API
Platform](https://console.cloud.google.com/apis/credentials/consent). If the
**Publishing Status** is **In Production** , click **Back to Testing** to
correct the issue.

### No test users added

If no test users are added to the **OAuth consent screen** , then an **Error
403: access_denied** populates.

![Erreur 403 Accès Interdit.](../../../_images/403-error1.png)

To correct this error, return to the **OAuth consent screen** , under **APIs &
Services**, and add test users to the app. Add the email to be configured in
Konvergo ERP.

### Type d’application

When creating the credentials (OAuth _Client ID_ and _Client Secret_), if
**Desktop App** is selected for the **Application Type** , an **Authorization
Error** appears (**Error 400:redirect_uri_mismatch**).

![Erreur 400 URL de redirection incorrecte.](../../../_images/error-4001.png)

To correct this error, delete the existing credentials, and create new
credentials, by selecting **Web Application** for the **Application Type**.

Then, under **Authorized redirect URIs** , click **ADD URI** , and type:
`https://yourdbname.odoo.com/google_account/authentication` in the field,
being sure to replace _yourdbname_ in the URL with the **real** Konvergo ERP database
name.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure that the domain (used in the URI:
<code>https://yourdbname.odoo.com/google_account/authentication</code>) is the exact same domain as
configured in the <code>web.base.url</code> system parameter.</p>
<p>Access the <code>web.base.url</code> by activating <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, and navigating to
Settings app ‣ Technical header menu ‣ Parameters section ‣ System
Parameters.</p>
</div>

  *[URL]: Uniform Resource Locator

