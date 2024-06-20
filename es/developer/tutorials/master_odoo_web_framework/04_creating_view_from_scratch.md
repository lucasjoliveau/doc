# Chapter 4: Creating a view from scratch

Advertencia

It is highly recommended that you complete [Chapter 1: Fields and
Views](01_fields_and_views.html) before starting this chapter. The concepts
introduced in Chapter 3, including views and examples, will be essential for
understanding the material covered in this chapter.

Let us see how one can create a new view, completely from scratch. In a way,
it is not very difficult to do, but there are no really good resources on how
to do it. Note that most situations should be solved by either customizing an
existing view, or with a client action.

For this exercise, let’s assume that we want to create a `gallery` view, which
is a view that lets us represent a set of records with an image field. In our
Awesome Tshirt scenario, we would like to be able to see a set of t-shirts
images.

The problem could certainly be solved with a kanban view, but this means that
it is not possible to have our normal kanban view and the gallery view in the
same action.

Let us make a gallery view. Each gallery view will be defined by an
`image_field` attribute in its arch:

    
    
    <gallery image_field="some_field"/>
    

To complete the tasks in this chapter, you will need to install the
awesome_gallery addon. This addon includes the necessary server files to add a
new view.

Goal

![../../../_images/overview2.png](../../../_images/overview2.png)

Solutions

The solutions for each exercise of the chapter are hosted on the [official
Odoo tutorials
repository](https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_gallery).

## 1\. Make a hello world view

First step is to create a JavaScript implementation with a simple component.

Exercise

  1. Create the `gallery_view.js` , `gallery_controller.js` and `gallery_controller.xml` files in `static/src`.

  2. Implement a simple hello world component in `gallery_controller.js`.

  3. In `gallery_view.js`, import the controller, create a view object, and register it in the view registry under the name `gallery`.

  4. Add `gallery` as one of the view type in the orders action.

  5. Make sure that you can see your hello world component when switching to the gallery view.

![../../../_images/view_button.png](../../../_images/view_button.png)
![../../../_images/new_view.png](../../../_images/new_view.png)

## 2\. Use the Layout component

So far, our gallery view does not look like a standard view. Let’s use the
`Layout` component to have the standard features like other views.

Exercise

  1. Import the `Layout` component and add it to the `components` of `GalleryController`.

  2. Update the template to use `Layout`. It needs a `display` prop, which can be found in `props.display`.

![../../../_images/layout1.png](../../../_images/layout1.png)

## 3\. Parse the arch

For now, our gallery view does not do much. Let’s start by reading the
information contained in the arch of the view.

The process of parsing an arch is usually done with a `ArchParser`, specific
to each view. It inherits from a generic `XMLParser` class.

Example

Here is an example of what an ArchParser might look like:

    
    
    import { XMLParser } from "@web/core/utils/xml";
    
    export class GraphArchParser extends XMLParser {
        parse(arch, fields) {
           const result = {};
           this.visitXML(arch, (node) => {
               ...
            });
           return result;
        }
    }
    

Exercise

  1. Create the `ArchParser` class in its own file. It can inherit from `XMLParser` in `@web/core/utils/xml`.

  2. Use it to read the `image_field` information.

  3. Update the `gallery` view code to add it to the props received by the controller.

Nota

It is probably a little overkill to do it like that, since we basically only
need to read one attribute from the arch, but it is a design that is used by
every other odoo views, since it lets us extract some upfront processing out
of the controller.

Ver también

[Example: The graph arch
parser](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/graph/graph_arch_parser.js)

## 4\. Load some data

Let us now get some real data.

Exercise

  1. Add a `loadImages(domain) {...}` method to the `GalleryController`. It should perform a `webSearchRead` call from the orm service to fetch records corresponding to the domain, and use `imageField` received in props.

  2. Modify the `setup` code to call that method in the `onWillStart` and `onWillUpdateProps` hooks.

  3. Modify the template to display the data inside the default slot of the `Layout` component.

Nota

The loading data code will be moved into a proper model in the next exercise.

![../../../_images/gallery_data.png](../../../_images/gallery_data.png)

## 5\. Reorganize code

Real views are a little bit more organized. This may be overkill in this
example, but it is intended to learn how to structure code in Odoo. Also, this
will scale better with changing requirements.

Exercise

  1. Move all the model code in its own `GalleryModel` class.

  2. Move all the rendering code in a `GalleryRenderer` component.

  3. Adapt the `GalleryController` and `gallery_view` to make it work.

## 6\. Display images

Exercise

Update the renderer to display images in a nice way, if the field is set. If
`image_field` is empty, display an empty box instead.

![../../../_images/tshirt_images.png](../../../_images/tshirt_images.png)

## 7\. Switch to form view on click

Exercise

Update the renderer to react to a click on an image and switch to a form view.
You can use the `switchView` function from the action service.

Ver también

[Code: The switchView
function](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/webclient/actions/action_service.js#L1329)

## 8\. Add an optional tooltip

It is useful to have some additional information on mouse hover.

Exercise

  1. Update the code to allow an optional additional attribute on the arch:
    
        <gallery image_field="some_field" tooltip_field="some_other_field"/>
    

  2. On mouse hover, display the content of the tooltip field. It should work if the field is a char field, a number field or a many2one field.

  3. Update the orders gallery view to add the customer as tooltip field.

![../../../_images/image_tooltip.png](../../../_images/image_tooltip.png)

Ver también

[Code: The tooltip
hook](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/tooltip/tooltip_hook.js)

## 9\. Add pagination

Exercise

Let’s add a pager on the control panel and manage all the pagination like in a
normal Odoo view. Note that it is surprisingly difficult.

![../../../_images/pagination.png](../../../_images/pagination.png)

Ver también

[Code: The usePager
hook](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/search/pager_hook.js)

## 10\. Validating views

We have a nice and useful view so far. But in real life, we may have issue
with users incorrectly encoding the `arch` of their Gallery view: it is
currently only an unstructured piece of XML.

Let us add some validation! In Odoo, XML documents can be described with an RN
file (Relax NG file), and then validated.

Exercise

  1. Add an RNG file that describes the current grammar:

     * A mandatory attribute `image_field`.

     * An optional attribute: `tooltip_field`.

  2. Add some code to make sure all views are validated against this RNG file.

  3. While we are at it, let us make sure that `image_field` and `tooltip_field` are fields from the current model.

Since validating an RNG file is not trivial, here is a snippet to help:

    
    
    # -*- coding: utf-8 -*-
    import logging
    import os
    
    from lxml import etree
    
    from odoo.loglevels import ustr
    from odoo.tools import misc, view_validation
    
    _logger = logging.getLogger(__name__)
    
    _viewname_validator = None
    
    @view_validation.validate('viewname')
    def schema_viewname(arch, **kwargs):
        """ Check the gallery view against its schema
    
        :type arch: etree._Element
        """
        global _viewname_validator
    
        if _viewname_validator is None:
            with misc.file_open(os.path.join('modulename', 'rng', 'viewname.rng')) as f:
                _viewname_validator = etree.RelaxNG(etree.parse(f))
    
        if _viewname_validator.validate(arch):
            return True
    
        for error in _viewname_validator.error_log:
            _logger.error(ustr(error))
        return False
    

Ver también

[Example: The RNG file of the graph
view](https://github.com/odoo/odoo/blob/16.0/addons/base/rng/graph_view.rng)

