# Payer par chèque

Lorsque vous décidez de payer une facture fournisseur, vous pouvez choisir de
payer par chèque. Vous pouvez ensuite imprimer tous les paiements enregistrés
par chèque. Enfin, le processus de rapprochement bancaire fera correspondre
les chèques que vous avez envoyés aux fournisseurs avec les relevés bancaires
effectifs.

## Configuration

### Activer le mode de paiement par chèque

To activate the checks payment method, go to Accounting ‣ Configuration ‣
Settings, and scroll down to the **Vendor Payments** section. There, you can
activate the payment method as well as set up the **Check Layout**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Once the <b>Checks</b> setting is activated, the <b>Checks</b> payment method is
automatically set up in the <b>Outgoing Payments</b> tabs of <b>bank</b> journals.</p></li>
<li><p>Certains pays exigent des modules spécifiques pour imprimer des chèques : ces modules peuvent être installés par défaut. Par exemple, le module <b>Format de chèques US</b> est nécessaire pour imprimer des chèques américains.</p></li>
</ul>
</div>

## Papier à chèque compatible pour l’impression de chèques

### États-Unis

Pour les États-Unis, Konvergo ERP prend en charge par défaut les formats de chèques
suivants :

  * **Quickbooks & Quicken** : chèque en haut, talons au milieu et en bas ;

  * **Peachtree** : chèque au milieu, talons en haut et en bas ;

  * **ADP®** : chèque en bas et talons en haut.

## Payer une facture fournisseur par chèque

Le paiement d’un fournisseur par chèque se fait en trois étapes :

  1. l’enregistrement du paiement

  2. l’impression des chèques par lot pour tous les paiements enregistrés

  3. le rapprochement des relevés bancaires

### Enregistrer un paiement par chèque

Pour enregistrer un paiement, ouvrez une facture fournisseur dans le menu
Achats ‣ Factures fournisseurs. Une fois que la facture fournisseur est
validée, vous pouvez enregistrer un paiement. Définissez le **Mode de
paiement** sur **Chèques** et validez le paiement.

### Imprimer des chèques

Sur votre **Tableau de bord de Comptabilité** dans le Journal **Banque** ,
vous pouvez voir le nombre de chèques enregistrés. En cliquant sur **Chèques à
imprimer** , vous avez la possibilité d’imprimer les chèques rapprochés.

Pour regrouper l’impression des chèques par lot, sélectionnez tous les
paiements dans la vue de liste et cliquez sur **Imprimer**.

