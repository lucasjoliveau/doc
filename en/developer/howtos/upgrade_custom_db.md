# Upgrade a customized database

Upgrading to a new version of Konvergo ERP can be challenging, especially if the
database you work on contains custom modules. This page intent is to explain
the technical process of upgrading a database with customized modules. Refer
to [Upgrade documentation](../../administration/upgrade) for guidance on
how to upgrade a database without customized modules.

We consider a custom module, any module that extends the standard code of Konvergo ERP
and that was not built with the Studio app. Before upgrading such a module, or
before requesting its upgrade, have a look at the [Service-level agreement
(SLA)](../../administration/upgrade#upgrade-sla) to make sure who’s
responsible for it.

While working on what we refer to as the **custom upgrade** of your database,
keep in mind the goals of an upgrade:

  1. Stay supported

  2. Get the latest features

  3. Enjoy the performance improvement

  4. Reduce the technical debt

  5. Benefit from security improvements

With every new version of Konvergo ERP, changes are introduced. These changes can
impact modules on which customization have been developed. This is the reason
why upgrading a database that contains custom modules requires additional
steps in order to upgrade the source code.

These are the steps to follow to upgrade customized databases:

  1. Stop the devolopments and challenge them.

  2. Request an upgraded database.

  3. Make your module installable on an empty database.

  4. Make your module installable on the upgraded database.

  5. Test extensively and do a rehearsal.

  6. Upgrade the production database.

## Step 1: Stop the developments

Starting an upgrade requires commitment and development resources. If
developments keep being made at the same time, those features will need to be
re-upgraded and tested every time you change them. This is why we recommend a
complete freeze of the codebase when starting the upgrade process. Needless to
say, bug fixing is exempt from this recommendation.

Once you have stopped development, it is a good practice to assess the
developments made and compare them with the features introduced between your
current version and the version you are targeting. Challenge the developments
as much as possible and find functional workarounds. Removing redundancy
between your developments and the standard version of Konvergo ERP will lead to an
eased upgrade process and reduce technical debt.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can find information on the changes between versions in the <a href="https:/odoo.com/page/release-notes">Release Notes</a>.</p>
</div>

## Step 2: Request an upgraded database

Once the developments have stopped for the custom modules and the implemented
features have been challenged to remove redundancy and unnecessary code, the
next step is to request an upgraded test database. To do so, follow the steps
mentioned in [Obtaining an upgraded test
database](../../administration/upgrade#upgrade-request-test-database),
depending on the hosting type of your database.

The purpose of this stage is not to start working with the custom modules in
the upgraded database, but to make sure the standard upgrade process works
seamlessly, and the test database is delivered properly. If that’s not the
case, and the upgrade request fails, request the assistance of Konvergo ERP via the
[support page](https://odoo.com/help?stage=migration) by selecting the option
related to testing the upgrade.

## Step 3: Empty database

Before working on an upgraded test database, we recommend to make the custom
developments work on an empty database in the targeted version of your
upgrade. This ensures that the customization is compatible with the new
version of Konvergo ERP, allows to analyze how it behaves and interacts with the new
features, and guarantees that they will not cause any issues when upgrading
the database.

Making the custom modules work in an empty database also helps avoid changes
and wrong configurations that might be present in the production database
(like studio customization, customized website pages, email templates or
translations). They are not intrinsically related to the custom modules and
that can raise unwanted issues in this stage of the upgrade process.

To make custom modules work on an empty database we advise to follow these
steps:

  1. Make custom modules installable

  2. Test and fixes

  3. Clean the code

  4. Make standard tests run successfully

### Make custom modules installable

The first step is to make the custom modules installable in the new Konvergo ERP
version. This means, starting by ensuring there are no tracebacks or warnings
during their installation. For this, install the custom modules, one by one,
in an empty database of the new Konvergo ERP version and fix the tracebacks and
warnings that arise from that.

This process will help detect issues during the installation of the modules.
For example:

  * Invalid module dependencies.

  * Syntax change: assets declaration, OWL updates, attrs.

  * References to standard fields, models, views not existing anymore or renamed.

  * Xpath that moved or were removed from views.

  * Methods renamed or removed.

  * …

### Test and fixes

Once there are no more tracebacks when installing the modules, the next step
is to test them. Even if the custom modules are installable on an empty
database, this does not guarantee there are no errors during their execution.
Because of this, we encourage to test thoroughly all the customization to make
sure everything is working as expected.

This process will help detect further issues that are not identified during
the module installation and can only be detected in runtime. For example,
deprecated calls to standard python or OWL functions, non-existing references
to standard fields, etc.

We recommend to test all the customization, especially the following elements:

  * Views

  * Email templates

  * Reports

  * Server actions and automated actions

  * Changes in the standard workflows

  * Computed fields

We also encourage to write automated tests to save time during the testing
iterations, increase the test coverage, and ensure that the changes and fixes
introduced do not break the existing flows. If there are tests already
implemented in the customization, make sure they are upgraded to the new Konvergo ERP
version and run successfully, fixing issues that might be present.

### Clean the code

At this stage of the upgrade process, we also suggest to clean the code as
much as possible. This includes:

  * Remove redundant and unnecessary code.

  * Remove features that are now part of Konvergo ERP standard, as described in Step 1: Stop the developments.

  * Clean commented code if it is not needed anymore.

  * Refactor the code (functions, fields, views, reports, etc.) if needed.

### Standard tests

Once the previous steps are completed, we advise to make sure all standard
tests associated to the dependencies of the custom module pass. Standard tests
ensure the validation of the code logic and prevent data corruption. They will
help you identify bugs or unwanted behavior before you work on your database.

In case there are standard test failing, we suggest to analyze the reason for
their failure:

  * The customization changes the standard workflow: Adapt the standard test to your workflow.

  * The customization did not take into account a special flow: Adapt your customization to ensure it works for all the standard workflows.

## Step 4: Upgraded database

Once the custom modules are installable and working properly in an empty
database, it is time to make them work on an [upgraded
database](../../administration/upgrade#upgrade-request-test-database).

To make sure the custom code is working flawlessly in the new version, follow
these steps:

  * Migrate the data

  * Test the custom modules

### Migrate the data

During the upgrade of the custom modules, you might have to use [upgrade
scripts](../reference/upgrades/upgrade_scripts) to reflect changes from
the source code to their corresponding data. Together with the upgrade
scripts, you can also make use of the [Upgrade
utils](../reference/upgrades/upgrade_utils) and its helper functions.

  * Any technical data that was renamed during the upgrade of the custom code (models, fields, external identifiers) should be renamed using upgrade scripts to avoid data loss during the module upgrade. See also: `rename_field()`, `rename_model()`, `rename_xmlid()`.

  * Data from standard models removed from the source code of the newer Konvergo ERP version and from the database during the standard upgrade process might need to be recovered from the old model table if it is still present.

> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Custom fields for model <code>sale.subscription</code> are not automatically migrated from Konvergo ERP 15 to
Konvergo ERP 16 (when the model was merged into <code>sale.order</code>). In this case, a SQL query can be
executed on an upgrade script to move the data from one table to the other. Take into account
that all columns/fields must already exist, so consider doing this in a <code>post-</code> script (See
<a href="../reference/upgrades/upgrade_scripts#upgrade-scripts-phases"><span class="std std-ref">Phases of upgrade scripts</span></a>).</p>
<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Spoiler</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">migrate</span><span class="p">(</span><span class="n">cr</span><span class="p">,</span> <span class="n">version</span><span class="p">):</span>
   <span class="n">cr</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
      <span class="sd">"""</span>
<span class="sd">      UPDATE sale_order so</span>
<span class="sd">         SET custom_field = ss.custom_field</span>
<span class="sd">        FROM sale_subscription ss</span>
<span class="sd">       WHERE ss.new_sale_order_id = so.id</span>
<span class="sd">      """</span>
   <span class="p">)</span>
</pre></div>
</div>
<p>Check the documentation for more information on <a href="../reference/upgrades/upgrade_scripts">Upgrade scripts</a>.</p>
</div></div></div></div></div>

Upgrade scripts can also be used to:

  * Ease the processing time of an upgrade. For example, to store the value of computed stored fields on models with an excessive number of records by using SQL queries.

  * Recompute fields in case the computation of their value has changed. See also `recompute_fields()`.

  * Uninstall unwanted custom modules. See also `remove_module()`.

  * Correct faulty data or wrong configurations.

#### Running and testing upgrade scripts

Konvergo ERP OnlineKonvergo ERP.shOn-premise

As the instalation of custom modules containing Python files is not allowed on
Konvergo ERP Online databases, it is not possible to run upgrade scripts on this
platform.

As explained on the `Konvergo ERP.sh` tab of [Obtaining an upgraded test
database](../../administration/upgrade#upgrade-request-test-database),
Konvergo ERP.sh is integrated with the upgrade platform.

Once the upgrade of a staging branch is on “Update on commit” mode, each time
a commit is pushed on the branch, the upgraded backup is restored and all the
custom modules are updated. This update includes the execution of the upgrade
scripts.

When upgrading the production database, the execution of the upgrade scripts
is also part of the update of the custom modules done by the platform when the
upgraded database is restored.

Once you receive the upgraded dump of the database from the [Upgrade
platform](https://upgrade.odoo.com), deploy the database and update all the
custom modules by invoking the command [odoo-bin](../reference/cli) in
the shell. To update the custom modules, use the option: `-u <modules>,
--update <modules>`.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>As mentioned in the <a href="../reference/cli">CLI documentation</a>, the command used
to call the CLI depends on how you installed Konvergo ERP.</p>
</div>

### Test the custom modules

To make sure the custom modules work properly with your data in the upgraded
database, they need to be tested as well. This helps ensure both the standard
and the custom data stored in the database are consistent and that nothing was
lost during the upgrade process.

Things to pay attention to:

  * Views not working: During the upgrade, if a view causes issues because of its content, it gets disabled. You can find the information on disabled views on the [Upgrade report](../../administration/upgrade#upgrade-upgrade-report). This view needs to be activated again (or removed if not useful anymore). To achieve this, we recommend the use of upgrade scripts.

  * [Module data](../tutorials/define_module_data) not updated: Custom records that have the `noupdate` flag are not updated when upgrading the module in the new database. For the custom data that needs to be updated due to changes in the new version, we recommend to use upgrade scripts to do so. See also: `update_record_from_xml()`.

## Step 5: Testing and rehearsal

When the custom modules are working properly in the upgraded database, it is
crucial to do another round of testing to assess the database usability and
detect any issues that might have gone unnoticed in previous tests. For
further information about testing the upgraded database, check [Testing the
new version of the database](../../administration/upgrade#upgrade-test-
your-db).

As mentioned in [Upgrading the production
database](../../administration/upgrade#upgrade-upgrade-prod), both
standard upgrade scripts and your database are constantly evolving. Therefore
it is highly recommended to frequently request new upgraded test databases and
ensure that the upgrade process is still successful.

In addition to that, make a full rehearsal of the upgrade process the day
before upgrading the production database to avoid undesired behavior during
the upgrade and to detect any issue that might have occurred with the migrated
data.

## Step 6: Production upgrade

Once you are confident about upgrading your production database, follow the
process described on [Upgrading the production
database](../../administration/upgrade#upgrade-upgrade-prod), depending
on the hosting type of your database.

