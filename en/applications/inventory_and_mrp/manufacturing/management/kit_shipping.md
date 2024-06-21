# Use kits

In Konvergo ERP, a _kit_ is a type of bill of materials (BoM) that can be manufactured
and sold. Kits are sets of unassembled components sold to customers. They may
be sold as standalone products, but are also useful tools for managing more
complex bills of materials (BoMs).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To use, manufacture, and sell kits, both the <b>Manufacturing</b> and <b>Inventory</b>
apps need to be installed.</p>
</div>

## Create the kit as a product

To use a kit as a sellable product, or simply as a component organization
tool, the kit should first be created as a product.

To create a kit product, go to Inventory app ‣ Products ‣ Products, and click
**Create**.

Then, assign a name to the new kit product. Next, under the **General
Information** tab, set the **Product Type** to **Consumable**. Kit products
work best as consumables, because the stock on-hand for kits is typically not
tracked.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Although kits should almost always be set to <b>Consumable</b>, companies using
<b>Anglo-Saxon</b> accounting might need to create kits as a <b>Storable Product</b>. This is
because when processing invoices for kits, the Cost of Goods Sold (COGS) will be posted in
accounting journals.</p>
</div>

Unlike storable products, the **Routes** designation under the **Inventory**
tab does not matter for kits, since Konvergo ERP uses the routes of the kit’s
individual components for replenishment purposes. All other parameters for the
kit product may be modified according to preference. Once ready, click
**Save** to save the new product.

The kit’s components must also be configured as products via Inventory app ‣
Products ‣ Products. These components require no specific configuration.

## Set up the kit BoM

After fully configuring the kit product and its components, a new BoM can be
created for the kit product.

To do so, go to Manufacturing app ‣ Products ‣ Bills of Materials, and click
**Create**. Next to the **Product** field, click the drop-down menu to reveal
a list of products, and select the previously configured kit product.

Then, for the **BoM Type** field, select the **Kit** option. Finally, under
the **Components** tab, click **Add a line** , and add each desired component,
and specify their quantities under the **Quantity** column.

Once ready, click **Save** to save the newly-created BoM.

![Kit selection on the bill of materials.](../../../../_images/bom-kit-
selection.png)

If the kit is solely being used as a sellable product, then only components
need to be added under the **Components** tab, and configuring manufacturing
operations is not necessary.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When a kit is sold as a product, it appears as a single line item on the quotation and sales
order. However, on delivery orders, each component of the kit is listed.</p>
</div>

## Use kits to manage complex BoMs

Kits are also used to manage multi-level BoMs. These are products that contain
**other** BoM products as components, and therefore require _nested_ BoMs.
Incorporating pre-configured kits into multi-level BoMs allows for cleaner
organization of bundled products.

To configure this type of BoM with a kit as a component, go to Manufacturing
app ‣ Products ‣ Bills of Materials, and click **Create**.

Next to the **Product** field, click the drop-down menu to reveal a list of
products, and select the desired BoM product. Then, for the **BoM Type**
field, select the **Manufacture this product** option.

Under the **Components** tab, click **Add a line** , and select a kit as the
component. Adding the kit as a component eliminates the need to add the kit’s
components individually. Any **BoM Type** can be used for the higher-level
product’s BoM.

Once ready, click **Save** to save changes.

![Kit as a component in a multilevel bill of
materials.](../../../../_images/multilevel-bom-kit.png)

### Structure & cost

To access a comprehensive overview of the multi-level BoM’s components, click
on the **Structure & Cost** smart button. Sublevel BoMs can be expanded and
viewed from this report.

![Expanded kit in the Structure and Cost
report.](../../../../_images/structure-and-cost-kit.png)

When creating a manufacturing order for a product with a multi-level BoM, the
kit product automatically expands to show all components. Any operations in
the kit’s BoM are also added to the list of work orders on the manufacturing
order.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Kits are primarily used to bundle components together for organization or sale. To manage
multi-level products that require manufactured sub-components, refer to <a href="sub_assemblies">this documentation</a> on sub-assemblies.</p>
</div>

  *[BoM]: bill of materials
  *[BoMs]: bills of materials
  *[BoM’s]: bill of material's

