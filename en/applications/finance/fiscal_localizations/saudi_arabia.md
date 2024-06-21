# Saudi Arabia

## Configuration

[Install](../../general/apps_modules#general-install) the following
modules to get all the features of the Saudi Arabian localization:

Name | Technical name | Description  
---|---|---  
Saudi Arabia - Accounting | `l10n_sa` | Default [fiscal localization package](../fiscal_localizations#fiscal-localizations-packages)  
Saudi Arabia - E-invoicing | `l10n_sa_edi` | ZATCA e-invoices implementation  
Saudi Arabia - E-invoicing (Simplified) | `l10n_sa_edi_simplified` | ZATCA simplified e-invoices implementation (Point of Sale)  
Saudi Arabia - Point of Sale | `l10n_sa_pos` | Point of Sale compliance  
  
## ZATCA e-invoices

The ZATCA e-invoicing system is designed to streamline and digitize the
invoicing process for businesses operating in Saudi Arabia.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx">ZATCA e-invoicing page</a></p>
</div>

### Company information

Go to Settings ‣ General Settings ‣ Companies, click **Update info** , and
ensure the following company information is complete and up-to-date.

  * The full **Company Name**.

  * All relevant **Address** fields, including the **Building Number** and **Plot Identification** (four digits each).

  * Select an enterprise **Identification Scheme**. It is recommended to use the **Commercial Registration Number**.

  * Enter the **Identification Number** for the selected **Identification Scheme**.

  * The **VAT** number.

  * Ensure the **Currency** is set to **SAR**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is also necessary to fill out similar information for partner companies.</p>
</div>

### Simulation mode

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>It is strongly recommended to thoroughly test all invoicing workflows using the Fatoora
<b>simulation</b> portal first, as <b>any</b> invoice submitted to the regular Fatoora portal will be
accounted for, which could lead to fines and penalties.</p>
</div>

#### Fatoora simulation portal

Log in on the [Fatoora portal](https://fatoora.zatca.gov.sa/) using the
company’s ZATCA credentials. Then, click the **Fatoora Simulation Portal**
button to switch to the simulation portal.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf">ZACTA Fatoora portal user manual version 3 (May 2023)</a></p>
</div>

#### ZATCA API integration

On Konvergo ERP, go to Accounting ‣ Configuration ‣ Settings. Under **ZATCA API
Integration** , select the **Simulation (Pre-Production)** **API mode** and
click **Save**.

#### Sales journals

Each sales journal on Konvergo ERP needs to be configured. To do so, go to Accounting
‣ Configuration ‣ Journals, open any sales journal (e.g., Customer Invoices),
and go to the **ZATCA** tab. Once there, enter any **Serial Number** to
identify the journal.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The same serial number can be used for all of the company’s sales journals.</p>
</div>

Next, click **Onboard Journal**. In the dialog box, providing an OTP code is
required. To retrieve it, open the [Fatoora simulation
portal](https://fatoora.zatca.gov.sa/), click **Onboard New Solution
Unit/Device** , choose the number of OTP codes to generate (one per journal to
configure), and click **Generate OTP Code**. Copy an OTP code, it into the
dialog box on Konvergo ERP, and click **Request**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>OTP codes expire after one hour.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If any issue occurs during onboarding, click <b>Regenerate CSR</b> to start again.</p>
</div>

#### Testing

When confirming an invoice, there is now an option to process the invoice,
sending it directly the Fatoora simulation portal. Konvergo ERP displays the portal’s
response after each submission. Only rejected invoices can be reset to draft
and edited on Konvergo ERP. Furthermore, at the end of each day, Konvergo ERP sends all
unprocessed invoices to the portal.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>Testing all invoicing workflows, preferably with real invoices and for a reasonable amount of
time, is recommended.</p></li>
<li><p>Compare the invoices received statistics page on the Fatoora simulation portal with the list of
invoices on Konvergo ERP to ensure both align.</p></li>
</ul>
</div>

#### Taxes

When using a **0% tax** in a customer invoice, it is necessary to specify the
reason behind such a rate. To configure taxes, go to Accounting ‣
Configuration ‣ Settings ‣ Taxes, and open the tax to edit. Under the
**Advanced Options** , select an **Exemption Reason Code** and click **Save**.

When using **retention** or **withholding an amount** in a customer invoice,
the tax used to retain the amount needs to be specified.

### Production mode

When ready for production, change the API mode to **Production** and click
**Save**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Setting the <b>API mode</b> to <b>Production</b> is <b>irreversible</b>.</p>
</div>

The sales journals initially linked to the simulation portal now needs to be
linked to the regular portal. To do so, onboard the journals again, ensuring
to use the regular [Fatoora portal](https://fatoora.zatca.gov.sa/) this time.

  *[OTP]: one-time password

