# Stratégies de rangement

Putaway is the process of routing products to appropriate storage locations
upon shipment arrival.

Konvergo ERP can accomplish this seamlessly using _putaway rules_ , which dictate how
products move through specified warehouse locations.

Upon shipment arrival, operations are generated based on putaway rules to
efficiently move products to specified locations, and ensure easy retrieval
for future delivery orders.

In warehouses that process specific kinds of products, putaway rules can also
prevent volatile substances from being stored in close proximity, by directing
them to different locations determined by the warehouse manager.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.youtube.com/watch?v=nCQMf6sj_w8">Konvergo ERP Tutorials: Putaway Rules</a></p>
</div>

## Configuration

To use putaway rules, navigate to Inventory app ‣ Configuration ‣ Settings,
and activate the **Multi-Step Routes** feature under the **Warehouse**
section. By doing so, the **Storage Locations** feature is also automatically
activated.

Finally, click **Save**.

![Activez les Routes en plusieurs étapes dans les paramètres de
l'Inventaire.](../../../../../_images/activate-multi-step-routes.png)

### Define putaway rule

To manage where specific products are routed for storage, navigate to
Inventory app ‣ Configuration ‣ Putaway Rules. Use the **Create** button to
configure a new putaway rule on a **Product** or **Product Category** that the
rule affects.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Putaway rules can be defined either per product/product category, and/or package type (the
<em>Packages</em> setting must be enabled in Inventory app ‣ Configuration ‣
Settings for that).</p>
</div>

In the same line, the **When product arrives in** location is where the
putaway rule is triggered to create an operation to move the product to the
**Store to** location.

For this to work, the **Store to** location must be a _sub-location_ of the
first (e.g., `WH/Stock/Fruits` is a specific, named location inside `WH/Stock`
to make the products stored here easier to find).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>In a warehouse location, <b>WH/Stock</b>, there are the following sub-locations:</p>
<ul>
<li><p>WH/Stock/Fruits</p></li>
<li><p>WH/Stock/Vegetables</p></li>
</ul>
<p>Ensure all apples are stored in the fruits section by filling the field <b>Store to</b> with
the location <code>WH/Stock/Fruits</code> when the <b>Product</b>, <code>Apple</code> arrives in <code>WH/Stock</code>.</p>
<p>Repeat this for all products and hit <b>Save</b>.</p>
<img alt="Create putaway rules for apples and carrots." class="align-center" src="../../../../../_images/create-putaway-rules.png"/>
</div>

### Putaway rule priority

Konvergo ERP selects a putaway rule based on the following priority list (from highest
to lowest) until a match is found:

  1. Package type and product

  2. Package type and product category

  3. Type de colis

  4. Produit

  5. Product category

<div class="alert alert-success">
<p class="alert-title">
Example</p><blockquote>
<div><p>The product <code>Lemonade can</code> has the following putaway rules configured:</p>
<ol class="arabic simple">
<li><p>When receiving a <code>Pallet</code> (<b>Package Type</b>) of <code>Lemonade cans</code>, it is redirected to
<code>WH/Stock/Pallets/PAL1</code>.</p></li>
<li><p><code>Lemonade can</code>’s <b>Product Category</b> is <code>All/drinks</code>, and when receiving a <code>Box</code> of
any item in this product category, items are redirected to <code>WH/Stock/Shelf 1</code>.</p></li>
<li><p>Any product on a <code>Pallet</code> is redirected to <code>WH/Stock/Pallets</code></p></li>
<li><p>The product <code>Lemonade can</code> is redirected to <code>WH/Stock/Shelf 2</code></p></li>
<li><p>Items in the <code>All/drinks</code> product category are redirected to <code>WH/Stock/Small Refrigerator</code>.</p></li>
</ol>
</div></blockquote>
<img alt="Quelques exemples de stratégies de rangement." class="align-center" src="../../../../../_images/putaway-example.png"/>
</div>

## Storage categories

A _storage category_ is an extra location attribute. Storage categories allow
the user to define the quantity of products that can be stored in the
location, and how the location will be selected with putaway rules.

### Configuration

To enable storage categories, go to Inventory app ‣ Configuration ‣ Settings,
and activate the **Storage Categories** feature in the **Warehouse** section.
Then, click **Save**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>Storage Locations</b> feature <b>must</b> be enabled to enable <b>Storage
Categories</b>.</p>
</div>

### Define storage category

To create a storage category, go to Inventory app ‣ Configuration ‣ Storage
Categories and click **Create**.

On the storage category form, type a name for the **Storage Category** field.

Options are available to limit the capacity by weight, by product, or by
package type. The **Allow New Product** field defines when the location is
considered available to store a product:

  * **Si l’emplacement est vide** : un produit peut être ajouté seulement si l’emplacement est vide.

  * **Si les produits sont identiques** : un produit peut être ajouté seulement si le même produit s’y trouve déjà.

  * **Autoriser les produits différents** : plusieurs produits différents peuvent être stockés dans cet emplacement en même temps.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Create putaway rules for pallet-stored items and ensure real-time storage capacity checks by
creating the <code>High Frequency pallets</code> storage category.</p>
<p>Name the <b>Storage Category</b>, and select <b>If all products are same</b> in the
<b>Allow New Product</b> field.</p>
<p>Then, define package capacity in the <b>Capacity by Package</b> tab, specifying the number
of packages for the designated <b>Package Type</b> and setting a maximum of <code>2.00</code> <code>Pallets</code>
for a specific location.</p>
<img alt="Create a storage category on the page." class="align-center" src="../../../../../_images/storage-category.png"/>
</div>

Une fois les paramètres de la catégorie d’emplacement enregistrés, la
catégorie d’emplacement peut être liée à un emplacement.

To do that, navigate to the location by going to Inventory app ‣ Configuration
‣ Locations, and select the location. Click **Edit** and select the created
category in the **Storage Category** field.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Assign the <code>High Frequency pallets</code> storage category to the <code>WH/Stock/pallets/PAL 1</code>
sub-location.</p>
<img alt="Lors de la création d'une catégorie d'emplacement, elle peut être liée à un entrepôt." class="align-center" src="../../../../../_images/location-storage-category.png"/>
</div>

### Catégories d’emplacement dans les stratégies de rangement

To continue the example from above, apply the `High Frequency Pallets` on the
`PAL1` and `PAL2` locations and rework the putaway rules as follows:

Supposons qu’une palette de canettes de limonade a été reçue :

  * Si PAL1 et PAL2 sont vides, la palette sera redirigée vers WH/Stock/Palettes/PAL1.

  * Si PAL1 est plein, la palette sera redirigée vers WH/Stock/Palettes/PAL2.

  * Si PAL1 et 2 sont pleins, la palette sera redirigée vers WH/Stock/Palettes.

![Les catégories d'emplacement utilisées dans une variété de stratégies de
rangement.](../../../../../_images/smart-putaways.png)

