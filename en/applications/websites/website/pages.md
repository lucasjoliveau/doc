# Pages

Konvergo ERP allows you to create pages for your website and customize their content
and appearance to your needs.

**Static** pages have stable content, such as the homepage. You can manually
create new ones, define their URLs, adapt their properties, etc. **Dynamic**
pages, on the other hand, are generated dynamically. All pages generated
automatically by Konvergo ERP, for example, when you install an app or module (e.g.,
`/shop` or `/blog`) or publish a new product or blog post, are dynamic pages
and are therefore managed differently.

## Page creation

Website pages can be created from the **frontend** and the **backend**. To
create a new website page, proceed as follows:

>   1.      * Either open the **Website** app, click **\+ New** in the top-
> right corner, then select **Page** ;
>
>      * Or go to Website ‣ Site ‣ Pages and click **New**.
>
>   2. Enter a **Page Title** ; this title is used in the menu and the page’s
> URL.
>
>   3. Click **Create**.
>
>   4. Customize the page’s content and appearance using the website builder,
> then click **Save**.
>
>   5. Publish the page.
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Disable <b>Add to menu</b> if the page should not appear in the menu.</p>
</div>

## Page management

### Publishing/unpublishing pages

Pages need to be published to make them accessible to website visitors. To
publish or unpublish a page, access it and toggle the switch in the upper-
right corner from **Unpublished** to **Published** , or vice versa.

![Unpublished/Published toggle](../../../_images/un-published_toggle.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is also possible to:</p>
<blockquote>
<div><ul>
<li><p>publish/unpublish a page from the <a href="#website-page-properties"><span class="std std-ref">page properties</span></a>, where you
can define a publishing date and/or restrict the page’s visibility if needed;</p></li>
<li><p>publish/unpublish several pages at once: go to Website ‣ Site ‣ Pages,
select the pages, then click <b>Action</b> and select <b>Publish</b> or
<b>Unpublish</b>.</p></li>
</ul>
</div></blockquote>
</div>

### Homepage

When you create a website, Konvergo ERP creates a dedicated **Home** page by default,
but you can define any website page as your homepage. To do so, go to Website
‣ Configuration ‣ Settings, then, in the **Website info** section, define the
URL of the desired page in the field **Homepage URL** (e.g., `/shop`).

Alternatively, you can define any static page as your homepage by going to
Website ‣ Site ‣ Properties. Select the **Publish** tab and enable **Use as
Homepage**.

### Page properties

To modify a static page’s properties, access the page you wish to modify, then
go to Site ‣ Properties.

The **Name** tab allows you to:

  * rename the page using the **Page Name** field;

  * modify the **Page URL**. In this case, you can redirect the old URL to the new one if needed. To do so, enable **Redirect Old URL** , then select the **Type** of redirection:

    * **301 Moved permanently** : to redirect the page permanently;

    * **302 Moved temporarily** : to redirect the page temporarily.

![Redirect old URL](../../../_images/page-redirection.png)

You can further adapt the page’s properties in the **Publish** tab:

  * **Show in Top Menu** : Disable if you don’t want the page to appear in the menu;

  * **Use as Homepage** : Enable if you want the page to be the homepage of your website;

  * **Indexed** : Disable if you don’t want the page to be shown in search engine results;

  * **Published** : Enable to publish the page;

  * **Publishing Date** : To publish the page at a specific moment, select the date, click the clock icon to set the time, then click the green check mark to validate your selection.

  * **Visibility** : Select who can access the page:

    * **All**

    * **Signed In**

    * **Restricted Group** : Select the [user access group(s)](../../general/users/access_rights) in the **Authorized group** field.

    * **With Password** : Enter the password in the **Password** field.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><em>Some</em> of these properties can also be modified from Website ‣ Site ‣ Pages.</p>
</div>

#### Duplicating pages

To duplicate a page, access the page, then go to Site ‣ Properties and click
**Duplicate Page**. Enter a **Page Name** , then click **OK**. By default, the
new page is added after the duplicated page in the menu, but you can remove it
from the menu or change its position using the [menu
editor](pages/menus).

#### Deleting pages

To delete a page, proceed as follows:

  1. Access the page, then go to Site ‣ Properties and click **Delete Page**.

  2. A pop-up window appears on the screen with all links referring to the page you want to delete, organized by category. To ensure website visitors don’t land on a 404 error page, you must update all the links on your website referring to the page. To do so, expand a category, then click on a link to open it in a new window. Alternatively, you can set up a redirection for the deleted page.

  3. Once you have updated the links (or set up a redirection), select the **I am sure about this** check box, then click **OK**.

### URL redirect mapping

URL redirect mapping consists in sending visitors and search engines to a URL
different from the one they initially requested. This technique is used, for
example, to prevent broken links when you delete a page, modify its URL, or
migrate your site from another platform to an Konvergo ERP
[domain](configuration/domain_names). It can also be used to improve
[Search Engine Optimization (SEO)](pages/seo).

To access existing URL redirections and create new ones, [activate the
developer mode](../../general/developer_mode) and go to Website ‣
Configuration ‣ Redirects.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>A redirect record is added automatically every time you <a href="#website-page-properties"><span class="std std-ref">modify a page’s URL</span></a> and enable <b>Redirect Old URL</b>.</p></li>
<li><p>You can set up redirections for <a href="#website-page-type"><span class="std std-ref">static and dynamic pages</span></a>.</p></li>
</ul>
</div>

To create a new redirection, click the **New** button, then fill in the
fields:

  * **Name** : Enter a name to identify the redirect.

  * **Action** : Select the type of redirection:

>     * **404 Not found** : visitors are redirected to a 404 error page when
> they try to access an unpublished or deleted page.
>
>     * **301 Moved Permanently** : for permanent redirections of unpublished
> or deleted static pages. The new URL is shown in search engine results, and
> the redirect is cached by browsers.
>
>     * **302 Moved Temporarily** : for short-term redirections, for example,
> if you are redesigning or updating a page. The new URL is neither cached by
> browsers nor shown in search engine results.
>
>     * **308 Redirect/Rewrite** : for permanent redirections of existing
> dynamic pages. The URL is renamed; the new name is shown in search engine
> results and is cached by browsers. Use this redirect type to rename a
> dynamic page, for example, if you wish to rename `/shop` into `/market`.

  * **URL from** : Enter the URL to be redirected (e.g., `/about-the-company`) or search for the desired dynamic page and select it from the list.

  * **URL to** : For 301, 302, and 308 redirects, enter the URL to be redirected to. If you want to redirect to an external URL, include the protocol (e.g., `https://`).

  * **Website** : Select a specific website.

  * **Sequence** : To define the order in which redirections are performed, e.g., in the case of redirect chains (i.e., a series of redirects where one URL is redirected to another one, which is itself further redirected to another URL).

Toggle the **Activate** switch to deactivate the redirection.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>404, 301, and 302 redirections are meant to migrate traffic from
<a href="#website-un-publish-page"><span class="std std-ref">unpublished</span></a> or <a href="#website-delete-page"><span class="std std-ref">deleted</span></a> pages
to <em>new</em> pages, while the 308 redirect is used for <em>permanent</em> redirections of <em>existing</em> pages.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://developers.google.com/search/docs/crawling-indexing/301-redirects">Google documentation on redirects and search</a></p></li>
<li><p><a href="pages/seo">Search Engine Optimization (SEO)</a></p></li>
</ul>
</div>

  * [Menus](pages/menus)
  * [Search Engine Optimization (SEO)](pages/seo)

