# Chapter 5: Testing

Automatically testing code is important when working on a codebase. It helps
ensure we don’t introduce (too many) bugs or regressions. Let us see how to
test our code.

Solutions

The solutions for each exercise of the chapter are hosted on the [official
Odoo tutorials
repository](https://github.com/odoo/tutorials/commits/16.0-solutions).

## 1\. Integration testing

To make sure our application works as expected, we can perform [integration
testing](../../reference/backend/testing.html#reference-testing-integration-
testing) by creating a tour: this is a sequence of steps that we can execute.
Each step wait until some desired DOM state is reached, then performs an
action. If, at some point, it is unable to go to the next step for a long
time, the tour fails.

Let’s write a tour to ensure that it is possible to perform an tshirt order
from our public route

Exercise

  1. In the `awesome_tshirt` addon, add a `/static/tests/tours` folder.

  2. Add a `/static/tests/tours/order_flow.js` file.

  3. Add a tour that performs the following steps:

    1. Open the `/awesome_tshirt/order` route.

    2. Fill the order form.

    3. Validate it.

    4. Navigate to our webclient.

    5. Open the list view for the the t-shirt order.

    6. Check that our order can be found in the list.

  4. Run the tour manually.

  5. Add a Python test to run it programmatically.

  6. Run the tour from the terminal.

## 2\. Unit testing a Component

It is also useful to test independently a component or a piece of code.
[QUnit](../../reference/backend/testing.html#reference-testing-qunit) tests
are useful to quickly locate an issue.

Exercise

  1. In the `awesome_tshirt` addon, add a `static/tests/counter_tests.js` file.

  2. Add a QUnit test that instantiates a counter, clicks on it, and makes sure it is incremented.

![../../../_images/component_test.png](../../../_images/component_test.png)

See also

[Example: Testing an Owl
component](https://github.com/odoo/odoo/blob/16.0/addons/web/static/tests/core/checkbox_tests.js)

## 3\. Unit testing our gallery view

Many components need more setup to be tested. In particular, we often need to
mock some demo data. Let us see how to do that.

Note

This depends on our Gallery View from [Chapter 4: Creating a view from
scratch](04_creating_view_from_scratch.html).

Exercise

  1. In the `awesome_gallery` addon, add a `/static/tests/gallery_view_tests.js` file.

  2. Add a test that instantiates the gallery view with some demo data.

  3. Add another test that checks that when the user clicks on an image, it is switched to the form view of the corresponding order.

![../../../_images/view_test.png](../../../_images/view_test.png)

See also

[Example: Testing a list
view](https://github.com/odoo/odoo/blob/16.0/addons/web/static/tests/views/list_view_tests.js)

