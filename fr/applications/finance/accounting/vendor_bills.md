# Factures fournisseurs

Dans Konvergo ERP, vous pouvez enregistrer des factures fournisseurs **manuellement**
ou **automatiquement** , tandis que la **Balance âgée des fournisseurs**
fournit une vue d’ensemble de toutes les factures en suspens pour vous aider à
payer les bons montants à temps.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p>Tutoriel <a href="https://www.odoo.com/slides/slide/registering-a-vendor-bill-1683?fullscreen=1">Enregistrer une facture fournisseur</a></p></li>
<li><p><a href="../../inventory_and_mrp/purchase/manage_deals/manage">Gérer des factures fournisseurs</a></p></li>
</ul>
</div>

## Création d’une facture fournisseur

### Manuellement

Créez une facture fournisseur manuellement en allant à Comptabilité ‣
Fournisseurs ‣ Factures fournisseurs et en cliquant sur **Créer**.

### Automatiquement

Les factures fournisseurs peuvent être créées automatiquement par l”**envoi
d’un email** à un [alias
d’email](vendor_bills/invoice_digitization#invoice-digitization-email-
alias) associé au journal des achats ou par le **chargement d’un PDF** dans
Comptabilité ‣ Fournisseurs ‣ Factures fournisseurs, en cliquant sur
**Charger**.

## Remplissage de la facture

Quand la facture est créée manuellement ou automatiquement, assurez-vous que
les champs suivants sont correctement complétés :

  * **Fournisseur** : Konvergo ERP remplit automatiquement certaines informations sur la base des informations enregistrées du fournisseur, des bons d’achat précédents ou des factures précédentes.

  * **Référence de la facture** : ajoutez la référence de la commande qui est fournie par le fournisseur et qui est utilisée pour faire le [lettrage](payments#payments-matching) à la réception des produits.

  * **Saisie automatique** : sélectionnez une facture/bon de commande précédent(e) afin de compléter le document automatiquement. Le champ **Fournisseur** doit être complété avant de remplir ce champ.

  * **Date de facturation** : c’est la date d’émission du document.

  * **Date comptable** : c’est la date à laquelle le document est enregistré dans votre comptabilité.

  * **Référence du paiement** : lors de l’enregistrement du paiement, elle est automatiquement indiquée dans le champ **Mémo**.

  * **Compte bancaire destinataire** : pour indiquer le numéro de compte sur lequel le paiement doit être effectué.

  * **Date d’échéance** ou **Conditions** pour payer la facture.

  * **Journal** : sélectionner le journal dans lequel la facture doit être enregistrée et la [Devise](get_started/multi_currency).

![Complétez la facture fournisseur](../../../_images/bill-completion.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Les factures peuvent être <a href="vendor_bills/invoice_digitization">numérisées</a> pour être complétées automatiquement en cliquant sur <b>Envoyer pour numérisation</b>.</p></li>
<li><p>Si vous chargez la facture, le document PDF s’affiche à la droite de l’écran, vous permettant de remplir facilement les informations de la facture.</p></li>
</ul>
</div>

## Confirmation de la facture

Cliquez sur **Confirmer** une fois que le document est complété. Le statut de
votre document passe à **Comptabilisé** et une écriture comptable est créée
sur la base de la configuration de la facture.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une fois la facture confirmée, il n’est plus possible de la mettre à jour. Cliquez sur <b>Remettre en brouillon</b> si des changements sont requis.</p>
</div>

## Paiement de la facture

Lors du paiement de la facture fournisseur, cliquez sur **Enregistrer un
paiement**. Une nouvelle fenêtre s’ouvre.

Sélectionnez le **Journal** , le **Mode de paiement** , le **Montant** que
vous voulez payer (paiement total ou partiel) et la **Devise**. Konvergo ERP remplit
le champ **Mémo** automatiquement si la **Référence du paiement** a été
correctement définie sur la facture fournisseur. Si le champ est vide, nous
vous recommandons de sélectionner le numéro de la facture fournisseur en tant
que référence.

Après la confirmation, une bannière **En paiement** apparaît sur la facture
jusqu’à ce qu’elle est [rapprochée](bank/reconciliation).

## Balance âgée des fournisseurs

Pour avoir une vue d’ensemble de vos factures fournisseurs impayées et leurs
dates d’échéance, vous pouvez utiliser la **Balance âgée des fournisseurs**.
Allez à Comptabilité ‣ Analyse ‣ Rapports des partenaires : Balance âgée des
fournisseurs.

Cliquez sur le nom d’un fournisseur pour afficher les détails de toutes les
factures impayées, les montants dus, les dates d’échéance, etc.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>En cliquant sur le bouton <b>Enregistrer</b>, vous pouvez exporter les informations disponibles sur l’écran au format PDF ou XLSX et les enregistrer dans le dossier de votre choix.</p></li>
<li><p>Il se peut que vous receviez plusieurs factures pour le même bon de commande si votre fournisseur est en reliquat et vous envoie des factures au fur et à mesure de l’expédition des produits ou si votre fournisseur vous envoie une facture partielle ou vous demande un acompte.</p></li>
</ul>
</div>

  * [Numérisation de documents assistée par IA](vendor_bills/invoice_digitization)
  * [Actifs immobilisés et immobilisations](vendor_bills/assets)
  * [Charges constatées d’avance et acomptes](vendor_bills/deferred_expenses)

