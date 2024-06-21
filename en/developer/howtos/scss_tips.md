# Write lean easy-to-maintain CSS

There are many ways to lean and simplify SCSS. The first step is to establish
if custom code is needed at all.

Konvergo ERP’s webclient has been designed to be modular, meaning that (potentially
all) classes can be shared across views. Check the code before creating a new
class. Chances are that there is already a class or an HTML tag doing exactly
what you’re looking for.

On top of that, Konvergo ERP relies on
[Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
(BS), one of the most complete CSS frameworks available. The framework has
been customized in order to match Konvergo ERP’s design (both community and enterprise
versions), meaning that you can use any BS class directly in Konvergo ERP and achieve
a visual result that is consistent with our UI.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><ul>
<li><p>The fact that a class achieves the desired visual result doesn’t necessarily mean that it’s the
right one for the job. Be aware of classes triggering JS behaviors, for example.</p></li>
<li><p>Be careful about class semantics. Applying a <b>button class</b> to a <b>title</b> is not only
semantically wrong, it may also lead to migration issues and visual inconsistencies.</p></li>
</ul>
</div>

The following sections describe tips to strip-down SCSS lines **when custom-
code is the only way to go**.

## Browser defaults

By default, each browser renders content using a _user agent stylesheet_. To
overcome inconsistencies between browsers, some of these rules are overridden
by [Bootstrap Reboot](https://getbootstrap.com/docs/5.1/content/reboot/).

At this stage all “browser-specific-decoration” rules have been stripped away,
but a big chunk of rules defining basic layout information is maintained (or
reinforced by _Reboot_ for consistency reasons).

You can rely on these rules.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Applying <code>display: block;</code> to a <code>&lt;div/&gt;</code> is normally not necessary.</p>
<div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="nt">div</span><span class="p">.</span><span class="nc">element</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="c">/* not needed 99% of the time */</span>
<span class="p">}</span>
</pre></div>
</div>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>In this instance, you may opt to switching the HTML tag rather than adding a new CSS rule.</p>
<div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="nt">span</span><span class="p">.</span><span class="nc">element</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="c">/* replace &lt;span&gt; with &lt;div&gt; instead</span>
<span class="c">      to get 'display: block' by default */</span>
<span class="p">}</span>
</pre></div>
</div>
</div>

Here’s a non-comprehensive list of default rules:

Tag / Attribute | Defaults  
---|---  
`<div/>`, `<section/>`, `<header/>`, `<footer/>`… | `display: block`  
`<span/>`, `<a/>`, `<em/>`, `<b/>`… | `display: inline`  
`<button/>`, `<label/>`, `<output/>`… | `display: inline-block`  
`<img/>`, `<svg/>` | `vertical-align: middle`  
`<summary/>`, `[role="button"]` | `cursor: pointer;`  
`<q/>` |  `:before {content: open-quote}` `:after {content: close-quote}`  
… | …  
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://github.com/twbs/bootstrap/blob/1a6fdfae6b/scss/_reboot.scss">Bootstrap Reboot on GitHub</a></p>
</div>

## HTML tags

It may seem obvious, but the simplest and most **consistent** way of making
text look like a title is to use a header tag (`<h1>`, `<h2>`, …). Besides
reboot rules, mostly all tags carry decorative styles defined by Konvergo ERP.

<div class="bg-light alert alert-success">
<p class="alert-title">
Example</p><div class="alert alert-danger docutils container">
<p>Don’t</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-WE1M" aria-selected="true" class="sphinx-tabs-tab code-tab group-tab" id="tab-0-WE1M" name="WE1M" role="tab" tabindex="0">XML</button><button aria-controls="panel-0-U0NTUw==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-0-U0NTUw==" name="U0NTUw==" role="tab" tabindex="-1">SCSS</button></div><div aria-labelledby="tab-0-WE1M" class="sphinx-tabs-panel code-tab group-tab" id="panel-0-WE1M" name="WE1M" role="tabpanel" tabindex="0"><div class="highlight-html notranslate"><div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">"o_module_custom_title"</span><span class="p">&gt;</span>
   Hello There!
<span class="p">&lt;/</span><span class="nt">span</span><span class="p">&gt;</span>

<span class="p">&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">"o_module_custom_subtitle"</span><span class="p">&gt;</span>
   I'm a subtitle.
<span class="p">&lt;/</span><span class="nt">span</span><span class="p">&gt;</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-0-U0NTUw==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-0-U0NTUw==" name="U0NTUw==" role="tabpanel" tabindex="0"><div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="p">.</span><span class="nc">o_module_custom_title</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="k">font-size</span><span class="p">:</span> <span class="mi">120</span><span class="kt">%</span><span class="p">;</span>
   <span class="k">font-weight</span><span class="p">:</span> <span class="kc">bold</span><span class="p">;</span>
   <span class="k">animation</span><span class="p">:</span> <span class="mi">1</span><span class="kt">s</span> <span class="kc">linear</span> <span class="mi">1</span><span class="kt">s</span> <span class="n">mycustomAnimation</span><span class="p">;</span>
<span class="p">}</span>

<span class="p">.</span><span class="nc">o_module_custom_subtitle</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="k">font-size</span><span class="p">:</span> <span class="mi">12</span><span class="kt">px</span><span class="p">;</span>
   <span class="k">font-weight</span><span class="p">:</span> <span class="kc">bold</span><span class="p">;</span>
   <span class="k">animation</span><span class="p">:</span> <span class="mi">2</span><span class="kt">s</span> <span class="kc">linear</span> <span class="mi">1</span><span class="kt">s</span> <span class="n">mycustomAnimation</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div></div>
</div>
<div class="alert alert-success docutils container">
<p>Do</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-1-WE1M" aria-selected="true" class="sphinx-tabs-tab code-tab group-tab" id="tab-1-WE1M" name="WE1M" role="tab" tabindex="0">XML</button><button aria-controls="panel-1-U0NTUw==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-1-U0NTUw==" name="U0NTUw==" role="tab" tabindex="-1">SCSS</button></div><div aria-labelledby="tab-1-WE1M" class="sphinx-tabs-panel code-tab group-tab" id="panel-1-WE1M" name="WE1M" role="tabpanel" tabindex="0"><div class="highlight-html notranslate"><div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">h5</span> <span class="na">class</span><span class="o">=</span><span class="s">"o_module_custom_title"</span><span class="p">&gt;</span>
   Hello There!
<span class="p">&lt;/</span><span class="nt">h5</span><span class="p">&gt;</span>

<span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">"o_module_custom_subtitle"</span><span class="p">&gt;</span>
   <span class="p">&lt;</span><span class="nt">b</span><span class="p">&gt;&lt;</span><span class="nt">small</span><span class="p">&gt;</span>I'm a subtitle.<span class="p">&lt;/</span><span class="nt">small</span><span class="p">&gt;&lt;/</span><span class="nt">b</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-1-U0NTUw==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-1-U0NTUw==" name="U0NTUw==" role="tabpanel" tabindex="0"><div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="p">.</span><span class="nc">o_module_custom_title</span> <span class="p">{</span>
   <span class="k">animation</span><span class="p">:</span> <span class="mi">1</span><span class="kt">s</span> <span class="kc">linear</span> <span class="mi">1</span><span class="kt">s</span> <span class="n">mycustomAnimation</span><span class="p">;</span>
<span class="p">}</span>

<span class="p">.</span><span class="nc">o_module_custom_subtitle</span> <span class="p">{</span>
   <span class="k">animation</span><span class="p">:</span> <span class="mi">2</span><span class="kt">s</span> <span class="kc">linear</span> <span class="mi">1</span><span class="kt">s</span> <span class="n">mycustomAnimation</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div></div>
</div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Besides reducing the amount of code, a modular-design approach (use classes, tags, mixins…)
keeps the visual result consistent and easily <b>maintainable</b>.</p>
<p>Following the last example, if Konvergo ERP titles’ design changes, these changes will be applied in the
<code>o_module_custom_title</code> element too since it’s using an <code>&lt;h5&gt;</code> tag.</p>
</div>

## Utility classes

Our framework defines a multitude of utility classes designed to cover almost
all layout/design/interaction needs. The simple fact that a class already
exists justifies its use over custom CSS whenever possible.

Take the example of `position-relative`.

    
    
    position-relative {
       position: relative !important;
    }
    

Since a utility-class is defined, any CSS line with the declaration `position:
relative` is **potentially** redundant.

Konvergo ERP relies on the default [Bootstrap utility-
classes](https://getbootstrap.com/docs/5.1/utilities/background/) stack and
defines its own using [Bootstrap
API](https://getbootstrap.com/docs/5.1/utilities/api/).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://getbootstrap.com/docs/5.1/utilities/api/">Bootstrap utility classes</a></p></li>
<li><p><a href="https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/scss/utilities_custom.scss">Konvergo ERP custom utilities on github</a></p></li>
</ul>
</div>

### Handling utility-classes verbosity

The downside of utility-classes is the potential lack of readability.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-html notranslate"><div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">myComponent</span> <span class="na">t-attf-class</span><span class="o">=</span><span class="s">"d-flex border px-lg-2 card</span>
<span class="s">{{props.readonly ? 'o_myComponent_disabled' : ''}}</span>
<span class="s">card d-lg-block position-absolute {{props.active ?</span>
<span class="s">'o_myComponent_active' : ''}}  myComponent px-3"</span><span class="p">/&gt;</span>
</pre></div>
</div>
</div>

To overcome the issue you may combine different approaches:

  * in Qweb attributes, only use classes to be toggled _on-the-fly_ ;

  * use new lines for each attribute;

  * order classes using the convention `[odoo component] [bootstrap component] [css declaration order]`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Applying <code>display: block;</code> to a <code>&lt;div/&gt;</code> is normally not necessary.</p>
<div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="nt">div</span><span class="p">.</span><span class="nc">element</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="c">/* not needed 99% of the time */</span>
<span class="p">}</span>
</pre></div>
</div>
</div>0 <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Applying <code>display: block;</code> to a <code>&lt;div/&gt;</code> is normally not necessary.</p>
<div class="highlight-css notranslate"><div class="highlight"><pre><span></span><span class="nt">div</span><span class="p">.</span><span class="nc">element</span> <span class="p">{</span>
   <span class="k">display</span><span class="p">:</span> <span class="kc">block</span><span class="p">;</span>
   <span class="c">/* not needed 99% of the time */</span>
<span class="p">}</span>
</pre></div>
</div>
</div>1

