# Alipay

[Alipay](https://www.alipay.com/) est une plateforme de paiement en ligne
établie en Chine par le groupe Alibaba.

Avertissement

Le fournisseur Alipay est obsolète. Nous vous recommandons d’utiliser plutôt
[AsiaPay](asiapay.html).

## Configuration

Pour plus d'infos

  * [Enable a payment provider](../payment_providers.html#payment-providers-add-new)

### Onglet des identifiants

Odoo a besoin de vos **identifiants API** pour se connecter à votre compte
Alipay. Ils incluent :

  * **Compte** : Selon l’endroit où vous vous trouvez - `Paiement rapide` si vous êtes un marchand chinois. - `Transfrontalier` si vous ne l’êtes pas.

  * **Email du vendeur Alipay** : L’adresse email publique de votre partenaire Alipay (pour le paiement rapide uniquement).

  * **ID Partenaire Marchand** : L’identifiant du partenaire public uniquement utilisé pour identifier le compte auprès d’Alipay.

  * **Clé de signature MD5** : La clé de signature.

Vous pouvez copier vos identifiants depuis votre compte Alipay et les coller
dans les champs associés dans l’onglet **Identifiants**.

Pour les récupérer, connectez-vous à votre compte Alipay, ils sont en première
page.

Important

Si vous testez Alipay, dans le _sandbox_ , changez le **statut** en _Mode
test_. Nous vous recommandons de le faire sur une base de données de test
Odoo, plutôt que sur votre base de données principale.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

