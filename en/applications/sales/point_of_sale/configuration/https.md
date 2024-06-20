# Secure connection (HTTPS)

If **Direct Devices** is enabled in a Point of Sale settings (for example, if
you use an [ePos printer](epos_printers.html)), HTTP becomes the default
protocol.

## Force your Point of Sale to use a secure connection (HTTPS)

Add a new **key** in the **System Parameters** to force your Point of Sale to
use a secure connection with the HTTPS protocol.

To do so, activate the [developer
mode](../../../general/developer_mode.html#developer-mode), go to Settings ‣
Technical ‣ Parameters ‣ System Parameters, then create a new parameter, add
the following values and click on _Save_.

  * **Key** : `point_of_sale.enforce_https`

  * **Value** : `True`

See also

  * [Self-signed certificate for ePOS printers](epos_ssc.html)

