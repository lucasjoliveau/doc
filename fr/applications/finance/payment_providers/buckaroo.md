# Buckaroo

[Buckaroo](https://www.buckaroo.eu/) est une société basée aux Pays-Bas qui
propose plusieurs possibilités de paiement en ligne.

## Configuration sur Buckaroo Plaza

  1. Connectez-vous à [Buckaroo Plaza](https://plaza.buckaroo.nl), allez à Mon Buckaroo ‣ Sites web et sélectionnez l’onglet **Paramètres push**.

  2. Cochez la case **Activer les réponses push** dans la section **Réponses push et tardives**.

  3. Saisissez l’URL de votre base de données Konvergo ERP suivie de `/payment/buckaroo/webhook` dans les champs de texte **Push URI Réussite/En attente** et **Push URI Échec**. Par exemple `https://yourcompany.odoo.com/payment/buckaroo/webhook`.

  4. Ne modifiez pas les autres champs et cliquez sur **Enregistrer**.

  5. Dans l’onglet **Général** , copiez la **Clé** du site web (c’est-à-dire, la clé utilisée pour identifier uniquement votre site web avec Buckaroo) et enregistrez-la pour plus tard.

  6. Allez à Configuration ‣ Sécurité ‣ Clé secrète, saisissez ou **générez** une **Clé secrète** et cliquez sur **Enregistrer**. Enregistrez la clé pour plus tard.

## Configuration dans Konvergo ERP

  1. [Allez au fournisseur de paiement Buckaroo](../payment_providers#payment-providers-add-new) et définissez son statut sur **Activé**.

  2. Dans l’onglet **Identifiants** , complétez dans les champs **Clé du site web** et **Clé secrète** les valeurs que vous avez enregistrées à l’étape Configuration sur Buckaroo Plaza.

  3. Configurez les options dans les autres onglets à votre guise.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers">Paiements en ligne</a></p>
</div>

