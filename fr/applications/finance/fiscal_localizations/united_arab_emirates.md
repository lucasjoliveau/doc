# Émirats arabes unis

## Installation

[Installez](../../general/apps_modules#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation des
**Émirats arabes unis** :

Nom | Nom technique | Description  
---|---|---  
**Émirats arabes unis - Comptabilité** | `l10n_ae` | [Package de localisation fiscale](../fiscal_localizations) par défaut. Inclut les comptes, les taxes et les rapports.  
**Émirats arabes unis - Paie** | `l10n_ae_hr_payroll` | Inclut les règles, les calculs et les structures salariales.  
**Émirats arabes unis - Paie avec Comptabilité** | `l10n_ae_hr_payroll_account` | Inclut les comptes liés au module de paie.  
**Émirats arabes unis - Point de Vente** | `l10n_ae_pos` | Inclut le reçu PdV conforme aux normes des Émirats arabes unis.  
![Sélectionnez les modules à installer.](../../../_images/l10n-ae-modules.png)

## Plan comptable

Allez à Comptabilité ‣ Configuration ‣ Plan comptable pour afficher tous les
comptes par défaut sdisponibles pour le package de localisation des Émirats
arabes unis. Vous pouvez filtrer par **Code** en utilisant les chiffres situés
à l’extrême gauche ou en cliquant sur Regrouper par ‣ Type de compte. Vous
pouvez **activer** /**désactiver** le rapprochement ou **configurez** des
comptes spécifiques selon vos besoins.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Gardez toujours au moins un <b>compte client</b> et un <b>compte fournisseur</b> actifs.</p></li>
<li><p>Il est également conseillé de <b>garder les comptes suivants actifs</b>, car ils sont utilisés comme comptes transitoires par Konvergo ERP ou sont spécifiques au <b>package de localisation des Émirats arabes unis</b>.</p>
<table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Code</p></th>
<th class="head"><p>Nom du compte</p></th>
<th class="head"><p>Type</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>102011</p></td>
<td><p>Comptes clients</p></td>
<td><p>Créances</p></td>
</tr>
<tr class="row-odd"><td><p>102012</p></td>
<td><p>Comptes clients (PdV)</p></td>
<td><p>Créances</p></td>
</tr>
<tr class="row-even"><td><p>201002</p></td>
<td><p>Dettes</p></td>
<td><p>Dettes</p></td>
</tr>
<tr class="row-odd"><td><p>101004</p></td>
<td><p>Banque</p></td>
<td><p>Banque et espèces</p></td>
</tr>
<tr class="row-even"><td><p>105001</p></td>
<td><p>Espèces</p></td>
<td><p>Banque et espèces</p></td>
</tr>
<tr class="row-odd"><td><p>100001</p></td>
<td><p>Transfert de liquidités</p></td>
<td><p>Actifs circulants</p></td>
</tr>
<tr class="row-even"><td><p>101002</p></td>
<td><p>Paiements entrants en suspens</p></td>
<td><p>Actifs circulants</p></td>
</tr>
<tr class="row-odd"><td><p>101003</p></td>
<td><p>Paiements sortants en suspens</p></td>
<td><p>Actifs circulants</p></td>
</tr>
<tr class="row-even"><td><p>104041</p></td>
<td><p>TVA en amont</p></td>
<td><p>Actifs circulants</p></td>
</tr>
<tr class="row-odd"><td><p>100103</p></td>
<td><p>TVA à percevoir</p></td>
<td><p>Actifs immobilisés</p></td>
</tr>
<tr class="row-even"><td><p>101001</p></td>
<td><p>Compte d’attente de la banque</p></td>
<td><p>Passifs circulants</p></td>
</tr>
<tr class="row-odd"><td><p>201017</p></td>
<td><p>TVA en aval</p></td>
<td><p>Passifs circulants</p></td>
</tr>
<tr class="row-even"><td><p>202001</p></td>
<td><p>Provision de fin de service</p></td>
<td><p>Passifs circulants</p></td>
</tr>
<tr class="row-odd"><td><p>202003</p></td>
<td><p>TVA à payer</p></td>
<td><p>Passifs immobilisés</p></td>
</tr>
<tr class="row-even"><td><p>999999</p></td>
<td><p>Profits/pertes non distribués</p></td>
<td><p>Bénéfices de l’année en cours</p></td>
</tr>
<tr class="row-odd"><td><p>400003</p></td>
<td><p>Salaire de base</p></td>
<td><p>Notes de frais</p></td>
</tr>
<tr class="row-even"><td><p>400004</p></td>
<td><p>Allocation de logement</p></td>
<td><p>Notes de frais</p></td>
</tr>
<tr class="row-odd"><td><p>400005</p></td>
<td><p>Allocation de transport</p></td>
<td><p>Notes de frais</p></td>
</tr>
<tr class="row-even"><td><p>400008</p></td>
<td><p>Indemnité de fin de service</p></td>
<td><p>Notes de frais</p></td>
</tr>
</tbody>
</table>
</li>
</ul>
</div>

## Taxes

Pour accéder à vos taxes, allez à Comptabilité ‣ Configuration ‣ Taxes.
Activez/désactivez ou [configurez](../accounting/taxes) les taxes
pertinentes pour vos activités en cliquant dessus. N’oubliez pas ne configurer
les comptes de taxes que sur le groupe de taxes de **5%** , les autres groupes
n’ayant pas besoin d’être clôturés. Pour ce faire, activez le [mode
développeur](../../general/developer_mode) et allez à Configuration ‣
Groupes de taxes. Définissez ensuite un **Compte courant de la taxe (dettes)**
, un **Compte courant de la taxe (créances)** , et un **Compte de versement
anticipé de la taxe** pour le groupe de **5%**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le mécanisme d’autoliquidation est pris en charge par Konvergo ERP.</p>
</div> ![Aperçu des taxes du package de localisation des Émirats
arabes unis.](../../../_images/uae-localization-taxes.png)

## Taux de change

Pour mettre à jour les taux de change, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Devises. Cliquez sur le bouton de mise à jour (**🗘**) situé à
côté du champ **Prochaine exécution**.

Pour lancer la mise à jour automatiquement à des intervalles définis, modifiez
l”**Intervalle** de **Manuellement** à la fréquence souhaitée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Par défaut, le service web des taux de change de la Banque centrale des Émirats arabes unis est utilisé. Plusieurs autres fournisseurs sont disponibles dans le champ <b>Service</b>.</p>
</div>

## Paie

Le module **Émirats arabes unis - Paie** crée les **règles salariales**
nécessaires dans l’application Paie conformément aux règles et aux
réglementations des Émirats arabes unis. Les règles salariales sont liées aux
comptes correspondants dans le **plan comptable**.

![La structure de paie des employés des Émirats arabes
unis.](../../../_images/uae-localization-salary-rules.png)

### Règles salariales

Pour appliquer ces règles au contrat d’un employé, allez à Paie ‣ Contracts ‣
Contrats et sélectionnez le contrat de l’employé. Dans le champ **Type de
structure salariale** , sélectionnez **Employé Émirats arabes unis**.

![Sélectionnez le type de structure salariale pour l'appliquer au
contrat.](../../../_images/uae-localization-salary-structure.png)

Dans l’onglet **Informations salariales** , vous pouvez y trouver les détails
suivants :

  * **Salaire** ;

  * **Allocation de logement** ;

  * **Allocation de transport** ;

  * **Autres allocations** ;

  * **Nombre de jours** : utilisé pour calculer la provision de fin de service.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Les <b>retenues pour congés</b> sont calculées à l’aide d’une règle salariale liée au type <b>congé sans solde</b> ;</p></li>
<li><p>Les autres retenues ou remboursements sont effectués <em>manuellement</em> à l’aide d’autres entrées ;</p></li>
<li><p>Les <b>heures supplémentaires</b> sont ajoutées <em>manuellement</em> en allant à Prestations ‣ Prestations ;</p></li>
<li><p>Les <b>Saisies sur salaire</b> sont générées en allant aux Contrats ‣ Saisies sur salaire. <b>Créez</b> ensuite une saisie et sélectionnez l”<b>Employé</b> et le <b>Type (Saisie sur salaire, Cession sur salaire, Pension alimentaire)</b>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour empêcher qu’une règle apparaisse sur une fiche de paie, allez à Paie ‣ Configuration ‣ Règles. Cliquez sur <b>Structure de paie des employés des Émirats arabes unis</b>, sélectionnez la règle à masquer et cliquez sur <b>Apparaît sur la fiche de paie</b>.</p>
</div>

### Provision de fin de service

La provision est définie par l’allocation mensuelle totale _divisée_ par 30,
puis _multipliée_ par le nombre de jours défini dans le champ **Nombre de
jours** en bas du formulaire de contrat.

La provision est ensuite calculée via une règle salariale associée à deux
comptes : l”**Indemnité de fin de service (compte de charges)** et la
**Provision de fin de service (compte de passifs immobilisés)**. Ce dernier
est utilisé pour payer le **montant de fin de service** en le réglant avec le
**compte créances**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le montant de fin de service est calculé sur la base du salaire brut et les date de début et de fin du contrat de l’employé.</p>
</div>

### Factures clients

Le package de localisation des Émirats arabes unis permet de générer des
factures en anglais, en arabe ou les deux. La localisation inclut également
une ligne pour afficher le **montant de TVA** par ligne.

