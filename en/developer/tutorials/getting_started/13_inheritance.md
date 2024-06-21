# Chapter 13: Inheritance

A powerful aspect of Konvergo ERP is its modularity. A module is dedicated to a
business need, but modules can also interact with one another. This is useful
for extending the functionality of an existing module. For example, in our
real estate scenario we want to display the list of a salesperson’s properties
directly in the regular user view.

But before going through the specific Konvergo ERP module inheritance, let’s see how
we can alter the behavior of the standard CRUD (Create, Retrieve, Update or
Delete) methods.

## Python Inheritance

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>It should not be possible to delete a property which is not new or canceled.</p></li>
</ul>
<img alt="Unlink" class="align-center" src="../../../_images/unlink.gif"/>
<ul>
<li><p>When an offer is created, the property state should change to ‘Offer Received’</p></li>
<li><p>It should not be possible to create an offer with a lower price than an existing offer</p></li>
</ul>
<img alt="Create" class="align-center" src="../../../_images/create.gif"/>
</div>

In our real estate module, we never had to develop anything specific to be
able to do the standard CRUD actions. The Konvergo ERP framework provides the
necessary tools to do them. In fact, such actions are already included in our
model thanks to classical Python inheritance:

    
    
    from odoo import fields, models
    
    class TestModel(models.Model):
        _name = "test_model"
        _description = "Test Model"
    
        ...
    

Our `class TestModel` inherits from `Model` which provides `create()`,
`read()`, `write()` and `unlink()`.

These methods (and any other method defined on `Model`) can be extended to add
specific business logic:

    
    
    from odoo import fields, models
    
    class TestModel(models.Model):
        _name = "test_model"
        _description = "Test Model"
    
        ...
    
        @api.model
        def create(self, vals):
            # Do some business logic, modify vals...
            ...
            # Then call super to execute the parent method
            return super().create(vals)
    

The decorator `model()` is necessary for the `create()` method because the
content of the recordset `self` is not relevant in the context of creation,
but it is not necessary for the other CRUD methods.

It is also important to note that even though we can directly override the
`unlink()` method, you will almost always want to write a new method with the
decorator `ondelete()` instead. Methods marked with this decorator will be
called during `unlink()` and avoids some issues that can occur during
uninstalling the model’s module when `unlink()` is directly overridden.

In Python 3, `super()` is equivalent to `super(TestModel, self)`. The latter
may be necessary when you need to call the parent method with a modified
recordset.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><ul>
<li><p>It is very important to <b>always</b> call <code>super()</code> to avoid breaking the flow. There are
only a few very specific cases where you don’t want to call it.</p></li>
<li><p>Make sure to <b>always</b> return data consistent with the parent method. For example, if
the parent method returns a <code>dict()</code>, your override must also return a <code>dict()</code>.</p></li>
</ul>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add business logic to the CRUD methods.</p>
<ul>
<li><p>Prevent deletion of a property if its state is not ‘New’ or ‘Canceled’</p></li>
</ul>
<p>Tip: create a new method with the <code>ondelete()</code> decorator and remember that
<code>self</code> can be a recordset with more than one record.</p>
<ul>
<li><p>At offer creation, set the property state to ‘Offer Received’. Also raise an error if the user
tries to create an offer with a lower amount than an existing offer.</p></li>
</ul>
<p>Tip: the <code>property_id</code> field is available in the <code>vals</code>, but it is an <code>int</code>. To
instantiate an <code>estate.property</code> object, use <code>self.env[model_name].browse(value)</code>
(<a href="https://github.com/odoo/odoo/blob/136e4f66cd5cafe7df450514937c7218c7216c93/addons/gamification/models/badge.py#L57">example</a>)</p>
</div>

## Model Inheritance

**Reference** : the documentation related to this topic can be found in
[Inheritance and extension](../../reference/backend/orm#reference-orm-
inheritance).

In our real estate module, we would like to display the list of properties
linked to a salesperson directly in the Settings / Users & Companies / Users
form view. To do this, we need to add a field to the `res.users` model and
adapt its view to show it.

Konvergo ERP provides two _inheritance_ mechanisms to extend an existing model in a
modular way.

The first inheritance mechanism allows modules to modify the behavior of a
model defined in an another module by:

  * adding fields to the model,

  * overriding the definition of fields in the model,

  * adding constraints to the model,

  * adding methods to the model,

  * overriding existing methods in the model.

The second inheritance mechanism (delegation) allows every record of a model
to be linked to a parent model’s record and provides transparent access to the
fields of this parent record.

![Inheritance Methods](../../../_images/inheritance_methods1.png)

In Konvergo ERP, the first mechanism is by far the most used. In our case, we want to
add a field to an existing model, which means we will use the first mechanism.
For example:

    
    
    from odoo import fields, models
    
    class InheritedModel(models.Model):
        _inherit = "inherited.model"
    
        new_field = fields.Char(string="New Field")
    

A practical example where two fields are added to a model can be found
[here](https://github.com/odoo/odoo/blob/60e9410e9aa3be4a9db50f6f7534ba31fea3bc29/addons/account_fleet/models/account_move.py#L39-L47).

By convention, each inherited model is defined in its own Python file. In our
example, it would be `models/inherited_model.py`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a field to Users.</p>
<ul>
<li><p>Add the following field to <code>res.users</code>:</p></li>
</ul>
<table class="table docutils">
<colgroup>
<col style="width: 25%"/>
<col style="width: 75%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>property_ids</p></td>
<td><p>One2many inverse of the field that references the salesperson in
<code>estate.property</code></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Add a domain to the field so it only lists the available properties.</p></li>
</ul>
</div>

In the next section let’s add the field to the view and check that everything
is working well!

## View Inheritance

**Reference** : the documentation related to this topic can be found in
[Inheritance](../../reference/backend/views#reference-views-inheritance).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section, the list of available properties linked
to a salesperson should be displayed in their user form view</p>
<img alt="Users" class="align-center" src="../../../_images/users.png"/>
</div>

Instead of modifying existing views in place (by overwriting them), Konvergo ERP
provides view inheritance where children ‘extension’ views are applied on top
of root views. These extension can both add and remove content from their
parent view.

An extension view references its parent using the `inherit_id` field. Instead
of a single view, its `arch` field contains a number of `xpath` elements that
select and alter the content of their parent view:

    
    
    <record id="inherited_model_view_form" model="ir.ui.view">
        <field name="name">inherited.model.form.inherit.test</field>
        <field name="model">inherited.model</field>
        <field name="inherit_id" ref="inherited.inherited_model_view_form"/>
        <field name="arch" type="xml">
            <!-- find field description and add the field
                 new_field after it -->
            <xpath expr="//field[@name='description']" position="after">
              <field name="new_field"/>
            </xpath>
        </field>
    </record>
    

`expr`

    

An [XPath](https://w3.org/TR/xpath) expression selecting a single element in
the parent view. Raises an error if it matches no element or more than one

`position`

    

Operation to apply to the matched element:

`inside`

    

appends `xpath`’s body to the end of the matched element

`replace`

    

replaces the matched element with the `xpath`’s body, replacing any `$0` node
occurrence in the new body with the original element

`before`

    

inserts the `xpath`’s body as a sibling before the matched element

`after`

    

inserts the `xpaths`’s body as a sibling after the matched element

`attributes`

    

alters the attributes of the matched element using the special `attribute`
elements in the `xpath`’s body

When matching a single element, the `position` attribute can be set directly
on the element to be found. Both inheritances below have the same result.

    
    
    <xpath expr="//field[@name='description']" position="after">
        <field name="idea_ids" />
    </xpath>
    
    <field name="description" position="after">
        <field name="idea_ids" />
    </field>
    

An example of a view inheritance extension can be found
[here](https://github.com/odoo/odoo/blob/691d1f087040f1ec7066e485d19ce3662dfc6501/addons/account_fleet/views/account_move_views.xml#L3-L17).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add fields to the Users view.</p>
<p>Add the <code>property_ids</code> field to the <code>base.view_users_form</code> in a new notebook page.</p>
<p>Tip: an example an inheritance of the users’ view can be found
<a href="https://github.com/odoo/odoo/blob/691d1f087040f1ec7066e485d19ce3662dfc6501/addons/gamification/views/res_users_views.xml#L5-L14">here</a>.</p>
</div>

Inheritance is extensively used in Konvergo ERP due to its modular concept. Do not
hesitate to read the corresponding documentation for more info!

In the [next chapter](14_other_module#tutorials-getting-started-14-other-
module), we will learn how to interact with other modules.

