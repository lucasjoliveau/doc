# Self-signed certificate for ePOS printers

To work with Konvergo ERP, some printer models that can be used without an [IoT
box](../../../general/iot/config/connect) may require [the HTTPS
protocol](https) to establish a secure connection between the browser and
the printer. However, trying to reach the printer’s IP address using HTTPS
leads to a warning page on most web browsers. In that case, you can
temporarily force the connection, which allows you to reach the page in HTTPS
and use the ePOS printer in Konvergo ERP as long as the browser window stays open.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The connection is lost after closing the browser window. Therefore, this method should only be
used as a <b>workaround</b> or as a pre-requisite for the <a href="#epos-ssc-instructions"><span class="std std-ref">following instructions</span></a>.</p>
</div>

## Generate, export, and import self-signed certificates

For a long-term solution, you must generate a **self-signed certificate**.
Then, export and import it into your browser.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p><b>Generating</b> an SSL certificate should only be done <b>once</b>. If you create another
certificate, devices using the previous one will lose HTTPS access.</p>
</div>

Windows 10 & Linux OSMac OSAndroid OSiOS

Generate a self-signed certificateExport a self-signed certificateImport a
self-signed certificate

Navigate to the ePOS’ IP address (e.g., `https://192.168.1.25`) and force the
connection by clicking **Advanced** and **Proceed to [IP address] (unsafe)**.

![warning page about the connection privacy on Google
Chrome](../../../../_images/browser-https-insecure.png)

Warning page on Google Chrome, Windows 10

Then, sign in using your printer credentials to access the ePOS printer
settings. To sign in, enter `epson` in the **ID** field and your printer
serial number in the **Password** field.

Click **Certificate List** in the **Authentication** section, and click
**create** to generate a new **Self-Signed Certificate**. The **Common Name**
should be automatically filled out. If not, fill it in with the printer IP
address number. Select the years the certificate will be valid in the
**Validity Period** field, click **Create** , and **Reset** or manually
restart the printer.

The self-signed certificate is generated. Reload the page and click
**SSL/TLS** in the **Security** section to ensure **Selfsigned Certificate**
is correctly selected in the **Server Certificate** section.

The export process is heavily dependent on the OS and the browser. Start by
accessing your ePOS printer settings on your web browser by navigating to its
IP address (e.g., `https://192.168.1.25`). Then, force the connection as
explained in the **Generate a self-signed certificate tab**.

If you are using **Google Chrome** ,

  1. click **Not secure** next to the search bar, and **Certificate is not valid** ;

![Connection to the printer not secure button in Google Chrome
browser.](../../../../_images/browser-warning.png)

  2. go to the **Details** tab and click **Export** ;

  3. add `.crt` at the end of the file name to ensure it has the correct extension;

  4. select **Base64-encoded ASCII, single certificate** , at the bottom of the pop-up window;

  5. save, and the certificate is exported.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Make sure that the certificate ends with the extension <code>.crt</code>. Otherwise, some
browsers might not see the file during the import process.</p>
</div>

If you are using **Mozilla Firefox** ,

  1. click the **lock-shaped** icon on the left of the address bar;

  2. go to Connection not secure ‣ More information ‣ Security tab ‣ View certificate;

![Connection is not secure button in Mozilla Firefox
browser](../../../../_images/mozilla-not-secure.png)

  1. scroll down to the **Miscellaneous** section;

  2. click **PEM (cert)** in the **Download** section;

  3. save, and the certificate is exported.

The import process is heavily dependent on the OS and the browser.

Windows 10Linux

Windows 10 manages certificates, which means that self-signed certificates
must be imported from the certification file rather than the browser. To do
so,

  1. open the Windows File Explorer and locate the downloaded certification file;

  2. right-click on the certification file and click **Install Certificate** ;

  3. select where to install the certificate and for whom - either for the **Current User** or all users (**Local Machine**). Then, click **Next** ;

  4. on the `Certificate Store` screen, tick **Place all certificates in the following store** , click **Browse…** , and select **Trusted Root Certification Authorities** ;

![../../../../_images/win-cert-wizard-store.png](../../../../_images/win-cert-
wizard-store.png)

  5. click **Finish** , accept the pop-up security window;

  6. restart the computer to make sure that the changes are applied.

If you are using **Google Chrome** ,

  1. open Chrome;

  2. go to Settings ‣ Privacy and security ‣ Security ‣ Manage certificates;

  3. go to the **Authorities** tab, click **Import** , and select the exported certification file;

  4. accept all warnings;

  5. click **ok** ;

  6. restart your browser.

If you are using **Mozilla Firefox** ,

  1. open Firefox;

  2. go to Settings ‣ Privacy & Security ‣ Security ‣ View Certificates… ‣ Import;

  3. select the exported certification file;

  4. tick the checkboxes and validate;

  5. restart your browser.

On Mac OS, you can secure the connection for all browsers by following these
steps:

  1. open Safari and navigate to your printer’s IP address. Doing so leads to a warning page;

  2. on the warning page, go to Show Details ‣ visit this website ‣ Visit Website, validate;

  3. reboot the printer so you can use it with any other browser.

To generate and export an SSL certificate and send it to IOS devices, open
**Google Chrome** or **Mozilla Firefox**. Then,

Generate a self-signed certificateExport a self-signed certificate

Navigate to the ePOS’ IP address (e.g., `https://192.168.1.25`) and force the
connection by clicking **Advanced** and **Proceed to [IP address] (unsafe)**.

![Warning page about the connection privacy on Google
Chrome](../../../../_images/browser-https-insecure.png)

Warning page on Google Chrome, Windows 10

Then, sign in using your printer credentials to access the ePOS printer
settings. To sign in, enter `epson` in the **ID** field and your printer
serial number in the **Password** field.

Click **Certificate List** in the **Authentication** section, and click
**create** to generate a new **Self-Signed Certificate**. The **Common Name**
should be automatically filled out. If not, fill it in with the printer IP
address number. Select the years the certificate will be valid in the
**Validity Period** field, click **Create** , and **Reset** or manually
restart the printer.

The self-signed certificate is generated. Reload the page and click
**SSL/TLS** in the **Security** section to ensure **Selfsigned Certificate**
is correctly selected in the **Server Certificate** section.

The export process is heavily dependent on the OS and the browser. Start by
accessing your ePOS printer settings on your web browser by navigating to its
IP address (e.g., `https://192.168.1.25`). Then, force the connection as
explained in the **Generate a self-signed certificate tab**.

If you are using **Google Chrome** ,

  1. click **Not secure** next to the search bar, and **Certificate is not valid** ;

![Connection to the printer not secure button in Google
Chrome](../../../../_images/browser-warning.png)

  2. go to the **Details** tab and click **Export** ;

  3. add `.crt` at the end of the file name to ensure it has the correct extension;

  4. select **Base64-encoded ASCII, single certificate** , at the bottom of the pop-up window;

  5. save, and the certificate is exported.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Make sure that the certificate ends with the extension <code>.crt</code>. Otherwise, some
browsers might not find the file during the import process.</p>
</div>

If you are using **Mozilla Firefox** ,

  1. click the **lock-shaped** icon on the left of the address bar;

  2. go to Connection not secure ‣ More information ‣ Security tab ‣ View certificate;

![Connection is not secure button in Mozilla
Firefox](../../../../_images/mozilla-not-secure.png)

  3. scroll down to the **Miscellaneous** section;

  4. click **PEM (cert)** in the **Download** section;

  5. save, and the certificate is exported.

To import an SSL certificate into an Android device, first create and export
it from a computer. Next, transfer the `.crt` file to the device using email,
Bluetooth, or USB. Once the file is on the device,

  1. open the settings and search for `certificate`;

  2. click **Certificate AC** (Install from device storage);

  3. select the certificate file to install it on the device.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The specific steps for installing a certificate may vary depending on the version of
Android and the device manufacturer.</p>
</div>

To import an SSL certificate into an iOS device, first create and export it
from a computer. Then, transfer the `.crt` file to the device using email,
Bluetooth, or any file-sharing service.

Downloading this file triggers a warning pop-up window. Click **Allow** to
download the configuration profile, and close the second pop-up window. Then,

  1. go to the **Settings App** on the iOS device;

  2. click **Profile Downloaded** under the user’s details box;

  3. locate the downloaded `.crt` file and select it;

  4. click **Install** on the top right of the screen;

  5. if a passcode is set on the device, enter the passcode;

  6. click **Install** on the top right of the certificate warning screen and the pop-up window;

  7. click **Done**.

![../../../../_images/ssl-ios-verified.png](../../../../_images/ssl-ios-
verified.png)

The certificate is installed, but it still needs to be authenticated. To do
so,

  1. go to Settings ‣ General ‣ About > Certificate Trust Settings;

  2. enable the installed certificate using the **slide button** ;

  3. click **Continue** on the pop-up window.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>If you need to export SSL certificates from an operating system or web browser that has not
been mentioned, search for <code>export SSL certificate</code> + <code>the name of your browser or operating
system</code> in your preferred search engine.</p></li>
<li><p>Similarly, to import SSL certificates from an unmentioned OS or browser, search for <code>import SSL
certificate root authority</code> + <code>the name of your browser or operating system</code> in your preferred
search engine.</p></li>
</ul>
</div>

## Check if the certificate was imported correctly

To confirm your printer’s connection is secure, connect to its IP address
using HTTPS. For example, navigate to `https://192.168.1.25` in your browser.
If the SSL certificate has been applied correctly, you should no longer see a
warning page, and the address bar should display a padlock icon, indicating
that the connection is secure.

  *[OS]: Operating System

