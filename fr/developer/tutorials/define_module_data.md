# Define module data

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>This tutorial is an extension of the <a href="getting_started">Getting started</a> tutorial. Make sure you have
completed it and use the <code>estate</code> module you have built as a base for the exercises in this
tutorial. Fetch the branch <code>16.0-core</code> from the <a href="https://github.com/odoo/technical-training-solutions/tree/16.0-core">technical-training-solutions</a> repository if you
want to start from a clean base.</p>
</div>

## Data Types

### Master Data

Master data is usually part of the technical or business requirements for the
module. In other words, such data is often necessary for the module to work
properly. This data will always be installed when installing the module.

We already met technical data previously since we have defined
[views](../reference/backend/views#reference-views) and
[actions](../reference/backend/actions#reference-actions). Those are one
kind of master data.

On top of technical data, business data can be defined, e.g. countries,
currencies, units of measure, as well as complete country localization (legal
reports, tax definitions, chart of account), and much more…

### Demo Data

In additional to master data, which are requirements for a module to work
properly, we also like having data for demonstration purposes:

  * Help the sales representatives make their demos quickly.

  * Have a set of working data for developers to test new features and see how these new features look with data they might not have added themselves.

  * Test that the data is loaded correctly, without raising an error.

  * Setup most of the features to be used quickly when creating a new database.

Demo data is automatically loaded when you start the server if you don’t
explicitly say you don’t want it. This can be done in the database manager or
with the command line.

    
    
    $ ./odoo-bin -h
    Usage: odoo-bin [options]
    
    Options:
    --version             show program's version number and exit
    -h, --help            show this help message and exit
    
    Common options:
      [...]
      --without-demo=WITHOUT_DEMO
                          disable loading demo data for modules to be installed
                          (comma-separated, use "all" for all modules). Requires
                          -d and -i. Default is none
    [...]
    
    $ ./odoo-bin --addons-path=... -d db -i account --without-demo=all
    

## Data Declaration

### Manifest

**Reference** : the documentation related to this topic can be found in
[Module Manifests](../reference/backend/module#reference-module-
manifest).

Data is declared either in CSV or in XML. Each file containing data must be
added in the manifest for them to be loaded.

The keys to use in the manifest to add new data are `data` for the master data
and `demo` for the demo data. Both values should be a list of strings
representing the relative paths to the files declaring the data.

Usually, demo data is in a `demo` folder, views and actions are in a `views`
folder, security related data is in a `security` folder, and other data is in
a `data` folder.

If your work tree looks like this:

    
    
    estate
    ├── data
    │   └── master_data.xml
    ├── demo
    │   └── demo_data.xml
    ├── models
    │   ├── *.py
    │   └── __init__.py
    ├── security
    │   └── ir.model.access.csv
    ├── views
    │   └── estate_property_offer_views.xml
    ├── __init__.py
    └── __manifest__.py
    

Your manifest should look like this:

    
    
    # -*- coding: utf-8 -*-
    
    {
        "name": "Real Estate",
        "depends": [
            ...
        ],
        "data": [
            "security/ir.model.access.csv",  # CSV and XML files are loaded at the same place
            "views/estate_property_offer_views.xml",  # Views are data too
            "data/master_data.xml",  # Split the data in multiple files depending on the model
        ],
        "demo": [
            "demo/demo_data.xml",
        ]
        "application": True,
    }
    

### CSV

**Reference** : the documentation related to this topic can be found in [CSV
data files](../reference/backend/data#reference-data-csvdatafiles).

The easiest way to declare simple data is by using the CSV format. This is
however limited in terms of features: use it for long lists of simple models,
but prefer XML otherwise.

    
    
    id,field_a,field_b,related_id:id
    id1,valueA1,valueB1,module.relatedid
    id2,valueA2,valueB2,module.relatedid
    

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Your IDE has probably an extension to have a syntax highlighting of the CSV files</p>
<ul>
<li><p><a href="https://atom.io/packages/rainbow-csv">Atom</a>.</p></li>
<li><p><a href="https://plugins.jetbrains.com/plugin/10037-csv-plugin">PyCharm/IntelliJ</a>.</p></li>
<li><p><a href="https://github.com/mechatroner/rainbow_csv">Vim</a>.</p></li>
<li><p><a href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv">Visual Studio</a>.</p></li>
</ul>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add some standard Real Estate Property Types for the <code>estate</code> module: Residential,
Commercial, Industrial and Land. These should always be installed.</p>
</div>

### XML

**Reference** : the documentation related to this topic can be found in [Data
Files](../reference/backend/data#reference-data).

When the data to create is more complex it can be useful, or even necessary,
to do it in XML.

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="field_a">valueA1</field>
        <field name="field_b">valueB1</field>
      </record>
    
      <record id="id2" model="tutorial.example">
        <field name="field_a">valueA2</field>
        <field name="field_b">valueB2</field>
      </record>
    </odoo>
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Create some demo data for the <code>estate</code> module.</p>
<table class="table docutils">
<colgroup>
<col style="width: 30%"/>
<col style="width: 33%"/>
<col style="width: 37%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Values</p></th>
<th class="head"><p>Values</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>name</p></td>
<td><p>Big Villa</p></td>
<td><p>Trailer home</p></td>
</tr>
<tr class="row-odd"><td><p>state</p></td>
<td><p>New</p></td>
<td><p>Canceled</p></td>
</tr>
<tr class="row-even"><td><p>description</p></td>
<td><p>A nice and big villa</p></td>
<td><p>Home in a trailer park</p></td>
</tr>
<tr class="row-odd"><td><p>postcode</p></td>
<td><p>12345</p></td>
<td><p>54321</p></td>
</tr>
<tr class="row-even"><td><p>date_availability</p></td>
<td><p>2020-02-02</p></td>
<td><p>1970-01-01</p></td>
</tr>
<tr class="row-odd"><td><p>expected_price</p></td>
<td><p>1,600,000</p></td>
<td><p>100,000</p></td>
</tr>
<tr class="row-even"><td><p>selling_price</p></td>
<td></td>
<td><p>120,000</p></td>
</tr>
<tr class="row-odd"><td><p>bedrooms</p></td>
<td><p>6</p></td>
<td><p>1</p></td>
</tr>
<tr class="row-even"><td><p>living_area</p></td>
<td><p>100</p></td>
<td><p>10</p></td>
</tr>
<tr class="row-odd"><td><p>facades</p></td>
<td><p>4</p></td>
<td><p>4</p></td>
</tr>
<tr class="row-even"><td><p>garage</p></td>
<td><p>True</p></td>
<td><p>False</p></td>
</tr>
<tr class="row-odd"><td><p>garden</p></td>
<td><p>True</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>garden_area</p></td>
<td><p>100000</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>garden_orientation</p></td>
<td><p>South</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>

#### Data Extension

During the Core Training, we saw in the [Chapter 13:
Inheritance](getting_started/13_inheritance#tutorials-getting-
started-13-inheritance) chapter we could inherit (extend) an existing view.
This was a special case of data extension: any data can be extended in a
module.

When you are adding new fields to an existing model in a new module, you might
want to populate those fields on the records created in the modules you are
depending on. This is done by giving the `xml_id` of the record you want to
extend. It won’t replace it, in this case we will set the `field_c` to the
given value for both records.

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="field_c">valueC1</field>
      </record>
    
      <record id="id2" model="tutorial.example">
        <field name="field_c">valueC2</field>
      </record>
    </odoo>
    

#### `ref`

Related fields can be set using the `ref` key. The value of that key is the
`xml_id` of the record you want to link. Remember the `xml_id` is composed of
the name of the module where the data is first declared, followed by a dot,
followed by the `id` of the record (just the `id` works too if you are in the
module declaring it).

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="related_id" ref="module.relatedid"/>
      </record>
    </odoo>
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Create some demo data offers for the properties you created.</p>
<p>Create offers using the partners defined in <code>base</code></p>
<table class="table docutils">
<colgroup>
<col style="width: 37%"/>
<col style="width: 24%"/>
<col style="width: 18%"/>
<col style="width: 21%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Partner</p></th>
<th class="head"><p>Estate</p></th>
<th class="head"><p>Price</p></th>
<th class="head"><p>Validity</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Azure Interior</p></td>
<td><p>Big Villa</p></td>
<td><p>10000</p></td>
<td><p>14</p></td>
</tr>
<tr class="row-odd"><td><p>Azure Interior</p></td>
<td><p>Big Villa</p></td>
<td><p>1500000</p></td>
<td><p>14</p></td>
</tr>
<tr class="row-even"><td><p>Deco Addict</p></td>
<td><p>Big Villa</p></td>
<td><p>1500001</p></td>
<td><p>14</p></td>
</tr>
</tbody>
</table>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Ensure both of your demo properties are created with their Property Type set to Residential.</p>
</div>

#### `eval`

The value to assign to a field is not always a simple string and you might
need to compute it. It can also be used to optimize the insertion of related
values, or because a constraint forces you to add the related values in batch.
See :Add X2many fields.

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="year" eval="datetime.now().year+1"/>
      </record>
    </odoo>
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>The offers you added should always be in a date relative to the installation of the
module.</p>
</div>

#### `search`

Sometimes, you need to call the ORM to do a `search`. This is not feasible
with the CSV format.

    
    
    <odoo>
      <record id="id1" model="account.move.line">
        <field name="account_id" search="[
          ('user_type_id', '=', ref('account.data_account_type_direct_costs')),
          ('company_id', '=', obj().env.company.id)]
        "/>
      </record>
    </odoo>
    

In this code snippet, it is needed because the master data depends on the
localization installed.

#### `function`

You might also need to execute python code when loading data.

    
    
    <function model="tutorial.example" name="action_validate">
        <value eval="[ref('demo_invoice_1')]"/>
    </function>
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Validate one of the demo data offers by using the « Accept Offer » button. Refuse the
others.</p>
</div>

### Add X2many fields

**Reference** : the documentation related to this topic can be found in
`Command`.

If you need to add related data in a One2many or a Many2many field, you can do
so by using the `Command` methods.

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="related_ids" eval="[
            Command.create({
                'name': 'My name',
            }),
            Command.create({
                'name': 'Your name',
            }),
            Command.link(ref('model.xml_id')),
        ]"/>
      </record>
    </odoo>
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Create one new Property, but this time with some offers created directly inside the
One2many field linked to the Offers.</p>
</div>

## Accessing the data

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>You should never access demo data outside of the demo data declaration, not even in
tests.</p>
</div>

There are multiple ways to access the master/demo data.

In python code, you can use the `env.ref(self, xml_id,
raise_if_not_found=True)` method. It returns the recordset linked to the
`xml_id` you specify.

In XML, you can use the `ref` key like this

    
    
    <odoo>
      <record id="id1" model="tutorial.example">
        <field name="related_id" ref="module.relatedid"/>
      </record>
    </odoo>
    

It will call the ref method, and store the id of the record returned on the
field `related_id` of the record of type `tutorial.example` with id `id1`.

In CSV, the title of the column must be suffixed with `:id` or `/id`.

    
    
    id,parent_id:id,name
    "child1","module.parent","Name1"
    "child2","module.parent","Name2"
    "child3","module.parent","Name3"
    

In SQL, it is more complicated, see the advanced section.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Your IDE has probably an extension to have a syntax highlighting of the CSV files</p>
<ul>
<li><p><a href="https://atom.io/packages/rainbow-csv">Atom</a>.</p></li>
<li><p><a href="https://plugins.jetbrains.com/plugin/10037-csv-plugin">PyCharm/IntelliJ</a>.</p></li>
<li><p><a href="https://github.com/mechatroner/rainbow_csv">Vim</a>.</p></li>
<li><p><a href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv">Visual Studio</a>.</p></li>
</ul>
</div>0

## Advanced

### What is the XML id?

Because we don’t want a column `xml_id` in every single SQL table of the
database, we need a mechanism to store it. This is done with the
`ir.model.data` model.

It contains the name of the record (the `xml_id`) along with the module in
which it is defined, the model defining it, and the id of it.

### No update

The records created with the `noupdate` flag won’t be updated when upgrading
the module that created them, but it will be created if it didn’t exist yet.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Your IDE has probably an extension to have a syntax highlighting of the CSV files</p>
<ul>
<li><p><a href="https://atom.io/packages/rainbow-csv">Atom</a>.</p></li>
<li><p><a href="https://plugins.jetbrains.com/plugin/10037-csv-plugin">PyCharm/IntelliJ</a>.</p></li>
<li><p><a href="https://github.com/mechatroner/rainbow_csv">Vim</a>.</p></li>
<li><p><a href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv">Visual Studio</a>.</p></li>
</ul>
</div>1

    
    
    <odoo noupdate="1">
      <record id="id1" model="model">
        <field name="fieldA" eval="True"/>
      </record>
    </odoo>
    

### Import as SQL

In some cases, it makes sense to do the import directly in SQL. This is
however discouraged as it bypasses all the features of the ORM, computed
fields (including metadata) and python constraints.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Your IDE has probably an extension to have a syntax highlighting of the CSV files</p>
<ul>
<li><p><a href="https://atom.io/packages/rainbow-csv">Atom</a>.</p></li>
<li><p><a href="https://plugins.jetbrains.com/plugin/10037-csv-plugin">PyCharm/IntelliJ</a>.</p></li>
<li><p><a href="https://github.com/mechatroner/rainbow_csv">Vim</a>.</p></li>
<li><p><a href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv">Visual Studio</a>.</p></li>
</ul>
</div>2

  * It can help to speed the import time by a lot [with huge files](https://github.com/odoo/enterprise/blob/d46cceef8c594b9056d0115edb7169e207a5986f/product_unspsc/hooks.py#L19).

  * For more complex imports like for the [translations](https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/models/ir_translation.py#L24).

  * It can be necessary to [initialize the database](https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/data/base_data.sql).

