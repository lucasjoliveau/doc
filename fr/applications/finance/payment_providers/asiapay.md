# AsiaPay

[AsiaPay](https://www.asiapay.com/) est un fournisseur de paiement en ligne
établi à Hong Kong qui couvre plusieurs pays asiatiques et modes de paiement.

## Configuration sur le tableau de bord d’AsiaPay

  1. Connectez-vous au [tableau de bord d’AsiaPay](https://www.paydollar.com/b2c2/eng/merchant/index.jsp) et allez à Profil ‣ Informations du compte. Copiez les valeurs des champs **Devise** et **Hachage de sécurité** et enregistrez-les pour plus tard.

  2. Allez à Profil ‣ Paramètres du compte de paiement et activez les options **Lien de valeur de retour (Datefeed)**.

Saisissez l’URL de votre base de données Konvergo ERP suivie de
`/payment/asiapay/webhook` dans le champ de texte **Lien de valeur de retour
(Datefeed)**.

Par exemple : `https://yourcompany.odoo.com/payment/asiapay/webhook`.

Cliquez sur **Test** pour vérifier si le webhook fonctionne convenablement.

  3. Cliquez sur **Mettre à jour** pour finaliser la configuration.

## Configuration dans Konvergo ERP

  1. [Allez au fournisseur de paiement AsiaPay](../payment_providers#payment-providers-add-new) et définissez son statut sur **Activé**.

  2. Dans l’onglet **Identifiants** , complétez dans les champs **Identifiant marchand** , **Devise** et **Secret de hachage de sécurité** les valeurs que vous avez enregistrées à l’étape Configuration sur le tableau de bord d’AsiaPay.

Par défaut, le fournisseur de paiement AsiaPay est configuré pour vérifier le
secret de hachage avec la fonction de hachage `SHA1`. Si une fonction
différente est définie sur votre compte, activez le [mode
développeur](../../general/developer_mode#developer-mode) et saisissez la
même valeur dans le champ **Fonction de hachage de sécurité** dans Konvergo ERP.

  3. Configurez les autres options à votre guise.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

