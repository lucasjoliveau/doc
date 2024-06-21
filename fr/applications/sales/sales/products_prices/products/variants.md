# Variantes de produit

Les variantes de produits sont utilisées pour donner à un seul produit une
variété de caractéristiques ou d’options différentes parmi lesquelles les
clients peuvent choisir, telles que la taille, le style ou la couleur.

Les variantes de produits peuvent être gérées via leur modèle de produit
individuel ou en allant aux **Variantes de produits** ou aux **Attributs**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>An apparel company has the following variant breakdown for one their best-selling t-shirts:</p>
<ul>
<li><p>Unisex Classic Tee</p>
<ul>
<li><p>Couleur : bleu, rouge, blanc, noir</p></li>
<li><p>Taille : S, M, L, XL, XXL</p></li>
</ul>
</li>
</ul>
<p>Here, the <b>T-shirt</b> is the product template, and <b>T-shirt: Blue, S</b> is a specific product
variant.</p>
<p><b>Color</b> and <b>Size</b> are <em>attributes</em>, and the corresponding options (like <b>Blue</b> and <b>S</b>)
are <em>values</em>.</p>
<p>In this instance, there is a total of twenty different product variants: four <b>Color</b> options
multiplied by five <b>Size</b> options. Each variant has its own inventory count, sales totals, and
other similar records in Konvergo ERP.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>

## Configuration

To use product variants, the _Variants_ setting **must** be activated in the
Konvergo ERP _Sales_ application.

To do that, go to Sales app ‣ Configuration ‣ Settings, and locate the
**Product Catalog** section at the top of the page.

In that section, check the box to enable the **Variants** feature.

![Activating product variants on the Settings page of the Konvergo ERP Sales
application.](../../../../../_images/activating-variants-setting.png)

Then, click **Save** at the top of the **Settings** page.

## Attributs

Before product variants can be set up, attributes **must** be created. To
create, manage, and modify attributes, navigate to Sales app ‣ Configuration ‣
Attributes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’ordre des attributs sur la page <b>Attributs</b> détermine la façon dont ils apparaissent sur les pages <b>Configurateur de produts</b>, le tableau de bord du <b>Point de Vente</b> et <b>eCommerce</b>.</p>
</div>

To create a new attribute from the **Attributes** page, click **New**. Doing
so reveals a blank attributes form that can be customized and configured in a
number of ways.

![A blank attribute creation form in the Konvergo ERP Sales
application.](../../../../../_images/attribute-creation.png)

First, create an **Attribute Name** , such as `Color` or `Size`.

Next, in the optional **Category** field, select a category from a drop-down
menu to group similar attributes under the same section for added specificity
and organization.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To view the details related to the attribute category selected, click the internal link
<b>➡️ (arrow)</b> icon to the far-right of the <b>Category</b> field. Doing so reveals
that attribute category’s detail form.</p>
<img alt="A standard attribute category detail page accessible via its internal link arrow icon." class="align-center" src="../../../../../_images/attribute-category-internal-link.png"/>
<p>Here, the <b>Category Name</b> and <b>Sequence</b> is displayed at the top. Followed by
<b>Related Attributes</b> associated with the category. These attributes can be
dragged-and-dropped into a desirable order of priority.</p>
<p>Attributes can be directly added to the category, as well, by clicking <b>Add a line</b>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>To create an attribute category directly from this field, start typing the name of the new
category, then select either <b>Create</b> or <b>Create and edit…</b> from the
drop-down menu that appears.</p>
<p>Clicking <b>Create</b> creates the category, which can be modified later. Clicking
<b>Create and edit…</b> creates the category and reveals a <b>Create Category</b>
pop-up window, in which the new attribute category can be configured and customized.</p>
</div>

Beneath the **Category** field are the **Display Type** options. The **Display
Type** determines how this product is shown on the online store, **Point of
Sale** dashboard, and **Product Configurator**.

The **Display Type** options are:

  * **Radio** : options appear in a bullet-style list on the product page of the online store.

  * **Pills** : options appear as selectable buttons on the product page of the online store.

  * **Select** : options appear in a drop-down menu on the product page of the online store.

  * **Color** : options appear as small, colored squares, which reflect any HTML color codes set, on the product page of the online store.

![Display Types on Product Configurator on the online store in
Konvergo ERP.](../../../../../_images/display-types.png)

The **Variants Creation Mode** field informs Konvergo ERP when to automatically create
a new variant once an attribute is added to a product.

  * **Instantanément** : crée toutes les variantes possibles dès que les attributs et les valeurs sont ajoutés à un modèle de produit.

  * **Dynamically** : creates variants **only** when corresponding attributes and values are added to a sales order.

  * **Never (option)** : never automatically creates variants.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Une fois ajouté à un produit, le <b>mode de création de variantes</b> d’un attribut ne peut être modifié.</p>
</div>

Lastly, the **eCommerce Filter Visibility** field determines whether these
attribute options are visible to the customer on the front-end, as they shop
on the online store.

  * **Visible** : the attribute values are visible to customers on the front-end.

  * **Hidden** : the attribute values are hidden from customers on the front-end.

### Attribute values

Attribute values should be added to the **Attribute Values** tab. Values can
be added to an attribute at any time, if needed.

To add a value, click **Add a line** in the **Attribute Values** tab.

Then, enter the name of the value in the **Value** column. Next, check the box
in the **Is custom value** column, if the value is custom (i.e. the customer
gets to provide unique specifications that are specific to this particular
value).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the <b>Display Type</b> - <b>Color</b> option is selected, the option to add an HTML
color code will appear to the far-right of the value line, to make it easier for salespeople and
customers to know exactly what color option they’re choosing.</p>
<img alt="Attribute values tab when add a line is clicked, showing the custom columns." class="align-center" src="../../../../../_images/attribute-value-add-a-line.png"/>
<p>To choose a color, click the blank circle in the <b>Color</b> column, which reveals an HTML
color selector pop-up window.</p>
<img alt="Selecting a color from the HTML color pop-up window that appears on attribute form." class="align-center" src="../../../../../_images/picking-a-color.png"/>
<p>In this pop-up window, select a specific color by dragging the color slider to a particular hue,
and clicking on the color portion directly on the color gradient window.</p>
<p>Or, choose a specific color by clicking the <em>dropper</em> icon, and selecting a desired color that’s
currently clickable on the screen.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez également créer des attributs directement à partir du modèle de produit en ajoutant une nouvelle ligne et en tapant le nom dans l’onglet <b>Variantes</b>.</p>
</div>

Once an attribute is added to a product, that product is listed and
accessible, via the attribute’s **Related Products** smart button. That button
lists every product in the database currently using that attribute.

## Variantes de produit

Once an attribute is created, use the attribute (and its values) to create a
product variant. To do that, go to Sales app ‣ Products ‣ Products, and select
an existing product to view that desired product’s form. Or, click **Create**
to create a new product, to which a product variant can be added.

On the product form, click the **Attributes & Variants** tab to view, manage,
and modify attributes and values for the product.

![The attributes and values tab on a typical product form in Konvergo ERP
Sales.](../../../../../_images/attributes-values-tab.png)

To add an attribute to a product, and subsequent attribute values, click **Add
a line** in the **Attributes & Variants** tab. Then, choose the desired
attribute from the drop-down menu that appears.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Attributes can be created directly from the <b>Attributes &amp; Variants</b> tab of a product
form. To do that, start typing the name of the new attribute in the blank field, and select
either <b>Create</b> or <b>Create and edit…</b> from the mini drop-down menu that
appears.</p>
<p>Clicking <b>Create</b> creates the attribute, which can be customized later. Clicking
<b>Create and edit…</b> creates the attribute, and a <b>Create Attribute</b> pop-up
form appears. In the pop-up form, proceed to modify the attribute in a number of ways.</p>
</div>

Once an attribute is selected in the **Attribute** column, proceed to select
the specific attribute values to apply to the product, via the drop-down menu
available in the **Values** column.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>There is no limit to how many values can be added.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>0

### Configure variants

To the far-right of the attribute line is a **Configure** button. When
clicked, Konvergo ERP reveals a separate page showcasing those specific **Product
Variant Values**.

![The Product Variant Values page accessible via the Configure button on a
product form.](../../../../../_images/product-variant-values.png)

Here, the specific **Value** name, **HTML Color Index** (if applicable), and
**Value Price Extra** are viewable.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>1

When a value is clicked on the **Product Variant Values** page, Konvergo ERP reveals a
separate page, detailing that value’s related details.

![A Product Variant Values page accessible via the Product Variants Values
general page.](../../../../../_images/product-variant-value-page.png)

On the specific product variant detail page, the **Value** and **Value Price
Extra** fields can be found, along with an **Exclude for** field.

In the **Exclude for** field, different **Product Templates** and specific
**Attribute Values** can be added. When added, this specific attribute value
will be excluded from those specific products.

### Variants smart button

When a product has attributes and variants configured in its **Attributes &
Variants** tab, a **Variants** smart button appears at the top of the product
form. The **Variants** smart button indicates how many variants are currently
configured for that specific product.

![The variants smart button at the top of the product form in Konvergo ERP
Sales.](../../../../../_images/variants-smart-button.png)

When the **Variants** smart button is clicked, Konvergo ERP reveals a separate page
showcasing all the specific product variant combinations configured for that
specific product.

![The variants page accessible via the variants smart button on the product
form in Konvergo ERP.](../../../../../_images/variants-page.png)

## Impact des variantes

In addition to offering more detailed product options to customers, product
variants have their own impacts that can be taken advantage of throughout the
Konvergo ERP database.

  * **Barcode** : barcodes are associated with each variant, instead of the product template. Each individual variant can have its own unique barcode/SKU.

  * **Price** : every product variant has its own public price, which is the sum of the product template price _and_ any extra charges for particular attributes.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>2

  * **Inventaire** : L’inventaire est compté pour chaque variante de produit individuelle. Sur le formulaire du modèle de produit, l’inventaire reflète la somme de toutes les variantes, mais l’inventaire réel est calculé par variante individuelle.

  * **Image** : Chaque variante de produit peut avoir sa propre image spécifique.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>3 <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de produit</a></p>
</div>4

