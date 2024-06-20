# Colombie

Odoo’s Colombian localization package provides accounting, fiscal, and legal
features for databases in Colombia – such as chart of accounts, taxes, and
electronic invoicing.

In addition, a series of videos on the subject is also available. These videos
cover how to start from scratch, set up configurations, complete common
workflows, and provide in-depth looks at some specific use cases as well.

Pour plus d'infos

[Smart Tutorial - Colombian Localization](https://www.odoo.com/slides/smart-
tutorial-localizacion-de-colombia-132).

## Configuration

### Installation des modules

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
colombienne :

Nom | Nom technique | Description  
---|---|---  
Colombie - Comptabilité | `l10n_co` | Default [fiscal localization package](../fiscal_localizations.html#fiscal-localizations-packages). This module adds the base accounting features for the Colombian localization: chart of accounts, taxes, withholdings, and identification document type.  
Colombie - Rapports comptables | `l10n_co_reports` | Inclut des rapports comptables permettant d’envoyer des certifications aux fournisseurs pour les retenues à la source appliquées.  
Facturation électronique pour la Colombie avec Carvajal | `l10n_co_edi` | This module includes the features required for integration with Carvajal, and generates the electronic invoices and support documents related to the vendor bills, based on DIAN regulations.  
Colombie - Point de Vente | `l10n_co_pos` | Includes Point of Sale receipts for Colombian localization.  
  
Note

When `Colombia` is selected for a company’s Fiscal Localization, Odoo
automatically installs certain modules.

### Configuration de l’entreprise

To configure your company information, go to the Contacts app, and search for
your company.

Alternatively, activate [developer
mode](../../general/developer_mode.html#developer-mode) and navigate to
General Setting ‣ Company ‣ Update Info ‣ Contact. Then, edit the contact form
and configure the following information:

  * Nom de la société.

  * Address: Including City, Department and ZIP code.

  * Identification Number: Select the Identification Type (`NIT`, `Cédula de Ciudadanía`, `Registro Civil`, etc.). When the Identification Type is `NIT`, the Identification Number **must** have the _verification digit_ at the end of the ID prefixed by a hyphen (`-`).

Ensuite, configurez les Informations fiscales dans l’onglet Ventes & Achats :

  * Obligaciones y Responsabilidades: Select the fiscal responsibility for the company (`O-13` Gran Contribuyente, `O-15` Autorretenedor, `O-23` Agente de retención IVA, `O-47` Regimen de tributación simple, `R-99-PN` No Aplica).

  * Gran Contribuyente : Sélectionnez cette option si la société est _Gran Contribuyente_.

  * Fiscal Regimen: Select the Tribute Name for the company (`IVA`, `INC`, `IVA e INC`, or `No Aplica`)

  * Nom commercial : Si la société utilise un nom commercial spécifique et qu’il doit être affiché sur la facture.

### Configuration des identifiants Carjaval

Once the modules are installed, the user credentials **must** be configured,
in order to connect with Carvajal Web Service. To do so, navigate to
Accounting ‣ Configuration ‣ Settings and scroll to the Colombian Electronic
Invoicing section. Then, fill in the required configuration information
provided by Carvajal:

  * Username and Password: Username and password (provided by Carvajal) to the company.

  * Registre national des sociétés : Numéro NIT de la société _sans_ le code de vérification.

  * Account ID: Company’s NIT number followed by `_01`.

  * Colombia Template Code: Select one of the two available templates (`CGEN03` or `CGNE04`) to be used in the PDF format of the electronic invoice.

Enable the Test mode checkbox to connect with the Carvajal testing
environment.

Once Odoo and Carvajal are fully configured and ready for production,
deactivate the Test mode checkbox to use the production database.

![Configurez les identifiants pour le service web Carvajal dans
Odoo.](../../../_images/carvajal-configuration.png)

Important

Test mode must **only** be used on duplicated databases, **not** the
production environment.

### Configuration des données du rapport

Les données de rapport peuvent être définies pour la section fiscale et les
informations bancaires dans le PDF dans le cadre des informations
configurables qui sont envoyées dans les XML.

Navigate to Accounting ‣ Configuration ‣ Settings, and scroll to the Colombian
Electronic Invoicing section, in order to find the Report Configuration
fields. Here the header information for each report type can be configured.

  * Gran Contribuyente

  * Tipo de Régimen

  * Retenedores de IVA

  * Autorretenedores

  * Resolución Aplicable

  * Actividad Económica

  * Bank Information

### Configuration des données de base

#### Partenaire

Partner contacts can be created in the _Contacts_ app. To do so, navigate to
Contacts, and click the Create button.

Then, name the contact, and using the radio buttons, select the contact type,
either Individual or Company.

Complete the full Address, including the City, State, and ZIP code. Then,
complete the identification and fiscal information.

##### Informations d’identification

Identification types, defined by the DIAN, are available on the partner form,
as part of the Colombian localization. Colombian partners **must** have their
Identification Number (VAT) and Document Type set.

Astuce

When the Document Type is `NIT`, the Identification Number needs to be
configured in Odoo, including the _verification digit at the end of the ID,
prefixed by a hyphen (`-`)_.

##### Informations fiscales

The partner’s responsibility codes (section 53 in the RUT document) are
included as part of the electronic invoicing module, as it is required by the
DIAN.

The required fields can be found under Partner ‣ Sales & Purchase Tab ‣ Fiscal
Information section:

  * Obligaciones y Responsabilidades: Select the fiscal responsibility for the company (`O-13` Gran Contribuyente, `O-15` Autorretenedor, `O-23` Agente de retención IVA, `O-47` Regimen de tributación simple, or `R-99-PN` No Aplica).

  * Gran Contribuyente : Sélectionnez cette option si la société est _Gran Contribuyente_.

  * Fiscal Regimen: Select the tribute name for the company (`IVA`, `INC`, `IVA e INC`, or `No Aplica`)

  * Nom commercial : Si la société utilise un nom commercial spécifique et qu’il doit être affiché sur la facture.

#### Produits

To manage products, navigate to Accounting ‣ Customers ‣ Products, then click
on a product.

When adding general information on the product form, it is required that
either the UNSPSC Category (Accounting tab), or Internal Reference (General
Information tab) field is configured. Be sure to Save the product once
configured.

#### Taxes

To create or modify taxes, go to Accounting ‣ Configuration ‣ Taxes, and
select the related tax.

If sales transactions include products with taxes, the Value Type field in the
Advanced Options tab needs to be configured per tax. Retention tax types (ICA,
IVA, Fuente) are also included. This configuration is used to display taxes
correctly in the invoice PDF.

![Les champs ICA, IVA et Fuente dans l'onglet Options avancées dans
Odoo.](../../../_images/retention-tax-types.png)

#### Journaux de vente

Once the DIAN has assigned the official sequence and prefix for the electronic
invoice resolution, the sales journals related to the invoice documents
**must** be updated in Odoo. To do so, navigate to Accounting ‣ Configuration
‣ Journals, and select an existing sales journal, or create a new one with the
Create button.

On the sales journal form, input the Journal Name, Type, and set a unique
Short Code in the Journals Entries tab. Then, configure the following data in
the Advanced Settings tab:

  * Facturation électronique : Activez UBL 2.1 (Colombie).

  * Résolution de facturation : Numéro de résolution délivré par la DIAN à la société.

  * Date de résolution : Date d’entrée en vigueur de la résolution.

  * Date de fin de la résolution : Date de fin de validité de la résolution.

  * Plage de numérotation (minimum) : Premier numéro de facture autorisé.

  * Plage de numérotation (maximum) : Dernier numéro de facture autorisé.

Note

The sequence and resolution of the journal **must** match the one configured
in Carvajal and the DIAN.

##### Séquence des factures

The invoice sequence and prefix **must** be correctly configured when the
first document is created.

Note

Odoo automatically assigns a prefix and sequence to the following invoices.

##### Journaux des achats

Once the DIAN has assigned the official sequence and prefix for the _support
document_ related to vendor bills, the purchase journals related to their
supporting documents need to be updated in Odoo. The process is similar to the
configuration of the sales journals.

##### Plan comptable

Le [plan comptable](../accounting/get_started/chart_of_accounts.html) est
installé par défaut dans le cadre du module de localisation, les comptes sont
mappés automatiquement dans les taxes, le compte fournisseur par défaut et le
compte client par défaut. Le plan comptable pour la Colombie est basé sur le
PUC (Plan Unico de Cuentas).

## Principaux flux de travail

### Facturation électronique

The following is a breakdown of the main workflow for electronic invoices with
the Colombian localization:

  1. Sender creates an invoice.

  2. Electronic invoice provider generates the legal XML file.

  3. Electronic invoice provider creates the CUFE (Invoice Electronic Code) with the electronic signature.

  4. Electronic invoice provider sends a notification to DIAN.

  5. DIAN validates the invoice.

  6. DIAN accepts or rejects the invoice.

  7. Electronic invoice provider generates the PDF invoice with a QR code.

  8. Electronic invoice provider sends invoice to the acquirer.

  9. Acquirer sends a receipt of acknowledgement, and accepts or rejects the invoice.

  10. Sender downloads a `.zip` file with the PDF and XML.

![Electronic invoice workflow for Colombian
localization.](../../../_images/workflow-electronic-invoice.png)

#### Création d’une facture

Note

The functional workflow taking place before an invoice validation does **not**
alter the main changes introduced with the electronic invoice.

Electronic invoices are generated and sent to both the DIAN and customer
through Carvajal’s web service integration. These documents can be created
from your sales order or manually generated. To create a new invoice, go to
Accounting ‣ Customers ‣ Invoices, and select Create. On the invoice form
configure the following fields:

  * Client : Informations relatives au client.

  * Journal : Journal utilisé pour les factures électroniques.

  * Type de facture électronique : Sélectionnez le type de document. Factura de Venta est sélectionné par défaut.

  * Lignes de facture : Précisez les produits avec les bonnes taxes.

Une fois que vous avez terminé, cliquez sur Confirmer.

#### Validation des factures

Après la confirmation de la facture, un fichier XML est créé et envoyé
automatiquement à Carvajal. La facture est ensuite traitée de manière
asynchrone par le service de facturation électronique UBL 2.1 (Colombie). Le
fichier s’affiche également dans le chatter.

![Fichier de facture XML Carvajal dans le chatter
d'Odoo.](../../../_images/invoice-sent.png)

The Electronic Invoice Name field is now displayed in the EDI Documents tab,
with the name of the XML file. Additionally, the Electronic Invoice Status
field is displayed with the initial value To Send. To process the invoice
manually, click on the Process Now button.

#### Réception des fichiers juridiques XML et PDF

The electronic invoice vendor (Carvajal) receives the XML file, and proceeds
to validate its structure and information.

Après avoir validé la facture électronique, générez un fichier XML légal, qui
inclut un signature numérique et un code unique (CUFE). Une facture PDF
comprenant un code QR et le CUFE est également généré. Si tout est correct, la
valeur du champ Facturation électronique passé à Envoyé.

A `.zip` containing the legal electronic invoice (in XML format) and the
invoice in (PDF format) is downloaded and displayed in the invoice chatter:

![Le fichier ZIP affiché dans le chatter de la facture dans
Odoo.](../../../_images/invoice-zip.png)

Le statut de la facture électronique passe à Accepté.

### Avoirs

The process for credit notes is the same as for invoices. To create a credit
note with reference to an invoice, go to Accounting ‣ Customers ‣ Invoices. On
the invoice, click Add Credit Note, and complete the following information:

  * Méthode de crédit : Sélectionnez le type de méthode de crédit.

    * Remboursement partiel : Utilisez cette option lorsqu’il s’agit d’un montant partiel.

    * Remboursement intégral : Utilisez cette option si l’avoir concerne le montant intégral.

    * Remboursement intégral et nouvelle facture brouillon : Utilisez cette option si l’avoir est validé automatiquement et lettré avec la facture. La facture originale est dupliquée comme un nouveau brouillon.

  * Motif : Saisissez le motif de l’avoir.

  * Date d’extourne : Sélectionnez si vous souhaitez une date spécifique pour l’avoir ou s’il s’agit de la date de la pièce comptable.

  * Utiliser un journal spécifique : Sélectionnez le journal pour votre avoir ou laissez-le vide si vous voulez utiliser le même journal que la facture originale.

  * Date de remboursement : Si vous avez choisi une date spécifique, sélectionnez la date pour le remboursement.

Une fois que vous avez terminé, cliquez sur le bouton Extourner.

### Notes de débit

The process for debit notes is similar to credit notes. To create a debit note
with reference to an invoice, go to Accounting ‣ Customers ‣ Invoices. On the
invoice, click the Add Debit Note button, and enter the following information:

  * Motif : Saisissez le motif de la note de débit.

  * Date de la note de débit : Sélectionnez les options spécifiques.

  * Copier les lignes : Sélectionnez cette option si vous devez enregistrer une note de débit avec les mêmes lignes que la facture.

  * Utiliser un journal spécifique : Sélectionnez le point d’impression pour votre note de débit ou laissez-le vide si vous voulez utiliser le même journal que la facture originale.

Une fois que vous avez terminé, cliquez sur Créer une note de débit.

### Document d’accompagnement pour les factures fournisseurs

With master data, credentials, and the purchase journal configured for support
documents related to vendor bills, you can start using _support documents_.

Les documents d’accompagnement pour les factures fournisseurs peuvent être
créés manuellement ou à partir de votre bon de commande. Allez à Comptabilité
‣ Fournisseurs ‣ Factures fournisseurs et saisissez les données suivantes :

  * Fournisseur : Saisissez les informations du fournisseur.

  * Date de facturation : Sélectionnez la date de la facture.

  * Journal : Sélectionnez le journal pour les documents d’accompagnement relatifs aux factures fournisseurs.

  * Lignes facturées : Précisez les produits avec les bonnes taxes.

Une fois que vous avez terminé, cliquez sur le bouton Confirmer. Après
confirmation, un fichier XML est créé et envoyé automatiquement à Carvajal.

### Erreurs courantes

Pendant la validation XML, les erreurs les plus courantes sont liées aux
données de base manquantes (_N° TVA du contact_ , _Adresse_ , _Produits_ ,
_Taxes_). Dans ces cas, les messages d’erreur s’affichent dans le chatter
après avoir mis à jour le statut de la facture électronique.

Après avoir corrigé les données de base, il est possible de retraiter le XML
avec les nouvelles données et d’envoyer la version mise à jour à l’aide du
bouton Réessayer.

![Erreurs de validation XML affichées dans le chatter de la facture dans
Odoo.](../../../_images/xml-validation-error.png)

## Rapports financiers

### Certificado de Retención en ICA

Ce rapport certifie aux fournisseurs les retenues effectuées au titre de
l’impôt colombien sur l’industrie et le commerce (ICA). Ce rapport se trouve
sous Comptabilité ‣ Rapports ‣ Relevés colombiens ‣ Certificado de Retención
en ICA.

![Rapport Certificado de Retención en ICA dans Odoo
Comptabilité.](../../../_images/ica-report.png)

### Certificado de Retención en IVA

Ce rapport certifie le montant retenu auprès des fournisseurs pour la retenue
de la TVA. Ce rapport se trouve sous Comptabilité ‣ Rapports ‣ Relevés
colombiens ‣ Certificado de Retención en IVA.

![Rapport Certificado de Retención en IVA dans Odoo
Comptabilité.](../../../_images/iva-report.png)

### Certificado de Retención en la Fuente

Ce certificat est délivré aux partenaires pour la retenue à la source qu’ils
ont effectuée. Le rapport se trouve sous Comptabilité ‣ Rapports ‣ Relevés
colombiens ‣ Certificado de Retención en Fuente.

![Rapport Certificado de Retención en Fuente dans Odoo
Comptabilité.](../../../_images/fuente-report.png)

  *[DIAN]: Dirección de Impuestos y Aduanas Nacionales
  *[RUT]: Registro único tributario

