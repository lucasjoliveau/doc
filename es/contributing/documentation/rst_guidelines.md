# RST guidelines

## Use relative links for internal URLs

If you need to reference an internal documentation page or a file that is not
sitting in the same directory as your current page, always make use of
_relative file paths_ rather than _absolute file paths_. An absolute file path
indicates the location of the target from the root of its file tree. A
relative file path makes use of smart notations (such as `../` that redirects
to the parent folder) to indicate the location of the target _relative_ to
that of the source document.

### Example

Given the following source file tree:

    
    
    documentation
    ├── content
    │   └── applications
    │   │   └── sales
    │   │   │   └── sales
    │   │   │   │   └── products_prices
    │   │   │   │   │   └── products
    │   │   │   │   │   │   └── import.rst
    │   │   │   │   │   │   └── variants.rst
    │   │   │   │   │   └── prices.rst
    

A reference to the rendered `prices.html` and `variants.html` could be made
from `import.rst` as follows:

  1. Absolute:

     * `https://odoo.com/documentation/16.0/applications/sales/sales/products_prices/prices.html`

     * `https://odoo.com/documentation/16.0/applications/sales/sales/products_prices/products/variants.html`

  2. Relative:

     * `../prices.html`

     * `variants.html`

The relative links are clearly superior in terms of readability and stability:
the references survive version updates, folder name changes and file tree
restructurations.

## Start a new line before the 100th character

In RST, it is possible to break a line without forcing a line break on the
rendered HTML. Make use of this feature to write **lines of maximum 100
characters**. A line break in a sentence results in an additional whitespace
in HTML. That means that you do not need to leave a trailing whitespace at the
end of a line to separate words.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>You can safely break a line around the separators (<code>--&gt;</code>) of <code>menuselection</code> markups and
anywhere in a hyperlink reference. For the <code>doc</code>, <code>ref</code> and <code>download</code> markups, this is
only true for the label part of the reference.</p>
</div>

### Example: Line breaks within markups

    
    
    To register your seller account in Konvergo ERP, go to :menuselection:`Sales --> Configuration --> Settings
    --> Amazon Connector --> Amazon Accounts` and click on :guilabel:`CREATE`. You can find the **Seller
    ID** under the link :guilabel:`Your Merchant Token`.
    

## Be consistent with indentation

Use only spaces (never tabs).

Use as many spaces at the beginning of an indented line as needed to align it
with the first character of the markup in the line above. This usually implies
3 spaces but you only need 2 for bulleted lists.

### Example: The first `:` is below the `i` (3 spaces)

    
    
    .. image:: media/example.png
       :align: center
       :alt: example
    

### Example: The `:titlesonly:` and page references start below the `t` (3
spaces)

    
    
    .. toctree::
       :titlesonly:
    
       payables/supplier_bills
       payables/pay
    

### Example: Continuation lines resume below the `I`’s of “Invoice” (2
spaces)

    
    
    - Invoice on ordered quantity: invoice the full order as soon as the sales order is confirmed.
    - Invoice on delivered quantity: invoice on what you delivered even if it's a partial delivery.
    

## Use the menuselection markup

Although chaining characters `‣` and menu names works fine to indicate a user
which menus to click, it is best to use the `menuselection` markup (see Use
the menuselection markup) for the same result. Indeed, it renders the menus
chain consistently with the rest of the documentation and would automatically
adapt to the new graphic chart if we were to switch to a new one. This markup
is used inline as follows: `:menuselection:`Sales --> Settings --> Products
--> Variants``.

## Write resilient code

  * Prefer the use of `#.` in numbered lists instead of `1.`, `2.`, etc. This removes the risk of breaking the numbering when adding new elements to the list and is easier to maintain.

  * Avoid using implicit hyperlink targets and prefer internal hyperlink targets instead. Referencing the implicit target `How to print quotations?` is more prone to break than a reference to the explicit target `_print_quotation` which never appears in the rendered HTML and is thus even less likely to be modified.

## Prefix hyperlink targets with application names

As hyperlink targets are visible from the entire documentation when referenced
with the `ref` markup, it is recommended to prefix the target name with that
of the related application. For instance, naming a target `_amazon/form`
instead of `_form` avoids unwanted behaviors and makes the purpose of the
target clear.

## Don’t break hyperlink targets

When refactoring (improving without adding new content) section headings or
hyperlink targets, take care not to break any hyperlink reference to these
targets or update them accordingly.

## Use single-underscore suffixes for hyperlink references

Although using a double-underscore suffix works most of the time for classic
hyperlink references, it is not recommended as double-underscores normally
indicate an anonymous hyperlink reference. This is a special kind of hyperlink
reference that makes use of nameless hyperlink targets consisting only of two
underscore.

tl;dr: Double-underscore suffixes work until they don’t and are bad practice,
use single-underscore suffixes instead.

