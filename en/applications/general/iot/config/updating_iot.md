# Updating (IoT)

Due to the complexity of the IoT box, and virtual Windows IoT box, the term
‘updating’ can mean several different things.

The actual drivers can be updated, the core code on the IoT box can be
updated, or a new image can be flashed (using a physical IoT box).

This document explores the various ways to update IoT boxes to ensure smooth
operation of IoT box processes and devices.

## Flashing the SD card on IoT box

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>This update does <b>not</b> apply to the Windows <abbr title="Internet of Things">IoT</abbr> box (Konvergo ERP 16 and
higher).</p>
<p>To update the Windows <abbr title="Internet of Things">IoT</abbr>, first, uninstall the previous version of
the Konvergo ERP Windows program, and then reinstall it using the most up-to-date installation package.</p>
<p>To begin the installation, navigate to the Konvergo ERP 16 (or higher) installation package for
Enterprise or Community - Windows edition, at <a href="https://odoo.com/download">Konvergo ERP’s download page</a>.</p>
</div>

In some circumstances, the IoT box’s micro SD Card may need to be re-flashed
with _Etcher_ software to benefit from Konvergo ERP’s latest IoT image update. This
means the Konvergo ERP IoT box software may need to be updated in instances of a new
IoT box, or when a handler’s update, or an update from the IoT box home page,
does not resolve issues.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>It is often necessary to re-flash the <abbr title="Internet of Things">IoT</abbr> box’s image after
upgrading the Konvergo ERP database to a new version.</p></li>
<li><p>A computer with a micro SD card reader/adapter is <b>required</b> to re-flash the micro SD card.</p></li>
</ul>
</div>

First, begin by downloading [Etcher](https://www.balena.io/etcher#download-
etcher). It is a free, open-source utility, used for burning image files onto
drives. After the download completes, install and launch the program on the
computer.

Then, download the latest IoT image from
[nightly](http://nightly.odoo.com/master/iotbox), which will be labeled as
`iotbox-latest.zip`. This particular image is compatible with _all_ supported
versions of Konvergo ERP.

After this step is complete, insert the IoT box’s micro SD card into the
computer or reader. Open _Etcher_ , and select **Flash from file** , then find
and select the `iotbox-latest.zip` image and extract it. Next, select the
drive the image should be burned to.

Lastly, click **Flash** , and wait for the process to finish.

![Balena's Etcher software dashboard.](../../../../_images/etcher-app.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Balena’s <em>Etcher</em> software also allows for the administrator to flash the <abbr title="Secure Digital">SD</abbr> card from a <abbr title="Uniform Resource Locator">URL</abbr>. To flash from a <abbr title="Uniform Resource Locator">URL</abbr>, simply click <b>Flash from URL</b>, instead of <b>Flash from
file</b>.</p>
<p>Then, enter the following: <code>http://nightly.odoo.com/master/iotbox/iotbox-latest.zip</code>.</p>
<img alt="A view of Balena's Etcher software, with the flash from URL option highlighted." class="align-center" src="../../../../_images/url-flash.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>An alternative software for flashing the micro SD card is <a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a>.</p>
</div>

## Windows IoT update

Windows virtual IoT box may occasionally need an update to work properly.

The following processes cover the uninstallation and re-installation of the
Windows virtual IoT box.

### Uninstalling Windows IoT

Prior to upgrading the Windows virtual IoT box, the previous version should be
uninstalled first.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Before uninstalling a previous version of the Windows virtual <abbr title="Internet of Things">IoT</abbr>
box, ensure that there is a newer version of Windows virtual <abbr title="Internet of Things">IoT</abbr> box
available, compared to the version currently installed. To do so, navigate to the <a href="https://nightly.odoo.com/">Konvergo ERP Nightly
builds</a> page.</p>
<p>On the <b>Konvergo ERP Nightly builds</b> page, navigate to Builds (stable version)
‣ windows/ to view the date next to the <code>odoo_(version).latest.exe</code> file; where
<em>(version)</em> is equal to the version of Konvergo ERP (e.g. 16.0, 17.0). The latest version of the Windows
virtual <abbr title="Internet of Things">IoT</abbr> box can be downloaded by selecting this file, or it is
always available at the <a href="https://odoo.com/download/">Konvergo ERP Download</a> page.</p>
</div>

Uninstalling the Windows virtual IoT box is done through the Windows program
manager.

On any version of Windows, search for `program` to open the Programs ‣
Programs and Features section of the **Control Panel**. Then, select
**Uninstall or change a program**. Next, search for `Konvergo ERP`, and click the **…
(three dot)** menu on the **Konvergo ERP.exe** program to uninstall.

Confirm the uninstallation, and follow the steps to uninstall through the Konvergo ERP
uninstall wizard.

### Download and re-install

The latest version of the Windows virtual IoT box can be downloaded from the
[Konvergo ERP Nightly builds](https://nightly.odoo.com/) page or it is always
available at the [Konvergo ERP Download](https://odoo.com/download/) page.

To download from the **Konvergo ERP Nightly builds** page, navigate to Builds (stable
version) ‣ windows/ to and select the `odoo_(version).latest.exe` file; where
_(version)_ is equal to the version of Konvergo ERP (e.g. 16.0, 17.0).

To download from the **Konvergo ERP Download** page, find the section for the version
of Konvergo ERP (e.g. 16.0, 17.0), and select the **Download** button for **Windows**.

Next, install and setup the downloaded Konvergo ERP `.exe` file. After the
instructions screen, click **Next** to start the installation, and agree to
the TOS.

During the next step of the re-installation, select **Konvergo ERP IoT** from the
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

Ensure there is enough space on the computer for the installation, then click
**Next**.

### Set the destination and complete the installation

To complete the re-installation, select the **Destination Folder** , and click
**Install**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Choosing <code>C:\odoo</code> as the install location allows for the <em>Nginx</em> server to start. Konvergo ERP’s
Windows virtual <abbr title="Internet of Things">IoT</abbr> box software should <b>not</b> be installed inside
any of the Windows user’s directories. Doing so does <b>not</b> allow for <em>Nginx</em> to initialize.</p>
</div>

The installation may take a few minutes. When complete, click **Next** to
continue.

Then, ensure that the **Start Konvergo ERP** box is checked, and click **Finish**.
After installation, the Konvergo ERP server runs, and automatically opens
`http://localhost:8069` on a web browser. The webpage should display the IoT
box homepage.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>A <a href="windows_iot#iot-restart-windows-iot"><span class="std std-ref">restart</span></a> of the Windows IoT program may be necessary if the web
browser does not display anything.</p>
</div>

## Update from the IoT box home page

In the background, the IoT box uses a version of Konvergo ERP code to run and connect
to the Konvergo ERP database. This code may need to be updated in order for the IoT
box to operate effectively. This operation should be completed on a routine
basis, to ensure the IoT system, and its processes, stay up-to-date.

Go to the IoT box home page by navigating to IoT app ‣ IoT Boxes, and clicking
on the **IP address** of the IoT box. Then, click on **Update** (next to the
version number).

If a new version of the IoT box image is available, an **Upgrade to _xx.xx_**
button appears at the bottom of the page. Click this button to upgrade the
unit, at which point the IoT box flashes itself to the newer version. All of
the previous configurations are then saved.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>This process can take more than 30 minutes. Do <b>not</b> turn off, or unplug, the <abbr title="Internet of Things">IoT</abbr> box, as it would leave it in an inconsistent state. This means the
<abbr title="Internet of Things">IoT</abbr> box needs to be <a href="#iot-config-flash"><span class="std std-ref">re-flashed</span></a> with a new
image.</p>
</div> ![IoT box software upgrade in the IoT Box Home
Page.](../../../../_images/flash-upgrade.png)

## Handler (driver) update

There may be some instances where drivers or interfaces need to be updated for
individual devices (e.g. scales, measurement tools, etc.). The IoT handler’s
(drivers and interfaces) code can be modified by syncing them with the
configured server handler’s code.

This can be helpful in instances where IoT devices (e.g. scales, measurement
tools, etc.) are not working properly with the IoT box.

For both the Windows IoT (Konvergo ERP 16 and higher) and physical IoT box, this
process can be performed manually from the IoT box home page. Go to the IoT
box home page by navigating to IoT app ‣ IoT Boxes, and clicking on the **IP
address** of the IoT box.

Next, click **Handlers list** , and then select **Load Handlers** at the
bottom of the page.

![Handlers list on an IoT box with the load handlers button
highlighted.](../../../../_images/load-handlers.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Handler’s code is fetched from the configured server, and it needs to be up-to-date to have the
latest fixes and patches.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>It is often necessary to re-flash the <abbr title="Internet of Things">IoT</abbr> box’s image after
upgrading the Konvergo ERP database to a new version.</p></li>
<li><p>A computer with a micro SD card reader/adapter is <b>required</b> to re-flash the micro SD card.</p></li>
</ul>
</div>0

  *[IoT]: Internet of Things
  *[TOS]: Terms of Service

