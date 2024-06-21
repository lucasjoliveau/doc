# Chapter 5: Testing

Automatically testing code is important when working on a codebase. It helps
ensure we don’t introduce (too many) bugs or regressions. Let us see how to
test our code.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>

## 1\. Integration testing

To make sure our application works as expected, we can perform [integration
testing](../../reference/backend/testing#reference-testing-integration-
testing) by creating a tour: this is a sequence of steps that we can execute.
Each step wait until some desired DOM state is reached, then performs an
action. If, at some point, it is unable to go to the next step for a long
time, the tour fails.

Let’s write a tour to ensure that it is possible to perform an tshirt order
from our public route

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>In the <code>awesome_tshirt</code> addon, add a <code>/static/tests/tours</code> folder.</p></li>
<li><p>Add a <code>/static/tests/tours/order_flow.js</code> file.</p></li>
<li><p>Add a tour that performs the following steps:</p>
<ol class="arabic simple">
<li><p>Open the <code>/awesome_tshirt/order</code> route.</p></li>
<li><p>Fill the order form.</p></li>
<li><p>Validate it.</p></li>
<li><p>Navigate to our webclient.</p></li>
<li><p>Open the list view for the the t-shirt order.</p></li>
<li><p>Check that our order can be found in the list.</p></li>
</ol>
</li>
<li><p>Run the tour manually.</p></li>
<li><p>Add a Python test to run it programmatically.</p></li>
<li><p>Run the tour from the terminal.</p></li>
</ol>
</div>

## 2\. Unit testing a Component

It is also useful to test independently a component or a piece of code.
[QUnit](../../reference/backend/testing#reference-testing-qunit) tests
are useful to quickly locate an issue.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>In the <code>awesome_tshirt</code> addon, add a <code>static/tests/counter_tests.js</code> file.</p></li>
<li><p>Add a QUnit test that instantiates a counter, clicks on it, and makes sure it is incremented.</p></li>
</ol>
<img alt="../../../_images/component_test.png" class="align-center" src="../../../_images/component_test.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/tests/core/checkbox_tests.js">Example: Testing an Owl component</a></p>
</div>

## 3\. Unit testing our gallery view

Many components need more setup to be tested. In particular, we often need to
mock some demo data. Let us see how to do that.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This depends on our Gallery View from <a href="04_creating_view_from_scratch">Chapter 4: Creating a view from scratch</a>.</p>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>In the <code>awesome_gallery</code> addon, add a <code>/static/tests/gallery_view_tests.js</code> file.</p></li>
<li><p>Add a test that instantiates the gallery view with some demo data.</p></li>
<li><p>Add another test that checks that when the user clicks on an image, it is switched to the form
view of the corresponding order.</p></li>
</ol>
<img alt="../../../_images/view_test.png" class="align-center" src="../../../_images/view_test.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/tests/views/list_view_tests.js">Example: Testing a list view</a></p>
</div>

