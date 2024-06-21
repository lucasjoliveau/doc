# Chapter 6: Finally, Some UI To Play With

Now that we’ve created our new [model](04_basicmodel#tutorials-getting-
started-04-basicmodel) and its corresponding [access
rights](05_securityintro#tutorials-getting-started-05-securityintro), it
is time to interact with the user interface.

At the end of this chapter, we will have created a couple of menus in order to
access a default list and form view.

## Data Files (XML)

**Reference** : the documentation related to this topic can be found in [Data
Files](../../reference/backend/data#reference-data).

In [Chapter 5: Security - A Brief
Introduction](05_securityintro#tutorials-getting-
started-05-securityintro), we added data through a CSV file. The CSV format is
convenient when the data to load has a simple format. When the format is more
complex (e.g. load the structure of a view or an email template), we use the
XML format. For example, this [help
field](https://github.com/odoo/odoo/blob/09c59012bf80d2ccbafe21c39e604d6cfda72924/addons/crm/views/crm_lost_reason_views.xml#L61-L69)
contains HTML tags. While it would be possible to load such data through a CSV
file, it is more convenient to use an XML file.

The XML files must be added to the same folders as the CSV files and defined
similarly in the `__manifest__.py`. The content of the data files is also
sequentially loaded when a module is installed or updated, therefore all
remarks made for CSV files hold true for XML files. When the data is linked to
views, we add them to the `views` folder.

In this chapter, we will load our first action and menus through an XML file.
Actions and menus are standard records in the database.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When performance is important, the CSV format is preferred over the XML format. This is the case in Konvergo ERP
where loading a CSV file is faster than loading an XML file.</p>
</div>

In Konvergo ERP, the user interface (actions, menus and views) is largely defined by
creating and composing records defined in an XML file. A common pattern is
Menu > Action > View. To access records the user navigates through several
menu levels; the deepest level is an action which triggers the opening of a
list of the records.

## Actions

**Reference** : the documentation related to this topic can be found in
[Actions](../../reference/backend/actions#reference-actions).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, an action should be loaded in the system. We won’t see
anything yet in the UI, but the file should be loaded in the log:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>INFO rd-demo odoo.modules.loading: loading estate/views/estate_property_views.xml
</pre></div>
</div>
</div>

Actions can be triggered in three ways:

  1. by clicking on menu items (linked to specific actions)

  2. by clicking on buttons in views (if these are connected to actions)

  3. as contextual actions on object

We will only cover the first case in this chapter. The second case will be
covered in a [later chapter](10_actions#tutorials-getting-
started-10-actions) while the last is the focus of an advanced topic. In our
Real Estate example, we would like to link a menu to the `estate.property`
model, so we are able to create a new record. The action can be viewed as the
link between the menu and the model.

A basic action for our `test_model` is:

    
    
    <record id="test_model_action" model="ir.actions.act_window">
        <field name="name">Test action</field>
        <field name="res_model">test_model</field>
        <field name="view_mode">tree,form</field>
    </record>
    

  * `id` is an [external identifier](../../glossary#term-external-identifier). It can be used to refer to the record (without knowing its in-database identifier).

  * `model` has a fixed value of `ir.actions.act_window` ([Window Actions (ir.actions.act_window)](../../reference/backend/actions#reference-actions-window)).

  * `name` is the name of the action.

  * `res_model` is the model which the action applies to.

  * `view_mode` are the views that will be available; in this case they are the list (tree) and form views. We’ll see [later](15_qwebintro#tutorials-getting-started-15-qwebintro) that there can be other view modes.

Examples can be found everywhere in Konvergo ERP, but
[this](https://github.com/odoo/odoo/blob/09c59012bf80d2ccbafe21c39e604d6cfda72924/addons/crm/views/crm_lost_reason_views.xml#L57-L70)
is a good example of a simple action. Pay attention to the structure of the
XML data file since you will need it in the following exercise.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add an action.</p>
<p>Create the <code>estate_property_views.xml</code> file in the appropriate folder and define it in the
<code>__manifest__.py</code> file.</p>
<p>Create an action for the model <code>estate.property</code>.</p>
</div>

Restart the server and you should see the file loaded in the log.

## Menus

**Reference** : the documentation related to this topic can be found in
[Shortcuts](../../reference/backend/data#reference-data-shortcuts).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, three menus should be created and the default view is
displayed:</p>
<img alt="Root menus" class="align-center" src="../../../_images/estate_menu_root.png"/>
<img alt="First level and action menus" class="align-center" src="../../../_images/estate_menu_action.png"/>
<img alt="Default form view" class="align-center" src="../../../_images/estate_form_default.png"/>
</div>

To reduce the complexity in declaring a menu (`ir.ui.menu`) and connecting it
to the corresponding action, we can use the `<menuitem>` shortcut .

A basic menu for our `test_model_action` is:

    
    
    <menuitem id="test_model_menu_action" action="test_model_action"/>
    

The menu `test_model_menu_action` is linked to the action `test_model_action`,
and the action is linked to the model `test_model`. As previously mentioned,
the action can be seen as the link between the menu and the model.

However, menus always follow an architecture, and in practice there are three
levels of menus:

  1. The root menu, which is displayed in the App switcher (the Konvergo ERP Community App switcher is a dropdown menu)

  2. The first level menu, displayed in the top bar

  3. The action menus

![Root menus](../../../_images/menu_01.png) ![First level and action
menus](../../../_images/menu_02.png)

The easiest way to define the structure is to create it in the XML file. A
basic structure for our `test_model_action` is:

    
    
    <menuitem id="test_menu_root" name="Test">
        <menuitem id="test_first_level_menu" name="First Level">
            <menuitem id="test_model_menu_action" action="test_model_action"/>
        </menuitem>
    </menuitem>
    

The name for the third menu is taken from the name of the `action`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add menus.</p>
<p>Create the <code>estate_menus.xml</code> file in the appropriate folder and define it in the
<code>__manifest__.py</code> file. Remember the sequential loading of the data files ;-)</p>
<p>Create the three levels of menus for the <code>estate.property</code> action created in the previous
exercise. Refer to the <b>Goal</b> of this section for the expected result.</p>
</div>

Restart the server and **refresh the browser**1. You should now see the menus,
and you’ll even be able to create your first real estate property
advertisement!

## Fields, Attributes And View

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, the selling price should be read-only and the number
of bedrooms and the availability date should have default values. Additionally the selling price
and availability date values won’t be copied when the record is duplicated.</p>
<img alt="Interaction between model and view" class="align-center" src="../../../_images/attribute_and_default.gif"/>
<p>The reserved fields <code>active</code> and <code>state</code> are added to the <code>estate.property</code> model.</p>
</div>

So far we have only used the generic view for our real estate property
advertisements, but in most cases we want to fine tune the view. There are
many fine-tunings possible in Konvergo ERP, but usually the first step is to make sure
that:

  * some fields have a default value

  * some fields are read-only

  * some fields are not copied when duplicating the record

In our real estate business case, we would like the following:

  * The selling price should be read-only (it will be automatically filled in later)

  * The availability date and the selling price should not be copied when duplicating a record

  * The default number of bedrooms should be 2

  * The default availability date should be in 3 months

### Some New Attributes

Before moving further with the view design, let’s step back to our model
definition. We saw that some attributes, such as `required=True`, impact the
table schema in the database. Other attributes will impact the view or provide
default values.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add new attributes to the fields.</p>
<p>Find the appropriate attributes (see <code>Field</code>) to:</p>
<ul>
<li><p>set the selling price as read-only</p></li>
<li><p>prevent copying of the availability date and the selling price values</p></li>
</ul>
</div>

Restart the server and refresh the browser. You should not be able to set any
selling prices. When duplicating a record, the availability date should be
empty.

### Default Values

Any field can be given a default value. In the field definition, add the
option `default=X` where `X` is either a Python literal value (boolean,
integer, float, string) or a function taking a model and returning a value:

    
    
    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    

The `name` field will have the value ‘Unknown’ by default while the
`last_seen` field will be set as the current time.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Set default values.</p>
<p>Add the appropriate default attributes so that:</p>
<ul>
<li><p>the default number of bedrooms is 2</p></li>
<li><p>the default availability date is in 3 months</p></li>
</ul>
<p>Tip: this might help you: <code>today()</code></p>
</div>

Check that the default values are set as expected.

### Reserved Fields

**Reference** : the documentation related to this topic can be found in
[Reserved Field names](../../reference/backend/orm#reference-orm-fields-
reserved).

A few field names are reserved for pre-defined behaviors. They should be
defined on a model when the related behavior is desired.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add active field.</p>
<p>Add the <code>active</code> field to the <code>estate.property</code> model.</p>
</div>

Restart the server, create a new property, then come back to the list view…
The property will not be listed! `active` is an example of a reserved field
with a specific behavior: when a record has `active=False`, it is
automatically removed from any search. To display the created property, you
will need to specifically search for inactive records.

![Inactive records](../../../_images/inactive.gif) <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Set a default value for active field.</p>
<p>Set the appropriate default value for the <code>active</code> field so it doesn’t disappear anymore.</p>
</div>

Note that the default `active=False` value was assigned to all existing
records.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, an action should be loaded in the system. We won’t see
anything yet in the UI, but the file should be loaded in the log:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>INFO rd-demo odoo.modules.loading: loading estate/views/estate_property_views.xml
</pre></div>
</div>
</div>0

The `state` will be used later on for several UI enhancements.

Now that we are able to interact with the UI thanks to the default views, the
next step is obvious: we want to define [our own
views](07_basicviews#tutorials-getting-started-07-basicviews).

1

    

A refresh is needed since the web client keeps a cache of the various menus
and views for performance reasons.

