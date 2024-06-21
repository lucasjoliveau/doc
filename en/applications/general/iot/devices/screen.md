# Connect a screen

In Konvergo ERP, an IoT box can be connected to a screen display. After being
configured, the screen can be used to display a Point of Sale (PoS) order to a
client.

![../../../../_images/screen-pos-client-
display.png](../../../../_images/screen-pos-client-display.png)

An example of a PoS (point of sale) order on a screen display.

Access the customer display by going to the IoT box homepage and clicking on
the **PoS Display** button. To get to the IoT box homepage, navigate to IoT
app ‣ IoT Boxes and click on the IoT box homepage link.

## Connection

The way to connect the screen display to the IoT box differs depending on the
model.

IoT Box model 4IoT Box model 3

Connect up to two screens with micro-HDMI cables on the side of the IoT box.
If two screens are connected, they can display distinct content (see Screen
Usage).

Connect the screen with an HDMI cable on the side of the IoT box.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../config/connect#iot-connect-schema"><span class="std std-ref">See the Raspberry Pi Schema</span></a>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Screen(s) should be connected before the <abbr title="Internet of Things">IoT</abbr> box is switched on. If
it is already on, connect the screen(s), and then restart the <abbr title="Internet of Things">IoT</abbr>
box by unplugging it for ten seconds and plugging it back into its power source.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The usage of HDMI/micro-HDMI adapters may cause issues which will result in a blank, black screen
on the screen display. Using the specific cable for the display connection is recommended.</p>
</div>

If the connection was successful, the screen should display the **POS Client
display** screen.

![The default "POS Client Display" screen that appears when a screen display
is successfully connected to an IoT box.](../../../../_images/screen-pos-
client-display-no-order.png)

The screen should also appear in the list of **Displays** on the IoT box
homepage. Alternatively, the display can be seen by accessing IoT app ‣
Devices.

![An example of a screen display name shown on the IoT Box Home
Page.](../../../../_images/screen-screen-name-example.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If no screen is detected, a default display named <b>Distant Display</b> will be displayed
instead. This indicates that there is no hardware screen connected.</p>
<blockquote>
<div><img alt='The "Distant Display" screen name will be used if no screen is detected.' class="align-center" src="../../../../_images/screen-no-screen.png"/>
</div></blockquote>
</div>

## Usage

### Show Point of Sale orders to customers

To use the screen in the _Point of Sale app_ , go to Point of Sale ‣
Configuration ‣ Point of Sale, select a PoS, click **Edit** if necessary, and
enable the **IoT Box** feature.

Next, select the screen from the **Customer Display** drop-down menu. Then
click **Save** , if required.

![Connect the screen display to the Point of Sale
app.](../../../../_images/screen-pos-screen-config.png)

The screen is now available for PoS sessions. A screen icon will appear in the
menu at the top of the screen to indicate the screen’s connection status.

![The "screen" icon on the Point of Sale display shows the connection status
with the screen.](../../../../_images/screen-pos-icon.png)

The screen will automatically show the PoS orders and update when changes are
made to the order.

![An example of a PoS order on a screen display.](../../../../_images/screen-
pos-client-display.png)

### Display a website on the screen

Open the screen form view by accessing IoT app ‣ Devices ‣ Customer Display.
This allows the user to choose a particular website URL to display on the
screen using the **Display URL** field.

  *[IoT]: Internet of Things
  *[PoS]: Point of Sale

