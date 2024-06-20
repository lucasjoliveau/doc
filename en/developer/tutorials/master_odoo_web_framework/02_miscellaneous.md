# Chapter 2: Miscellaneous

In the previous task, we learned how to create fields and views. There is
still much more to discover in the feature-rich Odoo web framework, so let’s
dive in and explore more in this chapter!

![../../../_images/previously_learned1.svg](../../../_images/previously_learned1.svg)

This is the progress that we have made in discovering the JavaScript web
framework at the end of [Chapter 1: Fields and
Views](01_fields_and_views.html).

Goal

![../../../_images/kitten_mode.png](../../../_images/kitten_mode.png)

Solutions

The solutions for each exercise of the chapter are hosted on the [official
Odoo tutorials
repository](https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt).

## 1\. Interacting with the notification system

Note

This task depends on [the previous exercises](01_fields_and_views.html).

After using the Print Label button for some t-shirt tasks, it is apparent that
there should be some feedback that the `print_label` action is completed (or
failed, for example, the printer is not connected or ran out of paper).

Exercise

  1. Display a [notification](../../reference/frontend/services.html#frontend-services-notification) message when the action is completed successfully, and a warning if it failed.

  2. If it failed, the notification should be permanent.

![../../../_images/notification.png](../../../_images/notification.png)

See also

[Example: Using the notification
service](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/views/fields/image_url/image_url_field.js)

## 2\. Add a systray item

Our beloved leader wants to keep a close eye on new orders. He wants to see
the number of new, unprocessed orders at all time. Let’s do that with a
systray item.

A [systray](../../reference/frontend/registries.html#frontend-registries-
systray) item is an element that appears in the system tray, which is a small
area located on the right-hand side of the navbar. The systray is used to
display notifications and provide access to certain features.

Exercise

  1. Create a systray component that connects to the statistics service we made previously.

  2. Use it to display the number of new orders.

  3. Clicking on it should open a list view with all of those orders.

  4. Bonus point: avoid making the initial RPC by adding the information to the session info. The session info is given to the web client by the server in the initial response.

![../../../_images/systray.png](../../../_images/systray.png)

See also

  * [Example: Systray item](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/webclient/user_menu/user_menu.js)

  * [Example: Adding some information to the “session info”](https://github.com/odoo/odoo/blob/16.0/addons/barcodes/models/ir_http.py)

  * [Example: Reading the session information](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/barcodes/static/src/barcode_service.js#L5)

## 3\. Real life update

So far, the systray item from above does not update unless the user refreshes
the browser. Let us do that by calling periodically (for example, every
minute) the server to reload the information.

Exercise

  1. The `tshirt` service should periodically reload its data.

Now, the question arises: how is the systray item notified that it should re-
render itself? It can be done in various ways but, for this training, we
choose to use the most _declarative_ approach:

Exercise

  2. Modify the `tshirt` service to return a [reactive](https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md#reactive) object. Reloading data should update the reactive object in place.

  3. The systray item can then perform a [useState](https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md#usestate) on the service return value.

  4. This is not really necessary, but you can also _package_ the calls to `useService` and `useState` in a custom hook `useStatistics`.

See also

  * [Documentation on reactivity](https://github.com/odoo/owl/blob/master/doc/reference/reactivity.md)

  * [Example: Use of reactive in a service](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/core/debug/profiling/profiling_service.js#L30)

## 4\. Add a command to the command palette

Now, let us see how we can interact with the command palette. The command
palette is a feature that allows users to quickly access various commands and
functions within the application. It is accessed by pressing `CTRL+K` in the
Odoo interface.

Exercise

Modify the [image preview field](01_fields_and_views.html#tutorials-master-
odoo-web-framework-image-preview-field) to add a command to the command
palette to open the image in a new browser tab (or window).

Ensure the command is only active whenever a field preview is visible on the
screen.

![../../../_images/new_command.png](../../../_images/new_command.png)

See also

[Example: Using the useCommand
hook](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/core/debug/debug_menu.js#L15)

## 5\. Monkey patching a component

Often, we can achieve what we want by using existing extension points that
allow for customization, such as registering something in a registry.
Sometimes, however, it happens that we want to modify something that has no
such mechanism. In that case, we must fall back on a less safe form of
customization: monkey patching. Almost everything in Odoo can be monkey
patched.

Bafien, our beloved leader, heard about employees performing better if they
are constantly being watched. Since he cannot be there in person for each of
his employees, he tasked you with updating the user interface to add a
blinking red eye in the control panel. Clicking on that eye should open a
dialog with the following message: “Bafien is watching you. This interaction
is recorded and may be used in legal proceedings if necessary. Do you agree to
these terms?”

Exercise

  1. [Inherit](../../reference/frontend/qweb.html#reference-qweb-template-inheritance) the `web.Breadcrumbs` template of the [ControlPanel component](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/search/control_panel) to add an icon next to the breadcrumbs. You might want to use the `fa-eye` or `fa-eyes` icons.

  2. [Patch](../../reference/frontend/patching_code.html) the component to display the message on click by using [the dialog service](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/dialog/dialog_service.js). You can use [ConfirmationDialog](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/confirmation_dialog/confirmation_dialog.js).

  3. Add the CSS class `blink` to the element representing the eye and paste the following code in a new CSS file located in your patch’s directory.
    
        .blink {
      animation: blink-animation 1s steps(5, start) infinite;
      -webkit-animation: blink-animation 1s steps(5, start) infinite;
    }
    @keyframes blink-animation {
      to {
        visibility: hidden;
      }
    }
    @-webkit-keyframes blink-animation {
      to {
          visibility: hidden;
      }
    }
    

![../../../_images/bafien_eye.png](../../../_images/bafien_eye.png)
![../../../_images/confirmation_dialog.png](../../../_images/confirmation_dialog.png)

See also

  * [Code: The patch function](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/core/utils/patch.js#L16)

  * [The Font Awesome website](https://fontawesome.com/)

  * [Example: Using the dialog service](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/board/static/src/board_controller.js#L88)

## 6\. Fetching orders from a customer

Let’s see how to use some standard components to build a powerful feature
combining autocomplete, fetching data, and fuzzy lookup. We will add an input
in our dashboard to easily search all orders from a given customer.

Exercise

  1. Update `tshirt_service.js` to add a `loadCustomers` method, which returns a promise that returns the list of all customers (and only performs the call once).

  2. Add the [AutoComplete component](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/autocomplete) to the dashboard, next to the buttons in the control panel.

  3. Fetch the list of customers with the tshirt service, and display it in the AutoComplete component, filtered by the [fuzzyLookup](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/utils/search.js) method.

![../../../_images/autocomplete.png](../../../_images/autocomplete.png)

## 7\. Reintroduce Kitten Mode

Let us add a special mode to Odoo: whenever the URL contains `kitten=1`, we
will display a kitten in the background of Odoo, because we like kittens.

Exercise

  1. Create a `kitten` service, which should check the content of the active URL hash with the help of the [router service](../../reference/frontend/services.html#frontend-services-router). If `kitten` is set in the URL, add the class `o-kitten-mode` to the document body.

  2. Add the following SCSS in `kitten_mode.scss`:
    
        .o-kitten-mode {
      background-image: url(https://upload.wikimedia.org/wikipedia/commons/5/58/Mellow_kitten_%28Unsplash%29.jpg);
      background-size: cover;
      background-attachment: fixed;
    }
    
    .o-kitten-mode > * {
      opacity: 0.9;
    }
    

  3. Add a command to the command palette to toggle the kitten mode. Toggling the kitten mode should toggle the class `o-kitten-mode` and update the current URL accordingly.

![../../../_images/kitten_mode.png](../../../_images/kitten_mode.png)

## 8\. Lazy loading our dashboard

This is not really necessary, but the exercise is interesting. Imagine that
our awesome dashboard is a large application with potentially multiple
external libraries and lots of code/styles/templates. Also, suppose that the
dashboard is used only by some users in some business flows. It would be
interesting to lazy load it in order to speed up the loading of the web client
in most cases.

So, let us do that!

Exercise

  1. Modify the manifest to create a new [bundle](../../reference/frontend/assets.html#reference-assets-bundle) `awesome_tshirt.dashboard`.

  2. Add the awesome dashboard code to this bundle. Create folders and move files if needed.

  3. Remove the code from the `web.assets_backend` bundle so that it is not loaded twice.

So far, we only removed the dashboard from the main bundle; we now want to
lazy load it. Currently, no client action is registered in the action
registry.

Exercise

  4. Create a new file `dashboard_loader.js`.

  5. Copy the code registering `AwesomeDashboard` to the dashboard loader.

  6. Register `AwesomeDashboard` as a [LazyComponent](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/src/core/assets.js#L265-L282).

  7. Modify the code in the dashboard loader to use the lazy component `AwesomeDashboard`.

If you open the Network tab of your browser’s dev tools, you should see that
`awesome_tshirt.dashboard.min.js` is now loaded only when the Dashboard is
first accessed.

See also

[Documentation on assets](../../reference/frontend/assets.html#reference-
assets)

