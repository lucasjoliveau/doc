# Configuration de la valorisation des stocks

Tous les stocks disponibles d’une entreprise contribuent à la valorisation de
son inventaire. Cette valeur doit être reflétée dans les documents comptables
de l’entreprise afin de montrer avec précision la valeur de l’entreprise et de
tous ses actifs.

Par défaut, Konvergo ERP utilise une valorisation périodique des stocks (également
connue sous le nom de valorisation manuelle des stocks). Cette méthode
implique que l’équipe comptable enregistre des pièces comptables basées sur
l’inventaire physique de l’entreprise et que les employés de l’entrepôt
prennent le temps de compter l’inventaire. Dans Konvergo ERP, cette méthode est
reflétée dans chaque catégorie de produit, où le champ **Méthode de coût**
sera défini sur `Prix standard` par défaut et le champ **Valorisation des
stocks** sera défini sur `Manuelle`.

![Les champs de valorisation des stocks sont situés sur la fiche de la
catégorie de produit.](../../../../../_images/inventory-valuation-fields.png)

Par ailleurs, la valorisation automatisée des stocks est une méthode de
valorisation intégrée qui met à jour la valeur de l’inventaire en temps réel
en créant des pièces comptables chaque fois qu’un mouvement de stock est
initié entre des emplacements dans l’inventaire d’une entreprise.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La valorisation automatisée des stocks est une méthode recommandée pour les experts-comptables, vu les étapes supplémentaires impliqués dans la configuration d’une pièce comptable. Même après la configuration initiale, la méthode sera vérifiée périodiquement pour s’assurer de son exactitude et des ajustements peuvent être nécessaires en permanence en fonction des besoins et des priorités de l’entreprise.</p>
</div>

## Types de comptabilité

Les pièces comptables dépendent du mode de comptabilité : _continentale_ ou
_anglo-saxonne_

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Verify the accounting mode by activating the <a href="../../../../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode (debug mode)</span></a> and navigating to
Accounting app ‣ Configuration ‣ Settings.</p>
<p>Then, in the search bar, look for <b>Anglo-Saxon Accounting</b>, to see if the feature is
enabled. If it is <b>not</b> enabled, Continental accounting mode is in use.</p>
<img alt="Show the Anglo-Saxon accounting mode feature." class="align-center" src="../../../../../_images/anglo-saxon.png"/>
</div>

In _Anglo-Saxon_ accounting, the costs of goods sold (COGS) are reported when
products are sold or delivered. This means that the cost of a good is only
recorded as an expense when a customer is invoiced for a product. So for
**manual** valuation method, set the **Expense Account** to `Stock Valuation`
for the current asset type; for **automatic** valuation method, set the the
**Expense Account** to an _Expenses_ or a _Cost of Revenue_ type (e.g. `Cost
of Production`, `Cost of Goods Sold`, etc.).

In _Continental_ accounting, the cost of a good is reported as soon as a
product is received into stock. Because of this, the **Expense Account** can
be set to **either** _Expenses_ or a _Cost of Revenue_ type, however, it is
more commonly set to an _Expenses_ account.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="#inventory-management-config-inventory-valuation"><span class="std std-ref">Details about configuring Expense and Stock accounts</span></a></p>
</div>

## Configuration

Make changes to inventory valuation options by navigating to Inventory app ‣
Configuration ‣ Product Categories. In the **Inventory Valuation** section,
select the desired **Costing Method** and **Inventory Valuation** options.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est possible d’utiliser des paramètres de valorisation différents pour différentes catégories de produits.</p>
</div> ![Show inventory valuation configuration
options.](../../../../../_images/config-inventory-valuation.png)

### Costing method

From the product category’s configuration page, choose the desired **Costing
Method** :

  * **Standard Price** : the default costing method in Konvergo ERP. The cost of the product is manually defined on the product form, and this cost is used to compute the valuation. Even if the purchase price on a purchase order differs, the valuation will still use the cost defined on the product form.

  * **Average Cost (AVCO)** : calculates the valuation of a product based on the average cost of that product, divided by the total number of available stock on-hand. With this costing method, inventory valuation is _dynamic_ , and constantly adjusts based on the purchase price of products.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous choisissez <b>Coût moyen (AVCO)</b> comme <b>Méthode de coût</b>, la modification de la valeur numérique dans le champ <b>Coût</b> pour les produits de la catégorie de produits respective crée un nouvel enregistrement dans le rapport de <em>Valorisation des stocks</em> pour ajuster la valeur du produit. Le montant du <b>Coût</b> sera automatiquement mis à jour en fonction du prix d’achat moyen du stock disponible et des coûts accumulés à partir des bons de commande validés.</p>
</div>

  * **First In First Out (FIFO)** : tracks the costs of incoming and outgoing items in real-time and uses the real price of the products to change the valuation. The oldest purchase price is used as the cost for the next good sold until an entire lot of that product is sold. When the next inventory lot moves up in the queue, an updated product cost is used based on the valuation of that specific lot. This method is arguably the most accurate inventory valuation method for a variety of reasons, however, it is highly sensitive to input data and human error.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Changing the costing method greatly impacts inventory valuation. It is highly recommended to
consult an accountant first before making any adjustments here.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="using_inventory_valuation">Utiliser la valorisation des stocks</a></p>
</div>

Quand la **Méthode de coût** est modifiée, la valeur des produits déjà en
stock qui utilisaient la méthode de coût **Standard** ne changera **pas** ; Au
contraire, les unités existantes conservent leur valeur et tout mouvement de
produit à partir de ce moment affecte le coût moyen. Si la valeur dans le
champ **Coût** sur une fiche produit est modifiée manuellement, Konvergo ERP génère un
enregistrement correspondant dans le rapport _Valorisation des stocks_.

### Valorisation des stocks

Inventory valuation in Konvergo ERP can be set to be updated manually or
automatically. While _Expense_ accounts apply to both, the _Stock Input_ and
_Stock Output_ accounts are only used for automated valuation.

Refer to the Expense and Stock input/output sections for details on
configuring each account type.

#### Compte de charges

To configure the _expense account_ , go to the **Account Properties** section
of the intended product category (Inventory app ‣ Configuration ‣ Product
Categories). Then, choose an existing account from the **Expense Account**
drop-down menu.

To ensure the chosen account is the correct **Type,** click the __**(right
arrow)** icon to the right of the account. Then, set the account type based on
the information below.

Anglo-SaxonContinental

AutomatedManual

In Anglo-Saxon accounting for automated inventory valuation, set the **Expense
Account** to the `Expenses` account. Then, click the __**(right arrow)** icon
to the right of the account.

In the pop-up window, choose **Expenses** or **Cost of Revenue** from the
**Type** drop-down menu.

![Show **Expense Account** field, and external link
icon.](../../../../../_images/external-link1.png)

To configure the **Expense Account** , choose **Stock Valuation** from the
field’s drop-down menu. Verify the account’s type by clicking the __**(right
arrow)** icon, and then ensure the **Type** is **Current Assets**.

![Show the **Expense Account** field.](../../../../../_images/manual-anglo-
saxon-expense.png)

AutomatedManual

Set the **Expense Account** to the **Expenses** or **Cost of Revenue** account
type.

Set the **Expense Account** to the **Expenses** or **Cost of Revenue** account
type.

#### Stock input/output (automated only)

To configure the **Stock Input Account** and **Stock Output Account** , go to
Inventory app ‣ Configuration ‣ Product Categories and select the desired
product category.

In the **Inventory Valuation** field, select **Automated**. Doing so makes the
**Account Stock Properties** section appear. These accounts are defined as
follows:

  * **Compte de valorisation des stocks** : lorsque la valorisation automatisée des stocks est activée sur un produit, ce compte contient la valeur actuelle des produits.

  * **Stock Journal** : accounting journal where entries are automatically posted when a product’s inventory valuation changes.

  * **Compte d’entrée en stock** : les écritures comptables de contrepartie pour tous les mouvements de stock entrants seront enregistrées dans ce compte, à moins qu’un compte de valorisation spécifique n’ait été défini sur l’emplacement d’origine. Il s’agit de la valeur par défaut pour tous les produits dans une catégorie donnée et peut également être défini directement pour chaque produit.

  * **Compte de sortie de stock** : les écritures comptables de contrepartie pour tous les mouvements de stock sortants seront enregistrées dans ce compte, à moins qu’un compte de valorisation spécifique n’ait été défini sur l’emplacement de destination. Il s’agit de la valeur par défaut pour tous les produits dans une catégorie donnée et peut également être défini directement pour chaque produit.

Anglo-SaxonContinental

In Anglo-Saxon accounting, the **Stock Input Account** and **Stock Output
Account** are set to _different_ **Current Assets** accounts. This way,
delivering products and invoicing the customer balance the _Stock Output_
account, while receiving products and billing vendors balance the _Stock
Input_ account.

To modify the account type, go to the click the __**(right arrow)** icon to
the right of the stock input/output account. In the pop-up window, choose
**Current Assets** from the **Type** drop-down menu.

![Display account setup page, highlighting the **Type**
field.](../../../../../_images/account-type.png)

The _Stock Input_ account is set to `Stock Interim (Received)`, a _Current
Asset_ account type.

In Continental accounting, the **Stock Input Account** and **Stock Output
Account** are set to **the same** **Current Assets** account. That way, one
account can be balanced when items are bought and sold.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The stock input and output accounts are both set to <code>Stock Interim (Received)</code>, a
<b>Current Assets</b> account type. They can also be set to the <code>Stock Interim
(Delivered)</code>, as long as the input and output accounts are assigned to the <b>same</b>
account.</p>
<img alt="Show the Stock Input and Output accounts." class="align-center" src="../../../../../_images/continental-stock-account.png"/>
</div>

## Inventory valuation reporting

Pour démarrer, allez à Comptabilité ‣ Analyse ‣ Bilan. En haut du tableau de
bord, changez la valeur du champ **À partir du** en **Aujourd’hui** et ajustez
les **Options** de filtrage sur **Tout déplier** afin de voir toutes les
données les plus récentes affichées en une seule fois.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../finance/accounting/get_started/cheat_sheet">Aide-mémoire de la comptabilité</a></p>
</div>

Sous le poste parent **Actifs circulants** , cherchez le poste imbriqué
**Compte de valorisation des stocks** , où est affichée la valorisation totale
de tout le stock disponible.

Le menu déroulant **Compte de valorisation du stock** permet d’accéder à des
informations plus spécifiques, en sélectionnant soit le **Grand livre** pour
obtenir une vue détaillée de toutes les pièces comptables, soit les
**Imputations comptables** pour passer en revue toutes les pièces comptables
individuelles qui ont été soumises au compte. Il est également possible
d’ajouter des annotations au **Bilan** en cliquant sur **Annoter** , en
complétant la zone de texte en cliquant sur **Enregistrer**.

![Voir la décomposition complète de la valorisation des stocks dans
l'application Konvergo ERP Comptabilité.](../../../../../_images/stock-valuation-
breakdown-in-accounting.png)

