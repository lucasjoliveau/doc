# Manufacturing product configuration

In order to manufacture a product in Konvergo ERP _Manufacturing_ , the product must
be properly configured. Doing so consists of enabling the _Manufacturing_
route and configuring a bill of materials (BoM) for the product. Once these
steps are completed, the product is selectable when creating a new
manufacturing order.

## Activate the Manufacture route

The Manufacture route is activated for each product on its own product page.
To do so, begin by navigating to Manufacturing ‣ Products ‣ Products. Then,
select an existing product, or create a new one by clicking **New**.

On the product page, select the **Inventory** tab, then enable the
**Manufacture** checkbox in the **Routes** section. This tells Konvergo ERP the
product can be manufactured.

![The Manufacturing route on the Inventory tab of a product
page.](../../../../_images/manufacturing-route.png)

## Configure a bill of materials (BoM)

Next, a BoM must be configured for the product so Konvergo ERP knows how it is
manufactured. A BoM is a list of the components and operations required to
manufacture a product.

To create a BoM for a specific product, navigate to Manufacturing ‣ Products ‣
Products, then select the product. On the product page, click the **Bill of
Materials** smart button at the top of the page, then select **New** to
configure a new BoM.

![The Bill of Materials smart button on a product
page.](../../../../_images/bom-smart-button1.png)

On the BoM, the **Product** field auto-populates with the product. In the
**Quantity** field, specify the number of units that the BoM produces.

Add a component to the BoM by selecting the **Components** tab and clicking
**Add a line**. Select a component from the **Component** drop-down menu, then
enter the quantity in the **Quantity** field. Continue adding components on
new lines until all components have been added.

![The Components tab on a bill of materials.](../../../../_images/components-
tab.png)

Next, select the **Operations** tab. Click **Add a line** and a **Create
Operations** pop-up window appears. In the **Operation** field, specify the
name of the operation being added (e.g. Assemble, Cut, etc.). Select the work
center where the operation will be carried out from the **Work Center** drop-
down menu. Finally, click **Save & Close** to finish adding operations, or
**Save & New** to add more.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>Operations</b> tab only appears if the <b>Work Orders</b> setting is enabled. To
do so, navigate to Manufacturing ‣ Configuration ‣ Settings, then enable the
<b>Work Orders</b> checkbox.</p>
</div> ![The Operations tab on a bill of
materials.](../../../../_images/operations-tab1.png) <div class="admonition-learn-more alert">
<p class="alert-title">
Learn more</p><p>The section above provides instructions for creating a basic <abbr title="Bill of Materials">BoM</abbr> that allows a product to be
manufactured in Konvergo ERP. However, it is by no means an exhaustive summary of all the options
available when configuring a <abbr title="Bill of Materials">BoM</abbr>. For more information about bills of materials, see the
documentation on how to <a href="bill_configuration#manufacturing-management-bill-configuration"><span class="std std-ref">create a bill of materials</span></a>.</p>
</div>

  *[BoM]: Bill of Materials

