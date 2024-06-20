# Accounting localization

Warning

This tutorial requires knowledge about how to build a module in Odoo (see
[Getting started](../tutorials/getting_started.html)).

## Installation procedure

On installing the
[account](https://github.com/odoo/odoo/blob/16.0/addons/account) module, the
localization module corresponding to the country code of the company is
installed automatically. In case of no country code set or no localization
module found, the
[l10n_generic_coa](https://github.com/odoo/odoo/blob/16.0/addons/l10n_generic_coa)
(US) localization module is installed by default. Check [post init
hook](https://github.com/odoo/odoo/blob/16.0/addons/account/__init__.py) for
details.

For example, [l10n_ch](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch)
will be installed if the company has `Switzerland` as country.

## Building a localization module

The structure of a basic `l10n_XX` module may be described with the following
`__manifest__.py` file:

    
    
    {
        "name": "COUNTRY - Accounting",
        "version": "1.0.0",
        "category": "Accounting/Localizations/Account Charts",
        "license": "LGPL-3",
        "depends": [
            "account",
            # "l10n_multilang",
        ],
        "data": [
            # Chart of Accounts
            "data/account_chart_template_data.xml",
            "data/account_account_tag_data.xml",
            "data/account.account.template.csv",
            "data/account.group.template.csv",
    
            # Taxes
            "data/account_tax_group_data.xml",
            "data/account_tax_report_data.xml",
            "data/account_tax_template_data.xml",
            "data/account_fiscal_position_template_data.xml",
            "data/account_account_template_post_data.xml",
    
            "data/account_chart_post_data.xml",
            "data/account_chart_template_try_loading.xml",
    
            # Views and others
            "views/xxxmodel_views.xml"
        ],
        "demo": [
            "demo/demo_company.xml",
        ]
    }
    

In the first file `data/account_chart_template_data.xml`, we set the name for
the chart of accounts along with some basic fields.

See also

[Chart Template
References](../reference/standard_modules/account/account_chart_template.html#reference-
account-chart-template)

Example

[addons/l10n_ch/data/l10n_ch_chart_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/data/l10n_ch_chart_data.xml)

Note

Recommended **xmlid** for the record is `chart_template`. If you need many
chart of accounts, you can add some suffixes, i.e. `chart_template_XXX`.

## Chart of Accounts

### Account tags

See also

[Account Tag
References](../reference/standard_modules/account/account_account_tag.html#reference-
account-account-tag)

Tags are a way to sort accounts. For example, imagine you want to create a
financial report having multiple lines but you have no way to find a rule to
dispatch the accounts according to their `code`. The solution is the usage of
tags, one for each report line, to filter accounts like you want.

Put the tags in the `data/account_account_tag_data.xml` file.

Example

[addons/l10n_lt/data/account.account.template.csv](https://github.com/odoo/odoo/blob/16.0/addons/l10n_lt/data/account.account.template.csv)

Example

[addons/l10n_at/data/account_account_template.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_at/data/account_account_template.xml)

### Accounts

See also

  * [Account References](../reference/standard_modules/account/account_account.html#reference-account-account)

  * [Chart of accounts](../../applications/finance/accounting/get_started/chart_of_accounts.html)

Obviously, Chart of Accounts cannot exist without Accounts. You need to
specify them in `data/account.account.template.csv`.

Example

[addons/l10n_ch/data/account.account.template.csv](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/data/account.account.template.csv)

CSV is prefered but you may use XML format instead.

Example

[addons/l10n_at/data/account_account_template.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_at/data/account_account_template.xml)

Warning

  * Avoid the usage of liquidity `account.account.type`! Indeed, the bank & cash accounts are created directly at the installation of the localization module and then, are linked to an `account.journal`.

  * Only one account of type payable/receivable is enough for the generic case. We need to define a PoS receivable account as well however. (linked in the CoA)

  * Don’t create too many accounts: 200-300 is enough. But mostly, we try to find a good balance where the CoA needs minimal adapting for most companies afterwards.

Next settings for the chart of accounts are set in a separate file, because we
need to provide a list of accounts first. In
`data/account_chart_post_data.xml`, we set some default accounts:

Example

[addons/l10n_ch/data/l10n_ch_chart_post_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/data/l10n_ch_chart_post_data.xml)

### Account groups

See also

[Account Group
References](../reference/standard_modules/account/account_group.html#reference-
account-group)

Account groups allow describing the hierarchical structure of the chart of
accounts. The filter needs to be activated in the report and then when you
decollapse into journal entries it will show the parents of the account.

It works with the prefix _start_ /_end_ , so every account where the code
starts with something between _start_ and _end_ will have this account.group
as the parent group. Furthermore, the account groups can have a parent account
group as well to form the hierarchy.

Example

[addons/l10n_il/data/account.group.template.csv](https://github.com/odoo/odoo/blob/16.0/addons/l10n_il/data/account.group.template.csv)

### Taxes

See also

  * [Tax References](../reference/standard_modules/account/account_tax.html#reference-account-tax)

  * [Taxes](../../applications/finance/accounting/taxes.html)

To add taxes you first need to specify tax groups. You normally need just one
tax group for every tax rate, except for the 0% as you need to often
distinguish between exempt, 0%, not subject, … taxes. This model only has two
required fields: _name_ and _country_. Create the file
`data/account_tax_group_data.xml` and list the groups:

    
    
    <odoo>
        <data noupdate="1">
            <record id="tax_group_tva_0" model="account.tax.group">
                <field name="name">TVA 0%</field>
                <field name="country_id" ref="base.ch"/>
            </record>
    
            ...
        </data>
    </odoo>
    

Example

[addons/l10n_ch/data/account_tax_group_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/data/account_tax_group_data.xml)

Example

[addons/l10n_uk/data/account.tax.group.csv](https://github.com/odoo/odoo/blob/16.0/addons/l10n_uk/data/account.tax.group.csv)

Now you can add the taxes via `data/account_tax_template_data.xml` file. The
first tax you define that is purchase/sale also becomes the default
purchase/sale tax for your products.

Example

[addons/l10n_ae/data/account_tax_template_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ae/data/account_tax_template_data.xml)

If some accounts should use default taxes, you can set them up in
`data/account_account_template_post_data.xml`

### Tax Report

Enterprise feature

The tax report is declared in the Invoicing (`account`) app, but the report is
only accessible when Accounting (`account_accountant`) is installed.

See also

  * [Report Line](../reference/standard_modules/account/account_report_line.html)

  * [Tax return (VAT declaration)](../../applications/finance/accounting/reporting/tax_returns.html)

In the previous section, you noticed the fields `invoice_repartition_line_ids`
or `refund_repartition_line_ids` and probably understood nothing about them.
Good news: you are not alone on this incomprehension. Bad news: you have to
figure it out a bit. The topic is complicated. Indeed:

    
    
    accounting_localization/tax_report.dot
    > Graph not rendered because `dot` is not installed

The simple version is that, in the tax template, you indicate in the
invoice/refund repartition lines whether the base or a percentage of the tax
needs to be reported in which report line (through the
_minus/plus_report_line_ids_ fields). It becomes clear also when you check the
tax configuration in the Odoo interface (or check the docs [Tax
References](../reference/standard_modules/account/account_tax.html#reference-
account-tax), [Tax Repartition
References](../reference/standard_modules/account/account_tax_repartition.html#reference-
account-tax-repartition)).

So, once you have properly configured taxes, you just need to add the
`data/account_tax_report_data.xml` file with a record for your
`account.report`. For it to be considered as a tax report, you need to provide
it with the right `root_report_id`.

    
    
    <odoo>
        <record id="tax_report" model="account.report">
            <field name="name">Tax Report</field>
            <field name="root_report_id" ref="account.generic_tax_report"/>
            <field name="country_id" ref="base.XX"/>
        </record>
    
        ...
    </odoo>
    

… followed by the declaration of its lines, as `account.report.line` records.

Example

[addons/l10n_au/data/account_tax_report_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_au/data/account_tax_report_data.xml)

### Fiscal positions

See also

  * [Fiscal Position References](../reference/standard_modules/account/account_fiscal_position.html#reference-account-fiscal-position)

  * [Fiscal positions (tax and account mapping)](../../applications/finance/accounting/taxes/fiscal_positions.html)

Specify fiscal positions in the
`data/account_fiscal_position_template_data.xml` file.

Example

[addons/l10n_es/data/account_fiscal_position_template_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_es/data/account_fiscal_position_template_data.xml)

## Final steps

The last step when installing a localization module is to try to apply its
chart of accounts to the current company (if it does not already have one).
The file `data/account_chart_template_try_loading.xml` is responsible for
that.

Example

[addons/l10n_ch/data/account_chart_template_data.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/data/account_chart_template_data.xml)

Finally, you may add a demo company, so the localization can easily be tested
in demo mode.

Example

[addons/l10n_ch/demo/demo_company.xml](https://github.com/odoo/odoo/blob/16.0/addons/l10n_ch/demo/demo_company.xml)

## Accounting reports

Enterprise feature

See also

[Reporting](../../applications/finance/accounting/reporting.html)

Accounting reports should be added via a separate module `l10n_XX_reports`
that should go to the [enterprise
repository](https://github.com/odoo/enterprise/blob/16.0).

Basic `__manifest__.py` file for such a module looks as following:

    
    
    {
        "name": "COUNTRY - Accounting Reports",
        "category": "Accounting/Localizations/Reporting",
        "version": "1.0.0",
        "license": "OEEL-1",
        "depends": [
            "l10n_XX", "account_reports"
        ],
        "data": [
            "data/balance_sheet.xml",
            "data/profit_and_loss.xml",
        ],
        "auto_install": True,
    }
    

Functional overview of financial reports is here:
[Reporting](../../applications/finance/accounting/reporting.html).

Some good examples:

  * [l10n_ch_reports/data/account_financial_html_report_data.xml](https://github.com/odoo/enterprise/blob/16.0/l10n_ch_reports/data/account_financial_html_report_data.xml)

  * [l10n_be_reports/data/account_financial_html_report_data.xml](https://github.com/odoo/enterprise/blob/16.0/l10n_be_reports/data/account_financial_html_report_data.xml)

You can check the meaning of the fields here:

  * [Report](../reference/standard_modules/account/account_report.html)

  * [Report Line](../reference/standard_modules/account/account_report_line.html)

If you gave a `root_report_id` to your report, it is now available in its
variant selector. If not, you still need to add a menu item for it. A default
menu item can be created from the form view of the report by clicking on
Actions ‣ Create Menu Item. You will then need to refresh the page to see it.
Alternatively, to create a dedicated section for a totally new report in the
Reporting menu, you need to create a new `ir.ui.menu` record (usually in the
main `l10n_XX` module) and a new `ir.actions.client` (usually in the new
report XML file) that calls the `account.report` with the new **report id**.
Then, set the new menu as `parent_id` field in the action model.

Example

  * [ir.ui.menu creation](https://github.com/odoo/odoo/blob/16.0/addons/l10n_be/data/menuitem_data.xml)

  * [ir.actions.client and menu item creation](https://github.com/odoo/enterprise/blob/16.0/l10n_be_reports/data/partner_vat_listing.xml)

