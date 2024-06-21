# Connect Microsoft Outlook 365 to Konvergo ERP using Azure OAuth

Konvergo ERP is compatible with Microsoft’s Azure OAuth for Microsoft 365. In order to
send and receive secure emails from a custom domain, all that is required is
to configure a few settings on the Azure platform and on the back end of the
Konvergo ERP database. This configuration works with either a personal email address
or an address created by a custom domain.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app">Microsoft Learn: Register an application with the Microsoft identity platform</a></p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../users/azure">Microsoft Azure sign-in authentication</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Outlook Calendar synchronization</a></p></li>
</ul>
</div>

## Setup in Microsoft Azure Portal

### Create a new application

To get started, go to [Microsoft’s Azure Portal](https://portal.azure.com/).
Log in with the **Microsoft Outlook Office 365** account if there is one,
otherwise log in with the personal **Microsoft account**. A user with
administrative access to the Azure Settings will need to connect and perform
the following configuration. Next, navigate to the section labeled **Manage
Microsoft Entra ID** (formally _Azure Active Directory_).

Now, click on **Add (+)** , located in the top menu, and then select **App
registration**. On the **Register an application** screen, rename the **Name**
to `Konvergo ERP` or something recognizable. Under the **Supported account types**
section select **Accounts in any organizational directory (Any Microsoft Entra
ID directory - Multitenant) and personal Microsoft accounts (e.g. Skype,
Xbox)**.

Under the **Redirect URL** section, select **Web** as the platform, and then
input `https://<odoo base url>/microsoft_outlook/confirm` in the **URL**
field. The Konvergo ERP base URL is the canonical domain at which your Konvergo ERP instance
can be reached in the URL field.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><em>mydatabase.odoo.com</em>, where <em>mydatabase</em> is the actual prefix of the database’s subdomain,
assuming it’s hosted on Konvergo ERP.com</p>
</div>

After the URL has been added to the field, **Register** the application so it
is created.

### API permissions

The **API permissions** should be set next. Konvergo ERP will need specific API
permissions to be able to read (IMAP) and send (SMTP) emails in the Microsoft
365 setup. First, click the **API permissions** link, located in the left menu
bar. Next, click on the **(+) Add a Permission** button and select **Microsoft
Graph** under **Commonly Used Microsoft APIs**. After, select the **Delegated
Permissions** option.

In the search bar, search for the following **Delegated permissions** and
click **Add permissions** for each one:

  * **SMTP.Send**

  * **IMAP.AccessAsUser.All**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>User.Read</b> permission will be added by default.</p>
</div> ![API permissions needed for Konvergo ERP integration are listed
under the Microsoft Graph.](../../../_images/permissions.png)

## Assign users and groups

After adding the API permissions, navigate back to the **Overview** of the
**Application** in the top of the left sidebar menu.

Now, add users to this application. Under the **Essentials** overview table,
click on the link labeled **Managed Application in Local Directory** , or the
last option on the bottom right-hand side of the table.

![Add users/groups by clicking the Managed application in local directory link
for the created application.](../../../_images/managed-application.png)

In the left sidebar menu, select **Users and Groups**. Next, click on **(+)
Add User/Group**. Depending on the account, either a **Group** and a **User**
can be added, or only **Users**. Personal accounts will only allow for
**Users** to be added.

Under **Users** or **Groups** , click on **None Selected** and add the users
or group of users that will be sending emails from the **Microsoft account**
in Konvergo ERP. **Add** the users/groups, click **Select** , and then **Assign** them
to the application.

### Create credentials

Now that the Microsoft Azure app is set up, credentials need to be created for
the Konvergo ERP setup. These include the **Client ID** and **Client Secret**. To
start, the **Client ID** can be copied from the **Overview** page of the app.
The **Client ID** or **Application ID** is located under the **Display Name**
in the **Essentials** overview of the app.

![Application/Client ID located in the Overview of the
app.](../../../_images/application-id.png)

Next, the **Client Secret Value** needs to be retrieved. To get this value,
click on **Certificates & Secrets** in the left sidebar menu. Then, a **Client
Secret** needs to be produced. In order to do this, click on the **(+) New
Client Secret** button.

A window on the right will populate with a button labeled **Add a client
secret**. Under **Description** , type in `Konvergo ERP Fetchmail` or something
recognizable, and then set the **expiration date**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A new <b>Client Secret</b> will need to be produced and configured if the first one
expires. In this event, there could be an interruption of service, so the expiration date should
be noted and set to the furthest possible date.</p>
</div>

Next, click on **Add** when these two values are entered. A **Client Secret
Value** and **Secret ID** will be created. It is important to copy the
**Value** or **Client Secret Value** into a notepad as it will become
encrypted after leaving this page. The **Secret ID** is not needed.

![Client Secret Value or Value in the app's
credentials.](../../../_images/secretvalue.png)

After these steps, the following items should be ready to be set up in Konvergo ERP:

  * A client ID (**Client ID** or **Application ID**)

  * A client secret (**Value** or **Client Secret Value**)

This completes the setup on the **Microsoft Azure Portal** side.

## Setup in Konvergo ERP

### Enter Microsoft Outlook credentials

First, open the Konvergo ERP database and navigate to the **Apps** module. Then,
remove the **Apps** filter from the search bar and type in `Outlook`. After
that, install the module called **Microsoft Outlook**.

Next, navigate to Settings ‣ General Settings, and under the **Discuss**
section, ensure that the checkbox for **Custom Email Servers** is checked.
This populates a new option for **Outlook Credentials**.

**Save** the progress.

Then, copy and paste the **Client ID** (Application ID) and **Client Secret
(Client Secret Value)** into the respective fields and **Save** the settings.

![Outlook Credentials in Konvergo ERP General
Settings.](../../../_images/outlookcreds.png)

### Configure outgoing email server

On the **General Settings** page, under the **Custom Email Servers** setting,
click the **Outgoing Email Servers** link to configure the Microsoft account.

Then, create a new email server and check the box for **Outlook**. Next, fill
in the **Name** (it can be anything) and the Microsoft Outlook email
**Username**.

If the **From Filter** field is empty, enter either a [domain or email
address](email_servers#email-communication-default).

Then, click on **Connect your Outlook account**.

A new window from Microsoft opens to complete the **authorization process**.
Select the appropriate email address that is being configured in Konvergo ERP.

![Permission page to grant access between newly created app and
Konvergo ERP.](../../../_images/verify-outlook.png)

Then, allow Konvergo ERP to access the Microsoft account by clicking on **Yes**. After
this, the page will navigate back to the newly configured **Outgoing Mail
Server** in Konvergo ERP. The configuration automatically loads the **token** in Konvergo ERP,
and a tag stating **Outlook Token Valid** appears in green.

![Valid Outlook Token indicator.](../../../_images/outlook-token.png)

Finally, click **Test Connection**. A confirmation message should appear. The
Konvergo ERP database can now send safe, secure emails through Microsoft Outlook using
OAuth authentication.

#### Configuration with a single outgoing mail server

Configuring a single outgoing server is the simplest configuration available
for Microsoft Azure and it doesn’t require extensive access rights for the
users in the database.

A generic email address would be used to send emails for all users within the
database. For example it could be structured with a `notifications` alias
(`notifications@example.com`) or `contact` alias (`contact@example.com`). This
address must be set as the **FROM Filtering** on the server. This address must
also match the `{mail.default.from}@{mail.catchall.domain}` key combination in
the system parameters.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For more information on the from filter visit: <a href="email_servers#email-communication-default"><span class="std std-ref">Use a default “From” email address</span></a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>System Parameters</b> can be accessed by activating <a href="../developer_mode#developer-mode"><span class="std std-ref">Developer mode (debug mode)</span></a> in the
Settings ‣ Technical ‣ Parameters ‣ System Parameters menu.</p>
</div>

When using this configuration, every email that is sent from the database will
use the address of the configured `notification` mailbox. However it should be
noted that the name of the sender will appear but their email address will
change:

![Name from real sender with static email.](../../../_images/from-name-
remain.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Single outgoing mail server configuration:</p>
<ul>
<li><p>Outgoing mail server <b>username</b> (login) = <code>notifications@example.com</code></p></li>
<li><p>Outgoing mail server <b>FROM Filtering</b> = <code>notifications@example.com</code></p></li>
<li><p><code>mail.catchall.domain</code> in system parameters = <code>example.com</code></p></li>
<li><p><code>mail.default.from</code> in system parameters = <code>notifications</code></p></li>
</ul>
</div>

#### User-specific (multiple user) configuration

In addition to a generic email server, individual email servers can be set up
for users in a database. These email addresses must be set as the **FROM
Filtering** on each individual server for this configuration to work.

This configuration is the more difficult of the two Microsoft Azure
configurations, in that it requires all users configured with email servers to
have access rights to settings in order to establish a connection to the email
server.

##### Setup

Each user should have a separate email server set up. The **FROM Filtering**
should be set so that only the user’s email is sent from that server. In other
words, only a user with an email address that matches the set **FROM
Filtering** is able to use this server.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For more information on the from filter visit: <a href="email_servers#email-communication-default"><span class="std std-ref">Use a default “From” email address</span></a>.</p>
</div>

A fallback server must be setup to allow for the sending of **notifications**.
The **FROM Filtering** for this server should have the value of the
`{mail.default.from}@{mail.catchall.domain}`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>System Parameters</b> can be accessed by activating <a href="../developer_mode#developer-mode"><span class="std std-ref">Developer mode (debug mode)</span></a> in the
Settings ‣ Technical ‣ Parameters ‣ System Parameters menu.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../users/azure">Microsoft Azure sign-in authentication</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Outlook Calendar synchronization</a></p></li>
</ul>
</div>0 <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../users/azure">Microsoft Azure sign-in authentication</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Outlook Calendar synchronization</a></p></li>
</ul>
</div>2

### Configure incoming email server

The incoming account should be configured in a similar way to the outgoing
email account. Navigate to the **Incoming Mail Servers** in the **Technical
Menu** and **Create** a new configuration. Check or Select the button next to
**Outlook Oauth Authentication** and enter the **Microsoft Outlook username**.
Click on **Connect your Outlook account**. Konvergo ERP will state: **Outlook Token
Valid** Now **Test and Confirm** the account. The account should be ready to
receive email to the Konvergo ERP database.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../users/azure">Microsoft Azure sign-in authentication</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Outlook Calendar synchronization</a></p></li>
</ul>
</div>3

