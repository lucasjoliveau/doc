# Outlook Calendar synchronization

Synchronizing a user’s _Outlook Calendar_ with Konvergo ERP is useful for keeping
track of tasks and appointments across all related applications.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../general/users/azure">Microsoft Azure sign-in authentication</a></p></li>
<li><p><a href="../../general/email_communication/azure_oauth">Connect Microsoft Outlook 365 to Konvergo ERP using Azure OAuth</a></p></li>
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
Tip</p><p>Ensure the database’s <abbr title="Uniform Resource Locator">URL</abbr> (domain) used in the URI is the
exact same domain as the one configured on the <code>web.base.url</code> system parameter.</p>
<p>Access the <code>web.base.url</code> by activating <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, and navigating to
Settings app ‣ Technical header menu ‣ Parameters section ‣ System
Parameters. Then, select it from the <b>Key</b> list on the <b>System Parameters</b>
page.</p>
</div> ![The "Supported account type" and
"Redirect URI" settings in the Microsoft Entra ID
portal.](../../../_images/azure-register-application.png)

For more information on the restrictions and limitations of URIs, check
Microsoft’s [Redirect URI (reply URL) restrictions and
limitations](https://docs.microsoft.com/en-us/azure/active-
directory/develop/reply-url) page.

Finally, on the application registration page, click **Register** button to
complete the application registration. The **Application (client) ID** is
produced. Copy this value, as it is needed later, in the Configuration in
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
Tip</p><p>Since resetting the synchronization can be tricky, Konvergo ERP recommends setting the maximum allowed
expiration date for the client secret (24 months or custom), so there is no need to
re-synchronize soon.</p>
</div>

Copy the **Value** for use in the next section.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Client secret values cannot be viewed, except immediately after creation. Be sure to save the
secret when created <em>before</em> leaving the page.</p>
</div>

## Configuration in Konvergo ERP

In the Konvergo ERP database, go to Settings app ‣ Integrations section, and tick the
checkbox beside the **Outlook Calendar** setting. Remember to click **Save**
to implement the changes.

![The "Outlook Calendar" setting activated in Konvergo ERP.](../../../_images/outlook-
calendar-setting.png)

From the Microsoft _Azure_ portal, under the **Overview** section of the
application, copy the **Application (Client) ID** , if it has not already been
copied, and paste it into the **Client ID** field in Konvergo ERP.

![The "Client ID" in the Microsoft Azure portal.](../../../_images/client-
id1.png)

Copy the previously-acquired **Value** (Client Secret Value), and paste it
into the **Client Secret** field in Konvergo ERP.

![The "Client Secret" token to be copied from Microsoft to
Konvergo ERP.](../../../_images/client-secret-value.png)

Finally, on the Konvergo ERP Settings ‣ General Settings page, click **Save**.

## Sync with Outlook

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Konvergo ERP highly recommends testing the Outlook calendar synchronization on a test database and a
test email address (that is not used for any other purpose) before attempting to sync the
desired Outlook Calendar with the user’s production database.</p>
<p>If the user has any past, present, or future events on their Konvergo ERP calendar before syncing their
Outlook calendar, Outlook will treat the events pulled from Konvergo ERP’s calendar during the sync as
new events, causing an email notification to be sent from Outlook to all the event attendees.</p>
<p>To avoid unwanted emails being sent to all past, present, and future event attendees, the user
must add the events from the Konvergo ERP calendar to the Outlook calendar before the first ever sync,
delete the events from Konvergo ERP, and then start the sync.</p>
<p>Even after synchronizing the Konvergo ERP Calendar with the Outlook calendar, Outlook will still send a
notification to all event participants every time an event is edited (created, deleted,
unarchived, or event date/time changed), with no exceptions. This is a limitation that cannot be
fixed from Konvergo ERP’s side.</p>
<p>In summary, once a user synchronizes their Outlook calendar with the Konvergo ERP calendar:</p>
<ul>
<li><p>Creating an event in Konvergo ERP causes Outlook to send an invitation to all event attendees.</p></li>
<li><p>Deleting an event in Konvergo ERP causes Outlook to send a cancellation to all event attendees.</p></li>
<li><p>Unarchiving an event in Konvergo ERP causes Outlook to send an invitation to all event attendees.</p></li>
<li><p>Archiving an event in Konvergo ERP causes Outlook to send a cancellation to all event attendees.</p></li>
<li><p>Adding a contact to an event causes Outlook to send an invitation to all event attendees.</p></li>
<li><p>Removing a contact from an event causes Outlook to send a cancellation to all event attendees.</p></li>
</ul>
</div>

### Sync Konvergo ERP Calendar and Outlook

In the Konvergo ERP database, open to the _Calendar_ module, and click the **Outlook**
sync button on the right-side of the page, beneath the monthly calendar.

![The "Outlook" sync button in Konvergo ERP Calendar.](../../../_images/outlook-sync-
button.png)

The synchronization is a two-way process, meaning that events are reconciled
in both accounts (_Outlook_ and Konvergo ERP). The page redirects to a Microsoft login
page, and the user is asked to log in to their account, if they are not
already. Finally, grant the required permissions by clicking **Accept**.

![Authentication process on Microsoft Outlook OAuth
page.](../../../_images/accept-terms.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>All users that want to use the synchronization simply need to <a href="#outlook-sync"><span class="std std-ref">sync their calendar with
Outlook</span></a>. The configuration of Microsoft’s <em>Azure</em> account is only done once, as
Microsoft <em>Entra ID</em> tenants’ client IDs and client secrets are unique, and help the user manage
a specific instance of Microsoft cloud services for internal and external users.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../general/integrations/mail_plugins/outlook">Outlook Plugin</a></p></li>
<li><p><a href="google">Synchronize Google calendar with Konvergo ERP</a></p></li>
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

