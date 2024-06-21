# Developer mode (debug mode)

The developer mode, also known as debug mode, unlocks access to advanced tools
and settings in Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Proceed with caution, as some developer tools and technical settings are considered advanced and
may have associated risks. Only use them if you understand the implications and are confident in
your actions.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The developer mode is also available with <a href="../../developer/reference/frontend/framework_overview#frontend-framework-assets-debug-mode"><span class="std std-ref">assets</span></a>,
which are used to debug JavaScript code, and with <a href="../../developer/reference/frontend/framework_overview#frontend-framework-tests-debug-mode"><span class="std std-ref">tests assets</span></a>, which are used to run test tours.</p>
</div>

## Activation

To activate it, open the **Settings** app, scroll down to the **Developer
Tools** section, and click **Activate the developer mode**.

Once activated, the **Deactivate the developer mode** option becomes
available.

![Activating the developer mode in the Settings
app](../../_images/settings.png)

To activate the developer mode **from anywhere in the database** , add
`?debug=1` to the URL after `/web` (e.g.,
`https://example.odoo.com/web?debug=1#action=menu&cids=1`). To deactivate it,
use `?debug=0` instead.

Use `?debug=assets` to activate the developer mode with assets and
`?debug=tests` to activate it with tests assets.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Open the <b>command palette</b> by pressing <code>Ctrl + K</code> or <code>Cmd ⌘ + K</code>, then type <code>debug</code> to
activate the developer mode with assets or deactivate it.</p>
</div> <div class="admonition-browser-extension alert">
<p class="alert-title">
Browser extension</p><p>The <a href="https://github.com/Droggol/Konvergo ERPDebug">Konvergo ERP Debug</a> browser extension adds an icon to toggle
developer mode on or off from the browser’s toolbar. It is available on the <a href="https://chromewebstore.google.com/detail/odoo-debug/hmdmhilocobgohohpdpolmibjklfgkbi">Chrome Web Store</a> and
<a href="https://addons.mozilla.org/firefox/addon/odoo-debug/">Firefox Add-ons</a>.</p>
</div>

## Developer tools and technical menu

Once the developer mode is activated, the developer tools can be accessed by
clicking the __**(bug)** icon. The menu contains tools useful for
understanding or editing technical data, such as a view’s field, filters, or
actions. The options available depend on where the menu is accessed from.

![Accessing the developer tools](../../_images/tools.png)

Database administrators can access the technical menu from the **Settings**
app. It contains advanced database settings, such as ones related to the
database structure, security, actions, etc.

![Accessing the technical menu](../../_images/technical.png)

