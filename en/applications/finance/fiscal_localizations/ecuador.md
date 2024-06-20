# Ecuador

## Introduction

With the Ecuadorian localization you can generate electronic documents with
its XML, Fiscal folio, with electronic signature and direct connection to tax
authority SRI.

The supported documents are Invoices, Credit Notes, Debit Notes, Purchase
Liquidations and Withholds.

The localization also Includes automations to easily predict the withholding
tax to be applied to each purchase invoice.

See also

  * [App Tour - Localización de Ecuador](https://www.youtube.com/watch?v=BQOXVSDeeK8)

  * [Smart Tutorial - Localización de Ecuador](https://www.odoo.com/slides/smart-tutorial-localizacion-de-ecuador-170)

### Glossary

Here are some terms that are essential on the Ecuadorian localization:

  * **SRI** : meaning _Servicio de Rentas Internas_ , the government organization that enforces pay of taxes in Ecuador.

  * **EDI** : stands for _Electronic Data Interchange_ , which refers to the sending of Electronics Documents.

  * **RIMPE** : stands for _Regimen Simplificado para Emprendedores y Negocios_ , the type of taxpayer qualified for SRI.

## Configuration

### Modules installation

[Install](../../general/apps_modules.html#general-install) the following
modules to get all the features of the Ecuadorian localization:

Name | Technical name | Description  
---|---|---  
Ecuadorian - Accounting | `l10n_ec` | The default [fiscal localization package](../fiscal_localizations.html), adds accounting characteristics for the Ecuadorian localization, which represent the minimum configuration required for a company to operate in Ecuador according to the guidelines set by the SRI. The module’s installation automatically loads: Chart of Accounts, taxes, documents types, tax support types. Additionally, the generation of forms 103 and 104 are automatic.  
Ecuadorian Accounting EDI | `l10n_ec_edi` | Includes all the technical and functional requirements to generate and validate [Electronics Documents](../accounting/customer_invoices/electronic_invoicing.html), based on the Technical documentation published by the SRI. The authorized documents are: Invoices, Credit Notes, Debit Notes, Withholdings and Purchase liquidations.  
  
Note

When you install a database from scratch selecting `Ecuador` as the country,
Odoo automatically installs the base module Ecuadorian - Accounting.

### Configure your company

To configure your company information, go to the Contacts app and search the
name given to your company or activate [developer
mode](../../general/developer_mode.html#developer-mode) and go to Company ‣
Contact and then edit the contact to configure the following information:

  1. Check the Company option on top

     * Name

     * Address

     * Identification Number

     * Taxpayer Type

     * Phone

     * Email

  2. Upload company logo and save

![Populate company data for Ecuador in Odoo
Contacts.](../../../_images/ecuador-company.png)

### Electronic documents

To upload your information for electronic documents go to Accounting ‣
Configuration ‣ Settings and search for **Ecuadorian Localization**.

Configure the next information:

  * Company legal name

  * Use production servers: check the checkbox if your company is going to do electronic documents in the production environment. If you want to use the testing environment for electronic documents then keep the checkbox unchecked.

  * Regime: select if your company is in General Regular or is qualified as RIMPE.

  * Forced to keep accounting books: check the checkbox if your company has this condition.

  * Default taxes for withholdings

  * Issue withholds: check the checkbox if your company is going to do electronic withholds.

  * Withhold consumibles: put the code of the withholding for when you buy goods.

  * Withhold services: put the code of the withholding for when you buy services.

  * Withhold credit card: put the code of the withholding for when you buy with credit card

  * Withhold agent number: put the company withholding agent resolution number, if applicable for your company.

  * Electronic Certificate File: upload electronic certificate and password, then save it.

  * Special tax contributor number: if your company is qualified as a special taxpayer, fill out this field with it’s corresponding tax contributor number.

![Electronic signature for Ecuador.](../../../_images/electronic-
signature.png)

Note

When configuring the withholdings in the configuration menu, these suggested
withholdings are only for domestic suppliers when no withholdings are setup on
their _Taxpayer Type_. Moreover, the Credit Card withholding set up is always
used when a Credit or Debit Card SRI Payment Metho is used.

### VAT withholding

This configuration only applies if you are qualified as a _Withholding Agent_
by the SRI, otherwise skip this step. To configure your VAT withholding, go to
Accounting ‣ Accounting ‣ Configuration ‣ Ecuadorian SRI: Taxpayer Type SRI.

You must configure the withholding percentage that applies for each type of
taxpayer, specify the Goods VAT Withholding and the Services VAT Withholding.

![Taxpayer Type configuration for Ecuador.](../../../_images/contributor-
type.png)

Tip

In the case that the Taxpayer Type is `RIMPE`, also configure the Profit
Withholding percentage.

### Printer points

To configure your printer points, go to Accounting ‣ Configuration ‣
Accounting: Journals.

Printer points need to be configured for each type of electronic document that
you need. For example: Customer Invoice, Credit Notes, and Debit Notes

For each printer point, you need to configure the following information:

  * Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for example: `001-001 Sales Documents`.

  * Type: refers to the type of journal, select `Sales`.

  * Use Documents?: this checkbox is automatically checked, leave it checked.

  * Emission Entity: configure the establishment number.

  * Emission Point: configure the printer point.

  * Emission address: configure the address of the establishment.

  * Default income account: configure the default income account.

  * Dedicated Credit Note Sequence: check the checkbox if _Credit Notes_ are to be generated from this printer point - journal.

  * Short Code: This is the unique code for the sequence of accounting entries, enter a unique 5-digit code, for example: `VT001`

Customer Invoice, Credit Notes and Debit Notes need to use the same journal as
the Emission Point, and the Entity Point should be unique per journal.

![Configuring a printer point for Ecuador electronic document type of Customer
Invoices.](../../../_images/printer-point.png)

Note

In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable it for Ecuador.

See also

[Electronic invoicing
(EDI)](../accounting/customer_invoices/electronic_invoicing.html)

### Withholding

A Withholding Journal must be defined, go to go to Accounting ‣ Configuration
‣ Accounting: Journals where you need to configure the following information:

  * Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for example: `001-001 Withholding`.

  * Type: refers to the type of journal, select `Miscellaneous`.

  * Withhold Type: Configure Purchase Withholding.

  * Use Documents?: this checkbox is automatically checked, leave it checked.

  * Emission Entity: configure the establishment number.

  * Emission Point: configure the printer point.

  * Emission address: configure the address of the establishment.

  * Default account: configure the default income account.

  * Short Code: This is the unique code for the sequence of accounting entries, enter a unique 5-digit code, for example: `RT001`

![Configuring withholding for Ecuador electronic document type of
Withholding.](../../../_images/withhold.png)

Note

In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable the sending of electronic invoicing for the withholding.

### Purchase Liquidations

When using Purchase Liquidations, a specific journal must be created, go to
Accounting ‣ Configuration ‣ Accounting: Journals and configure the following
information:

  * Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for example: `001-001 Withhold`.

  * Type: refers to the type of journal, select `Miscellaneous`.

  * Purchase Liquidations: check the checkbox to enable purchase liquidations.

  * Use Documents?: this checkbox is automatically checked, leave it checked.

  * Emission Entity: configure the establishment number.

  * Emission Point: configure the printer point.

  * Emission address: configure the address of the establishment.

  * Short Code: This is the unique code for the sequence of accounting entries, enter a unique 5-digit code, for example: `RT001`

![Configuring purchase liquidations for Ecuador electronic document type of
Withholding.](../../../_images/purchase-liqudations.png)

Note

In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable the sending of electronic invoicing for the withholding.

### Configure master data

#### Chart of accounts

The [chart of accounts](../accounting/get_started/chart_of_accounts.html) is
installed by default as part of the set of data included in the localization
module, the accounts are mapped automatically in Taxes, Default Account
Payable, Default Account Receivable.

The chart of accounts for Ecuador is based on the most updated version of
Superintendency of Companies, which is grouped in several categories and is
compatible with NIIF accounting.

You can add or delete accounts according to the company’s needs.

#### Products

In addition to the basic information in your products, you must add the
configuration of the withholding code (tax) that applies.

Go to Accounting ‣ Vendors: Products under the tab “Purchase”

![Product for Ecuador.](../../../_images/products.png)

#### Contacts

Configure the next information when you create a contact:

  * Check the Company option on top if it is a contact with RUC, or check Individual if it is a contact with cedula or passport.

  * Name

  * Address: Street is a required field to confirm the Electronic Invoice.

  * Identification Number: select an identification type `RUC`, `Cedula`, or `Passport`.

  * Taxpayer Type: select the contact’s SRI Taxpayer Type.

  * Phone

  * Email

![Contacts for Ecuador.](../../../_images/contacts.png)

Note

The SRI Taxpayer Type has inside the configuration of which VAT and Profit
withholding will apply when you use this contact on Vendor Bill, and then
create a withholding from there.

#### Review your taxes

As part of the localization module, taxes are automatically created with its
configuration and related financial accounts.

![Taxes for Ecuador.](../../../_images/taxes.png)

The following options have been automatically configured:

  * Tax Support: to be configured only in the IVA tax, this option is useful when you register purchase withholdings.

  * Code ATS: to be configured only for income tax withholding codes, it is important when you register the withholding.

  * Tax Grids: configure the codes of 104 form if it is a IVA tax and configure the codes of 103 form if it is a income tax withholding code.

  * Tax Name:

    * For IVA tax, format the name as: `IVA [percent] (104, [form code] [tax support code] [tax support short name])`

    * For income tax withholding code, format the name as: `Code ATS [Percent of withhold] [withhold name]`

Once the Ecuador module is installed, the most common taxes are automatically
configured. If you need to create an additional one, you can do so, for which
you must base yourself on the configuration of the existing taxes.

![Taxes with tax support for Ecuador.](../../../_images/taxes-with-tax-
support.png)

#### Review your Document Types

Some accounting transactions like _Customer Invoices_ and _Vendor Bills_ are
classified by document types. These are defined by the government fiscal
authorities, in this case by the SRI.

Each document type can have a unique sequence per journal where it is
assigned. As part of the localization, the document type includes the country
on which the document is applicable; also the data is created automatically
when the localization module is installed.

The information required for the document types is included by default so the
user does not need to fill anything there.

![Document types for Ecuador.](../../../_images/document-types.png)

## Workflows

Once you have configured your database, you can register your documents.

### Sales documents

#### Customer invoices

Customer invoices are electronic documents that, when validated, are sent to
SRI. These documents can be created from your sales order or manually. They
must contain the following data:

  * Customer: type the customer’s information.

  * Journal: select the option that matches the printer point for the customer invoice.

  * Document Type: type document type in this format `(01) Invoice`.

  * Payment Method (SRI): select how the invoice is going to be paid.

  * Products: specify the product with the correct taxes.

![Customer invoice for Ecuador.](../../../_images/customer-invoice.png)

#### Customer credit note

The [Customer credit note](../accounting/customer_invoices/credit_notes.html)
is an electronic document that, when validated, is sent to SRI. It is
necessary to have a validated (posted) invoice in order to register a credit
note. On the invoice there is a button named Credit note, click on this button
to be directed to the Create credit note form, then complete the following
information:

  * Credit Method: select the type of credit method.

    * Partial Refund: use this option when you need to type the first number of documents and if it is a partial credit note.

    * Full Refund: use this option if the credit note is for the total invoice and you need the credit note to be auto-validated and reconciled with the invoice.

    * Full refund and new draft invoice: use this option if the credit note is for the total invoice and you need the credit note to be auto-validated and reconciled with the invoice, and auto-create a new draft invoice.

  * Reason: type the reason for the credit note.

  * Rollback Date: select the specific options.

  * Reversal Date: type the date.

  * Use Specific Journal: select the printer point for your credit note, or leave it empty if you want to use the same journal as the original invoice.

Once reviewed, you can click on the Reverse button.

![Add Customer Credit Note for Ecuador.](../../../_images/add-customer-credit-
note.png)

When the Partial Refund option is used, you can change the amount of the
credit note and then validate it. Before validating the credit note, review
the following information:

  * Customer: type the customer’s information.

  * Journal: select the printer point for the customer Credit Note.

  * Document Type: this is the document type `(04) Credit Note`.

  * Products: It must specify the product with the correct taxes.

![Customer Credit Note for Ecuador.](../../../_images/customer-credit-
note.png)

#### Customer debit note

The Customer debit note is an electronic document that, when validated, is
sent to SRI. It is necessary to have a validated (posted) invoice in order to
register a debit note. On the invoice there is a button named Debit Note,
click on this button to be directed to the Create debit note form, then
complete the following information:

  * Reason: type the reason for the debit note.

  * Debit note date: select the specific options.

  * Copy lines: select this option if you need to register a debit note with the same lines of invoice.

  * Use Specific Journal: select the printer point for your credit note, or leave it empty if you want to use the same journal as the original invoice.

Once reviewed you can click on the Create Debit Note button.

![Add Customer Debit Note for Ecuador.](../../../_images/add-customer-debit-
note.png)

You can change the debit note amount, and then validate it. Before validating
the debit note, review the following information:

  * Customer: type the customer’s information.

  * Journal: select the printer point for the customer Credit Note.

  * Document Type: this is the document type `(05) Debit Note`.

  * Products: It must specify the product with the correct taxes.

![Customer Debit Note for Ecuador.](../../../_images/customer-debit-note.png)

#### Customer withholding

The Customer withholding is a non-electronic document for your company, this
document is issued by the client in order to apply a withholding to the sale.

It is necessary to have a validated (posted) invoice in order to register a
customer withholding. On the invoice there is a button named Add Withhold,
click on this button to be directed to the Customer withholding form, then
complete the following information:

  * Document Number: type the withholding number.

  * Withhold Lines: select the taxes that the customer is withholding.

Before validating the withholding, review that the amounts for each tax are
the same as the original document.

![Customer withhold for Ecuador.](../../../_images/customer-withhold.png)

### Purchase Documents

#### Vendor bill

The Vendor bill is a non-electronic document for your company, this document
is issued by your vendor when your company generates a purchase.

The bills can be created from the purchase order or manually, it must contain
the following information:

  * Vendor: type the vendor’s information.

  * Bill Date: select the date of invoice.

  * Journal: it is the journal for vendor bills.

  * Document Type: this is the document type `(01) Invoice`

  * Document number: type the document number.

  * Payment Method (SRI): select how the invoice is going to be paid.

  * Products: specify the product with the correct taxes.

![Purchases for Ecuador.](../../../_images/purchase-invoice.png)

Important

When creating the purchase withholding, verify that the bases (base amounts)
are correct. If you need to edit the amount of the tax in the Vendor bill,
click the Edit button. Otherwise, from the Journal Items tab click the Edit
button and set the adjustment to go where you want.

#### Purchase liquidation

The Purchase liquidation is an electronic document that, when validated, is
sent to SRI.

Companies issue this type of electronic document when they purchase, and the
vendor does not issue an invoice due to one or more of the following cases:

  * Services were provided by non-residents of Ecuador.

  * Services provided by foreign companies without residency or establishment in Ecuador.

  * Purchase of goods or services from natural persons not registered with a RUC, who due to their cultural level or hardiness are not able to issue sales receipts or customer invoices.

  * Reimbursement for the purchase of goods or services to employees in a dependency relationship (full-time employee).

  * Services provided by members of collegiate bodies for the exercise of their function.

These types of electronic documents can be created from the Purchase Order or
manually from the Vendor Bills form view. It must contain the following data:

  * Vendor: type the vendor’s information.

  * Journal: select the journal for the Purchase Liquidation with the correct printer point.

  * Document Type: this is the document type `(03) Purchase Liquidation`

  * Document number: type the document number (sequence), you will only have to do this once, then the sequence will be automatically assigned for the next documents.

  * Payment Method (SRI): select how the invoice is going to be paid.

  * Products: specify the product with the correct taxes.

Once you review the information you can validate the Purchase Liquidation.

![Purchase liquidation for Ecuador.](../../../_images/purchase-
liquidation.png)

#### Purchase withholding

The Purchase withholding is an electronic document that, when validated, is
sent to SRI.

It is necessary to have an invoice in a validated state in order to register a
Purchase withholding. On the invoice, there is a button named Add Withhold,
click on this button to be directed to the Withholding form, then complete the
following information:

  * Document number: type the document number (sequence), you will only have to do this once, then the sequence will be automatically assigned for the next documents.

  * Withhold lines: The taxes appear automatically according to the configuration of products and vendors, you should review if the taxes and tax support are correct, and, if it is not correct, you can edit and select the correct taxes and tax support.

Once you review the information you can validate the Withholding.

![Purchase withhold for Ecuador.](../../../_images/purchase-withhold.png)

Note

You can’t change the tax support for one that was not included in the
configuration of the taxes used on the Vendor Bill. To do so, go to the tax
applied on the Vendor Bill and change the Tax Support there.

A withholding tax can be divided into two or more lines, this will depend on
whether two or more withholdings percentages apply.

Example

The system suggests a VAT withholding of 30% with tax support 01, you can add
your VAT withholding of 70% in a new line with the same tax support, the
system will allow you as long as the total of the bases matches the total from
the Vendor Bill.

## Financial Reports

In Ecuador, there are fiscal reports that the company presents to SRI. In
Odoo, we have two of the main financial reports used by companies. These are
the reports 103 and 104.

To get these reports go to the Accounting app and select Reporting ‣
Statements Reports ‣ Tax Report and then filter by `Tax Report 103` or `Tax
Report 104`.

### Report 103

This report contains information of income tax withholdings in a given period,
this can be reported monthly or semi-annually.

You can see the information needed to report, which includes base and tax
amounts, which also includes the tax code within the parenthesis in order to
report it to the SRI.

![Report 103 form for Ecuador.](../../../_images/103-form.png)

### Report 104

This report contains information on VAT tax and VAT withholding for a given
period, this can be monthly or semi-annually.

You can see the information needed to report, which includes base and tax
amounts, which also includes the tax code within the parenthesis in order to
report it to the SRI.

![Report 104 form for Ecuador.](../../../_images/104-form.png)

### ATS report

[Install](../../general/apps_modules.html#general-install) the _ATS Report_
(`l10n_ec_reports_ats`) module to enable downloading the ATS report in XML
format.

Note

The Ecuadorian _ATS Report_ module is dependent on the previous installation
of the _Accounting_ app and the _Ecuadorian EDI module_.

#### Configuration

To issue electronic documents, ensure your company is configured as explained
in the electronic invoice section.

In the ATS, every document generated in Odoo (invoices, vendor bills, sales
and purchases withholdings, credit notes, and debit notes) will be included.

##### Vendor bills

When generating a vendor bill, it is necessary to register the authorization
number from the invoice that the vendor generated for the purchase. To do so,
go to Accounting ‣ Vendors ‣ Bills and select the bill. Then, enter the number
from the vendor’s invoice in the Authorization Number field.

##### Credit and debit notes

When generating a credit note or debit note manually or through importation,
it is necessary to link this note to the sales invoice that is being modified
by it.

Note

Remember to add all required information to the documents before downloading
the ATS file. For example, add the _Authorization Number_ and the _SRI Payment
Method_ on documents, when needed.

#### XML generation

To generate the ATS report, go to Accounting ‣ Reports ‣ Tax Report and choose
a time period for the desired ATS report, then click ATS.

The downloaded XML file is ready to be uploaded to _DIMM Formularios_.

![ATS report download for Ecuador in Odoo Accounting.](../../../_images/ats-
report.png)

Note

When downloading the ATS report, Odoo generates a warning pop-up alerting the
user if a document(s) has missing or incorrect data. Nevertheless, the user
can still download the XML file.

  *[SRI]: servicio de rentas internas
  *[ATS]: Anexo Transaccional Simplificado

