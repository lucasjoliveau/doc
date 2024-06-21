# Règles de réapprovisionnement

Les règles de réapprovisionnement sont utilisées pour maintenir les niveaux de
stock prévus au-dessus d’un certain seuil, sans dépasser un plafond défini.
Pour ce faire, elles précisent une quantité minimale que le stock ne doit pas
dépasser et une quantité maximale qu’il ne doit pas dépasser.

Vous pouvez configurer les règles de réapprovisionnement pour chaque produit
en fonction de la route utilisée pour le réapprovisionner. Si un produit
utilise la route _Acheter_ , une demande de prix est créée lorsque la règle de
réapprovisionnement est déclenchée. Si un produit utilise la route _Fabriquer_
, un ordre de fabrication (OF) est créé à la place. Il en est ainsi quelle que
soit la route de réassort sélectionnée.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=XEJZrCjoXaU">Konvergo ERP Tutorials: Automatic Reordering Rules</a></p></li>
<li><p><a href="https://www.youtube.com/watch?v=deIREJ1FFj4">Konvergo ERP Tutorials: Manual Reordering Rules</a></p></li>
</ul>
</div>

## Configurer les produits pour les règles de réapprovisionnement

In order to use reordering rules for a product, it must first be correctly
configured. Begin by navigating to Inventory app ‣ Products ‣ Products, then
select an existing product, or create a new one by clicking **New**.

On the product form, under the **General Information** tab, make sure that the
**Product Type** is set to **Storable Product**. This is necessary because
Konvergo ERP only tracks stock quantities for storable products, and this number is
used to trigger reordering rules.

![Définissez le type de produit sur
stockable.](../../../../../_images/product-type.png)

Ensuite, cliquez sur l’onglet **Inventaire** et sélectionnez une ou plusieurs
routes dans la section **Routes**. Cela indique à Konvergo ERP quelle route utiliser
pour réapprovisionner le produit.

![Sélectionnez une ou plusieurs routes dans l'onglet
Inventaire.](../../../../../_images/select-routes1.png)

Si le produit est réapprovisionné à l’aide de la route **Acheter** , confirmez
que la case **Peut être acheté** est cochée sous le nom du produit. Ceci fait
apparaître l’onglet **Achats**. Cliquez sur l’onglet **Achats** et spécifiez
au moins un fournisseur et le prix auquel il vend le produit, pour qu’Konvergo ERP
sache auprès de quelle entreprise le produit doit être acheté.

![Précisez un fournisseur et un prix dans l'onglet
Achats.](../../../../../_images/specify-vendor1.png)

Si le produit est réapprovisionné à l’aide de la route **Fabriquer** , il doit
avoir au moins une nomenclature associée. C’est nécessaire parce qu’Konvergo ERP crée
uniquement des ordres de fabrication pour les produits ayant une nomenclature.

If a BoM does not already exist for the product, select the **Bill of
Materials** smart button at the top of the product form, then click **New** to
configure a new BoM.

![Le bouton intelligent Nomenclature sur une fiche de
produit.](../../../../../_images/bom-smart-button.png)

## Créer de nouvelles règles de réapprovisionnement

To create a new reordering rule, navigate to Inventory app ‣ Configuration ‣
Reordering Rules, then click **New** , and fill out the new line as follows:

  * **Produit** : Le produit qui est réapprovisionné par la règle.

  * **Emplacement** : L’emplacement où le produit est stocké.

  * **Quantité min** : La quantité minimale qui peut être prévue sans que la règle ne soit déclenchée. Lorsque le stock prévu est inférieur à cette quantité, un ordre de réapprovisionnement est créé pour ce produit.

  * **Quantité max** : La quantité maximale jusqu’à laquelle le stock est réapprovisionné.

  * **Quantité multiple** : Précisez si le produit doit être réapprovisionné par lots d’une certaine quantité (par ex. un produit peut être réapprovisionné par lots de 20).

  * **UdM** : L’unité de mesure utilisée pour réapprovisionner le produit. Cette valeur peut être simplement `Unités` ou une unité de mesure spécifique pour le poids, la longueur, etc.

![Le formulaire de création d'une nouvelle règle de
réapprovisionnement.](../../../../../_images/reordering-rule-form.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Reordering rules can also be created from each product form. To do so, navigate to
Inventory app ‣ Products ‣ Products, then select a product. Click on
Reordering Rules smart button ‣ New, then fill out the new line, as detailed
above.</p>
</div>

For advanced usage of reordering rules, learn about the following reordering
rule fields:

  * Trigger

  * Visibility days

  * Preferred route

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The fields above are not available by default, and must be enabled by selecting the
<b>(slider)</b> icon in the far-right corner, and selecting the desired column from the
drop-down menu.</p>
</div>

## Déclencher

When stock falls below the reordering rule’s minimum, set the reordering
rule’s _trigger_ to _automatic_ to automatically create purchase or
manufacturing orders to replenish stock.

Alternatively, setting the reordering rule’s trigger to _manual_ displays the
product and forecasted stock on the _replenishment dashboard_ , where the
procurement manager can review the stock levels, lead times, and forecasted
dates of arrival.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="strategies">Sélectionner une stratégie de réassort</a></p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>The <b>Replenishment</b> dashboard is accessible by going to Inventory app
‣ Operations ‣ Replenishment.</p>
</div>

To enable the **Trigger** field, go to Inventory app ‣ Configuration ‣
Reordering Rules. Then, click the **(slider)** icon, located to the far-right
of the column titles, and enable the **Trigger** option from the additional
options drop-down menu that appears.

![Enable the Trigger field by toggling it in the additional options
menu.](../../../../../_images/enable-trigger.png)

In the **Trigger** column, select **Auto** or **Manual**. Refer to the
sections below to learn about the different types of reordering rules.

### Automatique

Automatic reordering rules, enabled by setting the reordering rule’s
**Trigger** field to **Auto** , generate purchase or manufacturing orders
when:

  1. the scheduler runs, and the _On Hand_ quantity is below the minimum

  2. a sales order is confirmed, and lowers the _Forecasted_ quantity of the product below the minimum

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>The scheduler is set to run once a day, by default.</p>
<p>To manually trigger a reordering rule before the scheduler runs, ensure <a href="../../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> is enabled, and then select Inventory app ‣ Operations ‣
Run Scheduler. Then, select the green <b>Run Scheduler</b> button on the pop-up window that
appears.</p>
<p>Be aware that this also triggers <em>any other</em> scheduled actions.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>The product, <code>Office Lamp</code>, has an automatic reordering rule set to trigger when the forecasted
quantity falls below the <b>Min Quantity</b> of <code>5.00</code>. Since the current
<b>Forecast</b> is <code>55.00</code>, the reordering rule is <b>not</b> triggered.</p>
<img alt="Show automatic reordering rule from the Reordering Rule page." class="align-center" src="../../../../../_images/auto.png"/>
</div>

If the **Buy** route is selected, then an RFQ is generated. To view and manage
RFQs, navigate to Purchase app ‣ Orders ‣ Requests for Quotation.

If the **Manufacture** route is selected, then an MO is generated. To view and
manage MOs, navigate to Manufacturing app ‣ Operations ‣ Manufacturing Orders.

When no route is selected, Konvergo ERP selects the **Route** specified in the
**Inventory** tab of the product form.

### Manuelle

Manual reordering rules, configured by setting the reordering rule’s
**Trigger** field to **Manual** , list a product on the replenishment
dashboard when the forecasted quantity falls below a specified minimum.
Products on this dashboard are called _needs_ , because they are needed to
fulfill upcoming sales orders, for which the forecasted quantity is not
enough.

The replenishment dashboard, accessible by navigating to Inventory app ‣
Operations ‣ Replenishment, considers sales order deadlines, forecasted stock
levels, and vendor lead times. It displays needs **only** when it is time to
reorder items.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the one-day window for ordering products is too short, skip to the <a href="#inventory-product-management-visibility-days"><span class="std std-ref">visibility days</span></a> section to make the need appear on the
replenishment dashboard a specified number of days in advance.</p>
</div> ![Click the Order Once button on the replenishment
dashboard to replenish stock.](../../../../../_images/manual.png)

## Visibility days

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Ensure <a href="../../shipping_receiving/advanced_operations_shipping/scheduled_dates">lead times</a>
are understood before proceeding with this section.</p>
</div>

When manual reordering rules are assigned to a product, _visibility days_ make
the product appear on the replenishment dashboard (Inventory app ‣ Operations
‣ Replenishment) a certain number of days in advance.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A product has a manual reordering rule set to trigger when the stock level falls below four
units. The current on-hand quantity is ten units.</p>
<p>The current date is February twentieth, and the <em>delivery date</em> on a sales order (in the
<b>Other Info</b> tab) is March third — twelve days from the current date.</p>
<p>The <a href="../../shipping_receiving/advanced_operations_shipping/scheduled_dates#inventory-management-purchase-lt"><span class="std std-ref">vendor lead time</span></a> is four days, and the
<a href="../../shipping_receiving/advanced_operations_shipping/scheduled_dates#inventory-management-purchase-security-lt"><span class="std std-ref">purchase security lead time</span></a> is one day.</p>
<p>When the <b>Visibility Days</b> field of the reordering rule is set to zero, the product
appears on the replenishment dashboard five days before the delivery date, which, in this case,
is February twenty-seventh.</p>
<img alt="Graphic representing when the need appears on the replenishment dashboard: Feb 27." class="align-center" src="../../../../../_images/need-dates.png"/>
<p>To see the product on the replenishment dashboard for the current date, February twentieth, set
the <b>Visibility Days</b> to <code>7.00</code>.</p>
</div>

To determine the number of visibility days needed to see a product on the
replenishment dashboard, subtract _today’s date_ from the _date the need
appears_ on the replenishment dashboard.

\\[Visibility~days = Need~appears~date - Today's~date\\]

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Reordering rules can also be created from each product form. To do so, navigate to
Inventory app ‣ Products ‣ Products, then select a product. Click on
Reordering Rules smart button ‣ New, then fill out the new line, as detailed
above.</p>
</div>0

## Route préférée

Konvergo ERP permet de sélectionner plusieurs routes dans l’onglet **Inventaire** de
chaque fiche produit. Par exemple, il est possible de sélectionner à la fois
**Acheter** et **Fabriquer** , permettant ainsi l’exécution des deux routes.

Konvergo ERP also enables users to set a preferred route for a product’s reordering
rule. This is the route that the rule defaults to if multiple are selected. To
select a preferred route, begin by navigating to Inventory app ‣ Configuration
‣ Reordering Rules or Inventory app ‣ Operations ‣ Replenishment.

Click inside of the column on the row of a reordering rule, and a drop-down
menu shows all available routes for that rule. Select one to set it as the
preferred route.

![Sélectionnez une route préférée dans le menu
déroulant.](../../../../../_images/select-preferred-route.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Reordering rules can also be created from each product form. To do so, navigate to
Inventory app ‣ Products ‣ Products, then select a product. Click on
Reordering Rules smart button ‣ New, then fill out the new line, as detailed
above.</p>
</div>1

  *[BoM]: Bill of Materials
  *[RFQ]: Request for Quotation
  *[RFQs]: Requests for Quotation
  *[MO]: Manufacturing Order
  *[MOs]: Manufacturing Orders

