# Chapter 14: Interact With Other Modules

In the [previous chapter](13_inheritance#tutorials-getting-
started-13-inheritance), we used inheritance to modify the behavior of a
module. In our real estate scenario, we would like to go a step further and be
able to generate invoices for our customers. Konvergo ERP provides an Invoicing
module, so it would be neat to create an invoice directly from our real estate
module, i.e. once a property is set to ‘Sold’, an invoice is created in the
Invoicing application.

## Concrete Example: Account Move

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Goal</b>: at the end of this section:</p>
<ul>
<li><p>A new module <code>estate_account</code> should be created</p></li>
<li><p>When a property is sold, an invoice should be issued for the buyer</p></li>
</ul>
<img alt="Invoice creation" class="align-center" src="../../../_images/create_inv.gif"/>
</div>

Any time we interact with another module, we need to keep in mind the
modularity. If we intend to sell our application to real estate agencies, some
may want the invoicing feature but others may not want it.

### Link Module

The common approach for such use cases is to create a ‘link’ module. In our
case, the module would depend on `estate` and `account` and would include the
invoice creation logic of the estate property. This way the real estate and
the accounting modules can be installed independently. When both are
installed, the link module provides the new feature.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Create a link module.</p>
<p>Create the <code>estate_account</code> module, which depends on the <code>estate</code> and <code>account</code> modules.
For now, it will be an empty shell.</p>
<p>Tip: you already did this at the
<a href="03_newapp#tutorials-getting-started-03-newapp"><span class="std std-ref">beginning of the tutorial</span></a>. The process is very
similar.</p>
</div>

When the `estate_account` module appears in the list, go ahead and install it!
You’ll notice that the Invoicing application is installed as well. This is
expected since your module depends on it. If you uninstall the Invoicing
application, your module will be uninstalled as well.

### Invoice Creation

It’s now time to generate the invoice. We want to add functionality to the
`estate.property` model, i.e. we want to add some extra logic for when a
property is sold. Does that sound familiar? If not, it’s a good idea to go
back to the [previous chapter](13_inheritance#tutorials-getting-
started-13-inheritance) since you might have missed something ;-)

As a first step, we need to extend the action called when pressing the [‘Sold’
button](10_actions#tutorials-getting-started-10-actions) on a property.
To do so, we need to create a [model
inheritance](13_inheritance#tutorials-getting-started-13-inheritance) in
the `estate_account` module for the `estate.property` model. For now, the
overridden action will simply return the `super` call. Maybe an example will
make things clearer:

    
    
    from odoo import models
    
    class InheritedModel(models.Model):
        _inherit = "inherited.model"
    
        def inherited_action(self):
            return super().inherited_action()
    

A practical example can be found
[here](https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/event_sale/models/account_move.py#L7-L16).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the first step of invoice creation.</p>
<ul>
<li><p>Create a <code>estate_property.py</code> file in the correct folder of the <code>estate_account</code> module.</p></li>
<li><p><code>_inherit</code> the <code>estate.property</code> model.</p></li>
<li><p>Override the <code>action_sold</code> method (you might have named it differently) to return the <code>super</code>
call.</p></li>
</ul>
<p>Tip: to make sure it works, add a <code>print</code> or a debugger breakpoint in the overridden method.</p>
</div>

Is it working? If not, maybe check that all Python files are correctly
imported.

If the override is working, we can move forward and create the invoice.
Unfortunately, there is no easy way to know how to create any given object in
Konvergo ERP. Most of the time, it is necessary to have a look at its model to find
the required fields and provide appropriate values.

A good way to learn is to look at how other modules already do what you want
to do. For example, one of the basic flows of Sales is the creation of an
invoice from a sales order. This looks like a good starting point since it
does exactly what we want to do. Take some time to read and understand the
[_create_invoices](https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/sale/models/sale.py#L610-L717)
method. When you are done crying because this simple task looks awfully
complex, we can move forward in the tutorial.

To create an invoice, we need the following information:

  * a `partner_id`: the customer

  * a `move_type`: it has several [possible values](https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/account/models/account_move.py#L138-L147)

  * a `journal_id`: the accounting journal

This is enough to create an empty invoice.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the second step of invoice creation.</p>
<p>Create an empty <code>account.move</code> in the override of the <code>action_sold</code> method:</p>
<ul>
<li><p>the <code>partner_id</code> is taken from the current <code>estate.property</code></p></li>
<li><p>the <code>move_type</code> should correspond to a ‘Customer Invoice’</p></li>
</ul>
<p>Tips:</p>
<ul>
<li><p>to create an object, use <code>self.env[model_name].create(values)</code>, where <code>values</code>
is a <code>dict</code>.</p></li>
<li><p>the <code>create</code> method doesn’t accept recordsets as field values.</p></li>
</ul>
</div>

When a property is set to ‘Sold’, you should now have a new customer invoice
created in Invoicing / Customers / Invoices.

Obviously we don’t have any invoice lines so far. To create an invoice line,
we need the following information:

  * `name`: a description of the line

  * `quantity`

  * `price_unit`

Moreover, an invoice line needs to be linked to an invoice. The easiest and
most efficient way to link a line to an invoice is to include all lines at
invoice creation. To do this, the `invoice_line_ids` field is included in the
`account.move` creation, which is a `One2many`. One2many and Many2many use
special ‘commands’ which have been made human readable with the `Command`
namespace. This namespace represents a triplet command to execute on a set of
records. The triplet was originally the only option to do these commands, but
it is now standard to use the namespace instead. The format is to place them
in a list which is executed sequentially. Here is a simple example to include
a One2many field `line_ids` at creation of a `test_model`:

    
    
    from odoo import Command
    
    def inherited_action(self):
        self.env["test_model"].create(
            {
                "name": "Test",
                "line_ids": [
                    Command.create({
                        "field_1": "value_1",
                        "field_2": "value_2",
                    })
                ],
            }
        )
        return super().inherited_action()
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add the third step of invoice creation.</p>
<p>Add two invoice lines during the creation of the <code>account.move</code>. Each property sold will
be invoiced following these conditions:</p>
<ul>
<li><p>6% of the selling price</p></li>
<li><p>an additional 100.00 from administrative fees</p></li>
</ul>
<p>Tip: Add the <code>invoice_line_ids</code> at creation following the example above.
For each line, we need a <code>name</code>, <code>quantity</code> and <code>price_unit</code>.</p>
</div>

This chapter might be one of the most difficult that has been covered so far,
but it is the closest to what Konvergo ERP development will be in practice. In the
[next chapter](15_qwebintro#tutorials-getting-started-15-qwebintro), we
will introduce the templating mechanism used in Konvergo ERP.

