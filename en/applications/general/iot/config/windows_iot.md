# Connect Windows IoT Konvergo ERP

A Virtual IoT box is a computer program that needs to be downloaded and
installed on a Windows computer. This requires a Windows operating system with
an Konvergo ERP 16 or later database.

The Windows virtual IoT box works the same way as a physical IoT box, with the
ability to run most of the same devices. All POS devices work with it, such as
a scale or printer. Payment terminals will also work, but it should be noted
that MRP devices are not compatible. _These include cameras or measurement
tools._

## Pre-requisites

The following items will be needed to complete the Windows IoT installation.

  * Konvergo ERP 16 database or any version above.

  * IoT compatible devices (except those mentioned above). Refer to: [Konvergo ERP’s compatible IoT devices](https://www.odoo.com/app/iot-hardware).

  * Device drivers for Windows.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP recommends using an updated, recent version of Windows (Windows 10/11) as some older
operating systems can cause the Windows virtual <abbr title="Internet of Things">IoT</abbr> to not work.</p>
</div>

  * Windows computer (laptop, desktop, or server).

  * Konvergo ERP IoT subscription. Refer to: [Internet of Things (IoT) eligibility](https_certificate_iot#iot-iot-eligibility).

## Connect the Windows virtual IoT box to an Konvergo ERP database

The Windows virtual IoT box is simple to setup in just a few easy steps.
Follow this process when installing the Windows virtual IoT software for the
first time.

### Download and initial installation

To begin the installation, navigate to the Konvergo ERP 16 or higher installation
package for Community - Windows edition at [Konvergo ERP’s download
page](https://odoo.com/download). Next, install and setup the Konvergo ERP `.exe`
file. After the instructions screen, click **Next** to start the installation
and agree to the TOS.

During the next step of the installation, select **Konvergo ERP IoT** from the
**Select the type of install** drop-down menu.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>For reference, the following should be installed:</p>
<ul>
<li><p><b>Konvergo ERP server</b></p></li>
<li><p><b>Konvergo ERP IoT</b></p></li>
<li><p><b>Nginx WebServer</b></p></li>
<li><p><b>Ghostscript interpreter</b></p></li>
</ul>
</div>

Ensure there is enough space on the computer for the installation and click
**Next**.

### Setting the destination and completing the installation

To complete the installation, select the **Destination Folder** and click
**Install**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Choosing <code>C:\odoo</code> as the install location will allow for the Nginx server to start. If the
folder doesn’t exist, then create it. Otherwise the installation files will be spread throughout
the hard drive.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Konvergo ERP’s Windows virtual IoT software should not be installed inside any of the Window’s User’s
directories. Doing so will not allow for Nginx to initialize.</p>
</div>

The installation may take a few minutes. When complete, click **Next** to
continue.

Ensure that the **Start Konvergo ERP** box is checked and click **Finish**. After
installation, the Konvergo ERP server will run and automatically open
`http://localhost:8069` on a web browser. The webpage should display the IoT
box homepage.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>A restart of the Windows IoT program may be necessary should the web browser not display
anything. <a href="#iot-restart-windows-iot"><span class="std std-ref">Restart Windows IoT box</span></a></p>
</div>

### Connecting devices

Next, connect the IoT devices to the Windows computer. Windows should
automatically detect the device because the driver is pre-installed on the
computer. If not, search for and install the Windows driver for the device.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Most devices connect to the Windows Machine for Windows IoT automatically through Windows
Plug-N-Play (PnP). However, if Windows does not automatically recognize the device after
connecting, then the administrator may need to install the corresponding drivers manually.</p>
<p>Devices automatically recognized:</p>
<ul>
<li><p>Regular ink/toner based printers</p></li>
<li><p>Receipt printers (Epson/Star)</p></li>
<li><p>Barcode scanners</p></li>
<li><p>Measurement devices (although some configuration of the measurement device settings is
required) See this documentation: <a href="../devices/measurement_tool">Connect a measurement tool</a></p></li>
</ul>
<p>Devices not automatically recognized (requires manual driver download):</p>
<ul>
<li><p>Label printers (Zebra)</p></li>
<li><p>Scales</p></li>
</ul>
<p>Reference the manufacturer’s website for the equipment in question. Then, download the drivers
and install them on the Windows machine. Reconnect the device in question and Windows will find
the device.</p>
</div>

Following connecting devices to the computer, refresh the IoT box homepage and
verify the device is seen. If not, reload the handlers through the IoT box
homepage.

Finally, connect Windows IoT to a database using existing instructions
(manually using the Token).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="connect">Connect an IoT box to Konvergo ERP</a></p>
</div>

Now the installation is complete, the devices connected to IoT can be used to
complete processes/actions.

## Troubleshooting

### Restart Windows IoT box

In some instances a manual restart of the physical IoT box can resolve the
issue of an IoT box not showing up on the database. For the Windows virtual
IoT box a manual restart of the Konvergo ERP server can resolve database connection
issues.

To restart the virtual Windows IoT server:

  1. Type `Services` into the Windows **Search Bar**.

  2. Select the Services App and scroll down to the **Konvergo ERP** service.

  3. Right click on **Konvergo ERP** and select **Start** or **Restart**. This action will manually restart the Konvergo ERP IoT server.

### Firewalls

Firewalls keep devices safe and secure. Sometimes they can block connections
that should be made though. The Windows virtual IoT box software may not be
reachable to the LAN due to a firewall preventing the connection. Consult your
local IT support team to make exceptions (network discovery) in the OS or
firewall program. Windows has their own firewall as do other virus protection
programs.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A client might encounter a time when they are able to reach the homepage of the <abbr title="Internet of Things">IoT</abbr> box, yet they cannot access it from another computer/mobile device/tablet
on the same network.</p>
</div>

#### Making an exception on Windows Defender

It is possible to allow other devices to access the Windows virtual IoT box
while keeping the firewall on. This is done by creating a rule on _Windows
Defender_ and allowing communication through port `8069`. The following
process describes the steps to take in order to make this exception.

##### Create a rule in Windows Defender

First, open the _Windows Firewall_ by navigating to the Start Menu and typing
in `Firewall`. Then, open the Windows Defender Firewall program. In the left-
hand menu, navigate to **Advanced Settings**.

Once **Advanced Settings** have been selected, click **Inbound Rules** in the
left-hand menu. Then, in the right-hand menu column (under **Inbound Rules**),
click on **New Rule** to create a new rule.

##### Configure new rule

On the Rule Type screen, select **Port**. Then click **Next**. From the
Protocol and Ports page leave the rule application to **TCP**. Then, select
**Specific Local Ports** for the **ports** option. In the text box, type in
`8069, 443`. Finally, click **Next** to continue to the next step.

On the Actions page, select **Allow the connection** and click **Next**. The
following page on the Rule Configuration wizard is the **Profile** page. On
this page, select whichever connection type applies to the network the Windows
machine is operating on. Ideally, select **Private** only connections. The
_Private_ connection type is the most secure connection while allowing the
selected port to communicate. Click **Next** to continue.

Finally, assign a new, unique name to the rule. For example, this name can be
`Konvergo ERP`. Optionally, add a brief description in the **Description** field.
Click **Finish** to complete the **Rule Configuration** wizard. Now, the new
rule is active and devices can connect to the Windows virtual IoT box.

#### Worldline exception

_Worldline_ is a payment terminal that can be connected to Konvergo ERP’s _PoS_ (point
of sale) system. It allows for a comprehensive and fluid payment experience
for customers. Worldline is available in Belgium, the Netherlands, and
Luxembourg.

When using the Windows IoT server to connect the Worldline payment terminal,
it is necessary to create an exception in the Windows firewall so that a
connection can be made between the Konvergo ERP database/IoT box and Worldline.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../sales/point_of_sale/payment_methods/terminals/worldline">Worldline</a></p>
</div>

To create the exception, first, open the _Windows Defender Firewall_ app on
the Windows machine. This can be accomplished by typing `windows defender` in
the **Search** bar.

Next, click **Advanced settings** in the left menu.

![Advanced settings option highlighted in the left pane of the Windows
Defender Firewall app.](../../../../_images/advanced-settings.png)

In the left menu, choose **Inbound Rules**.

![Windows Defender left window pane with inbound rules menu item
highlighted.](../../../../_images/inbound-rules.png)

After selecting **Inbound Rules** , select **New Rule** in the far right menu.

![New rule dropdown shown with new rule option
highlighted.](../../../../_images/new-rule.png)

Then, for the **Rule Type** , select the radio button for **Port**. Click
**Next** to continue to the rest of the configuration.

![Rule Type window open, with the radio button next to port
highlighted.](../../../../_images/radio-port.png)

On the **Protocols and Ports** page, choose the radio button for **TCP** ,
under **Does this rule apply to TCP or UDP?**.

Next, under **Does this rule apply to all local ports or specific ports?** ,
select the radio button for **Specific local ports**. Then, enter `9050`, and
click **Next** to continue.

![Protocol/port configuration window with TCP, specific port \(9050\) and Next
highlighted.](../../../../_images/protocol-port.png)

The next screen is the **Action** page. Under **What action should be taken
when a connection matches the specified conditions?** , choose the radio
button for **Allow the connection**. Then, click **Next** to continue.

A **Profile** page appears. Under **When does this rule apply?** , leave the
three boxes checked for: **Domain** , **Private** , and **Public**. Click
**Next** to continue to the naming convention page.

On the **Name** page, enter `Konvergo ERP Worldline`, under the **Name** field. Enter
a **Description (optional)**. Finally, once ready, click **Finish**.

The final **Inbound rule** should appear as follows:

| Konvergo ERP Worldline  
---|---  
Profile | All  
Enabled | Yes  
Action | Allow  
Override | No  
Program | Any  
Local Address | Any  
Remote Address | Any  
Protocol | TCP  
Local Port | 9050  
Remote Port | Any  
Authorized Users | Any  
Authorized Computers | Any  
Authorized Local Principals | Any  
Local User Owner | Any  
PolicyAppld | None  
Application Package | Any  
  
### Uninstalling Windows IoT

Uninstalling the Windows virtual IoT box is done through the Windows program
manager. Using any Windows version, search for `program`. Then, select **Add
or Remove Programs** located in the control panel. Search for `Konvergo ERP` and click
the **three dot menu** to uninstall.

Confirm the un-installation and follow the steps to uninstall through the Konvergo ERP
uninstall guide.

  *[IoT]: Internet of Things
  *[POS]: Point of Sale
  *[MRP]: Material Requirement Planning
  *[TOS]: Terms of Service
  *[LAN]: Local Area Network
  *[OS]: Operating System

