# Chapter 4: Creating a view from scratch

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>It is highly recommended that you complete <a href="01_fields_and_views">Chapter 1: Fields and Views</a> before starting this
chapter. The concepts introduced in Chapter 3, including views and examples, will be essential
for understanding the material covered in this chapter.</p>
</div>

Let us see how one can create a new view, completely from scratch. In a way,
it is not very difficult to do, but there are no really good resources on how
to do it. Note that most situations should be solved by either customizing an
existing view, or with a client action.

For this exercise, let’s assume that we want to create a `gallery` view, which
is a view that lets us represent a set of records with an image field. In our
Awesome Tshirt scenario, we would like to be able to see a set of t-shirts
images.

The problem could certainly be solved with a kanban view, but this means that
it is not possible to have our normal kanban view and the gallery view in the
same action.

Let us make a gallery view. Each gallery view will be defined by an
`image_field` attribute in its arch:

    
    
    <gallery image_field="some_field"/>
    

To complete the tasks in this chapter, you will need to install the
awesome_gallery addon. This addon includes the necessary server files to add a
new view.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div> <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_gallery">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>

## 1\. Make a hello world view

First step is to create a JavaScript implementation with a simple component.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create the <code>gallery_view.js</code> , <code>gallery_controller.js</code> and <code>gallery_controller.xml</code> files in
<code>static/src</code>.</p></li>
<li><p>Implement a simple hello world component in <code>gallery_controller.js</code>.</p></li>
<li><p>In <code>gallery_view.js</code>, import the controller, create a view object, and register it in the
view registry under the name <code>gallery</code>.</p></li>
<li><p>Add <code>gallery</code> as one of the view type in the orders action.</p></li>
<li><p>Make sure that you can see your hello world component when switching to the gallery view.</p></li>
</ol>
<img alt="../../../_images/view_button.png" class="align-center" src="../../../_images/view_button.png"/>
<img alt="../../../_images/new_view.png" class="align-center" src="../../../_images/new_view.png"/>
</div>

## 2\. Use the Layout component

So far, our gallery view does not look like a standard view. Let’s use the
`Layout` component to have the standard features like other views.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Import the <code>Layout</code> component and add it to the <code>components</code> of <code>GalleryController</code>.</p></li>
<li><p>Update the template to use <code>Layout</code>. It needs a <code>display</code> prop, which can be found in
<code>props.display</code>.</p></li>
</ol>
<img alt="../../../_images/layout1.png" class="align-center" src="../../../_images/layout1.png"/>
</div>

## 3\. Parse the arch

For now, our gallery view does not do much. Let’s start by reading the
information contained in the arch of the view.

The process of parsing an arch is usually done with a `ArchParser`, specific
to each view. It inherits from a generic `XMLParser` class.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Here is an example of what an ArchParser might look like:</p>
<div class="highlight-js notranslate"><div class="highlight"><pre><span></span><span class="kr">import</span> <span class="p">{</span> <span class="nx">XMLParser</span> <span class="p">}</span> <span class="nx">from</span> <span class="s2">"@web/core/utils/xml"</span><span class="p">;</span>

<span class="kr">export</span> <span class="kr">class</span> <span class="nx">GraphArchParser</span> <span class="kr">extends</span> <span class="nx">XMLParser</span> <span class="p">{</span>
    <span class="nx">parse</span><span class="p">(</span><span class="nx">arch</span><span class="p">,</span> <span class="nx">fields</span><span class="p">)</span> <span class="p">{</span>
       <span class="kr">const</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{};</span>
       <span class="k">this</span><span class="p">.</span><span class="nx">visitXML</span><span class="p">(</span><span class="nx">arch</span><span class="p">,</span> <span class="p">(</span><span class="nx">node</span><span class="p">)</span> <span class="p">=&gt;</span> <span class="p">{</span>
           <span class="p">...</span>
        <span class="p">});</span>
       <span class="k">return</span> <span class="nx">result</span><span class="p">;</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create the <code>ArchParser</code> class in its own file. It can inherit from <code>XMLParser</code> in
<code>@web/core/utils/xml</code>.</p></li>
<li><p>Use it to read the <code>image_field</code> information.</p></li>
<li><p>Update the <code>gallery</code> view code to add it to the props received by the controller.</p></li>
</ol>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>It is probably a little overkill to do it like that, since we basically only need to read one
attribute from the arch, but it is a design that is used by every other odoo views, since it
lets us extract some upfront processing out of the controller.</p>
</div>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/graph/graph_arch_parser.js">Example: The graph arch parser</a></p>
</div>

## 4\. Load some data

Let us now get some real data.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Add a <code>loadImages(domain) {...}</code> method to the <code>GalleryController</code>. It should perform a
<code>webSearchRead</code> call from the orm service to fetch records corresponding to the domain, and
use <code>imageField</code> received in props.</p></li>
<li><p>Modify the <code>setup</code> code to call that method in the <code>onWillStart</code> and <code>onWillUpdateProps</code>
hooks.</p></li>
<li><p>Modify the template to display the data inside the default slot of the <code>Layout</code> component.</p></li>
</ol>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>The loading data code will be moved into a proper model in the next exercise.</p>
</div>
<img alt="../../../_images/gallery_data.png" class="align-center" src="../../../_images/gallery_data.png"/>
</div>

## 5\. Reorganize code

Real views are a little bit more organized. This may be overkill in this
example, but it is intended to learn how to structure code in Konvergo ERP. Also, this
will scale better with changing requirements.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>1

## 6\. Display images

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>2

## 7\. Switch to form view on click

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>3 <div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>4

## 8\. Add an optional tooltip

It is useful to have some additional information on mouse hover.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>5 <div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>6

## 9\. Add pagination

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>7 <div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>8

## 10\. Validating views

We have a nice and useful view so far. But in real life, we may have issue
with users incorrectly encoding the `arch` of their Gallery view: it is
currently only an unstructured piece of XML.

Let us add some validation! In Konvergo ERP, XML documents can be described with an RN
file (Relax NG file), and then validated.

<div class="admonition-goal alert">
<p class="alert-title">
Goal</p><img alt="../../../_images/overview2.png" class="align-center" src="../../../_images/overview2.png"/>
</div>9 <div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_gallery">official Konvergo ERP tutorials repository</a>.</p>
</div></div></div></div>0

