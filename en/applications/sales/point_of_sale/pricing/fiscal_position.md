# Flexible taxes (fiscal positions)

When running a business, you may need to apply different taxes and record
transactions on various accounts based on the location and type of business of
your customers and providers.

The **fiscal positions** feature enables you to establish rules that
automatically select the right taxes and accounts used for each transaction.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../finance/accounting/taxes/fiscal_positions">Fiscal positions (tax and account mapping)</a></p></li>
<li><p><a href="../../../finance/accounting/taxes">Taxes</a></p></li>
</ul>
</div>

## Configuration

To enable the feature, go to Point of Sale ‣ Configuration ‣ Settings, scroll
down to the **Accounting** section, and enable **Flexible Taxes**.

Then, set a default fiscal position that should be applied to all sales in the
selected POS in the **Default** field. You can also add more fiscal positions
to choose from in the **Allowed** field.

![../../../../_images/flexible-taxes-
setting.png](../../../../_images/flexible-taxes-setting.png)

According to the [fiscal localization
package](../../../finance/fiscal_localizations) activated, several fiscal
positions are preconfigured and can be set and used in POS. However, you can
also [create new fiscal
positions](../../../finance/accounting/taxes/fiscal_positions#fiscal-
positions-mapping).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you do not set a fiscal position, the tax remains as defined in the <b>customer taxes</b> field
on the product form.</p>
</div>

## Use fiscal positions

Open a [POS session](../../point_of_sale#pos-session-start) to use one of
the allowed fiscal positions. Then, click the **Tax** button next to the
**book-shaped** icon and select a fiscal position from the list. Doing so
applies the defined rules automatically to all the products subject to the
chosen fiscal position’s regulations.

![../../../../_images/set-tax.png](../../../../_images/set-tax.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If a default fiscal position is set, the tax button displays the name of the fiscal position.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../finance/accounting/taxes/fiscal_positions">Fiscal positions (tax and account mapping)</a></p>
</div>

