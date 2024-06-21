# Search Engine Optimization (SEO)

Search Engine Optimization, often abbreviated as SEO, is a digital marketing
strategy to improve a website’s visibility and ranking in search engine
results (e.g., in Google). It involves optimizing various elements on your
website, including its content, social sharing, URLs, images, and page speed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Konvergo ERP provides several modules to help you build your website content, such as
<a href="../../ecommerce">eCommerce</a>, <a href="../../blog">Blog</a>, <a href="../../elearning">eLearning</a>, and <a href="../../forum">Forum</a>.</p></li>
<li><p>All Konvergo ERP themes rely on the CSS Framework <a href="https://getbootstrap.com/">Bootstrap</a> to render
efficiently according to the device: desktop, tablet, or mobile, which positively impacts
ranking in search engines.</p></li>
</ul>
</div>

## Content optimization

To optimize a webpage’s SEO, access the page, then go to Website ‣ Site ‣
Optimize SEO.

![Optimize SEO](../../../../_images/optimize-seo.png)

### Meta tags

Meta tags are HTML elements that provide information about a webpage to search
engines and website visitors. They play a crucial role in SEO by helping
search engines understand the content and context of a webpage and attract
visitors with appealing content. There are two types of meta tags in Konvergo ERP:

  * **Title** tags specify a webpage’s title and are displayed as a clickable link in search engine results. They should be concise, descriptive, and relevant to the page’s content. You can update the title tag of your webpage or keep it empty to use the default value based on the page’s content.

  * **Description** tags summarize the webpage’s content, often displayed in search engine results below the title. They are used to encourage the user to visit the page. You can update the description tag of your webpage or keep it empty to use the default value based on the page’s content.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Preview</b> card displays how the title and description tags should appear in search
results. It also includes the URL of your page.</p>
</div>

### Keywords

Keywords are one of the main elements of SEO. A website that is well optimized
for search engines speaks the same language as potential visitors, with
keywords for SEO helping them to connect to your site.

You can enter the keywords you consider essential in the **Keyword** field and
click **ADD** to see how they are used at different levels in your content
(H1, H2, page title, page description, page content) and the related searches
in Google. The tool also suggests relevant keywords to drive your web traffic.
The more keywords are present on your webpage, the better.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It is strongly recommended to only use one H1 title per page for SEO.</p>
</div>

### Image for social share

When you share your page on social media, your logo image is selected, but you
can upload any other image by clicking the upward arrow.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The <b>Social Preview</b> card displays how the page’s information would appear when
shared.</p></li>
<li><p>If you change the title of a blog post or the name of a product, the changes apply
automatically everywhere on your website. The old link still functions when external websites
use a <a href="../pages#website-url-redirection"><span class="std std-ref">301 redirect</span></a>, maintaining the SEO link juice.</p></li>
</ul>
</div>

## Images

The size of images has a significant impact on page speed, which is an
essential criterion for search engines to optimize SEO ranking.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Compare how your website ranks using <a href="https://pagespeed.web.dev/?utm_source=psi&amp;utm_medium=redirect">Google Page Speed</a>
or <a href="https://tools.pingdom.com/">Pingdom Website Speed Test</a>.</p>
</div>

Konvergo ERP automatically compresses uploaded images to reduce their weight and
improve the page loading speed. All images used in Konvergo ERP official themes are
also compressed by default. If you are using a third-party theme, it may
provide images that are not compressed efficiently.

**To modify an image** from your website, select the image, click **Edit** ,
then go to the **Customize** tab, and adapt the **width** in the **Image**
section.

![automated image compression](../../../../_images/image-width.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Alt tags are used to provide context to what an image is displaying, informing search engine
crawlers and allowing them to index an image correctly. Adding alt tags keywords in the
<b>Description</b> field is essential from an SEO perspective. This description is added to
the HTML code of your image, and it is shown when the image cannot be displayed.</p>
</div>

## Advanced features

### Structured data markup

Structured data markup is used to generate rich snippets in search engine
results. It is a way for websites to send structured data to search engine
robots, helping them understand your content and create well-presented search
results.

By default, Google supports many [rich
snippets](https://developers.google.com/search/blog/2009/05/introducing-rich-
snippets) for content types, including Reviews, People, Products, Businesses,
Events, and Organizations.

Microdata is a set of tags, introduced with HTML5, that help search engines
better understand your content and display it in a relevant way. Konvergo ERP
implements microdata as defined in the schema.org
[specification](https://schema.org/docs/gs) for events, eCommerce
products, forum posts, and contact addresses. This allows your product pages
to be displayed in Google using extra information like the price and rating of
a product:

![snippets in search engine results](../../../../_images/data-markup.png)

### robots.txt

A robots.txt file tells search engine crawlers which URLs the crawler can
access on your site, to index its content. This is used mainly to avoid
overloading your site with requests.

When indexing your website, search engines take a first look at the robots.txt
file. Konvergo ERP automatically creates one robot.txt file available on
`mydatabase.odoo.com/robots.txt`.

By editing a robots.txt file, you can control which site pages are accessible
to search engine crawlers. To add custom instructions to the file, go to
Website ‣ Configuration ‣ Settings, scroll down to the **SEO** section, and
click **Edit robots.txt**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>If you do not want the robots to crawl the <code>/about-us</code> page of your site, you can edit the
robots.txt file to add <code>Disallow: /about-us</code>.</p>
</div>

### Sitemap

The sitemap points out website pages and their relation to each other to
search engine robots. Konvergo ERP generates a `/sitemap.xml` file, including all
URLs. For performance reasons, this file is cached and updated every 12 hours.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If your website has a lot of pages, Konvergo ERP automatically creates a Sitemap Index file, respecting
the <a href="http://www.sitemaps.org/protocol">sitemaps.org protocol</a>, grouping sitemap URLs in
45000 chunks per file.</p>
</div>

Every sitemap entry has three attributes that are computed automatically:

  * `<loc>`: the URL of a page.

  * `<lastmod>`: last modification date of the resource, computed automatically based on the related object. For a page related to a product, this could be the last modification date of the product or the page.

  * `<priority>`: modules may implement their priority algorithm based on their content (for example, a forum might assign a priority based on the number of votes on a specific post). The priority of a static page is defined by its priority field, which is normalized (16 is the default).

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To prevent pages from appearing in a sitemap, go to Site ‣ Properties, click
the <b>Publish</b> tab, and turn off the <b>Indexed</b> feature.</p>
<blockquote>
<div><img alt="disabling the “Indexed” checkbox" src="../../../../_images/page-properties.png"/>
</div></blockquote>
</div>

### Hreflang HTML tags

Konvergo ERP automatically includes `hreflang` and `x-default` tags in the code of
your website’s multilingual pages. These HTML attributes are crucial in
informing search engines about a specific page’s language and geographical
targeting.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../configuration/translate">Translations</a></p>
</div>

