# VAT numbers verification (VIES)

**VAT Information Exchange System** \- abbreviated **VIES** \- is a tool
provided by the European Commission that allows you to check the validity of
VAT numbers of companies registered in the European Union.

Konvergo ERP provides a feature to **Verify VAT Numbers** when you save a contact.
This helps you make sure that your contacts provided you with a valid VAT
number without leaving Konvergo ERP interface.

## Configuration

To enable this feature, go to Accounting ‣ Configuration ‣ Settings ‣ Taxes,
enable the **Verify VAT Numbers** feature, and click on _Save_.

![Enable "Verify VAT Numbers" in Konvergo ERP Accounting](../../../../_images/vat-
validation-configuration.png)

## VAT Number validation

Whenever you create or modify a contact, make sure to fill out the **Country**
and **VAT** fields.

![Fill out the contact form with the country and VAT number before clicking on
*Save*](../../../../_images/vat-validation-contact-form.png)

When you click on _Save_ , Konvergo ERP runs a VIES VAT number check, and displays an
error message if the VAT number is invalid.

![Konvergo ERP displays an error message instead of saving when the VAT number is
invalid](../../../../_images/vat-validation-error.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>This tool checks the VAT number’s validity but does not check the other fields’ validity.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://ec.europa.eu/taxation_customs/vies/vatRequest">European Commission: VIES search engine</a></p></li>
</ul>
</div>

