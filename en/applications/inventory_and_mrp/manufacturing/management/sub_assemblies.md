# Manage semi-finished products

A _semi-finished product_ , also known as a _subassembly_ , is a manufactured
product that is used as a component in another product’s bill of materials
(BoM). Semi-finished products are used to simplify complex BoMs or to more
accurately represent a manufacturing flow. A BoM that contains semi-finished
products is referred to as a _multilevel BoM_ , where the main _top-level
product_ and its subassemblies are distinguished.

## Configure semi-finished products

To set up a multilevel BoM, the top-level product and semi-finished products
must be configured. Therefore, the first step is to create the semi-finished
products and their BoMs.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="bill_configuration">Bill of materials</a></p>
</div> ![A bill of materials for a semi-finished
product.](../../../../_images/semifinished-product-bom.png)

## Create the top-level bill of materials (BoM)

After the semi-finished products are fully configured, navigate to
Manufacturing ‣ Products ‣ Products. Then, **Create** the top-level product.
Configure the product’s specifications as desired, and be sure to **Save**.

Once the top-level product is configured, click the **Bill of Materials**
smart button on the product form, then click **Create** to make a BoM for the
top-level product. Then, simply add the semi-finished products to this BoM,
along with any other necessary components.

![A bill of materials for a top-level product, containing a subassembly
component.](../../../../_images/custom-computer-bom.png)

## Manage production planning

There are several methods to manage manufacturing order automation for
products with multilevel BoMs.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Semi-finished products are specifically used to manage manufacturable products with multilevel
BoMs. If a BoM is being created simply to organize components or bundle sellable products,
using <a href="kit_shipping">Kits</a> is the more appropriate option.</p>
</div>

To automatically trigger manufacturing orders for semi-finished products after
confirming a manufacturing order for the main product, there are two options:

  * **Option 1 (recommended):** Create _Reordering Rules_ for the semi-finished products and set both the minimum and maximum desired stock quantities to `0`.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../purchase/products/reordering">Configure reordering rules</a></p>
</div>

  * **Option 2:** Activate the **Replenish on Order (MTO)** and **Manufacture** routes under the **Inventory** tab of the semi-finished product’s product form.

Option 1 is more flexible than Option 2 and is therefore recommended.
Reordering rules do not directly link demand to replenishment, and therefore
allow stocks to be unreserved and redirected to other orders, if necessary.
The Replenish on Order (MTO) route creates a unique link between the semi-
finished and top-level products, exclusively reserving quantities for the
confirmed top-level manufacturing order.

Regardless of the method chosen, semi-finished products must be fully
manufactured before manufacturing can begin on the top-level product.

![A manufacturing order for a top-level
product.](../../../../_images/semifinished-on-mo.png)

  *[BoMs]: Bills of Materials
  *[BoM]: Bill of Materials

