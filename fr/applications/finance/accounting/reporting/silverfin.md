# Intégration Silverfin

[Silverfin](https://www.silverfin.com) est un fournisseur de services tiers
qui propose une plateforme cloud de comptabilité.

Konvergo ERP et Silverfin fournissent une intégration pour automatiser la
synchronisation des données.

## Configuration

Pour configurer cette intégration, vous devez saisir les données suivantes
dans votre compte Silverfin :

  * adresse mail de l’utilisateur

  * clé API Konvergo ERP

  * URL de la base de données Konvergo ERP

  * nom de votre base de données Konvergo ERP

### Clé API Konvergo ERP

You can create Konvergo ERP external API keys either for a single database (hosting:
Konvergo ERP Online, On-premise, and Konvergo ERP.sh) or for all databases managed by a single
user (hosting: Konvergo ERP Online).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Ces clés API sont personnelles et fournissent un accès complet à votre compte utilisateur. Conservez-les en toute sécurité.</p></li>
<li><p>You can copy the API key only at its creation. It is not possible to retrieve it later.</p></li>
<li><p>Si vous en avez à nouveau besoin, créez une nouvelle clé API (et supprimez l’ancienne).</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../developer/reference/external_api">External API</a></p>
</div>

#### Per database

To add an API key to a **single** database, connect to the database, enable
the [developer mode](../../../general/developer_mode#developer-mode),
click on the user menu, and then **My Profile** / **Preferences**. Under the
**Account Security** tab, click on **New API Key** , confirm your password,
give a descriptive name to your new key, and copy the API key.

![création d'une clé API externe Konvergo ERP pour une base de
données](../../../../_images/api-key-db.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../../developer/reference/external_api#api-external-api-keys"><span class="std std-ref">API Keys</span></a></p>
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
Astuce</p><p>Open the <a href="https://www.odoo.com/my/databases">database manager</a> to view all databases that will
be linked to the single API key.</p>
</div> ![création d'une clé API externe Konvergo ERP pour un utilisateur
Konvergo ERP](../../../../_images/api-key-user.png)

