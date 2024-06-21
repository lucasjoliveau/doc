# Gmail Plugin

The _Gmail Plugin_ integrates an Konvergo ERP database with a Gmail inbox, so users
can keep track of all their work between Gmail and Konvergo ERP, without losing any
information.

## Konvergo ERP Online users

For databases hosted on Konvergo ERP Online (or Konvergo ERP.sh), follow the steps below to
configure the Gmail Plugin.

### Install the Gmail Plugin

First, log in to the Gmail account that the user wishes to connect to Konvergo ERP.

From the Gmail inbox, click the plus sign icon on the right side panel to get
add-ons. If the side panel is not visible, click on the arrow icon at the
bottom right corner of the inbox to reveal it.

![Plus sign icon on the Gmail inbox side panel.](../../../../_images/gmail-
side-panel.png)

Then, use the search bar to search for `Konvergo ERP` and locate the **Konvergo ERP Inbox
Addin**.

![Konvergo ERP Inbox Addin on Google Workspace
Marketplace.](../../../../_images/google-workspace-marketplace.png)

Or, go directly to the **Konvergo ERP Inbox Addin** page on the [Google Workspace
Marketplace](https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275).

Once the plugin is located, click **Install**. Then, click **Continue** to
start the installation.

Next, select which Gmail account the user wishes to connect to Konvergo ERP. Then
click **Allow** to let Konvergo ERP access the Google account. Google will then show a
pop-up window confirming that the installation was successful.

### Configure the Konvergo ERP database

The **Mail Plugin** feature must be enabled in the Konvergo ERP database in order to
use the Gmail Plugin. To enable the feature, go to Settings ‣ General
Settings. Under the **Integrations** section, activate **Mail Plugin** , and
then click **Save**.

![The Mail Plugin feature in the Settings.](../../../../_images/mail-plugin-
setting.png)

### Configure the Gmail inbox

In the Gmail inbox, a purple Konvergo ERP icon is now visible on the right side panel.
Click on the Konvergo ERP icon to open up the Konvergo ERP plugin window. Then, click on any
email in the inbox. Click **Authorize Access** in the plugin window to grant
Konvergo ERP access to the Gmail inbox.

![The Authorize Access button in the right sidebar of the Konvergo ERP plugin
panel.](../../../../_images/authorize-access.png)

Next, click **Login**. Then, enter the URL of the Konvergo ERP database that the user
wishes to connect to the Gmail inbox, and log in to the database.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Use the general URL for the database, not the URL of a specific page in the database. For
example, use <code>https://mycompany.odoo.com</code>, not
<code>https://mycompany.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Finally, click **Allow** to let Gmail access the Konvergo ERP database. The browser
will then show a **Success!** message. After that, close the window. The Gmail
inbox and Konvergo ERP database are now connected.

## Konvergo ERP On-Premise users

For databases hosted on servers other than Konvergo ERP Online (or Konvergo ERP.sh), follow
the steps below to configure the Gmail Plugin.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>As part of their security guidelines, Google requires add-on creators to provide a list of URLs
that can be used in actions and redirections launched by the add-on. This protects users by
ensuring, for example, that no add-on redirects users toward a malicious website. (Read more on
<a href="https://developers.google.com/apps-script/manifest/allowlist-url">Google Apps Script</a>.)</p>
<p>Since Konvergo ERP can only list the <code>odoo.com</code> domain and not every on-premise customer’s unique server
domain, on-premise customers cannot install the Gmail Plugin from the Google Workspace
Marketplace.</p>
</div>

### Install the Gmail Plugin

First, access the [GitHub repository](https://github.com/odoo/mail-client-
extensions) for the Konvergo ERP Mail Plugins. Next, click on the green **Code**
button. Then, click **Download ZIP** to download the Mail Plugin files onto
the user’s computer.

![Download the ZIP file from the Konvergo ERP GitHub repository for Mail
Plugins.](../../../../_images/gh-download-zip.png)

Open the ZIP file on the computer. Then, go to mail-client-extensions-master ‣
gmail ‣ src ‣ views, and open the `login.ts` file using any text editor
software, such as Notepad (Windows), TextEdit (Mac), or Visual Studio Code.

Delete the following three lines of text from the `login.ts` file:

    
    
    if (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
         return notify("The URL must be a subdomain of odoo.com");
    }
    

This removes the `odoo.com` domain constraint from the Gmail Plugin program.

Next, in the ZIP file, go to mail-client-extensions-master ‣ gmail, and open
the file called **appsscript.json**. In the **urlFetchWhitelist** section,
replace all the references to `odoo.com` with the Konvergo ERP customer’s unique
server domain.

Then, in the same **gmail** folder, open the file called **README.md**. Follow
the instructions in the **README.md** file to push the Gmail Plugin files as a
Google Project.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The computer must be able to run Linux commands in order to follow the instructions on the
<b>README.md</b> file.</p>
</div>

After that, share the Google Project with the Gmail account that the user
wishes to connect to Konvergo ERP. Then, click **Publish** and **Deploy from
manifest**. Lastly, click **Install the add-on** to install the Gmail Plugin.

### Configure the Konvergo ERP database

The **Mail Plugin** feature must be enabled in the Konvergo ERP database in order to
use the Gmail Plugin. To enable the feature, go to Settings ‣ General
Settings. Under the **Integrations** section, activate **Mail Plugin** , and
then click **Save**.

![The Mail Plugin feature in the Settings.](../../../../_images/mail-plugin-
setting.png)

### Configure the Gmail inbox

In the Gmail inbox, a purple Konvergo ERP icon is now visible on the right side panel.
Click on the Konvergo ERP icon to open up the Konvergo ERP plugin window. Then, click on any
email in the inbox. Click **Authorize Access** in the plugin window to grant
Konvergo ERP access to the Gmail inbox.

![The Authorize Access button in the right sidebar of the Konvergo ERP plugin
panel.](../../../../_images/authorize-access.png)

Next, click **Login**. Then, enter the URL of the Konvergo ERP database that the user
wishes to connect to the Gmail inbox, and log in to the database.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Use the general URL for the database, not the URL of a specific page in the database. For
example, use <code>https://mycompany.odoo.com</code>, not
<code>https://mycompany.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Finally, click **Allow** to let Gmail access the Konvergo ERP database. The browser
will then show a **Success!** message. After that, close the window. The Gmail
inbox and Konvergo ERP database are now connected.

