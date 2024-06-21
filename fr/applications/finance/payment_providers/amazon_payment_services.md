# Amazon Payment Services

[Amazon Payment Services](https://paymentservices.amazon.com/) ou APS est un
fournisseur de paiement en ligne établi à Dubaï qui propose plusieurs options
de paiement en ligne.

## Configuration sur le tableau de bord APS

  1. Connectez-vous à votre [tableau de bord Amazon Payment Services](https://fort.payfort.com/) et allez aux Paramètres d’intégration ‣ Paramètres de sécurité. Générez le **Code d’accès** si aucun n’a encore été généré. Copiez les valeurs des champs **Identifiant marchand** , **Code d’accès** , **Phrase de demande SHA** et **Phrase de réponse SHA** et enregistrez-les pour plus tard.

  2. Saisissez l’URL de votre base de données Konvergo ERP dans l” **URL d’origine** , par exemple : `https://yourcompany.odoo.com/`. Puis, cliquez sur **Enregistrer les changements**.

  3. Allez aux Paramètres d’intégration ‣ Paramètres techniques et cliquez sur **Redirection**. Assurez-vous que le **Statut** est `Actif` et sélectionnez vos modes de paiement préférés dans **Options de paiement**.

  4. Définissez l’option **Envoyer les paramètres de réponse** sur **Oui** et saisissez l’URL de votre base de données suivi de `/payment/aps/return` dans l”**URL de redirection**.

Par exemple `https://yourcompany.odoo.com/payment/aps/return`.

Saisissez l’URL de votre base de données suivie de `/payment/aps/webhook` dans
les champs **Feedback de transaction** et **URL de notification**.

Par exemple `https://yourcompany.odoo.com/payment/aps/webhook`.

Cliquez sur **Enregistrer les changements**.

  5. Dans Paramètres d’intégration ‣ Modèle de page de paiement, vous pouvez personnaliser l’aspect de la page de paiement d’Amazon Payment Services (où les clients remplissent les détails de leur carte de crédit lors du paiement).

## Configuration dans Konvergo ERP

  1. [Allez au fournisseur de paiement Amazon Payment Services](../payment_providers#payment-providers-add-new), définissez son statut sur **Activé** et assurez-vous qu’il est **Publié**.

  2. Dans l’onglet **Identifiants** , complétez dans les champs **Identifiant Marchand** , **Code d’accès** , **Phrase de demande SHA** et **Phrase de réponse SHA** les valeurs que vous avez enregistrées à l’étape Configuration sur le tableau de bord APS.

  3. Configurez les autres options à votre guise.

