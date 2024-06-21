# Reçus et factures

## Réceptions

Configurez les reçus en allant à Point de Vente ‣ Configuration ‣ Point de
Vente, en sélectionnant un Point de vente et en allant à la section **Factures
& Reçus**.

Pour **personnaliser** l”**en-tête** et le **pied de page** , activez **En-
tête & Pied de page** et complétez les informations à imprimer sur les reçus
dans les deux champs.

Pour **imprimer les reçus** automatiquement après l’enregistrement du
paiement, activez le paramètre **Impression automatique du reçu**.

![Reçu du Point de Vente](../../../_images/receipt.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="restaurant/bill_printing">Factures fournisseurs</a></p></li>
<li><p><a href="configuration/epos_printers">ePOS printers</a></p></li>
</ul>
</div>

### Réimprimer un reçu

Depuis l’interface du point de vente, cliquez sur **Commandes** , ouvrez le
menu déroulant à côté de la barre de recherche et changez le filtre **Toutes
les commandes actives** par défaut en **Payé**. Sélectionnez ensuite la
commande correspondante et cliquez sur **Imprimer le ticket**.

![Bouton d'impression du reçu depuis le backend](../../../_images/print-
receipt.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez filtrer la liste des commandes en utilisant la barre de recherche. Tapez votre référence et cliquez sur <b>Numéro de reçu</b>, <b>Date</b>, ou <b>Client</b>.</p>
</div>

## Factures clients

Point de Vente vous permet d’émettre et d’imprimer des factures pour les
[clients enregistrés](../point_of_sale#pos-customers) lors du paiement et
de récupérer toutes les commandes facturées antérieurement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Toute facture créée dans un PdV crée une écriture dans le <a href="../../finance/accounting/get_started/cheat_sheet#cheat-sheet-journals"><span class="std std-ref">journal comptable</span></a> correspondant, précédemment <a href="#receipts-invoices-invoice-configuration"><span class="std std-ref">configuré</span></a>.</p>
</div>

### Configuration

Pour définir les journaux que vous utiliserez pour un PdV spécifique, allez
aux paramètres du [PdV”](configuration#configuration-settings) et faites
défiler jusqu’à la section de la comptabilité. Ensuite, vous pouvez déterminer
les journaux comptables utilisés par défaut pour les commandes et les factures
dans la section **Journaux par défaut**.

![section comptabilité dans les paramètres du point de
vente](../../../_images/invoice-config.png)

### Facturer un client

Lors du traitement d’un paiement, cliquez sur **Facture** en dessous du nom du
client afin d’émettre une facture pour cette commande.

Sélectionnez le mode de paiement et cliquez sur **Valider**. La **facture**
est automatiquement émise et prête à être téléchargée et/ou imprimée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour pouvoir émettre une facture, vous devez sélectionner un <a href="../point_of_sale#pos-customers"><span class="std std-ref">client</span></a>.</p>
</div>

### Récupérer des factures

Pour récupérer des factures à partir du **tableau de bord du PdV** ,

  1. accédez à toutes les commandes passées par votre Point de vente en allant au Point de vente ‣ Commandes ‣ Commandes;

  2. pour accéder à la facture d’une commande, ouvrez le **formulaire de commande** en sélectionnant la commande, puis cliquez sur **Facture**.

![bouton intelligent de facture sur un formulaire de
commande](../../../_images/invoice-smart-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Les <b>Commandes facturées</b> peuvent être identifiées par le statut <b>Facturé</b> dans la colonne <b>Statut</b>.</p></li>
<li><p>Vous pouvez filtrer la liste des commandes sur les commandes facturées en cliquant sur <b>Filtres</b> et <b>Facturé</b>.</p></li>
</ul>
</div>

### Codes QR pour générer des factures

Les clients peuvent également demander une facture en scannant le **Code QR**
imprimé sur leur reçu. Après avoir scanné leur code, ils doivent remplir un
formulaire avec leurs informations de facturation et cliquer sur **Obtenir ma
facture**. D’une part, cette opération génère une facture téléchargeable.
D’autre part, le statut de la commande passe de **Payé** ou **Comptabilisé** à
**Facturé** dans le backend d’Konvergo ERP.

![Changement du statut de la commande](../../../_images/order-status.png)

Pour utiliser cette fonctionnalité, vous devez activer les codes QR sur les
reçus en allant à Point de Vente ‣ Configuration ‣ Paramètres. Sélectionnez
ensuite le point de vente dans le champ **Point de vente** , allez jusqu’à la
section the **Factures & Reçus** et activez la fonctionnalité **Utiliser un
code QR sur le ticket**.

