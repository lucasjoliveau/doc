# Layout

In this chapter, you will learn how to:

  * Create a custom header.

  * Create a custom footer.

  * Modify a standard template.

  * Add a copyright section.

  * Improve your website’s responsiveness.

## Default

An Odoo page combines cross-page and unique elements. Cross-page elements are
the same on every page, while unique elements are only related to a specific
page. By default, a page has two cross-page elements, the header and the
footer, and a unique main element that contains the specific content of that
page.

    
    
    <div id="wrapwrap">
       <header/>
          <main>
             <div id="wrap" class="oe_structure">
                <!-- Page Content -->
             </div>
          </main>
       <footer/>
    </div>
    

Any Odoo XML file starts with encoding specifications. After that, you must
write your code inside an `<odoo>` tag.

    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <odoo>
       ...
    </odoo>
    

Note

Using precise file names is important to find information through all modules
quickly. File names should only contain lowercase alphanumerics and
underscores.

Always add an empty line at the end of your file. This can be done
automatically by configuring your IDE.

## XPath

XPath (XML Path Language) is an expression language that enables you to
navigate through elements and attributes in an XML document easily. XPath is
used to extend standard Odoo templates.

A view is coded the following way.

    
    
    <template id="..." inherit_id="..." name="...">
       <!-- Content -->
    </template>
    

Attribute | Description  
---|---  
id | ID of the modified view  
inherited_id | ID of the standard view  
name | Human-readable name of the modified view  
  
For each XPath, you modify two attributes: **expression** and **position**.

Example

`/website_airproof/views/website_templates.xml`

    
    
    <template id="layout" inherit_id="website.layout" name="Welcome Message">
       <xpath expr="//header" position="before">
          <!-- Content -->
       </xpath>
    </template>
    

This XPath adds a welcome message right before the page content.

Warning

Be careful when replacing default elements’ attributes. As your theme extends
the default one, your changes will take priority over any future Odoo update.

Note

  * You should update your module every time you create a new template or record.

  * _XML IDs_ of inheriting views should use the same _ID_ as the original record. It helps to find all inheritance at a glance. As final _XML IDs_ are prefixed by the module that creates them, there is no overlap.

### Expressions

XPath uses path expressions to select nodes in an XML document. Selectors are
used inside the expression to target the right element. The most useful ones
are listed below.

Descendent selectors | Description  
---|---  
/ | Selects from the root node.  
// | Selects nodes in the document from the current node that matches the selection no matter where they are.  
Attribute selectors | Description  
---|---  
* | Selects any XML tag. `*` can be replaced by a specific tag if the selection needs to be more precise.  
*[@id=”id”] | Selects a specific ID.  
*[hasclass(“class”)] | Selects a specific class.  
*[@name=”name”] | Selects a tag with a specific name.  
*[@t-call=”t-call”] | Selects a specific t-call.  
  
### Position

The position defines where the code is placed inside the template. The
possible values are listed below:

Position | Description  
---|---  
replace | Replaces the targeted node with the XPath content.  
inside | Adds the XPath content inside the targeted node.  
before | Adds the XPath content before the targeted node.  
after | Adds the XPath content after the targeted node.  
attributes | Adds the XPath content inside an attribute.  
  
Example

This XPath adds a `<div>` before the `<nav>` that is a direct child of the
`<header>`.

    
    
    <xpath expr="//header/nav" position="before">
       <div>Some content before the header</div>
    </xpath>
    

This XPath adds `x_airproof_header` in the class attribute of the header. You
also need to define a `separator` attribute to add a space before the class
you are adding.

    
    
    <xpath expr="//header" position="attributes">
       <attribute name="class" add="x_airproof_header" separator=" "/>
    </xpath>
    

This XPath removes `x_airproof_header` in the class attribute of the header.
In this case, you don’t need to use the `separator` attribute.

    
    
    <xpath expr="//header" position="attributes">
       <attribute name="class" remove="x_airproof_header" />
    </xpath>
    

This XPath removes the first element with a `.breadcrumb` class.

    
    
    <xpath expr="//*[hasclass('breadcrumb')]" position="replace"/>
    

This XPath adds an extra `<li>` element after the last child of the `<ul>`
element.

    
    
    <xpath expr="//ul" position="inside">
       <li>Last element of the list</li>
    </xpath>
    

See also

You can find more information about XPath in this [cheat
sheet](https://devhints.io/xpath).

## QWeb

QWeb is the primary templating engine used by Odoo. It is an XML templating
engine mainly used to generate HTML fragments and pages.

See also

[QWeb templates documentation](../../reference/frontend/qweb.html).

## Background

You can define a color or an image as the background of your website.

**Colors**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-color-palettes: map-merge($o-color-palettes,
       (
          'airproof': (
             'o-cc1-bg':                     'o-color-5',
             'o-cc5-bg':                     'o-color-1',
          ),
        )
    );
    

**Image/pattern**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'body-image': '/website_airproof/static/src/img/background-lines.svg',
          'body-image-type': 'image' or 'pattern'
       )
    );
    

## Header

By default, the header contains a responsive navigation menu and the company’s
logo. You can easily add new elements or create your own template.

### Standard

Enable one of the header default templates.

Important

Don’t forget that you may need to disable the active header template first.

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'header-template': 'Contact',
       ),
    );
    

`/website_airproof/data/presets.xml`

    
    
    <record id="website.template_header_contact" model="ir.ui.view">
       <field name="active" eval="True"/>
    </record>
    

### Custom

Create your own template and add it to the list.

Important

Don’t forget that you may need to disable the active header template first.

**Option**

Use the following code to add an option for your new custom header on the
Website Builder.

`/website_airproof/data/presets.xml`

    
    
    <template id="template_header_opt" inherit_id="website.snippet_options" name="Header Template - Option">
       <xpath expr="//we-select[@data-variable='header-template']" position="inside">
          <we-button title="airproof"
             data-customize-website-views="website_airproof.header"
             data-customize-website-variable="'airproof'"  data-img="/website_airproof/static/src/img/wbuilder/template_header_opt.svg"/>
       </xpath>
    </template>
    

Attribute | Description  
---|---  
data-customize-website-views | The template to enable  
data-customize-website-variable | The name given to the variable  
data-img | The thumbnail of the custom template shown in the templates selection on the Website Builder  
  
Now you have to explicitly define that you want to use your custom template in
the Odoo SASS variables.

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'header-template': 'airproof',
       ),
    );
    

**Layout**

`/website_airproof/views/website_templates.xml`

    
    
    <record id="header" model="ir.ui.view">
       <field name="name">Airproof Header</field>
       <field name="type">qweb</field>
       <field name="key">website_airproof.header</field>
       <field name="inherit_id" ref="website.layout"/>
       <field name="mode">extension</field>
       <field name="arch" type="xml">
          <xpath expr="//header//nav" position="replace">
             <!-- Static Content -->
             <!-- Components -->
             <!-- Editable areas -->
          </xpath>
       </field>
    </record>
    

### Components

In your custom header, you can call several sub-templates using the `t-call`
directive from QWeb:

#### Logo

    
    
    <t t-call="website.placeholder_header_brand">
       <t t-set="_link_class" t-valuef="..."/>
    </t>
    

Don’t forget to record the logo of your website in the database.

`/website_airproof/data/images.xml`

    
    
    <record id="website.default_website" model="website">
       <field name="logo" type="base64" file="website_airproof/static/src/img/content/logo.png"/>
    </record>
    

#### Menu

    
    
    <t t-foreach="website.menu_id.child_id" t-as="submenu">
       <t t-call="website.submenu">
          <t t-set="item_class" t-valuef="nav-item"/>
          <t t-set="link_class" t-valuef="nav-link"/>
       </t>
    </t>
    

#### Sign in

    
    
    <t t-call="portal.placeholder_user_sign_in">
       <t t-set="_item_class" t-valuef="nav-item"/>
       <t t-set="_link_class" t-valuef="nav-link"/>
    </t>
    

#### User dropdown

    
    
    <t t-call="portal.user_dropdown">
       <t t-set="_user_name" t-value="true"/>
       <t t-set="_icon" t-value="false"/>
       <t t-set="_avatar" t-value="false"/>
       <t t-set="_item_class" t-valuef="nav-item dropdown"/>
       <t t-set="_link_class" t-valuef="nav-link"/>
       <t t-set="_dropdown_menu_class" t-valuef="..."/>
    </t>
    

#### Language selector

    
    
    <t t-call="website.placeholder_header_language_selector">
       <t t-set="_div_classes" t-valuef="..."/>
    </t>
    

#### Call to action

    
    
    <t t-call="website.placeholder_header_call_to_action">
       <t t-set="_div_classes" t-valuef="..."/>
    </t>
    

#### Navbar toggler

    
    
    <t t-call="website.navbar_toggler">
       <t t-set="_toggler_class" t-valuef="..."/>
    </t>
    

See also

You can add a [header overlay](pages.html#header-overlay) to position your
header over the content of your page. It has to be done on each page
individually.

## Footer

By default, the footer contains a section with some static content. You can
easily add new elements or create your own template.

### Standard

Enable one of the default footer templates. Don’t forget that you may need to
disable the active footer template first.

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'header-template': 'Contact',
       ),
    );
    

`/website_airproof/data/presets.xml`

    
    
    <record id="website.template_header_contact" model="ir.ui.view">
       <field name="active" eval="True"/>
    </record>
    

### Custom

Create your own template and add it to the list. Don’t forget that you may
need to disable the active footer template first.

**Option**

`/website_airproof/data/presets.xml`

    
    
    <template id="template_header_opt" inherit_id="website.snippet_options" name="Footer Template - Option">
       <xpath expr="//we-select[@data-variable='footer-template']" position="inside">
          <we-button title="airproof"
             data-customize-website-views="website_airproof.footer"
             data-customize-website-variable="'airproof'"
             data-img="/website_airproof/static/src/img/wbuilder/template_header_opt.svg"/>
       </xpath>
    </template>
    

**Declaration**

`/website_airproof/static/src/scss/primary_variables.scss`

    
    
    $o-website-values-palettes: (
       (
          'footer-template': 'airproof',
       ),
    );
    

**Layout**

`/website_airproof/views/website_templates.xml`

    
    
    <record id="footer" model="ir.ui.view">
       <field name="name">Airproof Footer</field>
       <field name="type">qweb</field>
       <field name="key">website_airproof.footer</field>
       <field name="inherit_id" ref="website.layout"/>
       <field name="mode">extension</field>
       <field name="arch" type="xml">
          <xpath expr="//div[@id='footer']" position="replace">
             <div id="footer" class="oe_structure oe_structure_solo" t-ignore="true" t-if="not no_footer">
                <!-- Content -->
             </div>
          </xpath>
       </field>
    </record>
    

## Copyright

There is only one template available at the moment for the copyright bar.

To replace the content or modify its structure, you can add your own code to
the following XPath.

`/website_airproof/views/website_templates.xml`

    
    
    <template id="copyright" inherit_id="website.layout">
       <xpath expr="//div[hasclass('o_footer_copyright')]" position="replace">
          <div class="o_footer_copyright" data-name="Copyright">
             <!-- Content -->
          </div>
       </xpath>
    </template>
    

## Drop zone

Instead of defining the complete layout of a page, you can create building
blocks (snippets) and let the user choose where to drag and drop them,
creating the page layout on their own. We call this _modular design_.

You can define an empty area that the user can fill with snippets.

    
    
    <div id="oe_structure_layout_01" class="oe_structure"/>
    

Class | Description  
---|---  
oe_structure | Define a drag-and-drop area for the user.  
oe_structure_solo | Only one snippet can be dropped in this area.  
  
You can also populate an existing drop zone with your content.

    
    
    <template id="oe_structure_layout_01" inherit_id="..." name="...">
       <xpath expr="//*[@id='oe_structure_layout_01']" position="replace">
          <div id="oe_structure_layout_01" class="oe_structure oe_structure_solo">
             <!-- Content -->
          </div>
       </xpath>
    </template>
    

## Responsive

You can find some hints below to help you make your website responsive.

### Bootstrap

See also

  * [Bootstrap documentation on responsive breakpoints](https://getbootstrap.com/docs/4.6/layout/overview/#responsive-breakpoints)

  * [Bootstrap documentation on display property](https://getbootstrap.com/docs/4.6/utilities/display/)

**Font size**

As of v4.3.0, Bootstrap ships with the option to enable responsive font sizes,
allowing text to scale more naturally across device and viewport sizes. Enable
them by changing the `$enable-responsive-font-sizes` Sass variable to true.

See also

[Responsive Font Size GitHub](https://github.com/twbs/rfs/tree/v8.1.0)

### Website Builder

Hide a specific `<section>` on mobile.

    
    
    <section class="d-none d-md-block">
       <!-- Content -->
    </section>
    

Hide a `<col>` on mobile.

    
    
    <section>
       <div class="container">
          <div class="row d-flex align-items-stretch">
             <div class="col-lg-4 d-none d-md-block">
                <!-- Content -->
             </div>
          </div>
       </div>
    </section>
    

