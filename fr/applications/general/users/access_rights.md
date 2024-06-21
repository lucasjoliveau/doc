# Droits d’accès

_Access rights_ are permissions that determine the content and applications
users can access and edit. In Konvergo ERP, these permissions can be set for
individual users or for groups of users. Limiting permissions to only those
who need them ensures that users do not modify or delete anything they should
not have access to.

**Only** an _administrator_ can change access rights.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Making changes to access rights can have a detrimental impact on the database. This includes
<em>impotent admin</em>, which means that no user in the database can make changes to the access rights.
For this reason, Konvergo ERP recommends contacting an Konvergo ERP Business Analyst, or our Support Team, before
making changes.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>A user <b>must</b> have the specific <em>Administration</em> access rights set on their user profile, in
order to make changes on another user’s settings for access rights.</p>
<p>To access this setting, navigate to Settings app ‣ Manage users ‣ select a
user ‣ Access Rights tab ‣ Administration section ‣ Administration field.</p>
<p>Once at the setting, an already existing administrator <b>must</b> change the setting in the
<b>Administration</b> field to <b>Access Rights</b>.</p>
<p>Once complete, click <b>Save</b> to save the changes, and implement the user as an
administrator.</p>
</div>

## Utilisateurs

The access rights for [individual users](../users#users-add-individual)
are set when the user is added to the database, but they can be adjusted at
any point in the user’s profile.

To make changes to a user’s rights, click on the desired user to edit their
profile.

![Users menu in the Users & Companies section of the Settings app of
Konvergo ERP.](../../../_images/navigate-to-users-menu.png)

On the user’s profile page, in the **Access Rights** tab, scroll down to view
the current permissions.

For each app, use the drop-down menu to select what level of permission this
user should have. The options vary for each section, yet the most common are:
**Blank/None** , **User: Own Documents** , **User: All Documents** , or
**Administrator**.

The **Administration** field in the **Access Rights** tab has the following
options: **Settings** or **Access Rights**.

![The Sales apps drop-down menu to set the user's level of
permissions.](../../../_images/user-permissions-dropdown-menu.png)

## Create and modify groups

_Groups_ are app-specific sets of permissions that are used to manage common
access rights for a large amount of users. Administrators can modify the
existing groups in Konvergo ERP, or create new ones to define rules for models within
an application.

To access groups, first activate Konvergo ERP’s [developer
mode](../developer_mode#developer-mode), then go to Settings app ‣ Users
& Companies ‣ Groups.

![Groups menu in the Users & Companies section of the Settings app of
Konvergo ERP.](../../../_images/click-users-and-companies.png)

To create a new group from the **Groups** page, click **Create**. Then, from
the blank group form, select an **Application** , and complete the group form
(detailed below).

To modify existing groups, click on an existing group from the list displayed
on the **Groups** page, and edit the contents of the form.

Enter a **Name** for the group and tick the checkbox next to **Share Group** ,
if this group was created to set access rights for sharing data with some
users.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Always test the settings being changed to ensure they are being applied to the correct users.</p>
</div>

The group form contains multiple tabs for managing all elements of the group.
In each tab, click **Add a line** to add a new row for users or rules, and
click the **❌ (remove)** icon to remove a row.

![Tabs in the Groups form to modify the settings of the
group.](../../../_images/groups-form.png)

  * **Users** tab: lists the current users in the group. Users listed in black have administrative rights. Users without administrative access appear in blue. Click **Add a line** to add users to this group.

  * **Inherited** tab: inherited means that users added to this group are automatically added to the groups listed on this tab. Click **Add a line** to add inherited groups.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>For example, if the group <em>Sales/Administrator</em> lists the group <em>Website/Restricted Editor</em> in
its <b>Inherited</b> tab, then any users added to the <em>Sales/Administrator</em> group
automatically receive access to the <em>Website/Restricted Editor</em> group, as well.</p>
</div>

  * **Menus** tab: defines which menus/models the group can have access to. Click **Add a line** to add a specific menu.

  * **Views** tab: lists which views in Konvergo ERP the group has access to. Click **Add a line** to add a view to the group.

  * **Access Rights** tab: lists the first level of rights (models) that this group has access rights to. Click **Add a line** to link access rights to this group. In this tab, the **Model** column represents the common name of the menu/model, and the **Name** column represents the technical name given to the model. For each model, enable the following options as appropriate:

    * **Read** : users can see the object’s existing values.

    * **Write** : users can edit the object’s existing values.

    * **Create** : users can create new values for the object.

    * **Delete** : users can delete values for the object.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>First try searching for the common name of the model in the drop-down menu of the
<b>Model</b> column. The <b>Model</b> technical name can be found by expanding the
model common name, which can be done by clicking the <b>(external link)</b> icon.</p>
<p>The model technical name can also be accessed in <a href="../developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>.</p>
<p>On a form, navigate to any field, and hover over the field name. A box of backend information
reveals itself with the specific Konvergo ERP <b>Object</b> name in the backend. This is the
technical name of the model that should be added.</p>
<img alt="Technical information shown on a field of a model, with object highlighted." class="align-center" src="../../../_images/technical-info.png"/>
</div>

  * **Record Rules** : lists the second layer of editing and visibility rights. **Record Rules** overwrite, or refine, the group’s access rights. Click **Add a line** to add a record rule to this group. For each rule, choose values for the following options:

    * **Apply for Read**.

    * **Apply for Write**.

    * **Apply for Create**.

    * **Apply for Delete**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Record rules are written using a <em>domain</em>, or conditions that filter data. A domain expression
is a list of such conditions. For example:</p>
<p><code>[('mrp_production_ids', 'in', user.partner_id.commercial_partner_id.production_ids.ids)]</code></p>
<p>This record rule is to enable MRP consumption warnings for subcontractors.</p>
<p>Konvergo ERP has a library of preconfigured record rules for ease of use. Users without knowledge of
domains (and domain expressions) should consult an Konvergo ERP Business Analyst, or the Konvergo ERP Support
Team, before making changes.</p>
</div>

## Superuser mode

_Superuser mode_ allows the user to bypass record rules and access rights. To
activate _Superuser mode_ , first, activate [developer
mode](../developer_mode#developer-mode). Then, navigate to the _debug_
menu, represented by a **🪲 (bug)** icon, located in the top banner.

Finally, towards the bottom of the menu, click **Become Superuser**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Only users with <em>Settings</em> access for the <em>Administration</em> section of the <em>Access Rights</em> (in
their user profile) are allowed to log in to <em>Superuser mode</em>.</p>
</div> <div class="alert alert-danger">
<p class="alert-title">
Danger</p><p><em>Superuser mode</em> allows for circumvention of record rules and access rights, and therefore,
should be exercised with extreme caution.</p>
<p>Upon exiting <em>Superuser mode</em>, users may be locked out of the database, due to changes that were
made. This can cause <em>impotent admin</em>, or an administrator without the ability to change access
rights/settings.</p>
<p>In this case contact Konvergo ERP Support here: <a href="https://www.odoo.com/help">new help ticket</a>. The
support team is able to restore access using a support login.</p>
</div>

To leave _Superuser mode_ , log out of the account, by navigating to the
upper-right corner, and clicking on the **Konvergo ERPBot** username. Then, select the
**Log out** option.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>An alternative way to activate <em>Superuser mode</em> is to login as a superuser. To do that, navigate
to the login screen, and enter the appropriate <b>Email</b> and <b>Password</b>.</p>
<p>Instead of clicking <b>Login</b>, click <b>Log in as superuser</b>.</p>
</div>

