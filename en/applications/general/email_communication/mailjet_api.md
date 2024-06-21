# Mailjet API

Konvergo ERP is compatible with Mailjet’s API for mass mailing. Set up a dedicated
mass mailing server through Mailjet by configuring settings in the Mailjet
account and the Konvergo ERP database. In some circumstances, settings need to be
configured on the custom domain’s DNS settings as well.

## Set up in Mailjet

### Create API credentials

To get started, sign in to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, navigate to the
**Senders & Domains** section and click on **SMTP and SEND API Settings**.

![SMTP and Send API Settings link in the Senders & Domains section of
Mailjet.](../../../_images/api-settings.png)

Then, copy the SMTP configuration settings onto a notepad. They can be found
under the **Configuration (SMTP only)** section. The SMTP configuration
settings include the server address, the security option needed (Use SSL/TLS),
and the port number. The settings are needed to configure Mailjet in Konvergo ERP,
which is covered in the last section.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://documentation.mailjet.com/hc/articles/360043229473">Mailjet: How can I configure my SMTP parameters?</a></p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP blocks <code>port 25</code> on Konvergo ERP Online and Konvergo ERP.sh databases. <a href="email_servers#email-servers-restriction"><span class="std std-ref">See reference here</span></a>.</p>
</div> ![SMTP configuration from
Mailjet.](../../../_images/smtp-config.png)

Next, click on the button labeled **Retrieve your API credentials** to
retrieve the Mailjet API credentials.

Then, click on the eye icon to reveal the **API key**. Copy this key to a
notepad, as this serves as the **Username** in the Konvergo ERP configuration. Next,
click on the **Generate Secret Key** button to generate the **Secret Key**.
Copy this key to a notepad, as this serves as the **Password** in the Konvergo ERP
configuration.

### Add verified sender address(es)

The next step is to add a sender address or a domain to the Mailjet account
settings so that the email address or domain is approved to send emails using
Mailjet’s servers. First, navigate to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, click on the **Add a
Sender Domain or Address** link under the **Senders & Domains** section.

![Add a sender domain or address in the Mailjet
interface.](../../../_images/add-domain-email.png)

Determine if a sender’s email address or the entire domain needs to be added
to the Mailjet settings. It may be easier to configure the domain as a whole
if DNS access is available. Jump to the Add a domain section for steps on
adding the domain.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Either all email addresses of the Konvergo ERP database users who are sending emails using Mailjet’s
servers need to be configured or the domain(s) of the users’ email addresses can be configured.</p>
</div>

By default, the email address originally set up in the Mailjet account is
added as a trusted sender. To add another email address, click on the button
labeled **Add a sender address**. Then, add the email address that is
configured to send from the custom domain.

At minimum the following email addresses should be set up in the provider and
verified in Mailjet:

  * notifications@yourdomain.com

  * bounce@yourdomain.com

  * catchall@yourdomain.com

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Replace <code>yourdomain</code> with the custom domain for the Konvergo ERP database. If there isn’t one, then use
the <b>mail.catchall.domain</b> system parameter.</p>
</div>

After that, fill out the **Email Information** form, making sure to select the
appropriate email type: transactional email or mass emails. After completing
the form, an activation email is sent to the email address and the trusted
sender can be activated.

It is recommended to set up the SPF/DKIM/DMARC settings on the domain of the
sender.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://documentation.mailjet.com/hc/articles/360042412734-Authenticating-Domains-with-SPF-DKIM">Mailjet’s SPF/DKIM/DMARC documentation</a></p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If the database is not using a custom domain, then in order to verify the sender’s address, a
temporary alias (of the three email addresses mentioned above) should be set up in Konvergo ERP CRM to
create a lead. Then, the database is able to receive the verification email and verify the
accounts.</p>
</div>

### Add a domain

By adding an entire domain to the Mailjet account, all the sender addresses
related to that domain are automatically validated for sending emails using
Mailjet servers. First, navigate to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, click on **Add a
Sender Domain or Address** link under the **Senders & Domains** section. Then,
click on **Add domain** to add the custom domain.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The domain needs to be added to the Mailjet account and then validated through the <abbr title="Domain Name System">DNS</abbr>.</p>
</div>

After that, fill out the **Add a new Domain** page on Mailjet and click
**Continue**.

After adding the domain, a validation page will populate. Unless the Konvergo ERP
database is on-premise (in which case, choose **Option 1**), choose **Option
2: Create a DNS Record**. Copy the TXT record information to a notepad and
then navigate to the domain’s DNS provider to complete validation.

![The TXT record information to input on the domain's
DNS.](../../../_images/host-value-dns.png)

#### Setup in the domain’s DNS

After getting the TXT record information from the Mailjet account, add a TXT
record to the domain’s DNS. This process varies depending on the DNS provider.
Consult the provider for specific configuration processes. The TXT record
information consists of the **Host** and **Value**. Paste these into the
corresponding fields in the TXT record.

#### Return to Mailjet account information

After adding the TXT record to the domain’s DNS, navigate back to the Mailjet
account. Then, navigate to Account Information ‣ Add a Sender Domain or
Address, click the gear icon next to **Domain** , and select **Validate**.

This action can also be done by going to the [Sender domains &
addresses](https://app.mailjet.com/account/sender) page on the Mailjet account
information and clicking on **Manage**.

Next, click **Check Now** to validate the TXT record that was added on the
domain. A success screen will appear if the domain is configured correctly.

![Check DNS record in Mailjet.](../../../_images/check-dns.png)

After successfully setting up the domain, there is an option to **Authenticate
this domain (SPF/DKIM)**. This button populates SPF & DKIM provider.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://documentation.mailjet.com/hc/articles/360042412734-Authenticating-Domains-with-SPF-DKIM">Mailjet’s SPF/DKIM/DMARC documentation</a></p>
</div> ![Authenticate the domain with SPF/DKIM records in
Mailjet.](../../../_images/authenticate.png)

## Set up in Konvergo ERP

To complete the setup, navigate to the Konvergo ERP database and go to the
**Settings**. With [Developer mode (debug
mode)](../developer_mode#developer-mode) turned on, go to the Technical
Menu ‣ Email ‣ Outgoing Mail Servers. Then, create a new outgoing server
configuration by clicking on the **Create** button.

Next, input the `SMTP server` (in-v3.mailjet.com), `port number` (587 or 465),
and `Security (SSL/TLS)` that was copied earlier from the Mailjet account.
They can also be found [here](https://app.mailjet.com/account/setup). It is
recommended to use SSL/TLS even though Mailjet may not require it.

For the **Username** , input the **API KEY**. For the **Password** , input the
**SECRET KEY** that was copied from the Mailjet account to the notepad
earlier. These settings can be found on Mailjet ‣ Account Settings ‣ SMTP and
SEND API Settings.

Then, if the Mailjet server is used for mass emailing, set the **Priority**
value higher than that of any transactional email server(s). Finally, save the
settings and **Test the Connection**.

![Konvergo ERP outgoing email server settings.](../../../_images/server-settings.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In order for the notifications feature to work using Mailjet, there are three settings that need
to be set in Konvergo ERP.</p>
<ol class="arabic simple">
<li><p>The <b>From Filter</b> needs to be set on the server configuration. It is recommended
to set it as a domain and not a full email address. It should match the domain in the two
proceeding steps. More information can be referenced <a href="email_servers#email-communication-from-filter"><span class="std std-ref">here</span></a>.</p></li>
<li><p>The <b>mail.default.from</b> system parameter must have the value
<code>notifications@yourdomain.com</code>.</p></li>
<li><p>The <b>mail.default.from_filter</b> system parameter must have the value
<code>yourdomain.com</code>. Replace <code>yourdomain</code> with the custom domain for the Konvergo ERP database. If there
isn’t one, then use the <b>mail.catchall.domain</b> system parameter.</p></li>
</ol>
<p>For more information see <a href="email_servers#email-communication-default"><span class="std std-ref">Using a default email address</span></a>.</p>
<p>The <b>System Parameters</b> can be accessed by activating the <a href="../developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>.</p>
</div>

Once the setup is complete, the Konvergo ERP database is ready to use the Mailjet
email server for mass mailing or transactional emails!

  *[API]: Application Programming Interface
  *[DNS]: Domain Name System
  *[SMTP]: Simple Mail Transfer Protocol
  *[SSL]: Secure Sockets Layer
  *[TLS]: Transport Layer Security
  *[SPF]: Sender Policy Framework
  *[DKIM]: DomainKeys Identified Mail) records to input into the :abbr:`DNS (Domain Name System
  *[DMARC]: Domain-based Message Authentication, Reporting, and Conformance

