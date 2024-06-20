# Hosting

## Change hosting solution

The instructions to change the hosting type of a database depend on the
current solution used and to which solution the database should be moved.

## Transferring an on-premise database

### To Odoo Online

Important

  * Odoo Online is _not_ compatible with **non-standard apps**.

  * The database’s current version must be [supported](supported_versions.html).

  1. Create a [duplicate of the database](on_premise.html#on-premise-duplicate).

  2. In this duplicate, uninstall all **non-standard apps**.

  3. Use the database manager to grab a _dump with filestore_.

  4. [Submit a support ticket](https://www.odoo.com/help) including the following:

     * your **subscription number** ,

     * the **URL** you want to use for the database (e.g., `company.odoo.com`), and

     * the **dump** as an attachment or as a link to the file (required for 60 MB+ files).

  5. Odoo then makes sure the database is compatible before putting it online. In case of technical issues during the process, Odoo might contact you.

Note

If you have time constraints, [submit a support
ticket](https://www.odoo.com/help) as soon as possible to schedule the
transfer.

### To Odoo.sh

Follow the instructions found in [the Import your database
section](odoo_sh/getting_started/create.html#odoo-sh-import-your-database) of
the Odoo.sh _Create your project_ documentation.

## Transferring an Odoo Online database

Important

Odoo Online’s [intermediary versions](supported_versions.html#supported-
versions) are not supported by Odoo.sh or on-premise. Therefore, if the
database to transfer is running an intermediary version, it must be upgraded
first to the next [major version](supported_versions.html#supported-versions),
waiting for its release if necessary.

Example

Transferring an online database running on Odoo 16.3 would require first
upgrading it to Odoo 17.0.

Tip

Click the gear icon (⚙) next to the database name on the [Odoo Online database
manager](https://www.odoo.com/my/databases/) to display its version number.

Warning

If there is an active Odoo subscription linked to the database being migrated,
reach out to the Customer Service Manager or [submit a support
ticket](https://www.odoo.com/help) to complete the subscription transfer.

### To on-premise

  1. Sign in to [the Odoo Online database manager](https://www.odoo.com/my/databases/) and click the gear icon (⚙) next to the database name to Download a backup. If the download fails due to the file being too large, [contact Odoo support](https://www.odoo.com/help).

  2. Restore the database from the database manager on your local server using the backup.

### To Odoo.sh

  1. Sign in to [the Odoo Online database manager](https://www.odoo.com/my/databases/) and click the gear icon (⚙) next to the database name to Download a backup. If the download fails due to the file being too large, [contact Odoo support](https://www.odoo.com/help).

  2. Follow the instructions found in [the Import your database section](odoo_sh/getting_started/create.html#odoo-sh-import-your-database) of the Odoo.sh _Create your project_ documentation.

## Transferring an Odoo.sh database

### To Odoo Online

Important

Odoo Online is _not_ compatible with **non-standard apps**.

  1. Uninstall all **non-standard apps** in a staging build before doing it in the production build.

  2. [Create a support ticket](https://www.odoo.com/help) including the following:

     * your **subscription number** ,

     * the **URL** you want to use for the database (e.g., `company.odoo.com`),

     * which **branch** should be migrated,

     * in which **region** you want the database to be hosted (Americas, Europe, or Asia),

     * which user(s) will be the **administrator(s)** , and

     * **when** (and in which timezone) you want the database to be up and running.

  3. Odoo then makes sure the database is compatible before putting it online. In case of technical issues during the process, Odoo might contact you.

Note

  * If you have time constraints, [submit a support ticket](https://www.odoo.com/help) as soon as possible to schedule the transfer.

  * Select the **region** closest to most of your users to reduce latency.

  * Future **administrator(s)** must have an Odoo.com account.

  * The **date and time** you want the database to be up and running are helpful to organize the switch from the Odoo.sh server to the Odoo Online servers.

  * Databases are **not reachable** during their migration.

### To on-premise

  1. Download a [backup of your Odoo.sh production database](odoo_sh/getting_started/branches.html#odoo-sh-branches-backups).

  2. Restore the database from the database manager on your local server using the backup.

