# Chapter 4: Models And Basic Fields

At the end of the [previous chapter](03_newapp#tutorials-getting-
started-03-newapp), we were able to create an Konvergo ERP module. However, at this
point it is still an empty shell which doesn’t allow us to store any data. In
our real estate module, we want to store the information related to the
properties (name, description, price, living area…) in a database. The Konvergo ERP
framework provides tools to facilitate database interactions.

Before moving forward in the exercise, make sure the `estate` module is
installed, i.e. it must appear as “Installed” in the Apps list.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Do not use mutable global variables.</p>
<p>A single Konvergo ERP instance can run several databases in parallel within the same python process.
Distinct modules might be installed on each of these databases, therefore we cannot rely on
global variables that would be updated depending on installed modules.</p>
</div>

## Object-Relational Mapping

**Reference** : the documentation related to this topic can be found in the
[Models](../../reference/backend/orm#reference-orm-model) API.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, the table <code>estate_property</code> should be created:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>$ psql -d rd-demo
rd-demo=# SELECT COUNT(*) FROM estate_property;
count
-------
    0
(1 row)
</pre></div>
</div>
</div>

A key component of Konvergo ERP is the [ORM](https://en.wikipedia.org/wiki/Object-
relational_mapping) layer. This layer avoids having to manually write most
[SQL](https://en.wikipedia.org/wiki/SQL) and provides extensibility and
security services2.

Business objects are declared as Python classes extending `Model`, which
integrates them into the automated persistence system.

Models can be configured by setting attributes in their definition. The most
important attribute is `_name`, which is required and defines the name for the
model in the Konvergo ERP system. Here is a minimum definition of a model:

    
    
    from odoo import models
    
    class TestModel(models.Model):
        _name = "test_model"
    

This definition is enough for the ORM to generate a database table named
`test_model`. By convention all models are located in a `models` directory and
each model is defined in its own Python file.

Take a look at how the `crm_recurring_plan` table is defined and how the
corresponding Python file is imported:

  1. The model is defined in the file `crm/models/crm_recurring_plan.py` (see [here](https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/models/crm_recurring_plan.py#L1-L9))

  2. The file `crm_recurring_plan.py` is imported in `crm/models/__init__.py` (see [here](https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/models/__init__.py#L15))

  3. The folder `models` is imported in `crm/__init__.py` (see [here](https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/__init__.py#L5))

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Define the real estate properties model.</p>
<p>Based on example given in the CRM module, create the appropriate files and folder for the
<code>estate_property</code> table.</p>
<p>When the files are created, add a minimum definition for the
<code>estate.property</code> model.</p>
</div>

Any modification of the Python files requires a restart of the Konvergo ERP server.
When we restart the server, we will add the parameters `-d` and `-u`:

    
    
    $ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate
    

`-u estate` means we want to upgrade the `estate` module, i.e. the ORM will
apply database schema changes. In this case it creates a new table. `-d rd-
demo` means that the upgrade should be performed on the `rd-demo` database.
`-u` should always be used in combination with `-d`.

During the startup you should see the following warnings:

    
    
    ...
    WARNING rd-demo odoo.models: The model estate.property has no _description
    ...
    WARNING rd-demo odoo.modules.loading: The model estate.property has no access rules, consider adding one...
    ...
    

If this is the case, then you should be good! To be sure, double check with
`psql` as demonstrated in the **Goal**.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a description.</p>
<p>Add a <code>_description</code> to your model to get rid of one of the warnings.</p>
</div>

## Model fields

**Reference** : the documentation related to this topic can be found in the
[Fields](../../reference/backend/orm#reference-orm-fields) API.

Fields are used to define what the model can store and where they are stored.
Fields are defined as attributes in the model class:

    
    
    from odoo import fields, models
    
    class TestModel(models.Model):
        _name = "test_model"
        _description = "Test Model"
    
        name = fields.Char()
    

The `name` field is a `Char` which will be represented as a Python unicode
`str` and a SQL `VARCHAR`.

### Types

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, several basic fields should have been added to the table
<code>estate_property</code>:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>$ psql -d rd-demo

rd-demo=# \d estate_property;
                                            Table "public.estate_property"
    Column       |            Type             | Collation | Nullable |                   Default
--------------------+-----------------------------+-----------+----------+---------------------------------------------
id                 | integer                     |           | not null | nextval('estate_property_id_seq'::regclass)
create_uid         | integer                     |           |          |
create_date        | timestamp without time zone |           |          |
write_uid          | integer                     |           |          |
write_date         | timestamp without time zone |           |          |
name               | character varying           |           |          |
description        | text                        |           |          |
postcode           | character varying           |           |          |
date_availability  | date                        |           |          |
expected_price     | double precision            |           |          |
selling_price      | double precision            |           |          |
bedrooms           | integer                     |           |          |
living_area        | integer                     |           |          |
facades            | integer                     |           |          |
garage             | boolean                     |           |          |
garden             | boolean                     |           |          |
garden_area        | integer                     |           |          |
garden_orientation | character varying           |           |          |
Indexes:
    "estate_property_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "estate_property_create_uid_fkey" FOREIGN KEY (create_uid) REFERENCES res_users(id) ON DELETE SET NULL
    "estate_property_write_uid_fkey" FOREIGN KEY (write_uid) REFERENCES res_users(id) ON DELETE SET NULL
</pre></div>
</div>
</div>

There are two broad categories of fields: “simple” fields, which are atomic
values stored directly in the model’s table, and “relational” fields, which
link records (of the same or different models).

Simple field examples are `Boolean`, `Float`, `Char`, `Text`, `Date` and
`Selection`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add basic fields to the Real Estate Property table.</p>
<p>Add the following basic fields to the table:</p>
<table class="table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>name</p></td>
<td><p>Char</p></td>
</tr>
<tr class="row-odd"><td><p>description</p></td>
<td><p>Text</p></td>
</tr>
<tr class="row-even"><td><p>postcode</p></td>
<td><p>Char</p></td>
</tr>
<tr class="row-odd"><td><p>date_availability</p></td>
<td><p>Date</p></td>
</tr>
<tr class="row-even"><td><p>expected_price</p></td>
<td><p>Float</p></td>
</tr>
<tr class="row-odd"><td><p>selling_price</p></td>
<td><p>Float</p></td>
</tr>
<tr class="row-even"><td><p>bedrooms</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="row-odd"><td><p>living_area</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="row-even"><td><p>facades</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="row-odd"><td><p>garage</p></td>
<td><p>Boolean</p></td>
</tr>
<tr class="row-even"><td><p>garden</p></td>
<td><p>Boolean</p></td>
</tr>
<tr class="row-odd"><td><p>garden_area</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="row-even"><td><p>garden_orientation</p></td>
<td><p>Selection</p></td>
</tr>
</tbody>
</table>
<p>The <code>garden_orientation</code> field must have 4 possible values: “North”, “South”, “East”
and “West”. The selection list is defined as a list of tuples, see
<a href="https://github.com/odoo/odoo/blob/b0e0035b585f976e912e97e7f95f66b525bc8e43/addons/crm/report/crm_activity_report.py#L31-L34">here</a>
for an example.</p>
</div>

When the fields are added to the model, restart the server with `-u estate`

    
    
    $ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate
    

Connect to `psql` and check the structure of the table `estate_property`.
You’ll notice that a couple of extra fields were also added to the table. We
will revisit them later.

### Common Attributes

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, the columns <code>name</code> and <code>expected_price</code> should be
not nullable in the table <code>estate_property</code>:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rd-demo=# \d estate_property;</span>
<span class="go">                                            Table "public.estate_property"</span>
<span class="go">    Column       |            Type             | Collation | Nullable |                   Default</span>
<span class="go">--------------------+-----------------------------+-----------+----------+---------------------------------------------</span>
<span class="go">...</span>
<span class="go">name               | character varying           |           | not null |</span>
<span class="go">...</span>
<span class="go">expected_price     | double precision            |           | not null |</span>
<span class="go">...</span>
</pre></div>
</div>
</div>

Much like the model itself, fields can be configured by passing configuration
attributes as parameters:

    
    
    name = fields.Char(required=True)
    

Some attributes are available on all fields, here are the most common ones:

`string` (`str`, default: field’s name)

    

The label of the field in UI (visible by users).

`required` (`bool`, default: `False`)

    

If `True`, the field can not be empty. It must either have a default value or
always be given a value when creating a record.

`help` (`str`, default: `''`)

    

Provides long-form help tooltip for users in the UI.

`index` (`bool`, default: `False`)

    

Requests that Konvergo ERP create a [database index](https://use-the-index-
luke.com/sql/preface) on the column.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Set attributes for existing fields.</p>
<p>Add the following attributes:</p>
<table class="table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Attribute</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>name</p></td>
<td><p>required</p></td>
</tr>
<tr class="row-odd"><td><p>expected_price</p></td>
<td><p>required</p></td>
</tr>
</tbody>
</table>
<p>After restarting the server, both fields should be not nullable.</p>
</div>

### Automatic Fields

**Reference** : the documentation related to this topic can be found in
[Automatic fields](../../reference/backend/orm#reference-fields-
automatic).

You may have noticed your model has a few fields you never defined. Konvergo ERP
creates a few fields in all models1. These fields are managed by the system
and can’t be written to, but they can be read if useful or necessary:

`id` (`Id`)

    

The unique identifier for a record of the model.

`create_date` (`Datetime`)

    

Creation date of the record.

`create_uid` (`Many2one`)

    

User who created the record.

`write_date` (`Datetime`)

    

Last modification date of the record.

`write_uid` (`Many2one`)

    

User who last modified the record.

Now that we have created our first model, let’s [add some
security](05_securityintro#tutorials-getting-started-05-securityintro)!

1

    

it is possible to [disable the automatic creation of some
fields](../../reference/backend/orm#reference-fields-automatic-log-
access)

2

    

writing raw SQL queries is possible, but requires caution as this bypasses all
Konvergo ERP authentication and security mechanisms.

