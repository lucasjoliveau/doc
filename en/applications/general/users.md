# Users

Konvergo ERP defines a _user_ as someone who has access to a database. An
administrator can add as many users as the company needs and, in order to
restrict the type of information each user can access, rules can be applied to
each user. Users and access rights can be added and changed at any point.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="users/language">Change language</a></p></li>
<li><p><a href="users/access_rights">Access rights</a></p></li>
<li><p><a href="users/access_rights#access-rights-superuser"><span class="std std-ref">Superuser mode</span></a></p></li>
<li><p><a href="users/access_rights#access-rights-groups"><span class="std std-ref">Create and modify groups</span></a></p></li>
</ul>
</div>

## Add individual users

To add new users, navigate to Settings app ‣ Users section ‣ Manage Users, and
click on **Create**.

![View of the settings page emphasizing the manage users field in
Konvergo ERP.](../../_images/manage-users.png)

Fill in the form with all the required information. Under the [Access
Rights](users/access_rights) tab, choose the group within each
application the user can have access to.

The list of applications shown is based on the applications installed on the
database.

![View of a user's form emphasizing the access rights tab in
Konvergo ERP.](../../_images/new-user.png)

After filling out all the necessary fields on the page, click **Save**. An
invitation email is automatically sent to the user, using the email in the
**Email Address** field. The user must click on the link included in the email
to accept the invitation, and to create a database login.

![View of a user's form with a notification that the invitation email has been
sent in Konvergo ERP.](../../_images/invitation-email.png) <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If the company is on a monthly subscription plan, the database automatically updates to reflect
the added users. If the company is on a yearly or multi-year plan, an expiration banner appears
in the database. An upsell quotation can be created by clicking the banner to update the
subscription. Alternatively, <a href="https://www.odoo.com/help">send a support ticket</a> to resolve the
issue.</p>
</div>

### User type

With the [developer mode](developer_mode#developer-mode) activated,
**User Type** can be selected from the **Access Rights** tab of the user form,
accessible via Settings app ‣ Users section ‣ Manage Users.

There are three types of users: **Internal User** , **Portal** , and
**Public**.

![View of a user's form in developer mode emphasizing the user type field in
Konvergo ERP.](../../_images/user-type.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Users are considered internal database users. Portal users are external users, who only have
access to the database portal to view records. See the documentation on <a href="users/portal">Portal access</a>.</p>
<p>Public users are those visiting websites, via the website’s frontend.</p>
</div>

The **Portal** and **Public** user options do **not** allow the administrator
to choose access rights. These users have specific access rights pre-set (such
as, record rules and restricted menus), and usually do not belong to the usual
Konvergo ERP groups.

## Deactivate users

To deactivate (i.e. archive) a user, navigate to Settings app ‣ Users section
‣ Manage Users. Then, tick the checkbox to the left of the user(s) to be
deactivated.

After selecting the appropriate user to be archived, click the **⚙️ Actions**
icon, and select **Archive** from the resulting drop-down menu. Then, click
**OK** from the **Confirmation** pop-up window that appears.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p><b>Never</b> deactivate the main/administrator user (admin). Making changes to admin users can have
a detrimental impact on the database. This includes <em>impotent admin</em>, which means that no user in
the database can make changes to the access rights. For this reason, Konvergo ERP recommends contacting
an Konvergo ERP Business Analyst, or our Support Team, before making changes.</p>
</div>

### Error: too many users

If there are more users in an Konvergo ERP database than provisioned in the Konvergo ERP
Enterprise subscription, the following message is displayed.

![Too many users on a database error message.](../../_images/add-more-
users1.png)

When the message appears, the database administrator has 30 days to act before
the database expires. The countdown is updated every day.

To resolve the issue, either:

  * Add more users to the subscription by clicking the **Upgrade your subscription** link displayed in the message to validate the upsell quotation, and pay for the extra users.

  * Deactivate users, and reject the upsell quotation.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If the company is on a monthly subscription plan, the database automatically updates to reflect
the added users. If the company is on a yearly or multi-year plan, an expiration banner appears
in the database. An upsell quotation can be created by clicking the banner to update the
subscription. Alternatively, users can <a href="https://www.odoo.com/help">send a support ticket</a> to
resolve the issue.</p>
</div>

Once the database has the correct number of users, the expiration message
disappears automatically after a few days, when the next verification occurs.

## Password management

Password management is an important part of granting users autonomous access
to the database at all times. Konvergo ERP offers a few different methods to reset a
user’s password.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Konvergo ERP has a setting to specify the length needed for a password. This setting can be accessed by
navigating to Settings app ‣ Permissions section, and entering the desired
password length in the <b>Minimum Password Length</b> field. By default the value is <code>8</code>.</p>
</div> ![Minimum Password Length highlighted in the Permissions
section of General Settings.](../../_images/minimum-password-length.png)

### Reset password

Sometimes, users might wish to reset their personal password for added
security, so they are the only ones with access to the password. Konvergo ERP offers
two different reset options: one initiated by the user to reset the password,
and another where the administrator triggers a reset.

#### Enable password reset from login page

It is possible to enable/disable password resets directly from the login page.
This action is completed by the individual user, and this setting is enabled
by default.

To change this setting, go to Settings app ‣ Permissions section, activate
**Password Reset** , and then click **Save**.

![Enabling Password Reset in Konvergo ERP Settings](../../_images/password-reset-
login.png)

On the login page, click **Reset Password** to initiate the password reset
process, and have a reset-token sent to the email on file.

![Login screen on Konvergo ERP.com with the password reset option
highlighted.](../../_images/password-reset.png)

#### Send reset instructions

Go to Settings app ‣ Users & Companies ‣ Users, select the user from the list,
and click on **Send Password Reset Instructions** on the user form. An email
is automatically sent to them with password reset instructions.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Send Password Reset Instructions</b> button <b>only</b> appears if the Konvergo ERP invitation
email has already been confirmed by the user. Otherwise, a <b>Re-send Invitation Email</b>
button appears.</p>
</div>

This email contains all the instructions needed to reset the password, along
with a link redirecting the user to an Konvergo ERP login page.

![Example of an email with a password reset link for an Konvergo ERP
account.](../../_images/password-reset-email.png)

### Change user password

Go to Settings app ‣ Users & Companies ‣ Users, and select a user to access
its form. Click on the **⚙️ Actions** icon, and select **Change Password**
from, the resulting drop-down menu. Enter a new password in the **New
Password** column of the **Change Password** pop-up window that appears, and
confirm the change by clicking **Change Password**.

![Change a user's password on Konvergo ERP.](../../_images/change-password.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This operation only modifies the password of the users locally, and does <b>not</b> affect their
odoo.com account.</p>
<p>If the odoo.com password needs to be changed, use the <a href="#users-reset-password-email"><span class="std std-ref">send the password reset instructions</span></a>. Konvergo ERP.com passwords grant access to the <em>My Databases</em> page, and
other portal features.</p>
</div>

After clicking **Change Password** , the page is redirected to an Konvergo ERP login
page where the database can be re-accessed using the new password.

## Multi Companies

The **Multi Companies** field on a user form allows an administrator to
provide access to multiple companies for existing users. To configure a multi-
company environment for a user, navigate to the desired user by going to:
Settings app ‣ Users section ‣ Manage users. Then, select the user to open
their user form, and configure with multi-company access.

Under **Multi Companies** in the **Access Rights** tab, set the fields labeled
**Allowed Companies** and **Default Company**.

The **Allowed Companies** field can contain multiple companies. These are the
companies the user can access and edit, according to the set access rights.
The **Default Company** is the company the user defaults to, upon logging in
each time. This field can contain only **one** company.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If multi-company access is not configured correctly, it could lead to inconsistent multi-company
behaviors. Because of this, only experienced Konvergo ERP users should make access rights changes to
users for databases with a multi-company configuration. For technical explanations, refer to the
developer documentation on <a href="../../developer/howtos/company">Multi-company Guidelines</a>.</p>
</div> ![View of a user's form emphasizing the multi companies
field in Konvergo ERP.](../../_images/multi-companies.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="companies">Companies</a></p>
</div>

  * [Change language](users/language)
  * [Two-factor Authentication](users/2fa)
  * [Access rights](users/access_rights)
  * [Portal access](users/portal)
  * [Google Sign-In Authentication](users/google)
  * [Microsoft Azure sign-in authentication](users/azure)
  * [Sign in with LDAP](users/ldap)

