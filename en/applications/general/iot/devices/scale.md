# Connect a scale

A scale can be connected to the IoT box on an Odoo database in a few easy
steps. After setup, the _Point of Sale_ app can be used to weigh products,
which is helpful if their prices are calculated based on weight.

Important

  * In EU member states, [certification is legally required](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG) to use a scale as an integrated device.

  * Odoo is not certified in several countries, including France, Germany, and Switzerland. If you reside in one of these countries, you can still use a scale but without integration to your Odoo database.

  * Alternatively, you have the option to acquire a _non-integrated_ certified scale that prints certified labels, which can then be scanned into your Odoo database.

See also

[Directive 2014/31/EU of the European Parliament](https://eur-
lex.europa.eu/legal-
content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)

## Connection

To link the scale to the IoT box, connect it with a USB cable.

Note

In some cases, a serial port to USB adapter may be needed.

If the scale is [compatible with Odoo IoT Box](https://www.odoo.com/page/iot-
hardware), there is no need to set up anything because it will be
automatically detected as soon as it is connected.

![IOT box auto detection.](../../../../_images/iot-choice.png)

The IoT box may need to be restarted and the scale’s drivers may need to be
downloaded to the box in some cases. To update the drivers, go to the IoT box
homepage and click on Drivers List. Then, click on Load Drivers.

![View of the IoT box settings and driver list.](../../../../_images/driver-
list.png)

If loading the drivers still doesn’t allow for the scale to function, it may
be that the scale is not compatible with the Odoo IoT box. In this case, a
different scale will need to be used.

## Use a scale in a point of sale (POS) system

To use the scale in the _Point of Sale app_ , go to PoS app ‣ 3-Dot Menu on
the PoS ‣ Settings, then enable the IoT box feature. After this is complete,
the scale device can be set.

Select the scale from the Electronic Scale drop-down menu. Then click Save to
save the changes, if required.

![List of the external tools that can be used with PoS and the IoT
box.](../../../../_images/electronic-scale-feature.png)

The scale is now available in all the PoS sessions. Now, if a product has a
price per weight set, clicking on it on the PoS screen opens the scale screen,
where the cashier can weigh the product and add the correct price to the cart.

![Electronic Scale dashboard view when no items are being
weighed.](../../../../_images/scale-view.png)

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus
  *[PoS]: Point of Sale

