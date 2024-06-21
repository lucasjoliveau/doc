# Cash rounding

**Cash rounding** is required when the lowest physical denomination of
currency, or the smallest coin, is higher than the minimum unit of account.

For example, some countries require their companies to round up or down the
total amount of an invoice to the nearest five cents, when the payment is made
in cash.

Each point of sale in Konvergo ERP can be configured to apply cash rounding to the
totals of its bills or receipts.

## Configuration

Go to Point of Sale ‣ Configuration ‣ Settings and enable _Cash Rounding_ ,
then click on _Save_.

![../../../../_images/cash_rounding011.png](../../../../_images/cash_rounding011.png)

Go to Point of Sale ‣ Configuration ‣ Point of Sale, open the point of sale
you want to configure, and enable the _Cash Rounding_ option.

To define the **Rounding Method** , open the drop-down list and click on
_Create and Edit…_.

Define here your _Rounding Precision_ , _Profit Account_ , and _Loss Account_
, then save both the Rounding Method and your Point of Sale settings.

![../../../../_images/cash_rounding02.png](../../../../_images/cash_rounding02.png)

All total amounts of this point of sale now add a line to apply the rounding
according to your settings.

![../../../../_images/cash_rounding03.png](../../../../_images/cash_rounding03.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP Point of Sale only supports the <b>Add a rounding line</b> rounding strategy.</p>
</div>

