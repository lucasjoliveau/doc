# Setup

In this chapter, you will learn:

  * To set up your local development environment.

  * The outline of the Konvergo ERP database structure.

  * To export and import an Konvergo ERP database in your local environment.

  * To have an Konvergo ERP instance up and running.

## Install

There are multiple ways to [install
Konvergo ERP](../../../administration/on_premise), depending on the intended use
case. This documentation assumes you use the [source
install](../../../administration/on_premise/source) (running Konvergo ERP from
the source code), which is best suited for Konvergo ERP designers and developers.

## Databases

### Structure

Every Konvergo ERP application works similarly; they are built with the same logic. A
model contains fields and relational fields that link to other models. Each
model has views representing all its fields, with backend and frontend views.

#### Models

The basis of Konvergo ERP is models. Models use fields to record the data. Records are
stored in a database: they are therefore linked to a model. In Konvergo ERP, you can
find the different models in the backend by enabling the [developer
mode](../../../applications/general/developer_mode#developer-mode) and
then going to Settings ‣ Technical ‣ Database Structure: Models.

![Models page](../../../_images/models-page.png)

#### Fields

In a model, we will centralize fields (field names we need to target in our
code).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../applications/studio/fields">Campos y widgets</a></p>
</div>

##### Classic fields

  * Date

  * Char

  * Selection

  * …

##### Relational fields

Relational fields call a field from another model. They allow you to link
models together and make them interact easily. In other words, when you use a
relational field, you link a record with another one (located on another
model), enabling you to retrieve the content of the fields located on this
linked record.

  * **Many2one** fields are filled in by choosing one record from a list of records on another model (from _many_ records, you select _one_). For example, the _customer_ field on a quotation makes you choose one customer from a list of several customers on the _contact_ model.

  * **One2many** fields are reverse searches of existing many2one relations. For example, you could list on a contact all their existing quotations (from _one_ record, you display _many_).

  * **Many2many** fields are filled in by choosing one or several records from a list of records on another model. For example, you can put several tags on one product, and several products can use the same tags (from _many_ records, you can select _many_).

#### Views

Views define how records should be displayed to end-users. They are specified
in XML, meaning they can be edited independently from the models they
represent. They are flexible and allow deep customization of the screens they
control.

##### Backend vs. Frontend

  * **Backend views** : Kanban, List, Form, etc.

  * **Frontend view** : QWeb

##### Static vs. Dynamic

  * **Static pages** have stable content, such as the homepage. You can define their URL and set some properties like published, indexed, etc.

  * **Dynamic pages** are dynamically generated, such as the product page. Their URL is dynamic and is accessible to all by default (this can be changed by configuring access rights).

##### Standard vs. Inherited

  * **Standard views** are base views implemented by Konvergo ERP. They are directly derived from their model. You should never change them as they allow updating an Konvergo ERP database without overwriting a client’s modifications.

  * **Inherited views** are duplicated views. Modifications always take place in an inherited view. If there is a duplicate view, there will be two views with the same name in the database, but the duplicated view will not have an ID like for standard view.

### Import an existing database

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>You can directly go to the <a href="theming">Theming</a> chapter if you do not need to import an existing
database.</p>
</div>

#### Dump

##### Konvergo ERP SaaS

Go to `<database_url>/saas_worker/dump`.

##### Konvergo ERP.sh

  1. Connect to Konvergo ERP.sh.

  2. Select the branch you want to back up.

  3. Choose the **BACKUPS** tab.

  4. Click the **Create Backup** button.

  5. When the process is over, a notification appears. Open it and click the **Go to Backup** button.

  6. Click the **Download** icon. Select **Testing** under **Purpose** and **With filestore** under **Filestore**.

![Download backup](../../../_images/download-backup.png)

  7. You will receive a notification when the dump is ready to be downloaded. Open it and click on **Download** to get your dump.

![Database backup](../../../_images/database-backup.png)

#### Move filestore

Copy all the folders included in the filestore folder and paste them to the
following location on your computer:

  * macOS: `/Users/<User>/Library/Application Support/Konvergo ERP/filestore/<database_name>`

  * Linux: `/home/<User>/.local/share/Konvergo ERP/filestore/<database_name>`

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><code>/Library</code> is a hidden folder.</p>
</div>

#### Database setup

Create an empty database.

    
    
    createdb <database_name>
    

Import the SQL file in the database that you just created.

    
    
    psql <database_name> < dump.sql
    

Reset the admin user password.

    
    
    psql \c
    <database_name>
    update res_users set login='admin', password='admin' where id=2;
    

## Getting started

### Running Konvergo ERP

Once all dependencies are set up, Konvergo ERP can be launched by running `odoo-bin`,
the command-line interface of the server. It is located at the root of the
Konvergo ERP Community directory.

  * [Running Konvergo ERP](../../../administration/on_premise/source#install-source-running-odoo)

  * [Docker](https://hub.docker.com/_/odoo/)

To configure the server, you can specify command-line arguments or a
configuration file. The first method is presented below.

The [CLI](../../reference/cli#reference-cmdline) offers several
functionalities related to Konvergo ERP. You can use it to [run the
server](../../reference/cli#reference-cmdline-server), scaffold an Konvergo ERP
theme, populate a database, or count the number of lines of code.

### Shell script

A typical way to [run the server](../../reference/cli#reference-cmdline-
server) would be to add all command line arguments to a `.sh` script.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span>./odoo-bin --addons-path=../enterprise,addons --db-filter=<span class="nt">&lt;database&gt;</span> -d <span class="nt">&lt;database&gt;</span> --without-demo=all -i website --dev=xml
</pre></div>
</div>
</div>  Folder | Description  
---|---  
[`--addons-path`](../../reference/cli#cmdoption-odoo-bin-addons-path) | Comma-separated list of directories in which modules are stored. These directories are scanned for modules.  
[`-d`](../../reference/cli#cmdoption-odoo-bin-d) [`--database`](../../reference/cli#cmdoption-odoo-bin-d) | database(s) used when installing or updating modules.  
[`--db-filter`](../../reference/cli#cmdoption-odoo-bin-db-filter) | Hides databases that do not match the filter.  
[`-i`](../../reference/cli#cmdoption-odoo-bin-i) [`--init`](../../reference/cli#cmdoption-odoo-bin-i) | Comma-separated list of modules to install before running the server. (requires `-d`)  
[`-u`](../../reference/cli#cmdoption-odoo-bin-u) [`--update`](../../reference/cli#cmdoption-odoo-bin-u) | Comma-separated list of modules to update before running the server. (requires `-d`)  
[`--without-demo`](../../reference/cli#cmdoption-odoo-bin-without-demo) | Disables demo data loading for modules installed comma-separated; use `all` for all modules. (requires `-d` and `-i`)  
[`--dev`](../../reference/cli#cmdoption-odoo-bin-dev) | Comma-separated list of features. For development purposes only. [More info](../../reference/cli#reference-cmdline-dev)  
  
### Sign in

After the server has started (the INFO log `odoo.modules.loading: Modules
loaded.` is printed), open <http://localhost:8069> in your web browser and log
in with the base administrator account.

Type **admin** for the email and **admin** for the password.

![Welcome homepage](../../../_images/welcome-homepage.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Hit <em>CTRL+C</em> to stop the server. Do it twice if needed.</p>
</div>

### Developer mode

The developer mode, also known as debug mode, is useful for development as it
gives access to additional tools. In the next chapters, it is assumed that you
have enabled the developer mode.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../applications/general/developer_mode">Modo de desarrollador (modo de depuración)</a></p>
</div>

