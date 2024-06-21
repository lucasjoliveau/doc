# Fiscal positions (tax and account mapping)

Default taxes and accounts are set on products and customers to create new
transactions on the fly. However, depending on the customers’ and providers’
localization and business type, using different taxes and accounts for a
transaction might be necessary.

**Fiscal positions** allow the creation of rules to adapt the taxes and
accounts used for a transaction automatically.

They can be applied automatically, manually, or assigned to a partner.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Several default fiscal positions are available as part of your <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">fiscal localization
package</span></a>.</p>
</div>

## Configuration

> ### Tax and account mapping

To edit or create a fiscal position, go to Accounting ‣ Configuration ‣ Fiscal
Positions, and open the entry to modify or click on **New**.

The mapping of taxes and accounts is based on the default taxes and accounts
defined in the product form.

  * To map to another tax or account, fill out the right column (**Tax to Apply** / **Account to Use Instead**).

![Example of a fiscal position's tax mapping](../../../../_images/fiscal-
positions-tax-mapping.png) ![Example of a fiscal position's account
mapping](../../../../_images/fiscal-positions-account-mapping.png)

  * To remove a tax, leave the field **Tax to Apply** empty.

  * To replace a tax with several other taxes, add multiple lines using the same **Tax on Product**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The mapping only works with <em>active</em> taxes. Therefore, make sure they are active by going to
Accounting ‣ Configuration ‣ Taxes.</p>
</div>

## Application

### Automatic application

To automatically apply a fiscal position following a set of conditions, go to
Accounting ‣ Configuration ‣ Fiscal Positions, open the fiscal position to
modify, and tick **Detect Automatically**.

From there, several conditions can be activated:

  * **VAT Required** : the customer’s VAT number must be present on their contact form.

  * **Country Group** and **Country** : the fiscal position is only applied to the selected country or country group.

![Example of a fiscal position automatic application
settings](../../../../_images/fiscal-positions-automatic.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Taxes on <b>eCommerce orders</b> are automatically updated once the customer has logged in or filled
out their billing details.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The fiscal positions’ <b>sequence</b> defines which fiscal position is applied if all conditions
set on multiple fiscal positions are met simultaneously.</p>
<p>For example, suppose the first fiscal position in a sequence targets <em>country A</em> while the second
fiscal position targets a <em>country group</em> that comprises <em>country A</em>. In that case, only the
first fiscal position will be applied to customers from <em>country A</em>.</p>
</div>

### Manual application

To manually select a fiscal position, open a sales order, invoice, or bill, go
to the **Other Info** tab and select the desired **Fiscal Position** before
adding product lines.

![Selection of a fiscal position on a sales order, invoice, or
bill](../../../../_images/fiscal-positions-manual.png)

### Assign to a partner

To define which fiscal position must be used by default for a specific
partner, go to Accounting ‣ Customers ‣ Customers, select the partner, open
the **Sales & Purchase** tab, and select the **Fiscal Position**.

![Selection of a fiscal position on a customer](../../../../_images/fiscal-
positions-customer.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
<li><p><a href="taxcloud">TaxCloud integration</a> (decommissioning TaxCloud integration in Konvergo ERP 17+)</p></li>
<li><p><a href="B2B_B2C">B2B (tax excluded) and B2C (tax included) pricing</a></p></li>
</ul>
</div>

