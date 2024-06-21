# Customizing the web client

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>This tutorial is outdated.</p>
</div>

This guide is about creating modules for Konvergo ERP’s web client.

To create websites with Konvergo ERP, see [Building a Website](website); to add
business capabilities or extend existing business systems of Konvergo ERP, see
[Building a Module](backend).

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>

## A Simple Module

Let’s start with a simple Konvergo ERP module holding basic web component
configuration and letting us test the web framework.

The example module is available online and can be downloaded using the
following command:

    
    
    $ git clone http://github.com/odoo/petstore
    

This will create a `petstore` folder wherever you executed the command. You
then need to add that folder to Konvergo ERP’s [`addons
path`](../reference/cli#cmdoption-odoo-bin-addons-path), create a new
database and install the `oepetstore` module.

If you browse the `petstore` folder, you should see the following content:

    
    
    oepetstore
    |-- images
    |   |-- alligator.jpg
    |   |-- ball.jpg
    |   |-- crazy_circle.jpg
    |   |-- fish.jpg
    |   `-- mice.jpg
    |-- __init__.py
    |-- oepetstore.message_of_the_day.csv
    |-- __manifest__.py
    |-- petstore_data.xml
    |-- petstore.py
    |-- petstore.xml
    `-- static
        `-- src
            |-- css
            |   `-- petstore.css
            |-- js
            |   `-- petstore.js
            `-- xml
                `-- petstore.xml
    

The module already holds various server customizations. We’ll come back to
these later, for now let’s focus on the web-related content, in the `static`
folder.

Files used in the « web » side of an Konvergo ERP module must be placed in a `static`
folder so they are available to a web browser, files outside that folder can
not be fetched by browsers. The `src/css`, `src/js` and `src/xml` sub-folders
are conventional and not strictly necessary.

`oepetstore/static/css/petstore.css`

    

Currently empty, will hold the
[CSS](http://www.w3.org/Style/CSS/Overview.en) for pet store content

`oepetstore/static/xml/petstore.xml`

    

Mostly empty, will hold [QWeb
Templates](../reference/frontend/qweb#reference-qweb) templates

`oepetstore/static/js/petstore.js`

    

The most important (and interesting) part, contains the logic of the
application (or at least its web-browser side) as javascript. It should
currently look like:

    
    
    odoo.oepetstore = function(instance, local) {
        var _t = instance.web._t,
            _lt = instance.web._lt;
        var QWeb = instance.web.qweb;
    
        local.HomePage = instance.Widget.extend({
            start: function() {
                console.log("pet store home page loaded");
            },
        });
    
        instance.web.client_actions.add(
            'petstore.homepage', 'instance.oepetstore.HomePage');
    }
    

Which only prints a small message in the browser’s console.

The files in the `static` folder, need to be defined within the module in
order for them to be loaded correctly. Everything in `src/xml` is defined in
`__manifest__.py` while the contents of `src/css` and `src/js` are defined in
`petstore.xml`, or a similar file.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>

## Konvergo ERP JavaScript Module

Javascript doesn’t have built-in modules. As a result variables defined in
different files are all mashed together and may conflict. This has given rise
to various module patterns used to build clean namespaces and limit risks of
naming conflicts.

The Konvergo ERP framework uses one such pattern to define modules within web addons,
in order to both namespace code and correctly order its loading.

`oepetstore/static/js/petstore.js` contains a module declaration:

    
    
    odoo.oepetstore = function(instance, local) {
        local.xxx = ...;
    }
    

In Konvergo ERP web, modules are declared as functions set on the global `odoo`
variable. The function’s name must be the same as the addon (in this case
`oepetstore`) so the framework can find it, and automatically initialize it.

When the web client loads your module it will call the root function and
provide two parameters:

  * the first parameter is the current instance of the Konvergo ERP web client, it gives access to various capabilities defined by the Konvergo ERP (translations, network services) as well as objects defined by the core or by other modules.

  * the second parameter is your own local namespace automatically created by the web client. Objects and variables which should be accessible from outside your module (either because the Konvergo ERP web client needs to call them or because others may want to customize them) should be set inside that namespace.

## Classes

Much as modules, and contrary to most object-oriented languages, javascript
does not build in _classes_1 although it provides roughly equivalent (if
lower-level and more verbose) mechanisms.

For simplicity and developer-friendliness Konvergo ERP web provides a class system
based on John Resig’s [Simple JavaScript
Inheritance](http://ejohn.org/blog/simple-javascript-inheritance/).

New classes are defined by calling the `extend()` method of
`odoo.web.Class()`:

    
    
    var MyClass = instance.web.Class.extend({
        say_hello: function() {
            console.log("hello");
        },
    });
    

The `extend()` method takes a dictionary describing the new class’s content
(methods and static attributes). In this case, it will only have a `say_hello`
method which takes no parameters.

Classes are instantiated using the `new` operator:

    
    
    var my_object = new MyClass();
    my_object.say_hello();
    // print "hello" in the console
    

And attributes of the instance can be accessed via `this`:

    
    
    var MyClass = instance.web.Class.extend({
        say_hello: function() {
            console.log("hello", this.name);
        },
    });
    
    var my_object = new MyClass();
    my_object.name = "Bob";
    my_object.say_hello();
    // print "hello Bob" in the console
    

Classes can provide an initializer to perform the initial setup of the
instance, by defining an `init()` method. The initializer receives the
parameters passed when using the `new` operator:

    
    
    var MyClass = instance.web.Class.extend({
        init: function(name) {
            this.name = name;
        },
        say_hello: function() {
            console.log("hello", this.name);
        },
    });
    
    var my_object = new MyClass("Bob");
    my_object.say_hello();
    // print "hello Bob" in the console
    

It is also possible to create subclasses from existing (used-defined) classes
by calling `extend()` on the parent class, as is done to subclass `Class()`:

    
    
    var MySpanishClass = MyClass.extend({
        say_hello: function() {
            console.log("hola", this.name);
        },
    });
    
    var my_object = new MySpanishClass("Bob");
    my_object.say_hello();
    // print "hola Bob" in the console
    

When overriding a method using inheritance, you can use `this._super()` to
call the original method:

    
    
    var MySpanishClass = MyClass.extend({
        say_hello: function() {
            this._super();
            console.log("translation in Spanish: hola", this.name);
        },
    });
    
    var my_object = new MySpanishClass("Bob");
    my_object.say_hello();
    // print "hello Bob \n translation in Spanish: hola Bob" in the console
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p><code>_super</code> is not a standard method, it is set on-the-fly to the next
method in the current inheritance chain, if any. It is only defined
during the <em>synchronous</em> part of a method call, for use in asynchronous
handlers (after network calls or in <code>setTimeout</code> callbacks) a reference
to its value should be retained, it should not be accessed via <code>this</code>:</p>
<div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="c1">// broken, will generate an error</span>
<span class="nx">say_hello</span><span class="o">:</span> <span class="kd">function</span> <span class="p">()</span> <span class="p">{</span>
    <span class="nx">setTimeout</span><span class="p">(</span><span class="kd">function</span> <span class="p">()</span> <span class="p">{</span>
        <span class="k">this</span><span class="p">.</span><span class="nx">_super</span><span class="p">();</span>
    <span class="p">}.</span><span class="nx">bind</span><span class="p">(</span><span class="k">this</span><span class="p">),</span> <span class="mi">0</span><span class="p">);</span>
<span class="p">}</span>

<span class="c1">// correct</span>
<span class="nx">say_hello</span><span class="o">:</span> <span class="kd">function</span> <span class="p">()</span> <span class="p">{</span>
    <span class="c1">// don't forget .bind()</span>
    <span class="kd">var</span> <span class="nx">_super</span> <span class="o">=</span> <span class="k">this</span><span class="p">.</span><span class="nx">_super</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="k">this</span><span class="p">);</span>
    <span class="nx">setTimeout</span><span class="p">(</span><span class="kd">function</span> <span class="p">()</span> <span class="p">{</span>
        <span class="nx">_super</span><span class="p">();</span>
    <span class="p">}.</span><span class="nx">bind</span><span class="p">(</span><span class="k">this</span><span class="p">),</span> <span class="mi">0</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
</div>

## Widgets Basics

The Konvergo ERP web client bundles [jQuery](http://jquery.org) for easy DOM
manipulation. It is useful and provides a better API than standard [W3C
DOM](http://www.w3.org/TR/DOM-Level-3-Core/)2, but insufficient to structure
complex applications leading to difficult maintenance.

Much like object-oriented desktop UI toolkits (e.g. [Qt](http://qt-
project.org), [Cocoa](https://developer.apple.com/technologies/mac/cocoa)
or [GTK](http://www.gtk.org)), Konvergo ERP Web makes specific components responsible
for sections of a page. In Konvergo ERP web, the base for such components is the
`Widget()` class, a component specialized in handling a page section and
displaying information for the user.

### Your First Widget

The initial demonstration module already provides a basic widget:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            console.log("pet store home page loaded");
        },
    });
    

It extends `Widget()` and overrides the standard method `start()`, which —
much like the previous `MyClass` — does little for now.

This line at the end of the file:

    
    
    instance.web.client_actions.add(
        'petstore.homepage', 'instance.oepetstore.HomePage');
    

registers our basic widget as a client action. Client actions will be
explained later, for now this is just what allows our widget to be called and
displayed when we select the Pet Store ‣ Pet Store ‣ Home Page menu.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>because the widget will be called from outside our module, the web client
needs its « fully qualified » name, not the local version.</p>
</div>

### Display Content

Widgets have a number of methods and features, but the basics are simple:

  * set up a widget

  * format the widget’s data

  * display the widget

The `HomePage` widget already has a `start()` method. That method is part of
the normal widget lifecycle and automatically called once the widget is
inserted in the page. We can use it to display some content.

All widgets have a `$el` which represents the section of page they’re in
charge of (as a [jQuery](http://jquery.org) object). Widget content should be
inserted there. By default, `$el` is an empty `<div>` element.

A `<div>` element is usually invisible to the user if it has no content (or
without specific styles giving it a size) which is why nothing is displayed on
the page when `HomePage` is launched.

Let’s add some content to the widget’s root element, using jQuery:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            this.$el.append("<div>Hello dear Konvergo ERP user!</div>");
        },
    });
    

That message will now appear when you open Pet Store ‣ Pet Store ‣ Home Page

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>to refresh the javascript code loaded in Konvergo ERP Web, you will need to reload
the page. There is no need to restart the Konvergo ERP server.</p>
</div>

The `HomePage` widget is used by Konvergo ERP Web and managed automatically. To learn
how to use a widget « from scratch » let’s create a new one:

    
    
    local.GreetingsWidget = instance.Widget.extend({
        start: function() {
            this.$el.append("<div>We are so happy to see you again in this menu!</div>");
        },
    });
    

We can now add our `GreetingsWidget` to the `HomePage` by using the
`GreetingsWidget`’s `appendTo()` method:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            this.$el.append("<div>Hello dear Konvergo ERP user!</div>");
            var greeting = new local.GreetingsWidget(this);
            return greeting.appendTo(this.$el);
        },
    });
    

  * `HomePage` first adds its own content to its DOM root

  * `HomePage` then instantiates `GreetingsWidget`

  * Finally it tells `GreetingsWidget` where to insert itself, delegating part of its `$el` to the `GreetingsWidget`.

When the `appendTo()` method is called, it asks the widget to insert itself at
the specified position and to display its content. The `start()` method will
be called during the call to `appendTo()`.

To see what happens under the displayed interface, we will use the browser’s
DOM Explorer. But first let’s alter our widgets slightly so we can more easily
find where they are, by `adding a class to their root elements`:

    
    
    local.HomePage = instance.Widget.extend({
        className: 'oe_petstore_homepage',
        ...
    });
    local.GreetingsWidget = instance.Widget.extend({
        className: 'oe_petstore_greetings',
        ...
    });
    

If you can find the relevant section of the DOM (right-click on the text then
**Inspect Element**), it should look like this:

    
    
    <div class="oe_petstore_homepage">
        <div>Hello dear Konvergo ERP user!</div>
        <div class="oe_petstore_greetings">
            <div>We are so happy to see you again in this menu!</div>
        </div>
    </div>
    

Which clearly shows the two `<div>` elements automatically created by
`Widget()`, because we added some classes on them.

We can also see the two message-holding divs we added ourselves

Finally, note the `<div class="oe_petstore_greetings">` element which
represents the `GreetingsWidget` instance is _inside_ the `<div
class="oe_petstore_homepage">` which represents the `HomePage` instance, since
we appended

### Widget Parents and Children

In the previous part, we instantiated a widget using this syntax:

    
    
    new local.GreetingsWidget(this);
    

The first argument is `this`, which in that case was a `HomePage` instance.
This tells the widget being created which other widget is its _parent_.

As we’ve seen, widgets are usually inserted in the DOM by another widget and
_inside_ that other widget’s root element. This means most widgets are « part
» of another widget, and exist on behalf of it. We call the container the
_parent_ , and the contained widget the _child_.

Due to multiple technical and conceptual reasons, it is necessary for a widget
to know who is its parent and who are its children.

`getParent()`

    

can be used to get the parent of a widget:

    
    
    local.GreetingsWidget = instance.Widget.extend({
        start: function() {
            console.log(this.getParent().$el );
            // will print "div.oe_petstore_homepage" in the console
        },
    });
    

`getChildren()`

    

can be used to get a list of its children:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            var greeting = new local.GreetingsWidget(this);
            greeting.appendTo(this.$el);
            console.log(this.getChildren()[0].$el);
            // will print "div.oe_petstore_greetings" in the console
        },
    });
    

When overriding the `init()` method of a widget it is _of the utmost
importance_ to pass the parent to the `this._super()` call, otherwise the
relation will not be set up correctly:

    
    
    local.GreetingsWidget = instance.Widget.extend({
        init: function(parent, name) {
            this._super(parent);
            this.name = name;
        },
    });
    

Finally, if a widget does not have a parent (e.g. because it’s the root widget
of the application), `null` can be provided as parent:

    
    
    new local.GreetingsWidget(null);
    

### Destroying Widgets

If you can display content to your users, you should also be able to erase it.
This is done via the `destroy()` method:

    
    
    greeting.destroy();
    

When a widget is destroyed it will first call `destroy()` on all its children.
Then it erases itself from the DOM. If you have set up permanent structures in
`init()` or `start()` which must be explicitly cleaned up (because the garbage
collector will not handle them), you can override `destroy()`.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>when overriding <code>destroy()</code>, <code>_super()</code>
<em>must always</em> be called otherwise the widget and its children are not
correctly cleaned up leaving possible memory leaks and « phantom events »,
even if no error is displayed</p>
</div>

## The QWeb Template Engine

In the previous section we added content to our widgets by directly
manipulating (and adding to) their DOM:

    
    
    this.$el.append("<div>Hello dear Konvergo ERP user!</div>");
    

This allows generating and displaying any type of content, but gets unwieldy
when generating significant amounts of DOM (lots of duplication, quoting
issues, …)

As many other environments, Konvergo ERP’s solution is to use a [template
engine](http://en.wikipedia.org/wiki/Web_template_system). Konvergo ERP’s template
engine is called [QWeb Templates](../reference/frontend/qweb#reference-
qweb).

QWeb is an XML-based templating language, similar to
[Genshi](http://en.wikipedia.org/wiki/Genshi_\(templating_language\)),
[Thymeleaf](http://en.wikipedia.org/wiki/Thymeleaf) or
[Facelets](http://en.wikipedia.org/wiki/Facelets). It has the following
characteristics:

  * It’s implemented fully in JavaScript and rendered in the browser

  * Each template file (XML files) contains multiple templates

  * It has special support in Konvergo ERP Web’s `Widget()`, though it can be used outside of Konvergo ERP’s web client (and it’s possible to use `Widget()` without relying on QWeb)

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The rationale behind using QWeb instead of existing javascript template
engines is the extensibility of pre-existing (third-party) templates, much
like Konvergo ERP <a href="../reference/backend/views#reference-views"><span class="std std-ref">views</span></a>.</p>
<p>Most javascript template engines are text-based which precludes easy
structural extensibility where an XML-based templating engine can be
generically altered using e.g. XPath or CSS and a tree-alteration DSL (or
even just XSLT). This flexibility and extensibility is a core
characteristic of Konvergo ERP, and losing it was considered unacceptable.</p>
</div>

### Using QWeb

First let’s define a simple QWeb template in the almost-empty
`oepetstore/static/src/xml/petstore.xml` file:

    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <templates xml:space="preserve">
        <t t-name="HomePageTemplate">
            <div style="background-color: red;">This is some simple HTML</div>
        </t>
    </templates>
    

Now we can use this template inside of the `HomePage` widget. Using the `QWeb`
loader variable defined at the top of the page, we can call to the template
defined in the XML file:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            this.$el.append(QWeb.render("HomePageTemplate"));
        },
    });
    

`QWeb.render()` looks for the specified template, renders it to a string and
returns the result.

However, because `Widget()` has special integration for QWeb the template can
be set directly on the widget via its `template` attribute:

    
    
    local.HomePage = instance.Widget.extend({
        template: "HomePageTemplate",
        start: function() {
            ...
        },
    });
    

Although the result looks similar, there are two differences between these
usages:

  * with the second version, the template is rendered right before `start()` is called

  * in the first version the template’s content is added to the widget’s root element, whereas in the second version the template’s root element is directly _set as_ the widget’s root element. Which is why the « greetings » sub-widget also gets a red background

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>templates should have a single non-<code>t</code> root element, especially if
they’re set as a widget’s <code>template</code>. If there are
multiple « root elements », results are undefined (usually only the first
root element will be used and the others will be ignored)</p>
</div>

#### QWeb Context

QWeb templates can be given data and can contain basic display logic.

For explicit calls to `QWeb.render()`, the template data is passed as second
parameter:

    
    
    QWeb.render("HomePageTemplate", {name: "Klaus"});
    

with the template modified to:

    
    
    <t t-name="HomePageTemplate">
        <div>Hello <t t-esc="name"/></div>
    </t>
    

will result in:

    
    
    <div>Hello Klaus</div>
    

When using `Widget()`”s integration it is not possible to provide additional
data to the template. The template will be given a single `widget` context
variable, referencing the widget being rendered right before `start()` is
called (the widget’s state will essentially be that set up by `init()`):

    
    
    <t t-name="HomePageTemplate">
        <div>Hello <t t-esc="widget.name"/></div>
    </t>
    
    
    
    local.HomePage = instance.Widget.extend({
        template: "HomePageTemplate",
        init: function(parent) {
            this._super(parent);
            this.name = "Mordecai";
        },
        start: function() {
        },
    });
    

Result:

    
    
    <div>Hello Mordecai</div>
    

#### Template Declaration

We’ve seen how to _render_ QWeb templates, let’s now see the syntax of the
templates themselves.

A QWeb template is composed of regular XML mixed with QWeb _directives_. A
QWeb directive is declared with XML attributes starting with `t-`.

The most basic directive is `t-name`, used to declare new templates in a
template file:

    
    
    <templates>
        <t t-name="HomePageTemplate">
            <div>This is some simple HTML</div>
        </t>
    </templates>
    

`t-name` takes the name of the template being defined, and declares that it
can be called using `QWeb.render()`. It can only be used at the top-level of a
template file.

#### Escaping

The `t-esc` directive can be used to output text:

    
    
    <div>Hello <t t-esc="name"/></div>
    

It takes a Javascript expression which is evaluated, the result of the
expression is then HTML-escaped and inserted in the document. Since it’s an
expression it’s possible to provide just a variable name as above, or a more
complex expression like a computation:

    
    
    <div><t t-esc="3+5"/></div>
    

or method calls:

    
    
    <div><t t-esc="name.toUpperCase()"/></div>
    

#### Outputting HTML

To inject HTML in the page being rendered, use `t-raw`. Like `t-esc` it takes
an arbitrary Javascript expression as parameter, but it does not perform an
HTML-escape step.

    
    
    <div><t t-raw="name.link(user_account)"/></div>
    

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p><code>t-raw</code> <em>must not</em> be used on any data which may contain non-escaped
user-provided content as this leads to <a href="http://en.wikipedia.org/wiki/Cross-site_scripting">cross-site scripting</a>
vulnerabilities</p>
</div>

#### Conditionals

QWeb can have conditional blocks using `t-if`. The directive takes an
arbitrary expression, if the expression is falsy (`false`, `null`, `0` or an
empty string) the whole block is suppressed, otherwise it is displayed.

    
    
    <div>
        <t t-if="true == true">
            true is true
        </t>
        <t t-if="true == false">
            true is not true
        </t>
    </div>
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>0

#### Iteration

To iterate on a list, use `t-foreach` and `t-as`. `t-foreach` takes an
expression returning a list to iterate on `t-as` takes a variable name to bind
to each item during iteration.

    
    
    <div>
        <t t-foreach="names" t-as="name">
            <div>
                Hello <t t-esc="name"/>
            </div>
        </t>
    </div>
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>1

#### Defining attributes

QWeb provides two related directives to define computed attributes: `t-att-
_name_` and `t-attf-_name_`. In either case, _name_ is the name of the
attribute to create (e.g. `t-att-id` defines the attribute `id` after
rendering).

`t-att-` takes a javascript expression whose result is set as the attribute’s
value, it is most useful if all of the attribute’s value is computed:

    
    
    <div>
        Input your name:
        <input type="text" t-att-value="defaultName"/>
    </div>
    

`t-attf-` takes a _format string_. A format string is literal text with
interpolation blocks inside, an interpolation block is a javascript expression
between `{{` and `}}`, which will be replaced by the result of the expression.
It is most useful for attributes which are partially literal and partially
computed such as a class:

    
    
    <div t-attf-class="container {{ left ? 'text-left' : '' }} {{ extra_class }}">
        insert content here
    </div>
    

#### Calling other templates

Templates can be split into sub-templates (for simplicity, maintainability,
reusability or to avoid excessive markup nesting).

This is done using the `t-call` directive, which takes the name of the
template to render:

    
    
    <t t-name="A">
        <div class="i-am-a">
            <t t-call="B"/>
        </div>
    </t>
    <t t-name="B">
        <div class="i-am-b"/>
    </t>
    

rendering the `A` template will result in:

    
    
    <div class="i-am-a">
        <div class="i-am-b"/>
    </div>
    

Sub-templates inherit the rendering context of their caller.

#### To Learn More About QWeb

For a QWeb reference, see [QWeb
Templates](../reference/frontend/qweb#reference-qweb).

#### Exercise

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>2

## Widget Helpers

### `Widget`’s jQuery Selector

Selecting DOM elements within a widget can be performed by calling the
`find()` method on the widget’s DOM root:

    
    
    this.$el.find("input.my_input")...
    

But because it’s a common operation, `Widget()` provides an equivalent
shortcut through the `$()` method:

    
    
    local.MyWidget = instance.Widget.extend({
        start: function() {
            this.$("input.my_input")...
        },
    });
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>3

### Easier DOM Events Binding

We have previously bound DOM events using normal jQuery event handlers (e.g.
`.click()` or `.change()`) on widget elements:

    
    
    local.MyWidget = instance.Widget.extend({
        start: function() {
            var self = this;
            this.$(".my_button").click(function() {
                self.button_clicked();
            });
        },
        button_clicked: function() {
            ..
        },
    });
    

While this works it has a few issues:

  1. it is rather verbose

  2. it does not support replacing the widget’s root element at runtime as the binding is only performed when `start()` is run (during widget initialization)

  3. it requires dealing with `this`-binding issues

Widgets thus provide a shortcut to DOM event binding via `events`:

    
    
    local.MyWidget = instance.Widget.extend({
        events: {
            "click .my_button": "button_clicked",
        },
        button_clicked: function() {
            ..
        }
    });
    

`events` is an object (mapping) of an event to the function or method to call
when the event is triggered:

  * the key is an event name, possibly refined with a CSS selector in which case only if the event happens on a selected sub-element will the function or method run: `click` will handle all clicks within the widget, but `click .my_button` will only handle clicks in elements bearing the `my_button` class

  * the value is the action to perform when the event is triggered

It can be either a function:

    
        events: {
        'click': function (e) { /* code here */ }
    }
    

or the name of a method on the object (see example above).

In either case, the `this` is the widget instance and the handler is given a
single parameter, the [jQuery event
object](http://api.jquery.com/category/events/event-object/) for the event.

## Widget Events and Properties

### Events

Widgets provide an event system (separate from the DOM/jQuery event system
described above): a widget can fire events on itself, and other widgets (or
itself) can bind themselves and listen for these events:

    
    
    local.ConfirmWidget = instance.Widget.extend({
        events: {
            'click button.ok_button': function () {
                this.trigger('user_chose', true);
            },
            'click button.cancel_button': function () {
                this.trigger('user_chose', false);
            }
        },
        start: function() {
            this.$el.append("<div>Are you sure you want to perform this action?</div>" +
                "<button class='ok_button'>Ok</button>" +
                "<button class='cancel_button'>Cancel</button>");
        },
    });
    

This widget acts as a facade, transforming user input (through DOM events)
into a documentable internal event to which parent widgets can bind
themselves.

`trigger()` takes the name of the event to trigger as its first (mandatory)
argument, any further arguments are treated as event data and passed directly
to listeners.

We can then set up a parent event instantiating our generic widget and
listening to the `user_chose` event using `on()`:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            var widget = new local.ConfirmWidget(this);
            widget.on("user_chose", this, this.user_chose);
            widget.appendTo(this.$el);
        },
        user_chose: function(confirm) {
            if (confirm) {
                console.log("The user agreed to continue");
            } else {
                console.log("The user refused to continue");
            }
        },
    });
    

`on()` binds a function to be called when the event identified by `event_name`
is. The `func` argument is the function to call and `object` is the object to
which that function is related if it is a method. The bound function will be
called with the additional arguments of `trigger()` if it has any. Example:

    
    
    start: function() {
        var widget = ...
        widget.on("my_event", this, this.my_event_triggered);
        widget.trigger("my_event", 1, 2, 3);
    },
    my_event_triggered: function(a, b, c) {
        console.log(a, b, c);
        // will print "1 2 3"
    }
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>4

### Properties

Properties are very similar to normal object attributes in that they allow
storing data on a widget instance, however they have the additional feature
that they trigger events when set:

    
    
    start: function() {
        this.widget = ...
        this.widget.on("change:name", this, this.name_changed);
        this.widget.set("name", "Nicolas");
    },
    name_changed: function() {
        console.log("The new value of the property 'name' is", this.widget.get("name"));
    }
    

  * `set()` sets the value of a property and triggers `change:_propname_` (where _propname_ is the property name passed as first parameter to `set()`) and `change`

  * `get()` retrieves the value of a property.

### Exercise

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>5

## Modify existing widgets and classes

The class system of the Konvergo ERP web framework allows direct modification of
existing classes using the `include()` method:

    
    
    var TestClass = instance.web.Class.extend({
        testMethod: function() {
            return "hello";
        },
    });
    
    TestClass.include({
        testMethod: function() {
            return this._super() + " world";
        },
    });
    
    console.log(new TestClass().testMethod());
    // will print "hello world"
    

This system is similar to the inheritance mechanism, except it will alter the
target class in-place instead of creating a new class.

In that case, `this._super()` will call the original implementation of a
method being replaced/redefined. If the class already had sub-classes, all
calls to `this._super()` in sub-classes will call the new implementations
defined in the call to `include()`. This will also work if some instances of
the class (or of any of its sub-classes) were created prior to the call to
`include()`.

## Translations

The process to translate text in Python and JavaScript code is very similar.
You could have noticed these lines at the beginning of the `petstore.js` file:

    
    
    var _t = instance.web._t,
        _lt = instance.web._lt;
    

These lines are simply used to import the translation functions in the current
JavaScript module. They are used thus:

    
    
    this.$el.text(_t("Hello user!"));
    

In Konvergo ERP, translations files are automatically generated by scanning the source
code. All piece of code that calls a certain function are detected and their
content is added to a translation file that will then be sent to the
translators. In Python, the function is `_()`. In JavaScript the function is
`_t()` (and also `_lt()`).

`_t()` will return the translation defined for the text it is given. If no
translation is defined for that text, it will return the original text as-is.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>6

`_lt()` (« lazy translate ») is similar but somewhat more complex: instead of
translating its parameter immediately, it returns an object which, when
converted to a string, will perform the translation.

It is used to define translatable terms before the translations system is
initialized, for class attributes for instance (as modules are loaded before
the user’s language is configured and translations are downloaded).

## Communication with the Konvergo ERP Server

### Contacting Models

Most operations with Konvergo ERP involve communicating with _models_ implementing
business concern, these models will then (potentially) interact with some
storage engine (usually
[PostgreSQL](http://en.wikipedia.org/wiki/PostgreSQL)).

Although [jQuery](http://jquery.org) provides a
[$.ajax](http://api.jquery.com/jquery.ajax/) function for network
interactions, communicating with Konvergo ERP requires additional metadata whose setup
before every call would be verbose and error-prone. As a result, Konvergo ERP web
provides higher-level communication primitives.

To demonstrate this, the file `petstore.py` already contains a small model
with a sample method:

    
    
    class message_of_the_day(models.Model):
        _name = "oepetstore.message_of_the_day"
    
        @api.model
        def my_method(self):
            return {"hello": "world"}
    
        message = fields.Text(),
        color = fields.Char(size=20),
    

This declares a model with two fields, and a method `my_method()` which
returns a literal dictionary.

Here is a sample widget that calls `my_method()` and displays the result:

    
    
    local.HomePage = instance.Widget.extend({
        start: function() {
            var self = this;
            var model = new instance.web.Model("oepetstore.message_of_the_day");
            model.call("my_method", {context: new instance.web.CompoundContext()}).then(function(result) {
                self.$el.append("<div>Hello " + result["hello"] + "</div>");
                // will show "Hello world" to the user
            });
        },
    });
    

The class used to call Konvergo ERP models is `odoo.Model()`. It is instantiated with
the Konvergo ERP model’s name as first parameter (`oepetstore.message_of_the_day`
here).

`call()` can be used to call any (public) method of an Konvergo ERP model. It takes
the following positional arguments:

`name`

    

The name of the method to call, `my_method` here

`args`

    

an array of [positional
arguments](https://docs.python.org/2/glossary#term-argument) to provide
to the method. Because the example has no positional argument to provide, the
`args` parameter is not provided.

Here is an other example with positional arguments:

    
    
    @api.model
    def my_method2(self, a, b, c): ...
    
    
    
    model.call("my_method", [1, 2, 3], ...
    // with this a=1, b=2 and c=3
    

`kwargs`

    

a mapping of [keyword arguments](https://docs.python.org/2/glossary#term-
argument) to pass. The example provides a single named argument `context`.

    
    
    @api.model
    def my_method2(self, a, b, c): ...
    
    
    
    model.call("my_method", [], {a: 1, b: 2, c: 3, ...
    // with this a=1, b=2 and c=3
    

`call()` returns a deferred resolved with the value returned by the model’s
method as first argument.

### CompoundContext

The previous section used a `context` argument which was not explained in the
method call:

    
    
    model.call("my_method", {context: new instance.web.CompoundContext()})
    

The context is like a « magic » argument that the web client will always give
to the server when calling a method. The context is a dictionary containing
multiple keys. One of the most important key is the language of the user, used
by the server to translate all the messages of the application. Another one is
the time zone of the user, used to compute correctly dates and times if Konvergo ERP
is used by people in different countries.

The `argument` is necessary in all methods, otherwise bad things could happen
(such as the application not being translated correctly). That’s why, when you
call a model’s method, you should always provide that argument. The solution
to achieve that is to use `odoo.web.CompoundContext()`.

`CompoundContext()` is a class used to pass the user’s context (with language,
time zone, etc…) to the server as well as adding new keys to the context (some
models” methods use arbitrary keys added to the context). It is created by
giving to its constructor any number of dictionaries or other
`CompoundContext()` instances. It will merge all those contexts before sending
them to the server.

    
    
    model.call("my_method", {context: new instance.web.CompoundContext({'new_key': 'key_value'})})
    
    
    
    @api.model
    def my_method(self):
        print(self.env.context)
        // will print: {'lang': 'en_US', 'new_key': 'key_value', 'tz': 'Europe/Brussels', 'uid': 1}
    

You can see the dictionary in the argument `context` contains some keys that
are related to the configuration of the current user in Konvergo ERP plus the
`new_key` key that was added when instantiating `CompoundContext()`.

### Queries

While `call()` is sufficient for any interaction with Konvergo ERP models, Konvergo ERP Web
provides a helper for simpler and clearer querying of models (fetching of
records based on various conditions): `query()` which acts as a shortcut for
the common combination of `search()` and :`read()`. It provides a clearer
syntax to search and read models:

    
    
    model.query(['name', 'login', 'user_email', 'signature'])
         .filter([['active', '=', true], ['company_id', '=', main_company]])
         .limit(15)
         .all().then(function (users) {
        // do work with users records
    });
    

versus:

    
    
    model.call('search', [['active', '=', true], ['company_id', '=', main_company]], {limit: 15})
        .then(function (ids) {
            return model.call('read', [ids, ['name', 'login', 'user_email', 'signature']]);
        })
        .then(function (users) {
            // do work with users records
        });
    

  * `query()` takes an optional list of fields as parameter (if no field is provided, all fields of the model are fetched). It returns a `odoo.web.Query()` which can be further customized before being executed

  * `Query()` represents the query being built. It is immutable, methods to customize the query actually return a modified copy, so it’s possible to use the original and the new version side-by-side. See `Query()` for its customization options.

When the query is set up as desired, simply call `all()` to execute it and
return a deferred to its result. The result is the same as `read()`”s, an
array of dictionaries where each dictionary is a requested record, with each
requested field a dictionary key.

## Exercises

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>7 <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>8

## Existing web components

### The Action Manager

In Konvergo ERP, many operations start from an
[action](../reference/backend/actions#reference-actions): opening a menu
item (to a view), printing a report, …

Actions are pieces of data describing how a client should react to the
activation of a piece of content. Actions can be stored (and read through a
model) or they can be generated on-the fly (locally to the client by
javascript code, or remotely by a method of a model).

In Konvergo ERP Web, the component responsible for handling and reacting to these
actions is the _Action Manager_.

#### Using the Action Manager

The action manager can be invoked explicitly from javascript code by creating
a dictionary describing [an
action](../reference/backend/actions#reference-actions) of the right
type, and calling an action manager instance with it.

`do_action()` is a shortcut of `Widget()` looking up the « current » action
manager and executing the action:

    
    
    instance.web.TestWidget = instance.Widget.extend({
        dispatch_to_new_action: function() {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: "product.product",
                res_id: 1,
                views: [[false, 'form']],
                target: 'current',
                context: {},
            });
        },
    });
    

The most common action `type` is `ir.actions.act_window` which provides views
to a model (displays a model in various manners), its most common attributes
are:

`res_model`

    

The model to display in views

`res_id` (optional)

    

For form views, a preselected record in `res_model`

`views`

    

Lists the views available through the action. A list of `[view_id,
view_type]`, `view_id` can either be the database identifier of a view of the
right type, or `false` to use the view by default for the specified type. View
types can not be present multiple times. The action will open the first view
of the list by default.

`target`

    

Either `current` (the default) which replaces the « content » section of the
web client by the action, or `new` to open the action in a dialog box.

`context`

    

Additional context data to use within the action.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>This guide assumes knowledge of:</p>
<ul>
<li><p>Javascript basics and good practices</p></li>
<li><p><a href="http://jquery.org">jQuery</a></p></li>
<li><p><a href="http://underscorejs.org">Underscore.js</a></p></li>
</ul>
<p>It also requires <a href="../../administration/on_premise">an installed Konvergo ERP</a>, and <a href="http://git-scm.com">Git</a>.</p>
</div>9

### Client Actions

Throughout this guide, we used a simple `HomePage` widget which the web client
automatically starts when we select the right menu item. But how did the Konvergo ERP
web know to start this widget? Because the widget is registered as a _client
action_.

A client action is (as its name implies) an action type defined almost
entirely in the client, in javascript for Konvergo ERP web. The server simply sends an
action tag (an arbitrary name), and optionally adds a few parameters, but
beyond that _everything_ is handled by custom client code.

Our widget is registered as the handler for the client action through this:

    
    
    instance.web.client_actions.add('petstore.homepage', 'instance.oepetstore.HomePage');
    

`instance.web.client_actions` is a `Registry()` in which the action manager
looks up client action handlers when it needs to execute one. The first
parameter of `add()` is the name (tag) of the client action, and the second
parameter is the path to the widget from the Konvergo ERP web client root.

When a client action must be executed, the action manager looks up its tag in
the registry, walks the specified path and displays the widget it finds at the
end.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>0

On the server side, we had simply defined an `ir.actions.client` action:

    
    
    <record id="action_home_page" model="ir.actions.client">
        <field name="tag">petstore.homepage</field>
    </record>
    

and a menu opening the action:

    
    
    <menuitem id="home_page_petstore_menu" parent="petstore_menu"
              name="Home Page" action="action_home_page"/>
    

### Architecture of the Views

Much of Konvergo ERP web’s usefulness (and complexity) resides in views. Each view
type is a way of displaying a model in the client.

#### The View Manager

When an `ActionManager` instance receive an action of type
`ir.actions.act_window`, it delegates the synchronization and handling of the
views themselves to a _view manager_ , which will then set up one or multiple
views depending on the original action’s requirements:

![../../_images/viewarchitecture.png](../../_images/viewarchitecture.png)

#### The Views

Most [Konvergo ERP views](../reference/backend/views#reference-views) are
implemented through a subclass of `odoo.web.View()` which provides a bit of
generic basic structure for handling events and displaying model information.

The _search view_ is considered a view type by the main Konvergo ERP framework, but
handled separately by the web client (as it’s a more permanent fixture and can
interact with other views, which regular views don’t do).

A view is responsible for loading its own description XML (using
`fields_view_get`) and any other data source it needs. To that purpose, views
are provided with an optional view identifier set as the `view_id` attribute.

Views are also provided with a `DataSet()` instance which holds most necessary
model information (the model name and possibly various record ids).

Views may also want to handle search queries by overriding `do_search()`, and
updating their `DataSet()` as necessary.

### The Form View Fields

A common need is the extension of the web form view to add new ways of
displaying fields.

All built-in fields have a default display implementation, a new form widget
may be necessary to correctly interact with a new field type (e.g. a
[GIS](../glossary#term-GIS) field) or to provide new representations and
ways to interact with existing field types (e.g. validate `Char` fields which
should contain email addresses and display them as email links).

To explicitly specify which form widget should be used to display a field,
simply use the `widget` attribute in the view’s XML description:

    
    
    <field name="contact_mail" widget="email"/>
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>1

Fields are instantiated by the form view after it has read its XML description
and constructed the corresponding HTML representing that description. After
that, the form view will communicate with the field objects using some
methods. These methods are defined by the `FieldInterface` interface. Almost
all fields inherit the `AbstractField` abstract class. That class defines some
default mechanisms that need to be implemented by most fields.

Here are some of the responsibilities of a field class:

  * The field class must display and allow the user to edit the value of the field.

  * It must correctly implement the 3 field attributes available in all fields of Konvergo ERP. The `AbstractField` class already implements an algorithm that dynamically calculates the value of these attributes (they can change at any moment because their value change according to the value of other fields). Their values are stored in _Widget Properties_ (the widget properties were explained earlier in this guide). It is the responsibility of each field class to check these widget properties and dynamically adapt depending of their values. Here is a description of each of these attributes:

    * `required`: The field must have a value before saving. If `required` is `true` and the field doesn’t have a value, the method `is_valid()` of the field must return `false`.

    * `invisible`: When this is `true`, the field must be invisible. The `AbstractField` class already has a basic implementation of this behavior that fits most fields.

    * `readonly`: When `true`, the field must not be editable by the user. Most fields in Konvergo ERP have a completely different behavior depending on the value of `readonly`. As example, the `FieldChar` displays an HTML `<input>` when it is editable and simply displays the text when it is read-only. This also means it has much more code it would need to implement only one behavior, but this is necessary to ensure a good user experience.

  * Fields have two methods, `set_value()` and `get_value()`, which are called by the form view to give it the value to display and get back the new value entered by the user. These methods must be able to handle the value as given by the Konvergo ERP server when a `read()` is performed on a model and give back a valid value for a `write()`. Remember that the JavaScript/Python data types used to represent the values given by `read()` and given to `write()` is not necessarily the same in Konvergo ERP. As example, when you read a many2one, it is always a tuple whose first value is the id of the pointed record and the second one is the name get (ie: `(15, "Agrolait")`). But when you write a many2one it must be a single integer, not a tuple anymore. `AbstractField` has a default implementation of these methods that works well for simple data type and set a widget property named `value`.

Please note that, to better understand how to implement fields, you are
strongly encouraged to look at the definition of the `FieldInterface`
interface and the `AbstractField` class directly in the code of the Konvergo ERP web
client.

#### Creating a New Type of Field

In this part we will explain how to create a new type of field. The example
here will be to re-implement the `FieldChar` class and progressively explain
each part.

##### Simple Read-Only Field

Here is a first implementation that will only display text. The user will not
be able to modify the content of the field.

    
    
    local.FieldChar2 = instance.web.form.AbstractField.extend({
        init: function() {
            this._super.apply(this, arguments);
            this.set("value", "");
        },
        render_value: function() {
            this.$el.text(this.get("value"));
        },
    });
    
    instance.web.form.widgets.add('char2', 'instance.oepetstore.FieldChar2');
    

In this example, we declare a class named `FieldChar2` inheriting from
`AbstractField`. We also register this class in the registry
`instance.web.form.widgets` under the key `char2`. That will allow us to use
this new field in any form view by specifying `widget="char2"` in the
`<field/>` tag in the XML declaration of the view.

In this example, we define a single method: `render_value()`. All it does is
display the widget property `value`. Those are two tools defined by the
`AbstractField` class. As explained before, the form view will call the method
`set_value()` of the field to set the value to display. This method already
has a default implementation in `AbstractField` which simply sets the widget
property `value`. `AbstractField` also watch the `change:value` event on
itself and calls the `render_value()` when it occurs. So, `render_value()` is
a convenience method to implement in child classes to perform some operation
each time the value of the field changes.

In the `init()` method, we also define the default value of the field if none
is specified by the form view (here we assume the default value of a `char`
field should be an empty string).

##### Read-Write Field

Read-only fields, which only display content and don’t allow the user to
modify it can be useful, but most fields in Konvergo ERP also allow editing. This
makes the field classes more complicated, mostly because fields are supposed
to handle both editable and non-editable mode, those modes are often
completely different (for design and usability purpose) and the fields must be
able to switch between modes at any moment.

To know in which mode the current field should be, the `AbstractField` class
sets a widget property named `effective_readonly`. The field should watch for
changes in that widget property and display the correct mode accordingly.
Example:

    
    
    local.FieldChar2 = instance.web.form.AbstractField.extend({
        init: function() {
            this._super.apply(this, arguments);
            this.set("value", "");
        },
        start: function() {
            this.on("change:effective_readonly", this, function() {
                this.display_field();
                this.render_value();
            });
            this.display_field();
            return this._super();
        },
        display_field: function() {
            var self = this;
            this.$el.html(QWeb.render("FieldChar2", {widget: this}));
            if (! this.get("effective_readonly")) {
                this.$("input").change(function() {
                    self.internal_set_value(self.$("input").val());
                });
            }
        },
        render_value: function() {
            if (this.get("effective_readonly")) {
                this.$el.text(this.get("value"));
            } else {
                this.$("input").val(this.get("value"));
            }
        },
    });
    
    instance.web.form.widgets.add('char2', 'instance.oepetstore.FieldChar2');
    
    
    
    <t t-name="FieldChar2">
        <div class="oe_field_char2">
            <t t-if="! widget.get('effective_readonly')">
                <input type="text"></input>
            </t>
        </div>
    </t>
    

In the `start()` method (which is called immediately after a widget has been
appended to the DOM), we bind on the event `change:effective_readonly`. That
allows us to redisplay the field each time the widget property
`effective_readonly` changes. This event handler will call `display_field()`,
which is also called directly in `start()`. This `display_field()` was created
specifically for this field, it’s not a method defined in `AbstractField` or
any other class. We can use this method to display the content of the field
depending on the current mode.

From now on the conception of this field is typical, except there is a lot of
verifications to know the state of the `effective_readonly` property:

  * In the QWeb template used to display the content of the widget, it displays an `<input type="text" />` if we are in read-write mode and nothing in particular in read-only mode.

  * In the `display_field()` method, we have to bind on the `change` event of the `<input type="text" />` to know when the user has changed the value. When it happens, we call the `internal_set_value()` method with the new value of the field. This is a convenience method provided by the `AbstractField` class. That method will set a new value in the `value` property but will not trigger a call to `render_value()` (which is not necessary since the `<input type="text" />` already contains the correct value).

  * In `render_value()`, we use a completely different code to display the value of the field depending if we are in read-only or in read-write mode.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>2

### The Form View Custom Widgets

Form fields are used to edit a single field, and are intrinsically linked to a
field. Because this may be limiting, it is also possible to create _form
widgets_ which are not so restricted and have less ties to a specific
lifecycle.

Custom form widgets can be added to a form view through the `widget` tag:

    
    
    <widget type="xxx" />
    

This type of widget will simply be created by the form view during the
creation of the HTML according to the XML definition. They have properties in
common with the fields (like the `effective_readonly` property) but they are
not assigned a precise field. And so they don’t have methods like
`get_value()` and `set_value()`. They must inherit from the `FormWidget`
abstract class.

Form widgets can interact with form fields by listening for their changes and
fetching or altering their values. They can access form fields through their
`field_manager` attribute:

    
    
    local.WidgetMultiplication = instance.web.form.FormWidget.extend({
        start: function() {
            this._super();
            this.field_manager.on("field_changed:integer_a", this, this.display_result);
            this.field_manager.on("field_changed:integer_b", this, this.display_result);
            this.display_result();
        },
        display_result: function() {
            var result = this.field_manager.get_field_value("integer_a") *
                         this.field_manager.get_field_value("integer_b");
            this.$el.text("a*b = " + result);
        }
    });
    
    instance.web.form.custom_widgets.add('multiplication', 'instance.oepetstore.WidgetMultiplication');
    

`FormWidget` is generally the `FormView()` itself, but features used from it
should be limited to those defined by `FieldManagerMixin()`, the most useful
being:

  * `get_field_value(field_name)()` which returns the value of a field.

  * `set_values(values)()` sets multiple field values, takes a mapping of `{field_name: value_to_set}`

  * An event `field_changed:_field_name_` is triggered any time the value of the field called `field_name` is changed

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>3 <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>All JavaScript files are concatenated and <a href="../glossary#term-minified"><span class="xref std std-term">minified</span></a> to improve
application load time.</p>
<p>One of the drawback is debugging becomes more difficult as
individual files disappear and the code is made significantly less
readable. It is possible to disable this process by enabling the
« developer mode »: log into your Konvergo ERP instance (user <em>admin</em> password
<em>admin</em> by default) open the user menu (in the top-right corner of the
Konvergo ERP screen) and select <b>About Konvergo ERP</b> then <b>Activate
the developer mode</b>:</p>
<img alt="../../_images/about_odoo.png" class="align-center" src="../../_images/about_odoo.png"/>
<img alt="../../_images/devmode.png" class="align-center" src="../../_images/devmode.png"/>
<p>This will reload the web client with optimizations disabled, making
development and debugging significantly more comfortable.</p>
</div>4

1

    

as a separate concept from instances. In many languages classes are full-
fledged objects and themselves instance (of metaclasses) but there remains two
fairly separate hierarchies between classes and instances

2

    

as well as papering over cross-browser differences, although this has become
less necessary over time

