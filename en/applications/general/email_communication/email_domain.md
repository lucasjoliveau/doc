# Configure DNS records to send emails in Konvergo ERP

## SPAM labels overview

Sometimes, emails from Konvergo ERP are misclassified by the different email providers
and end up in spam folders. At the moment, some settings are out of Konvergo ERP’s
control, notably the way the different email providers classify Konvergo ERP’s emails
according to their own restriction policy and/or limitations.

It is standard in Konvergo ERP that emails are received from `"name of the author"
<notifications@mycompany.odoo.com>`. In other words this can be translated to:
`"name of the author" <{ICP.mail.from.filter}@{mail.catchall.domain}>`. In
this case ICP stands for `ir.config.parameters`, which are the System
Parameters. Deliverability is greatly improved with the [notifications
configuration](email_servers#email-servers-notifications).

In order for servers to accept emails from Konvergo ERP on a more regular basis, one
of the solutions is for customers to create rules within their own mailbox. A
filter can be added to the email inbox so that when email is received from
Konvergo ERP (`notifications@mycompany.odoo.com`) it is moved to the inbox. It is also
possible to add the Konvergo ERP database domain onto a safe senders list or whitelist
on the receiving domain.

If an Konvergo ERP email server appears on a blacklist, notify Konvergo ERP via a [new help
ticket](https://www.odoo.com/help) and the support team will work to get the
servers removed from the blacklist.

Should the Konvergo ERP database be using a custom domain for sending emails from Konvergo ERP
there are three records that should be implemented on the custom domain’s DNS
to ensure deliverability of email. This includes setting records for SPF, DKIM
and DMARC. Ultimately though, it is up to the discretion of the final
receiving mailbox.

## Be SPF compliant

The Sender Policy Framework (SPF) protocol allows the owner of a domain name
to specify which servers are allowed to send emails from that domain. When a
server receives an incoming email, it checks whether the IP address of the
sending server is on the list of allowed IPs according to the sender’s SPF
record.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <abbr title="Sender Policy Framework">SPF</abbr> verification is performed on the domain mentioned in
the <code>Return-Path</code> field of the email. In the case of an email sent by Konvergo ERP, this domain
corresponds to the value of the <code>mail.catchall.domain</code> key in the database system parameters.</p>
</div>

The SPF policy of a domain is set using a TXT record. The way to create or
modify a TXT record depends on the provider hosting the DNS zone of the domain
name. In order for the verification to work properly, each domain can only
have one SPF record.

If the domain name does not yet have a SPF record, create one using the
following input: `v=spf1 include:_spf.odoo.com ~all`

If the domain name already has a SPF record, the record must be updated (and
do not create a new one).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>If the TXT record is <code>v=spf1 include:_spf.google.com ~all</code>, edit it to add
<code>include:_spf.odoo.com</code>: <code>v=spf1 include:_spf.odoo.com include:_spf.google.com ~all</code></p>
</div>

Check if the SPF record is valid with a free tool like [MXToolbox
SPF](https://mxtoolbox.com/spf.aspx).

## Enable DKIM

The DomainKeys Identified Mail (DKIM) allows a user to authenticate emails
with a digital signature.

When sending an email, the Konvergo ERP server includes a unique DKIM signature in the
headers. The recipient’s server decrypts this signature using the DKIM record
in the database’s domain name. If the signature and the key contained in the
record match, this guarantees that the message is authentic and has not been
altered during transport.

To enable DKIM, add a CNAME record to the DNS zone of the domain name:

`odoo._domainkey IN CNAME odoo._domainkey.odoo.com.`

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If the domain name is <code>mycompany.com</code>, make sure to create a subdomain
<code>odoo._domainkey.mycompany.com</code> whose canonical name is <code>odoo._domainkey.odoo.com.</code>.</p>
</div>

The way to create or modify a CNAME record depends on the provider hosting the
DNS zone of the domain name. The most common providers are listed below.

Check if the DKIM record is valid with a free tool like [DKIM
Core](https://dkimcore.org/tools/). If a selector is asked, enter `odoo`.

## Check the DMARC policy

The Domain-based Message Authentication, Reporting, & Conformance (DMARC)
record is a protocol that unifies SPF and DKIM. The instructions contained in
the DMARC record of a domain name tell the destination server what to do with
an incoming email that fails the SPF and/or DKIM check.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>DMARC: TXT record</p>
<p><code>v=DMARC1; p=none;</code></p>
</div>

There are three DMARC policies:

  * `p=none`

  * `p=quarantine`

  * `p=reject`

`p=quarantine` and `p=reject` instruct the server that receives an email to
quarantine that email or ignore it if the SPF and/or DKIM check fails.

If the domain name uses DMARC and has defined one of these policies, the
domain must be SPF compliant or enable DKIM.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Yahoo or AOL are examples of email providers with a <abbr title="Domain-based Message Authentication, Reporting, &amp; Conformance">DMARC</abbr> policy set to <code>p=reject</code>. Konvergo ERP strongly advises
against using an <em>@yahoo.com</em> or <em>@aol.com</em> address for the database users. These emails will
never reach their recipient.</p>
</div>

`p=none` is used for the domain owner to receive reports about entities using
their domain. It should not impact the deliverability if the DMARC check
fails.

DMARC records are comprised of tags in the form of DNS records. These
tags/parameters allow for reporting, such as RUA and RUF, along with more
precise specification like PCT, P, SP ADKIM & ASPF. For best practice, the the
DMARC policy should not start out being too restrictive.

The following chart displays available tags:

Tag Name | Purpose | Example  
---|---|---  
v | Protocol version | `v=DMARC1`  
pct | Percentage of messages subjected to filtering | `pct=20`  
ruf | Reporting URI for forensic reports | `ruf=mailto:authfail@example.com`  
rua | Reporting URI of aggregate reports | `rua=mailto:aggrep@example.com`  
p | Policy for organizational domain | `p=quarantine`  
sp | Policy for subdomains of the OD | `sp=reject`  
adkim | Alignment mode for DKIM | `adkim=s`  
aspf | Alignment mode for SPF | `aspf=r`  
  
Check the DMARC record of a domain name with a tool like [MXToolbox
DMARC](https://mxtoolbox.com/DMARC.aspx).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://dmarc.org/overview/">DMARC.org is another great resource to learn about DMARC records.</a></p>
</div>

## SPF, DKIM & DMARC documentation of common providers

  * [OVH DNS](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/)

  * [OVH SPF](https://docs.ovh.com/us/en/domains/web_hosting_the_spf_record/)

  * [GoDaddy TXT record](https://www.godaddy.com/help/add-a-txt-record-19232)

  * [GoDaddy SPF](https://www.godaddy.com/help/add-an-spf-record-19218)

  * [GoDaddy DKIM](https://www.godaddy.com/help/add-a-cname-record-19236)

  * [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/)

  * [CloudFlare DNS](https://support.cloudflare.com/hc/en-us/articles/360019093151)

  * [Google Domains](https://support.google.com/domains/answer/3290350?hl=en)

  * [Azure DNS](https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal)

To fully test the configuration, use the [Mail-Tester](https://www.mail-
tester.com/) tool, which gives a full overview of the content and
configuration in one sent email. Mail-Tester can also be used to configure
records for other, lesser-known providers.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://www.mail-tester.com/spf/">Using Mail-Tester to set SPF Records for specific carriers</a></p>
</div>

  *[SPF]: Sender Policy Framework
  *[DKIM]: DomainKeys Identified Mail
  *[DMARC]: Domain-based Message Authentication, Reporting, & Conformance
  *[DNS]: Domain Name System
  *[CNAME]: Canonical Name
  *[RUA]: Reporting URI of aggregate reports
  *[RUF]: Reporting URI for forensic reports
  *[PCT]: Percentage of messages subjected to filtering
  *[P]: Policy for organizational domain
  *[SP]: Policy for subdomains of the OD
  *[ADKIM]: Alignment mode for DKIM
  *[ASPF]: Alignment mode for SPF

