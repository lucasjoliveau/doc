# Synchronize Google calendar with Konvergo ERP

Synchronize Google Calendar with Konvergo ERP to see and manage meetings from both
platforms (updates go in both directions). This integration helps organize
schedules, so a meeting is never missed.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../general/users/google">Google Sign-In Authentication</a></p></li>
<li><p><a href="../../general/email_communication/google_oauth">Connect Gmail to Konvergo ERP using Google OAuth</a></p></li>
</ul>
</div>

## Setup in Google

### Select (or create) a project

Create a new Google API project and enable the Google Calendar API. First, go
to the [Google API Console](https://console.developers.google.com) and log
into the Google account.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If this is the first time visiting this page, Google will prompt the user to enter a country and
agree to the Terms of Service. Select a country from the drop-down list and agree to the
<abbr title="Terms of Service">ToS</abbr>.</p>
</div>

Next, click **Select a project** and select (or create) an API project to
configure OAuth in, and store credentials. Click **New Project**.

![Create a new API project to store credentials.](../../../_images/new-api-
project.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Give the API Project a clear name, like “Konvergo ERP Sync”, so it can be easily identified.</p>
</div>

### Enable Google calendar API

Now, click on **Enabled APIs and Services** in the left menu. Select **Enabled
APIs and Services** again if the **Search bar** doesn’t appear.

![Enable APIs and Services on the API Project.](../../../_images/enable-apis-
services.png)

After that, search for `Google Calendar API` using the search bar and select
**Google Calendar API** from the search results. Click **Enable**.

![Enable the Google Calendar API.](../../../_images/enable-google-cal-api.png)

### OAuth consent screen

Now that the API project has been created, OAuth should be configured. To do
that, click on **OAuth consent** in the left menu and then select the **User
Type**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p><em>Personal</em> Gmail Accounts are only allowed to be <b>External</b> User Type, which means Google may
require an approval, or for <em>Scopes</em> to be added on. However, using a <em>Google WorkSpace</em> account
allows for <b>Internal</b> User Type to be used.</p>
<p>Note, as well, that while the API connection is in the <em>External</em> testing mode, then no approval
is necessary from Google. User limits in this testing mode is set to 100 users.</p>
</div>

In the second step, **OAuth Consent Screen** , type `Konvergo ERP` in the **App name**
field, select the email address for the **User support email** field, and type
the email address for the **Developer contact information** section. Then,
click **Save and Continue**.

Skip the third step, Scopes, by clicking **Save and Continue**.

Next, if continuing in testing mode (External), add the email addresses being
configured under the **Test users** step, by clicking on **Add Users** , and
then the **Save and Continue** button. A summary of the app registration
appears.

Finally, scroll to the bottom, and click on **Back to Dashboard**.

Now, the OAuth consent has been configured, and it’s time to create
credentials.

### Create credentials

The _Client ID_ and the _Client Secret_ are both needed to connect Google
Calendar to Konvergo ERP. This is the last step in the Google console. Begin by
clicking **Credentials** in the left menu. Then, click **Create Credentials**
, and select **OAuth client ID** , Google will open a guide to create
credentials.

Under Create OAuth Client ID, select **Website application** for the
**Application Type** field, and type `My Konvergo ERP Database` for the **Name**.

  * Under the **Authorized JavaScript Origins** section, click **\+ Add URI** and type the company’s Konvergo ERP full URL address.

  * Under the **Authorized redirect URIs** section, click **\+ Add URI** and type the company’s Konvergo ERP URL address followed by `/google_account/authentication`. Finally, click **Create**.

![Add the authorized JavaScript origins and the authorized redirect
URIs.](../../../_images/uri.png)

A **Client ID** and **Client Secret** will appear, copy these to a notepad.

## Setup in Konvergo ERP

Once the _Client ID_ and the _Client Secret_ are located, open the Konvergo ERP
database and go to Settings ‣ General Settings ‣ Integrations ‣ Google
Calendar. Check the box next to **Google Calendar**.

![The Google Calendar checkbox in General
Settings.](../../../_images/settings-google-cal.png)

Next, copy and paste the _Client ID_ and the _Client Secret_ from the Google
Calendar API credentials page into their respective fields below the **Google
Calendar** checkbox. Then, click **Save**.

## Sync calendar in Konvergo ERP

Finally, open the Calendar app in Konvergo ERP and click on the **Google** sync button
to sync Google Calendar with Konvergo ERP.

![Click the Google sync button in Konvergo ERP Calendar to sync Google Calendar with
Konvergo ERP.](../../../_images/sync-google.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When syncing Google Calendar with Konvergo ERP for the first time, the page will redirect to the Google
Account. From there, select the <b>Email Account</b> that should have access, then select
<b>Continue</b> (should the app be unverifed), and finally select <b>Continue</b> (to
give permission for the transfer of data)`.</p>
</div> ![Give Konvergo ERP
permission to access Google Calendar.](../../../_images/trust-odoo.png)

Now, Konvergo ERP Calendar is successfully synced with Google Calendar!

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Konvergo ERP highly recommends testing the Google calendar synchronization on a test database and a test
email address (that is not used for any other purpose) before attempting to sync the desired
Google Calendar with the user’s production database.</p>
<p>Once a user synchronizes their Google calendar with the Konvergo ERP calendar:</p>
<ul>
<li><p>Creating an event in Konvergo ERP causes Google to send an invitation to all event attendees.</p></li>
<li><p>Deleting an event in Konvergo ERP causes Google to send a cancellation to all event attendees.</p></li>
<li><p>Adding a contact to an event causes Google to send an invitation to all event attendees.</p></li>
<li><p>Removing a contact from an event causes Google to send a cancellation to all event attendees.</p></li>
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

## Google OAuth FAQ

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

![403 Access Denied Error.](../../../_images/403-error1.png)

To correct this error, return to the **OAuth consent screen** , under **APIs &
Services**, and add test users to the app. Add the email to be configured in
Konvergo ERP.

### Application Type

When creating the credentials (OAuth _Client ID_ and _Client Secret_), if
**Desktop App** is selected for the **Application Type** , an **Authorization
Error** appears (**Error 400:redirect_uri_mismatch**).

![Error 400 Redirect URI Mismatch.](../../../_images/error-4001.png)

To correct this error, delete the existing credentials, and create new
credentials, by selecting **Web Application** for the **Application Type**.

Then, under **Authorized redirect URIs** , click **ADD URI** , and type:
`https://yourdbname.odoo.com/google_account/authentication` in the field,
being sure to replace _yourdbname_ in the URL with the **real** Konvergo ERP database
name.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Ensure that the domain (used in the URI:
<code>https://yourdbname.odoo.com/google_account/authentication</code>) is the exact same domain as
configured in the <code>web.base.url</code> system parameter.</p>
<p>Access the <code>web.base.url</code> by activating <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, and navigating to
Settings app ‣ Technical header menu ‣ Parameters section ‣ System
Parameters.</p>
</div>

  *[URL]: Uniform Resource Locator

