# Mollie

[Mollie](https://www.mollie.com/) est une plateforme de paiement en ligne
établie aux Pays-Bas.

## Configuration

Pour plus d'infos

  * [Enable a payment provider](../payment_providers.html#payment-providers-add-new)

### Onglet des identifiants

Odoo a besoin de vos **identifiants API** pour se connecter à votre compte
Mollie, qui incluent :

  * **Clé API** : La Clé API test ou live selon la configuration du fournisseur.

Vous pouvez copier vos identifiants depuis votre compte Mollie et les coller
dans les champs associés dans l’onglet **Identifiants**.

Pour récupérer votre clé API, connectez-vous à votre compte Mollie, accédez à
Développeurs‣ Clés API, et copiez votre **Clé API** Test ou Live.

Important

Si vous testez Mollie, avec la clé API de test, définissez le **Statut** sur
_Mode test_. Nous vous recommandons de le faire sur une base de données Odoo
de test, plutôt que sur votre base de données principale.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

