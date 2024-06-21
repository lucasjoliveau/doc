# Synchronisation du Calendrier Outlook

Synchronizing a user’s _Outlook Calendar_ with Konvergo ERP is useful for keeping
track of tasks and appointments across all related applications.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../general/users/azure">Authentification de connexion Microsoft Azure</a></p></li>
<li><p><a href="../../general/email_communication/azure_oauth">Connecter Microsoft Outlook 365 à Konvergo ERP avec Azure OAuth</a></p></li>
</ul>
</div>

## Microsoft Azure setup

To sync the _Outlook Calendar_ with Konvergo ERP’s _Calendar_ , a Microsoft _Azure_
account is required. Creating an account is free for users who have never
tried, or paid for, _Azure_. For more information, view the account options on
the [Azure website](https://azure.microsoft.com/en-
us/free/?WT.mc_id=A261C142F).

Refer to [Microsoft’s documentation](https://docs.microsoft.com/en-
us/azure/active-directory/develop/quickstart-create-new-tenant) on how to set
up a Microsoft _Entra ID_ (formally called Microsoft _Azure Active Directory
(Azure AD)_). This is an API console to manage and register Microsoft
applications.

Existing Microsoft _Entra ID_ users should log in at the [Microsoft Azure
developer portal](https://portal.azure.com/#home). Next, select **View** under
the section labeled **Manage Microsoft Entra ID**.

### Register application

After logging in with the Microsoft _Entra ID_ , [register an
application](https://docs.microsoft.com/en-us/azure/active-
directory/develop/quickstart-register-app).

To create an application, click **\+ Add** in the top menu. From the resulting
drop-down menu, select **App Registration**.

![Microsoft Azure management page with + Add and App Registration menu
highlighted.](../../../_images/app-register.png)

Enter a unique **Name** for the connected application.

Choosing the appropriate **Supported account type** is essential, or else the
connected application will not work. Users who wish to connect their _Outlook
Calendar_ to Konvergo ERP should select the **Accounts in any organizational directory
(Any Microsoft Entra ID directory - Multitenant) and personal Microsoft
accounts (e.g. Skype, Xbox)** option for **Supported account types**.

When configuring the **Redirect URI** , choose the **Web** option from the
first drop-down menu. Then, enter the Konvergo ERP database URI (URL) followed by
`/microsoft_account/authentication`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Enter <code>https://yourdbname.odoo.com/microsoft_account/authentication</code> for the <b>Redirect
URI</b>. Replace <code>yourdbname.odoo.com</code> with the <abbr title="Uniform Resource Locator">URL</abbr>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the database’s <abbr title="Uniform Resource Locator">URL</abbr> (domain) used in the URI is the
exact same domain as the one configured on the <code>web.base.url</code> system parameter.</p>
<p>Access the <code>web.base.url</code> by activating <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, and navigating to
Settings app ‣ Technical header menu ‣ Parameters section ‣ System
Parameters. Then, select it from the <b>Key</b> list on the <b>System Parameters</b>
page.</p>
</div> ![Les paramètres "types de comptes
pris en charge" et "l'URL de redirection" dans le portail Microsoft Entra
ID.](../../../_images/azure-register-application.png)

For more information on the restrictions and limitations of URIs, check
Microsoft’s [Redirect URI (reply URL) restrictions and
limitations](https://docs.microsoft.com/en-us/azure/active-
directory/develop/reply-url) page.

Finally, on the application registration page, click **Register** button to
complete the application registration. The **Application (client) ID** is
produced. Copy this value, as it is needed later, in the Configuration dans
Konvergo ERP.

![Application client ID highlighted in the essentials section of the newly
created application.](../../../_images/app-client-id.png)

### Create client secret

The second credential needed to complete the synchronization of the Microsoft
_Outlook Calendar_ is the _Client Secret_. The user **must** add a client
secret, as this allows Konvergo ERP to authenticate itself, requiring no interaction
from the user’s side. _Certificates_ are optional.

To add a client secret, click Certificates & secrets in the left menu. Then
click **\+ New client secret** to create the client secret.

![New client secret page with certificates and secrets menu and new client
secret option highlighted.](../../../_images/client-secret.png)

Next, type a **Description** , and select when the client secret **Expires**.
Available options include: **90 days (3 months)** , **365 days (12 months)** ,
**545 days (18 months)** , **730 days (24 months)** or **Custom**. The
**Custom** option allows the administrator to set a **Start** and **End**
date.

Finally, click **Add** to **Add a client secret**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Since resetting the synchronization can be tricky, Konvergo ERP recommends setting the maximum allowed
expiration date for the client secret (24 months or custom), so there is no need to
re-synchronize soon.</p>
</div>

Copy the **Value** for use in the next section.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Client secret values cannot be viewed, except immediately after creation. Be sure to save the
secret when created <em>before</em> leaving the page.</p>
</div>

## Configuration dans Konvergo ERP

In the Konvergo ERP database, go to Settings app ‣ Integrations section, and tick the
checkbox beside the **Outlook Calendar** setting. Remember to click **Save**
to implement the changes.

![Le paramètre "Calendrier Outlook" activé dans
Konvergo ERP.](../../../_images/outlook-calendar-setting.png)

From the Microsoft _Azure_ portal, under the **Overview** section of the
application, copy the **Application (Client) ID** , if it has not already been
copied, and paste it into the **Client ID** field in Konvergo ERP.

![L'"ID client" dans le portail de Microsoft Azure.](../../../_images/client-
id1.png)

Copy the previously-acquired **Value** (Client Secret Value), and paste it
into the **Client Secret** field in Konvergo ERP.

![Le jeton "Secret client" à copier de Microsoft vers
Konvergo ERP.](../../../_images/client-secret-value.png)

Enfin, sur la page Paramètres ‣ Paramètres généraux d’Konvergo ERP, cliquez sur
**Enregistrer**.

## Synchroniser avec Outlook

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Konvergo ERP recommande vivement de tester la synchronisation du calendrier Outlook sur une base de données de test et une adresse email de test (qui n’est pas utilisée à d’autres fins) avant de tenter de synchroniser le calendrier Outlook souhaité avec la base de données de production de l’utilisateur.</p>
<p>Si l’utilisateur a des événements passés, présents ou futurs dans son calendrier Outlook avant de le synchroniser, Outlook traitera les événements tirés du calendrier d’Konvergo ERP comme de nouveaux événements, ce qui entraînera l’envoi par Outlook d’une notification par email à tous les participants à l’événement.</p>
<p>Pour éviter l’envoi d’emails non désirés à tous les participants d’événements passés, présents et futurs, l’utilisateur doit ajouter les événements du calendrier Konvergo ERP au calendrier Outlook avant la toute première synchronisation, supprimer les événements dans Konvergo ERP et relancer la synchronisation.</p>
<p>Même après avoir synchronisé le calendrier Konvergo ERP avec le calendrier Outlook, Outlook enverra toujours une notification à tous les participants chaque fois qu’un événement est modifié (créé, supprimé, archivé ou changement de date/heure), sans exception. Il s’agit d’une limitation qui ne peut être corrigée par Konvergo ERP.</p>
<p>En résumé, une fois qu’un utilisateur synchronise son calendrier Outlook avec le calendrier Konvergo ERP :</p>
<ul>
<li><p>La création d’un événement Konvergo ERP pousse Outlook à envoyer une invitation à tous les participants à l’événement.</p></li>
<li><p>L’annulation d’un événement Konvergo ERP pousse Outlook à envoyer une annulation à tous les participants à l’événement.</p></li>
<li><p>La restauration d’un événement dans Konvergo ERP pousse Outlook à envoyer une invitation à tous les participants à l’événement.</p></li>
<li><p>L’archivage d’un événement dans Konvergo ERP pousse Outlook à envoyer une annulation à tous les participants à l’événement.</p></li>
<li><p>L’ajout d’un contact à un événement pousse Outlook à envoyer une invitation à tous les participants à l’événement.</p></li>
<li><p>La suppression d’un contact d’un événement pousse Outlook à envoyer une annulation à tous les participants à l’événement.</p></li>
</ul>
</div>

### Synchroniser le calendrier Konvergo ERP et Outlook

In the Konvergo ERP database, open to the _Calendar_ module, and click the **Outlook**
sync button on the right-side of the page, beneath the monthly calendar.

![Le bouton de synchronisation "Outlook" dans Konvergo ERP
Calendrier](../../../_images/outlook-sync-button.png)

The synchronization is a two-way process, meaning that events are reconciled
in both accounts (_Outlook_ and Konvergo ERP). The page redirects to a Microsoft login
page, and the user is asked to log in to their account, if they are not
already. Finally, grant the required permissions by clicking **Accept**.

![Authentication process on Microsoft Outlook OAuth
page.](../../../_images/accept-terms.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>All users that want to use the synchronization simply need to <a href="#outlook-sync"><span class="std std-ref">sync their calendar with
Outlook</span></a>. The configuration of Microsoft’s <em>Azure</em> account is only done once, as
Microsoft <em>Entra ID</em> tenants” client IDs and client secrets are unique, and help the user manage
a specific instance of Microsoft cloud services for internal and external users.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../general/integrations/mail_plugins/outlook">Plugin Outlook</a></p></li>
<li><p><a href="google">Synchroniser Google Agenda avec Konvergo ERP</a></p></li>
</ul>
</div>

## Troubleshoot sync

There may be times when the _Microsoft Outlook Calendar_ account does not sync
correctly with Konvergo ERP. Sync issues can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be performed
using the **Reset Account** button, which can be accessed by navigating to
Settings app ‣ Manage Users. Then, select the user to modify the calendar, and
click on the **Calendar** tab.

![Reset buttons highlighted on the calendar tab of the
user.](../../../_images/outlook-reset.png)

Next, click **Reset Account** under the correct calendar.

### Reset options

The following reset options are available for troubleshooting _Microsoft
Outlook Calendar_ sync with Konvergo ERP:

![Outlook calendar reset options in Konvergo ERP.](../../../_images/reset-
calendar1.png)

**User’s Existing Events** :

>   * **Leave them untouched** : no changes to the events.
>
>   * **Delete from the current Microsoft Calendar account** : delete the
> events from _Microsoft Outlook Calendar_.
>
>   * **Delete from Konvergo ERP** : delete the events from the Konvergo ERP calendar.
>
>   * **Delete from both** : delete the events from both _Microsoft Outlook
> Calendar_ and Konvergo ERP calendar.
>
>

**Next Synchronization** :

>   * **Synchronize only new events** : sync new events on _Microsoft Outlook
> Calendar_ and/or Konvergo ERP calendar.
>
>   * **Synchronize all existing events** : sync all events on _Microsoft
> Outlook Calendar_ and/or Konvergo ERP calendar.
>
>

Click **Confirm** after making the selection to modify the user’s events and
the calendar synchronization.

