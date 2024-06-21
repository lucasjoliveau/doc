# Exporter et importer des données

Dans Konvergo ERP, il est parfois nécessaire d’exporter ou d’importer des données pour
exécuter des rapports ou pour modifier des données. Ce document traite de
l’exportation et de l’importation de données dans et hors d’Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Parfois, les utilisateurs rencontrent une erreur de « TimeOut » -dépassement de temps- ou une écriture d’enregistrement ne se termine pas en raison de sa taille. Cela peut se produire lors de grands exports ou dans les cas où le fichier d’importation est trop volumineux. Pour contourner cette limitation liée à la taille des enregistrements, traitez les exports ou imports par lots de plus petite taille.</p>
</div>

## Exporter des données depuis Konvergo ERP

Lorsqu’on travaille avec une base de données, il est parfois nécessaire
d’exporter les données dans un fichier distinct. Cela peut aider à la
réalisation de rapports sur les activités, cependant, Konvergo ERP offre un outil de
reporting précis et facile à utiliser avec chaque application disponible.

Avec Konvergo ERP, les valeurs peuvent être exportées de n’importe quel champ dans
n’importe quel enregistrement. Pour ce faire, activez la vue en liste (icône à
quatre lignes horizontales), sur les éléments à exporter, puis sélectionnez
les enregistrements à exporter. Pour sélectionner un enregistrement, cochez la
case à côté de l’enregistrement correspondant. Enfin, cliquez sur ⚙️ “Action”,
puis sur “Exporter”.

![Vue des différentes options à activer ou sur lesquelles cliquer pour
exporter des données.](../../_images/list-view-export.png)

When clicking on **Export** , an **Export Data** pop-over window appears, with
several options for the data to export:

![Overview of options to consider when exporting data in
Konvergo ERP..](../../_images/export-data-overview.png)

  1. With the **I want to update data (import-compatable export)** option ticked, the system only shows the fields that can be imported. This is helpful in the case where the existing records need to be updated. This works like a filter. Leaving the box unticked, gives many more field options because it shows all the fields, not just the ones that can be imported.

  2. When exporting, there is the option to export in two formats: `.csv` and `.xls`. With `.csv`, items are separated by a comma, while `.xls` holds information about all the worksheets in a file, including both content and formatting.

  3. These are the items that can be exported. Use the **> (right arrow)** icon to display more sub-field options. Use the **Search** bar to find specific fields. To use the **Search** option more efficiently, click on all the **> (right arrows)** to display all fields.

  4. The **\+ (plus sign)** icon button is present to add fields to the **Fields to export** list.

  5. The **↕️ (up-down arrow)** to the left of the selected fields can be used to move the fields up and down, to change the order in which they are displayed in the exported file. Drag-and-drop using the **↕️ (up-down arrow)** icon.

  6. The **🗑️ (trash can)** icon is used to remove fields. Click on the **🗑️ (trash can)** icon to remove the field.

  7. For recurring reports, it is helpful to save export presets. Select all the needed fields, and click on the template drop-down menu. Once there, click on **New template** , and give a unique name to the export just created. The next time the same list needs to be exported, select the related template that was previously saved from the drop-down menu.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>

## Importer des données dans Konvergo ERP

Importing data into Konvergo ERP is extremely helpful during implementation, or in
times where data needs to be updated in bulk. The following documentation
covers how to import data into an Konvergo ERP database.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Imports are permanent and <b>cannot</b> be undone. However, it is possible to use filters (<code>created
on</code> or <code>last modified</code>) to identify records changed or created by the import.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Activating <a href="../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> changes the visible import settings in the left
menu. Doing so reveals an Advanced menu. Included in this advanced menu are two
options: <b>Track history during import</b> and <b>Allow matching with subfields</b>.</p>
<img alt="Advanced import options when developer mode is activated." class="align-center" src="../../_images/advanced-import.png"/>
<p>If the model uses openchatter, the <b>Track history during import</b> option sets up
subscriptions and sends notifications during the import, but leads to a slower import.</p>
<p>Should the <b>Allow matching with subfields</b> option be selected, then all subfields
within a field are used to match under the <b>Konvergo ERP Field</b> while importing.</p>
</div>

### Les prémices

Data can be imported on any Konvergo ERP business object using either Excel (`.xlsx`)
or CSV (`.csv`) formats. This includes: contacts, products, bank statements,
journal entries, and orders.

Open the view of the object to which the data should be imported/populated,
and click on ⭐ Favorites ‣ Import records.

![Favorites menu revealed with the import records option
highlighted.](../../_images/import-button.png)

After clicking **Import records** , Konvergo ERP reveals a separate page with
templates that can be downloaded and populated with the company’s own data.
Such templates can be imported in one click, since the data mapping is already
done. To download a template click **Import Template for Customers** at the
center of the page.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>When importing a <abbr title="Comma-separated Values">CSV</abbr> file, Konvergo ERP provides <b>Formatting</b>
options. These options do <b>not</b> appear when importing the proprietary Excel file type (<code>.xls</code>,
<code>.xlsx</code>).</p>
<img alt="Formatting options presented when a CVS file is imported in Konvergo ERP." class="align-center" src="../../_images/formatting.png"/>
</div>

Make necessary adjustments to the _Formatting_ options, and ensure all columns
in the **Konvergo ERP field** and **File Column** are free of errors. Finally, click
**Import** to import the data.

### Adapt a template

Import templates are provided in the import tool of the most common data to
import (contacts, products, bank statements, etc.). Open them with any
spreadsheet software (_Microsoft Office_ , _OpenOffice_ , _Google Drive_ ,
etc.).

Once the template is downloaded, proceed to follow these steps:

  * Add, remove, and sort columns to best fit the data structure.

  * It is strongly advised to **not** remove the **External ID** (ID) column (see why in the next section).

  * Set a unique ID to every record by dragging down the ID sequencing in the **External ID** (ID) column.

![An animation of the mouse dragging down the ID column, so each record has a
unique ID.](../../_images/dragdown.gif) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When a new column is added, Konvergo ERP may not be able to map it automatically, if its label does not
fit any field within Konvergo ERP. However, new columns can be mapped manually when the import is tested.
Search the drop-down menu for the corresponding field.</p>
<img alt="Drop-down menu expanded in the initial import screen on Konvergo ERP." class="align-center" src="../../_images/field_list.png"/>
<p>Then, use this field’s label in the import file to ensure future imports are successful.</p>
</div>
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Another useful way to find out the proper column names to import is to export a sample file
using the fields that should be imported. This way, if there is not a sample import template,
the names are accurate.</p>
</div>

### Import from another application

The **External ID** (ID) is a unique identifier for the line item. Feel free
to use one from previous software to facilitate the transition to Konvergo ERP.

La définition d’un ID n’est pas obligatoire lors de l’importation, mais elle
est utile dans de nombreux cas :

  * Update imports: import the same file several times without creating duplicates.

  * Import relation fields.

To recreate relationships between different records, the unique identifier
from the original application should be used to map it to the **External ID**
(ID) column in Konvergo ERP.

When another record is imported that links to the first one, use **XXX/ID**
(XXX/External ID) for the original unique identifier. This record can also be
found using its name.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>It should be noted that there will be a conflict if two or more records have the same name.</p>
</div>

The **External ID** (ID) can also be used to update the original import, if
modified data needs to be re-imported later, therefore, it is a good practice
to specify it whenever possible.

### Field missing to map column

Konvergo ERP heuristically tries to find the type of field for each column inside the
imported file, based on the first ten lines of the files.

For example, if there is a column only containing numbers, only the fields
with the _integer_ type are presented as options.

While this behavior might be beneficial in most cases, it is also possible
that it could fail, or the column may be mapped to a field that is not
proposed by default.

If this happens, check the **Show fields of relation fields (advanced)
option** , then a complete list of fields becomes available for each column.

![Searching for the field to match the tax
column.](../../_images/field_list.png)

### Change data import format

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP can automatically detect if a column is a date, and tries to guess the date format from a
set of most commonly used date formats. While this process can work for many date formats, some
date formats are not recognizable. This can cause confusion, due to day-month inversions; it is
difficult to guess which part of a date format is the day, and which part is the month, in a
date, such as <code>01-03-2016</code>.</p>
</div>

When importing a CSV file, Konvergo ERP provides **Formatting** options.

To view which date format Konvergo ERP has found from the file, check the **Date
Format** that is shown when clicking on options under the file selector. If
this format is incorrect, change it to the preferred format using _ISO 8601_
to define the format.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p><em>ISO 8601</em> is an international standard, covering the worldwide exchange, along with the
communication of date and time-related data. For example, the date format should be <code>YYYY-MM-DD</code>.
So, in the case of July 24th 1981, it should be written as <code>1981-07-24</code>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>0

### Import numbers with currency signs

Konvergo ERP fully supports numbers with parenthesis to represent negative signs, as
well as numbers with currency signs attached to them. Konvergo ERP also automatically
detects which thousand/decimal separator is used. If a currency symbol unknown
to Konvergo ERP is used, it might not be recognized as a number, and the import
crashes.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>1

Examples of supported numbers (using “thirty-two thousand” as the figure):

  * 32.000,00

  * 32000,00

  * 32,000.00

  * -32000.00

  * (32000.00)

  * $ 32.000,00

  * (32000.00 €)

Exemple de ce qui ne fonctionne pas :

  * ABC 32.000,00

  * $ (32.000,00)

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>2

### Import preview table not displayed correctly

By default, the import preview is set on commas as field separators, and
quotation marks as text delimiters. If the CSV file does not have these
settings, modify the **Formatting** options (displayed under the **Import**
CSV file bar after selecting the CSV file).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>3

### Change CSV file format in spreadsheet application

When editing and saving CSV files in spreadsheet applications, the computer’s
regional settings are applied for the separator and delimiter. Konvergo ERP suggests
using _OpenOffice_ or _LibreOffice_ , as both applications allow modifications
of all three options (from _LibreOffice_ application, go to “Save As” dialog
box ‣ Check the box “Edit filter settings” ‣ Save).

Microsoft Excel can modify the encoding when saving (“Save As” dialog box ‣
“Tools” drop-down menu ‣ Encoding tab).

### Difference between Database ID and External ID

Some fields define a relationship with another object. For example, the
country of a contact is a link to a record of the “Country” object. When such
fields are imported, Konvergo ERP has to recreate links between the different records.
To help import such fields, Konvergo ERP provides three mechanisms.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is helpful to know the field’s external identifier. For example, <b>Related Company</b>
in the export user interface is equal to <em>parent_id</em> (external identifier). This is helpful
because then, the only data exported is what should be modified and re-imported.</p>
</div>4

For example, to reference the country of a contact, Konvergo ERP proposes three
different fields to import:

  * **Country** : the name or code of the country

  * **Country/Database ID** : the unique Konvergo ERP ID for a record, defined by the ID PostgreSQL column

  * **Country/External ID** : the ID of this record referenced in another application (or the `.XML` file that imported it)

For the country of Belgium, for example, use one of these three ways to
import:

  * **Country** : `Belgium`

  * **Country/Database ID** : `21`

  * **Country/External ID** : `base.be`

According to the company’s need, use one of these three ways to reference
records in relations. Here is an example when one or the other should be used,
according to the need:

  * Use **Country** : this is the easiest way when data comes from CSV files that have been created manually.

  * Use **Country/Database ID** : this should rarely be used. It is mostly used by developers as the main advantage is to never have conflicts (there may be several records with the same name, but they always have a unique Database ID)

  * Use **Country/External ID** : use _External ID_ when importing data from a third-party application.

When _External IDs_ are used, import CSV files with the **External ID** (ID)
column defining the _External ID_ of each record that is imported. Then, a
reference can be made to that record with columns, like `Field/External ID`.
The following two CSV files provide an example for products and their
categories.

  * [`CSV file for categories`](../../_downloads/b00ebfcb154b6770ed0398d1a9aeb3bd/External_id_3rd_party_application_product_categories.csv)

  * [`CSV file for Products`](../../_downloads/c3355b134fea5ce15f88558701029667/External_id_3rd_party_application_products.csv)

### Import relation fields

An Konvergo ERP object is always related to many other objects (e.g. a product is
linked to product categories, attributes, vendors, etc.). To import those
relations, the records of the related object need to be imported first, from
their own list menu.

This can be achieved by using either the name of the related record, or its
ID, depending on the circumstances. The ID is expected when two records have
the same name. In such a case add `/ ID` at the end of the column title (e.g.
for product attributes: `Product Attributes / Attribute / ID`).

#### Options for multiple matches on fields

If, for example, there are two product categories with the child name
`Sellable` (e.g. `Misc. Products/Sellable` & `Other Products/Sellable`), the
validation is halted, but the data may still be imported. However, Konvergo ERP
recommends that the data is not imported because it will all be linked to the
first `Sellable` category found in the _Product Category_ list (`Misc.
Products/Sellable`). Konvergo ERP, instead, recommends modifying one of the
duplicate’s values, or the product category hierarchy.

However, if the company does not wish to change the configuration of product
categories, Konvergo ERP recommends making use of the _External ID_ for this field,
“Category”.

#### Import many2many relationship fields

The tags should be separated by a comma, without any spacing. For example, if
a customer needs to be linked to both tags: `Manufacturer` and `Retailer` then
“Manufacturer,Retailer” needs to be encoded in the same column of the CSV
file.

  * [`Fichier CSV pour Fabricant, Détaillant`](../../_downloads/3e57aa5f999e49c58169bf4ac7eb0afb/m2m_customers_tags.csv)

#### Import one2many relationships

If a company wants to import a sales order with several order lines, a
specific row **must** be reserved in the CSV file for each order line. The
first order line is imported on the same row as the information relative to
order. Any additional lines need an additional row that does not have any
information in the fields relative to the order.

As an example, here is a CSV file of some quotations that can be imported,
based on demo data:

  * [`File for some Quotations`](../../_downloads/bdf01933a07f1490224f9d53de24764b/purchase.order_functional_error_line_cant_adpat.csv)

The following CSV file shows how to import purchase orders with their
respective purchase order lines:

  * [`Purchase orders with their respective purchase order lines`](../../_downloads/a72f76fb9667dfb8c2795ec523e6f4b3/o2m_purchase_order_lines.csv)

The following CSV file shows how to import customers and their respective
contacts:

  * [`Customers and their respective contacts`](../../_downloads/e4356873a7ad7151783745c8228f370a/o2m_customers_contacts.csv)

### Import records several times

If an imported file contains one of the columns: **External ID** or **Database
ID** , records that have already been imported are modified, instead of being
created. This is extremely useful as it allows users to import the same CSV
file several times, while having made some changes in between two imports.

Konvergo ERP takes care of creating or modifying each record, depending if it is new
or not.

This feature allows a company to use the _Import/Export tool_ in Konvergo ERP to
modify a batch of records in a spreadsheet application.

### Value not provided for a specific field

If all fields are not set in the CSV file, Konvergo ERP assigns the default value for
every non-defined field. But, if fields are set with empty values in the CSV
file, Konvergo ERP sets the empty value in the field, instead of assigning the default
value.

### Export/import different tables from an SQL application to Konvergo ERP

If data needs to be imported from different tables, relations need to be
recreated between records belonging to different tables. For instance, if
companies and people are imported, the link between each person and the
company they work for needs to be recreated.

To manage relations between tables, use the `External ID` facilities of Konvergo ERP.
The `External ID` of a record is the unique identifier of this record in
another application. The `External ID` must be unique across all records of
all objects. It is a good practice to prefix this `External ID` with the name
of the application or table. (like, “company_1”, “person_1” - instead of “1”)

As an example, suppose there is an SQL database with two tables that are to be
imported: companies and people. Each person belongs to one company, so the
link between a person and the company they work for must be recreated.

Test this example, with a [`sample of a PostgreSQL
database`](../../_downloads/6a43d52743cdb4f58e92cdf08131b012/database_import_test.sql).

First, export all companies and their _External ID_. In PSQL, write the
following command:

    
    
    > copy (select 'company_'||id as "External ID",company_name as "Name",'True' as "Is a Company" from companies) TO '/tmp/company.csv' with CSV HEADER;
    

This SQL command creates the following CSV file:

    
    
    External ID,Name,Is a Company
    company_1,Bigees,True
    company_2,Organi,True
    company_3,Boum,True
    

To create the CSV file for people linked to companies, use the following SQL
command in PSQL:

    
    
    > copy (select 'person_'||id as "External ID",person_name as "Name",'False' as "Is a Company",'company_'||company_id as "Related Company/External ID" from persons) TO '/tmp/person.csv' with CSV
    

It produces the following CSV file:

    
    
    External ID,Name,Is a Company,Related Company/External ID
    person_1,Fabien,False,company_1
    person_2,Laurence,False,company_1
    person_3,Eric,False,company_2
    person_4,Ramsy,False,company_3
    

In this file, Fabien and Laurence are working for the Bigees company
(`company_1`), and Eric is working for the Organi company. The relation
between people and companies is done using the _External ID_ of the companies.
The _External ID_ is prefixed by the name of the table to avoid a conflict of
ID between people and companies (`person_1` and `company_1`, who shared the
same ID 1 in the original database).

The two files produced are ready to be imported in Konvergo ERP without any
modifications. After having imported these two CSV files, there are four
contacts and three companies (the first two contacts are linked to the first
company). Keep in mind to first import the companies, and then the people.

  *[CSV]: Comma-separated Values

