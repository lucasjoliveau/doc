# Konvergo ERP Online

[Konvergo ERP Online](https://www.odoo.com/trial) provides private databases which are
fully managed and hosted by Konvergo ERP. It can be used for long-term production or
to test Konvergo ERP thoroughly, including customizations that don’t require code.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP Online is incompatible with custom modules or the Konvergo ERP App Store.</p>
</div>

Konvergo ERP Online databases are accessed using any web browser and do not require a
local installation.

To quickly try out Konvergo ERP, shared [demo](https://demo.odoo.com) instances are
available. No registration is required, but each instance only lives for a few
hours.

## Database management

To manage a database, go to the [database
manager](https://www.odoo.com/my/databases) and sign in as the database
administrator.

All the main database management options are available by clicking the
database name, except the upgrade option, which can be accessed by clicking
the **arrow in a circle** icon next to the database name. It is only displayed
if an upgrade is available.

![Accessing the database management options](../_images/database-manager.png)

  * Upgrade

  * Duplicate

  * Rename

  * Download

  * Domain names

  * Tags

  * Delete

  * Contact us

  * Invite / remove users

## Upgrade

Trigger a database upgrade.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For more information about the upgrade process, check out the <a href="upgrade#upgrade-request-test-database"><span class="std std-ref">Konvergo ERP Online upgrade
documentation</span></a>.</p>
</div>

## Duplicate

Create an exact copy of the database, which can be used to perform testing
without compromising daily operations.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>By checking <b>For testing purposes</b>, all external actions (emails, payments, delivery
orders, etc.) are disabled by default on the duplicated database.</p></li>
<li><p>Duplicated databases expire automatically after 15 days.</p></li>
<li><p>A maximum of five duplicates can be made per database. Under extraordinary circumstances,
contact <a href="https://www.odoo.com/help">support</a> to raise the limit.</p></li>
</ul>
</div>

## Rename

Rename the database and its URL.

## Download

Download a ZIP file containing a backup of the database.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Databases are backed up daily as per the <a href="https://www.odoo.com/cloud-sla">Konvergo ERP Cloud Hosting SLA</a>.</p>
</div>

## Domain names

Use a custom [domain
name](../applications/websites/website/configuration/domain_names) to
access the database via another URL.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can <a href="../applications/websites/website/configuration/domain_names#domain-name-register"><span class="std std-ref">register a domain name for free</span></a>.</p>
</div>

## Tags

Add tags to easily identify and sort your databases.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can search for tags in the search bar.</p>
</div>

## Delete

Delete a database instantly.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Deleting a database means that all data is permanently lost. The deletion is instant and applies
to all users. It is recommended to create a backup of the database before deleting it.</p>
</div>

Carefully read the warning message and only proceed if the implications of
deleting a database are fully understood.

![The warning message displayed before deleting a
database](../_images/delete.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Only an administrator can delete a database.</p></li>
<li><p>The database name is immediately made available to anyone.</p></li>
<li><p>Deleting a database if it has expired or is linked to a subscription is impossible. In that
case, contact <a href="https://www.odoo.com/help">Konvergo ERP Support</a>.</p></li>
</ul>
</div>

## Contact us

Access the [Konvergo ERP.com support page](https://www.odoo.com/help) with the
database’s details already pre-filled.

## Invite / remove users

To invite users, fill out the new user’s email address and click **Invite**.
To add multiple users, click **Add more users**.

![Inviting a user on a database](../_images/invite-users.png)

To remove users, select them and click **Remove**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../applications/general/users">Users</a></p></li>
<li><p><a href="odoo_accounts">Konvergo ERP.com accounts</a></p></li>
</ul>
</div>

