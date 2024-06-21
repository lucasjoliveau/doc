# Outlook Plugin

Outlook allows for third-party applications to connect in order to execute
database actions from emails. Konvergo ERP has a plugin for Outlook that allows for
the creation of an opportunity from the email panel.

## Configuration

The Outlook [Mail Plugin](../mail_plugins) needs to be configured both on
Konvergo ERP and Outlook.

### Enable Mail Plugin

First, enable the _Mail Plugin_ feature in the database. Go to Settings ‣
General Settings ‣ Integrations, enable **Mail Plugin** , and **Save** the
configuration.

### Install the Outlook Plugin

Download (Save Page As ‣ Web Page XML only) the following XML file to upload
later: <https://download.odoocdn.com/plugins/outlook/manifest.xml>.

Next, open the Outlook mailbox, and select any email. After completing this,
click on the **More actions** button in the upper right-side and select **Get
Add-ins**.

![More actions button in Outlook](../../../../_images/more-actions.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>For locally installed versions of Microsoft Outlook, access the <b>Get Add-ins</b> menu item
while in preview mode (<b>not</b> with a message open). First, click on the <b>…
(ellipsis)</b> icon in the upper right of the previewed message, then scroll down, and click on
<b>Get Add-ins</b>.</p>
</div>

Following this step, select the **My add-ins** tab on the left-side.

![My add-ins in Outlook](../../../../_images/my-add-ins.png)

Under **Custom add-ins** towards the bottom, click on **\+ Add a custom add-
in** , and then on **Add from file…**

![Custom add-ins in Outlook](../../../../_images/custom-add-ins.png)

For the next step, attach the `manifest.xml` file downloaded above, and press
**OK**. Next, read the warning and click on **Install**.

![Custom add-in installation warning in Outlook](../../../../_images/add-in-
warning.png)

### Connect the database

Now, Outlook will be connected to the Konvergo ERP database. First, open any email in
the Outlook mailbox, click on the **More actions** button in the upper right-
side, and select **Konvergo ERP for Outlook**.

![Konvergo ERP for Outlook add-in button](../../../../_images/odoo-for-outlook.png)

The right-side panel can now display **Company Insights**. At the bottom,
click on **Login**.

![Logging in the Konvergo ERP database](../../../../_images/panel-login.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Only a limited amount of <b>Company Insights</b> (<em>Lead Enrichment</em>) requests are available as a
trial database. This feature requires <a href="../mail_plugins#mail-plugins-pricing"><span class="std std-ref">prepaid credits</span></a>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If, after a short while, the panel is still empty, it is possible that the browser cookie
settings prevented it from loading. Note that these settings also change if the browser is in
“Incognito” mode.</p>
<p>To fix this issue, configure the browser to always allow cookies on Konvergo ERP’s plugin page.</p>
<p>For Google Chrome, change the browser cookie settings by following the guide at:
<a href="https://support.google.com/chrome/answer/95647">https://support.google.com/chrome/answer/95647</a>
and adding <code>download.odoo.com</code> to the list of <b>Sites that can always use cookies</b>.</p>
<p>Once this is complete, the Outlook panel needs to be opened again.</p>
</div>

Now, enter the Konvergo ERP database URL and click on **Login**.

![Entering the Konvergo ERP database URL](../../../../_images/enter-database-url.png)

Next, click on **Allow** to open the pop-up window.

![New window pop-up warning](../../../../_images/new-window-warning.png)

If the user isn’t logged into the database, enter the credentials. Click on
**Allow** to let the Outlook Plugin connect to the database.

![Allowing the Outlook Plugin to connect to a
database](../../../../_images/odoo-permission.png)

### Add a shortcut to the plugin

By default, the Outlook Plugin can be opened from the _More actions_ menu.
However, to save time, it’s possible to add it next to the other default
actions.

In the Outlook mailbox, click on **Settings** , then on **View all Outlook
settings**.

![Viewing all Outlook settings](../../../../_images/all-outlook-settings.png)

Now, select **Customize actions** under **Mail** , click on **Konvergo ERP for
Outlook** , and then **Save**.

![Konvergo ERP for Outlook customized action](../../../../_images/customize-
actions.png)

Following this step, open any email; the shortcut should be displayed.

![Konvergo ERP for Outlook customized action](../../../../_images/odoo-outlook-
shortcut.png)

### Using the plugin

Now that the plug-in is installed and operational, all that needs to be done
to create a lead is to click on the `O` [Konvergo ERP icon] or navigate to **More
actions** and click on **Konvergo ERP for Outlook**. The side panel will appear on the
right-side, and under **Opportunities** click on **New**. A new window with
the created opportunity in the Konvergo ERP database will populate.

