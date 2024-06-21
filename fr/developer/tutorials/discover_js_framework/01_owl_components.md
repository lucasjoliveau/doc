# Chapter 1: Owl Components

This chapter introduces the [Owl framework](https://github.com/odoo/owl), a
tailor-made component system for Konvergo ERP. The main building blocks of OWL are
[components](https://github.com/odoo/owl/blob/master/doc/reference/component.md)
and
[templates](https://github.com/odoo/owl/blob/master/doc/reference/templates.md).

In Owl, every part of user interface is managed by a component: they hold the
logic and define the templates that are used to render the user interface. In
practice, a component is represented by a small JavaScript class subclassing
the `Component` class.

Before getting into the exercises, make sure you have followed all the steps
described in this [tutorial
introduction](../discover_js_framework#tutorials-discover-js-framework-
setup).

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the <a href="https://github.com/odoo/tutorials/commits/16.0-solutions/owl_playground">official Konvergo ERP tutorials
repository</a>. It
is recommended to try to solve them first without looking at the solution!</p>
</div></div></div></div><div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>

In this chapter, we use the `owl_playground` addon, which provides a
simplified environment that only contains Owl and a few other files. The goal
is to learn Owl itself, without relying on Konvergo ERP web client code. To get
started, open the `/owl_playground/playground` route with your browser: it
should display an Owl component with the text _hello world_.

## Example: a `Counter` component

First, let us have a look at a simple example. The `Counter` component shown
below is a component that maintains an internal number value, displays it, and
updates it whenever the user clicks on the button.

    
    
    import { Component, useState } from "@odoo/owl";
    
    class Counter extends Component {
        static template = "my_module.Counter";
    
        setup() {
            this.state = useState({ value: 0 });
        }
    
        increment() {
            this.state.value++;
        }
    }
    

The `Counter` component specifies the name of the template to render. The
template is written in XML and defines a part of user interface:

    
    
    <templates xml:space="preserve">
       <t t-name="my_module.Counter" owl="1">
          <p>Counter: <t t-esc="state.value"/></p>
          <button class="btn btn-primary" t-on-click="increment">Increment</button>
       </t>
    </templates>
    

You maybe noticed the `owl="1"` temporary attribute, it allows Konvergo ERP to
differentiate Owl templates from the old JavaScript framework templates. Note
that Owl templates are not the same as QWeb templates: they can contain
additional directives, such as `t-on-click`.

## 1\. Displaying a counter

As a first exercise, let us implement a counter in the `Playground` component
located in `owl_playground/static/src/`. To see the result, you can go to the
`/owl_playground/playground` route with your browser.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Modify <code>playground.js</code> so that it acts as a counter like in the example above. You will
need to use the <a href="https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usestate">useState hook</a> so that the component is re-rendered
whenever any part of the state object that has been read by this component is modified.</p></li>
<li><p>In the same component, create an <code>increment</code> method.</p></li>
<li><p>Modify the template in <code>playground.xml</code> so that it displays your counter variable. Use
<a href="https://github.com/odoo/owl/blob/master/doc/reference/templates.md#outputting-data">t-esc</a> to output the data.</p></li>
<li><p>Add a button in the template and specify a <a href="https://github.com/odoo/owl/blob/master/doc/reference/event_handling.md#event-handling">t-on-click</a> attribute in the button to
trigger the <code>increment</code> method whenever the button is clicked.</p></li>
</ol>
</div>
![../../../_images/counter.png](../../../_images/counter.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>The Konvergo ERP JavaScript files downloaded by the browser are minified. For debugging purpose, it’s
easier when the files are not minified. Switch to <a href="../../../applications/general/developer_mode#developer-mode-activation"><span class="std std-ref">debug mode with assets</span></a> so that the files are not minified.</p>
</div>

## 2\. Extract counter in a component

For now we have the logic of a counter in the `Playground` component, let us
see how to create a [sub-
component](https://github.com/odoo/owl/blob/master/doc/reference/component.md#sub-
components) from it.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Extract the counter code from the <code>Playground</code> component into a new <code>Counter</code> component.</p></li>
<li><p>You can do it in the same file first, but once it’s done, update your code to move the
<code>Counter</code> in its own folder and file. Import it relatively from <code>./counter/counter</code>. Make sure
the template is in its own file, with the same name.</p></li>
</ol>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Don’t forget <code>/** @odoo-module **/</code> in your JavaScript files. More information on this can
be found <a href="../../reference/frontend/javascript_modules#frontend-modules-native-js"><span class="std std-ref">here</span></a>.</p>
</div>

## 3\. A todo component

We will create new components in `owl_playground/static/src/` to keep track of
a list of todos. This will be done incrementally in multiple exercises that
will introduce various concepts.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic">
<li><p>Create a <code>Todo</code> component that receive a <code>todo</code> object in <a href="https://github.com/odoo/owl/blob/master/doc/reference/props.md">props</a>, and display it. It should show something like
<b>3. buy milk</b>.</p></li>
<li><p>Add the Bootstrap classes <code>text-muted</code> and <code>text-decoration-line-through</code> on the task if it is
done. To do that, you can use <a href="https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-attributes">dynamic attributes</a>.</p></li>
<li><p>Modify <code>owl_playground/static/src/playground.js</code> and
<code>owl_playground/static/src/playground.xml</code> to display your new <code>Todo</code> component with
some hard-coded props to test it first.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="nx">setup</span><span class="p">()</span> <span class="p">{</span>
    <span class="p">...</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">todo</span> <span class="o">=</span> <span class="p">{</span> <span class="nx">id</span><span class="o">:</span> <span class="mi">3</span><span class="p">,</span> <span class="nx">description</span><span class="o">:</span> <span class="s2">"buy milk"</span><span class="p">,</span> <span class="nx">done</span><span class="o">:</span> <span class="kc">false</span> <span class="p">};</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</li>
</ol>
</div> ![../../../_images/todo.png](../../../_images/todo.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-class-attribute">Owl: Dynamic class attributes</a></p>
</div>

## 4\. Props validation

The `Todo` component has an implicit API. It expects to receive in its props
the description of a todo object in a specified format: `id`, `description`
and `done`. Let us make that API more explicit. We can add a props definition
that will let Owl perform a validation step in [dev
mode](https://github.com/odoo/owl/blob/master/doc/reference/app.md#dev-mode).
You can activate the dev mode in the [App
configuration](https://github.com/odoo/owl/blob/master/doc/reference/app.md#configuration).

> It is a good practice to do props validation for every component.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Add <a href="https://github.com/odoo/owl/blob/master/doc/reference/props.md#props-validation">props validation</a> to the <code>Todo</code>
component.</p></li>
<li><p>Open the <b>Console</b> tab of your browser’s dev tools and make sure the props
validation passes in dev mode, which is activated by default in <code>owl_playground</code>. The dev mode
can be activated and deactivated by modifying the <code>dev</code> attribute in the in the <code>config</code>
parameter of the <a href="https://github.com/odoo/owl/blob/master/doc/reference/app.md#mount-helper">mount</a> function in
<code>owl_playground/static/src/main.js</code>.</p></li>
<li><p>Remove <code>done</code> from the props and reload the page. The validation should fail.</p></li>
</ol>
</div>

## 5\. A list of todos

Now, let us display a list of todos instead of just one todo. For now, we can
still hard-code the list.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>0
![../../../_images/todo_list.png](../../../_images/todo_list.png)

## 6\. Adding a todo

So far, the todos in our list are hard-coded. Let us make it more useful by
allowing the user to add a todo to the list.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>1
![../../../_images/create_todo.png](../../../_images/create_todo.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>2

## 7\. Focusing the input

Let’s see how we can access the DOM with
[t-ref](https://github.com/odoo/owl/blob/master/doc/reference/refs.md) and
[useRef](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>4

## 8\. Toggling todos

Now, let’s add a new feature: mark a todo as completed. This is actually
trickier than one might think. The owner of the state is not the same as the
component that displays it. So, the `Todo` component needs to communicate to
its parent that the todo state needs to be toggled. One classic way to do this
is by using a [callback
prop](https://github.com/odoo/owl/blob/master/doc/reference/props.md#binding-
function-props) `toggleState`.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>5
![../../../_images/toggle_todo.png](../../../_images/toggle_todo.png)

## 9\. Deleting todos

The final touch is to let the user delete a todo.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>7
![../../../_images/delete_todo.png](../../../_images/delete_todo.png)

## 10\. Generic card with slots

Owl has a powerful
[slot](https://github.com/odoo/owl/blob/master/doc/reference/slots.md) system
to allow you to write generic components. This is useful to factorize the
common layout between different parts of the interface.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>If you use Chrome as your web browser, you can install the <code>Owl Devtools</code> extension. This
extension provides many features to help you understand and profile any Owl application.</p>
<p><a href="https://www.youtube.com/watch?v=IUyQjwnrpzM">Video: How to use the DevTools</a></p>
</div>9 ![../../../_images/card1.png](../../../_images/card1.png)
<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Modify <code>playground.js</code> so that it acts as a counter like in the example above. You will
need to use the <a href="https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usestate">useState hook</a> so that the component is re-rendered
whenever any part of the state object that has been read by this component is modified.</p></li>
<li><p>In the same component, create an <code>increment</code> method.</p></li>
<li><p>Modify the template in <code>playground.xml</code> so that it displays your counter variable. Use
<a href="https://github.com/odoo/owl/blob/master/doc/reference/templates.md#outputting-data">t-esc</a> to output the data.</p></li>
<li><p>Add a button in the template and specify a <a href="https://github.com/odoo/owl/blob/master/doc/reference/event_handling.md#event-handling">t-on-click</a> attribute in the button to
trigger the <code>increment</code> method whenever the button is clicked.</p></li>
</ol>
</div>0

## 11\. Extensive props validation

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Modify <code>playground.js</code> so that it acts as a counter like in the example above. You will
need to use the <a href="https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usestate">useState hook</a> so that the component is re-rendered
whenever any part of the state object that has been read by this component is modified.</p></li>
<li><p>In the same component, create an <code>increment</code> method.</p></li>
<li><p>Modify the template in <code>playground.xml</code> so that it displays your counter variable. Use
<a href="https://github.com/odoo/owl/blob/master/doc/reference/templates.md#outputting-data">t-esc</a> to output the data.</p></li>
<li><p>Add a button in the template and specify a <a href="https://github.com/odoo/owl/blob/master/doc/reference/event_handling.md#event-handling">t-on-click</a> attribute in the button to
trigger the <code>increment</code> method whenever the button is clicked.</p></li>
</ol>
</div>1

