# United Arab Emirates

## Installation

[Install](../../general/apps_modules#general-install) the following
modules to get all the features of the **United Arab Emirates** localization:

Name | Technical name | Description  
---|---|---  
**United Arab Emirates - Accounting** | `l10n_ae` | Default [fiscal localization package](../fiscal_localizations). Includes all accounts, taxes, and reports.  
**U.A.E. - Payroll** | `l10n_ae_hr_payroll` | Includes all rules, calculations, and salary structures.  
**U.A.E. - Payroll with Accounting** | `l10n_ae_hr_payroll_account` | Includes all accounts related to the payroll module.  
**United Arab Emirates - Point of Sale** | `l10n_ae_pos` | Includes the UAE-compliant POS receipt.  
![Select the modules to install.](../../../_images/l10n-ae-modules.png)

## Chart of accounts

Go to Accounting ‣ Configuration ‣ Chart of Accounts to view all default
accounts available for the UAE localization package. You can filter by
**Code** using the numbers on the far left or by clicking on Group By ‣
Account Type. You can **Enable** /**Disable** reconciliation or **configure**
specific accounts according to your needs.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Always keep at least one <b>receivable account</b> and one <b>payable account</b> active.</p></li>
<li><p>It is also advised to <b>keep the accounts below active</b>, as they are used either as transitory
accounts by Konvergo ERP or are specific to the <b>UAE localization package</b>.</p>
<table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Code</p></th>
<th class="head"><p>Account Name</p></th>
<th class="head"><p>Type</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>102011</p></td>
<td><p>Accounts Receivable</p></td>
<td><p>Receivable</p></td>
</tr>
<tr class="row-odd"><td><p>102012</p></td>
<td><p>Accounts Receivable (POS)</p></td>
<td><p>Receivable</p></td>
</tr>
<tr class="row-even"><td><p>201002</p></td>
<td><p>Payables</p></td>
<td><p>Payable</p></td>
</tr>
<tr class="row-odd"><td><p>101004</p></td>
<td><p>Bank</p></td>
<td><p>Bank and Cash</p></td>
</tr>
<tr class="row-even"><td><p>105001</p></td>
<td><p>Cash</p></td>
<td><p>Bank and Cash</p></td>
</tr>
<tr class="row-odd"><td><p>100001</p></td>
<td><p>Liquidity Transfer</p></td>
<td><p>Current Assets</p></td>
</tr>
<tr class="row-even"><td><p>101002</p></td>
<td><p>Outstanding Receipts</p></td>
<td><p>Current Assets</p></td>
</tr>
<tr class="row-odd"><td><p>101003</p></td>
<td><p>Outstanding Payments</p></td>
<td><p>Current Assets</p></td>
</tr>
<tr class="row-even"><td><p>104041</p></td>
<td><p>VAT Input</p></td>
<td><p>Current Assets</p></td>
</tr>
<tr class="row-odd"><td><p>100103</p></td>
<td><p>VAT Receivable</p></td>
<td><p>Non-current Assets</p></td>
</tr>
<tr class="row-even"><td><p>101001</p></td>
<td><p>Bank Suspense Account</p></td>
<td><p>Current Liabilities</p></td>
</tr>
<tr class="row-odd"><td><p>201017</p></td>
<td><p>VAT Output</p></td>
<td><p>Current Liabilities</p></td>
</tr>
<tr class="row-even"><td><p>202001</p></td>
<td><p>End of Service Provision</p></td>
<td><p>Current Liabilities</p></td>
</tr>
<tr class="row-odd"><td><p>202003</p></td>
<td><p>VAT Payable</p></td>
<td><p>Non-current Liabilities</p></td>
</tr>
<tr class="row-even"><td><p>999999</p></td>
<td><p>Undistributed Profits/Losses</p></td>
<td><p>Current Year Earnings</p></td>
</tr>
<tr class="row-odd"><td><p>400003</p></td>
<td><p>Basic Salary</p></td>
<td><p>Expenses</p></td>
</tr>
<tr class="row-even"><td><p>400004</p></td>
<td><p>Housing Allowance</p></td>
<td><p>Expenses</p></td>
</tr>
<tr class="row-odd"><td><p>400005</p></td>
<td><p>Transportation Allowance</p></td>
<td><p>Expenses</p></td>
</tr>
<tr class="row-even"><td><p>400008</p></td>
<td><p>End of Service Indemnity</p></td>
<td><p>Expenses</p></td>
</tr>
</tbody>
</table>
</li>
</ul>
</div>

## Taxes

To access your taxes, go to Accounting ‣ Configuration ‣ Taxes.
Activate/deactivate, or [configure](../accounting/taxes) the taxes
relevant to your business by clicking on them. Remember to only set tax
accounts on the **5%** tax group, as other groups do not need closing. To do
so, enable the [developer mode](../../general/developer_mode) and go to
Configuration ‣ Tax Groups. Then, set a **Tax current account (payable)** ,
**Tax current account (receivable)** , and an **Advance Tax payment account**
for the **5%** group.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <abbr title="Reverse Charge Mechanism">RCM</abbr> is supported by Konvergo ERP.</p>
</div> ![Preview of the UAE localization package's
taxes.](../../../_images/uae-localization-taxes.png)

## Currency exchange rates

To update the currency exchange rates, go to Accounting ‣ Configuration ‣
Settings ‣ Currencies. Click on the update button (**🗘**) found next to the
**Next Run** field.

To launch the update automatically at set intervals, change the **Interval**
from **Manually** to the desired frequency.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, the UAE Central Bank exchange rates web service is used. Several other providers are
available under the <b>Service</b> field.</p>
</div>

## Payroll

The **UAE - Payroll** module creates the necessary **salary rules** in the
Payroll app in compliance with the UAE rules and regulations. The salary rules
are linked to the corresponding accounts in the **chart of accounts**.

![The UAE Employee Payroll Structure.](../../../_images/uae-localization-
salary-rules.png)

### Salary rules

To apply these rules to an employee’s contract, go to Payroll ‣ Contracts ‣
Contracts and select the employee’s contract. In the **Salary Structure Type**
field, select **UAE Employee**.

![Select the Salary Structure Type to apply to the
contract.](../../../_images/uae-localization-salary-structure.png)

Under the **Salary Information** tab, you can find details such as the:

  * **Wage** ;

  * **Housing Allowance** ;

  * **Transportation Allowance** ;

  * **Other Allowances** ;

  * **Number of Days** : used to calculate the end of service provision.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p><b>Leave deductions</b> are calculated using a salary rule linked to the <b>unpaid leave</b> time-off
type;</p></li>
<li><p>Any other deductions or reimbursements are made <em>manually</em> using other inputs;</p></li>
<li><p><b>Overtimes</b> are added <em>manually</em> by going to Work Entries ‣ Work Entries;</p></li>
<li><p><b>Salary attachments</b> are generated by going to Contracts ‣
Salary Attachments. Then, <b>Create</b> an attachment and select the <b>Employee</b>
and the <b>Type (Attachment of Salary, Assignment of Salary, Child Support)</b>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To prevent a rule from appearing on a paycheck, go to Payroll ‣ Configuration
‣ Rules. Click on <b>UAE Employee Payroll Structure</b>, select the rule to hide, and
uncheck <b>Appears on Payslip</b>.</p>
</div>

### End of service provision

The provision is defined as the total monthly allowance _divided_ by 30 and
then _multiplied_ by the number of days set in the field **Number of days** at
the bottom of a contract’s form.

The provision is then calculated via a salary rule associated with two
accounts: the **End Of Service Indemnity (Expense account)** and the **End of
Service Provision (Non-current Liabilities account)**. The latter is used to
pay off the **end of service amount** by settling it with the **payables
account**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The end of service amount is calculated based on the gross salary and the start and end dates of
the employee’s contract.</p>
</div>

### Invoices

The UAE localization package allows the generation of invoices in English,
Arabic, or both. The localization also includes a line to display the **VAT
amount** per line.

