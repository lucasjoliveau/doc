# Virements bancaires

Le mode de paiement **Virement bancaire** vous permet de fournir des
instructions de paiement à vos clients, telles que les coordonnées bancaires
et la communication. Elles s’affichent :

  * à la fin du processus de paiement, une fois que le client a sélectionné **Virement bancaire** en tant que mode de paiement et a cliqué sur le bouton **Payer maintenant** :

![Instructions de paiement lors du passage en
caisse](../../../_images/payment_instructions_checkout.png)

  * sur le portail client :

![Instructions de paiement sur le portail
client](../../../_images/payment_instructions_portal.png)

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Bien que ce mode soit très accessible et ne nécessite qu’une configuration minimale, il est très inefficace du point de vue du processus. Nous recommandons plutôt de mettre en place un <a href="../payment_providers">fournisseur de paiement</a>.</p></li>
<li><p>Les commandes en ligne restent au stade du <b>Devis envoyé</b> (c’est-à-dire de la commande non payée) jusqu’à ce que vous receviez le paiement et que vous <b>confirmiez</b> la commande.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Le <b>virement bancaire</b> peut aussi être utilisé comme un modèle pour d’autres modes de paiement traités manuellement, tels que les chèques, en le renommant ou en le dupliquant.</p>
</div>

## Configuration

Pour configurer le **virement bancaire** , allez à Comptabilité / Site Web ‣
Configuration ‣ Fournisseurs de paiement et ouvrez la carte **Virement
bancaire**. Ensuite, dans l’onglet **Configuration** :

  * Sélectionnez la **Communication** à utiliser ;

    * **Basé sur la référence du document** : numéro du bon de commande ou de la facture

    * **Basé sur l’ID client** : l’identifiant du client

  * Cochez la case **Activer les codes QR** pour activer les [paiements par code QR](../accounting/customer_invoices/epc_qr_code).

Définissez les instructions de paiement dans l’onglet **Messages** :

![Définissez les instructions de
paiement](../../../_images/payment_instructions.png)

Si vous avez déjà défini [un compte bancaire](../accounting/bank), le
numéro du compte sera automatiquement ajouté au message par défaut généré par
Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers#payment-providers-journal"><span class="std std-ref">Journal des paiements</span></a></p>
</div>

