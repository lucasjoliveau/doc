# Les Philippines

## Configuration

[Installez](../../general/apps_modules#general-install) le [package de
localisation fiscale](../fiscal_localizations#fiscal-localizations-
packages) des **🇵🇭 Philippines** pour bénéficier de toutes les fonctionnalités
comptables par défaut de la localisation philippine, telles que le plan
comptable, les taxes et le rapport BIR 2307. Ces éléments constituent un
modèle de base pour commencer à utiliser la comptabilité philippine.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>When creating a new database and selecting the <code>Philippines</code> as a country, the fiscal
localization module <b>Philippines - Accounting</b> is automatically installed.</p></li>
<li><p>If the module is installed in an existing company, the <b>chart of accounts</b> and <b>taxes</b> will
<em>not</em> be replaced if there are already posted journal entries.</p></li>
<li><p>Le rapport BIR 2307 est installé, mais il se peut que les retenues à la source doivent être créées manuellement.</p></li>
</ul>
</div>

### Plan comptable et taxes

A minimum configuration default chart of accounts is installed, and the
following types of taxes are installed and linked to the relevant account:

  * TVA 12%

  * Exonération de la TVA

  * Retenues à la source

For the withholding taxes (Configuration ‣ Taxes), there is an additional
**Philippines ATC** field under the **Philippines** tab.

![Le champ Philippines ATC code défini sur les
taxes.](../../../_images/philippines-atc-code.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les codes ATC des taxes sont utilisés dans le rapport BIR 2307. Si une taxe est créée manuellement, il faut ajouter son code ATC.</p>
</div>

### Contacts

Lorsque le contact d’une société ou d’un particulier (qui n’appartient à
aucune société) est situé aux Philippines, remplissez le champ **ID fiscal**
avec son `Numéro d'identification fiscale (NIF)`.

Pour les particuliers qui n’appartiennent à aucune société, identifiez-les
grâce aux champs supplémentaires suivants :

  * **Prénom**

  * **Deuxième prénom**

  * **Nom de famille**

![Contact de type particulier avec les champs Prénom, Deuxième prénom et Nom
de famille.](../../../_images/philippines-contact-individual.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour les <b>Sociétés</b> et les <b>Particuliers</b>, le NIF doit respecter le format <code>NNN-NNN-NNN-NNNNN</code>. Le code de la succursale doit suivre les derniers chiffres du NIF, sinon il peut être laissé à <code>00000</code>.</p>
</div>

## Rapport BIR 2307

**BIR 2307** report data, also known as [Certificate of Creditable Tax
Withheld at Source](https://www.bir.gov.ph/index.php/bir-
forms/certificates), can be generated for purchase orders and vendor
payments with the applicable withholding taxes.

Pour générer un rapport BIR 2307, sélectionnez une ou plusieurs factures
fournisseurs dans la vue liste et cliquez sur Action ‣ Télécharger BIR 2307
XLS.

![Plusieurs factures fournisseurs sélectionnées avec l'action "Télécharger BIR
2307 XLS".](../../../_images/philippines-multi-bill.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez effectuer la même action sur une facture fournisseur à partir de la vue formulaire.</p>
</div>

Une fenêtre contextuelle apparaît pour revoir la sélection, puis cliquez sur
**Générer**.

![Menu contextuel pour générer le fichier XLS du BIR
2307.](../../../_images/philippines-generate.png)

Cette opération génère le fichier `Form_2307.xls` qui répertorie toutes les
lignes de la facture fournisseur avec la retenue à la source applicable.

The process above can also be used for a _single_ vendor
[payment](../accounting/payments) if it is linked to one or more [vendor
bills](../accounting/payments) with applied withholding taxes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If no withholding tax is applied, then the XLS file will not generate records for those vendor
bill lines.</p></li>
<li><p>When grouping payments for multiple bills, Konvergo ERP splits the payments based on the contact. From
a payment, clicking Action ‣ Download BIR 2307 XLS generates a report that
only includes vendor bills related to that contact.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP cannot generate the BIR 2307 PDF report or DAT files directly. The generated
<code>Form_2307.xls</code> file can be exported to an <em>external</em> tool to convert it to BIR DAT or PDF
format.</p>
</div>

