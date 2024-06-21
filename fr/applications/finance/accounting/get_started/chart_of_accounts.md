# Plan comptable

The **chart of accounts (COA)** is the list of all the accounts used to record
financial transactions in the general ledger of an organization. The chart of
accounts can be found under Accounting‣Configuration‣Chart of Accounts.

When browsing your chart of accounts, you can sort the accounts by **Code** ,
**Account Name** , or **Type** , but other options are available in the drop-
down menu **(⋮)**.

![Regroupez les comptes par type dans Konvergo ERP
Comptabilité](../../../../_images/chart-of-accounts-sort.png)

## Configuration d’un compte

The country you select during the creation of your database (or additional
company in your database) determines which [fiscal localization
package](../../fiscal_localizations) is installed by default. This
package includes a standard chart of accounts already configured according to
the country’s regulations. You can use it directly or set it according to your
company’s needs.

To create a new account, go to Accounting‣Configuration‣Chart of Accounts,
click **Create** , and fill in (at the minimum) the required fields (**Code,
Account Name, Type**).

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Il n’est pas possible de modifier la <b>localisation fiscale</b> d’une entreprise une fois qu’une pièce comptable a été comptabilisée.</p>
</div>

### Code et nom

Each account is identified by its **Code** and **Name** , which also indicate
the account’s purpose.

### Type

Il est très important de configurer correctement le **type de compte** , car
il a de multiples fonctions :

  * Informations sur l’objectif et le comportement du compte

  * Générer des rapports juridiques et financiers spécifiques à chaque pays

  * Définir les règles pour clôturer un exercice

  * Générer des écritures d’ouverture

To configure an account type, open the **Type** field’s drop-down selector and
select the corresponding type from the following list:

Rapport | Catégorie | Types de compte  
---|---|---  
Bilan | Actifs | Créances  
Banque et espèces  
Actifs circulants  
Actifs immobilisés  
Prépaiements  
Immobilisations  
Passifs | Dettes  
Carte de crédit  
Passifs circulants  
Passifs immobilisés  
Fonds propres | Fonds propres  
Bénéfices de l’année en cours  
Compte de résultat | Produits | Produits  
Autres revenus  
Charges | Charges  
Amortissement  
Coût des produits  
Autre | Autre | Hors bilan  
  
#### Automatisation des actifs, des charges constatées d’avance et des
produits constatés d’avance

Some **account types** can **automate** the creation of
[assets](../vendor_bills/assets#assets-automation) entries, [deferred
expenses](../vendor_bills/deferred_expenses#deferred-expenses-automation)
entries, and [deferred
revenues](../customer_invoices/deferred_revenues#deferred-revenues-
automation) entries. To **automate** entries, click **Setup** on an account
line and go to the **Automation** tab.

You have three choices for the **Automation** tab:

  1. **Non** : il s’agit de la valeur par défaut. Rien ne se passe.

  2. **Create in draft** : whenever a transaction is posted on the account, a draft entry is created but not validated. You must first fill out the corresponding form.

  3. **Create and validate** : you must also select a **Deferred Expense Model**. Whenever a transaction is posted on the account, an entry is created and immediately validated.

### Taxes par défaut

In the **Setup** menu of an account, select a **default tax** to be applied
when this account is chosen for a product sale or purchase.

### Étiquettes

Some accounting reports require **tags** to be set on the relevant accounts.
To add a tag, under **Setup** , click the **Tags** field and select an
existing tag or **Create** a new one.

### Groupes de comptes

**Account groups** are useful to list multiple accounts as _sub-accounts_ of a
bigger account and thus consolidate reports such as the **Trial Balance**. By
default, groups are handled automatically based on the code of the group. For
example, a new account `131200` is going to be part of the group `131000`. You
can attribute a specific group to an account in the **Group** field under
**Setup**.

#### Créer manuellement des groupes de comptes

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les utilisateurs réguliers ne devraient pas avoir besoin de créer manuellement des groupes de comptes. La section suivante n’est destinée qu’à des cas d’utilisation rares et avancés.</p>
</div>

To create a new account group, activate [developer
mode](../../../general/developer_mode#developer-mode) and head to
Accounting app‣Configuration‣Account Groups. Here, create a new group and
enter the **name, code prefix, and company** to which that group account
should be available. Note that you must enter the same code prefix in both
**From** and **to** fields.

![Création de groupes de comptes.](../../../../_images/account-groups.png)

To display your **Trial Balance** report with your account groups, go to
Accounting‣Reporting‣Trial Balance, then open the **Options** menu and select
**Hierarchy and Subtotals**.

![Groupes de compte dans la balance générale dans Konvergo ERP
Comptabilité](../../../../_images/chart-of-accounts-groups.png)

### Autoriser le lettrage

Certains comptes, tels que les comptes créés pour enregistrer les transactions
d’un mode de paiement, peuvent être utilisés pour le lettrage des pièces
comptables.

Par exemple, une facture payée par carte de crédit peut être marquée comme
**payée** si elle est lettrée avec son paiement. Par conséquent, le compte
utilisé pour enregistrer les paiements par carte de crédit doit être configuré
de manière à **autoriser le lettrage**.

To do so, check the **Allow Reconciliation** box in the account’s settings,
and **Save** ; or enable the button from the chart of accounts view.

![Allow reconciliation for accounts in Konvergo ERP
Accounting](../../../../_images/chart-of-accounts-reconciliation.png)

### Obsolète

It is not possible to delete an account once a transaction has been recorded
on it. You can make them unusable by using the **Deprecated** feature: check
the **Deprecated** box in the account’s settings, and **Save**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="cheat_sheet">Aide-mémoire de la comptabilité</a></p></li>
<li><p><a href="../vendor_bills/assets">Actifs immobilisés et immobilisations</a></p></li>
<li><p><a href="../vendor_bills/deferred_expenses">Charges constatées d’avance et acomptes</a></p></li>
<li><p><a href="../customer_invoices/deferred_revenues">Produits constatés d’avance</a></p></li>
<li><p><a href="../../fiscal_localizations">Localisations fiscales</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/chart-of-accounts-1630">Tutoriels Konvergo ERP : Plan comptable</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/update-your-chart-of-accounts-1658">Tutoriels Konvergo ERP : Mettre à jour votre plan comptable</a></p></li>
</ul>
</div>

