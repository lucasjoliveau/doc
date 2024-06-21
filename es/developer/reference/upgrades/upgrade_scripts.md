# Upgrade scripts

An upgrade script is a Python file containing a function called `migrate()`,
which the upgrade process invokes during the update of a module.

migrate(_cr_ , _version_)

    

Parámetros

    

  * **cr** (`Cursor`) – current database cursor

  * **version** ([_str_](https://docs.python.org/3/library/stdtypes#str "\(en Python versión 3.12\)")) – installed version of the module

Typically, this function executes one or multiple SQL queries and can also
access Konvergo ERP’s ORM, as well as the [Upgrade utils](upgrade_utils).

## Writing upgrade scripts

Upgrade scripts follow a specific tree structure with a naming convention
which determines when they are executed.

The structure of an upgrade script path is
`$module/migrations/$version/_pre,post,end_ -*.py`, where `$module` is the
module for which the script will run, `$version` is the full version of the
module (including Konvergo ERP’s major version and the module’s minor version) and
`{pre|post|end}-*.py` is the file that needs to be executed. The file’s name
will determine the phase and order in which it is executed for that module and
version.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>From Konvergo ERP 13 the top-level directory for the upgrade scripts can also be named <code>upgrades</code>. This
naming is preferred since it has the correct meaning: <em>migrate</em> can be confused with <em>moving out
of Konvergo ERP</em>. Thus <code>$module/upgrades/$version/</code> is also valid.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Upgrade scripts are only executed when the module is being updated. Therefore, the
module’s minor version set in the <code>$version</code> directory needs to be higher than the module’s
installed version and equal or lower to the updated version of the module.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Directory structure of an upgrade script for a custom module named <code>awesome_partner</code> upgraded
to version <code>2.0</code> on Konvergo ERP 17.</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>awesome_partner/
|-- migrations/
|   |-- 17.0.2.0/
|   |   |-- pre-exclamation.py
</pre></div>
</div>
<p>Two upgrade scripts examples with the content of the <code>pre-exclamation.py</code>, file adding
«!» at the end of partners” names:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>

<span class="n">_logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="vm">__name__</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">migrate</span><span class="p">(</span><span class="n">cr</span><span class="p">,</span> <span class="n">version</span><span class="p">):</span>
    <span class="n">cr</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="s2">"UPDATE res_partner SET name = name || '!'"</span><span class="p">)</span>
    <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Updated </span><span class="si">%s</span><span class="s2"> partners"</span><span class="p">,</span> <span class="n">cr</span><span class="o">.</span><span class="n">rowcount</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="kn">from</span> <span class="nn">odoo.upgrade</span> <span class="kn">import</span> <span class="n">util</span>

<span class="n">_logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="vm">__name__</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">migrate</span><span class="p">(</span><span class="n">cr</span><span class="p">,</span> <span class="n">version</span><span class="p">):</span>
    <span class="n">env</span> <span class="o">=</span> <span class="n">util</span><span class="o">.</span><span class="n">env</span><span class="p">(</span><span class="n">cr</span><span class="p">)</span>

    <span class="n">partners</span> <span class="o">=</span> <span class="n">env</span><span class="p">[</span><span class="s2">"res.partner"</span><span class="p">]</span><span class="o">.</span><span class="n">search</span><span class="p">([])</span>
    <span class="k">for</span> <span class="n">partner</span> <span class="ow">in</span> <span class="n">partners</span><span class="p">:</span>
        <span class="n">partner</span><span class="o">.</span><span class="n">name</span> <span class="o">+=</span> <span class="s2">"!"</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Updated </span><span class="si">%s</span><span class="s2"> partners"</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">partners</span><span class="p">))</span>
</pre></div>
</div>
<p>Note that in the second example, the script takes advantage of the <a href="upgrade_utils">Upgrade utils</a> to
access the ORM. Check the documentation to find out more about this library.</p>
</div>

## Phases of upgrade scripts

The upgrade process consists of three phases for each version of each module:

>   1. The pre-phase, before the module is loaded.
>
>   2. The post-phase, after the module and its dependencies are loaded and
> updated.
>
>   3. The end-phase, after all modules have been loaded and updated for that
> version.
>
>

Upgrade scripts are grouped according to the first part of their filenames
into the corresponding phase. Within each phase, the files are executed
according to their lexical order.

<div class="admonition-execution-order-of-example-scripts-for-one-module-in-one-version alert">
<p class="alert-title">
Execution order of example scripts for one module in one version</p><ol class="arabic simple">
<li><p><code>pre-10-do_something.py</code></p></li>
<li><p><code>pre-20-something_else.py</code></p></li>
<li><p><code>post-do_something.py</code></p></li>
<li><p><code>post-something.py</code></p></li>
<li><p><code>end-01-migrate.py</code></p></li>
<li><p><code>end-migrate.py</code></p></li>
</ol>
</div>

