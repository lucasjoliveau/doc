# Theming

After your development environment is fully set up, you can start building the
skeleton of your theme module. In this chapter, you will discover how to:

  * Enable/disable the Website Builder’s standard options and templates.

  * Define the colors and fonts to use for your design.

  * Get the most out of Bootstrap variables.

  * Add custom styles and JavaScript.

## Theme module

Konvergo ERP comes with a default theme that provides minimal structure and layout.
When you create a new theme, you are extending the default theme.

Remember to add the directory containing your module to the `addons-path`
command-line argument when running Konvergo ERP in your development environment.

### Technical naming

The first step is to create a new directory.

    
    
    website_airproof
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Prefix it with <code>website_</code> and use only lowercase ASCII alphanumeric characters and underscores.</p>
<p>In this documentation, we will use <b>Airproof</b> (a fictional project) as an example.</p>
</div>

### File structure

Themes are packaged like any Konvergo ERP module. Even if you are designing a basic
website, you need to package its theme like a module.

    
    
    website_airproof
    ├── data
    ├── i18n
    ├── lib
    ├── static
    │   ├── description
    │   ├── fonts
    │   ├── image_shapes // Shapes for images
    │   ├── shapes // Shapes for background
    │   └── src
    │       ├── img
    │       │   ├── content // For those used in the pages of your website
    │       │   └── wbuilder // For those used in the builder
    │       ├── js
    │       ├── scss
    │       └── snippets // custom snippets
    ├── views
    ├── __init__.py
    └── __manifest__.py
    

Folder | Description  
---|---  
data | Presets, menus, pages, images, shapes, … (`*.xml`)  
i18n | Translations (`*.po`, `*.pot`)  
lib | External libraries (`*.js`)  
static | Custom assets (`*.jpg`, `*.gif`, `*.png`, `*.svg`, `*.pdf`, `*.scss`, `*.js`)  
views | Custom views and templates (`*.xml`)  
  
### Initialization

An Konvergo ERP module is also a Python package with a `__init__.py` file containing
import instructions for various Python files in the module. This file can
remain empty for now.

### Declaration

An Konvergo ERP module is declared by its manifest file. This file declares a Python
package as an Konvergo ERP module and specifies the module’s metadata. It must at
least contain the `name` field, which is always required. It usually contains
much more information.

`/website_airproof/__manifest__.py`

    
    
    {
       'name': 'Airproof Theme',
       'description': '...',
       'category': 'Website/Theme',
       'version': '15.0.0',
       'author': '...',
       'license': '...',
       'depends': ['website'],
       'data': [
          # ...
       ],
       'assets': {
          # ...
       },
    }
    

Field | Description  
---|---  
name | Human-readable name of the module (required)  
description | Extended description of the module, in [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText)  
category | Classification category within Konvergo ERP  
version | Konvergo ERP version this module is addressing  
author | Name of the module author  
license | Distribution license for the module  
depends | Konvergo ERP modules must be loaded before this one, either because this module uses features they create or because it alters resources they define  
data | List of XML files  
assets | List of SCSS and JS files  
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>

## Default options

First, try to construct your theme by using Konvergo ERP’s default options. This
ensures two things:

  1. You do not re-invent something which already exists. For example, as Konvergo ERP provides an option to add a border on the footer, you shouldn’t recode it yourself. Instead, enable the default option first, then extend it if needed.

  2. The user can still use all of Konvergo ERP’s features with your theme. For example, if you recode the border on the footer, you may break the default option or make it useless, giving the user a bad experience. Also, your recode might not work as well as the default option, as other Konvergo ERP features may rely on it.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Use four spaces per indentation level.</p></li>
<li><p>Do not use tabs.</p></li>
<li><p>Never mix spaces and tabs.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../contributing/development/coding_guidelines">Konvergo ERP coding guidelines</a></p>
</div>

### Konvergo ERP variables

Konvergo ERP declares many CSS rules, most entirely customizable by overriding the
related SCSS variables. To do so, create a `primary_variables.scss` file and
add it to the `_assets_primary_variables` bundle.

**Declaration**

`/website_airproof/__manifest__.py`

    
    
    'assets': {
       'web._assets_primary_variables': [
          ('prepend', 'website_airproof/static/src/scss/primary_variables.scss'),
       ],
    },
    

By reading the source code, variables related to options are easily
noticeable.

    
    
    <we-button title="..."
       data-name="..."
       data-customize-website-views="..."
       data-customize-website-variable="'Sidebar'"
       data-img="..."/>
    

These variables can be overridden through the `$o-website-value-palettes` map,
for example.

#### Global

**Declaration**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          // Templates
          // Colors
          // Fonts
          // Buttons
          // ...
       ),
    );
    

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>That file must only contain definitions and overrides of SCSS variables and mixins.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://github.com/odoo/odoo/blob/34c0c9c1ae00aba391932129d4cefd027a9c6bbd/addons/website/static/src/scss/primary_variables.scss#L1954">Primary variables SCSS</a></p>
</div>

#### Fonts

You can embed any font on your website. The Website Builder automatically
makes them available in the font selector.

**Declaration**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-theme-font-configs: (
       <font-name>: (
          'family': <css font family list>,
          'url' (optional): <related part of Google fonts URL>,
          'properties' (optional): (
             <font-alias>: (
                <website-value-key>: <value>,
                ...,
             ),
          ...,
       )
    )
    

**Use**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'font':                             '<font-name>',
          'headings-font':                    '<font-name>',
          'navbar-font':                      '<font-name>',
          'buttons-font':                     '<font-name>',
       ),
    );
    

##### Google fonts

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-theme-font-configs: (
       'Poppins': (
          'family':                         ('Poppins', sans-serif),
          'url':                            'Poppins:400,500',
          'properties' : (
             'base': (
                'font-size-base':           1rem,
             ),
          ),
       ),
    );
    

##### Custom fonts

First, create a specific SCSS file to declare your custom font(s).

`/website_airproof/__manifest__.py`

    
    
    'assets': {
       'web.assets_frontend': [
          'website_airproof/static/src/scss/font.scss',
       ],
    },
    

Then, use the `@font-face` rule to allow you custom font(s) to be loaded on
your website.

`/website_airproof/static/src/scss/font.scss`

    
    
    @font-face {
       font-family: '<font-name>';
       ...
    }
    

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-theme-font-configs: (
       'Proxima Nova': (
          'family':                         ('Proxima Nova', sans-serif),
          'properties' : (
             'base': (
                'font-size-base':           1rem,
             ),
          ),
       ),
    );
    

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>It is recommended to use the .woff format for your fonts.</p>
</div>

#### Colors

The Website Builder relies on palettes composed of five named colors. Defining
those in your theme ensures it stays consistent.

Color | Description  
---|---  
o-color-1 | Primary  
o-color-2 | Secondary  
o-color-3 | Extra  
o-color-4 | Whitish  
o-color-5 | Blackish  
![Theme colors](../../../_images/theme-colors.png)

**Declaration**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-color-palettes: map-merge($o-color-palettes,
       (
          'airproof': (
             'o-color-1':                    #bedb39,
             'o-color-2':                    #2c3e50,
             'o-color-3':                    #f2f2f2,
             'o-color-4':                    #ffffff,
             'o-color-5':                    #000000,
          ),
       )
    );
    

Add the created palette to the list of palettes offered by the Website
Builder.

    
    
    $o-selected-color-palettes-names: append($o-selected-color-palettes-names, 'airproof');
    

**Use**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'color-palettes-name':              'airproof',
       ),
    );
    

![Theme colors Airproof](../../../_images/theme-colors-airproof.png)

**Color combinations**

Based on the previously defined five color palettes, the Website Builder
automatically generates five color combinations, each defining a color for the
background, text, headings, links, primary buttons, and secondary buttons.
These colors can be customized later by the user.

![Theme colors](../../../_images/theme-colors-big.png)

The colors used in a color combination are accessible and can be overridden
through the BS `$colors map` using a specific prefix (`o-cc` for `color
combination`).

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-color-palettes: map-merge($o-color-palettes,
       (
          'airproof': (
    
             'o-cc*-bg':                     'o-color-*',
             'o-cc*-text':                   'o-color-*',
             'o-cc*-headings':               'o-color-*',
             'o-cc*-h2':                     'o-color-*',
             'o-cc*-h3':                     'o-color-*',
             'o-cc*-h4':                     'o-color-*',
             'o-cc*-h5':                     'o-color-*',
             'o-cc*-h6':                     'o-color-*',
             'o-cc*-link':                   'o-color-*',
             'o-cc*-btn-primary':            'o-color-*',
             'o-cc*-btn-primary-border':     'o-color-*',
             'o-cc*-btn-secondary':          'o-color-*',
             'o-cc*-btn-secondary-border':   'o-color-*',
    
          ),
       )
    );
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For each <code>o-cc*</code>, replace the <code>*</code> with the digit (1 - 5) corresponding to the desired color
combination.</p>
<p>The default text color is <code>o-color-5</code>. If the background is too dark, it will automatically
change to the <code>o-color-4</code> color.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://github.com/odoo/odoo/blob/34c0c9c1ae00aba391932129d4cefd027a9c6bbd/addons/web_editor/static/src/scss/web_editor.common.scss#L711">Color combinations SCSS</a></p>
</div> <div class="admonition-demo-page alert">
<p class="alert-title">
Demo page</p><p>The Website Builder automatically generates a page to view the color combinations of the theme
color palette: <a href="http://localhost:8069/website/demo/color-combinations">http://localhost:8069/website/demo/color-combinations</a></p>
</div>

### Bootstrap variables

Konvergo ERP includes Bootstrap by default. You can use all variables and mixins of
the framework.

If Konvergo ERP does not provide the variable you are looking for, there could be a
Bootstrap variable that allows it. Indeed all Konvergo ERP layouts respect Bootstrap
structures and use Bootstrap components or their extensions. If you customize
a Bootstrap variable, you add a generic style for the whole user website.

Use a dedicated file added to the `_assets_frontend_helpers` bundle to
override Bootstrap values and _not_ the `primary_variables.scss` file.

**Declaration**

`/website_airproof/__manifest__.py`

    
    
    'assets': {
       'web._assets_frontend_helpers': [
          ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
       ],
    },
    

**Use**

`/website_airproof/static/src/scss/bootstrap_overridden.scss`

    
    
    // Typography
    $h1-font-size:                 4rem !default;
    
    // Navbar
    $navbar-nav-link-padding-x:    1rem!default;
    
    // Buttons + Forms
    $input-placeholder-color:      o-color('o-color-1') !default;
    
    // Cards
    $card-border-width:            0 !default;
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>1 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>2
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>3

### Views

For some options, in addition to the Website Builder variable, you also have
to activate a specific view.

By reading the source code, templates related to options are easily found.

    
    
    <we-button title="..."
       data-name="..."
       data-customize-website-views="website.template_header_default"
       data-customize-website-variable="'...'"
       data-img="..."/>
    
    
    
    <template id="..." inherit_id="..." name="..." active="True"/>
    <template id="..." inherit_id="..." name="..." active="False"/>
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>4

## Assets

For this part, we will refer to the `assets_frontend` bundle located in the
web module. This bundle specifies the list of assets loaded by the Website
Builder, and the goal is to add your SCSS and JS files to the bundle.

### Styles

The Website Builder together with Bootstrap are great for defining the basic
styles of your website. But to design something unique, you should go a step
further. For this, you can easily add any SCSS file to your theme.

**Declaration**

`/website_airproof/__manifest__.py`

    
    
    'assets': {
       'web.assets_frontend': [
          'website_airproof/static/src/scss/theme.scss',
       ],
    },
    

Feel free to reuse the variables from your Bootstrap file and the ones used by
Konvergo ERP in your `theme.scss` file.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>5

### Interactivity

Konvergo ERP supports three different kinds of JavaScript files:

  * [plain JavaScript files](../../reference/frontend/javascript_modules#frontend-modules-plain-js) (no module system),

  * [native JavaScript module](../../reference/frontend/javascript_modules#frontend-modules-native-js), and

  * [Konvergo ERP modules](../../reference/frontend/javascript_modules#frontend-modules-odoo-module) (using a custom module system).

Most new Konvergo ERP JavaScript codes should use the native JavaScript module system.
It’s simpler and brings the benefit of a better developer experience with
better integration with the IDE.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>6

    
    
    /** @odoo-module **/
    

**Declaration**

`/website_airproof/__manifest__.py`

    
    
    'assets': {
       'web.assets_frontend': [
          'website_airproof/static/src/js/theme.js',
       ],
    },
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>8 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create a website theme, you only need to install the Website app. If you need other apps
(Blogs, Events, eCommerce, …), you can also add them.</p>
</div>9

