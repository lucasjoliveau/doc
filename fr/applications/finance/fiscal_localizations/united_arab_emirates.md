# Émirats arabes unis

## Installation

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation des
**Émirats arabes unis** :

Nom | Nom technique | Description  
---|---|---  
Émirats arabes unis - Comptabilité | `l10n_ae` | [Package de localisation fiscale](../fiscal_localizations.html) par défaut. Inclut les comptes, les taxes et les rapports.  
Émirats arabes unis - Paie | `l10n_ae_hr_payroll` | Inclut les règles, les calculs et les structures salariales.  
Émirats arabes unis - Paie avec Comptabilité | `l10n_ae_hr_payroll_account` | Inclut les comptes liés au module de paie.  
Émirats arabes unis - Point de Vente | `l10n_ae_pos` | Inclut le reçu PdV conforme aux normes des Émirats arabes unis.  
![Sélectionnez les modules à installer.](../../../_images/l10n-ae-modules.png)

## Plan comptable

Allez à Comptabilité ‣ Configuration ‣ Plan comptable pour afficher tous les
comptes par défaut sdisponibles pour le package de localisation des Émirats
arabes unis. Vous pouvez filtrer par Code en utilisant les chiffres situés à
l’extrême gauche ou en cliquant sur Regrouper par ‣ Type de compte. Vous
pouvez activer/désactiver le rapprochement ou **configurez** des comptes
spécifiques selon vos besoins.

Important

  * Gardez toujours au moins un **compte client** et un **compte fournisseur** actifs.

  * Il est également conseillé de **garder les comptes suivants actifs** , car ils sont utilisés comme comptes transitoires par Odoo ou sont spécifiques au **package de localisation des Émirats arabes unis**.

Code | Nom du compte | Type  
---|---|---  
102011 | Comptes clients | Créances  
102012 | Comptes clients (PdV) | Créances  
201002 | Dettes | Dettes  
101004 | Banque | Banque et espèces  
105001 | Espèces | Banque et espèces  
100001 | Transfert de liquidités | Actifs circulants  
101002 | Paiements entrants en suspens | Actifs circulants  
101003 | Paiements sortants en suspens | Actifs circulants  
104041 | TVA en amont | Actifs circulants  
100103 | TVA à percevoir | Actifs immobilisés  
101001 | Compte d’attente de la banque | Passifs circulants  
201017 | TVA en aval | Passifs circulants  
202001 | Provision de fin de service | Passifs circulants  
202003 | TVA à payer | Passifs immobilisés  
999999 | Profits/pertes non distribués | Bénéfices de l’année en cours  
400003 | Salaire de base | Notes de frais  
400004 | Allocation de logement | Notes de frais  
400005 | Allocation de transport | Notes de frais  
400008 | Indemnité de fin de service | Notes de frais  

## Taxes

Pour accéder à vos taxes, allez à Comptabilité ‣ Configuration ‣ Taxes.
Activez/désactivez ou [configurez](../accounting/taxes.html) les taxes
pertinentes pour vos activités en cliquant dessus. N’oubliez pas ne configurer
les comptes de taxes que sur le groupe de taxes de **5%** , les autres groupes
n’ayant pas besoin d’être clôturés. Pour ce faire, activez le [mode
développeur](../../general/developer_mode.html) et allez à Configuration ‣
Groupes de taxes. Définissez ensuite un Compte courant de la taxe (dettes), un
Compte courant de la taxe (créances), et un Compte de versement anticipé de la
taxe pour le groupe de **5%**.

Note

Le mécanisme d’autoliquidation est pris en charge par Odoo.

![Aperçu des taxes du package de localisation des Émirats arabes
unis.](../../../_images/uae-localization-taxes.png)

## Taux de change

Pour mettre à jour les taux de change, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Devises. Cliquez sur le bouton de mise à jour (🗘) situé à côté du
champ Prochaine exécution.

Pour lancer la mise à jour automatiquement à des intervalles définis, modifiez
l”Intervalle de Manuellement à la fréquence souhaitée.

Note

Par défaut, le service web des taux de change de la Banque centrale des
Émirats arabes unis est utilisé. Plusieurs autres fournisseurs sont
disponibles dans le champ Service.

## Paie

Le module Émirats arabes unis - Paie crée les **règles salariales**
nécessaires dans l’application Paie conformément aux règles et aux
réglementations des Émirats arabes unis. Les règles salariales sont liées aux
comptes correspondants dans le **plan comptable**.

![La structure de paie des employés des Émirats arabes
unis.](../../../_images/uae-localization-salary-rules.png)

### Règles salariales

Pour appliquer ces règles au contrat d’un employé, allez à Paie ‣ Contracts ‣
Contrats et sélectionnez le contrat de l’employé. Dans le champ Type de
structure salariale, sélectionnez Employé Émirats arabes unis.

![Sélectionnez le type de structure salariale pour l'appliquer au
contrat.](../../../_images/uae-localization-salary-structure.png)

Dans l’onglet Informations salariales, vous pouvez y trouver les détails
suivants :

  * Salaire ;

  * Allocation de logement ;

  * Allocation de transport ;

  * Autres allocations ;

  * Nombre de jours : utilisé pour calculer la provision de fin de service.

Note

  * Les **retenues pour congés** sont calculées à l’aide d’une règle salariale liée au type **congé sans solde** ;

  * Les autres retenues ou remboursements sont effectués _manuellement_ à l’aide d’autres entrées ;

  * Les **heures supplémentaires** sont ajoutées _manuellement_ en allant à Prestations ‣ Prestations ;

  * Les **Saisies sur salaire** sont générées en allant aux Contrats ‣ Saisies sur salaire. Créez ensuite une saisie et sélectionnez l”Employé et le Type (Saisie sur salaire, Cession sur salaire, Pension alimentaire).

Astuce

Pour empêcher qu’une règle apparaisse sur une fiche de paie, allez à Paie ‣
Configuration ‣ Règles. Cliquez sur Structure de paie des employés des Émirats
arabes unis, sélectionnez la règle à masquer et cliquez sur Apparaît sur la
fiche de paie.

### Provision de fin de service

La provision est définie par l’allocation mensuelle totale _divisée_ par 30,
puis _multipliée_ par le nombre de jours défini dans le champ Nombre de jours
en bas du formulaire de contrat.

La provision est ensuite calculée via une règle salariale associée à deux
comptes : l”**Indemnité de fin de service (compte de charges)** et la
**Provision de fin de service (compte de passifs immobilisés)**. Ce dernier
est utilisé pour payer le **montant de fin de service** en le réglant avec le
**compte créances**.

Note

Le montant de fin de service est calculé sur la base du salaire brut et les
date de début et de fin du contrat de l’employé.

### Factures clients

Le package de localisation des Émirats arabes unis permet de générer des
factures en anglais, en arabe ou les deux. La localisation inclut également
une ligne pour afficher le **montant de TVA** par ligne.

