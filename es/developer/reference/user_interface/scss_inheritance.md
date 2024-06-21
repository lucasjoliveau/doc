# SCSS inheritance

## Overview

Managing SCSS assets in Konvergo ERP is not as straightforward as it is in some other
environments, but it’s highly efficient.

Modularity is key. The inheritance scheme described further allows Konvergo ERP to:

  * customize the Bootstrap CSS framework;

  * handle two different webclient designs (Community and Enterprise);

  * handle backend and frontend bundles separately (including the user’s website design);

  * contextually load only necessary assets;

  * handle multiple color-schemes (e.g.: dark-mode);

## SCSS’s `!default` directive

«Direct variables’ overrides» are technically possible in SCSS but may lead to
inconsistent results in complex environments like Konvergo ERP.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="literal-block-wrapper docutils container" id="id1">
<div class="code-block-caption"><span class="caption-text"><code>library.scss</code></span><a href="#id1" title="Enlace permanente a este código fuente">¶</a></div>
<div class="highlight-scss notranslate"><div class="highlight"><pre><span></span><span class="nv">$foo</span><span class="o">:</span> <span class="ni">red</span><span class="p">;</span>
</pre></div>
</div>
</div>
<div class="literal-block-wrapper docutils container" id="id2">
<div class="code-block-caption"><span class="caption-text"><code>customization_layer.scss</code></span><a href="#id2" title="Enlace permanente a este código fuente">¶</a></div>
<div class="highlight-scss notranslate"><div class="highlight"><pre><span></span><span class="nv">$foo</span><span class="o">:</span> <span class="ni">blue</span><span class="p">;</span> <span class="c1">// -&gt; Don't!</span>
</pre></div>
</div>
</div>
</div>

Indeed, since the compilation process acts across different interdependent
bundles, re-assigning a variable in the «wrong spot» may lead to unexpected
cascading results.

SCSS provides several techniques to overcome these issues (e.g.:
[shadowing](https://sass-lang.com/documentation/variables#shadowing)), but the
most critical procedure in Konvergo ERP is the use of the `!default` flag.

When using the `!default` flag, the compiler assigns a value **only** if that
variable is not yet defined.

As a result of this technique, the priority in which variables are assigned
matches the assets” loading order.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="literal-block-wrapper docutils container" id="id3">
<div class="code-block-caption"><span class="caption-text"><code>customization_layer.scss</code></span><a href="#id3" title="Enlace permanente a este código fuente">¶</a></div>
<div class="highlight-scss notranslate"><div class="highlight"><pre><span></span><span class="nv">$foo</span><span class="o">:</span> <span class="ni">red</span> <span class="nv">!default</span><span class="p">;</span>
</pre></div>
</div>
</div>
<div class="literal-block-wrapper docutils container" id="id4">
<div class="code-block-caption"><span class="caption-text"><code>library.scss</code></span><a href="#id4" title="Enlace permanente a este código fuente">¶</a></div>
<div class="highlight-scss notranslate"><div class="highlight"><pre><span></span><span class="nv">$foo</span><span class="o">:</span> <span class="ni">blue</span> <span class="nv">!default</span><span class="p">;</span> <span class="c1">// -&gt; Already defined, line ignored.</span>
<span class="nv">$bar</span><span class="o">:</span> <span class="ni">black</span> <span class="nv">!default</span><span class="p">;</span> <span class="c1">// -&gt; Not defined yet, value assigned.</span>
</pre></div>
</div>
</div>
<div class="literal-block-wrapper docutils container" id="id5">
<div class="code-block-caption"><span class="caption-text"><code>component.scss</code></span><a href="#id5" title="Enlace permanente a este código fuente">¶</a></div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>.component {
   color: $foo; // -&gt; 'color: red;'
   background: $bar; // -&gt; 'background: black;'
}
</pre></div>
</div>
</div>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><code>!default</code> flag on the <a href="https://sass-lang.com/documentation/variables#default-values">SASS Documentation</a></p>
</div>

## Konvergo ERP’s SCSS inheritance system

The following diagram conceptually illustrates the compilation order in which
the CSS and SCSS variables are defined.

    
    
    ↓ [Compilation starts]
    ⏐
    ↓ web.dark_mode_variables
    ⏐   ├─ Primary Variables
    ⏐   └─ Components Variables
    ⏐
    ↓ web._assets_primary_variables
    ⏐   ├─ Primary Variables (enterprise)
    ⏐   ├─ Components Variables (enterprise)
    ⏐   ├─ Primary Variables (community)
    ⏐   └─ Components Variables (community)
    ⏐
    ↓ web._assets_bootstrap
    ⏐
    ↓ web.assets_backend
    ⏐   ├─ ...
    ⏐   ├─ CSS variables definition
    ⏐   └─ CSS variables contextual adaptations
    ⏐
    ● [Visual result on screen]
    

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>This diagram is incomplete and does not match the current bundles” organization. Read more on
<a href="../frontend/assets#reference-assets-bundle"><span class="std std-ref">asset bundles</span></a>.</p>
</div>

