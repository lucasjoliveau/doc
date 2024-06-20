# Razorpay

[Razorpay](https://razorpay.com/) est un fournisseur de paiement en ligne
établi en Inde qui couvre plus de 100 modes de paiement.

## Configuration sur le tableau de bord de Razorpay

  1. Connectez-vous au [tableau de bord de Razorpay](https://dashboard.razorpay.com/) et allez à Paramètres ‣ Clés API. Générez les nouvelles clés et copiez les valeurs des champs ID clé et Secret clé et enregistrez-les pour plus tard.

  2. Allez à Paramètres ‣ Webhooks, cliquez sur Créer un nouveau Webhook et saisissez l’URL de votre base de données Odoo suivie de `/payment/razorpay/webhook` dans le champ de texte URL Webhook.

Par exemple : `https://example.odoo.com/payment/razorpay/webhook`.

  3. Complétez le champ Secret avec un mot de passe de votre choix et enregistrez-le pour plus tard.

  4. Assurez-vous de cocher les cases payment.authorized, payment.captured, payment.failed, refund.failed et refund.processed.

  5. Cliquez sur Créer un Webhook pour finaliser la configuration.

## Configuration dans Odoo

  1. [Allez au fournisseur de paiement Razorpay](../payment_providers.html#payment-providers-add-new) et définissez son statut sur Activé.

  2. Dans l’onglet Identifiants, complétez dans les champs ID clé, Clé secret et Secret Webhook les valeurs que vous avez enregistrées à l’étape Configuration sur le tableau de bord de Razorpay.

  3. Configurez les autres options à votre guise.

Important

Si vous configurez Odoo pour capturer les montants manuellement :

  * Assurez-vous que l”**annulation manuelle** d’une transaction n’est pas prise en charge par Razorpay.

  * Si la transaction n’a pas été capturée après **cinq jours** , elle sera automatiquement **annulée**.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

