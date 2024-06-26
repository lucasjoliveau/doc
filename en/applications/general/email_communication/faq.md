# Email issues

This document contains an explanation of the most recurring emailing issues in
Konvergo ERP.

## Outgoing emails

### Email is not sent

The first indicator showing that an email has not been sent is the presence of
a red **✉️ (envelope)** icon, next to the date and time of the message,
located in the chatter.

![Red envelope icon displayed in chatter.](../../../_images/red-envelop.png)

Unsent emails also appear in the Konvergo ERP email queue. In [developer
mode](../developer_mode#developer-mode), the email queue can be accessed
by going to Settings app ‣ Technical menu ‣ Email ‣ Emails. Unsent emails
appear in turquoise, while sent emails appear in grey.

#### Common error messages

##### Daily limit reached

![Warning in Konvergo ERP upon email limit reached.](../../../_images/email-limit.png)

Each email service provider has its own email sending limits. The limits may
be daily, hourly, or sometimes, per minute. This is the same for Konvergo ERP, which
limits a customer’s sending to prevent Konvergo ERP’s email servers from being
blacklisted.

Here are the default limits for new databases:

  * **200 emails per day** for Konvergo ERP Online and Konvergo ERP.sh databases with an active subscription.

  * **20 emails per day** for one-app free databases.

  * **50 emails per day** for trial databases.

  * In the case of migration, the daily limit might be reset to 50 emails per day.

If the daily limit is reached:

  * Contact the Konvergo ERP support team, who may increase the daily limit depending on the following factors:

    1. How many users are in the database?

    2. Which apps are installed?

    3. The bounce rate: the percentage of email addresses that did not receive emails because they were returned by a mail server on its way to the final recipient.

  * Use an external outgoing email server to be independent of Konvergo ERP’s mail limit (refer to the corresponding [email documentation](email_servers)).

  * Wait until 11 PM (UTC) for the daily limit to reset, and retry sending the email. In [developer mode](../developer_mode#developer-mode), go to Settings app ‣ Technical menu ‣ Email ‣ Emails, then click the **Retry** button next to an unsent email.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The daily email limit is comprehensive to the database. By default, any internal message,
notification, logged note, etc. counts as an email in the daily limit if it notifies someone via
email. This can be mitigated by receiving <a href="../../productivity/discuss#discuss-app-notification-preferences"><span class="std std-ref">notifications in Konvergo ERP</span></a>, instead of emails.</p>
</div>

##### SMTP error

Simple Mail Transport Protocol (SMTP) error messages explain why an email
wasn’t transmitted successfully. SMTP is a protocol to describe the email
structure, and transmits data from messages over the Internet. The error
messages generated by email services are helpful tools to diagnose and
troubleshoot email problems.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>This is an example of a 554 SMTP permanent delivery error: <code>554: delivery error: Sorry, your
message to ------@yahoo.com cannot be delivered. This mailbox is disabled (554.30). -
mta4471.mail.bf1.yahoo.com --- Below this line is a copy of the message.</code></p>
</div>

The debug menu can be used to investigate SMTP sending issues from a database.
To access the menu, [developer mode](../developer_mode#developer-mode)
must be activated. Once activated, navigate to the Debug Menu in the top right
of the menu bar (the **🐞 (bug)** icon), Debug Menu ‣ Manage Messages

The **Manage Messages** menu opens a list of all the messages sent in a
particular record. Within each message there is information on sending,
including the type, and subtype, of the message.

Other information includes to whom the message was sent, and whether Konvergo ERP
received a bounce-back message from an email server.

![Manage messages menu option on the debug menu.](../../../_images/manage-
messages.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>A user must be on a view in Konvergo ERP that has a chatter in order for the <b>Manage Messages</b>
menu option to appear.</p>
</div>

###### No error populated

Konvergo ERP is not always capable of providing information for the reason it failed.
The different email providers implement a personalized policy of bounced
emails, and it is not always possible for Konvergo ERP to interpret it correctly.

If this is a recurring problem with the same client, or the same domain, do
not hesitate to contact [Konvergo ERP Support](https://www.odoo.com/help) for help in
finding a reason.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>One of the most common reasons for an email failing to send with no error message is related to
<a href="email_domain#email-communication-spf-compliant"><span class="std std-ref">SPF</span></a> and/or <a href="email_domain#email-communication-dkim-compliant"><span class="std std-ref">DKIM</span></a> configuration. Also, check to make sure the
<code>mail.bounce.alias</code> is defined in the <em>system parameters</em>. Access system parameters in
<a href="../developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> by navigating to Settings app ‣
Technical menu ‣ Parameters ‣ System Parameters.</p>
</div>

### Email is sent late

Email campaigns send at a scheduled time, using a delay pre-programed in the
database. Konvergo ERP uses a delayed task to send emails that are considered “not
urgent” (newsletter formats, such as: mass mailing, marketing automation, and
events). The system utility **cron** can be used to schedule programs to run
automatically at predetermined intervals. Konvergo ERP uses that policy in order to
avoid cluttering the mail servers and, instead, prioritizes individual
communication. This **cron** is called **Mail: Email Queue Manager** , and can
be accessed in [developer mode](../developer_mode#developer-mode) by
going to Settings app ‣ Technical menu ‣ Automation ‣ Scheduled Actions.

![Email scheduled to be sent later.](../../../_images/email-scheduled-
later.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>What is a <b>cron</b>? A cron is an action that Konvergo ERP runs in the background to execute particular
code to complete a task.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>By default, the <em>Mass Mailing cron</em> runs every 60 minutes. This can be changed to no less than 5
minutes. However, running the action every 5 minutes would bog down the Konvergo ERP database (stress the
system), so this is not recommended. To edit the mass mailing cron, select the scheduled action
<b>Mail: Email Queue Manager</b>, and proceed to make any necessary adjustments.</p>
</div>

Emails that are considered urgent (communication from one person to another,
such as sales orders, invoices, purchase orders, etc.) are sent immediately.

## Incoming emails

When there is an issue with incoming emails, there might not be an indication,
per se, in Konvergo ERP. It is the sending email client, who tries to contact a
database, that will get a bounce-back message (most of the time a **550:
mailbox unavailable** error message).

### Email is not received

The steps that should be taken depend on the Konvergo ERP platform where the database
is hosted.

**Konvergo ERP.sh** users can find their live logs on the folder `~/logs/`.

Logs are a stored collection of all the tasks completed in a database. They
are a text-only representation, complete with timestamps of every action taken
on the Konvergo ERP database. This can be helpful to track emails leaving the
database. Failure to send can also be seen by logs that indicate that the
message tried to send repeatedly. Logs will show every action to the email
servers from the database.

The folder `~/logs/` (accessed by the command line or on the Konvergo ERP.sh
dashboard) of an Konvergo ERP.sh database contains a list of files containing the logs
of the database. The log files are created everyday at 5:00 AM (UTC).

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>The two most recent days (today and yesterday) are not compressed, while the older ones are, in
order to save space. The naming of the files for today and yesterday are respectively:
<code>odoo.log</code> and <code>odoo.log.1</code>.</p>
<p>For the following days, they are named with their dates, and then compressed. Use the command
<b class="command o_code">grep</b> and <b class="command o_code">zgrep</b> (for the compressed ones) to search through the files.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For more information on logs and how to access them via the Konvergo ERP.sh dashboard, see <a href="../../../administration/odoo_sh/getting_started/branches#odoosh-logs"><span class="std std-ref">this
administration documentation</span></a>.</p>
<p>For more information on accessing logs via the command line visit <a href="../../../developer/reference/cli#reference-cmdline-server-logging"><span class="std std-ref">this developer
documentation</span></a>.</p>
</div>

**Konvergo ERP Online** users won’t have access to the logs. However [Konvergo ERP
Support](https://www.odoo.com/help) can be contacted if there is a recurring
issue with the same client or domain.

## Get help from Konvergo ERP support

In order to get helped efficiently, please provide as much information as
possible. Here is a list of what can be helpful when reaching out to the Konvergo ERP
Support team about an issue:

  1. Send a copy of the email headers. The `.EML` file (or **headers**) of the email is the file format containing all the technical information required for an investigation. The documentation from the email provider might explain how to access the EML file/header files. Once the headers of the email are obtained, adding it into the Konvergo ERP Support ticket is the most efficient way for the Konvergo ERP Support team to investigate.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://support.google.com/mail/answer/29436">Gmail documentation on headers</a></p></li>
<li><p><a href="https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c#tab=Web">Outlook documentation on headers</a></p></li>
</ul>
</div>

  2. Explain the exact flow that is being followed to normally receive those emails in Konvergo ERP. Here are examples of questions whose answers can be useful:

     * Is this a notification message from a reply being received in Konvergo ERP?

     * Is this a message being sent from the Konvergo ERP database?

     * Is there an incoming email server being used, or is the email somehow being redirected?

     * Is there an example of an email that has been correctly forwarded?

  3. Provide answers to the following questions:

     * Is it a generic issue, or is it specific to a use case? If specific to a use case, which one exactly?

     * Is it working as expected? In case the email is sent using Konvergo ERP, the bounce email should reach the Konvergo ERP database, and display the red envelope.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The bounce system parameter needs to be set in the technical settings in order for the database
to correctly receive bounce messages. To access this setting, go to Settings app
‣ Technical menu ‣ Parameters ‣ System Parameters. Then select the parameter name
<b>mail.bounce.alias</b> and set the value to <code>bounce</code> if it isn’t already set.</p>
</div>

  *[SMTP]: Simple Mail Transport Protocol

