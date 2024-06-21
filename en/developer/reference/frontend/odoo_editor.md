# Konvergo ERP Editor

Konvergo ERP Editor is Konvergo ERP’s own rich text editor. Its sources can be found in the
[odoo-editor
directory](https://github.com/odoo/odoo/blob/16.0/addons/web_editor/static/src/js/editor/odoo-
editor).

## Powerbox

The Powerbox is a piece of user interface that contains commands organized
into categories. It appears when typing `/` in the editor. The commands can be
filtered when the user inputs text, and navigated with the arrow keys.

![The Powerbox opened after typing "/".](../../../_images/powerbox.png)

### Modifying the Powerbox

Only one Powerbox should be instantiated at the time, and that job is done by
the editor itself. Its Powerbox instance can be found in its `powerbox`
instance variable. To change the Powerbox’s contents and options, change the
options passed to the editor before it gets instantiated.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Never instantiate the Powerbox yourself. Always use the current editor’s own
instance instead.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Say we want to add a new command <code>Document</code> to the Powerbox, just for the
<code>mass_mailing</code> module. We want to add it to a new category called
<code>Documentation</code> and we want it all the way at the top of the Powerbox.</p>
<p><code>mass_mailing</code> <a href="https://github.com/odoo/odoo/blob/16.0/addons/mass_mailing/static/src/js/wysiwyg.js">extends</a>
<code>web_editor</code>’s <a href="https://github.com/odoo/odoo/blob/16.0/addons/web_editor/static/src/js/wysiwyg/wysiwyg.js">Wysiwyg class</a>, which
instantiates the editor in its <code>start</code> method. Before doing so, it
calls its own <code>_getPowerboxOptions</code> method, which can conveniently be
overridden to add our new commands.</p>
<p>Since <code>mass_mailing</code> already overrides <code>_getPowerboxOptions</code>, let’s just add
our new command to it:</p>
<div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="nx">_getPowerboxOptions</span><span class="o">:</span> <span class="kd">function</span> <span class="p">()</span> <span class="p">{</span>
    <span class="kr">const</span> <span class="nx">options</span> <span class="o">=</span> <span class="k">this</span><span class="p">.</span><span class="nx">_super</span><span class="p">();</span>
    <span class="c1">// (existing code before the return statement)</span>
    <span class="nx">options</span><span class="p">.</span><span class="nx">categories</span><span class="p">.</span><span class="nx">push</span><span class="p">({</span>
        <span class="nx">name</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Documentation'</span><span class="p">),</span>
        <span class="nx">priority</span><span class="o">:</span> <span class="mi">300</span><span class="p">,</span>
    <span class="p">});</span>
    <span class="nx">options</span><span class="p">.</span><span class="nx">commands</span><span class="p">.</span><span class="nx">push</span><span class="p">({</span>
        <span class="nx">name</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Document'</span><span class="p">),</span>
        <span class="nx">category</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Documentation'</span><span class="p">),</span>
        <span class="nx">description</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s2">"Add this text to your mailing's documentation"</span><span class="p">),</span>
        <span class="nx">fontawesome</span><span class="o">:</span> <span class="s1">'fa-book'</span><span class="p">,</span>
        <span class="nx">priority</span><span class="o">:</span> <span class="mi">1</span><span class="p">,</span> <span class="c1">// This is the only command in its category anyway.</span>
    <span class="p">});</span>
    <span class="k">return</span> <span class="nx">options</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In order to allow the names and descriptions of your commands and
categories to be translated, make sure to wrap them in the <code>_t</code> function.</p>
</div>
<div class="alert alert-tip">
<p class="alert-title">
Tip</p><p>To avoid out-of-control escalations, don’t use random numbers for your
priorities: look at which other priorities already exist and choose your
value accordingly (like you would do for a <code>z-index</code>).</p>
</div>
</div>

### Opening a custom Powerbox

It is possible to open the Powerbox with a custom set of categories and
commands, bypassing all pre-existing ones. To do that, call the `open` method
of the Powerbox and pass it your custom commands and categories.

![The Powerbox opened with custom categories and commands when pasting an
image URL.](../../../_images/powerbox-custom.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>We need the current instance of the Powerbox, which can be found in the
current editor. In the <a href="https://github.com/odoo/odoo/blob/16.0/addons/web_editor/static/src/js/wysiwyg/wysiwyg.js">Wysiwyg class</a>, you
will find it as <code>this.odooEditor.powerbox</code>.</p>
<p>Now to open it with our custom “Document” command in a custom
“Documentation” category:</p>
<div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="k">this</span><span class="p">.</span><span class="nx">odooEditor</span><span class="p">.</span><span class="nx">powerbox</span><span class="p">.</span><span class="nx">open</span><span class="p">(</span>
    <span class="p">[{</span>
        <span class="nx">name</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Document'</span><span class="p">),</span>
        <span class="nx">category</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Documentation'</span><span class="p">),</span>
        <span class="nx">description</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s2">"Add this text to your mailing's documentation"</span><span class="p">),</span>
        <span class="nx">fontawesome</span><span class="o">:</span> <span class="s1">'fa-book'</span><span class="p">,</span>
        <span class="nx">priority</span><span class="o">:</span> <span class="mi">1</span><span class="p">,</span> <span class="c1">// This is the only command in its category anyway.</span>
    <span class="p">}],</span>
    <span class="p">[{</span>
        <span class="nx">name</span><span class="o">:</span> <span class="nx">_t</span><span class="p">(</span><span class="s1">'Documentation'</span><span class="p">),</span>
        <span class="nx">priority</span><span class="o">:</span> <span class="mi">300</span><span class="p">,</span>
    <span class="p">}]</span>
<span class="p">);</span>
</pre></div>
</div>
</div>

### Filtering commands

There are three ways to filter commands:

  1. Via the `powerboxFilters` Powerbox option.

  2. Via a given command’s `isDisabled` entry.

  3. The user can filter commands by simply typing text after opening the Powerbox. It will fuzzy-match that text with the names of the categories and commands.

![The Powerbox with its commands filtered using the word
"head".](../../../_images/powerbox-filtered.png)

### Reference

#### Category

Name | Type | Description  
---|---|---  
`name` | `string` | the name of the category  
`priority` | `number` | used to order the category: a category with a higher priority is displayed higher into the Powerbox (categories with the same priority are ordered alphabetically)  
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If several categories exist with the same name, they will be grouped into
one. Its priority will be that defined in the version of the category that
was declared last.</p>
</div>

#### Command

Name | Type | Description  
---|---|---  
`name` | `string` | the name of the command  
`category` | `string` | the name of the category the command belongs to  
`description` | `string` | a short text to describe the command  
`fontawesome` | `string` | the name of a _Font Awesome_ that will serve as the command’s icon  
`priority` | `number` | used to order the command: a command with a higher priority is displayed higher into the Powerbox (commands with the same priority are ordered alphabetically)  
`callback` | `function` (`() => void`) | the function to execute when the command is picked (can be asynchronous)  
`isDisabled` (optional) | `function` (`() => void`) | a function used to disable the command under certain conditions (when it returns `true`, the command will be disabled)  
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the command points to a category that doesn’t exist yet, that category
will be created and appended at the end of the Powerbox.</p>
</div>

#### Options

The following options can be passed to Konvergo ERPEditor, that will then be passed to
the instance of the Powerbox:

Name | Type | Description  
---|---|---  
`commands` | `array of commands` | commands to add to the default defined by the editor  
`categories` | `array of categories` | categories to add to the default defined by the editor  
`powerboxFilters` | `array of functions` (`commands => commands`) | functions used to filter commands displayed in the Powerbox  
`getContextFromParentRect` | `function` (`() => DOMRect`) | a function that returns the `DOMRect` of an ancestor of the editor (can be useful when the editor is in an iframe)

