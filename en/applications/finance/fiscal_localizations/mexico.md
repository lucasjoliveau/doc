# Mexico

## Webinars

A video on the Mexican localization is also available. This video covers how
to implement this localization from scratch, including how to set up the
configurations, how to complete common workflows, and provides an in-depth
look at several specific use cases, as well.

  * [Video webinar of a complete demo](https://www.youtube.com/watch?v=5cdogjm0GCI).

## Introduction

The Konvergo ERP Mexican localization modules allow for the signing of electronic
invoices, according to the specifications of the SAT for [version 4.0 of the
CFDI](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo_20_Guia_de_llenado_CFDI.pdf),
a legal requirement, as of January 1, 2022. These modules also add relevant
accounting reports (such as: the DIOT, enables foreign trade, and the creation
of delivery guides).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In order to electronically sign any documents in Konvergo ERP, ensure the <em>Sign</em> application is
installed.</p>
</div>

## Configuration

### Requirements

It is necessary to meet the following requirements before configuring the
Mexican localization modules in Konvergo ERP:

  1. Be registered in the SAT, with a valid RFC.

  2. Have a [Certificate of Digital Seal](https://www.gob.mx/sat/acciones-y-programas/certificado-de-sello-digital) (CSD).

  3. Choose a PAC (Proveedor Autorizado de Certificación / Authorized Certification Provider). Currently, Konvergo ERP works with the following PACs: [Solución Factible](https://solucionfactible.com/), [Quadrum (formerly Finkok)](https://cfdiquadrum.com.mx/) and [SW Sapien - Smarter Web](https://sw.com.mx/).

  4. Have knowledge and experience with billing, sales, and accounting in Konvergo ERP. This documentation **only** contains the necessary information needed to use Konvergo ERP.

### Installing modules

[Install](../../general/apps_modules#general-install) the following
modules to get all the features of the Mexican localization. The
[Accounting](../accounting) and _Contacts_ modules are required to be
installed for this configuration:

Name | Technical name | Description  
---|---|---  
**Mexico - Accounting** | `l10n_mx` | The default [fiscal localization package](../fiscal_localizations), adds accounting characteristics for the Mexican localization, such as: the most common taxes and the chart of accounts – based on [the SAT account grouping code](https://www.gob.mx/cms/uploads/attachment/file/151586/codigo_agrupador.pdf).  
**EDI for Mexico** | `l10n_mx_edi` | Includes all the technical and functional requirements to generate and validate [Electronics Documents](../accounting/customer_invoices/electronic_invoicing) — based on the technical documentation published by the SAT. This allows you to send invoices (with or without addedums) and payment complements to the government.  
**EDI v4.0 for Mexico** | `l10n_mx_edi_40` | Necessary to create XML documents with the correct specifications of the CFDI 4.0.  
**Konvergo ERP Mexican Localization Reports** | `l10n_mx_reports` | Adapts reports for Mexico’s Electronic Accounting: Chart of Accounts, Trial Balance, and DIOT.  
**Mexico - Localization Reports for Closing** | `l10n_mx_reports_closing` | Necessary to create the Closing Entry (Also known as the _month 13th move_).  
**Konvergo ERP Mexican XML Polizas Export** | `l10n_mx_xml_polizas` | Allows the export of XML files of Journal Entries for a compulsory audit.  
**Konvergo ERP Mexican XML Polizas Export Edi bridge** | `l10n_mx_xml_polizas_edi` | Complements the module `l10n_mx_xml_polizas`.  
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>

The following modules are optional. It’s recommended to install them _only_ if
meeting a specific requirement. Make sure that they are needed for the
business.

Name | Technical name | Description  
---|---|---  
**EDI for Mexico (Advanced Features)** | `l10n_mx_edi_extended` | Adds the external trade complement to invoices: A legal requirement for selling products to foreign countries.  
**EDI v4.0 for Mexico (COMEX)** | `l10n_mx_edi_extended_40` | Adapts the module `l10n_mx_edi_extended` for CFDI 4.0.  
**Mexico - Electronic Delivery Guide** | `l10n_mx_edi_stock` | Lets you create a _Carta Porte_ : A bill of lading that proves to the government you are sending goods between A & B with a signed electronic document.  
**Electronic Delivery Guide for Mexico CFDI 4.0** | `l10n_mx_edi_stock_40` | Adapts the module `l10n_mx_edi_stock` for CFDI 4.0  
**Konvergo ERP Mexico Localization for Stock/Landing** | `l10n_mx_edi_landing` | Allows managing customs numbers related to landed costs in electronic documents.  
  
### Configure your company

After installing the correct modules, the next step is to verify that your
company is configured with the correct data. To do so, go to Settings ‣
General Settings ‣ Companies, and select **Update Info** under your company
name.

Enter the full **Address** in the resulting form, including: **ZIP** code,
**State** , **Country** , and RFC (**VAT** number).

According to the requirements of the CFDI 4.0, the name of the main company
contact **must** coincide with your business name registered in the SAT,
without the legal entity abbreviation.

![Main company contact requirements for a correct
invoicing.](../../../_images/mx-company-info.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>

Next, go to Settings ‣ Accounting ‣ Electronic Invoicing (MX) ‣ Fiscal Regime,
then select the regime that applies to your company from the drop-down list,
and click **Save**.

![Fiscal regime configuration in the Accounting
settings.](../../../_images/mx-fiscal-regime.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>

### Contacts

To create a contact that can be invoiced, go to Contacts ‣ Create. Then, enter
the contact name, full **Address** including: **ZIP** code, **State** ,
**Country** , and RFC (**VAT** number).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>As with your own company, all of your contacts needs to have their correct business name
registered in the <abbr title="Servicio de Administración Tributaria">SAT</abbr>. This also applies to the <b>Fiscal Regime</b>, which needs to be
added in the <b>MX EDI</b> tab.</p>
</div>

### Taxes

Some additional configurations for factor type and tax objects need to be
added to the sales taxes in order to properly sign invoices.

#### Factor type

The _Factor Type_ field is pre-loaded in the default taxes. If new taxes are
created, you need to make sure to configure this field. To do so, go to
Accounting ‣ Configuration ‣ Taxes, then enable the **Factor Type** field in
the **Advanced Options** tab for all records, with the **Tax Type** set as
**Sales**.

![Factor Type Sales tax type configuration.](../../../_images/mx-factor-
type.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Mexico manages two different kinds of 0% VAT to accommodate two scenarios:</p>
<ul>
<li><p><em>0% VAT</em> set the <b>Factor Type</b> as <b>Tasa</b></p></li>
<li><p><em>VAT Exempt</em> set the <b>Factor Type</b> as <b>Exento</b></p></li>
</ul>
</div>

#### Tax object

One requirement of the CFDI 4.0 is that the resulting XML file needs (or does
not need) to break down the taxes of the operation. There are three different
possible values that are added in the XML file:

  * `01`: Not subject to tax - this value is added automatically if your invoice line doesn’t contain any taxes.

  * `02`: Subject to tax - this is the default configuration of any invoice line that contains taxes.

  * `03`: Subject to tax and not forced to break down - this value can be triggered on-demand for certain customers to replace the value 02.

To use the `03` value, navigate to Contacts ‣ your customer’s invoice ‣ MX EDI
tab, and activate the **No Tax Breakdown** checkbox.

![No Tax Breakdown option on the MX EDI tab of the customer's
invoice.](../../../_images/mx-tax-breakdown.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <b>No Tax Breakdown</b> value applies <b>only</b> to specific fiscal regimes and/or taxes.
Consult your accountant first to see if it is needed for your business before making any
modification.</p>
</div>

#### Other tax configurations

When registering a payment, Konvergo ERP will carry out the movement of taxes from the
_Cash Basis Transition Account_ to the account set in the **Definition** tab.
For such movement, a tax base account will be used: (`Base Imponible de
Impuestos en Base a Flujo de Efectivo`) in the journal entry when
reclassifying taxes. **Do not delete this account**.

If you create a new tax in Accounting ‣ Configuration ‣ Taxes, you need to add
the correct **Tax Grids** for it (`IVA`, `ISR` or `IEPS`). Konvergo ERP **only**
supports these three groups of taxes.

![Tax accounts available for Konvergo ERP.](../../../_images/mx-taxes-config.png)

### Products

To configure products, go to Accounting ‣ Customers ‣ Products, then select a
product to configure, or **Create** a new one. In the **Accounting** tab, and
in the **UNSPSC Product Category** field, select the category that represents
the product. The process can be done manually, or through [a bulk
import](../../essentials/export_import_data).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>All products need to have an <abbr title="Servicio de Administración Tributaria">SAT</abbr> code associated with them in order to prevent validation
errors.</p>
</div>

### Electronic invoicing

#### PAC credentials

After you have processed your [Private Key
(CSD)](https://www.sat.gob.mx/aplicacion/16660/genera-y-descarga-tus-archivos-
a-traves-de-la-aplicacion-certifica) with the SAT, you **must** register
directly with the PAC of your choice before you start creating invoices from
Konvergo ERP.

Once you’ve created your account with any of these providers, go to Settings ‣
Accounting ‣ Electronic Invoicing (MX). Under the **MX PAC** section, enter
the name of your PAC with your credentials (**PAC username** and **PAC
password**).

![Configuring PAC credentials from the Accounting
settings.](../../../_images/mx-pac-account.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you do not have credentials, but want to test the electronic invoicing, you can activate the
<b>MX PAC test environment</b> checkbox, and select <b>Solucion Factible</b> as the
<abbr title="Proveedor Autorizado de Certificación / Authorized Certification Provider">PAC</abbr>. You do not need to add a username or password for a test environment.</p>
</div>

#### .cer and .key certificates

The [digital certificates of the
company](https://www.gob.mx/tramites/ficha/certificado-de-sello-
digital/SAT139) must be uploaded within the **MX Certificates** section. To do
so, navigate to Settings ‣ Accounting ‣ Electronic Invoicing (MX). Under the
**MX Certificates** section, select **Add a line** , and a window will open.
Click **Create** , and from there, upload your digital **Certificate** (`.cer`
file), your **Certificate Key** (`.key` file), and your **Certificate
Password**. To finish, click on **Save & Close**.

![Certificate and key upload inputs.](../../../_images/mx-certificates.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you still do not have one of the contracted <abbr title="Proveedor Autorizado de Certificación / Authorized Certification Provider">PAC</abbr>s and you want to test electronic invoicing,
you can use the following <abbr title="Servicio de Administración Tributaria">SAT</abbr> test certificates:</p>
<ul>
<li><p><a download="" href="../../../_downloads/b59328d6458977aebd30f2f8286679e1/certificate.cer"><code>Certificate</code></a></p></li>
<li><p><a download="" href="../../../_downloads/19f36789d1d2bc50ef639d1141721304/certificate.key"><code>Certificate Key</code></a></p></li>
<li><p><b>Password</b>: <code>12345678a</code></p></li>
</ul>
</div>

## Workflows

### Electronic invoicing

The invoicing process in Konvergo ERP is based on [Annex
20](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm) version
4.0 of electronic invoicing of the SAT.

#### Customer invoices

To start invoicing from Konvergo ERP, a customer invoice must be created using the
[standard invoicing flow](../accounting/customer_invoices).

While the document is in draft mode, changes can be made to it (the correct
**Payment Way** or **Usage** that the customer might require can be added, for
example.)

After you **Confirm** the customer invoice, a blue message appears stating:
**The invoice will be processed asynchronously by the following E-invoicing
service: CFDI (4.0)**.

Pressing the **Process Now** button sends the document to the government so it
can be signed. After receiving the signed document back from the government,
the **Fiscal Folio** field appears on the document, and the XML file is
attached in the chatter.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>0

To send the signed invoice to your client by mail, you can send both the XML
and PDF files together, directly from Konvergo ERP, by clicking the **Send & Print**
button. You can also download the PDF file to your computer, by clicking the
**Print** button, and selecting the desired print option.

#### Credit notes

While an invoice is a document type “I” (Ingreso), a credit note is a document
type “E” (Egreso).

The only addition to the [standard flow for credit
notes](../accounting/customer_invoices/credit_notes) is that, as a
requirement of the SAT, there has to be a relation between a credit note and
an invoice through the fiscal folio.

Because of this requirement, the field **CFDI Origin** adds this relation with
a `01|`, followed by the fiscal folio of the original invoice.

![Example CFDI Origin number.](../../../_images/mx-creating-credit-note.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>1

#### Payment complements

##### Payment policy

One addition of the Mexican localization is the **Payment Policy** field .
[According to the SAT
documentation](https://www.sat.gob.mx/consultas/92764/comprobante-de-
recepcion-de-pagos), there may be 2 types of payments:

  * `PUE` (Pago en una Sola Exhibición/Payment in a Single Exhibition)

  * `PPD` (Pago en Parcialidades o Diferido/Payment in Installements or Deferred)

> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>2

The difference lies in the _Due Date_ or _Payment Terms_ of the invoice.

To configure PUE invoices, navigatge to Accounting ‣ Customers ‣ Invoices, and
either select an invoice **Due Date** within the same month, or choose a
payment term that does not imply changing the due month (immediate payment, 15
days, 21 days, all falling within the current month).

![Example of an invoice with the PUE requirements.](../../../_images/mx-pue-
payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>3

To configure PPD invoices, navigate to Accounting ‣ Customers ‣ Invoices, and
select an invoice with a **Due Date** after the first day of the following
month. This also applies if your **Payment Term** is due in the following
month.

![Example of an invoice with the PPD requirements.](../../../_images/mx-ppd-
payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>4

##### Payment flow

In both cases, the payment process in Konvergo ERP [is the
same](../accounting/customer_invoices), the main difference being
payments related to PPD invoices trigger the creation of a document type “P”
(Pago).

If a payment is related to a PUE invoice, it can be registered with the
wizard, and be associated with the corresponding invoice. To do so, navigate
to Accounting ‣ Customers ‣ Invoices, and select an invoice. Then, click the
**Register Payment** button. The invoice status changes to **In Payment** ,
since the payment is effectively validated when it is bank reconciled.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>5

While this process is the same for PPD invoices, the addition of the creating
an [electronic
document](../accounting/customer_invoices/electronic_invoicing) means
some additional requirements are needed to correctly send the document to the
SAT.

From an invoice, you need to confirm the specific **Payment Way** where you
received the payment. Because of this, the **Payment Way** field **cannot** be
set as `99 - Por Definir (To Define)`.

If you are going to add a bank account number in the **Accounting** tab of a
customer’s contact card, it must have a valid account number.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>6

If a payment is related to a signed invoice with the **Payment Policy** `PPD`,
Konvergo ERP generates the corresponding payment complement automatically, once you
click **Process Now**.

![CFDI \(4.0\) E-invoicing service process payment now
message.](../../../_images/mx-signed-complement.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>7

#### Invoice cancellations

It is possible to cancel the EDI documents sent to the SAT. According to the
[Reforma Fiscal 2022](https://www.sat.gob.mx/consultas/91447/nuevo-esquema-de-
cancelacion), since January 1st, 2022, there are two requirements for this:

  * With all cancellation requests, you **must** specify a _cancellation reason_.

  * After 24 hours have passed since the creation of the invoice, the client **must** be asked to accept the cancellation.

There are four different cancellation reasons. In Konvergo ERP, you can cancel
invoices with the reasons _01 Invoices sent with errors with a relation_ , and
_02 Invoices sent with errors without a relation_.

The following sections break down the process of canceling invoices for each
cancellation reason in Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>8

##### 01 - invoices sent with errors with a relation

This cancellation reason must be used when a new invoice needs to substitute
the original one, due to an error in any field.

Begin by navigating to Accounting ‣ Customers ‣ Invoices, and select the old
invoice. Copy the **Fiscal Folio** from the old invoice. Then, navigate to the
new invoice, and in the **CFDI Origin** field, add the value `04|` and paste
the **Fiscal Folio** of the old invoice after the value. Finally, sign the new
document.

Next, navigate back to the old invoice, and notice the **Substituted By**
field is now available. Click the **Request EDI Cancellation** button on the
old invoice, and then click **Process Now** in the blue section that appears.
The invoice status changes to **Canceled** , and a confirmation is logged in
the chatter.

Now, the invoice should be canceled in the SAT as well. You can confirm this
was done correctly, by pressing **Retry** in the SAT status field.

If the document was canceled more than 24 hours after its creation, you may
need to ask the client to accept the cancellation in their “Buzón Tributario”
directly from the [SAT website](https://www.sat.gob.mx/home).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When installing a database from scratch and selecting <b>Mexico</b> as the country, Konvergo ERP
automatically installs the following modules: <b>Mexico - Accounting</b>, <b>EDI for
Mexico</b>, and <b>EDI v4.0 for Mexico</b>.</p>
</div>9 ![Old invoice with CFDI
Origin.](../../../_images/mx-01-invoice-cancellation-substitute.png) ![Invoice
with the Substituted By field referencing the CFDI Origin
invoice.](../../../_images/mx-01-invoice-cancellation.png)

##### 02 - invoices sent with errors without a relation

This cancellation reason has to be used when an invoice was sent with an error
in any field, and does not need to be replaced by another one.

For this case, navigate to Accounting ‣ Customers ‣ Invoices, and select the
old invoice. From here, the only requirement is to click the **Request EDI
Cancellation** button, and then click the **Process Now** button.

Because the field **Substituted By** does not appear when using this
cancellation reason, the SAT should automatically detect that the cancellation
reason is 02.

##### Payment cancellations

It is also possible to cancel _Payment Complements_. For this, go to the
payment, via Accounting ‣ Customers ‣ Payments, and select **Request EDI
Cancellation**. As with invoices, a blue button will appear. Click **Process
now** , and the document will be sent to the SAT. After a few seconds, you can
click **Retry** to confirm the current SAT status.

Finally, the payment status is moved to **Cancelled**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>0

#### Invoicing special use cases

##### CFDI to public

If the customer you are selling goods or services to does not require an
invoice, a _CFDI to Public_ has to be created.

If you use the **Customer** name `PUBLICO EN GENERAL`, an error will be
triggered. This is a main change in the CFDI 4.0 that requires invoices with
that specific name to need additional fields, which Konvergo ERP does not currently
support. So, for a _CFDI to Public_ to be created, you need to add any name to
your customer that is **not** `PUBLICO EN GENERAL`. (For example: `CLIENTE
FINAL`).

In addition to this, it is required that the **ZIP** code of your company is
added, the generic RFC is set as `XAXX010101000`, and the **Fiscal Regime** of
your customer must be set as: `Sin obligaciones fiscales`.

![CFDI to Public Customer field configuration.](../../../_images/mx-cfdi-to-
public.png)

##### Multicurrency

The main currency in Mexico is MXN. While this is mandatory for all Mexican
companies, it is possible to send and receive invoices (and payments) in
different currencies. To enable the use of
[multicurrency](../accounting/get_started/multi_currency), navigate to
the Accounting ‣ Settings ‣ Currencies, and set **Mexican Bank** as the
**Service** in the **Automatic Currency Rates** section. Then, set the
**Interval** field to the frequency you wish to update the exchange rates.

This way, the XML file of the document will have the correct exchange rate,
and the total amount, in both the foreign currency and in MXN.

It is highly recommended to use [a bank account for each
currency](../accounting/bank/foreign_currency).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>1 ![Multi-currency configuration in the Accounting
settings.](../../../_images/mx-multicurrency-1.png)

##### Down payments

There can be cases where you receive a payment in advance from a customer that
needs to be applied to an invoice later. In order to do this in Konvergo ERP, it is
required to properly link invoices to each other with the **CFDI Origin**
field. To do so, it is necessary to have the [Sales](../../sales) app
installed.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>2

First, navigate to the Sales app to create a product `Anticipo` and configure
it. The **Product Type** must be **Service** , and use the **UNSPSC Category**
must be: `84111506 Servicios de facturación`.

Then, go to Sales ‣ Settings ‣ Invoicing ‣ Down Payments, and add the
_Anticipo_ product as the default.

Create a sales order with the total amount, and create a down payment (either
using a percentage or fixed amount). Then, sign the document, and **Register
the Payment**.

When the time comes for the customer to get the final invoice, create it again
from the same sales order. In the **Create Invoices** wizard, select **Regular
Invoice** , and uncheck **Deduct down payments**.

Then, copy the **Fiscal Folio** from the first invoice, and paste it into the
**CDFI Origin** of the second invoice, adding the prefix `07|` before the
value. Then, sign the document.

After this, create a credit note for the first invoice. Copy the **Fiscal
Folio** from the second invoice, and paste it in the **CFDI Origin** of the
credit note, adding the prefix `07|`. Then, sign the document.

With this, all electronic documents are linked to each other. The final step
is to fully pay the new invoice. At the bottom of the new invoice, you can
find the credit note in the **Outstanding credits** \- add it as payment.
Finally, register the remaining amount with the **Register Payment** wizard.

### External trade

The external trade is a complement to a regular invoice that adds certain
values in both the XML and PDF, to invoices with a foreign customer according
to [SAT
regulations](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/complemento_comercio_exterior.htm),
such as:

  * The specific address of the receiver and the sender

  * The addition of a **Tariff Fraction** that identifies the type of product

  * The correct **Incoterm** (International Commercial Terms), among others (_certificate of origin_ and _special units of measure_).

This allows the correct identification of exporters and importers, in addition
to expanding the description of the merchandise sold.

Since January 1, 2018, external trade is a requirement for taxpayers, who
carry export operations of type A1. While the current CFDI is 4.0, the
external trade is currently on version 1.1

In order to use this feature, the modules **l10n_mx_edi_extended** and
**l10n_mx_edi_extended_40** have to be installed.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>3

#### Configuration

##### Contacts

To configure your company contact for external trade, navigate to Accounting ‣
Customers ‣ Customers, and select your **Company**. While the CFDI 4.0
requirements ask you to add a valid **ZIP** code in your contact, the external
trade complement adds the requirement that your **City** and the **State**
must also be valid. All three fields must coincide with the [Official SAT
Catalog](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/catalogos_emision_cfdi_complemento_ce.htm),
or you will receive an error.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>4

The fields **Locality** and **Colony Code** are optional and can be added in
the company directly in Settings ‣ General Settings ‣ Companies. These two
fields have to coincide with the data in the SAT.

![Optional external trade company fields.](../../../_images/mx-external-trade-
rescompany.png)

To configure the contact data for a foreign receiving client, navigate to
Accounting ‣ Customers ‣ Customers, and select the foreign client’s contact.
The contact must have the following fields completed to avoid errors:

  1. The entire company **Address** , including a valid **ZIP** code and the foreign **Country**.

  2. The format of the foreign **VAT** (tax identification number, for example: Colombia `123456789-1`)

  3. In the **MX EDI** tab, you need to address if the customer receives goods for a period of time temporarily (**Temporary**) or permanently (**Definitive**).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>5 ![Required external trade customer
fields.](../../../_images/mx-external-trade-customer-contact.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>6

##### Products

All products involved with external trade have four fields that are required,
two of them exclusive to external trade.

  1. The **Internal Reference** of the product is in the **General Information** tab.

  2. The **Weight** of the product must be more than `0`.

  3. The [correct](https://www.ventanillaunica.gob.mx/vucem/Clasificador) **Tariff Fraction** of the product in the **Accounting** tab.

  4. The **UMT Aduana** corresponds to the **Tariff Fraction**.

![Required external trade product fields.](../../../_images/mx-external-trade-
product.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>7

#### Invoicing flow

Before creating an invoice, it is important to take into account that external
trade invoices require to convert the amounts of your product into USD.
Therefore, [multicurrency](../accounting/get_started/multi_currency)
**must** be enabled and _USD_ **must** be activated in the **Currencies**
section. The correct **Service** to run is **Mexican Bank**.

Then, with the correct exchange rate set up in Accounting ‣ Settings ‣
Currency, the only fields left are **Incoterm** and the optional **Certificate
Source** in the **Other Info** tab.

![External trade Other Info tab of a product.](../../../_images/mx-external-
trade-other-info.png)

Finally, sign the invoice with the same process as a regular invoice, and
click the **Process Now** button.

### Delivery guide

A [Carta Porte](https://www.sat.gob.mx/consultas/68823/complemento-carta-
porte-) is a bill of lading: a document that states the type, quantity, and
destination of goods being carried.

On December 1st, 2021, version 2.0 of this CFDI was implemented for all
transportation providers, intermediaries, and owners of goods. Konvergo ERP is able to
generate a document type “T” (Traslado), which, unlike other documents, is
created in a delivery order instead of an invoice or payment.

Konvergo ERP can create XML and PDF files with (or without) ground transport, and can
process materials that are treated as _Dangerous Hazards_.

In order to use this feature, the modules **l10n_mx_edi_extended** ,
**l10n_mx_edi_extended_40** , **l10n_mx_edi_stock** and
**l10n_mx_edi_stock_40** have to be installed.

In addition to this, it is necessary to have the
[Inventory](../../inventory_and_mrp/inventory) and
[Sales](../../sales/sales) apps installed, as well.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>8

#### Configuration

Konvergo ERP manages two different types of CFDI:

  * **No Federal Highways** : Is used when the _Distance to Destination_ is [less than 30 KM](http://omawww.sat.gob.mx/cartaporte/Paginas/documentos/PreguntasFrecuentes_Autotransporte.pdf).

  * **Federal Transport** : Is used when the _Distance to Destination_ exceeds 30 KM.

Other than the standard requirements of regular invoicing (The RFC of the
customer, the UNSPSC code, etc.), if you are using _No Federal Highways_ , no
external configuration is needed.

For _Federal Transport_ , several configurations have to be added to contacts,
vehicle setups, and products. Those configurations are added to the XML and
PDF files.

##### Contacts and vehicles

Like the external trade feature, the **Address** in both the company and the
final customer must be complete. The **ZIP** code, **City** , and **State**
must coincide with the `Official SAT Catalog for Carta Porte <sat-catalog_>_`.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>From a legal point of view, a Mexican company <b>must</b> use the local currency (MXN). Therefore,
Konvergo ERP does not provide features to manage an alternative configuration. If you want to manage
another currency, let MXN be the default currency and use a <a href="../../sales/sales/products_prices/prices/pricing">pricelist</a>, instead.</p>
</div>9 ![Delivery guide contact
configuration.](../../../_images/mx-delivery-guide-contacts.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>0

Another addition to this feature is the **Vehicle Setups** menu found in
Inventory ‣ Settings ‣ Mexico. This menu lets you add all the information
related to the vehicle used for the delivery order.

All fields are mandatory to create a correct delivery guide.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>1

In the **Intermediaries** section, you must add the operator of the vehicle.
The only mandatory fields for this contact are the **VAT** and **Operator
Licence**.

![Delivery guide vehicle configuration.](../../../_images/mx-delivery-guide-
vehicle.png)

##### Products

Similar to regular invoicing, all products must have a **UNSPSC category**. In
addition to this, there are two extra configurations for products involved in
delivery guides:

  * The **Product Type** must be set as **Storable Product** for stock movements to be created.

  * In the **Inventory** tab, the field **Weight** should have more than `0`.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>2 ![Delivery guide product
configuration.](../../../_images/mx-delivery-guide-products.png)

#### Sales and inventory flow

To create a delivery guide, first, you need to create and confirm a sales
order from Sales ‣ Sales Order. This generates a **Delivery** smart button.
Click it, and **Validate** the transfer.

After the status is set to **Done** , you can edit the transfer, and select
the **Transport Type** (either **No Federal Highways** or **Federal
Transport**).

If your delivery guide has the type **No Federal Highways** , you can save the
transfer, and then click **Generate Delivery Guide**. The resulting XML can be
found in the chatter.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>3

If your delivery guide has the type, **Federal Transport** , the tab **MX
EDI** appears. There, enter a value in **Distance to Destination (KM)** bigger
than `0`, and select the **Vehicle Setup** used for this delivery.

![Delivery guide MX EDI tab configuration.](../../../_images/mx-delivery-
guide-federal-transport.png)

##### Dangerous hazards

Certain values in the **UNSPSC Category** are considered in the [official SAT
catalog](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/complemento_carta_porte.htm)
as _dangerous hazards_. These categories need additional considerations when
creating a delivery guide with **Federal Transport**.

First, select your product from Inventory ‣ Products ‣ Products. Then, in the
**Accounting** tab, the fields **Hazardous Material Designation Code (MX)**
and **Hazardous Packaging (MX)** must be filled with the correct code from the
SAT catalog.

![Delivery guide hazardous material product required
fields.](../../../_images/mx-delivery-guide-hazards-designation.png)

In Inventory ‣ Settings ‣ Mexico ‣ Vehicle Setup, the data from the
**Environment Insurer** and **Environment Insurance Policy** has to be filed,
as well. After this, continue with the regular process to create a delivery
guide.

![Delivery Guide environment insurer required fields.](../../../_images/mx-
delivery-guide-hazards-environment.png)

### Customs numbers

A _customs declaration_ (Pedimento Aduanero) is a fiscal document that
certifies that all contributions to the fiscal entity (the SAT) has been paid
for, including the import/export of goods.

According to the [Annex
20](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm) of CFDI
4.0, in documents where the invoiced goods come from a first-hand import
operation, the field, **Customs Number** , needs to be added to all lines of
products involved with the operation.

To do so, the module **l10n_mx_edi_landing** must be installed, in addition to
the [Inventory](../../inventory_and_mrp/inventory),
[Purchase](../../inventory_and_mrp/purchase) and
[Sales](../../sales/sales) apps.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>4

#### Configuration

In order to track the correct customs number for a specific invoice, Konvergo ERP uses
[landed
costs](../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs).
Go to Inventory ‣ Configuration ‣ Settings ‣ Valuation. Make sure that
**Landed Costs** is activated.

Begin by creating a _service_ -type product called, `Pedimento`. In the
**Purchase** tab, activate **Is a Landed Cost** , and select a **Default Split
Method**.

Then, configure the _storable products_ that hold the customs numbers. To do
so, create the storable products, and make sure the **Product Category** has
the following configuration.

  * **Costing Method** : Either **FIFO** or **AVCO**

  * **Inventory Valuation** : **Automated**

  * **Stock Valuation Account** : **115.01.01 Inventario**

  * **Stock Journal** : **Inventory Valuation**

  * **Stock Input Account** : **115.05.01 Mercancías en tránsito**

  * **Stock Output Account** : **115.05.01 Mercancías en tránsito**

![Storable products general configuration.](../../../_images/mx-landing-
configuration.png) ![Storable product category
configuration.](../../../_images/mx-landing-configuration-category.png)

#### Purchase and sales flow

After you configure your product, follow the standard [purchase
flow](../../inventory_and_mrp/purchase).

Create a purchase order from Purchase ‣ Orders ‣ Purchase Order. Then, confirm
the order to display a **Receipt** smart button. Click on the **Receipt**
smart button to **Validate** the receipt.

Go to Inventory ‣ Operations ‣ Landed Costs, and create a new record. Add the
transfer that you just created, and both: the product `Pedimento` and
**Customs number**.

Optionally, you can add a cost amount. After this, validate the landed cost.
Once **Posted** , all products related to that receipt have the customs number
assigned.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>5 ![Customs number on a landed costs Inventory
record.](../../../_images/mx-landing-inventory.png)

Now, create a sales order, and confirm it. This should trigger a **Delivery**
smart button. Validate it.

Finally, create an invoice from the sales order, and confirm it. The invoice
line related to your product has a customs number in it. This number should
match the customs number added in the _Landed Costs_ record you created
earlier.

![Customs number on confirmed sales order product.](../../../_images/mx-
landing-invoice.png)

### Electronic accounting

For Mexico, [Electronic
Accounting](https://www.sat.gob.mx/aplicacion/42150/envia-tu-contabilidad-
electronica) refers to the obligation to keep accounting records and entries
through electronic means, and to enter accounting information on a monthly
basis, through the SAT website.

It consists of three main XML files:

  1. The updated list of the chart of accounts that you are currently using.

  2. A monthly trial balance, plus a closing entry report, also known as: _Trial Balance Month 13_.

  3. Either optional, or for a compulsory audit, an export of the journal entries in your general ledger.

The resulting XML files follow the requirements of the [Anexo Técnico de
Contabilidad Electrónica
1.3](https://www.gob.mx/cms/uploads/attachment/file/151135/Anexo24_05012015.pdf).

In addition to this, you can generate the
[DIOT](https://www.sat.gob.mx/declaracion/74295/presenta-tu-declaracion-
informativa-de-operaciones-con-terceros-\(diot\)-): A report of vendor’s
journal entries that involve IVA taxes that can be exported in a `.txt` file.

In order to use these reports, the modules **l10n_mx_reports** ,
**l10n_mx_reports_closing** , **l10n_mx_xml_polizas** and
**l10n_mx_xml_polizas_edi** have to be installed, as well as the
[Accounting](../accounting/get_started).

You can find the _Chart of accounts_ , _Trial Balance Month 13_ , and _DIOT_
reports in Accounting ‣ Reporting ‣ Mexico.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>6

#### Chart of accounts

The [chart of accounts](../accounting/get_started/chart_of_accounts) in
México follows a specific pattern based on SAT’s’ [Código agrupador de
cuentas](http://omawww.sat.gob.mx/fichas_tematicas/buzon_tributario/Documents/codigo_agrupador.pdf).

You can create any account, as long as it respects SAT’s encoding group: the
pattern is `NNN.YY.ZZ` or `NNN.YY.ZZZ`.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>7

When a new account is created in Accounting ‣ Configuration ‣ Chart of
Accounts, with the SAT encoding group pattern, the correct grouping code
appears in **Tags** , and your account appears in the _COA_ report.

Once you create all your accounts, make sure the correct **Tags** are added.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>8

Once everything is set up, you can go to Accounting ‣ Reporting ‣ Mexico ‣
COA, and click the **SAT (XML)** button to generate an XML file containing all
of your accounts, which will be ready to upload to the SAT website.

#### Trial balance

The trial balance reports the initial balance, credit, and total balance of
your accounts, provided that you added their correct encoding group.

This report can be generated monthly, and a corresponding XML file is created,
if you go to Accounting ‣ Reporting ‣ Mexico ‣ Trial Balance, and click the
**SAT (XML)** button. Select the month you want to download beforehand.

![Trial balance report.](../../../_images/mx-reports-trial-balance.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you want to test the Mexican localization, the company can be configured with a real address
within Mexico (including all fields), and add <code>EKU9003173C9</code> as the <b>VAT</b> and <code>ESCUELA
KEMPER URGATE</code> as the <b>Company Name</b>. For the <b>Fiscal Regime</b>, use
<b>General de Ley Personas Morales</b>.</p>
</div>9

An additional report is the _Month 13_ : a closing balance sheet that shows
any adjustments or movements made in the accounting to close the year.

To generate this XML document, navigate to Accounting ‣ Accounting ‣
Miscellaneous ‣ Journal Entries, and create a new document. Here, add all
amounts to modify, and balance the debit and/or credit of each one.

After this is done, click **Mark as Closing Entry** , and the report found in
Accounting ‣ Reporting ‣ Mexico ‣ Trial Balance Month 13, contains the total
amount of the year, plus all the additions of the journal entry.

The XML file is generated by pressing the **SAT (XML)** button.

![Trial Balance Month 13 setup.](../../../_images/mx-reports-trial-
balance-13.png) ![Trial Balance Month 13 report.](../../../_images/mx-reports-
trial-balance-13-report.png)

#### General ledger

By law, all transactions in Mexico must be recorded digitally. Since Konvergo ERP
automatically creates all the underlying journal entries of your invoicing and
payments, you can export your journal entries to comply with SAT’s audits
and/or tax refunds.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>As with your own company, all of your contacts needs to have their correct business name
registered in the <abbr title="Servicio de Administración Tributaria">SAT</abbr>. This also applies to the <b>Fiscal Regime</b>, which needs to be
added in the <b>MX EDI</b> tab.</p>
</div>0

To create the XML, go to Accounting ‣ Reporting ‣ Audit Reports ‣ General
Ledger, and click **XML (Polizas)**. Here, you can select between four types
of **Export** types:

  * **Tax audit**

  * **Audit certification**

  * **Return of goods**

  * **Compensation**

For **Tax audit** , or **Audit certification** , you need to write the **Order
Number** provided by the SAT. For **Return of goods** , or **Compensation** ,
you need to write your **Process Number** , also provided by the SAT.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>As with your own company, all of your contacts needs to have their correct business name
registered in the <abbr title="Servicio de Administración Tributaria">SAT</abbr>. This also applies to the <b>Fiscal Regime</b>, which needs to be
added in the <b>MX EDI</b> tab.</p>
</div>1

#### DIOT report

The DIOT (Declaración Informativa de Operaciones con Terceros / _Informative
Declaration of Operations with Third Parties_) is an additional obligation
with the SAT, where the current status of creditable and non-creditable
payments, withholdings, and refunds of VAT from your vendor bills, are
provided to the SAT.

Unlike other reports, the DIOT is uploaded to a software provided by the SAT
that contains the A-29 form. In Konvergo ERP, you can download the records of your
transactions as a `.txt` file that can be uploaded to the form, avoiding
direct capture of this data.

The transactions file contains the total amount of your payments registered in
vendor bills, broken down into the corresponding types of IVA. The **VAT** and
**Country** is mandatory for all vendors.

To get the DIOT report, go to Accounting ‣ Reports ‣ Mexico ‣ Transactions
with third parties [DIOT]. Select the month that suits you, and click **DIOT
(TXT)** to download the `.txt` file.

![A Vendor Bill that is In Payment.](../../../_images/mx-reports-diot-
example.png) ![DIOT \(TXT\) download button.](../../../_images/mx-reports-
diot-example-download.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>As with your own company, all of your contacts needs to have their correct business name
registered in the <abbr title="Servicio de Administración Tributaria">SAT</abbr>. This also applies to the <b>Fiscal Regime</b>, which needs to be
added in the <b>MX EDI</b> tab.</p>
</div>2

  *[SAT]: Servicio de Administración Tributaria
  *[DIOT]: Declaración Informativa de Operaciones con Terceros
  *[RFC]: Registro Federal de Contribuyentes
  *[PAC]: Proveedor Autorizado de Certificación / Authorized Certification Provider
  *[PUE]: Pago en una Sola Exhibición/Payment in a Single Exhibition
  *[PPD]: Pago en Parcialidades o Diferido/Payment in Installements or Deferred

