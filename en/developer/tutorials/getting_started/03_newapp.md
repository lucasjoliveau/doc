# Chapter 3: A New Application

The purpose of this chapter is to lay the foundation for the creation of a
completely new Konvergo ERP module. We will start from scratch with the minimum needed
to have our module recognized by Konvergo ERP. In the upcoming chapters, we will
progressively add features to build a realistic business case.

## The Real Estate Advertisement module

Our new module will cover a business area which is very specific and therefore
not included in the standard set of modules: real estate. It is worth noting
that before developing a new module, it is good practice to verify that Konvergo ERP
doesn’t already provide a way to answer the specific business case.

Here is an overview of the main list view containing some advertisements:

![List view 01](../../../_images/overview_list_view_01.png)

The top area of the form view summarizes important information for the
property, such as the name, the property type, the postcode and so on. The
first tab contains information describing the property: bedrooms, living area,
garage, garden…

![Form view 01](../../../_images/overview_form_view_01.png)

The second tab lists the offers for the property. We can see here that
potential buyers can make offers above or below the expected selling price. It
is up to the seller to accept an offer.

![Form view 02](../../../_images/overview_form_view_02.png)

Here is a quick video showing the workflow of the module.

Hopefully, this video will be recorded soon :-)

## Prepare the addon directory

**Reference** : the documentation related to this topic can be found in
[manifest](../../reference/backend/module#reference-module-manifest).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: the goal of this section is to have Konvergo ERP recognize our new module, which will
be an empty shell for now. It will be listed in the Apps:</p>
<img alt="The new module appears in the list" class="align-center" src="../../../_images/app_in_list.png"/>
</div>

The first step of module creation is to create its directory. In the
`tutorials` directory, add a new directory `estate`.

A module must contain at least 2 files: the `__manifest__.py` file and a
`__init__.py` file. The `__init__.py` file can remain empty for now and we’ll
come back to it in the next chapter. On the other hand, the `__manifest__.py`
file must describe our module and cannot remain empty. Its only required field
is the `name`, but it usually contains much more information.

Take a look at the [CRM
file](https://github.com/odoo/odoo/blob/fc92728fb2aa306bf0e01a7f9ae1cfa3c1df0e10/addons/crm/__manifest__.py#L1-L67)
as an example. In addition to providing the description of the module (`name`,
`category`, `summary`, `website`…), it lists its dependencies (`depends`). A
dependency means that the Konvergo ERP framework will ensure that these modules are
installed before our module is installed. Moreover, if one of these
dependencies is uninstalled, then our module and **any other that depends on
it will also be uninstalled**. Think about your favorite Linux distribution
package manager (`apt`, `dnf`, `pacman`…): Konvergo ERP works in the same way.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Create the required addon files.</p>
<p>Create the following folders and files:</p>
<ul>
<li><p><code>/home/$USER/src/tutorials/estate/__init__.py</code></p></li>
<li><p><code>/home/$USER/src/tutorials/estate/__manifest__.py</code></p></li>
</ul>
<p>The <code>__manifest__.py</code> file should only define the name and the dependencies of our modules.
The only necessary framework module for now is <code>base</code>.</p>
</div>

Restart the Konvergo ERP server and go to Apps. Click on Update Apps List, search for
`estate` and… tadaaa, your module appears! Did it not appear? Maybe try
removing the default ‘Apps’ filter ;-)

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Remember to enable the <a href="../../../applications/general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> as explained in the previous
chapter. You won’t see the <b>Update Apps List</b> button otherwise.</p>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Make your module an ‘App’.</p>
<p>Add the appropriate key to your <code>__manifest__.py</code> so that the module appears when the ‘Apps’
filter is on.</p>
</div>

You can even install the module! But obviously it’s an empty shell, so no menu
will appear.

All good? If yes, then let’s [create our first
model](04_basicmodel#tutorials-getting-started-04-basicmodel)!

