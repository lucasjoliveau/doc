# AvaTax use

AvaTax is a tax calculation software that can be integrated with Odoo in the
United States and Canada. Once the [integration setup](../avatax.html) is
complete, the calculated tax is simple and automatic.

## Calcul des taxes

Automatically calculate taxes on Odoo quotations and invoices with AvaTax by
confirming the documents during the sales flow. Alternatively, calculate the
taxes manually by clicking the Compute taxes using Avatax button while these
documents are in draft mode.

Astuce

Clicking the Compute taxes using Avatax button recalculates taxes if any
product lines are edited on the invoice.

![Sales quotation with the confirm and compute taxes using AvaTax buttons
highlighted.](../../../../../_images/calculate-avatax.png)

The tax calculation is triggered during the following automatic trigger and
manual trigger circumstances.

### Automatic triggers

  * When the sales rep sends the quote by email with Send by email button (pop-up).

  * When the customer views the online quote on the portal.

  * When a quote is confirmed and becomes a sales order.

  * When the customer views the invoice on the portal.

  * When a draft invoice is validated.

  * When the customer views the subscription in the portal.

  * When a subscription generates an invoice.

  * When the customer gets to the last screen of the eCommerce checkout.

### Manual triggers

  * Compute taxes using Avatax button at the bottom of the quote.

  * Compute taxes using Avatax button at the top of the invoice.

Astuce

Use the Avalara Partner Code field that is available on customer records,
quotations, and invoices to cross-reference data in Odoo and AvaTax. This
field is located under the Other info tab of the sales order or quotation in
the Sales section.

On the customer record, navigate to _Contacts app_ and select a contact. Then
open the Sales & Purchase tab and the Avalara Partner Code under the Sales
section.

Important

The Automatic Tax Mapping (AvaTax) fiscal position is also applied on those
Odoo documents, like subscriptions.

Pour plus d'infos

  * [Positions fiscales (correspondances de taxes et de comptes)](../fiscal_positions.html)

## AvaTax synchronization

Synchronization occurs with AvaTax, when the _invoice_ is created in Odoo.
This means the sales tax is recorded with Avalara (AvaTax software developer).

To do so, navigate to Sales app ‣ Orders ‣ Quotations. Select a quotation from
the list.

After confirming a quotation and validating the delivery, click Create
Invoice. Indicate whether it is a Regular invoice, Down payment (percentage),
or Down payment (fixed amount).

Then click Create and view invoice. The recorded taxes can be seen in the
Journal Items tab of the invoice. There will be different taxes depending on
the location of the Delivery Address.

![Journal items highlighted on a invoice in
Odoo.](../../../../../_images/journal-items.png)

Finally, press the Confirm button to complete the invoice and synchronize with
the AvaTax portal.

Avertissement

An invoice cannot be Reset to draft because this causes de-synchronization
with the AvaTax Portal. Instead, click Add credit note and state: `Sync with
AvaTax Portal`. See this documentation: [Avoirs et
remboursements](../../customer_invoices/credit_notes.html).

## Fixed price discounts

Add a fixed price discount to a valuable customer by click Add a line on the
customer’s invoice. Add the product discount and set the Price to either a
positive or negative value. To recalculate the taxes, click Compute taxes
using Avatax.

Astuce

Tax calculation can even be done on negative subtotals and credit notes.

## Journalisation

It is possible to log Avalara/_AvaTax_ actions in Odoo for further analysis,
or verification of functionality. Logging is accessible through the _AvaTax_
settings.

To start logging _AvaTax_ actions, first, navigate to the Accounting app ‣
Configuration ‣ Settings.

Then, in the Taxes section, under the AvaTax settings, click Start logging for
30 minutes.

Upon starting the log process, Odoo will log all Avalara/_AvaTax_ actions
performed in the database.

To view the logs, click on Show logs to the right of the Start logging for 30
minutes. This reveals a detailed list of Avalara/_AvaTax_ actions. This list
is sortable by the following columns:

  * Created on: timestamp of the _AvaTax_ calculation.

  * Created by: numeric value of the user in the database.

  * Database name: name of the database.

  * Type: two values can be chosen for this field, Server or Client.

  * Name: Avalara service name. In this case, it will be _AvaTax_.

  * Level: by default, this will be `INFO`.

  * Path: indicates the path taken to make the calculation.

  * Line: indicates the line the calculation is made on.

  * Function: indicates the calculation taken on the line.

![Avalara logging page with top row of list
highlighted.](../../../../../_images/logging.png)

Click into the log line to reveal another field, called Message.

This field populates a raw transcription of the transaction, which involves
the creation (or adjustment) of a sales invoice using the Avalara _AvaTax_
API.

The transaction includes details, such as addresses for shipping from and to,
line items describing the products or services, tax codes, tax amounts, and
other relevant information.

The Message contains the calculated taxes for different jurisdictions and
confirms the creation (or adjustment) of the transaction.

Astuce

Custom fields can be made using Odoo _Studio_. Click the __(ellipsis) menu to
the far-right of the header row. Then click __ Add custom field. This action
opens Odoo _Studio_.

Important

Odoo _Studio_ requires a _custom_ pricing plan. Consult the database’s
customer success manager for more information on switching plans. Or to see if
Odoo _Studio_ is included in the database’s current pricing plan. See this
documentation: [Studio](../../../../studio.html).

Pour plus d'infos

  * [AvaTax integration](../avatax.html)

  * [Avalara (Avatax) portal](avalara_portal.html)

  * [US Tax Compliance: Avatax elearning video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)

  * [Positions fiscales (correspondances de taxes et de comptes)](../fiscal_positions.html)

