# Chapter 1: Owl Components

This chapter introduces the [Owl framework](https://github.com/odoo/owl), a
tailor-made component system for Odoo. The main building blocks of OWL are
[components](https://github.com/odoo/owl/blob/master/doc/reference/component.md)
and
[templates](https://github.com/odoo/owl/blob/master/doc/reference/templates.md).

In Owl, every part of user interface is managed by a component: they hold the
logic and define the templates that are used to render the user interface. In
practice, a component is represented by a small JavaScript class subclassing
the `Component` class.

Before getting into the exercises, make sure you have followed all the steps
described in this [tutorial
introduction](../discover_js_framework.html#tutorials-discover-js-framework-
setup).

Solutions

The solutions for each exercise of the chapter are hosted on the [official
Odoo tutorials
repository](https://github.com/odoo/tutorials/commits/16.0-solutions/owl_playground).
It is recommended to try to solve them first without looking at the solution!

Truco

If you use Chrome as your web browser, you can install the `Owl Devtools`
extension. This extension provides many features to help you understand and
profile any Owl application.

[Video: How to use the DevTools](https://www.youtube.com/watch?v=IUyQjwnrpzM)

In this chapter, we use the `owl_playground` addon, which provides a
simplified environment that only contains Owl and a few other files. The goal
is to learn Owl itself, without relying on Odoo web client code. To get
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
    

You maybe noticed the `owl="1"` temporary attribute, it allows Odoo to
differentiate Owl templates from the old JavaScript framework templates. Note
that Owl templates are not the same as QWeb templates: they can contain
additional directives, such as `t-on-click`.

## 1\. Displaying a counter

As a first exercise, let us implement a counter in the `Playground` component
located in `owl_playground/static/src/`. To see the result, you can go to the
`/owl_playground/playground` route with your browser.

Exercise

  1. Modify `playground.js` so that it acts as a counter like in the example above. You will need to use the [useState hook](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usestate) so that the component is re-rendered whenever any part of the state object that has been read by this component is modified.

  2. In the same component, create an `increment` method.

  3. Modify the template in `playground.xml` so that it displays your counter variable. Use [t-esc](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#outputting-data) to output the data.

  4. Add a button in the template and specify a [t-on-click](https://github.com/odoo/owl/blob/master/doc/reference/event_handling.md#event-handling) attribute in the button to trigger the `increment` method whenever the button is clicked.

![../../../_images/counter.png](../../../_images/counter.png)

Truco

The Odoo JavaScript files downloaded by the browser are minified. For
debugging purpose, it’s easier when the files are not minified. Switch to
[debug mode with
assets](../../../applications/general/developer_mode.html#developer-mode-
activation) so that the files are not minified.

## 2\. Extract counter in a component

For now we have the logic of a counter in the `Playground` component, let us
see how to create a [sub-
component](https://github.com/odoo/owl/blob/master/doc/reference/component.md#sub-
components) from it.

Exercise

  1. Extract the counter code from the `Playground` component into a new `Counter` component.

  2. You can do it in the same file first, but once it’s done, update your code to move the `Counter` in its own folder and file. Import it relatively from `./counter/counter`. Make sure the template is in its own file, with the same name.

Importante

Don’t forget `/** @odoo-module **/` in your JavaScript files. More information
on this can be found
[here](../../reference/frontend/javascript_modules.html#frontend-modules-
native-js).

## 3\. A todo component

We will create new components in `owl_playground/static/src/` to keep track of
a list of todos. This will be done incrementally in multiple exercises that
will introduce various concepts.

Exercise

  1. Create a `Todo` component that receive a `todo` object in [props](https://github.com/odoo/owl/blob/master/doc/reference/props.md), and display it. It should show something like **3\. buy milk**.

  2. Add the Bootstrap classes `text-muted` and `text-decoration-line-through` on the task if it is done. To do that, you can use [dynamic attributes](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-attributes).

  3. Modify `owl_playground/static/src/playground.js` and `owl_playground/static/src/playground.xml` to display your new `Todo` component with some hard-coded props to test it first.

Example

    
        setup() {
        ...
        this.todo = { id: 3, description: "buy milk", done: false };
    }
    

![../../../_images/todo.png](../../../_images/todo.png)

Ver también

[Owl: Dynamic class
attributes](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-
class-attribute)

## 4\. Props validation

The `Todo` component has an implicit API. It expects to receive in its props
the description of a todo object in a specified format: `id`, `description`
and `done`. Let us make that API more explicit. We can add a props definition
that will let Owl perform a validation step in [dev
mode](https://github.com/odoo/owl/blob/master/doc/reference/app.md#dev-mode).
You can activate the dev mode in the [App
configuration](https://github.com/odoo/owl/blob/master/doc/reference/app.md#configuration).

> It is a good practice to do props validation for every component.

Exercise

  1. Add [props validation](https://github.com/odoo/owl/blob/master/doc/reference/props.md#props-validation) to the `Todo` component.

  2. Open the Console tab of your browser’s dev tools and make sure the props validation passes in dev mode, which is activated by default in `owl_playground`. The dev mode can be activated and deactivated by modifying the `dev` attribute in the in the `config` parameter of the [mount](https://github.com/odoo/owl/blob/master/doc/reference/app.md#mount-helper) function in `owl_playground/static/src/main.js`.

  3. Remove `done` from the props and reload the page. The validation should fail.

## 5\. A list of todos

Now, let us display a list of todos instead of just one todo. For now, we can
still hard-code the list.

Exercise

  1. Change the code to display a list of todos instead of just one. Create a new `TodoList` component to hold the `Todo` components and use [t-foreach](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#loops) in its template.

  2. Think about how it should be keyed with the `t-key` directive.

![../../../_images/todo_list.png](../../../_images/todo_list.png)

## 6\. Adding a todo

So far, the todos in our list are hard-coded. Let us make it more useful by
allowing the user to add a todo to the list.

Exercise

  1. Add an input above the task list with placeholder _Enter a new task_.

  2. Add an [event handler](https://github.com/odoo/owl/blob/master/doc/reference/event_handling.md) on the `keyup` event named `addTodo`.

  3. Implement `addTodo` to check if enter was pressed (`ev.keyCode === 13`), and in that case, create a new todo with the current content of the input as the description and clear the input of all content.

  4. Make sure the todo has a unique id. It can be just a counter that increments at each todo.

  5. Wrap the todo list in a `useState` hook to let Owl know that it should update the UI when the list is modified.

  6. Bonus point: don’t do anything if the input is empty.
    
        this.todos = useState([]);
    

![../../../_images/create_todo.png](../../../_images/create_todo.png)

Ver también

[Owl:
Reactivity](https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md)

## 7\. Focusing the input

Let’s see how we can access the DOM with
[t-ref](https://github.com/odoo/owl/blob/master/doc/reference/refs.md) and
[useRef](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref).

Exercise

  1. Focus the `input` from the previous exercise when the dashboard is [mounted](https://github.com/odoo/owl/blob/master/doc/reference/component.md#mounted). This this should be done from the `TodoList` component.

  2. Bonus point: extract the code into a specialized [hook](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md) `useAutofocus` in a new `owl_playground/utils.js` file.

Ver también

[Owl: Component
lifecycle](https://github.com/odoo/owl/blob/master/doc/reference/component.md#lifecycle)

## 8\. Toggling todos

Now, let’s add a new feature: mark a todo as completed. This is actually
trickier than one might think. The owner of the state is not the same as the
component that displays it. So, the `Todo` component needs to communicate to
its parent that the todo state needs to be toggled. One classic way to do this
is by using a [callback
prop](https://github.com/odoo/owl/blob/master/doc/reference/props.md#binding-
function-props) `toggleState`.

Exercise

  1. Add an input with the attribute `type="checkbox"` before the id of the task, which must be checked if the state `done` is true.

Truco

QWeb does not create attributes computed with the `t-att` directive if it
evaluates to a falsy value.

  2. Add a callback props `toggleState`.

  3. Add a `click` event handler on the input in the `Todo` component and make sure it calls the `toggleState` function with the todo id.

  4. Make it work!

![../../../_images/toggle_todo.png](../../../_images/toggle_todo.png)

## 9\. Deleting todos

The final touch is to let the user delete a todo.

Exercise

  1. Add a new callback prop `removeTodo`.

  2. Insert `<span class="fa fa-remove"/>` in the template of the `Todo` component.

  3. Whenever the user clicks on it, it should call the `removeTodo` method.

Truco

If you’re using an array to store your todo list, you can use the JavaScript
`splice` function to remove a todo from it.

    
    
    // find the index of the element to delete
    const index = list.findIndex((elem) => elem.id === elemId);
    if (index >= 0) {
        // remove the element at index from list
        list.splice(index, 1);
    }
    

![../../../_images/delete_todo.png](../../../_images/delete_todo.png)

## 10\. Generic card with slots

Owl has a powerful
[slot](https://github.com/odoo/owl/blob/master/doc/reference/slots.md) system
to allow you to write generic components. This is useful to factorize the
common layout between different parts of the interface.

Exercise

  1. Insert a new `Card` component between the `Counter` and `Todolist` components. Use the following Bootstrap HTML structure for the card:
    
        <div class="card" style="width: 18rem;">
        <img src="..." class="card-img-top" alt="..." />
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
                Some quick example text to build on the card title and make up the bulk
                of the card's content.
            </p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>
    

  2. This component should have two slots: one slot for the title, and one for the content (the default slot). It should be possible to use the `Card` component as follows:
    
        <Card>
        <t t-set-slot="title">Card title</t>
        <p class="card-text">Some quick example text...</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </Card>
    

  3. Bonus point: if the `title` slot is not given, the `h5` should not be rendered at all.

![../../../_images/card1.png](../../../_images/card1.png)

Ver también

[Bootstrap: documentation on
cards](https://getbootstrap.com/docs/5.2/components/card/)

## 11\. Extensive props validation

Exercise

  1. Add prop validation on the `Card` component.

  2. Try to express in the props validation system that it requires a `default` slot, and an optional `title` slot.

