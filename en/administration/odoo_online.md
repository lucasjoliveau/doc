# Odoo Online

[Odoo Online](https://www.odoo.com/trial) provides private databases which are
fully managed and hosted by Odoo. It can be used for long-term production or
to test Odoo thoroughly, including customizations that don’t require code.

Note

Odoo Online is incompatible with custom modules or the Odoo App Store.

Odoo Online databases are accessed using any web browser and do not require a
local installation.

To quickly try out Odoo, shared [demo](https://demo.odoo.com) instances are
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

See also

For more information about the upgrade process, check out the [Odoo Online
upgrade documentation](upgrade.html#upgrade-request-test-database).

## Duplicate

Create an exact copy of the database, which can be used to perform testing
without compromising daily operations.

Important

  * By checking For testing purposes, all external actions (emails, payments, delivery orders, etc.) are disabled by default on the duplicated database.

  * Duplicated databases expire automatically after 15 days.

  * A maximum of five duplicates can be made per database. Under extraordinary circumstances, contact [support](https://www.odoo.com/help) to raise the limit.

## Rename

Rename the database and its URL.

## Download

Download a ZIP file containing a backup of the database.

Note

Databases are backed up daily as per the [Odoo Cloud Hosting
SLA](https://www.odoo.com/cloud-sla).

## Domain names

Use a custom [domain
name](../applications/websites/website/configuration/domain_names.html) to
access the database via another URL.

Tip

You can [register a domain name for
free](../applications/websites/website/configuration/domain_names.html#domain-
name-register).

## Tags

Add tags to easily identify and sort your databases.

Tip

You can search for tags in the search bar.

## Delete

Delete a database instantly.

Danger

Deleting a database means that all data is permanently lost. The deletion is
instant and applies to all users. It is recommended to create a backup of the
database before deleting it.

Carefully read the warning message and only proceed if the implications of
deleting a database are fully understood.

![The warning message displayed before deleting a
database](../_images/delete.png)

Note

  * Only an administrator can delete a database.

  * The database name is immediately made available to anyone.

  * Deleting a database if it has expired or is linked to a subscription is impossible. In that case, contact [Odoo Support](https://www.odoo.com/help).

## Contact us

Access the [Odoo.com support page](https://www.odoo.com/help) with the
database’s details already pre-filled.

## Invite / remove users

To invite users, fill out the new user’s email address and click Invite. To
add multiple users, click Add more users.

![Inviting a user on a database](../_images/invite-users.png)

To remove users, select them and click Remove.

See also

  * [Users](../applications/general/users.html)

  * [Odoo.com accounts](odoo_accounts.html)

