# Les Philippines

## Configuration

[Installez](../../general/apps_modules.html#general-install) le [package de
localisation fiscale](../fiscal_localizations.html#fiscal-localizations-
packages) des 🇵🇭 Philippines pour bénéficier de toutes les fonctionnalités
comptables par défaut de la localisation philippine, telles que le plan
comptable, les taxes et le rapport BIR 2307. Ces éléments constituent un
modèle de base pour commencer à utiliser la comptabilité philippine.

Note

  * When creating a new database and selecting the `Philippines` as a country, the fiscal localization module **Philippines - Accounting** is automatically installed.

  * If the module is installed in an existing company, the **chart of accounts** and **taxes** will _not_ be replaced if there are already posted journal entries.

  * Le rapport BIR 2307 est installé, mais il se peut que les retenues à la source doivent être créées manuellement.

### Plan comptable et taxes

A minimum configuration default chart of accounts is installed, and the
following types of taxes are installed and linked to the relevant account:

  * TVA 12%

  * Exonération de la TVA

  * Retenues à la source

For the withholding taxes (Configuration ‣ Taxes), there is an additional
Philippines ATC field under the Philippines tab.

![Le champ Philippines ATC code défini sur les
taxes.](../../../_images/philippines-atc-code.png)

Note

Les codes ATC des taxes sont utilisés dans le rapport BIR 2307. Si une taxe
est créée manuellement, il faut ajouter son code ATC.

### Contacts

Lorsque le contact d’une société ou d’un particulier (qui n’appartient à
aucune société) est situé aux Philippines, remplissez le champ ID fiscal avec
son `Numéro d'identification fiscale (NIF)`.

Pour les particuliers qui n’appartiennent à aucune société, identifiez-les
grâce aux champs supplémentaires suivants :

  * Prénom

  * Deuxième prénom

  * Nom de famille

![Contact de type particulier avec les champs Prénom, Deuxième prénom et Nom
de famille.](../../../_images/philippines-contact-individual.png)

Note

Pour les Sociétés et les Particuliers, le NIF doit respecter le format `NNN-
NNN-NNN-NNNNN`. Le code de la succursale doit suivre les derniers chiffres du
NIF, sinon il peut être laissé à `00000`.

## Rapport BIR 2307

**BIR 2307** report data, also known as [Certificate of Creditable Tax
Withheld at Source](https://www.bir.gov.ph/index.php/bir-
forms/certificates.html), can be generated for purchase orders and vendor
payments with the applicable withholding taxes.

Pour générer un rapport BIR 2307, sélectionnez une ou plusieurs factures
fournisseurs dans la vue liste et cliquez sur Action ‣ Télécharger BIR 2307
XLS.

![Plusieurs factures fournisseurs sélectionnées avec l'action "Télécharger BIR
2307 XLS".](../../../_images/philippines-multi-bill.png)

Astuce

Vous pouvez effectuer la même action sur une facture fournisseur à partir de
la vue formulaire.

Une fenêtre contextuelle apparaît pour revoir la sélection, puis cliquez sur
Générer.

![Menu contextuel pour générer le fichier XLS du BIR
2307.](../../../_images/philippines-generate.png)

Cette opération génère le fichier `Form_2307.xls` qui répertorie toutes les
lignes de la facture fournisseur avec la retenue à la source applicable.

The process above can also be used for a _single_ vendor
[payment](../accounting/payments.html) if it is linked to one or more [vendor
bills](../accounting/payments.html) with applied withholding taxes.

Note

  * If no withholding tax is applied, then the XLS file will not generate records for those vendor bill lines.

  * When grouping payments for multiple bills, Odoo splits the payments based on the contact. From a payment, clicking Action ‣ Download BIR 2307 XLS generates a report that only includes vendor bills related to that contact.

Important

Odoo cannot generate the BIR 2307 PDF report or DAT files directly. The
generated `Form_2307.xls` file can be exported to an _external_ tool to
convert it to BIR DAT or PDF format.

