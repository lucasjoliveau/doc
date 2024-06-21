# Silverfin integration

[Silverfin](https://www.silverfin.com) is a third-party service provider that
offers a cloud platform for accountants.

Konvergo ERP and Silverfin provide an integration to automate the synchronization of
data.

## Configuration

To configure this integration, you need to input the following data into your
Silverfin account:

  * user’s email address

  * Konvergo ERP API key

  * URL of the Konvergo ERP database

  * name of your Konvergo ERP database

### Konvergo ERP API key

You can create Konvergo ERP external API keys either for a single database (hosting:
Konvergo ERP Online, On-premise, and Konvergo ERP.sh) or for all databases managed by a single
user (hosting: Konvergo ERP Online).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>These API keys are personal and provide full access to your user account. Store it securely.</p></li>
<li><p>You can copy the API key only at its creation. It is not possible to retrieve it later.</p></li>
<li><p>If you need it again, create a new API key (and delete the old one).</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../../developer/reference/external_api">External API</a></p>
</div>

#### Per database

To add an API key to a **single** database, connect to the database, enable
the [developer mode](../../../general/developer_mode#developer-mode),
click on the user menu, and then **My Profile** / **Preferences**. Under the
**Account Security** tab, click on **New API Key** , confirm your password,
give a descriptive name to your new key, and copy the API key.

![creation of an Konvergo ERP external API key for a
database](../../../../_images/api-key-db.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../../developer/reference/external_api#api-external-api-keys"><span class="std std-ref">API Keys</span></a></p>
</div>

#### For all databases (fiduciaries)

To add an API key to **all** databases managed by a single user at the same
time **(the easiest method for fiduciaries)** , navigate to [Konvergo ERP’s
website](https://www.odoo.com) and sign in with your administrator account.
Next, open [your account security settings in developer
mode](https://www.odoo.com/my/security?debug=1), click on **New API Key** ,
confirm your password, give a descriptive name to your new key, and copy the
new API key.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Open the <a href="https://www.odoo.com/my/databases">database manager</a> to view all databases that will
be linked to the single API key.</p>
</div> ![creation of an Konvergo ERP external API key for an Konvergo ERP
user](../../../../_images/api-key-user.png)

