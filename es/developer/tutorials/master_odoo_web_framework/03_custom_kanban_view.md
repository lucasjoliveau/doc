# Chapter 3: Custom kanban view

Advertencia

It is highly recommended that you complete [Chapter 1: Fields and
Views](01_fields_and_views.html) before starting this chapter. The concepts
introduced in Chapter 3, including views and examples, will be essential for
understanding the material covered in this chapter.

We have gained an understanding of the numerous capabilities offered by the
Odoo web framework. As a next step, we will customize a kanban view. This is a
more complicated project that will showcase some non trivial aspects of the
framework. The goal is to practice composing views, coordinating various
aspects of the UI, and doing it in a maintainable way.

Bafien had the greatest idea ever: a mix of a kanban view and a list view
would be perfect for your needs! In a nutshell, he wants a list of customers
on the left of the task’s kanban view. When you click on a customer on the
left sidebar, the kanban view on the right is filtered to only display orders
linked to that customer.

Goal

![../../../_images/overview1.png](../../../_images/overview1.png)

Solutions

The solutions for each exercise of the chapter are hosted on the [official
Odoo tutorials
repository](https://github.com/odoo/tutorials/commits/16.0-solutions/awesome_tshirt).

## 1\. Create a new kanban view

Since we are customizing the kanban view, let us start by extending it and
using our extension in the kanban view for the tshirt orders.

Exercise

  1. Extend the kanban view by extending the kanban controller and by creating a new view object.

  2. Register it in the views registry under `awesome_tshirt.customer_kanban`.

  3. Update the kanban arch to use the extended view. This can be done with the `js_class` attribute.

## 2\. Create a CustomerList component

We will need to display a list of customers, so we might as well create the
component.

Exercise

  1. Create a `CustomerList` component which only displays a `div` with some text for now.

  2. It should have a `selectCustomer` prop.

  3. Create a new template extending (XPath) the kanban controller template to add the `CustomerList` next to the kanban renderer. Give it an empty function as `selectCustomer` for now.

  4. Subclass the kanban controller to add `CustomerList` in its sub-components.

  5. Make sure you see your component in the kanban view.

![../../../_images/customer_list.png](../../../_images/customer_list.png)

## 3\. Load and display data

Exercise

  1. Modify the `CustomerList` component to fetch a list of all customers in `onWillStart`.

  2. Display the list in the template with a `t-foreach`.

  3. Whenever a customer is selected, call the `selectCustomer` function prop.

![../../../_images/customer_data.png](../../../_images/customer_data.png)

## 4\. Update the main kanban view

Exercise

  1. Implement `selectCustomer` in the kanban controller to add the proper domain.

  2. Modify the template to give the real function to the `CustomerList` `selectCustomer` prop.

Since it is not trivial to interact with the search view, here is a quick
snippet to help:

    
    
    selectCustomer(customer_id, customer_name) {
       this.env.searchModel.setDomainParts({
          customer: {
                domain: [["customer_id", "=", customer_id]],
                facetLabel: customer_name,
          },
       });
    }
    

![../../../_images/customer_filter.png](../../../_images/customer_filter.png)

## 5\. Only display customers which have an active order

There is a `has_active_order` field on `res.partner`. Let us allow the user to
filter results on customers with an active order.

Exercise

  1. Add an input of type checkbox in the `CustomerList` component, with a label «Active customers» next to it.

  2. Changing the value of the checkbox should filter the list on customers with an active order.

![../../../_images/active_customer.png](../../../_images/active_customer.png)

## 6\. Add a search bar to the customer list

Exercise

Add an input above the customer list that allows the user to enter a string
and to filter the displayed customers, according to their name.

Truco

You can use the `fuzzyLookup` function to perform the filter.

![../../../_images/customer_search.png](../../../_images/customer_search.png)

Ver también

  * [Code: The fuzzylookup function](https://github.com/odoo/odoo/blob/16.0/addons/web/static/src/core/utils/search.js)

  * [Example: Using fuzzyLookup](https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/addons/web/static/tests/core/utils/search_test.js#L17)

## 7\. Refactor the code to use `t-model`

To solve the previous two exercises, it is likely that you used an event
listener on the inputs. Let us see how we could do it in a more declarative
way, with the
[t-model](https://github.com/odoo/owl/blob/master/doc/reference/input_bindings.md)
directive.

Exercise

  1. Make sure you have a reactive object that represents the fact that the filter is active (something like `this.state = useState({ displayActiveCustomers: false, searchString: ''})`).

  2. Modify the code to add a getter `displayedCustomers` which returns the currently active list of customers.

  3. Modify the template to use `t-model`.

## 8\. Paginate customers!

Exercise

  1. Add a [pager](../../reference/frontend/owl_components.html#frontend-pager) in the `CustomerList`, and only load/render the first 20 customers.

  2. Whenever the pager is changed, the customer list should update accordingly.

This is actually pretty hard, in particular in combination with the filtering
done in the previous exercise. There are many edge cases to take into account.

![../../../_images/customer_pager.png](../../../_images/customer_pager.png)

