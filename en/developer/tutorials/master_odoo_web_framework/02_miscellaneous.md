# Chapter 2: Miscellaneous

In the previous task, we learned how to create fields and views. There is
still much more to discover in the feature-rich Konvergo ERP web framework, so let’s
dive in and explore more in this chapter!

![../../../_images/previously_learned1.svg](../../../_images/previously_learned1.svg)

This is the progress that we have made in discovering the JavaScript web
framework at the end of [Chapter 1: Fields and
Views](01_fields_and_views).

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/kitten_mode.png" class="align-center" src="../../../_images/kitten_mode.png"/>
</div> <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>

## 1\. Interacting with the notification system

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This task depends on <a href="01_fields_and_views">the previous exercises</a>.</p>
</div>

After using the **Print Label** button for some t-shirt tasks, it is apparent
that there should be some feedback that the `print_label` action is completed
(or failed, for example, the printer is not connected or ran out of paper).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Display a <a href="../../reference/frontend/services#frontend-services-notification"><span class="std std-ref">notification</span></a> message when the action is
completed successfully, and a warning if it failed.</p></li>
<li><p>If it failed, the notification should be permanent.</p></li>
</ol>
<img alt="../../../_images/notification.png" class="align-center" src="../../../_images/notification.png" style="width: 387.59999999999997px; height: 148.79999999999998px;"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/fields/image_url/image_url_field.js">Example: Using the notification service</a></p>
</div>

## 2\. Add a systray item

Our beloved leader wants to keep a close eye on new orders. He wants to see
the number of new, unprocessed orders at all time. Let’s do that with a
systray item.

A [systray](../../reference/frontend/registries#frontend-registries-
systray) item is an element that appears in the system tray, which is a small
area located on the right-hand side of the navbar. The systray is used to
display notifications and provide access to certain features.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a systray component that connects to the statistics service we made previously.</p></li>
<li><p>Use it to display the number of new orders.</p></li>
<li><p>Clicking on it should open a list view with all of those orders.</p></li>
<li><p>Bonus point: avoid making the initial RPC by adding the information to the session info. The
session info is given to the web client by the server in the initial response.</p></li>
</ol>
<img alt="../../../_images/systray.png" class="align-center" src="../../../_images/systray.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/webclient/user_menu/user_menu.js">Example: Systray item</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/barcodes/models/ir_http.py">Example: Adding some information to the “session info”</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/barcodes/static/src/barcode_service.js#L5">Example: Reading the session information</a></p></li>
</ul>
</div>

## 3\. Real life update

So far, the systray item from above does not update unless the user refreshes
the browser. Let us do that by calling periodically (for example, every
minute) the server to reload the information.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>The <code>tshirt</code> service should periodically reload its data.</p></li>
</ol>
</div>

Now, the question arises: how is the systray item notified that it should re-
render itself? It can be done in various ways but, for this training, we
choose to use the most _declarative_ approach:

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple" start="2">
<li><p>Modify the <code>tshirt</code> service to return a <a href="https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md#reactive">reactive</a> object. Reloading data should update the
reactive object in place.</p></li>
<li><p>The systray item can then perform a <a href="https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md#usestate">useState</a> on the service return value.</p></li>
<li><p>This is not really necessary, but you can also <em>package</em> the calls to <code>useService</code> and
<code>useState</code> in a custom hook <code>useStatistics</code>.</p></li>
</ol>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md">Documentation on reactivity</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/core/debug/profiling/profiling_service.js#L30">Example: Use of reactive in a service</a></p></li>
</ul>
</div>

## 4\. Add a command to the command palette

Now, let us see how we can interact with the command palette. The command
palette is a feature that allows users to quickly access various commands and
functions within the application. It is accessed by pressing `CTRL+K` in the
Konvergo ERP interface.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>0 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>1

## 5\. Monkey patching a component

Often, we can achieve what we want by using existing extension points that
allow for customization, such as registering something in a registry.
Sometimes, however, it happens that we want to modify something that has no
such mechanism. In that case, we must fall back on a less safe form of
customization: monkey patching. Almost everything in Konvergo ERP can be monkey
patched.

Bafien, our beloved leader, heard about employees performing better if they
are constantly being watched. Since he cannot be there in person for each of
his employees, he tasked you with updating the user interface to add a
blinking red eye in the control panel. Clicking on that eye should open a
dialog with the following message: “Bafien is watching you. This interaction
is recorded and may be used in legal proceedings if necessary. Do you agree to
these terms?”

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>2 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>3

## 6\. Fetching orders from a customer

Let’s see how to use some standard components to build a powerful feature
combining autocomplete, fetching data, and fuzzy lookup. We will add an input
in our dashboard to easily search all orders from a given customer.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>4

## 7\. Reintroduce Kitten Mode

Let us add a special mode to Konvergo ERP: whenever the URL contains `kitten=1`, we
will display a kitten in the background of Konvergo ERP, because we like kittens.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>5

## 8\. Lazy loading our dashboard

This is not really necessary, but the exercise is interesting. Imagine that
our awesome dashboard is a large application with potentially multiple
external libraries and lots of code/styles/templates. Also, suppose that the
dashboard is used only by some users in some business flows. It would be
interesting to lazy load it in order to speed up the loading of the web client
in most cases.

So, let us do that!

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>6

So far, we only removed the dashboard from the main bundle; we now want to
lazy load it. Currently, no client action is registered in the action
registry.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>7

If you open the **Network** tab of your browser’s dev tools, you should see
that `awesome_tshirt.dashboard.min.js` is now loaded only when the Dashboard
is first accessed.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>8

