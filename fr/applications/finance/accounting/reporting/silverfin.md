# Intégration Silverfin

[Silverfin](https://www.silverfin.com) est un fournisseur de services tiers
qui propose une plateforme cloud de comptabilité.

Odoo et Silverfin fournissent une intégration pour automatiser la
synchronisation des données.

## Configuration

Pour configurer cette intégration, vous devez saisir les données suivantes
dans votre compte Silverfin :

  * adresse mail de l’utilisateur

  * clé API Odoo

  * URL de la base de données Odoo

  * nom de votre base de données Odoo

### Clé API Odoo

You can create Odoo external API keys either for a single database (hosting:
Odoo Online, On-premise, and Odoo.sh) or for all databases managed by a single
user (hosting: Odoo Online).

Important

  * Ces clés API sont personnelles et fournissent un accès complet à votre compte utilisateur. Conservez-les en toute sécurité.

  * You can copy the API key only at its creation. It is not possible to retrieve it later.

  * Si vous en avez à nouveau besoin, créez une nouvelle clé API (et supprimez l’ancienne).

Pour plus d'infos

[External API](../../../../developer/reference/external_api.html)

#### Per database

To add an API key to a **single** database, connect to the database, enable
the [developer mode](../../../general/developer_mode.html#developer-mode),
click on the user menu, and then My Profile / Preferences. Under the Account
Security tab, click on New API Key, confirm your password, give a descriptive
name to your new key, and copy the API key.

![création d'une clé API externe Odoo pour une base de
données](../../../../_images/api-key-db.png)

Pour plus d'infos

[API Keys](../../../../developer/reference/external_api.html#api-external-api-
keys)

#### For all databases (fiduciaries)

To add an API key to **all** databases managed by a single user at the same
time **(the easiest method for fiduciaries)** , navigate to [Odoo’s
website](https://www.odoo.com) and sign in with your administrator account.
Next, open [your account security settings in developer
mode](https://www.odoo.com/my/security?debug=1), click on New API Key, confirm
your password, give a descriptive name to your new key, and copy the new API
key.

Astuce

Open the [database manager](https://www.odoo.com/my/databases) to view all
databases that will be linked to the single API key.

![création d'une clé API externe Odoo pour un utilisateur
Odoo](../../../../_images/api-key-user.png)

