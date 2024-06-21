# Accounting and Invoicing

**Konvergo ERP Invoicing** is a standalone invoicing app to create invoices, send them
to your customers, and manage payments.

**Konvergo ERP Accounting** is a full featured accounting app. Accountant productivity
is at the core of its development with features such as AI-powered invoice
recognition, synchronization with your bank accounts, smart matching
suggestions, etc.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://www.odoo.com/slides/accounting-19">Konvergo ERP Tutorials: Accounting</a></p>
</div>

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting)

## Double-entry bookkeeping

Konvergo ERP automatically creates all the underlying journal entries for all
accounting transactions (e.g., customer invoices, vendor bills, point-of-sales
orders, expenses, inventory valuations, etc.).

Konvergo ERP uses the double-entry bookkeeping system, whereby every entry needs a
corresponding and opposite counterpart in a different account, with one
account debited and the other credited. It ensures that all transactions are
recorded accurately and consistently and that the accounts always balance.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="accounting/get_started/cheat_sheet">Accounting Cheat Sheet</a></p>
</div>

## Accrual and cash basis

Both accrual and cash basis accounting are supported in Konvergo ERP. This allows
reporting income and expense either when the transaction occurs (accrual
basis) or when the payment is made or received (cash basis).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="accounting/taxes/cash_basis">Cash basis</a></p>
</div>

## Multi-company

Several companies can be managed within the same database. Each company has
its [chart of accounts](accounting/get_started/chart_of_accounts), which
is also useful to generate consolidation reports. Users can access several
companies but can only work on a single company’s accounting at a time.

## Multi-currency environment

A [multi-currency](accounting/get_started/multi_currency) environment
with an automated exchange rate to ease international transactions is
available in Konvergo ERP. Every transaction is recorded in the company’s default
currency; for transactions occurring in another currency, Konvergo ERP stores both the
value in the company’s currency and the transactions’ currency value. Konvergo ERP
generates currency gains and losses after reconciling the journal items.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="accounting/bank/foreign_currency">Manage a bank in a foreign currency</a></p>
</div>

## International standards

Konvergo ERP Accounting supports more than 70 countries. It provides the central
standards and mechanisms common to all nations, and thanks to country-specific
modules, local requirements are fulfilled. Fiscal positions exist to address
regional specificities like the chart of accounts, taxes, or any other
requirements.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="fiscal_localizations">Fiscal localization packages</a></p>
</div>

## Accounts receivable and payable

By default, there is a single account for the account receivable entries and
one for the account payable entries. As transactions are linked to your
**contacts** , you can run a report per customer, vendor, or supplier.

The **Partner Ledger** report displays the balance of your customers and
suppliers. It is available by going to Accounting ‣ Reporting ‣ Partner
Ledger.

## Reporting

The following financial [reports](accounting/reporting) are available and
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
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><a href="accounting/reporting/customize">Create and customize reports</a> with Konvergo ERP’s report engine.</p>
</div>

### Tax report

Konvergo ERP computes all accounting transactions for the specific tax period and uses
these totals to calculate the tax obligation.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Once the tax report has been generated for a period, Konvergo ERP locks it and prevents the creation of
new journal entries involving VAT. Any correction to customer invoices or vendor bills has to
be recorded in the next period.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Depending on the country’s localization, an XML version of the tax report can be generated to be
uploaded to the VAT platform of the relevant taxation authority.</p>
</div>

## Bank synchronization

The bank synchronization system directly connects with your bank institution
to automatically import all transactions into your database. It gives an
overview of your cash flow without logging into an online banking system or
waiting for paper bank statements.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="accounting/bank/bank_synchronization">Bank synchronization</a></p>
</div>

## Inventory valuation

Both periodic (manual) and perpetual (automated) inventory valuations are
supported in Konvergo ERP. The available methods are standard price, average price,
LIFO and FIFO (First-In, First-Out).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config">Inventory valuation configuration</a></p>
</div>

## Retained earnings

Retained earnings are the portion of income retained by a business. Konvergo ERP
calculates current year earnings in real-time, so no year-end journal or
rollover is required. The profit and loss balance is automatically reported on
the balance sheet report.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="accounting/get_started/cheat_sheet">Accounting Cheat Sheet</a></p>
</div>0

## Fiduciaries

The **Accounting Firms** mode can be activated by going to Accounting ‣
Configuration ‣ Settings ‣ Accounting Firms mode. When enabled:

  * The document’s sequence becomes editable on all documents;

  * The **Total (tax incl.)** field appears to speed up and control the encoding by automating line creation with the right account and tax;

  * **Invoice Date** and **Bill Date** are pre-filled when encoding a transaction.

  * A **Quick encoding** option is available for customer invoices and vendor bills.

  * [Get started](accounting/get_started)
    * [Accounting cheat sheet](accounting/get_started/cheat_sheet)
    * [Chart of accounts](accounting/get_started/chart_of_accounts)
    * [Multi-currency system](accounting/get_started/multi_currency)
    * [Average price on returned goods](accounting/get_started/avg_price_valuation)
    * [VAT units](accounting/get_started/vat_units)
  * [Taxes](accounting/taxes)
    * [Cash basis taxes](accounting/taxes/cash_basis)
    * [Withholding taxes](accounting/taxes/retention)
    * [VAT numbers verification (VIES)](accounting/taxes/vat_verification)
    * [Fiscal positions (tax and account mapping)](accounting/taxes/fiscal_positions)
    * [AvaTax integration](accounting/taxes/avatax)
      * [AvaTax use](accounting/taxes/avatax/avatax_use)
      * [Avalara (Avatax) portal](accounting/taxes/avatax/avalara_portal)
    * [TaxCloud integration](accounting/taxes/taxcloud)
    * [EU intra-community distance selling](accounting/taxes/eu_distance_selling)
    * [B2B (tax excluded) and B2C (tax included) pricing](accounting/taxes/B2B_B2C)
  * [Customer invoices](accounting/customer_invoices)
    * [Invoicing processes](accounting/customer_invoices/overview)
    * [Delivery and invoice addresses](accounting/customer_invoices/customer_addresses)
    * [Payment terms and installment plans](accounting/customer_invoices/payment_terms)
    * [Default terms and conditions (T&C)](accounting/customer_invoices/terms_conditions)
    * [Cash discounts and tax reduction](accounting/customer_invoices/cash_discounts)
    * [Credit notes and refunds](accounting/customer_invoices/credit_notes)
    * [Cash rounding](accounting/customer_invoices/cash_rounding)
    * [Deferred revenues](accounting/customer_invoices/deferred_revenues)
    * [Electronic invoicing (EDI)](accounting/customer_invoices/electronic_invoicing)
    * [Snailmail](accounting/customer_invoices/snailmail)
    * [EPC QR codes](accounting/customer_invoices/epc_qr_code)
    * [Incoterms](accounting/customer_invoices/incoterms)
  * [Vendor bills](accounting/vendor_bills)
    * [AI-powered document digitization](accounting/vendor_bills/invoice_digitization)
    * [Non-current assets and fixed assets](accounting/vendor_bills/assets)
    * [Deferred expenses and prepayments](accounting/vendor_bills/deferred_expenses)
  * [Payments](accounting/payments)
    * [Online payments](accounting/payments/online)
      * [Install the patch to disable online invoice payment](accounting/payments/online/install_portal_patch)
    * [Checks](accounting/payments/checks)
    * [Batch payments by bank deposit](accounting/payments/batch)
    * [Batch payments: SEPA Direct Debit (SDD)](accounting/payments/batch_sdd)
    * [Follow-up on invoices](accounting/payments/follow_up)
    * [Internal transfers](accounting/payments/internal_transfers)
    * [Pay with SEPA](accounting/payments/pay_sepa)
    * [Pay by checks](accounting/payments/pay_checks)
    * [Forecast future bills to pay](accounting/payments/forecast)
  * [Bank and cash accounts](accounting/bank)
    * [Bank synchronization](accounting/bank/bank_synchronization)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge)
      * [Ponto](accounting/bank/bank_synchronization/ponto)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking)
    * [Transactions](accounting/bank/transactions)
    * [Bank reconciliation](accounting/bank/reconciliation)
    * [Reconciliation models](accounting/bank/reconciliation_models)
    * [Manage a bank account in a foreign currency](accounting/bank/foreign_currency)
    * [Cash register](accounting/bank/cash_register)
  * [Reporting](accounting/reporting)
    * [Tax return (VAT declaration)](accounting/reporting/tax_returns)
    * [Tax carryover](accounting/reporting/tax_carryover)
    * [Analytic accounting](accounting/reporting/analytic_accounting)
    * [Financial budget](accounting/reporting/budget)
    * [Intrastat](accounting/reporting/intrastat)
    * [Data inalterability check report](accounting/reporting/data_inalterability)
    * [Silverfin integration](accounting/reporting/silverfin)
    * [Custom reports](accounting/reporting/customize)
    * [Year-end closing](accounting/reporting/year_end)

  *[LIFO]: Last-In, First-Out
  *[EDI]: electronic data interchange

