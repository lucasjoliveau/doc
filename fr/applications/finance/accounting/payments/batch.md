# Paiements par lot par dépôt bancaire

Un **dépôt par lot** est un moyen pratique de regrouper les paiements des
clients et de les déposer sur votre compte bancaire. La fonctionnalité vous
permet de répertorier plusieurs paiements et de générer un bordereau de dépôt
détaillé avec une référence de lot. Cette référence peut être utilisée lors du
rapprochement pour faire correspondre les lignes du relevé bancaire avec les
transactions du dépôt par lot.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Paiements clients et
cochez **Paiements par lot** pour activer la fonctionnalité.

## Déposer plusieurs paiements dans un lot

### Enregistrer les paiements

Avant d’effectuer un dépôt par lot, il est nécessaire d’enregistement le
paiement de chaque transaction. Pour ce faire, ouvrez la facture client
concernée et cliquez sur **Enregistrer un paiement**. Dans la fenêtre
contextuelle, sélectionnez le **Journal** lié à votre compte bancaire et
**Dépôt par lot** comme **Mode de paiement** , et cliquez sur **Créer un
paiement**.

![L'enregistrement d'un paiement client dans le cadre d'un dépôt par
lot](../../../../_images/batch-payments.png)

### Ajouter des paiements à un dépôt par lot

Pour ajouter des paiements à un dépôt par lot, allez à Comptabilité ‣ Clients
‣ Paiements par lot, et cliquez sur **Nouveau**. Ensuite, sélectionnez la
**Banque** et choisissez **Dépôt par lot** comme **Mode de paiement**.

![Remplissez un nouveau formulaire de paiement par lot
entrant](../../../../_images/batch-customer-payment.png)

Cliquez sur **Ajouter une ligne**. Dans la fenêtre contextuelle, cochez tous
les paiements que vous voulez inclure dans le dépôt par lot, puis cliquez sur
**Sélectionner**.

![Sélectionnez tous les paiements à inclure dans le dépôt par
lot](../../../../_images/batch-lines-selection.png)

Une fois cela fait, cliquez sur **Valider** pour finaliser le dépôt par lot.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cliquez sur <b>Imprimer</b> pour télécharger un fichier PDF à inclure dans le bordereau de dépôt.</p>
</div>

### Rapprochement bancaire

Une fois que les transactions bancaires sont sur votre base de données, vous
pouvez rapprocher les lignes de relevé bancaire avec le paiement par lot. Pour
ce faire, allez au **Tableau de bord de Comptabilité** et cliquez sur
**Lettrer Éléments** sur le compte bancaire concerné. Allez à l’onglet
**Paiements par lot** pour sélectionner un lot spécifique et cliquez sur
**Valider** pour finaliser le processus.

![Rapprocher le paiement par lot avec toutes ses
transactions](../../../../_images/batch-reconciliation.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un paiement spécifique n’a pas pu être traité par la banque ou est manquant, supprimez le paiement concerné avant de procéder au rapprochement.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payments">Paiements</a></p></li>
<li><p><a href="batch_sdd">Paiements par lot : Prélèvement SEPA (SDD)</a></p></li>
</ul>
</div>

