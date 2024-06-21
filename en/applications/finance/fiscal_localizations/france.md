# France

## FEC - Fichier des Écritures Comptables

An FEC Fichier des Écritures Comptables audit file contains all the accounting
data and entries recorded in all the accounting journals for a financial year.
The entries in the file must be arranged in chronological order.

Since January 1st, 2014, every French company is required to produce and
transmit this file upon request by the tax authorities for audit purposes.

### FEC Import

To make the onboarding of new users easier, Konvergo ERP Enterprise’s French [fiscal
localization package](../fiscal_localizations#fiscal-localizations-
packages) includes the **FEC Import** feature (module name:
`l10n_fr_fec_import`), which enables the import of existing FEC files from
older software.

To enable this feature, go to Accounting ‣ Configuration ‣ Settings ‣
Accounting Import, enable **FEC Import** , and _Save_.

Next, go to Accounting ‣ Configuration ‣ FEC Import, upload your FEC file, and
click on _Import_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><div class="line-block">
<div class="line">Importing FEC files from different year takes no particular action or computation.</div>
<div class="line">Should multiple files contain any “Reports à Nouveaux” (RAN) with the starting balance of the
year, you might need to cancel those entries in the User Interface. Konvergo ERP makes those entries
(RAN) useless.</div>
</div>
</div>

#### File formats

FEC files can only be in CSV format, as the XML format is not supported.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>

Our module expects the files to meet the following technical specifications:

  * **Encoding** : UTF-8, UTF-8-SIG and iso8859_15.

  * **Separator** : any of these: `;` or `|` or `,` or `TAB`.

  * **Line terminators** : both CR+LF (`\r\n`) and LF (`\n`) character groups are supported.

  * **Date format** : `%Y%m%d`

#### Fields description and use

# | Field name | Description | Use | Format  
---|---|---|---|---  
01 | JournalCode | Journal Code | `journal.code` and `journal.name` if `JournalLib` is not provided | Alphanumeric  
02 | JournalLib | Journal Label | `journal.name` | Alphanumeric  
03 | EcritureNum | Numbering specific to each journal sequence number of the entry | `move.name` | Alphanumeric  
04 | EcritureDate | Accounting entry Date | `move.date` | Date (yyyyMMdd)  
05 | CompteNum | Account Number | `account.code` | Alphanumeric  
06 | CompteLib | Account Label | `account.name` | Alphanumeric  
07 | CompAuxNum | Secondary account Number (accepts null) | `partner.ref` | Alphanumeric  
08 | CompAuxLib | Secondary account Label (accepts null) | `partner.name` | Alphanumeric  
09 | PieceRef | Document Reference | `move.ref` and `move.name` if `EcritureNum` is not provided | Alphanumeric  
10 | PieceDate | Document Date | `move.date` | Date (yyyyMMdd)  
11 | EcritureLib | Account entry Label | `move_line.name` | Alphanumeric  
12 | Debit | Debit amount | `move_line.debit` | Float  
13 | Credit | Credit amount (Field name “Crédit” is not allowed) | `move_line.credit` | Float  
14 | EcritureLet | Accounting entry cross reference (accepts null) | `move_line.fec_matching_number` | Alphanumeric  
15 | DateLet | Accounting entry date (accepts null) | unused | Date (yyyyMMdd)  
16 | ValidDate | Accounting entry validation date | unused | Date (yyyyMMdd)  
17 | Montantdevise | Currency amount (accepts null) | `move_line.amount_currency` | Float  
18 | Idevise | Currency identifier (accepts null) | `currency.name` | Alphanumeric  
  
These two fields can be found in place of the others in the sence above.

12 | Montant | Amount | `move_line.debit` or `move_line.credit` | Float  
---|---|---|---|---  
13 | Sens | Can be “C” for Credit or “D” for Debit | determines `move_line.debit` or `move_line.credit` | Char  
  
#### Implementation details

The following accounting entities are imported from the FEC files: **Accounts,
Journals, Partners** , and **Moves**.

Our module determines the encoding, the line-terminator character, and the
separator that are used in the file.

A check is then performed to see if every line has the correct number of
fields corresponding to the header.

If the check passes, then the file is read in full, kept in memory, and
scanned. Accounting entities are imported one type at a time, in the following
order.

##### Accounts

Every accounting entry is related to an account, which should be determined by
the field `CompteNum`.

##### Code matching

Should a similar account code already be present in the system, the existing
one is used instead of creating a new one.

Accounts in Konvergo ERP generally have a number of digits that are default for the
fiscal localization. As the FEC module is related to the French localization,
the default number of relevant digits is 6.

This means that the account codes the trailing zeroes are right-trimmed, and
that the comparison between the account codes in the FEC file and the ones
already existing in Konvergo ERP is performed only on the first six digits of the
codes.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The account code <code>65800000</code> in the file is matched against an existing <code>658000</code> account in Konvergo ERP,
and that account is used instead of creating a new one.</p>
</div>

##### Reconcilable flag

An account is technically flagged as _reconcilable_ if the first line in which
it appears has the `EcritureLet` field filled out, as this flag means that the
accounting entry is going to be reconciled with another one.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In case the line somehow has this field not filled out, but the entry still has to be reconciled
with a payment that hasn’t yet been recorded, this isn’t a problem anyway; the account is
flagged as reconcilable as soon as the import of the move lines requires it.</p>
</div>

##### Account type and Templates matching

As the **type** of the account is not specified in the FEC format, **new**
accounts are created with the default type _Current Assets_ and then, at the
end of the import process, they are matched against the installed Chart of
Account templates. Also, the _reconcile_ flag is also computed this way.

The match is done with the left-most digits, starting by using all digits,
then 3, then 2.

<div class="alert alert-success">
<p class="alert-title">
Example</p><table class="table docutils">
<colgroup>
<col style="width: 14%"/>
<col style="width: 14%"/>
<col style="width: 20%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Code</p></th>
<th class="head"><p>Full comparison</p></th>
<th class="head"><p>3-digits comparison</p></th>
<th class="head"><p>2-digits comparison</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Template</p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-odd"><td><p>CompteNum</p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>401</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-even"><td><p><b>Result</b></p></td>
<td></td>
<td></td>
<td></td>
<td><p>Match <b>found</b></p></td>
</tr>
</tbody>
</table>
</div>

The type of the account is then flagged as _payable_ and _reconcilable_ as per
the account template.

##### Journals

Journals are also checked against those already existing in Konvergo ERP to avoid
duplicates, also in the case of multiple FEC files imports.

Should a similar journal code already be present in the system, the existing
one is used instead of creating a new one.

New journals have their name prefixed by the string `FEC-`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><code>ACHATS</code> -&gt; <code>FEC-ACHATS</code></p>
</div>

The journals are _not_ archived, the user is entitled to handle them as he
wishes.

##### Journal type determination

The journal type is also not specified in the format (as per the accounts) and
therefore it is at first created with the default type `general`.

At the end of the import process, the type is determined as per these rules
regarding related moves and accounts:

  * `bank`: Moves in these journals always have a line (debit or credit) impacting a liquidity account.

`cash` / `bank` can be interchanged, so `bank` is set everywhere when this
condition is met.

  * `sale`: Moves in these journals mostly have debit lines on receivable accounts and credit lines on tax income accounts.

Sale refund journal items are debit/credit inverted.

  * `purchase`: Moves in these journals mostly have credit lines on payable accounts and debit lines on expense accounts.

Purchase refund journal items are debit/credit inverted.

  * `general`: for everything else.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>A minimum of three moves is necessary for journal type identification.</p></li>
<li><p>A threshold of 70% of moves must correspond to a criteria for a journal type to be determined.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Suppose we are analyzing the moves that share a certain <code>journal_id</code>.</p>
<table class="table docutils">
<colgroup>
<col style="width: 76%"/>
<col style="width: 9%"/>
<col style="width: 15%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Moves</p></th>
<th class="head"><p>Count</p></th>
<th class="head"><p>Percentage</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>that have a sale account line and no purchase account line</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
<tr class="row-odd"><td><p>that have a purchase account line and no sale account line</p></td>
<td><p>1</p></td>
<td><p>25%</p></td>
</tr>
<tr class="row-even"><td><p>that have a liquidity account line</p></td>
<td><p>3</p></td>
<td><p><b>75%</b></p></td>
</tr>
<tr class="row-odd"><td><p><b>Total</b></p></td>
<td><p>4</p></td>
<td><p>100%</p></td>
</tr>
</tbody>
</table>
<p>The journal <code>type</code> would be <code>bank</code>, because the bank moves percentage (75%) exceeds the threshold
(70%).</p>
</div>

##### Partners

Each partner keeps its `Reference` from the field `CompAuxNum`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>These fields are searchable, in line with former FEC imports on the accounting expert’s side for
fiscal/audit purposes.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Users can merge partners with the Data Cleaning App, where Vendors and Customers or similar
partner entries may be merged by the user, with assistance from the system that groups them by
similar entries.</p>
</div>

##### Moves

Entries are immediately posted and reconciled after submission, using the
`EcritureLet` field to do the matching between the entries themselves.

The `EcritureNum` field represents the name of the moves. We noticed that
sometimes it may not be filled out. In this case, the field `PieceRef` is
used.

##### Rounding issues

There is a rounding tolerance with a currency-related precision on debit and
credit (i.e., 0.01 for EUR). Under this tolerance, a new line is added to the
move, named _Import rounding difference_ , targeting the accounts:

  * `658000` Charges diverses de gestion courante, for added debits

  * `758000` Produits divers de gestion courante, for added credits

##### Missing move name

Should the `EcritureNum` not be filled out, it may also happen that the
`PieceRef` field is also not suited to determine the move name (it may be used
as an accounting move line reference) leaving no way to actually find which
lines are to be grouped in a single move, and effectively impeding the
creation of balanced moves.

One last attempt is made, grouping all lines from the same journal and date
(`JournalLib`, `EcritureDate`). Should this grouping generate balanced moves
(sum(credit) - sum(debit) = 0), then each different combination of journal and
date creates a new move.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>0

Should this attempt fail, the user is prompted an error message with all the
move lines that are supposedly unbalanced.

##### Partner information

If a line has the partner information specified, the information is copied to
the accounting move itself if the targeted Journal is of type _payable_ or
_receivable_.

### Export

If you have installed the French [fiscal localization
package](../fiscal_localizations#fiscal-localizations-packages), you
should be able to download the FEC. To do so, go to Accounting ‣ Reporting ‣
France ‣ FEC.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>1 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>2

## French Accounting Reports

If you have installed the French Accounting, you will have access to some
accounting reports specific to France:

  * Bilan comptable

  * Compte de résultats

  * Plan de Taxes France

## Get the VAT anti-fraud certification with Konvergo ERP

As of January 1st 2018, a new anti-fraud legislation comes into effect in
France and DOM-TOM. This new legislation stipulates certain criteria
concerning the inalterability, security, storage and archiving of sales data.
These legal requirements are implemented in Konvergo ERP, version 9 onward, through a
module and a certificate of conformity to download.

### Is my company required to use anti-fraud software?

Your company is required to use an anti-fraud cash register software like Konvergo ERP
(CGI art. 286, I. 3° bis) if:

  * You are taxable (not VAT exempt) in France or any DOM-TOM,

  * Some of your customers are private individuals (B2C).

This rule applies to any company size. Auto-entrepreneurs are exempted from
VAT and therefore are not affected.

### Get certified with Konvergo ERP

Getting compliant with Konvergo ERP is very easy.

Your company is requested by the tax administration to deliver a certificate
of conformity testifying that your software complies with the anti-fraud
legislation. This certificate is granted by Konvergo ERP SA to Konvergo ERP Enterprise users
[here](https://www.odoo.com/my/contract/french-certification/). If you use
Konvergo ERP Community, you should [upgrade to Konvergo ERP
Enterprise](../../../administration/on_premise/community_to_enterprise)
or contact your Konvergo ERP service provider.

In case of non-conformity, your company risks a fine of €7,500.

To get the certification, just follow the following steps:

  * If you use **Konvergo ERP Point of Sale** , [install](../../general/apps_modules#general-install) the **France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis)** module by going to Apps, removing the _Apps_ filter, then searching for _l10n_fr_pos_cert_ , and installing the module.

  * Make sure a country is set on your company, otherwise your entries won’t be encrypted for the inalterability check. To edit your company’s data, go to Settings ‣ Users & Companies ‣ Companies. Select a country from the list; Do not create a new country.

  * Download the mandatory certificate of conformity delivered by Konvergo ERP SA [here](https://www.odoo.com/my/contract/french-certification/).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>3

### Anti-fraud features

The anti-fraud module introduces the following features:

  * **Inalterability** : deactivation of all the ways to cancel or modify key data of POS orders, invoices and journal entries;

  * **Security** : chaining algorithm to verify the inalterability;

  * **Storage** : automatic sales closings with computation of both period and cumulative totals (daily, monthly, annually).

#### Inalterability

All the possible ways to cancel and modify key data of paid POS orders,
confirmed invoices and journal entries are deactivated, if the company is
located in France or in any DOM-TOM.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>4

#### Security

To ensure inalterability, every order or journal entry is encrypted upon
validation. This number (or hash) is calculated from the key data of the
document as well as from the hash of the precedent documents.

The module introduces an interface to test the data inalterability. If any
information is modified on a document after its validation, the test will
fail. The algorithm recomputes all the hashes and compares them against the
initial ones. In case of failure, the system points out the first corrupted
document recorded in the system.

Users with _Manager_ access rights can launch the inalterability check. For
POS orders, go to Point of Sales ‣ Reporting ‣ French Statements. For invoices
or journal entries, go to Invoicing/Accounting ‣ Reporting ‣ French
Statements.

#### Storage

The system also processes automatic sales closings on a daily, monthly and
annual basis. Such closings distinctly compute the sales total of the period
as well as the cumulative grand totals from the very first sales entry
recorded in the system.

Closings can be found in the _French Statements_ menu of Point of Sale,
Invoicing and Accounting apps.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>6

### Responsibilities

Do not uninstall the module! If you do so, the hashes will be reset and none
of your past data will be longer guaranteed as being inalterable.

Users remain responsible for their Konvergo ERP instance and must use it with due
diligence. It is not permitted to modify the source code which guarantees the
inalterability of data.

Konvergo ERP absolves itself of all and any responsibility in case of changes in the
module’s functions caused by 3rd party applications not certified by Konvergo ERP.

### More Information

You can find more information about this legislation in the following official
documents.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The FEC CSV file has a plain text format representing a data table, with the first line being a
header and defining the list of fields for each entry, and each following line representing one
accounting entry, in no predetermined order.</p>
</div>7

