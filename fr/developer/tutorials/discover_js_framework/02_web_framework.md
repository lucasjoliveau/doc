# Chapter 2: Konvergo ERP Web Framework

The first part of this tutorial introduced you to most of Owl ideas. It is now
time to learn about the Konvergo ERP JavaScript framework in its entirety, as used by
the web client.

![../../../_images/previously_learned.svg](../../../_images/previously_learned.svg)

For this chapter, we will start from the empty dashboard provided by the
`awesome_tshirt` addon. We will progressively add features to it, using the
Konvergo ERP JavaScript framework.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview_02.png" class="align-center" src="../../../_images/overview_02.png"/>
</div> <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>

## 1\. A new Layout

Most screens in the Konvergo ERP web client uses a common layout: a control panel on
top, with some buttons, and a main content zone just below. This is done using
the [Layout
component](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/search/layout.js),
available in `@web/search/layout`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Update the <code>AwesomeDashboard</code> component located in <code>awesome_tshirt/static/src/</code> to use the
<code>Layout</code> component. You can use
<code>{controlPanel: { "top-right": false, "bottom-right": false } }</code> for the <code>display</code> props of
the <code>Layout</code> component.</p>
<p>Open <a href="http://localhost:8069/web">http://localhost:8069/web</a>, then open the <b>Awesome T-Shirts</b> app, and see the
result.</p>
</div>
![../../../_images/new_layout.png](../../../_images/new_layout.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/webclient/actions/reports/report_action.js">Example: use of Layout in client action</a> and
<a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/webclient/actions/reports/report_action.xml">template</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/kanban/kanban_controller.xml">Example: use of Layout in kanban view</a></p></li>
</ul>
</div>

## 2\. Add some buttons for quick navigation

Let us now use the action service for an easy access to the common views in
Konvergo ERP.

[Services](../../reference/frontend/services#frontend-services) is a
notion defined by the Konvergo ERP JavaScript framework; it is a persistent piece of
code that exports a state and/or functions. Each service can depend on other
services, and components can import a service with the `useService()` hook.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>This shows how to open the settings view from a component using the action service.</p>
<div class="highlight-js notranslate"><div class="highlight"><pre><span></span><span class="kr">import</span> <span class="p">{</span> <span class="nx">useService</span> <span class="p">}</span> <span class="nx">from</span> <span class="s2">"@web/core/utils/hooks"</span><span class="p">;</span>
<span class="p">...</span>
<span class="nx">setup</span><span class="p">()</span> <span class="p">{</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">action</span> <span class="o">=</span> <span class="nx">useService</span><span class="p">(</span><span class="s2">"action"</span><span class="p">);</span>
<span class="p">}</span>
<span class="nx">openSettings</span><span class="p">()</span> <span class="p">{</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">action</span><span class="p">.</span><span class="nx">doAction</span><span class="p">(</span><span class="s2">"base_setup.action_general_configuration"</span><span class="p">);</span>
<span class="p">}</span>
<span class="p">...</span>
</pre></div>
</div>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Let us add three buttons in the control panel bottom left zone.</p>
<ol class="arabic">
<li><p>A button <code>Customers</code>, which opens a kanban view with all customers (this action already
exists, so you should use <a href="https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/odoo/addons/base/views/res_partner_views.xml#L525">its xml id</a>).</p></li>
<li><p>A button <code>New Orders</code>, which opens a list view with all orders created in the last 7 days. Use
the <a href="https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273//addons/web/static/src/core/domain.js#L19">Domain</a> helper class to represent the domain.</p>
<div class="alert alert-tip">
<p class="alert-title">
Astuce</p><p>One way to represent the desired domain could be
<code>[('create_date','&gt;=', (context_today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d'))]</code></p>
</div>
</li>
<li><p>A button <code>Cancelled Order</code>, which opens a list of all orders created in the last 7 days, but
already cancelled. Rather than defining the action twice, factorize it in a new <code>openOrders</code>
method.</p></li>
</ol>
</div>
![../../../_images/navigation_buttons.png](../../../_images/navigation_buttons.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/account/static/src/components/journal_dashboard_activity/journal_dashboard_activity.js#L35">Example: doAction use</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/webclient/actions/action_service.js">Code: action service</a></p></li>
</ul>
</div>

## 3\. Call the server, add some statistics

Let’s improve the dashboard by adding a few cards (see the `Card` component
[made in the previous chapter](01_owl_components#tutorials-discover-js-
framework-generic-card)) containing a few statistics. There is a route
`/awesome_tshirt/statistics` that performs some computations and returns an
object containing some useful information.

Whenever we need to call a specific controller, we need to use the [rpc
service](../../reference/frontend/services#frontend-services-rpc). It
only exports a single function that perform the request: `rpc(route, params,
settings)`

Here is a short explanation on the various arguments:

  * `route` is the target route, as a string. For example `/myroute/`.

  * `params` is an object that contains all data that will be given to the controller. (optional)

  * `settings` are for advanced controls on the request. Make it silent, or using a specific xhr instance. (optional)

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A basic request could look like this:</p>
<div class="highlight-js notranslate"><div class="highlight"><pre><span></span><span class="nx">setup</span><span class="p">()</span> <span class="p">{</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">rpc</span> <span class="o">=</span> <span class="nx">useService</span><span class="p">(</span><span class="s2">"rpc"</span><span class="p">);</span>
    <span class="nx">onWillStart</span><span class="p">(</span><span class="nx">async</span> <span class="p">()</span> <span class="p">=&gt;</span> <span class="p">{</span>
        <span class="kr">const</span> <span class="nx">result</span> <span class="o">=</span> <span class="nx">await</span> <span class="k">this</span><span class="p">.</span><span class="nx">rpc</span><span class="p">(</span><span class="s2">"/my/controller"</span><span class="p">,</span> <span class="p">{</span><span class="nx">a</span><span class="o">:</span> <span class="mi">1</span><span class="p">,</span> <span class="nx">b</span><span class="o">:</span> <span class="mi">2</span><span class="p">});</span>
        <span class="c1">// ...</span>
    <span class="p">});</span>
<span class="p">}</span>
</pre></div>
</div>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Change <code>Dashboard</code> so that it uses the <code>rpc</code> service.</p></li>
<li><p>Call the statistics route <code>/awesome_tshirt/statistics</code> in the <code>onWillStart</code> hook.</p></li>
<li><p>Display a few cards in the dashboard containing:</p>
<ul>
<li><p>Number of new orders this month</p></li>
<li><p>Total amount of new orders this month</p></li>
<li><p>Average amount of t-shirt by order this month</p></li>
<li><p>Number of cancelled orders this month</p></li>
<li><p>Average time for an order to go from “new” to “sent” or “cancelled”</p></li>
</ul>
</li>
</ol>
</div>
![../../../_images/statistics.png](../../../_images/statistics.png)
<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>0

## 4\. Cache network calls, create a service

If you open the **Network** tab of your browser’s dev tools, you will see that
the call to `/awesome_tshirt/statistics` is done every time the client action
is displayed. This is because the `onWillStart` hook is called each time the
`Dashboard` component is mounted. But in this case, we would prefer to do it
only the first time, so we actually need to maintain some state outside of the
`Dashboard` component. This is a nice use case for a service!

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>1 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>2 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>3

## 5\. Display a pie chart

Everyone likes charts (!), so let us add a pie chart in our dashboard. It will
display the proportions of t-shirts sold for each size: S/M/L/XL/XXL.

For this exercise, we will use [Chart.js](https://www.chartjs.org/). It is the
chart library used by the graph view. However, it is not loaded by default, so
we will need to either add it to our assets bundle, or lazy load it. Lazy
loading is usually better since our users will not have to load the chartjs
code every time if they don’t need it.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>4
![../../../_images/pie_chart.png](../../../_images/pie_chart.png)
<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>5

## 6\. Going further

Here is a list of some small improvements you could try to do if you have the
time:

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>6 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>7

