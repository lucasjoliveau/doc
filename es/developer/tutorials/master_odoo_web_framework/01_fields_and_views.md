# Chapter 1: Fields and Views

In the previous chapter, we learned a range of skills, including how to create
and use services, work with the Layout component, make the dashboard
translatable, and lazy load a JavaScript library like Chart.js. Now, let’s
learn how to create new fields and views.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Solutions</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>The solutions for each exercise of the chapter are hosted on the
<a href="https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt">official Konvergo ERP tutorials repository</a>. It
is recommended not to look at them before trying the exercises.</p>
</div></div></div></div>

Fields and views are among the most important concepts in the Konvergo ERP user
interface. They are key to many important user interactions, and should
therefore work perfectly. In the context of the JavaScript framework, fields
are components specialized for visualizing/editing a specific field for a
given record. For example, a (Python) model may define a char field, which
will be represented by a field component `CharField`.

A field component is basically just a component registered in the `fields`
[registry](../../reference/frontend/registries#frontend-registries). The
field component may define some additional static keys (metadata), such as
`displayName` or `supportedTypes`, and the most important one: `extractProps`,
which prepare the base props received by the `CharField`.

## Example: a simple field

Let us discuss a simplified implementation of a `CharField`. First, here is
the template:

    
    
    <t t-name="web.CharField" owl="1">
        <t t-if="props.readonly">
            <span t-esc="formattedValue" />
        </t>
        <t t-else="">
            <input
                class="o_input"
                t-att-type="props.isPassword ? 'password' : 'text'"
                t-att-placeholder="props.placeholder"
                t-on-change="updateValue"
            />
        </t>
    </t>
    

It features a readonly mode and an edit mode, which is an input with a few
attributes. Now, here is the JavaScript code:

    
    
    export class CharField extends Component {
        get formattedValue() {
            return formatChar(this.props.value, { isPassword: this.props.isPassword });
        }
    
        updateValue(ev) {
            let value = ev.target.value;
            if (this.props.shouldTrim) {
                value = value.trim();
            }
            this.props.update(value);
        }
    }
    
    CharField.template = "web.CharField";
    CharField.displayName = _lt("Text");
    CharField.supportedTypes = ["char"];
    
    CharField.extractProps = ({ attrs, field }) => {
        return {
            shouldTrim: field.trim && !archParseBoolean(attrs.password),
            maxLength: field.size,
            isPassword: archParseBoolean(attrs.password),
            placeholder: attrs.placeholder,
        };
    };
    
    registry.category("fields").add("char", CharField);
    

There are a few important things to notice:

  * The `CharField` receives its (raw) value in props. It needs to format it before displaying it.

  * It receives an `update` function in its props, which is used by the field to notify the owner of the state that the value of this field has been changed. Note that the field does not (and should not) maintain a local state with its value. Whenever the change has been applied, it will come back (possibly after an onchange) by the way of the props.

  * It defines an `extractProps` function. This is a step that translates generic standard props, specific to a view, to specialized props, useful to the component. This allows the component to have a better API, and may make it so that it is reusable.

Fields have to be registered in the `fields` registry. Once it’s done, they
can be used in some views (namely: `form`, `list`, `kanban`) by using the
`widget` attribute.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>

## 1\. An `image_preview` field

Each new order on the website will be created as an `awesome_tshirt.order`.
This model has a `image_url` field (of type `char`), which is currently only
visible as a string. We want to be able to see the image itself in the form
view.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a new <code>ImagePreview</code> component and register it in the proper <a href="../../reference/frontend/registries#frontend-registries"><span class="std std-ref">registry</span></a>. Use the <code>CharField</code> component in your template. You can use <a href="https://github.com/odoo/owl/blob/master/doc/reference/props.md#dynamic-props">t-props</a> to pass props received by <code>ImagePreview</code>
to <code>CharField</code>. Update the arch of the form view to use your new field by setting the <code>widget</code>
attribute.</p></li>
<li><p>Change the code of the <code>ImagePreview</code> component so that the image is displayed below the URL.</p></li>
<li><p>When the field is readonly, only the image should be displayed and the URL should be hidden.</p></li>
</ol>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>It is possible to solve this exercise by inheriting <code>CharField</code>, but the goal of this exercise is
to create a field from scratch.</p>
</div>
![../../../_images/image_field.png](../../../_images/image_field.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/fields/char/char_field.js">Code: CharField</a></p>
</div>

## 2\. Improving the `image_preview` field

We want to improve the field of the previous task to help the staff recognize
orders for which some action should be done.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Display a warning «MISSING TSHIRT DESIGN» in red if there is no image URL specified on the order.</p>
</div>
![../../../_images/missing_image.png](../../../_images/missing_image.png)

## 3\. Customizing a field component

Let’s see how to use inheritance to extend an existing component.

There is a `is_late`, readonly, boolean field on the order model. That would
be useful information to see on the list/kanban/view. Then, let us say that we
want to add a red word «Late!» next to it whenever it is set to `true`.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a new <code>LateOrderBoolean</code> field inheriting from <code>BooleanField</code>. The template of
<code>LateOrderBoolean</code> can also <a href="../../reference/frontend/qweb#reference-qweb-template-inheritance"><span class="std std-ref">inherit</span></a> from the
<code>BooleanField</code> template.</p></li>
<li><p>Use it in the list/kanban/form view.</p></li>
<li><p>Modify it to add a red <code>Late</code> next to it, as requested.</p></li>
</ol>
</div>
![../../../_images/late_field.png](../../../_images/late_field.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/account/static/src/components/account_type_selection">Example: A field inheriting another</a></p></li>
<li><p><a href="../../reference/backend/views#reference-views-inheritance"><span class="std std-ref">Documentation on xpath</span></a></p></li>
</ul>
</div>

## 4\. Message for some customers

Konvergo ERP form views support a `widget` API, which is like a field, but more
generic. It is useful to insert arbitrary components in the form view. Let us
see how we can use it.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>For a super efficient workflow, we would like to display an alert block with specific messages
depending on some conditions:</p>
<ul>
<li><p>If the <code>image_url</code> field is not set, it should display «No image».</p></li>
<li><p>If the <code>amount</code> of the order is higher than 100 euros, it should display «Add promotional
material».</p></li>
<li><p>Make sure that your widget is updated in real time.</p></li>
</ul>
<div class="alert alert-tip">
<p class="alert-title">
Truco</p><p>Try to evaluate <code>props.record</code> in the <b>Console</b> tab of your browser’s dev tools.</p>
</div>
</div>
![../../../_images/warning_widget.png](../../../_images/warning_widget.png)
<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>0

## 5\. Use `markup`

Let’s see how we can display raw HTML in a template. The `t-out` directive can
be used for that propose. Indeed, [it generally acts like t-esc, unless the
data has been marked explicitly with a markup
function](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#outputting-
data). In that case, its value is injected as HTML.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>1 <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>2
![../../../_images/warning_widget2.png](../../../_images/warning_widget2.png)

## 6\. Add buttons in the control panel

Views are among the most important components in Konvergo ERP: they allow users to
interact with their data. Let us discuss how Konvergo ERP views are designed.

The power of Konvergo ERP views is that they declare how a particular screen should
work with an XML document (usually named `arch`, short for architecture). This
description can be extended/modified by xpaths serverside. Then, the browser
loads that document, parses it (fancy word to say that it extracts the useful
information), and then represents the data accordingly.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>3

A view is defined in the view registry by an object with a few specific keys.

  * `type`: The (base) type of a view (for example, `form`, `list`…).

  * `display_name`: What should be displayed in the tooltip in the view switcher.

  * `icon`: Which icon to use in the view switcher.

  * `multiRecord`: Whether the view is supposed to manage a single record or a set of records.

  * `Controller`: The component that will be used to render the view (the most important information).

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>4

Most (or all?) Konvergo ERP views share a common architecture:

![../../../_images/view_architecture.svg](../../../_images/view_architecture.svg)

The view description can define a `props` function, which receives the
standard props, and computes the base props of the concrete view. The `props`
function is executed only once, and can be thought of as being some kind of
factory. It is useful to parse the `arch` XML document, and to allow the view
to be parameterized (for example, it can return a Renderer component that will
be used as Renderer). Then, it is easy to customize the specific renderer used
by a sub view.

The props will be extended before being given to the Controller. In
particular, the search props (domain/context/groupby) will be added.

Finally, the root component, commonly called the `Controller`, coordinates
everything. It uses the generic `Layout` component (to add a control panel),
instantiates a `Model`, and uses a `Renderer` component in the `Layout`
default slot. The `Model` is tasked with loading and updating data, and the
`Renderer` is supposed to handle all rendering work, along with all user
interactions.

In practice, once the t-shirt order is printed, we need to print a label to
put on the package. To do that, let us add a button in the order’s form view’s
control panel, which will call a model method.

There is a service dedicated to calling models methods: `orm_service`, located
in `core/orm_service.js`. It provides a way to call common model methods, as
well as a generic `call(model, method, args, kwargs)` method.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>5 <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>6 <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-xml notranslate"><div class="highlight"><pre><span></span><span class="nt">&lt;field</span> <span class="na">name=</span><span class="s">"preview_moves"</span> <span class="na">widget=</span><span class="s">"account_resequence_widget"</span><span class="nt">/&gt;</span>
</pre></div>
</div>
</div>9

## 7\. Auto-reload the kanban view

Bafien is upset: he wants to see the kanban view of the tshirt orders on his
external monitor, but the view needs to be up-to-date. He is tired of clicking
on the **refresh** icon every 30s, so he tasked you to find a way to do it
automatically.

Just like the previous exercise, that kind of customization requires creating
a new JavaScript view.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a new <code>ImagePreview</code> component and register it in the proper <a href="../../reference/frontend/registries#frontend-registries"><span class="std std-ref">registry</span></a>. Use the <code>CharField</code> component in your template. You can use <a href="https://github.com/odoo/owl/blob/master/doc/reference/props.md#dynamic-props">t-props</a> to pass props received by <code>ImagePreview</code>
to <code>CharField</code>. Update the arch of the form view to use your new field by setting the <code>widget</code>
attribute.</p></li>
<li><p>Change the code of the <code>ImagePreview</code> component so that the image is displayed below the URL.</p></li>
<li><p>When the field is readonly, only the image should be displayed and the URL should be hidden.</p></li>
</ol>
</div>0 <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create a new <code>ImagePreview</code> component and register it in the proper <a href="../../reference/frontend/registries#frontend-registries"><span class="std std-ref">registry</span></a>. Use the <code>CharField</code> component in your template. You can use <a href="https://github.com/odoo/owl/blob/master/doc/reference/props.md#dynamic-props">t-props</a> to pass props received by <code>ImagePreview</code>
to <code>CharField</code>. Update the arch of the form view to use your new field by setting the <code>widget</code>
attribute.</p></li>
<li><p>Change the code of the <code>ImagePreview</code> component so that the image is displayed below the URL.</p></li>
<li><p>When the field is readonly, only the image should be displayed and the URL should be hidden.</p></li>
</ol>
</div>1

