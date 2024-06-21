# Démo

Le **fournisseur de paiement Démo** d’Konvergo ERP vous permet de tester les flux
commerciaux impliquant des transactions en ligne sans exiger de véritables
identifiants bancaires.

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Définissez le statut sur <b>Mode test</b>.</p>
</div>

## Résultat du paiement

Au moment de passer à la caisse ou de payer une facture en ligne, vous pouvez
sélectionner le résultat du paiement lorsque vous utilisez le fournisseur de
service Démo. Pour ce faire, cliquez sur le menu déroulant **Statut du
paiement** et sélectionnez le résultat souhaité.

![Résultats de paiement.](../../../_images/demo-payment-outcome.png)

## Statut de la transaction

Si vous sélectionnez **En attente** en tant que **Résultat du paiement** ,
vous pouvez modifier le statut de la transaction directement dans la vue
formulaire. Pour accéder à la vue formulaire de la transaction, activez le
[mode développeur](../../general/developer_mode#developer-mode) et allez
à Comptabilité / Site Web ‣ Configuration ‣ Transactions de paiement. Ensuite,
modifiez le statut d’une transaction en cliquant sur la barre de statut
(**Brouillon, En attente, Autorisé, Confirmé, Annulé, Erreur**).

![Barre de statut de la transaction.](../../../_images/demo-view-form.png)

