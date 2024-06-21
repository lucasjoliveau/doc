# Razorpay

[Razorpay](https://razorpay.com/) est un fournisseur de paiement en ligne
établi en Inde qui couvre plus de 100 modes de paiement.

## Configuration sur le tableau de bord de Razorpay

  1. Connectez-vous au [tableau de bord de Razorpay](https://dashboard.razorpay.com/) et allez à Paramètres ‣ Clés API. Générez les nouvelles clés et copiez les valeurs des champs **ID clé** et **Secret clé** et enregistrez-les pour plus tard.

  2. Allez à Paramètres ‣ Webhooks, cliquez sur **Créer un nouveau Webhook** et saisissez l’URL de votre base de données Konvergo ERP suivie de `/payment/razorpay/webhook` dans le champ de texte **URL Webhook**.

Par exemple : `https://example.odoo.com/payment/razorpay/webhook`.

  3. Complétez le champ **Secret** avec un mot de passe de votre choix et enregistrez-le pour plus tard.

  4. Assurez-vous de cocher les cases **payment.authorized** , **payment.captured** , **payment.failed** , **refund.failed** et **refund.processed**.

  5. Cliquez sur **Créer un Webhook** pour finaliser la configuration.

## Configuration dans Konvergo ERP

  1. [Allez au fournisseur de paiement Razorpay](../payment_providers#payment-providers-add-new) et définissez son statut sur **Activé**.

  2. Dans l’onglet **Identifiants** , complétez dans les champs **ID clé** , **Clé secret** et **Secret Webhook** les valeurs que vous avez enregistrées à l’étape Configuration sur le tableau de bord de Razorpay.

  3. Configurez les autres options à votre guise.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous configurez Konvergo ERP pour capturer les montants manuellement :</p>
<ul>
<li><p>Assurez-vous que l”<b>annulation manuelle</b> d’une transaction n’est pas prise en charge par Razorpay.</p></li>
<li><p>Si la transaction n’a pas été capturée après <b>cinq jours</b>, elle sera automatiquement <b>annulée</b>.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

