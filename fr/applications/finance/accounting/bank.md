# Comptes bancaires et d’espèces

Vous pouvez gérer autant de comptes bancaires ou d’espèces que nécessaire dans
votre base de données. Bien les configurer vous permet d’avoir toutes vos
données bancaires à jour et prêtes à être
[rapprochées](bank/reconciliation) avec vos pièces comptables.

Dans Konvergo ERP Comptabilité, chaque compte bancaire dispose d’un journal dédié,
configuré pour comptabiliser toutes les écritures dans un compte dédié. Le
journal et le compte sont automatiquement créés et configurés chaque fois que
vous ajoutez un compte bancaire.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les journaux et les comptes d’espèces doivent être configurés manuellement.</p>
</div>

Les journaux de banque sont affichés par défaut sur le **Tableau de bord de la
Comptabilité** sous forme de cartes avec des boutons d’action.

![Les journaux de banque sont affichés sur le tableau de bord de la
comptabilité et contiennent des boutons d'action.](../../../_images/card.png)

## Gérer vos comptes bancaires et d’espèces

### Connecter votre banque pour la synchronisation automatique

Pour connecter votre compte bancaire à votre base de données, allez à
Comptabilité ‣ Configuration ‣ Banques : Ajouter un compte bancaire,
sélectionnez votre banque dans la liste et cliquez sur **Connecter** et suivez
les instructions.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="bank/bank_synchronization">Synchronisation bancaire</a></p>
</div>

### Créer un compte bancaire

Si votre établissement bancaire n’est pas disponible dans Konvergo ERP ou si vous ne
souhaitez pas connecter votre compte bancaire à votre base de données, vous
pouvez configurer votre compte bancaire manuellement.

Pour ajouter un compte bancaire manuellement, allez à Comptabilité ‣
Configuration ‣ Banques : Ajouter un compte bancaire, cliquez sur **La créer**
(en bas à droite) et complétez le formulaire.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Konvergo ERP détecte automatiquement le type de compte bancaire (par ex. IBAN) et active certaines fonctionnalités en conséquence.</p></li>
<li><p>Un journal de banque par défaut est disponible et peut être utilisé pour configurer votre compte bancaire en allant à Comptabilité ‣ Configuration ‣ Comptabilité : Journaux ‣ Banque. Ouvrez le formulaire et modifiez les champs pour correspondre à vos informations de compte bancaire.</p></li>
</ul>
</div>

### Créer un journal d’espèces

Pour créer un nouveau journal d’espèces, allez à Comptabilité ‣ Configuration
‣ Comptabilité : Journaux, cliquez sur **Créer** et sélectionnez **Espèces**
dans le champ **Type**.

Pour plus d’informations sur les champs d’informations comptables, lisez la
section Configuration de cette page.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Un journal d’espèces par défaut est disponible et peut être utilisé immédiatement. Vous pouvez l’analyser en allant à Comptabilité ‣ Configuration ‣ Comptabilité : Journaux ‣ Espèces.</p>
</div>

### Modifier un journal de banque ou d’espèces existant

Pour éditer un journal de banque existant, allez à Comptabilité ‣
Configuration ‣ Comptabilité : Journaux et sélectionnez le journal que vous
souhaitez modifier.

## Configuration

Vous pouvez modifier les informations comptables et le numéro de compte
bancaire en fonction de vos besoins.

![Configurez vos informations bancaires manuellement](../../../_images/bank-
journal-config.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="get_started/multi_currency">Système multidevise</a></p></li>
<li><p><a href="bank/transactions">Transactions</a></p></li>
</ul>
</div>

### Compte d’attente

Les transactions du relevé bancaire sont comptabilisées sur le **Compte
d’attente** jusqu’au rapprochement définitif qui permet de trouver le bon
compte.

### Comptes de perte et de profit

Le **Compte de profit** est utilisé pour enregistrer un bénéfice lorsque le
solde final d’une caisse diffère de ce que le système calcule, tandis que le
**Compte de perte** est utilisé pour enregistrer une perte lorsque le solde
final d’une caisse diffère de ce que le système calcule.

### Devise

Vous pouvez modifier la devise utilisée pour saisir les relevés.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="get_started/multi_currency">Système multidevise</a></p>
</div>

### Numéro de compte

Si vous devez **modifier les détails de votre compte bancaire** , cliquez sur
la flèche du lien externe à côté de votre **Numéro de compte**. Sur la
nouvelle page, cliquez sur la flèche du lien externe à côté de votre
**Banque** et mettez à jour vos informations bancaires en conséquence. Ces
détails sont utilisés lors de l’enregistrement des paiements.

![Modifiez vos informations bancaires](../../../_images/bank-account-
number.png)

### Flux de données bancaires

Les **Flux de données bancaires** définissent la manière dont les relevés
bancaires sont enregistrés. Trois options sont disponibles :

  * **Indéfini pour le moment** , qui doit être sélectionné lorsque vous ne savez pas encore si vous allez synchroniser votre compte bancaire avec votre base de données ou pas.

  * **Import (CAMT, CODA, CSV, OFX, QIF)** , qui doit être sélectionné si vous souhaitez importer vos relevés bancaires dans un format différent.

  * **Synchronisation bancaire automatisée** , qui doit être sélectionnée si votre banque est synchronisée avec votre base de données.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="bank/bank_synchronization">Synchronisation bancaire</a></p></li>
<li><p><a href="bank/transactions">Transactions</a></p></li>
</ul>
</div>

## Comptes en suspens

Par défaut, les paiements sont enregistrés sur des comptes transitoires
appelés **comptes en suspens** , avant d’être enregistrés sur votre compte
bancaire.

  * Un **compte de paiements sortants en suspens** est un compte sur lequel les paiements sont enregistrés jusqu’à ce qu’ils sont liés à un retrait sur votre relevé bancaire.

  * Un **compte de paiements entrants en suspens** est un compte sur lequel les paiements sont enregistrés jusqu’à ce qu’ils sont liés à un dépôt sur votre relevé bancaire.

Ces comptes doivent être de type
[type](get_started/chart_of_accounts#chart-of-account-type) **Actifs
circulants**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le transfert d’un compte en suspens vers un compte bancaire s’effectue automatiquement lors du rapprochement du compte bancaire avec le relevé bancaire.</p>
</div>

### Configuration des comptes par défaut

Les comptes en suspens sont définis par défaut. Si nécessaire, vous pouvez les
mettre à jour en allant à Comptabilité ‣ Configuration ‣ Paramètres ‣ Comptes
par défaut et en mettant à jour votre **Compte de paiements entrants en
suspens** et votre **Compte de paiements sortants en suspens**.

### Configuration des journaux de banque et d’espèces

Vous pouvez également configurer des comptes en suspens spécifiques pour tout
journal dont le [type](get_started/chart_of_accounts#chart-of-account-
type) est **Banque** ou **Espèces**.

À partir de votre **Tableau de bord de comptabilité** , cliquez sur la
sélection de menu ⋮ du journal que vous souhaitez configurer et cliquez sur
**Configuration** , puis ouvrez l’onglet **Paiements entrants/sortants**. Pour
afficher la colonne des comptes en suspens, cliquez sur le bouton à bascule et
cochez la case **Comptes de paiements entrants/sortants en suspens** , puis
mettez à jour le compte.

![Cliquez sur le bouton à bascule et cliquez sur Comptes en
suspens](../../../_images/toggle-button.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Si vous ne précisez pas de compte de paiements sortants en suspens ou de compte de paiements entrants en suspens pour un journal spécifique, Konvergo ERP utilise les comptes en suspens par défaut.</p></li>
<li><p>Si votre compte bancaire principal est ajouté en tant que compte de paiements entrants en suspens ou compte de paiements sortants en suspens, lorsqu’un paiement est enregistré, le statut de la facture client ou fournisseur est directement défini sur <b>Payé</b>.</p></li>
</ul>
</div>

  * [Synchronisation bancaire](bank/bank_synchronization)
    * [Salt Edge](bank/bank_synchronization/saltedge)
    * [Ponto](bank/bank_synchronization/ponto)
    * [Enable Banking](bank/bank_synchronization/enablebanking)
  * [Transactions](bank/transactions)
  * [Rapprochement bancaire](bank/reconciliation)
  * [Modèles de lettrage](bank/reconciliation_models)
  * [Gérer un compte bancaire en devise étrangère](bank/foreign_currency)
  * [Caisse](bank/cash_register)

