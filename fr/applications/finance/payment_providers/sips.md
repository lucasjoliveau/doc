# SIPS

[SIPS](https://sips.worldline.com/) est une solution de paiement en ligne de
la multinationale Worldline.

## Configuration

Pour plus d'infos

  * [Enable a payment provider](../payment_providers.html#payment-providers-add-new)

### Onglet des identifiants

Odoo a besoin de vos **identifiants API** pour se connecter à votre compte
SIPS. Ils incluent :

  * **Identifiant du marchand** : L’identifiant utilisé uniquement pour identifier le compte marchand auprès de SIPS.

  * **Clé secrète** : La clé pour signer le compte marchand avec SIPS.

  * **Version clé secrète** : La version de la clé, préremplie.

  * **Version Interface** : Préremplie, ne la modifiez pas.

Vous pouvez copier vos identifiants à partir de la documentation
d’informations sur votre environnement SIPS, dans la section **PROD** , et les
coller dans les champs associés dans l’onglet **Identifiants**.

Important

Si vous testez SIPS avec les informations d’identification _TEST_ , définissez
le **Statut** sur _Mode test_. Nous vous recommandons de le faire sur une base
de données de test Odoo, plutôt que sur votre base de données principale.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

