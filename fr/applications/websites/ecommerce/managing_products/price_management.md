# Gestion des prix

Konvergo ERP propose de multiples options pour sélectionner le prix affiché sur votre
site web, ainsi que des prix spécifiques en fonction de critères définis.

## Taxes

### Configuration des taxes

Pour ajouter une taxe sur un produit, vous pouvez soit définir une taxe dans
le champ **Taxes clients** du **modèle de produit** , soit utiliser des
[positions fiscales](../../../finance/accounting/taxes/fiscal_positions).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../finance/accounting/taxes">Taxes</a></p></li>
<li><p><a href="../../../finance/accounting/taxes/avatax">AvaTax integration</a></p></li>
<li><p><a href="../../../finance/accounting/taxes/taxcloud">Intégration TaxCloud</a></p></li>
<li><p><a href="../../../finance/accounting/taxes/fiscal_positions">Positions fiscales (correspondances de taxes et de comptes)</a></p></li>
</ul>
</div>

### Affichage des taxes

Le choix de la taxe sur le prix affiché dépend de la réglementation d’un pays
ou du type de clients **(B2B ou B2C)**. Pour sélectionner le type de prix
affiché, allez à Site Web ‣ Configuration ‣ Paramètres, descendez jusqu’à la
section **Boutique - Produits** et sélectionnez **Hors taxes** ou **Toutes
taxes comprises**.

  * **Hors taxes** : le prix affiché sur le site web s’entend **hors taxes** , et la taxe est calculée à l’étape de la vérification de votre panier ;

  * **Toutes taxes comprises** : le prix affiché sur le site web s’entend **toutes taxes comprises**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ce paramètre est <b>global</b> et le type d’affichage des taxes est le même pour tous vos sites web. Il n’est donc pas possible de sélectionner des affichages des taxes différents pour des sites web différents. Il peut s’agir d’un point important à prendre en considération lors de la mise en œuvre d’une base de données comportant plusieurs sites d’eCommerce destinés à différents types de clients (c’est-à-dire B2B et B2C).</p>
</div>

Vous pouvez choisir d’afficher le type de prix à côté du prix en allant à Site
Web ‣ Site ‣ Page d’accueil ‣ Boutique, en sélectionnant un produit et ensuite
en allant à Modifier ‣ Personnaliser et en activant **Indication taxes**.

![Type de taxe affiché sur la page produit](../../../../_images/price-tax-
display-type.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/accounting/taxes/B2B_B2C">Prix B2B (hors taxes) et B2C (toutes taxes comprises)</a></p>
</div>

## Prix à l’unité

Il est possible d’afficher un [prix à
l’unité](../../../inventory_and_mrp/inventory/product_management/product_replenishment/uom)
sur la page produit. Pour ce faire, allez à Site Web ‣ Configuration ‣
Paramètres et activez **Prix de référence du produit** dans la section
**Boutique - Produits**. Une fois l’option activée, veillez à ce qu’un montant
soit défini dans le champ **Nombre d’unités de base** du **modèle du produit**
et dans le champ **Prix de vente**.

![Prix à l'unité sur le modèle du produit](../../../../_images/price-cost-per-
unit.png)

Le prix par unité de mesure se trouve au-dessus du bouton **Ajouter au
panier** sur la page produit.

![Prix à l'unité sur la page produit](../../../../_images/price-cost-per-unit-
page.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Attention, la mention du prix à l’unité peut être <b>obligatoire</b> dans certains pays.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/inventory/product_management/product_replenishment/uom">Unités de mesure</a></p>
</div>

### Configuration des prix : listes de prix

Les listes de prix sont l’outil principal pour gérer les prix dans votre
eCommerce. Elles vous permettent de définir des prix spécifiques au site web -
différents du prix affiché sur le modèle du produit - en fonction du **groupe
de pays** , de la **devise** , de la **quantité minimale** , de la **période**
, ou de la **variante**. Vous pouvez créer autant de listes de prix que
nécessaire, mais il est obligatoire d’avoir au moins une liste de prix
configurée par site web. Si aucune liste de prix personnalisée n’est ajoutée,
la **liste de prix publique** sera utilisée par défaut sur tous les sites web.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../sales/sales/products_prices/prices/pricing">Listes de prix, remises et formules</a></p>
</div>

#### Configuration

Les listes de prix se trouvent dans Site web ‣ eCommerce ‣ Listes de prix,
mais elles doivent d’abord être activées. Pour ce faire, allez à Site Web ‣
Configuration ‣ Paramètres et descendez jusqu’à la section **Boutique -
Produits**. Vous y trouverez deux options :

  * **Plusieurs prix par produit** ;

  * **Règles de prix avancées (remises, formules)**.

La **première** option vous permet de définir des prix différentes par
_segment_ de client, c’est-à-dire des clients enregistrés, des clients VIP,
des clients réguliers, etc. La **deuxième** option vous permet de définir des
règles de _modification des prix_ , telles que les **remises** , **marges** ,
**arrondis** , etc.

#### Devise étrangère

Si vous vendez dans **plusieurs devises** et si vous avez des listes de prix
en devises étrangères, les clients peuvent sélectionner leur liste de prix
correspondante n’importe où sur la page de la **boutique** dans le menu
déroulant à côté de la **barre de recherche**.

![Sélection des listes de prix](../../../../_images/price-pricelists.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../sales/sales/products_prices/prices/pricing">Listes de prix, remises et formules</a></p></li>
<li><p><a href="../../../sales/sales/products_prices/prices/currencies">Devises étrangères</a></p></li>
</ul>
</div>

### Remise permanente

Si vous avez réduit de façon permanente le prix d’un produit, un moyen
populaire d’attirer l’attention des clients est la stratégie du **barré**. La
stratégie consiste à afficher le prix précédent barré et le **nouveau produit
réduit** à côté.

![Prix barré](../../../../_images/price-strikethrough.png)

Pour afficher un prix “barré”, activez l’option **Comparaison de prix** sous
Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Produits. Ensuite, allez au
modèle du produit (Site Web ‣ eCommerce ‣ Produits), et dans le champ
**Comparer au prix** , saisissez le **nouveau** prix.

