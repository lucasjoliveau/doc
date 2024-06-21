# RST cheat sheet

## Headings

For each formatting line (e.g., `===`), write as many symbols (`=`) as there
are characters in the header.

The symbols used for the formatting are, in fact, not important. Only the
order in which they are written matters, as it determines the size of the
decorated heading. This means that you may encounter different heading
formatting and in a different order, in which case you should follow the
formatting in place in the document. In any other case, use the formatting
shown below.

Heading size | Formatting  
---|---  
H1 | 
    
    
    =======
    Heading
    =======
      
  
H2 | 
    
    
    Heading
    =======
      
  
H3 | 
    
    
    Heading
    -------
      
  
H4 | 
    
    
    Heading
    ~~~~~~~
      
  
H5 | 
    
    
    Heading
    *******
      
  
H6 | 
    
    
    Heading
    ^^^^^^^
      
  
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Each document must have <b>exactly one H1 heading</b>. No less, no more.</p>
</div>

## Markups

### Emphasis (italic)

To emphasize a part of the text. The text is rendered in italic.

Fill out the information _before_ saving the form.  
---  
      
    
    Fill out the information *before* saving the form.
      
  
### Strong emphasis (bold)

To emphasize a part of the text. The text is rendered in bold.

A **subdomain** is a domain that is a part of another domain.  
---  
      
    
    A **subdomain** is a domain that is a part of another domain.
      
  
### Technical term (literal)

To write a technical term or a specific value to insert. The text is rendered
in literal.

Insert the IP address of your printer, for example, `192.168.1.25`.  
---  
      
    
    Insert the IP address of your printer, for example, `192.168.1.25`.
      
  
### Definitions

Use the `dfn` markup to define a term.

The documentation is written in RST and needs to be built (converted to HTML)
to display nicely.  
---  
      
    
    The documentation is written in RST and needs to be built (:dfn:`converted to HTML`) to display
    nicely.
      
  
### Abbreviations

Use the `abbr` markup to write a self-defining abbreviation that is displayed
as a tooltip.

Konvergo ERP uses OCR and artificial intelligence technologies to recognize the
content of the documents.  
---  
      
    
    Konvergo ERP uses :abbr:`OCR (optical character recognition)` and artificial intelligence technologies to
    recognize the content of the documents.
      
  
### GUI element

Use the `guilabel` markup to identify any text of the interactive user
interface (e.g., button labels, view titles, field names, lists items, …).

Update your credentials, then click on **Save**.  
---  
      
    
    Update your credentials, then click on :guilabel:`Save`.
      
  
### Menu selection

Use the `menuselection` markup to guide the user through a sequence of menus.

To review your sales performance, go to Sales ‣ Reporting ‣ Dashboard.  
---  
      
    
    To review your sales performance, go to :menuselection:`Sales --> Reporting --> Dashboard`.
      
  
### File

Use the `file` markup to indicate a file path or name.

Create redirections with the `redirects.txt` file at the root of the
repository.  
---  
      
    
    Create redirections with the :file:`redirects.txt` file at the root of the repository.
      
  
### Command

Use the `command` markup to highlight a command.

Run the command **make clean html** to delete existing built files and build
the documentation to HTML.  
---  
      
    
    Run the command :command:`make clean html` to delete existing built files and build the
    documentation to HTML.
      
  
### Icons

Use the `icon` markup to add a class name of an icon. There are two icon sets
used in Konvergo ERP: [FontAwesome4](https://fontawesome.com/v4/icons/) and [Konvergo ERP
UI](../../developer/reference/user_interface/icons). It is recommended to
accompany an icon with a GUI element as a descriptor, however, it is not
mandatory.

The graph view is represented by the __**(area chart)** icon. The pivot view
is represented by the __icon.  
---  
      
    
    The graph view is represented by the :icon:`fa-area-chart` :guilabel:`(area chart)` icon.
    The pivot view is represented by the :icon:`oi-view-pivot` icon.
      
  
## Lists

### Bulleted list

  * This is a bulleted list.
  * It has two items, the second item uses two lines.

  
---  
      
    
    - This is a bulleted list.
    - It has two items, the second
      item uses two lines.
      
  
### Numbered list

  1. This is a numbered list.
  2. Numbering is automatic.

  
---  
      
    
    #. This is a numbered list.
    #. Numbering is automatic.
      
  
  6. Use this format to start the numbering with a number other than one.
  7. The numbering is automatic from there.

  
---  
      
    
    6. Use this format to start the numbering
       with a number other than one.
    #. The numbering is automatic from there.
      
  
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>

### Nested lists

  * This is the first item of a bulleted list.
    1. It has a nested numbered list
    2. with two items.

  
---  
      
    
    - This is the first item of a bulleted list.
    
      #. It has a nested numbered list
      #. with two items.
      
  
## Hyperlinks

### External hyperlinks

External hyperlinks are links to a URL with a custom label. They follow this
syntax: ``label <URL>`_`

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The URL can be a relative path to a file within the documentation.</p></li>
<li><p>Use the <a href="#contributing-doc-pages-hyperlinks"><span class="std std-ref">documentation pages hyperlinks</span></a> if you target
another documentation page.</p></li>
</ul>
</div>  For instance, [this is an external hyperlink to Konvergo ERP’s
website](https://www.odoo.com).  
---  
      
    
    For instance, `this is an external hyperlink to Konvergo ERP's website <https://www.odoo.com>`_.
      
  
### External hyperlink aliases

External hyperlink aliases allow creating shortcuts for external hyperlinks.

The definition syntax is as follows: `.. _target: URL`

There are two ways to reference them, depending on the use case:

  1. `target_` creates a hyperlink with the target name as label and the URL as reference. Note that the `_` moved after the target!

  2. ``label <target_>`_` does exactly what you expect: the label replaces the name of the target, and the target is replaced by the URL.

A [proof-of-concept](https://en.wikipedia.org/wiki/Proof_of_concept) is a
simplified version, a prototype of what is expected to agree on the main lines
of expected changes. [PoC](https://en.wikipedia.org/wiki/Proof_of_concept) is
a common abbreviation.  
---  
      
    
    .. _proof-of-concept: https://en.wikipedia.org/wiki/Proof_of_concept
    
       A proof-of-concept_ is a simplified version, a prototype of what is expected to agree on the main
       lines of expected changes. `PoC <proof-of-concept_>`_ is a common abbreviation.
      
  
### Custom anchors

Custom anchors follow the same syntax as external hyperlink aliases but
without any URL. Indeed, they are internal. They allow referencing a specific
part of a document by using the target as an anchor. When the user clicks on
the reference, the documentation scrolls to the part of the page containing
the anchor.

The definition syntax is: `.. _target:`

There are two ways to reference them, both using the `ref` markup:

  1. `:ref:`target`` creates a hyperlink to the anchor with the heading defined below as label.

  2. `:ref:`label <target>`` creates a hyperlink to the anchor with the given label.

See [Use relative links for internal URLs](rst_guidelines#contributing-
relative-links) to learn how to write proper relative links for internal
references.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Custom anchors can be referenced from other files than the ones in which they are defined.</p></li>
<li><p>Notice that there is no <code>_</code> at the end, contrary to what is done with <a href="#contributing-external-hyperlinks"><span class="std std-ref">external
hyperlinks</span></a>.</p></li>
</ul>
</div>  This can easily be done by creating a new product, see
[How to create a product?](https://example.com/product) for additional help.
**How to create a product?** As explained at the [start of the
page](https://example.com/scroll-to-start-of-page), …  
---  
      
    
    .. _sales/quotation/start-of-page:
    
    This can easily be done by creating a new product, see :ref:`product` for additional help.
    
    .. _sales/quotation/product:
    
    How to create a product?
    ========================
    
    As explained at the :ref:`start of the page <sales/quotation/start-of-page>`, ...
      
  
### Documentation pages hyperlinks

The `doc` markup allows referencing a documentation page wherever it is in the
file tree through a relative file path.

As usual, there are two ways to use the markup:

  1. `:doc:`path_to_doc_page`` creates a hyperlink to the documentation page with the title of the page as label.

  2. `:doc:`label <path_to_doc_page>`` creates a hyperlink to the documentation page with the given label.

Please refer to [this
documentation](https://example.com/doc/accounting/invoices) and to [Send
a pro-forma invoice](https://example.com/doc/sales/proforma).  
---  
      
    
    Please refer to :doc:`this documentation <customer_invoices>` and to
    :doc:`../sales/sales/invoicing/proforma`.
      
  
### File download hyperlinks

The `download` markup allows referencing files (that are not necessarily RST
documents) within the source tree to be downloaded.

Download this [module structure
template](https://example.com/doc/odoosh/extras/my_module.zip) to start
building your module in no time.  
---  
      
    
    Download this :download:`module structure template <extras/my_module.zip>` to start building your
    module in no time.
      
  
## Images

The `image` markup allows inserting images in a document.

![Create an invoice.](../../_images/create-invoice1.png)  
---  
      
    
    .. image:: rst_cheat_sheet/create-invoice.png
       :align: center
       :alt: Create an invoice.
      
  
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Add the <code>:class: o-no-modal</code> <a href="https://docutils.sourceforge.io/docs/ref/rst/directives#common-options">option</a> to an image to
prevent opening it in a modal.</p>
</div>

## Alert blocks (admonitions)

### See also

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://example.com/doc/accounting/invoices">Customer invoices</a></p></li>
<li><p><a href="https://example.com/doc/sales/proforma#activate-the-feature">Pro-forma invoices</a></p></li>
</ul>
</div>  
---  
      
    
    .. seealso::
       - :doc:`customer_invoices`
       - `Pro-forma invoices <../sales/sales/invoicing/proforma.html#activate-the-feature>`_
      
  
### Note

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Use this alert block to grab the reader’s attention about additional information.</p>
</div>  
---  
      
    
    .. note::
       Use this alert block to grab the reader's attention about additional information.
      
  
### Tip

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Use this alert block to inform the reader about a useful trick that requires an action.</p>
</div>  
---  
      
    
    .. tip::
       Use this alert block to inform the reader about a useful trick that requires an action.
      
  
### Example

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Use this alert block to show an example.</p>
</div>  
---  
      
    
    .. example::
       Use this alert block to show an example.
      
  
### Exercise

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Use this alert block to suggest an exercise to the reader.</p>
</div>  
---  
      
    
    .. exercise::
       Use this alert block to suggest an exercise to the reader.
      
  
### Important

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>0  
---  
      
    
    .. important::
       Use this alert block to notify the reader about important information.
      
  
### Warning

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>1  
---  
      
    
    .. warning::
       Use this alert block to require the reader to proceed with caution with what is described in the
       warning.
      
  
### Danger

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>2  
---  
      
    
    .. danger::
       Use this alert block to bring the reader's attention to a serious threat.
      
  
### Custom

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>3  
---  
      
    
    .. admonition:: Title
    
       Customize this alert block with a **Title** of your choice.
      
  
## Tables

### List tables

List tables use two-level bulleted lists to convert data into a table. The
first level represents the rows and the second level represents the columns.

| Name | Country | Favorite color  
---|---|---  
Raúl | Montenegro | Purple  
Mélanie | France | Red  
      
    
    .. list-table::
       :header-rows: 1
       :stub-columns: 1
    
       * - Name
         - Country
         - Favorite colour
       * - Raúl
         - Montenegro
         - Purple
       * - Mélanie
         - France
         - Turquoise
      
  
### Grid tables

Grid tables represent the rendered table and are more visual to work with.

|  | Shirts | T-shirts  
---|---|---  
**Available colours** | Purple | Green  
Turquoise | Orange  
**Sleeves length** | Long sleeves | Short sleeves  
      
    
    +-----------------------+--------------+---------------+
    |                       | Shirts       | T-shirts      |
    +=======================+==============+===============+
    | **Available colours** | Purple       | Green         |
    |                       +--------------+---------------+
    |                       | Turquoise    | Orange        |
    +-----------------------+--------------+---------------+
    | **Sleeves length**    | Long sleeves | Short sleeves |
    +-----------------------+--------------+---------------+
      
  
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>4

## Code blocks

    
    
    def main():
        print("Hello world!")
      
  
---  
      
    
    .. code-block:: python
    
       def main():
           print("Hello world!")
      
  
## Spoilers

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>5  
---  
      
    
    .. spoiler:: Answer to the Ultimate Question of Life, the Universe, and Everything
    
       **42**
      
  
## Content tabs

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Prefer the use of autonumbered lists with <code>#.</code> for better code resilience.</p>
</div>6

### Basic tabs

Basic tabs are useful to split the content into multiple options. The `tabs`
markup is used to define sequence of tabs. Each tab is then defined with the
`tab` markup followed by a label.

Konvergo ERP OnlineKonvergo ERP.shOn-premiseContent dedicated to Konvergo ERP Online users.
Alternative for Konvergo ERP.sh users. Third version for On-premise users.  
---  
      
    
    .. tabs::
    
       .. tab:: Konvergo ERP Online
    
          Content dedicated to Konvergo ERP Online users.
    
       .. tab:: Konvergo ERP.sh
    
          Alternative for Konvergo ERP.sh users.
    
       .. tab:: On-premise
    
          Third version for On-premise users.
      
  
### Nested tabs

Tabs can be nested inside one another.

StarsMoons The SunProxima CentauriPolarisThe closest star to us. The second
closest star to us. The North Star. The MoonTitanOrbits the Earth. Orbits
Jupiter.  
---  
      
    
    .. tabs::
    
       .. tab:: Stars
    
          .. tabs::
    
             .. tab:: The Sun
    
                The closest star to us.
    
             .. tab:: Proxima Centauri
    
                The second closest star to us.
    
             .. tab:: Polaris
    
                The North Star.
    
       .. tab:: Moons
    
          .. tabs::
    
             .. tab:: The Moon
    
                Orbits the Earth.
    
             .. tab:: Titan
    
                Orbits Jupiter.
      
  
### Group tabs

Group tabs are special tabs that synchronize based on a group label. The last
selected group is remembered and automatically selected when the user returns
to the page or visits another page with the tabs group. The `group-tab` markup
is used to define group tabs.

C++PythonJavaC++ Python Java C++PythonJava

    
    
    int main(const int argc, const char **argv) {
        return 0;
    }
    
    
    
    def main():
        return
    
    
    
    class Main {
        public static void main(String[] args) {}
    }
      
  
---  
      
    
    .. tabs::
    
       .. group-tab:: C++
    
          C++
    
       .. group-tab:: Python
    
          Python
    
       .. group-tab:: Java
    
          Java
    
    .. tabs::
    
       .. group-tab:: C++
    
          .. code-block:: c++
    
             int main(const int argc, const char **argv) {
                 return 0;
             }
    
       .. group-tab:: Python
    
          .. code-block:: python
    
             def main():
                 return
    
       .. group-tab:: Java
    
          .. code-block:: java
    
             class Main {
                 public static void main(String[] args) {}
             }
      
  
### Code tabs

Code tabs are essentially group tabs that treat the content as a code block.
The `code-tab` markup is used to define a code tab. Just as for the `code-
block` markup, the language defines the syntax highlighting of the tab. If
set, the label is used instead of the language for grouping tabs.

Hello C++Hello PythonHello JavaScript

    
    
    #include <iostream>
    
    int main() {
        std::cout << "Hello World";
        return 0;
    }
    
    
    
    print("Hello World")
    
    
    
    console.log("Hello World");
      
  
---  
      
    
    .. tabs::
    
       .. code-tab:: c++ Hello C++
    
          #include <iostream>
    
          int main() {
              std::cout << "Hello World";
              return 0;
          }
    
       .. code-tab:: python Hello Python
    
          print("Hello World")
    
       .. code-tab:: javascript Hello JavaScript
    
          console.log("Hello World");
      
  
## Cards

#### [DocumentationUse this guide to acquire the tools and knowledge you need
to write documentation. Step-by-step guide](../documentation)####
[Content guidelinesList of guidelines and trips and tricks to make your
content shine at its brightest! ](content_guidelines)#### [RST
guidelinesList of technical guidelines to observe when writing with
reStructuredText. ](rst_guidelines)  
---  
      
    
    .. cards::
    
       .. card:: Documentation
          :target: ../documentation
          :tag: Step-by-step guide
          :large:
    
          Use this guide to acquire the tools and knowledge you need to write documentation.
    
       .. card:: Content guidelines
          :target: content_guidelines
    
          List of guidelines and trips and tricks to make your content shine at its brightest!
    
       .. card:: RST guidelines
          :target: rst_guidelines
    
          List of technical guidelines to observe when writing with reStructuredText.
      
  
## Document metadata

Sphinx supports document-wide metadata markups that specify a behavior for the
entire page.

They must be placed between colons (`:`) at the top of the source file.

**Metadata** | **Purpose**  
---|---  
`show-content` | Make a toctree page accessible from the navigation menu.  
`show-toc` | Show the table of content on a page that has the `show-content` metadata markup.  
`code-column` |  Show a dynamic side column that can be used to display interactive tutorials or code excerpts. For example, see [Aide-mémoire de la comptabilité](../../applications/finance/accounting/get_started/cheat_sheet).  
`hide-page-toc` | Hide the « On this page » sidebar and use full page width for the content.  
`custom-css` | Link CSS files (comma-separated) to the document.  
`custom-js` | Link JS files (comma-separated) to the document.  
`classes` | Assign the specified classes to the `<main/>` element of the document.  
`orphan` | Suppress the need to include the document in a toctree.  
`nosearch` | Exclude the document from search results.  
  
## Formatting tips

### Break the line but not the paragraph

A first long line that you break in two -> here <\- is rendered as a single
line. A second line that follows a line break.  
---  
      
    
    | A first long line that you break in two
      -> here <- is rendered as a single line.
    | A second line that follows a line break.
      
  
### Escape markup symbols (Advanced)

Markup symbols escaped with backslashes (`\`) are rendered normally. For
instance, `this \*\*line of text\*\* with \*markup\* symbols` is rendered as
“this **line of text** with *markup* symbols”.

When it comes to backticks (```), which are used in many cases such as
external hyperlinks, using backslashes for escaping is no longer an option
because the outer backticks interpret enclosed backslashes and thus prevent
them from escaping inner backticks. For instance, ``\`this formatting\```
produces an `[UNKNOWN NODE title_reference]` error. Instead, ````this
formatting```` should be used to produce the following result: ``this
formatting``.

  *[OCR]: optical character recognition
  *[GUI]: graphical user interface
  *[RST]: reStructuredText

