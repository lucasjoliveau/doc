# Chapter 10: Ready For Some Action?

So far we have mostly built our module by declaring fields and views. We just
introduced business logic in the [previous
chapter](09_compute_onchange#tutorials-getting-started-09-compute-
onchange) thanks to computed fields and onchanges. In any real business
scenario, we would want to link some business logic to action buttons. In our
real estate example, we would like to be able to:

  * cancel or set a property as sold

  * accept or refuse an offer

One could argue that we can already do these things by changing the state
manually, but this is not really convenient. Moreover, we want to add some
extra processing: when an offer is accepted we want to set the selling price
and the buyer for the property.

## Action Type

**Reference** : the documentation related to this topic can be found in
[Actions](../../reference/backend/actions#reference-actions) and [Error
management](../../reference/backend/orm#reference-exceptions).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>You should be able to cancel or set a property as sold:</p></li>
</ul>
<img alt="Cancel and set to sold" class="align-center" src="../../../_images/property.gif"/>
<p>A canceled property cannot be sold and a sold property cannot be canceled. For the sake of
clarity, the <code>state</code> field has been added on the view.</p>
<ul>
<li><p>You should be able to accept or refuse an offer:</p></li>
</ul>
<img alt="Accept or refuse an offer" class="align-center" src="../../../_images/offer_01.gif"/>
<ul>
<li><p>Once an offer is accepted, the selling price and the buyer should be set:</p></li>
</ul>
<img alt="Accept an offer" class="align-center" src="../../../_images/offer_02.gif"/>
</div>

In our real estate module, we want to link business logic with some buttons.
The most common way to do this is to:

  * Add a button in the view, for example in the `header` of the view:

    
    
    <form>
        <header>
            <button name="action_do_something" type="object" string="Do Something"/>
        </header>
        <sheet>
            <field name="name"/>
        </sheet>
    </form>
    

  * and link this button to business logic:

    
    
    from odoo import fields, models
    
    class TestAction(models.Model):
        _name = "test.action"
    
        name = fields.Char()
    
        def action_do_something(self):
            for record in self:
                record.name = "Something"
            return True
    

By assigning `type="object"` to our button, the Konvergo ERP framework will execute a
Python method with `name="action_do_something"` on the given model.

The first important detail to note is that our method name isn’t prefixed with
an underscore (`_`). This makes our method a **public** method, which can be
called directly from the Konvergo ERP interface (through an RPC call). Until now, all
methods we created (compute, onchange) were called internally, so we used
**private** methods prefixed by an underscore. You should always define your
methods as private unless they need to be called from the user interface.

Also note that we loop on `self`. Always assume that a method can be called on
multiple records; it’s better for reusability.

Finally, a public method should always return something so that it can be
called through XML-RPC. When in doubt, just `return True`.

There are hundreds of examples in the Konvergo ERP source code. One example is this
[button in a
view](https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/crm/views/crm_lead_views.xml#L9-L11)
and its [corresponding Python
method](https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/crm/models/crm_lead.py#L746-L760)

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Cancel and set a property as sold.</p>
<ul>
<li><p>Add the buttons “Cancel” and “Sold” to the <code>estate.property</code> model. A canceled property
cannot be set as sold, and a sold property cannot be canceled.</p>
<p>Refer to the first image of the <b>Goal</b> for the expected result.</p>
<p>Tip: in order to raise an error, you can use the <a href="../../reference/backend/orm#reference-exceptions"><span class="std std-ref">UserError</span></a>
function. There are plenty of examples in the Konvergo ERP source code ;-)</p>
</li>
<li><p>Add the buttons “Accept” and “Refuse” to the <code>estate.property.offer</code> model.</p>
<p>Refer to the second image of the <b>Goal</b> for the expected result.</p>
<p>Tip: to use an icon as a button, have a look
<a href="https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/event/views/event_views.xml#L521">at this example</a>.</p>
</li>
<li><p>When an offer is accepted, set the buyer and the selling price for the corresponding property.</p>
<p>Refer to the third image of the <b>Goal</b> for the expected result.</p>
<p>Pay attention: in real life only one offer can be accepted for a given property!</p>
</li>
</ul>
</div>

## Object Type

In [Chapter 6: Finally, Some UI To Play With](06_firstui#tutorials-
getting-started-06-firstui), we created an action that was linked to a menu.
You may be wondering if it is possible to link an action to a button. Good
news, it is! One way to do it is:

    
    
    <button type="action" name="%(test.test_model_action)d" string="My Action"/>
    

We use `type="action"` and we refer to the [external
identifier](../../glossary#term-external-identifier) in the `name`.

In the [next chapter](11_constraints#tutorials-getting-
started-11-constraints) we’ll see how we can prevent encoding incorrect data
in Konvergo ERP.

