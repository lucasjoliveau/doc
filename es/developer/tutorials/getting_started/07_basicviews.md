# Chapter 7: Basic Views

We have seen in the [previous chapter](06_firstui#tutorials-getting-
started-06-firstui) that Konvergo ERP is able to generate default views for a given
model. In practice, the default view is **never** acceptable for a business
application. Instead, we should at least organize the various fields in a
logical manner.

Views are defined in XML files with actions and menus. They are instances of
the `ir.ui.view` model.

In our real estate module, we need to organize the fields in a logical way:

  * in the list (tree) view, we want to display more than just the name.

  * in the form view, the fields should be grouped.

  * in the search view, we must be able to search on more than just the name. Specifically, we want a filter for the “Available” properties and a shortcut to group by postcode.

## List

**Reference** : the documentation related to this topic can be found in
[List](../../reference/backend/views#reference-views-list).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>Goal</b>: at the end of this section, the list view should look like this:</p>
<img alt="List view" class="align-center" src="../../../_images/list1.png"/>
</div>

List views, also called tree views, display records in a tabular form.

Their root element is `<tree>`. The most basic version of this view simply
lists all the fields to display in the table (where each field is a column):

    
    
    <tree string="Tests">
        <field name="name"/>
        <field name="last_seen"/>
    </tree>
    

A simple example can be found
[here](https://github.com/odoo/odoo/blob/6da14a3aadeb3efc40f145f6c11fc33314b2f15e/addons/crm/views/crm_lost_reason_views.xml#L46-L54).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a custom list view.</p>
<p>Define a list view for the <code>estate.property</code> model in the appropriate XML file. Check the
<b>Goal</b> of this section for the fields to display.</p>
<p>Tips:</p>
<ul>
<li><p>do not add the <code>editable="bottom"</code> attribute that you can find in the example above. We’ll
come back to it later.</p></li>
<li><p>some field labels may need to be adapted to match the reference.</p></li>
</ul>
</div>

As always, you need to restart the server (do not forget the `-u` option) and
refresh the browser to see the result.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>You will probably use some copy-paste in this chapter, therefore always make sure that the <code>id</code>
remains unique for each view!</p>
</div>

## Form

**Reference** : the documentation related to this topic can be found in
[Form](../../reference/backend/views#reference-views-form).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>Goal</b>: at the end of this section, the form view should look like this:</p>
<img alt="Form view" class="align-center" src="../../../_images/form.png"/>
</div>

Forms are used to create and edit single records.

Their root element is `<form>`. They are composed of high-level structure
elements (groups and notebooks) and interactive elements (buttons and fields):

    
    
    <form string="Test">
        <sheet>
            <group>
                <group>
                    <field name="name"/>
                </group>
                <group>
                    <field name="last_seen"/>
                </group>
                <notebook>
                    <page string="Description">
                        <field name="description"/>
                    </page>
                </notebook>
            </group>
        </sheet>
    </form>
    

It is possible to use regular HTML tags such as `div` and `h1` as well as the
the `class` attribute (Konvergo ERP provides some built-in classes) to fine-tune the
look.

A simple example can be found
[here](https://github.com/odoo/odoo/blob/6da14a3aadeb3efc40f145f6c11fc33314b2f15e/addons/crm/views/crm_lost_reason_views.xml#L16-L44).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a custom form view.</p>
<p>Define a form view for the <code>estate.property</code> model in the appropriate XML file. Check the
<b>Goal</b> of this section for the expected final design of the page.</p>
</div>

This might require some trial and error before you get to the expected result
;-) It is advised that you add the fields and the tags one at a time to help
understand how it works.

In order to avoid relaunching the server every time you do a modification to
the view, it can be convenient to use the `--dev xml` parameter when launching
the server:

    
    
    $ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate --dev xml
    

This parameter allows you to just refresh the page to view your view
modifications.

## Search

**Reference** : the documentation related to this topic can be found in
[Search](../../reference/backend/views#reference-views-search).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>Goal</b>: at the end of this section, the search view should look like this:</p>
<img alt="Search fields" class="align-center" src="../../../_images/search_01.png"/>
<img alt="Filter" class="align-center" src="../../../_images/search_02.png"/>
<img alt="Group By" class="align-center" src="../../../_images/search_03.png"/>
</div>

Search views are slightly different from the list and form views since they
don’t display _content_. Although they apply to a specific model, they are
used to filter other views” content (generally aggregated views such as
[List](../../reference/backend/views#reference-views-list)). Beyond the
difference in use case, they are defined the same way.

Their root element is `<search>`. The most basic version of this view simply
lists all the fields for which a shortcut is desired:

    
    
    <search string="Tests">
        <field name="name"/>
        <field name="last_seen"/>
    </search>
    

The default search view generated by Konvergo ERP provides a shortcut to filter by
`name`. It is very common to add the fields which the user is likely to filter
on in a customized search view.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a custom search view.</p>
<p>Define a search view for the <code>estate.property</code> model in the appropriate XML file. Check the
first image of this section’s <b>Goal</b> for the list of fields.</p>
</div>

After restarting the server, it should be possible to filter on the given
fields.

Search views can also contain `<filter>` elements, which act as toggles for
predefined searches. Filters must have one of the following attributes:

  * `domain`: adds the given domain to the current search

  * `context`: adds some context to the current search; uses the key `group_by` to group results on the given field name

A simple example can be found
[here](https://github.com/odoo/odoo/blob/715a24333bf000d5d98b9ede5155d3af32de067c/addons/delivery/views/delivery_view.xml#L30-L44).

Before going further in the exercise, it is necessary to introduce the
“domain” concept.

### Domains

**Reference** : the documentation related to this topic can be found in
[Search domains](../../reference/backend/orm#reference-orm-domains).

In Konvergo ERP, a domain encodes conditions on records: a domain is a list of
criteria used to select a subset of a model’s records. Each criterion is a
triplet with a _field name_ , an _operator_ and a _value_. A record satisfies
a criterion if the specified field meets the condition of the operator applied
to the value.

For instance, when used on the _Product_ model the following domain selects
all _services_ with a unit price greater than _1000_ :

    
    
    [('product_type', '=', 'service'), ('unit_price', '>', 1000)]
    

By default criteria are combined with an implicit AND, meaning _every_
criterion needs to be satisfied for a record to match a domain. The logical
operators `&` (AND), `|` (OR) and `!` (NOT) can be used to explicitly combine
criteria. They are used in prefix position (the operator is inserted before
its arguments rather than between). For instance, to select products “which
are services _OR_ have a unit price which is _NOT_ between 1000 and 2000”:

    
    
    ['|',
        ('product_type', '=', 'service'),
        '!', '&',
            ('unit_price', '>=', 1000),
            ('unit_price', '<', 2000)]
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>XML does not allow <code>&lt;</code> and <code>&amp;</code> to be used inside XML
elements. To avoid parsing errors, entity references should be used:
<code>&amp;lt;</code> for <code>&lt;</code> and <code>&amp;amp;</code> for <code>&amp;</code>. Other entity references
(<code>&amp;gt;</code>, <code>&amp;apos;</code> &amp; <code>&amp;quot;</code>) are optional.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;filter</span> <span class="na">name=</span><span class="s">"negative"</span> <span class="na">domain=</span><span class="s">"[('test_val', '&amp;lt;', 0)]"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add filter and Group By.</p>
<p>The following should be added to the previously created search view:</p>
<ul>
<li><p>a filter which displays available properties, i.e. the state should be “New” or
“Offer Received”.</p></li>
<li><p>the ability to group results by postcode.</p></li>
</ul>
</div>

Looking good? At this point we are already able to create models and design a
user interface which makes sense business-wise. However, a key component is
still missing: the [link between models](08_relations#tutorials-getting-
started-08-relations).

