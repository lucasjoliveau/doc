# Accounting and Invoicing

**Odoo Invoicing** is a standalone invoicing app to create invoices, send them
to your customers, and manage payments.

**Odoo Accounting** is a full featured accounting app. Accountant productivity
is at the core of its development with features such as AI-powered invoice
recognition, synchronization with your bank accounts, smart matching
suggestions, etc.

See also

[Odoo Tutorials: Accounting](https://www.odoo.com/slides/accounting-19)

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started.html)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes.html)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices.html)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills.html)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments.html)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank.html)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting.html)

## Double-entry bookkeeping

Odoo automatically creates all the underlying journal entries for all
accounting transactions (e.g., customer invoices, vendor bills, point-of-sales
orders, expenses, inventory valuations, etc.).

Odoo uses the double-entry bookkeeping system, whereby every entry needs a
corresponding and opposite counterpart in a different account, with one
account debited and the other credited. It ensures that all transactions are
recorded accurately and consistently and that the accounts always balance.

See also

[Accounting Cheat Sheet](accounting/get_started/cheat_sheet.html)

## Accrual and cash basis

Both accrual and cash basis accounting are supported in Odoo. This allows
reporting income and expense either when the transaction occurs (accrual
basis) or when the payment is made or received (cash basis).

See also

[Cash basis](accounting/taxes/cash_basis.html)

## Multi-company

Several companies can be managed within the same database. Each company has
its [chart of accounts](accounting/get_started/chart_of_accounts.html), which
is also useful to generate consolidation reports. Users can access several
companies but can only work on a single company’s accounting at a time.

## Multi-currency environment

A [multi-currency](accounting/get_started/multi_currency.html) environment
with an automated exchange rate to ease international transactions is
available in Odoo. Every transaction is recorded in the company’s default
currency; for transactions occurring in another currency, Odoo stores both the
value in the company’s currency and the transactions’ currency value. Odoo
generates currency gains and losses after reconciling the journal items.

See also

[Manage a bank in a foreign currency](accounting/bank/foreign_currency.html)

## International standards

Odoo Accounting supports more than 70 countries. It provides the central
standards and mechanisms common to all nations, and thanks to country-specific
modules, local requirements are fulfilled. Fiscal positions exist to address
regional specificities like the chart of accounts, taxes, or any other
requirements.

See also

[Fiscal localization packages](fiscal_localizations.html)

## Accounts receivable and payable

By default, there is a single account for the account receivable entries and
one for the account payable entries. As transactions are linked to your
**contacts** , you can run a report per customer, vendor, or supplier.

The **Partner Ledger** report displays the balance of your customers and
suppliers. It is available by going to Accounting ‣ Reporting ‣ Partner
Ledger.

## Reporting

The following financial [reports](accounting/reporting.html) are available and
updated in real-time:

Financial reports  
---  
Statement | Balance sheet  
Profit and loss  
Cash flow statement  
Tax report  
ES sales list  
Audit | General ledger  
Trial balance  
Journal report  
Intrastat report  
Check register  
Partner | Partner ledger  
Aged receivable  
Aged payable  
Management | Invoice analysis  
Unrealized currency gains/losses  
Depreciation schedule  
Disallowed expenses  
Budget analysis  
Product margins  
1099 report  
  
Tip

[Create and customize reports](accounting/reporting/customize.html) with
Odoo’s report engine.

### Tax report

Odoo computes all accounting transactions for the specific tax period and uses
these totals to calculate the tax obligation.

Important

Once the tax report has been generated for a period, Odoo locks it and
prevents the creation of new journal entries involving VAT. Any correction to
customer invoices or vendor bills has to be recorded in the next period.

Note

Depending on the country’s localization, an XML version of the tax report can
be generated to be uploaded to the VAT platform of the relevant taxation
authority.

## Bank synchronization

The bank synchronization system directly connects with your bank institution
to automatically import all transactions into your database. It gives an
overview of your cash flow without logging into an online banking system or
waiting for paper bank statements.

See also

[Bank synchronization](accounting/bank/bank_synchronization.html)

## Inventory valuation

Both periodic (manual) and perpetual (automated) inventory valuations are
supported in Odoo. The available methods are standard price, average price,
LIFO and FIFO (First-In, First-Out).

See also

[Inventory valuation
configuration](../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config.html)

## Retained earnings

Retained earnings are the portion of income retained by a business. Odoo
calculates current year earnings in real-time, so no year-end journal or
rollover is required. The profit and loss balance is automatically reported on
the balance sheet report.

See also

[Accounting Cheat Sheet](accounting/get_started/cheat_sheet.html)

## Fiduciaries

The Accounting Firms mode can be activated by going to Accounting ‣
Configuration ‣ Settings ‣ Accounting Firms mode. When enabled:

  * The document’s sequence becomes editable on all documents;

  * The Total (tax incl.) field appears to speed up and control the encoding by automating line creation with the right account and tax;

  * Invoice Date and Bill Date are pre-filled when encoding a transaction.

  * A Quick encoding option is available for customer invoices and vendor bills.

  * [Get started](accounting/get_started.html)
    * [Accounting cheat sheet](accounting/get_started/cheat_sheet.html)
    * [Chart of accounts](accounting/get_started/chart_of_accounts.html)
    * [Multi-currency system](accounting/get_started/multi_currency.html)
    * [Average price on returned goods](accounting/get_started/avg_price_valuation.html)
    * [VAT units](accounting/get_started/vat_units.html)
  * [Taxes](accounting/taxes.html)
    * [Cash basis taxes](accounting/taxes/cash_basis.html)
    * [Withholding taxes](accounting/taxes/retention.html)
    * [VAT numbers verification (VIES)](accounting/taxes/vat_verification.html)
    * [Fiscal positions (tax and account mapping)](accounting/taxes/fiscal_positions.html)
    * [AvaTax integration](accounting/taxes/avatax.html)
      * [AvaTax use](accounting/taxes/avatax/avatax_use.html)
      * [Avalara (Avatax) portal](accounting/taxes/avatax/avalara_portal.html)
    * [TaxCloud integration](accounting/taxes/taxcloud.html)
    * [EU intra-community distance selling](accounting/taxes/eu_distance_selling.html)
    * [B2B (tax excluded) and B2C (tax included) pricing](accounting/taxes/B2B_B2C.html)
  * [Customer invoices](accounting/customer_invoices.html)
    * [Invoicing processes](accounting/customer_invoices/overview.html)
    * [Delivery and invoice addresses](accounting/customer_invoices/customer_addresses.html)
    * [Payment terms and installment plans](accounting/customer_invoices/payment_terms.html)
    * [Default terms and conditions (T&C)](accounting/customer_invoices/terms_conditions.html)
    * [Cash discounts and tax reduction](accounting/customer_invoices/cash_discounts.html)
    * [Credit notes and refunds](accounting/customer_invoices/credit_notes.html)
    * [Cash rounding](accounting/customer_invoices/cash_rounding.html)
    * [Deferred revenues](accounting/customer_invoices/deferred_revenues.html)
    * [Electronic invoicing (EDI)](accounting/customer_invoices/electronic_invoicing.html)
    * [Snailmail](accounting/customer_invoices/snailmail.html)
    * [EPC QR codes](accounting/customer_invoices/epc_qr_code.html)
    * [Incoterms](accounting/customer_invoices/incoterms.html)
  * [Vendor bills](accounting/vendor_bills.html)
    * [AI-powered document digitization](accounting/vendor_bills/invoice_digitization.html)
    * [Non-current assets and fixed assets](accounting/vendor_bills/assets.html)
    * [Deferred expenses and prepayments](accounting/vendor_bills/deferred_expenses.html)
  * [Payments](accounting/payments.html)
    * [Online payments](accounting/payments/online.html)
      * [Install the patch to disable online invoice payment](accounting/payments/online/install_portal_patch.html)
    * [Checks](accounting/payments/checks.html)
    * [Batch payments by bank deposit](accounting/payments/batch.html)
    * [Batch payments: SEPA Direct Debit (SDD)](accounting/payments/batch_sdd.html)
    * [Follow-up on invoices](accounting/payments/follow_up.html)
    * [Internal transfers](accounting/payments/internal_transfers.html)
    * [Pay with SEPA](accounting/payments/pay_sepa.html)
    * [Pay by checks](accounting/payments/pay_checks.html)
    * [Forecast future bills to pay](accounting/payments/forecast.html)
  * [Bank and cash accounts](accounting/bank.html)
    * [Bank synchronization](accounting/bank/bank_synchronization.html)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge.html)
      * [Ponto](accounting/bank/bank_synchronization/ponto.html)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking.html)
    * [Transactions](accounting/bank/transactions.html)
    * [Bank reconciliation](accounting/bank/reconciliation.html)
    * [Reconciliation models](accounting/bank/reconciliation_models.html)
    * [Manage a bank account in a foreign currency](accounting/bank/foreign_currency.html)
    * [Cash register](accounting/bank/cash_register.html)
  * [Reporting](accounting/reporting.html)
    * [Tax return (VAT declaration)](accounting/reporting/tax_returns.html)
    * [Tax carryover](accounting/reporting/tax_carryover.html)
    * [Analytic accounting](accounting/reporting/analytic_accounting.html)
    * [Financial budget](accounting/reporting/budget.html)
    * [Intrastat](accounting/reporting/intrastat.html)
    * [Data inalterability check report](accounting/reporting/data_inalterability.html)
    * [Silverfin integration](accounting/reporting/silverfin.html)
    * [Custom reports](accounting/reporting/customize.html)
    * [Year-end closing](accounting/reporting/year_end.html)

  *[LIFO]: Last-In, First-Out
  *[EDI]: electronic data interchange

