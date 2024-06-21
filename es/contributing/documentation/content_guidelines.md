# Content guidelines

To give the community the best documentation possible, we listed here a few
guidelines, tips and tricks that will make your content shine at its
brightest! While we encourage you to adopt your own writing style, some rules
still apply to give the reader more clarity and comprehension.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We strongly recommend contributors to carefully read the other documents related to this section
of the documentation. Good knowledge of the ins and outs of <b>RST writing</b> is required to write
and submit your contribution. Note that it also affects your writing style itself.</p>
<ul>
<li><p><a href="../documentation">Documentation</a></p></li>
<li><p><a href="rst_cheat_sheet">RST cheat sheet</a></p></li>
<li><p><a href="rst_guidelines">RST guidelines</a></p></li>
</ul>
</div>

## Writing style

**Writing for documentation** isn’t the same as writing for a blog or another
medium. Readers are more likely to skim read until they’ve found the
information they are looking for. Keep in mind that the user documentation is
a place to inform and describe, not to convince and promote.

### Consistency

_Consistency is key to everything._

Make sure that your writing style remains **consistent**. If you modify an
existing text, try to match the existing tone and presentation, or rewrite it
to match your own style.

### Grammatical tenses

In English, descriptions and instructions require the use of a **Present
Tense** , while a _future tense_ is appropriate only when a specific event is
to happen ulteriorly. This logic might be different in other languages.

  * Good example (present):

_Screenshots are automatically resized to fit the content block’s width._

  * Bad example (future):

_When you take a screenshot, remember that it will be automatically resized to
fit the content block’s width._

### Paragraphing

A paragraph comprises several sentences that are linked by a shared idea. They
usually are two to six lines long.

In English, a new idea implies a new paragraph, rather than having a _line
break_ as it is common to do in some other languages. _Line breaks_ are useful
for layout purposes but shouldn’t be used as a grammatical way of separating
ideas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="rst_cheat_sheet#contributing-line-break"><span class="std std-ref">RST cheat sheet: Break the line but not the paragraph</span></a></p></li>
</ul>
</div>

### Titles and headings

To write good titles and headings:

  * **Be concise.**

    * **Avoid sentences** , unnecessary verbs, questions, and titles starting with «how to.»

  * **Don’t use pronouns** in your titles, especially 2nd person (_your_).

  * Use **sentence case**. This means you capitalize only:

    * the first word of the title or heading

    * the first word after a colon

    * proper nouns (brands, product and service names, etc.)

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Most titles and headings generally refer to a concept and do <em>not</em> represent the name of a
feature or a model.</p></li>
<li><p>Do not capitalize the words of an acronym if they don’t entail a proper noun.</p></li>
<li><p>Verbs in headings are fine since they often describe an action.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><ul>
<li><p><b>Titles</b> (H1)</p>
<ul>
<li><p>Quotation templates</p></li>
<li><p>Lead mining</p></li>
<li><p>Resupply from another warehouse</p></li>
<li><p>Synchronize Google Calendar with Konvergo ERP</p></li>
<li><p>Batch payments: SEPA Direct Debit (SDD)</p></li>
<li><p>Digitize vendor bills with optical character recognition (OCR)</p></li>
</ul>
</li>
<li><p><b>Headings</b> (H2, H3)</p>
<ul>
<li><p>Project stages</p></li>
<li><p>Email alias</p></li>
<li><p>Confirm the quotation</p></li>
<li><p>Generate SEPA Direct Debit XML files to submit payments</p></li>
</ul>
</li>
</ul>
</div>

## Document structure

Use different **heading levels** to organize your text by sections and sub-
sections. Your headings are not only displayed in the document but also on the
navigation menu (only the H1) and on the «On this page» sidebar (all H2 to
H6).

**H1: Page title** Your _page title_ gives your reader a quick and clear
understanding of what your content is about. The _content_ in this section
describes the upcoming content from a **business point of view** , and
shouldn’t put the emphasis on Konvergo ERP, as this is documentation and not
marketing. Start first with a **lead paragraph** , which helps the reader make
sure that they’ve found the right page, then explain the **business aspects of
this topic** in the following paragraphs.  
---  
|  **H2: Section title (configuration)** This first H2 section is about the
configuration of the feature, or the prerequisites to achieve a specific goal.
To add a path, make sure you use the `:menuselection:` specialized directive
(see link below). Example: To do so, go to `:menuselection:`App name --> Menu
--> Sub-menu``, and enable the XYZ feature.  
|  **H2: Section title (main sections)** Create as many main sections as you
have actions or features to distinguish. The title can start with a verb, but
try to avoid using «Create …».  
|  |  **H3: Subsection** Subsections are perfect for assessing very specific points. The title can be in the form of a question, if appropriate.  
| **H2: Next Section**  
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="rst_cheat_sheet#contributing-headings"><span class="std std-ref">RST cheat sheet: headings</span></a></p></li>
<li><p><a href="rst_cheat_sheet#contributing-markups"><span class="std std-ref">RST cheat sheet: markups</span></a></p></li>
</ul>
</div>

## Organizing the documentation

When writing documentation about a given topic, try to keep pages within the
same folder organized.

For most topics, a single page should do the job. Place it in the appropriate
section of the documentation (e.g., content related to the CRM app go under
Applications -> Sales -> CRM) and follow the document structure guidelines.

For more complex topics, you may need several pages to cover all their
aspects. Usually, you will find yourself adding documentation to a topic that
is already partially covered. In that case, either create a new page and place
it at the same level as other related pages or add new sections to an existing
page. If you are documenting a complex topic from scratch, organize your
content between one parent page (the TOC page) and several child pages.
Whenever possible, write content on the parent page and not only on the child
pages. Make the parent page accessible from the navigation menu by using the
[show-content](rst_cheat_sheet#contributing-document-metadata) metadata
directive.

## Images

Adding a few images to illustrate your text helps the readers to understand
and memorize your content. However, avoid adding too many images: it isn’t
necessary to illustrate all steps and features, and it may overload your page.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Don’t forget to <a href="../documentation#contributing-documentation-first-contribution"><span class="std std-ref">compress your PNG files with pngquant</span></a>.</p>
</div>

### Screenshots

Screenshots are automatically resized to fit the content block’s width. This
implies that screenshots can’t be too wide, else they would appear very small
on-screen. Therefore, we recommend to avoid to take screenshots of a full
screen display of the app, unless it is relevant to do so.

A few tips to improve your screenshots:

  1. **Zoom** in your browser. We recommend a 110% zoom for better results.

  2. **Resize** your browser’s width, either by _resizing the window_ itself or by opening the _browser’s developer tools_ (press the `F12` key) and resizing the width.

  3. **Select** the relevant area, rather than keeping the full window.

  4. If necessary, you can **edit** the screenshot to remove unnecessary fields and to narrow even more Konvergo ERP’s display.

![Three tips to take good screenshots for the Konvergo ERP
documentation.](../../_images/screenshot-tips.gif) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Resizing the window’s width is the most important step to do as Konvergo ERP’s responsive design
automatically resizes all fields to match the window’s width.</p>
</div>

### Media files

A **media filename** :

  * is written in **lower-case letters**

  * is **relevant** to the media’s content. (E.g., `screenshot-tips.gif`.)

  * separates its words with a **hyphen** `-` (E.g., `awesome-filename.png`.)

Each document has its own folder in which the media files are located. The
folder’s name must be the same as the document’s filename.

For example, the document `doc_filename.rst` refers to two images that are
placed in the folder `doc_filename`.

    
    
    ├── section
    │   └── doc_filename
    │   │   └── screenshot-tips.gif
    │   │   └── awesome-filename.png
    │   └── doc_filename.rst
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Previously, image filenames would mostly be named with numbers (e.g., <code>feature01.png</code>) and
placed in a single <code>media</code> folder. While it is advised not to name your <em>new</em> images in that
fashion, it is also essential <b>not to rename unchanged files</b>, as doing this would double the
weight of renamed image files on the repository. They will eventually all be replaced as the
content referencing those images is updated.</p>
</div>

### ALT tags

An **ALT tag** is a _text alternative_ to an image. This text is displayed if
the browser fails to render the image. It is also helpful for users who are
visually impaired. Finally, it helps search engines, such as Google, to
understand what the image is about and index it correctly, which improves the
SEO significantly.

Good ALT tags are:

  * **Short** (one line maximum)

  * **Not a repetition** of a previous sentence or title

  * A **good description** of the action happening on the image

  * Easily **understandable** if read aloud

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="rst_cheat_sheet#contributing-image"><span class="std std-ref">RST cheat sheet: image directive</span></a></p></li>
</ul>
</div>

  *[TOC]: Tree Of Contents
  *[SEO]: Search Engine Optimization

