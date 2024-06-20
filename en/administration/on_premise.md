# On-premise

## Register a database

To register your database, enter your subscription code in the banner in the
app dashboard. If the registration is successful, the banner will turn green
and display the database expiration date.

Tip

The expiration date is also displayed at the bottom of the Settings page.

## Duplicate a database

Duplicate a database by accessing the database manager on your server (`<odoo-
server>/web/database/manager`). Typically, you want to duplicate your
production database into a neutralized testing database. It can be done by
checking the neutralize box when prompted, which executes all `neutralize.sql`
scripts for every installed module.

## Common error messages and solutions

### Registration error

In case of a registration error, the following message should be displayed.

![Database registration error message](../_images/error-message-sub-code.png)

To resolve the issue:

  * Check the **validity of your Odoo Enterprise subscription** by verifying if your subscription details have the tag In Progress on your [Odoo Account](https://accounts.odoo.com/my/subscription) or contact your Account Manager.

  * Ensure that **no other database is linked** to the subscription code, as only one database can be linked per subscription.

Tip

If a test or a development database is needed, you can duplicate a database.

  * Verify that **no databases share the same UUID** (Universally Unique Identifier) by opening your [Odoo Contract](https://accounts.odoo.com/my/subscription). If two or more databases share the same UUID, their name will be displayed.

![Database UUID error message](../_images/unlink-db-name-collision.png)

If that is the case, manually change the database(s) UUID or [send a support
ticket](https://www.odoo.com/help).

  * As the update notification must be able to reach Odoo’s subscription validation servers, ensure your **network and firewall settings** allow the Odoo server to open outgoing connections towards:

    * `services.odoo.com` on port `443` (or `80`)

    * for older deployments, `services.openerp.com` on port `443` (or `80`)

These ports must be kept open even after registering a database, as the update
notification runs once a week.

### Too many users error

If you have more users in a local database than provisioned in your Odoo
Enterprise subscription, the following message should be displayed.

![Too many users on a database error message](../_images/add-more-users.png)

When the message appears, you have 30 days to act before the database expires.
The countdown is updated every day.

To resolve the issue, either:

  * **Add more users** to your subscription by clicking the Upgrade your subscription link displayed in the message to validate the upsell quotation and pay for the extra users.

  * [Deactivate users](../applications/general/users.html#users-deactivate) and **reject** the upsell quotation.

Important

If you are on a monthly subscription plan, the database will automatically
update to reflect the added user(s). If you are on a yearly or multi-year
plan, an expiration banner will appear in the database. You can create the
upsell quotation by clicking the banner to update the subscription or [send a
support ticket](https://www.odoo.com/help) to resolve the issue.

Once your database has the correct number of users, the expiration message
disappears automatically after a few days, when the next verification occurs.

### Database expired error

If your database expires before you renew your subscription, the following
message should be displayed.

![Database expired error message](../_images/database-expired.png)

This message appears if you fail to act before the end of the 30-day
countdown.

To resolve the issue, either:

  * Click the Renew your subscription link displayed in the message and complete the process. If you pay by wire transfer, your subscription will be renewed when the payment arrives which can take a few days. Credit card payments are processed immediately.

  * [Send a support ticket](https://www.odoo.com/help).

  * Packaged installers
    * Linux
      * [Prepare](on_premise/packages.html#prepare)
      * [Repository](on_premise/packages.html#repository)
      * [Distribution package](on_premise/packages.html#distribution-package)
    * [Windows](on_premise/packages.html#windows)
  * Source install
    * Fetch the sources
      * [Archive](on_premise/source.html#archive)
      * [Git](on_premise/source.html#git)
    * Prepare
      * [Python](on_premise/source.html#python)
      * [PostgreSQL](on_premise/source.html#postgresql)
      * [Dependencies](on_premise/source.html#dependencies)
    * [Running Odoo](on_premise/source.html#running-odoo)
  * Bugfix updates
    * [Introduction](on_premise/update.html#introduction)
    * [In a nutshell](on_premise/update.html#in-a-nutshell)
    * [Step 1: Download an updated Odoo version](on_premise/update.html#step-1-download-an-updated-odoo-version)
    * [Step 2: Make a backup of your database](on_premise/update.html#step-2-make-a-backup-of-your-database)
    * Step 3: Install the updated version
      * [Packaged Installers](on_premise/update.html#packaged-installers)
      * [Source Install (Tarball)](on_premise/update.html#source-install-tarball)
      * [Source Install (Github)](on_premise/update.html#source-install-github)
      * [Docker](on_premise/update.html#docker)
  * System configuration
    * dbfilter
      * [Configuration samples](on_premise/deploy.html#configuration-samples)
    * PostgreSQL
      * [Configuration sample](on_premise/deploy.html#configuration-sample)
      * Configuring Odoo
        * [Configuration sample](on_premise/deploy.html#id3)
      * [SSL Between Odoo and PostgreSQL](on_premise/deploy.html#ssl-between-odoo-and-postgresql)
    * Builtin server
      * [Worker number calculation](on_premise/deploy.html#worker-number-calculation)
      * [memory size calculation](on_premise/deploy.html#memory-size-calculation)
      * [LiveChat](on_premise/deploy.html#livechat)
      * [Configuration sample](on_premise/deploy.html#id5)
    * HTTPS
      * [Configuration sample](on_premise/deploy.html#id7)
      * [HTTPS Hardening](on_premise/deploy.html#https-hardening)
    * Odoo as a WSGI Application
      * [Cron Workers](on_premise/deploy.html#cron-workers)
      * [LiveChat](on_premise/deploy.html#id8)
    * Serving static files and attachments
      * [Serving static files](on_premise/deploy.html#serving-static-files)
      * [Serving attachments](on_premise/deploy.html#serving-attachments)
    * Security
      * [Blocking Brute Force Attacks](on_premise/deploy.html#blocking-brute-force-attacks)
      * [Database Manager Security](on_premise/deploy.html#database-manager-security)
      * Reset the master password
        * [Locate configuration file](on_premise/deploy.html#locate-configuration-file)
        * [Change old password](on_premise/deploy.html#change-old-password)
        * [Restart Odoo server](on_premise/deploy.html#restart-odoo-server)
        * [Use web interface to re-encrypt password](on_premise/deploy.html#use-web-interface-to-re-encrypt-password)
    * [Supported Browsers](on_premise/deploy.html#supported-browsers)
  * Email gateway
    * [Prerequisites](on_premise/email_gateway.html#prerequisites)
    * [For Postfix](on_premise/email_gateway.html#for-postfix)
    * [For Exim](on_premise/email_gateway.html#for-exim)
  * Geo IP
    * [Installation](on_premise/geo_ip.html#installation)
    * [How to test GeoIP geolocation in your Odoo website](on_premise/geo_ip.html#how-to-test-geoip-geolocation-in-your-odoo-website)
  * Switch from Community to Enterprise
    * [On Linux, using an installer](on_premise/community_to_enterprise.html#on-linux-using-an-installer)
    * [On Linux, using the source code](on_premise/community_to_enterprise.html#on-linux-using-the-source-code)
    * [On Windows](on_premise/community_to_enterprise.html#on-windows)

