# Electronic invoicing (EDI)

EDI, or electronic data interchange, is the inter-company communication of
business documents, such as purchase orders and invoices, in a standard
format. Sending documents according to an EDI standard ensures that the
machine receiving the message can interpret the information correctly. Various
EDI file formats exist and are available depending on your company’s country.

EDI feature enables automating the administration between companies and might
also be required by some governments for fiscal control or to facilitate the
administration.

Electronic invoicing of your documents such as customer invoices, credit notes
or vendor bills is one of the application of EDI.

Konvergo ERP supports, among others, the following formats.

Format Name | Applicability  
---|---  
Factur-X (PDF/A-3) | For French and German companies  
Peppol BIS Billing 3.0 (UBL) | For companies whose countries are part of the [EAS list](https://docs.peppol.eu/poacc/billing/3.0/codelist/eas/)  
E-FFF | For Belgian companies  
XRechnung (UBL) | For German companies  
Fattura PA (IT) | For Italian companies  
CFDI (4.0) | For Mexican companies  
Peru UBL 2.1 | For Peruvian companies  
SII IVA Llevanza de libros registro (ES) | For Spanish companies  
UBL 2.1 (Columbia) | For Colombian companies  
Egyptian Tax Authority | For Egyptian companies  
E-Invoice (IN) | For Indian companies  
NLCIUS (Netherlands) | For Dutch companies  
EHF 3.0 | For Norwegian companies  
SG BIS Billing 3.0 | For Singaporean companies  
A-NZ BIS Billing 3.0 | For Australian/New Zealand companies  
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Fiscal localization packages</span></a></p>
</div>

## Configuration

Go to Accounting ‣ Configuration ‣ Journals ‣ Customer Invoices ‣ Advanced
Settings ‣ Electronic Invoicing and enable the formats you need for this
journal.

![Select the EDI format you need](../../../../_images/formats.png)

Once an electronic invoicing format is enabled, XML documents are generated
when clicking on **Confirm** in documents such as invoices, credit notes, etc.
These documents are either visible in the attachment section, or embedded in
the PDF.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>For E-FFF, the xml file only appears after having generated the PDF (<b>Print</b> or
<b>Send &amp; Print</b> button), since the PDF needs to be embedded inside the xml.</p></li>
<li><p>Every PDF generated from Konvergo ERP contains a <b>Factur-X</b> XML file (for interoperability purpose).
For German and French companies, the option <b>Factur-X (PDF/A-3)</b> in addition enables
validation checks on the invoice and generates a PDF/A-3 compliant file, required by plaftorms like Chorus Pro.</p></li>
<li><p>The formats available depend on the country registered in your company’s <b>General
Information</b>.</p></li>
<li><p>Konvergo ERP supports the <b>Peppol BIS Billing 3.0</b> format that can be used via existing access
points.</p></li>
</ul>
</div>

  *[EDI]: electronic data interchange

