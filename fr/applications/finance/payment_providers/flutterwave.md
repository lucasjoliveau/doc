# Flutterwave

[Flutterwave](https://flutterwave.com/) est un fournisseur de paiement en
ligne établi au Nigéria qui couvre plusieurs pays africains et modes de
paiement.

## Configuration sur le tableau de bord Flutterwave

  1. Connectez-vous au [tableau de bord Flutterwave](https://dashboard.flutterwave.com/) et allez à Paramètres ‣ API. Copiez les valeurs des champs **Clé publique** et **Clé secrète** et enregistrez-les pour plus tard.

  2. Allez à Paramètres ‣ Webhooks et saisissez l’URL de votre base de données Konvergo ERP suivie de `/payment/flutterwave/webhook` dans le champ de texte **URL**.

Par exemple : `https://yourcompany.odoo.com/payment/flutterwave/webhook`.

  3. Complétez le **Hachage secret** avec un mot de passe que vous générez et enregistrez sa valeur pour plus tard.

  4. Assurez-vous que _toutes_ les autres cases sont cochées.

  5. Cliquez sur **Enregistrer** pour finaliser la configuration.

![Paramètres Flutterwave](../../../_images/flutterwave-settings.png)

## Configuration dans Konvergo ERP

  1. [Allez au fournisseur de paiement Flutterwave](../payment_providers#payment-providers-add-new) et définissez son statut sur **Activé**.

  2. Dans l’onglet **Identifiants** , complétez dans les champs **Clé publique** , **Clé secrète** et **Secret Webhook** les valeurs que vous avez enregistrées à l’étape Configuration sur le tableau de bord Flutterwave.

  3. Configurez les autres options à votre guise.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous choisissez d’autoriser l’enregistrement des modes de paiement, il est recommandé de n’activer que les paiements par carte à partir du tableau de bord Flutterwave, car seules les cartes peuvent être enregistrées en tant que jetons de paiement. Pour ce faire, allez à votre tableau de bord Flutterwave et ensuite à Paramètres ‣ Paramètres du compte.</p>
</div>

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

