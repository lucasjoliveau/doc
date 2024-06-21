# Bill of materials

A _bill of materials_ (or _BoM_ for short) is a document that defines the
quantity of each component required to make or deliver a finished product. It
can also include various operations and the individual step guidelines needed
to complete a production process.

In Konvergo ERP Manufacturing, multiple BoMs can be linked to each product, so even
product variants can have their own tailored BoMs.

Correctly setting up a BoM helps optimize the manufacturing process and save
time.

## Set up a bill of materials (BoM)

The simplest BoM setup is one without operations or instructions, only
components. In this case, the production is solely managed using
_Manufacturing Orders_.

To create a BoM from the **Manufacturing** module, go to Products ‣ Bills of
Materials. Then, click **Create**. Next, specify the **Product**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>A <abbr title="Bill of Materials">BoM</abbr> can also be created directly from the product form, in which
case the <b>Product</b> field is pre-filled.</p>
</div>

For a standard BoM, set the **BoM Type** to **Manufacture this Product**.
Then, click **Add a Line** to specify the various components that make up the
production of the final product and their respective quantities. New
components can be created quickly through the BoM, or can be created
beforehand in Manufacturing ‣ Products ‣ Products ‣ Create. Finally, click
**Save** to finish creating the BoM.

![Set up a Bill of Materials.](../../../../_images/bom-form.png)

### Specify a bill of materials (BoM) for a product variant

BoMs can also be assigned to specific _Product Variants_ , with two setup
options available to choose from.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In order to assign <abbr title="Bills of Materials">BoMs</abbr> to product variants, the product’s variant
attributes must already be configured on the product form.</p>
</div>

The first method is to create one BoM per variant by creating a new BoM and
specifying the **Product Variant**. The second method is to create one master
BoM that contains all of the components, and specify which variant each
component applies to using the **Apply on Variants** column.

![Product Variants in the Bill of Materials.](../../../../_images/bom-
variants.png)

## Set up operations

Add an **Operation** to a BoM to specify instructions for production and
register time spent on an operation. To use this feature, first enable the
**Work Orders** feature in Manufacturing ‣ Configuration ‣ Settings ‣
Operations.

Then, when creating a new BoM, click on the **Operations** tab and click **Add
a line** to add a new operation. In the **Create Operations** box, give the
operation a name, specify the **Work Center** and duration settings. Like
components, Konvergo ERP gives the option to specify a product variant in the **Apply
on Variants** field so the operation only applies to that variant. Finally,
click **Save & Close**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Each operation is unique, as it is always exclusively linked to one <abbr title="Bill of Materials">BoM</abbr>. Operations can be reused when configuring a new <abbr title="Bill of Materials">BoM</abbr>,
with the <b>Copy Existing Operations</b> feature.</p>
</div> ![Copy Existing Operations
feature.](../../../../_images/copy-existing-operations.png)

## Add by-products to a bill of materials (BoM)

A _By-Product_ is a residual product that is created during production in
addition to the main product of a BoM. Unlike the primary product, there can
be more than one by-product on a BoM.

To add by-products to a BoM, first enable the **By-Products** feature in
Manufacturing ‣ Configuration ‣ Settings ‣ Operations.

Once the feature is enabled, you can add by-products to a BoM by clicking on
the **Operations** tab and clicking **Add a line**. Then, name the by-product
and indicate the **Quantity** and the **Unit of Measure**. If the BoM has
configured operations, specify exactly which operation the by-product is
produced from in the **Produced in Operation** field. Finally, click **Save**.

  *[BoMs]: Bills of Materials
  *[BoM]: Bill of Materials

