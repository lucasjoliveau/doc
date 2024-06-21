# Noms de domaine

Domain names are text-based addresses identifying online locations, such as
websites. They provide a more memorable and recognizable way for people to
navigate the internet than numerical IP addresses.

**Konvergo ERP Online** and **Konvergo ERP.sh** databases use a **subdomain** of the
`odoo.com` **domain** by default (e.g., `mycompany.odoo.com`).

However, you can use a custom domain name instead by registering a free domain
name (only available for Konvergo ERP Online databases) or by configuring a domain
name you already own.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odoo.com/slides/slide/register-a-free-domain-name-1663">Konvergo ERP Tutorials: Register a free domain name [video]</a></p>
</div>

## Enregistrer un nom de domaine gratuit avec Konvergo ERP

To register a one-year free domain name for your Konvergo ERP Online database, sign in
to your account and go to the [database
manager](https://www.odoo.com/my/databases). Click the gear icon (**⚙️**) next
to the database name and select **Domain Names**.

![Accessing a database's domain names
configuration](../../../../_images/domain-names.png)

Search for the desired domain name and check its availability.

![Searching for an available domain name](../../../../_images/domain-
search.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>

Select the desired domain name, fill in the **Domain Owner** form, and click
**Register**. The chosen domain name is directly linked to the database.

![Filling in the domain owner information](../../../../_images/domain-
owner.png)

Next, you should map your domain name to your Konvergo ERP website.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A verification email from <code>noreply@domainnameverification.net</code> will be sent to the email address
provided in the <b>Domain Owner</b> form. It is essential to verify your email address to
keep the domain active and receive the renewal quote before expiration.</p>
</div>

The domain name registration is free for the first year. After this period,
Konvergo ERP will continue to manage the domain in partnership with **Gandi.net** ,
the domain name registrar, and you will be charged [Gandi.net’s renewal
rate](https://www.gandi.net/en/domain). Konvergo ERP sends a renewal quotation every
year to the email address mentioned in the **Domain Owner** form several weeks
before the expiration date of the domain. The domain is renewed automatically
when the quotation is confirmed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The offer is only available for <b>Konvergo ERP Online</b> databases.</p></li>
<li><p>The offer is limited to <b>one</b> domain name per client.</p></li>
<li><p>The offer is limited to the registration of a <b>new</b> domain name.</p></li>
<li><p>The offer is available to <em>One App Free</em> plans. Ensure that your website contains enough
original content for Konvergo ERP to verify that your request is legitimate and respects <a href="https://www.odoo.com/acceptable-use">Konvergo ERP’s
Acceptable Use Policy</a>. Given the high number of
requests, it can take Konvergo ERP several days to review them.</p></li>
</ul>
</div>

### DNS records

To manage your free domain name DNS records, open the [database
manager](https://www.odoo.com/my/databases), click the gear icon (**⚙️**) next
to the database name, select **Domain Names** , and click **DNS**.

  * **A** : the A record holds the IP address of the domain. It is automatically created and **cannot** be edited or deleted.

  * **CNAME** : CNAME records forward one domain or subdomain to another domain. One is automatically created to map the `www.` subdomain to the database. If the database is renamed, the CNAME record **must** also be renamed.

  * **MX** : MX records instruct servers on where to deliver emails.

  * **TXT** : TXT records can be used for different purposes (e.g., to verify domain name ownership).

Any modification to the DNS records can take up to **72 hours** to propagate
worldwide on all servers.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="https://www.odoo.com/help">Submit a support ticket</a> if you need assistance to manage your
domain name.</p>
</div>

### Mailbox

The one-year free domain name offer does **not** include a mailbox. There are
two options to link your domain name with a mailbox.

#### Use a subdomain

You can create a subdomain (e.g., `subdomain.yourdomain.com`) to use as an
alias domain for the database. It allows users to create records in the
database from emails received on their `email@subdomain.yourdomain.com` alias.

To do so, open the [database manager](https://www.odoo.com/my/databases),
click the gear icon (**⚙️**) next to the database name, and go to Domain Names
‣ DNS ‣ Add DNS record ‣ CNAME. Next, enter the desired subdomain in the
**Name** field (e.g., `subdomain`), the original database domain with a period
at the end (e.g., `mycompany.odoo.com.`) in the **Content** field, and click
**Add record**.

Then, add the alias domain as your _own domain_ by clicking **Use my own
domain** , entering the alias domain (e.g., `subdomain.yourdomain.com`),
clicking **Verify** , and then **I confirm, it’s done**.

Finally, go to your database and open the **Settings**. Enable **Custom Email
Servers** , enter the **Alias Domain** (e.g., `subdomain.yourdomain.com`) and
click **Save**.

#### Use an external email provider

To use an external email provider, you should configure an MX record. To do
so, open the [database manager](https://www.odoo.com/my/databases), click the
gear icon (**⚙️**) next to the database name, click Domain Names ‣ DNS ‣ Add
DNS record ‣ MX. The values you should enter for the **Name** , **Content** ,
and **Priority** fields depend on the external email provider.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://support.google.com/a/answer/174125?hl=en">Google Workspace: MX record values</a></p></li>
<li><p><a href="https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online">Outlook and Exchange Online: Add an MX record for email</a></p></li>
</ul>
</div>

## Configurer un nom de domaine existant

If you already have a domain name, you can use it for your Konvergo ERP website.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>It is strongly recommended to follow <b>in order</b> these three steps to avoid any <a href="#domain-name-ssl"><span class="std std-ref">SSL
certificate validation</span></a> issues:</p>
<ol class="arabic simple">
<li><p><a href="#domain-name-cname"><span class="std std-ref">Add a CNAME record</span></a></p></li>
<li><p><a href="#domain-name-db-map"><span class="std std-ref">Map your domain name to your Konvergo ERP database</span></a></p></li>
<li><p><a href="#domain-name-website-map"><span class="std std-ref">Map your domain name to your Konvergo ERP website</span></a></p></li>
</ol>
</div>

### Ajouter un enregistrement CNAME

Adding a CNAME record to forward your domain name to the address of your Konvergo ERP
database is required.

Konvergo ERP OnlineKonvergo ERP.sh

The CNAME record’s target address should be your database’s address as defined
at its creation (e.g., `mycompany.odoo.com`).

The CNAME record’s target address should be the project’s main address, which
can be found on Konvergo ERP.sh by going to Settings ‣ Project Name, or a specific
branch (production, staging or development) by going to Branches ‣ select the
branch ‣ Settings ‣ Custom domains, and clicking **How to set up my domain?**.
A message indicates which address your CNAME record should target.

The specific instructions depend on your DNS hosting service.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.godaddy.com/help/add-a-cname-record-19236">GoDaddy: Add a CNAME record</a></p></li>
<li><p><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain">Namecheap: How to create a CNAME record for your domain</a></p></li>
<li><p><a href="https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record">OVHcloud: Add a new DNS record</a></p></li>
<li><p><a href="https://support.cloudflare.com/hc/en-us/articles/360019093151">Cloudflare: Manage DNS records</a></p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP only supports subdomains. To use your naked domain name <span class="dfn"><span>(a domain name without any
subdomains or prefixes)</span></span> (<code>yourdomain.com</code>), create a redirection 301 to redirect visitors to
<code>www.yourdomain.com</code>.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>You own the domain name <code>yourdomain.com</code>, and your Konvergo ERP Online database’s address is
<code>mycompany.odoo.com</code>. You want to access your Konvergo ERP database primarily with the domain
<code>www.yourdomain.com</code> and also with the naked domain <code>yourdomain.com</code>.</p>
<p>To do so, create a CNAME record for the <code>www</code> subdomain, with <code>mycompany.odoo.com</code> as the target.
Next, create a redirect (301 permanent or visible redirect) to redirect visitors from
<code>yourdomain.com</code> to <code>wwww.yourdomain.com</code>.</p>
</div>

### Map a domain name to an Konvergo ERP database

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>0

Konvergo ERP OnlineKonvergo ERP.sh

Open the [database manager](https://www.odoo.com/my/databases), click the gear
icon (**⚙️**) next to the database name, and go to Domain Names ‣ Use my own
domain. Then, enter the domain name (e.g., `yourdomain.com`), click **Verify**
and **I confirm, it’s done**.

![Mapping a domain name to an Konvergo ERP Online database](../../../../_images/map-
database-online.png)

On Konvergo ERP.sh, go to Branches ‣ select your branch ‣ Settings ‣ Custom domains,
type the domain name to add, then click **Add domain**.

![Mapping a domain name to an Konvergo ERP.sh branch](../../../../_images/map-
database-sh.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>1

#### Chiffrement SSL (protocole HTTPS)

**SSL encryption** allows visitors to navigate a website through a secure
connection, which appears as the _https://_ protocol at the beginning of a web
address rather than the non-secure _http://_ protocol.

Konvergo ERP generates a separate SSL certificate for each domain mapped to a database
using [Let’s Encrypt’s certificate authority and ACME
protocol](https://letsencrypt.org/how-it-works/).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>2 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>3

#### URL de base web d’une base de données

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>4

The _web base URL_ or root URL of a database affects your main website address
and all the links sent to your customers (e.g., quotations, portal links,
etc.).

To make your custom domain name the _web base URL_ of your database, access
your database using your custom domain name and log in as an administrator (a
user part of the Settings access right group under Administration).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>5 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>6

### Map a domain name to an Konvergo ERP website

Mapping your domain name to your website is different than mapping it to your
database:

  * It defines your domain name as the main one for your website, helping search engines to index your website correctly.

  * It defines your domain name as the base URL for your database, including portal links sent by email to your customers.

  * If you have multiple websites, it maps your domain name to the appropriate website.

Go to Website ‣ Configuration ‣ Settings. If you have multiple websites,
select the one you want to configure. In the **Domain** field, enter the
address of your website (e.g., `https://www.yourdomain.com`) and **Save**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>7 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ensure the Website app is installed if the domain name registration option does not appear.</p>
</div>8

  *[DNS]: domain name system

