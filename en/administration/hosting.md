# Hosting

## Change hosting solution

The instructions to change the hosting type of a database depend on the
current solution used and to which solution the database should be moved.

## Transferring an on-premise database

### To Konvergo ERP Online

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Konvergo ERP Online is <em>not</em> compatible with <b>non-standard apps</b>.</p></li>
<li><p>The database’s current version must be <a href="supported_versions">supported</a>.</p></li>
</ul>
</div>

  1. Create a [duplicate of the database](on_premise#on-premise-duplicate).

  2. In this duplicate, uninstall all **non-standard apps**.

  3. Use the database manager to grab a _dump with filestore_.

  4. [Submit a support ticket](https://www.odoo.com/help) including the following:

     * your **subscription number** ,

     * the **URL** you want to use for the database (e.g., `company.odoo.com`), and

     * the **dump** as an attachment or as a link to the file (required for 60 MB+ files).

  5. Konvergo ERP then makes sure the database is compatible before putting it online. In case of technical issues during the process, Konvergo ERP might contact you.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you have time constraints, <a href="https://www.odoo.com/help">submit a support ticket</a> as soon as
possible to schedule the transfer.</p>
</div>

### To Konvergo ERP.sh

Follow the instructions found in [the Import your database
section](odoo_sh/getting_started/create#odoo-sh-import-your-database) of
the Konvergo ERP.sh _Create your project_ documentation.

## Transferring an Konvergo ERP Online database

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP Online’s <a href="supported_versions#supported-versions"><span class="std std-ref">intermediary versions</span></a> are not supported by Konvergo ERP.sh or
on-premise. Therefore, if the database to transfer is running an intermediary version, it must be
upgraded first to the next <a href="supported_versions#supported-versions"><span class="std std-ref">major version</span></a>, waiting for its release if
necessary.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Transferring an online database running on Konvergo ERP 16.3 would require first upgrading it to Konvergo ERP
17.0.</p>
</div>
<div class="alert alert-tip">
<p class="alert-title">
Tip</p><p>Click the gear icon (<b>⚙</b>) next to the database name on the <a href="https://www.odoo.com/my/databases/">Konvergo ERP Online database
manager</a> to display its version number.</p>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>If there is an active Konvergo ERP subscription linked to the database being migrated, reach out to
the Customer Service Manager or <a href="https://www.odoo.com/help">submit a support ticket</a>  to
complete the subscription transfer.</p>
</div>
</div>

### To on-premise

  1. Sign in to [the Konvergo ERP Online database manager](https://www.odoo.com/my/databases/) and click the gear icon (**⚙**) next to the database name to **Download** a backup. If the download fails due to the file being too large, [contact Konvergo ERP support](https://www.odoo.com/help).

  2. Restore the database from the database manager on your local server using the backup.

### To Konvergo ERP.sh

  1. Sign in to [the Konvergo ERP Online database manager](https://www.odoo.com/my/databases/) and click the gear icon (**⚙**) next to the database name to **Download** a backup. If the download fails due to the file being too large, [contact Konvergo ERP support](https://www.odoo.com/help).

  2. Follow the instructions found in [the Import your database section](odoo_sh/getting_started/create#odoo-sh-import-your-database) of the Konvergo ERP.sh _Create your project_ documentation.

## Transferring an Konvergo ERP.sh database

### To Konvergo ERP Online

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP Online is <em>not</em> compatible with <b>non-standard apps</b>.</p>
</div>

  1. Uninstall all **non-standard apps** in a staging build before doing it in the production build.

  2. [Create a support ticket](https://www.odoo.com/help) including the following:

     * your **subscription number** ,

     * the **URL** you want to use for the database (e.g., `company.odoo.com`),

     * which **branch** should be migrated,

     * in which **region** you want the database to be hosted (Americas, Europe, or Asia),

     * which user(s) will be the **administrator(s)** , and

     * **when** (and in which timezone) you want the database to be up and running.

  3. Konvergo ERP then makes sure the database is compatible before putting it online. In case of technical issues during the process, Konvergo ERP might contact you.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If you have time constraints, <a href="https://www.odoo.com/help">submit a support ticket</a> as soon as
possible to schedule the transfer.</p></li>
<li><p>Select the <b>region</b> closest to most of your users to reduce latency.</p></li>
<li><p>Future <b>administrator(s)</b> must have an Konvergo ERP.com account.</p></li>
<li><p>The <b>date and time</b> you want the database to be up and running are helpful to organize the
switch from the Konvergo ERP.sh server to the Konvergo ERP Online servers.</p></li>
<li><p>Databases are <b>not reachable</b> during their migration.</p></li>
</ul>
</div>

### To on-premise

  1. Download a [backup of your Konvergo ERP.sh production database](odoo_sh/getting_started/branches#odoo-sh-branches-backups).

  2. Restore the database from the database manager on your local server using the backup.

