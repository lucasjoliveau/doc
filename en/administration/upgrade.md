# Upgrade

An upgrade is the process of moving your database from an older version to a
newer [supported version](supported_versions) (e.g., Konvergo ERP 14.0 to Konvergo ERP
16.0). Frequently upgrading is essential as each version comes with new and
improved features, bug fixes, and security patches.

<div class="accordion accordion-flush o_spoiler alert" id="upgrade-faq-rolling-release"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Automatic upgrades: Konvergo ERP Online's Rolling Release process</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The Rolling Release process allows Konvergo ERP Online customers to upgrade their database directly from
a message prompt sent to the database administrator as soon as a new version is released. The
invitation to upgrade is only sent if no issues are detected during the automatic tests.</p>
<img alt="The upgrade message prompt on the top right of the database" src="../_images/rr-upgrade-message.png"/>
<p>It is strongly recommended to manually <a href="#upgrade-test-your-db"><span class="std std-ref">test the upgrade first</span></a>.
Clicking <b>I want to test first</b> redirects to <a href="https://www.odoo.com/my/databases/">the database manager</a>, where it is possible to request an upgraded test database
and check it for any discrepancies.</p>
<p>It is <b>not</b> recommended to click <b>Upgrade Now</b> without testing first, as it
immediately triggers the live production database upgrade.</p>
<p>If the Rolling Release process detects an issue with the upgrade, it will be deactivated until
the issue is resolved.</p>
</div></div></div></div>

An upgrade does not cover:

>   * Downgrading to a previous version of Konvergo ERP
>
>   * [Switching editions](on_premise/community_to_enterprise) (e.g.,
> from Community to Enterprise)
>
>   * [Changing hosting type](hosting#hosting-change-solution) (e.g.,
> from on-premise to Konvergo ERP Online)
>
>   * Migrating from another ERP to Konvergo ERP
>
>

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>

## Upgrading in a nutshell

  1. Request an upgraded test database (see obtaining an upgraded test database).

  2. If applicable, upgrade the source code of your custom module to be compatible with the new version of Konvergo ERP (see [Upgrade a customized database](../developer/howtos/upgrade_custom_db)).

  3. Thoroughly test the upgraded database (see testing the new version of the database).

  4. Report any issue encountered during the testing to Konvergo ERP by [submitting a ticket for an issue related to my future upgrade (I am testing an upgrade)](https://odoo.com/help?stage=migration).

  5. Once all issues are resolved and you are confident that the upgraded database can be used as your main database without any issues, plan the upgrade of your production database.

  6. Request the upgrade for the production database, rendering it unavailable for the time it takes to complete the process (see upgrading the production database).

  7. Report any issue encountered during the upgrade to Konvergo ERP by [submitting a ticket for an issue related to my upgrade (production)](https://odoo.com/help?stage=post_upgrade).

## Obtaining an upgraded test database

The [Upgrade page](https://upgrade.odoo.com/) is the main platform for
requesting an upgraded database. However, depending on the hosting type, you
can upgrade from the command line (on-premise), the [Konvergo ERP Online database
manager](https://odoo.com/my/databases), or your [Konvergo ERP.sh
project](https://odoo.sh/project).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The Upgrade platform follows the same <a href="https://www.odoo.com/privacy">Privacy Policy</a> as the
other Konvergo ERP.com services. Visit the <a href="https://www.odoo.com/gdpr">General Data Protection Regulation page</a> to learn more about how Konvergo ERP handles your data and privacy.</p>
</div>

Konvergo ERP OnlineKonvergo ERP.shOn-premise

Konvergo ERP Online databases can be manually upgraded via the [database
manager](https://odoo.com/my/databases).

The database manager displays all databases associated with the user’s
account. Databases not on the most recent version of Konvergo ERP display an arrow in
a circle icon next to their name, indicating that they can be upgraded.

![The database manager with an upgrade button next to the name of a
database.](../_images/databases-page.png)

Click the **arrow in a circle** icon to start the upgrade process. In the
popup, fill in:

  * The **version** of Konvergo ERP you want to upgrade to, usually the latest version

  * The **email** address that should receive the link to the upgraded database

  * The **Purpose** of the upgrade, which is automatically set to **Test** for your first upgrade request

![The "Upgrade your database" popup.](../_images/upgrade-popup.png)

The **Upgrade in progress** tag is displayed next to the database name until
completion. Once the process succeeds, an email containing a link to the
upgraded test database is sent to the address provided. The database can also
be accessed from the database manager by clicking the dropdown arrow before
the database name.

![Clicking the menu arrow displays the upgraded test
database.](../_images/access-upgraded-db.png)

Konvergo ERP.sh is integrated with the upgrade platform to simplify the upgrade
process.

![Konvergo ERP.sh project and tabs](../_images/odoo-sh-staging.png)

The **latest production daily automatic backup** is then sent to the [upgrade
platform](https://upgrade.odoo.com).

Once the upgrade platform is done upgrading the backup and uploading it on the
branch, it is put in a **special mode** : each time a **commit is pushed** on
the branch, a **restore operation** of the upgraded backup and an **update of
all the custom modules** occur. This allows you to test your custom modules on
a pristine copy of the upgraded database. The log file of the upgrade process
can be found in your newly upgraded staging build by going to
`~/logs/upgrade.log`.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In databases where custom modules are installed, their source code must be up-to-date with
the target version of Konvergo ERP before the upgrade can be performed. If there are none, the
“update on commit” mode is skipped, the upgraded database is built as soon as it is
transferred from the upgrade platform, and the upgrade mode is exited.</p>
<p>Check out the <a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> page for more information.</p>
</div>

The standard upgrade process can be initiated by entering the following
command line on the machine where the database is hosted:

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <your db name> -t <target version>
    

The following command can be used to display the general help and the main
commands:

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) --help
    

An upgraded test database can also be requested via the [Upgrade
page](https://upgrade.odoo.com/).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In databases where custom modules are installed, their source code must be up-to-date with
the target version of Konvergo ERP before the upgrade can be performed. Check out the
<a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> page for more information.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>For security reasons, only the person who submitted the upgrade request can download it.</p></li>
<li><p>For storage reasons, the database’s copy is submitted without a filestore to the upgrade
server. Therefore, the upgraded database does not contain the production filestore.</p></li>
<li><p>Before restoring the upgraded database, its filestore must be merged with the production
filestore to be able to perform tests in the same conditions as it would be in the new
version.</p></li>
<li><p>The upgraded database contains:</p>
<ul>
<li><p>A <code>dump.sql</code> file containing the upgraded database</p></li>
<li><p>A <code>filestore</code> folder containing files extracted from in-database records into
attachments (if there are any) and new standard Konvergo ERP files from the targeted Konvergo ERP
version (e.g., new images, icons, payment provider’s logos, etc.).
This is the folder that should be merged with the production filestore
in order to get the full upgraded filestore.</p></li>
</ul>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can request multiple test databases if you wish to test an upgrade more than once.</p>
</div> <div class="alert alert-primary" id="upgrade-upgrade-report">
<p class="alert-title">
Note</p><p>When an upgrade request is completed, an upgrade report is attached to the successful upgrade
email, and it becomes available in the Discuss app for users who are part of the “Administration
/ Settings” group. This report provides important information about the changes introduced by
the new version.</p>
</div>

## Testing the new version of the database

It is essential to spend some time testing the upgraded test database to
ensure that you are not stuck in your day-to-day activities by a change in
views, behavior, or an error message once the upgrade goes live.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Test databases are neutralized, and some features are disabled to prevent them from impacting the
production database:</p>
<ol class="arabic simple">
<li><p>Scheduled actions are disabled.</p></li>
<li><p>Outgoing mail servers are disabled by archiving the existing ones and adding a fake one.</p></li>
<li><p>Payment providers and delivery carriers are reset to the test environment.</p></li>
<li><p>Bank synchronization is disabled. Should you want to test the synchronization, contact your
bank synchronization provider to get sandbox credentials.</p></li>
</ol>
</div>

Testing as many of your business flows as possible is strongly recommended to
ensure they are working correctly and to get more familiar with the new
version.

<div class="admonition-basic-test-checklist alert">
<p class="alert-title">
Basic test checklist</p><ul>
<li><p>Are there views that are deactivated in your test database but active in your production
database?</p></li>
<li><p>Are your usual views still displayed correctly?</p></li>
<li><p>Are your reports (invoice, sales order, etc.) correctly generated?</p></li>
<li><p>Are your website pages working correctly?</p></li>
<li><p>Are you able to create and modify records? (sales orders, invoices, purchases, users, contacts,
companies, etc.)</p></li>
<li><p>Are there any issues with your mail templates?</p></li>
<li><p>Are there any issues with saved translations?</p></li>
<li><p>Are your search filters still present?</p></li>
<li><p>Can you export your data?</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>0

If you face an issue while testing your upgraded test database, you can
request the assistance of Konvergo ERP by [submitting a ticket for an issue related to
my future upgrade (I am testing an
upgrade)](https://odoo.com/help?stage=migration). In any case, it is essential
to report any problem encountered during the testing to fix it before
upgrading your production database.

You might encounter significant differences with standard views, features,
fields, and models during testing. Those changes cannot be reverted on a case-
by-case basis. However, if a change introduced by a new version breaks a
customization, it is the responsibility of the maintainer of your custom
module to make it compatible with the new version of Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>1

## Upgrading the production database

Once the tests are completed and you are confident that the upgraded database
can be used as your main database without any issues, it is time to plan the
go-live day. It can be planned in coordination with Konvergo ERP’s upgrade support
analysts by [submitting a ticket for an issue related to my future upgrade (I
am testing an upgrade)](https://odoo.com/help?stage=migration).

Your production database will be unavailable during its upgrade. Therefore, we
recommend planning the upgrade at a time when the use of the database is
minimal.

As the standard upgrade scripts and your database are constantly evolving, it
is also recommended to frequently request another upgraded test database to
ensure that the upgrade process is still successful, especially if it takes a
long time to finish. **Fully rehearsing the upgrade process the day before
upgrading the production database is also recommended.**

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>2

The process of upgrading a production database is similar to upgrading a test
database with a few exceptions.

Konvergo ERP OnlineKonvergo ERP.shOn-premise

The process is similar to obtaining an upgraded test database, except for the
purpose option, which must be set to **Production** instead of **Test**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>3

The process is similar to obtaining an upgraded test database on the
**Production** branch.

![View from the upgrade tab](../_images/odoo-sh-prod.png)

The process is **triggered as soon as a new commit is made** on the branch.
This allows the upgrade process to be synchronized with the deployment of the
custom modules’ upgraded source code. If there are no custom modules, the
upgrade process is triggered immediately.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>4

The update of your custom modules must be successful to complete the entire
upgrade process. Make sure the status of your staging upgrade is
**successful** before trying it in production. More information on how to
upgrade your custom modules can be found on [Upgrade a customized
database](../developer/howtos/upgrade_custom_db).

The command to upgrade a database to production is similar to the one of
upgrading a test database except for the argument `test`, which must be
replaced by `production`:

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) production -d <your db name> -t <target version>
    

An upgraded production database can also be requested via the [Upgrade
page](https://upgrade.odoo.com/). Once the database is uploaded, any
modification to your production database will **not** be present on your
upgraded database. This is why we recommend not using it during the upgrade
process.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>5

In case of an issue with your production database, you can request the
assistance of Konvergo ERP by [submitting a ticket for an issue related to my upgrade
(production)](https://odoo.com/help?stage=post_upgrade).

## Service-level agreement (SLA)

With Konvergo ERP Enterprise, upgrading a database to the most recent version of Konvergo ERP
is **free** , including any support required to rectify potential
discrepancies in the upgraded database.

Information about the upgrade services included in the Enterprise Licence is
available in the [Konvergo ERP Enterprise Subscription
Agreement](../legal/terms/enterprise#upgrade). However, this section
clarifies what upgrade services you can expect.

### Upgrade services covered by the SLA

Databases hosted on Konvergo ERP’s cloud platforms (Konvergo ERP Online and Konvergo ERP.sh) or self-
hosted (On-Premise) can benefit from upgrade services at all times for:

  * the upgrade of all **standard applications** ;

  * the upgrade of all **customizations created with the Studio app** , as long as Studio is still installed and the respective subscription is still active; and

  * the upgrade of all **developments and customizations covered by a maintenance of customizations subscription**.

Upgrade services are limited to the technical conversion and adaptation of a
database (standard modules and data) to make it compatible with the version
targeted by the upgrade.

### Upgrade services not covered by the SLA

The following upgrade-related services are **not** included:

  * the **cleaning** of pre-existing data and configurations while upgrading;

  * the upgrade of **custom modules created in-house or by third parties** , including Konvergo ERP partners;

  * lines of **code added to standard modules** , i.e., customizations created outside the Studio app, code entered manually, and [automated actions using Python code](../applications/studio/automated_actions#studio-automated-actions-action); and

  * **training** on using the upgraded version’s features and workflows.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If your database contains custom modules, it cannot be upgraded until a version of your custom
modules is available for the target version of Konvergo ERP. For customers maintaining their own custom
modules, we recommend to parallelize the process by <a href="#upgrade-request-test-database"><span class="std std-ref">requesting an upgraded database</span></a> while also <a href="../developer/howtos/upgrade_custom_db">upgrading the source code of your custom
modules</a>.</p>
</div>6

