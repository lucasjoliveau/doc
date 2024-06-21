# Microsoft Azure sign-in authentication

The Microsoft Azure OAuth sign-in authentication is a useful function that
allows Konvergo ERP users to sign in to their database with their Microsoft Azure
account.

This is particularly helpful if the organization uses Azure Workspace, and
wants employees within the organization to connect to Konvergo ERP using their
Microsoft Accounts.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Databases hosted on Konvergo ERP.com should not use OAuth login for the owner or administrator of the
database as it would unlink the database from their Konvergo ERP.com account. If OAuth is set up for that
user, the database will no longer be able to be duplicated, renamed, or otherwise managed from
the Konvergo ERP.com portal.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../productivity/calendar/outlook">Outlook Calendar synchronization</a></p></li>
<li><p><a href="../email_communication/azure_oauth">Connect Microsoft Outlook 365 to Konvergo ERP using Azure OAuth</a></p></li>
</ul>
</div>

## Configuration

Integrating the Microsoft sign-in function requires configuration on Microsoft
and Konvergo ERP.

### Konvergo ERP System Parameter

First activate the [developer mode](../developer_mode#developer-mode),
and then go to Settings ‣ Technical ‣ System Parameters.

Click **Create** and on the new/blank form that appears, add the following
system parameter `auth_oauth.authorization_header` to the **Key** field, and
set the **Value** to `1`. Then click **Save** to finish.

### Microsoft Azure dashboard

#### Create a new application

Now that the system parameters in Konvergo ERP have been set up, it’s time to create a
corresponding application inside of Microsoft Azure. To get started creating
the new application, go to [Microsoft’s Azure
Portal](https://portal.azure.com/). Log in with the **Microsoft Outlook Office
365** account if there is one, otherwise, log in with a personal **Microsoft
account**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A user with administrative access to the <em>Azure Settings</em> must connect and perform the following
configuration steps below.</p>
</div>

Next, navigate to the section labeled **Manage Microsoft Entra ID** (formally
_Azure Active Directory_). The location of this link is usually in the center
of the page.

Now, click on the **Add (+)** icon, located in the top menu, and then select
**App registration** from the drop-down menu. On the **Register an
application** screen, rename the **Name** field to `Konvergo ERP Login OAuth` or a
similarly recognizable title. Under the **Supported account types** section
select the option for **Accounts in this organizational directory only
(Default Directory only - Single tenant)**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The <b>Supported account types</b> can vary by Microsoft account type and end use of the
OAuth. For example: Is the login meant for internal users within one organization or is it meant
for customer portal access? The above configuration is used for internal users in an
organization.</p>
<p>Choose <b>Personal Microsoft accounts only</b> if the target audience is meant for portal
users. Choose <b>Accounts in this organizational directory only (Default Directory only -
Single tenant)</b> if the target audience is company users.</p>
</div>

Under the **Redirect URL** section, select **Web** as the platform, and then
input `https://<odoo base url>/auth_oauth/signin` in the **URL** field. The
Konvergo ERP base URL is the canonical domain at which your Konvergo ERP instance can be
reached (e.g. _mydatabase.odoo.com_ if you are hosted on Konvergo ERP.com) in the
**URL** field. Then, click **Register** , and the application is created.

#### Authentication

Edit the new app’s authentication by clicking on the **Authentication** menu
item in the left menu after being redirected to the application’s settings
from the previous step.

Next, the type of _tokens_ needed for the OAuth authentication will be chosen.
These are not currency tokens but rather authentication tokens that are passed
between Microsoft and Konvergo ERP. Therefore, there is no cost for these tokens; they
are used merely for authentication purposes between two APIs. Select the
tokens that should be issued by the authorization endpoint by scrolling down
the screen and check the boxes labeled: **Access tokens (used for implicit
flows)** and **ID tokens (used for implicit and hybrid flows)**.

![Authentication settings and endpoint
tokens.](../../../_images/authentication-tokens.png)

Click **Save** to ensure these settings are saved.

#### Gather credentials

With the application created and authenticated in the Microsoft Azure console,
credentials will be gathered next. To do so, click on the **Overview** menu
item in the left-hand column. Select and copy the **Application (client) ID**
in the window that appears. Paste this credential to a clipboard / notepad, as
this credential will be used in the Konvergo ERP configuration later.

After finishing this step, click on **Endpoints** on the top menu and click
the _copy icon_ next to **OAuth 2.0 authorization endpoint (v2)** field. Paste
this value in the clipboard / notepad.

![Application ID and OAuth 2.0 authorization endpoint \(v2\)
credentials.](../../../_images/overview-azure-app.png)

### Konvergo ERP setup

Finally, the last step in the Microsoft Azure OAuth configuration is to
configure some settings in Konvergo ERP. Navigate to Settings ‣ Integrations ‣ OAuth
Authentication and check the box to activate the OAuth login feature. Click
**Save** to ensure the progress is saved. Then, sign in to the database once
the login screen loads.

Once again, navigate to Settings ‣ Integrations ‣ OAuth Authentication and
click on **OAuth Providers**. Now, select **New** in the upper-left corner and
name the provider `Azure`.

Paste the **Application (client) ID** from the previous section into the
**Client ID** field. After completing this, paste the new **OAuth 2.0
authorization endpoint (v2)** value into the **Authorization URL** field.

For the **UserInfo URL** field, paste the following URL:
`https://graph.microsoft.com/oidc/userinfo`

In the **Scope** field, paste the following value: `openid profile email`.
Next, the Windows logo can be used as the CSS class on the login screen by
entering the following value: `fa fa-fw fa-windows`, in the **CSS class**
field.

Check the box next to the **Allowed** field to enable the OAuth provider.
Finally, add `Microsoft Azure` to the **Login button label** field. This text
will appear next to the Windows logo on the login page.

![Konvergo ERP provider setup in the Settings application.](../../../_images/odoo-
provider-settings.png)

**Save** the changes to complete the OAuth authentication setup in Konvergo ERP.

### User experience flows

For a user to log in to Konvergo ERP using Microsoft Azure, the user must be on the
Konvergo ERP password reset page. This is the only way that Konvergo ERP is able to link the
Microsoft Azure account and allow the user to log in.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Existing users must <a href="../users#users-reset-password"><span class="std std-ref">reset their password</span></a> to access the
Konvergo ERP password reset page. New Konvergo ERP users must click the new user invitation link
that was sent via email, then click on <b>Microsoft Azure</b>. Users should not set a new
password.</p>
</div>

To sign in to Konvergo ERP for the first time using the Microsoft Azure OAuth
provider, navigate to the Konvergo ERP password reset page (using the new user
invitation link). A password reset page should appear. Then, click on the
option labeled **Microsoft Azure**. The page will redirect to the Microsoft
login page.

![Microsoft Outlook login page.](../../../_images/odoo-login.png)

Enter the **Microsoft Email Address** and click **Next**. Follow the process
to sign in to the account. Should 2FA be turned on, then an extra step may be
required.

![Enter Microsoft login credentials.](../../../_images/login-next.png)

Finally, after logging in to the account, the page will redirect to a
permissions page where the user will be prompted to **Accept** the conditions
that the Konvergo ERP application will access their Microsoft information.

![Accept Microsoft conditions for permission access to your account
information.](../../../_images/accept-access.png)

  *[URL]: Uniform Resource Locator
  *[APIs]: application programming interfaces
  *[2FA]: Two Factor Authentication

