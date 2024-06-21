# Chapter 3: Custom kanban view

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>It is highly recommended that you complete <a href="01_fields_and_views">Chapter 1: Fields and Views</a> before starting this
chapter. The concepts introduced in Chapter 3, including views and examples, will be essential
for understanding the material covered in this chapter.</p>
</div>

We have gained an understanding of the numerous capabilities offered by the
Konvergo ERP web framework. As a next step, we will customize a kanban view. This is a
more complicated project that will showcase some non trivial aspects of the
framework. The goal is to practice composing views, coordinating various
aspects of the UI, and doing it in a maintainable way.

Bafien had the greatest idea ever: a mix of a kanban view and a list view
would be perfect for your needs! In a nutshell, he wants a list of customers
on the left of the task’s kanban view. When you click on a customer on the
left sidebar, the kanban view on the right is filtered to only display orders
linked to that customer.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview1.png" class="align-center" src="../../../_images/overview1.png"/>
</div> <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>

## 1\. Create a new kanban view

Since we are customizing the kanban view, let us start by extending it and
using our extension in the kanban view for the tshirt orders.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Extend the kanban view by extending the kanban controller and by creating a new view object.</p></li>
<li><p>Register it in the views registry under <code>awesome_tshirt.customer_kanban</code>.</p></li>
<li><p>Update the kanban arch to use the extended view. This can be done with the <code>js_class</code>
attribute.</p></li>
</ol>
</div>

## 2\. Create a CustomerList component

We will need to display a list of customers, so we might as well create the
component.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a <code>CustomerList</code> component which only displays a <code>div</code> with some text for now.</p></li>
<li><p>It should have a <code>selectCustomer</code> prop.</p></li>
<li><p>Create a new template extending (XPath) the kanban controller template to add the
<code>CustomerList</code> next to the kanban renderer. Give it an empty function as <code>selectCustomer</code> for
now.</p></li>
<li><p>Subclass the kanban controller to add <code>CustomerList</code> in its sub-components.</p></li>
<li><p>Make sure you see your component in the kanban view.</p></li>
</ol>
<img alt="../../../_images/customer_list.png" class="align-center" src="../../../_images/customer_list.png" style="width: 627.6px; height: 544.8px;"/>
</div>

## 3\. Load and display data

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Modify the <code>CustomerList</code> component to fetch a list of all customers in <code>onWillStart</code>.</p></li>
<li><p>Display the list in the template with a <code>t-foreach</code>.</p></li>
<li><p>Whenever a customer is selected, call the <code>selectCustomer</code> function prop.</p></li>
</ol>
<img alt="../../../_images/customer_data.png" class="align-center" src="../../../_images/customer_data.png" style="width: 613.1999999999999px; height: 746.4px;"/>
</div>

## 4\. Update the main kanban view

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Implement <code>selectCustomer</code> in the kanban controller to add the proper domain.</p></li>
<li><p>Modify the template to give the real function to the <code>CustomerList</code> <code>selectCustomer</code> prop.</p></li>
</ol>
<p>Since it is not trivial to interact with the search view, here is a quick snippet to help:</p>
<div class="highlight-js notranslate"><div class="highlight"><pre><span></span><span class="nx">selectCustomer</span><span class="p">(</span><span class="nx">customer_id</span><span class="p">,</span> <span class="nx">customer_name</span><span class="p">)</span> <span class="p">{</span>
   <span class="k">this</span><span class="p">.</span><span class="nx">env</span><span class="p">.</span><span class="nx">searchModel</span><span class="p">.</span><span class="nx">setDomainParts</span><span class="p">({</span>
      <span class="nx">customer</span><span class="o">:</span> <span class="p">{</span>
            <span class="nx">domain</span><span class="o">:</span> <span class="p">[[</span><span class="s2">"customer_id"</span><span class="p">,</span> <span class="s2">"="</span><span class="p">,</span> <span class="nx">customer_id</span><span class="p">]],</span>
            <span class="nx">facetLabel</span><span class="o">:</span> <span class="nx">customer_name</span><span class="p">,</span>
      <span class="p">},</span>
   <span class="p">});</span>
<span class="p">}</span>
</pre></div>
</div>
<img alt="../../../_images/customer_filter.png" class="align-center" src="../../../_images/customer_filter.png" style="width: 780.0px; height: 516.0px;"/>
</div>

## 5\. Only display customers which have an active order

There is a `has_active_order` field on `res.partner`. Let us allow the user to
filter results on customers with an active order.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Add an input of type checkbox in the <code>CustomerList</code> component, with a label “Active customers”
next to it.</p></li>
<li><p>Changing the value of the checkbox should filter the list on customers with an active order.</p></li>
</ol>
<img alt="../../../_images/active_customer.png" class="align-center" src="../../../_images/active_customer.png" style="width: 303.59999999999997px; height: 368.4px;"/>
</div>

## 6\. Add a search bar to the customer list

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add an input above the customer list that allows the user to enter a string and to filter the
displayed customers, according to their name.</p>
<div class="alert alert-tip">
<p class="alert-title">
Tip</p><p>You can use the <code>fuzzyLookup</code> function to perform the filter.</p>
</div>
<img alt="../../../_images/customer_search.png" class="align-center" src="../../../_images/customer_search.png" style="width: 304.8px; height: 498.0px;"/>
</div> <div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview1.png" class="align-center" src="../../../_images/overview1.png"/>
</div>0

## 7\. Refactor the code to use `t-model`

To solve the previous two exercises, it is likely that you used an event
listener on the inputs. Let us see how we could do it in a more declarative
way, with the
[t-model](https://github.com/odoo/owl/blob/master/doc/reference/input_bindings.md)
directive.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview1.png" class="align-center" src="../../../_images/overview1.png"/>
</div>1

## 8\. Paginate customers!

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview1.png" class="align-center" src="../../../_images/overview1.png"/>
</div>2

