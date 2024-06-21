# Secure connection (HTTPS)

If **Direct Devices** is enabled in a Point of Sale settings (for example, if
you use an [ePos printer](epos_printers)), HTTP becomes the default
protocol.

## Force your Point of Sale to use a secure connection (HTTPS)

Add a new **key** in the **System Parameters** to force your Point of Sale to
use a secure connection with the HTTPS protocol.

To do so, activate the [developer
mode](../../../general/developer_mode#developer-mode), go to Settings ‣
Technical ‣ Parameters ‣ System Parameters, then create a new parameter, add
the following values and click on _Save_.

  * **Key** : `point_of_sale.enforce_https`

  * **Value** : `True`

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="epos_ssc">Self-signed certificate for ePOS printers</a></p></li>
</ul>
</div>

