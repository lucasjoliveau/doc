# Chapter 8: Relations Between Models

The [previous chapter](07_basicviews#tutorials-getting-
started-07-basicviews) covered the creation of custom views for a model
containing basic fields. However, in any real business scenario we need more
than one model. Moreover, links between models are necessary. One can easily
imagine one model containing the customers and another one containing the list
of users. You might need to refer to a customer or a user on any existing
business model.

In our real estate module, we want the following information for a property:

  * the customer who bought the property

  * the real estate agent who sold the property

  * the property type: house, apartment, penthouse, castle…

  * a list of tags characterizing the property: cozy, renovated…

  * a list of the offers received

## Many2one

**Reference** : the documentation related to this topic can be found in
`Many2one`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>a new <code>estate.property.type</code> model should be created with the corresponding menu, action and views.</p></li>
</ul>
<img alt="Property type" class="align-center" src="../../../_images/property_type.png"/>
<ul>
<li><p>three Many2one fields should be added to the <code>estate.property</code> model: property type, buyer and seller.</p></li>
</ul>
<img alt="Property" class="align-center" src="../../../_images/property_many2one.png"/>
</div>

In our real estate module, we want to define the concept of property type. A
property type is, for example, a house or an apartment. It is a standard
business need to categorize properties according to their type, especially to
refine filtering.

A property can have **one** type, but the same type can be assigned to
**many** properties. This is supported by the **many2one** concept.

A many2one is a simple link to another object. For example, in order to define
a link to the `res.partner` in our test model, we can write:

    
    
    partner_id = fields.Many2one("res.partner", string="Partner")
    

By convention, many2one fields have the `_id` suffix. Accessing the data in
the partner can then be easily done with:

    
    
    print(my_test_object.partner_id.name)
    

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://www.postgresql.org/docs/12/tutorial-fk">foreign keys</a></p>
</div>

In practice a many2one can be seen as a dropdown list in a form view.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the Real Estate Property Type table.</p>
<ul>
<li><p>Create the <code>estate.property.type</code> model and add the following field:</p></li>
</ul>
<table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Attributes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>name</p></td>
<td><p>Char</p></td>
<td><p>required</p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Add the menus as displayed in this section’s <b>Goal</b></p></li>
<li><p>Add the field <code>property_type_id</code> into your <code>estate.property</code> model and its form, tree
and search views</p></li>
</ul>
<p>This exercise is a good recap of the previous chapters: you need to create a
<a href="04_basicmodel#tutorials-getting-started-04-basicmodel"><span class="std std-ref">model</span></a>, set the
<a href="05_securityintro#tutorials-getting-started-05-securityintro"><span class="std std-ref">model</span></a>, add an
<a href="06_firstui#tutorials-getting-started-06-firstui"><span class="std std-ref">action and a menu</span></a>, and
<a href="07_basicviews#tutorials-getting-started-07-basicviews"><span class="std std-ref">create a view</span></a>.</p>
<p>Tip: do not forget to import any new Python files in <code>__init__.py</code>, add new data files in
<code>__manifest.py__</code>  or add the access rights ;-)</p>
</div>

Once again, restart the server and refresh to see the results!

In the real estate module, there are still two missing pieces of information
we want on a property: the buyer and the salesperson. The buyer can be any
individual, but on the other hand the salesperson must be an employee of the
real estate agency (i.e. an Konvergo ERP user).

In Konvergo ERP, there are two models which we commonly refer to:

  * `res.partner`: a partner is a physical or legal entity. It can be a company, an individual or even a contact address.

  * `res.users`: the users of the system. Users can be ‘internal’, i.e. they have access to the Konvergo ERP backend. Or they can be ‘portal’, i.e. they cannot access the backend, only the frontend (e.g. to access their previous orders in eCommerce).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the buyer and the salesperson.</p>
<p>Add a buyer and a salesperson to the <code>estate.property</code> model using the two common models
mentioned above. They should be added in a new tab of the form view, as depicted in this section’s <b>Goal</b>.</p>
<p>The default value for the salesperson must be the current user. The buyer should not be copied.</p>
<p>Tip: to get the default value, check the note below or look at an example
<a href="https://github.com/odoo/odoo/blob/5bb8b927524d062be32f92eb326ef64091301de1/addons/crm/models/crm_lead.py#L92">here</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The object <code>self.env</code> gives access to request parameters and other useful
things:</p>
<ul>
<li><p><code>self.env.cr</code> or <code>self._cr</code> is the database <em>cursor</em> object; it is
used for querying the database</p></li>
<li><p><code>self.env.uid</code> or <code>self._uid</code> is the current user’s database id</p></li>
<li><p><code>self.env.user</code> is the current user’s record</p></li>
<li><p><code>self.env.context</code> or <code>self._context</code> is the context dictionary</p></li>
<li><p><code>self.env.ref(xml_id)</code> returns the record corresponding to an XML id</p></li>
<li><p><code>self.env[model_name]</code> returns an instance of the given model</p></li>
</ul>
</div>

Now let’s have a look at other types of links.

## Many2many

**Reference** : the documentation related to this topic can be found in
`Many2many`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>a new <code>estate.property.tag</code> model should be created with the corresponding menu and action.</p></li>
</ul>
<img alt="Property tag" class="align-center" src="../../../_images/property_tag.png"/>
<ul>
<li><p>tags should be added to the <code>estate.property</code> model:</p></li>
</ul>
<img alt="Property" class="align-center" src="../../../_images/property_many2many.png"/>
</div>

In our real estate module, we want to define the concept of property tags. A
property tag is, for example, a property which is ‘cozy’ or ‘renovated’.

A property can have **many** tags and a tag can be assigned to **many**
properties. This is supported by the **many2many** concept.

A many2many is a bidirectional multiple relationship: any record on one side
can be related to any number of records on the other side. For example, in
order to define a link to the `account.tax` model on our test model, we can
write:

    
    
    tax_ids = fields.Many2many("account.tax", string="Taxes")
    

By convention, many2many fields have the `_ids` suffix. This means that
several taxes can be added to our test model. It behaves as a list of records,
meaning that accessing the data must be done in a loop:

    
    
    for tax in my_test_object.tax_ids:
        print(tax.name)
    

A list of records is known as a _recordset_ , i.e. an ordered collection of records. It supports standard Python operations on collections, such as `len()` and `iter()`, plus extra set operations like `recs1 | recs2`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the Real Estate Property Tag table.</p>
<ul>
<li><p>Create the <code>estate.property.tag</code> model and add the following field:</p></li>
</ul>
<table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Attributes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>name</p></td>
<td><p>Char</p></td>
<td><p>required</p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Add the menus as displayed in this section’s <b>Goal</b></p></li>
<li><p>Add the field <code>tag_ids</code> to your <code>estate.property</code> model and in its form and tree views</p></li>
</ul>
<p>Tip: in the view, use the <code>widget="many2many_tags"</code> attribute as demonstrated
<a href="https://github.com/odoo/odoo/blob/5bb8b927524d062be32f92eb326ef64091301de1/addons/crm_iap_lead_website/views/crm_reveal_views.xml#L36">here</a>.
The <code>widget</code> attribute will be explained in detail in <a href="12_sprinkles#tutorials-getting-started-12-sprinkles"><span class="std std-ref">a later chapter of the training</span></a>.
For now, you can try to adding and removing it and see the result ;-)</p>
</div>

## One2many

**Reference** : the documentation related to this topic can be found in
`One2many`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>a new <code>estate.property.offer</code> model should be created with the corresponding form and tree view.</p></li>
<li><p>offers should be added to the <code>estate.property</code> model:</p></li>
</ul>
<img alt="Property offers" class="align-center" src="../../../_images/property_offer.png"/>
</div>

In our real estate module, we want to define the concept of property offers. A
property offer is an amount a potential buyer offers to the seller. The offer
can be lower or higher than the expected price.

An offer applies to **one** property, but the same property can have **many**
offers. The concept of **many2one** appears once again. However, in this case
we want to display the list of offers for a given property so we will use the
**one2many** concept.

A one2many is the inverse of a many2one. For example, we defined on our test
model a link to the `res.partner` model thanks to the field `partner_id`. We
can define the inverse relation, i.e. the list of test models linked to our
partner:

    
    
    test_ids = fields.One2many("test_model", "partner_id", string="Tests")
    

The first parameter is called the `comodel` and the second parameter is the
field we want to inverse.

By convention, one2many fields have the `_ids` suffix. They behave as a list
of records, meaning that accessing the data must be done in a loop:

    
    
    for test in partner.test_ids:
        print(test.name)
    

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Because a <code>One2many</code> is a virtual relationship,
there <em>must</em> be a <code>Many2one</code> field defined in the comodel.</p>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the Real Estate Property Offer table.</p>
<ul>
<li><p>Create the <code>estate.property.offer</code> model and add the following fields:</p></li>
</ul>
<table class="table docutils">
<colgroup>
<col style="width: 29%"/>
<col style="width: 37%"/>
<col style="width: 15%"/>
<col style="width: 20%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Attributes</p></th>
<th class="head"><p>Values</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>price</p></td>
<td><p>Float</p></td>
<td></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>status</p></td>
<td><p>Selection</p></td>
<td><p>no copy</p></td>
<td><p>Accepted, Refused</p></td>
</tr>
<tr class="row-even"><td><p>partner_id</p></td>
<td><p>Many2one (<code>res.partner</code>)</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>property_id</p></td>
<td><p>Many2one (<code>estate.property</code>)</p></td>
<td><p>required</p></td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Create a tree view and a form view with the <code>price</code>, <code>partner_id</code> and <code>status</code> fields. No
need to create an action or a menu.</p></li>
<li><p>Add the field <code>offer_ids</code> to your <code>estate.property</code> model and in its form view as
depicted in this section’s <b>Goal</b>.</p></li>
</ul>
</div>

There are several important things to notice here. First, we don’t need an
action or a menu for all models. Some models are intended to be accessed only
through another model. This is the case in our exercise: an offer is always
accessed through a property.

Second, despite the fact that the `property_id` field is required, we did not
include it in the views. How does Konvergo ERP know which property our offer is linked
to? Well that’s part of the magic of using the Konvergo ERP framework: sometimes
things are defined implicitly. When we create a record through a one2many
field, the corresponding many2one is populated automatically for convenience.

Still alive? This chapter is definitely not the easiest one. It introduced a
couple of new concepts while relying on everything that was introduced before.
The [next chapter](09_compute_onchange#tutorials-getting-
started-09-compute-onchange) will be lighter, don’t worry ;-)

