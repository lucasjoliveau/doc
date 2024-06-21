# Chapter 1: Architecture Overview

## Multitier application

Konvergo ERP follows a [multitier
architecture](https://en.wikipedia.org/wiki/Multitier_architecture), meaning
that the presentation, the business logic and the data storage are separated.
More specifically, it uses a three-tier architecture (image from Wikipedia):

![Three-tier architecture](../../../_images/three_tier.svg)

The presentation tier is a combination of HTML5, JavaScript and CSS. The logic
tier is exclusively written in Python, while the data tier only supports
PostgreSQL as an RDBMS.

Depending on the scope of your module, Konvergo ERP development can be done in any of
these tiers. Therefore, before going any further, it may be a good idea to
refresh your memory if you don’t have an intermediate level in these topics.

In order to go through this tutorial, you will need a very basic knowledge of
HTML and an intermediate level of Python. Advanced topics will require more
knowledge in the other subjects. There are plenty of tutorials freely
accessible, so we cannot recommend one over another since it depends on your
background.

For reference this is the official [Python
tutorial](https://docs.python.org/3.7/tutorial/).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Since version 15.0, Konvergo ERP is actively transitioning to using its own in-house developed <a href="https://odoo.github.io/owl/">OWL
framework</a> as part of its presentation tier. The legacy JavaScript
framework is still supported but will be deprecated over time. This will be discussed further in
advanced topics.</p>
</div>

## Konvergo ERP modules

Both server and client extensions are packaged as _modules_ which are
optionally loaded in a _database_. A module is a collection of functions and
data that target a single purpose.

Konvergo ERP modules can either add brand new business logic to an Konvergo ERP system or
alter and extend existing business logic. One module can be created to add
your country’s accounting rules to Konvergo ERP’s generic accounting support, while a
different module can add support for real-time visualisation of a bus fleet.

Everything in Konvergo ERP starts and ends with modules.

Terminology: developers group their business features in Konvergo ERP _modules_. The
main user-facing modules are flagged and exposed as _Apps_ , but a majority of
the modules aren’t Apps. _Modules_ may also be referred to as _addons_ and the
directories where the Konvergo ERP server finds them form the `addons_path`.

### Composition of a module

An Konvergo ERP module **can** contain a number of elements:

[Business objects](../../reference/backend/orm#reference-orm)

    

A business object (e.g. an invoice) is declared as a Python class. The fields
defined in these classes are automatically mapped to database columns thanks
to the ORM layer.

[Object views](../../reference/backend/views#reference-views)

    

Define UI display

[Data files](../../reference/backend/data#reference-data)

    

XML or CSV files declaring the model data:

  * [views](../../reference/backend/views#reference-views) or [reports](../../reference/backend/reports#reference-reports),

  * configuration data (modules parametrization, [security rules](../../reference/backend/security#reference-security)),

  * demonstration data

  * and more

[Web controllers](../../reference/backend/http#reference-controllers)

    

Handle requests from web browsers

Static web data

    

Images, CSS or JavaScript files used by the web interface or website

None of these elements are mandatory. Some modules may only add data files
(e.g. country-specific accounting configuration), while others may only add
business objects. During this training, we will create business objects,
object views and data files.

### Module structure

Each module is a directory within a _module directory_. Module directories are
specified by using the [`--addons-path`](../../reference/cli#cmdoption-
odoo-bin-addons-path) option.

An Konvergo ERP module is declared by its
[manifest](../../reference/backend/module#reference-module-manifest).

When an Konvergo ERP module includes business objects (i.e. Python files), they are
organized as a [Python
package](https://docs.python.org/3/tutorial/modules#packages) with a
`__init__.py` file. This file contains import instructions for various Python
files in the module.

Here is a simplified module directory:

    
    
    module
    ├── models
    │   ├── *.py
    │   └── __init__.py
    ├── data
    │   └── *.xml
    ├── __init__.py
    └── __manifest__.py
    

## Konvergo ERP Editions

Konvergo ERP is available in [two versions](https://www.odoo.com/page/editions): Konvergo ERP
Enterprise (licensed & shared sources) and Konvergo ERP Community (open-source). In
addition to services such as support or upgrades, the Enterprise version
provides extra functionalities to Konvergo ERP. From a technical point-of-view, these
functionalities are simply new modules installed on top of the modules
provided by the Community version.

Ready to start? Before writing actual code, let’s go to the [next
chapter](02_setup) to review the Konvergo ERP installation process. Even if Konvergo ERP
is already running on your system, we strongly suggest you go through this
chapter to make sure we start on the same page during the development of our
new application.

  *[ORM]: Object-Relational Mapping

