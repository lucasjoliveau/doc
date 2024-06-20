# Virements bancaires

Le mode de paiement **Virement bancaire** vous permet de fournir des
instructions de paiement à vos clients, telles que les coordonnées bancaires
et la communication. Elles s’affichent :

  * à la fin du processus de paiement, une fois que le client a sélectionné Virement bancaire en tant que mode de paiement et a cliqué sur le bouton Payer maintenant :

![Instructions de paiement lors du passage en
caisse](../../../_images/payment_instructions_checkout.png)

  * sur le portail client :

![Instructions de paiement sur le portail
client](../../../_images/payment_instructions_portal.png)

Note

  * Bien que ce mode soit très accessible et ne nécessite qu’une configuration minimale, il est très inefficace du point de vue du processus. Nous recommandons plutôt de mettre en place un [fournisseur de paiement](../payment_providers.html).

  * Les commandes en ligne restent au stade du Devis envoyé (c’est-à-dire de la commande non payée) jusqu’à ce que vous receviez le paiement et que vous confirmiez la commande.

Astuce

Le **virement bancaire** peut aussi être utilisé comme un modèle pour d’autres
modes de paiement traités manuellement, tels que les chèques, en le renommant
ou en le dupliquant.

## Configuration

Pour configurer le **virement bancaire** , allez à Comptabilité / Site Web ‣
Configuration ‣ Fournisseurs de paiement et ouvrez la carte Virement bancaire.
Ensuite, dans l’onglet Configuration :

  * Sélectionnez la Communication à utiliser ;

    * Basé sur la référence du document : numéro du bon de commande ou de la facture

    * Basé sur l’ID client : l’identifiant du client

  * Cochez la case Activer les codes QR pour activer les [paiements par code QR](../accounting/customer_invoices/epc_qr_code.html).

Définissez les instructions de paiement dans l’onglet Messages :

![Définissez les instructions de
paiement](../../../_images/payment_instructions.png)

Si vous avez déjà défini [un compte bancaire](../accounting/bank.html), le
numéro du compte sera automatiquement ajouté au message par défaut généré par
Odoo.

Pour plus d'infos

[Journal des paiements](../payment_providers.html#payment-providers-journal)

