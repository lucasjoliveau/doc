# Factures fournisseurs

Dans Odoo, vous pouvez enregistrer des factures fournisseurs **manuellement**
ou **automatiquement** , tandis que la **Balance âgée des fournisseurs**
fournit une vue d’ensemble de toutes les factures en suspens pour vous aider à
payer les bons montants à temps.

Pour plus d'infos

  * Tutoriel [Enregistrer une facture fournisseur](https://www.odoo.com/slides/slide/registering-a-vendor-bill-1683?fullscreen=1)

  * [Gérer des factures fournisseurs](../../inventory_and_mrp/purchase/manage_deals/manage.html)

## Création d’une facture fournisseur

### Manuellement

Créez une facture fournisseur manuellement en allant à Comptabilité ‣
Fournisseurs ‣ Factures fournisseurs et en cliquant sur Créer.

### Automatiquement

Les factures fournisseurs peuvent être créées automatiquement par l”**envoi
d’un email** à un [alias
d’email](vendor_bills/invoice_digitization.html#invoice-digitization-email-
alias) associé au journal des achats ou par le **chargement d’un PDF** dans
Comptabilité ‣ Fournisseurs ‣ Factures fournisseurs, en cliquant sur Charger.

## Remplissage de la facture

Quand la facture est créée manuellement ou automatiquement, assurez-vous que
les champs suivants sont correctement complétés :

  * Fournisseur : Odoo remplit automatiquement certaines informations sur la base des informations enregistrées du fournisseur, des bons d’achat précédents ou des factures précédentes.

  * Référence de la facture : ajoutez la référence de la commande qui est fournie par le fournisseur et qui est utilisée pour faire le [lettrage](payments.html#payments-matching) à la réception des produits.

  * Saisie automatique : sélectionnez une facture/bon de commande précédent(e) afin de compléter le document automatiquement. Le champ Fournisseur doit être complété avant de remplir ce champ.

  * Date de facturation : c’est la date d’émission du document.

  * Date comptable : c’est la date à laquelle le document est enregistré dans votre comptabilité.

  * Référence du paiement : lors de l’enregistrement du paiement, elle est automatiquement indiquée dans le champ Mémo.

  * Compte bancaire destinataire : pour indiquer le numéro de compte sur lequel le paiement doit être effectué.

  * Date d’échéance ou Conditions pour payer la facture.

  * Journal : sélectionner le journal dans lequel la facture doit être enregistrée et la [Devise](get_started/multi_currency.html).

![Complétez la facture fournisseur](../../../_images/bill-completion.png)

Note

  * Les factures peuvent être [numérisées](vendor_bills/invoice_digitization.html) pour être complétées automatiquement en cliquant sur Envoyer pour numérisation.

  * Si vous chargez la facture, le document PDF s’affiche à la droite de l’écran, vous permettant de remplir facilement les informations de la facture.

## Confirmation de la facture

Cliquez sur Confirmer une fois que le document est complété. Le statut de
votre document passe à Comptabilisé et une écriture comptable est créée sur la
base de la configuration de la facture.

Note

Une fois la facture confirmée, il n’est plus possible de la mettre à jour.
Cliquez sur Remettre en brouillon si des changements sont requis.

## Paiement de la facture

Lors du paiement de la facture fournisseur, cliquez sur Enregistrer un
paiement. Une nouvelle fenêtre s’ouvre.

Sélectionnez le Journal, le Mode de paiement, le Montant que vous voulez payer
(paiement total ou partiel) et la Devise. Odoo remplit le champ Mémo
automatiquement si la Référence du paiement a été correctement définie sur la
facture fournisseur. Si le champ est vide, nous vous recommandons de
sélectionner le numéro de la facture fournisseur en tant que référence.

Après la confirmation, une bannière En paiement apparaît sur la facture
jusqu’à ce qu’elle est [rapprochée](bank/reconciliation.html).

## Balance âgée des fournisseurs

Pour avoir une vue d’ensemble de vos factures fournisseurs impayées et leurs
dates d’échéance, vous pouvez utiliser la **Balance âgée des fournisseurs**.
Allez à Comptabilité ‣ Analyse ‣ Rapports des partenaires : Balance âgée des
fournisseurs.

Cliquez sur le nom d’un fournisseur pour afficher les détails de toutes les
factures impayées, les montants dus, les dates d’échéance, etc.

Note

  * En cliquant sur le bouton Enregistrer, vous pouvez exporter les informations disponibles sur l’écran au format PDF ou XLSX et les enregistrer dans le dossier de votre choix.

  * Il se peut que vous receviez plusieurs factures pour le même bon de commande si votre fournisseur est en reliquat et vous envoie des factures au fur et à mesure de l’expédition des produits ou si votre fournisseur vous envoie une facture partielle ou vous demande un acompte.

  * [Numérisation de documents assistée par IA](vendor_bills/invoice_digitization.html)
  * [Actifs immobilisés et immobilisations](vendor_bills/assets.html)
  * [Charges constatées d’avance et acomptes](vendor_bills/deferred_expenses.html)

