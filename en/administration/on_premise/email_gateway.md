# Email gateway

The Konvergo ERP mail gateway allows you to inject directly all the received emails in
Konvergo ERP.

Its principle is straightforward: your SMTP server executes the “mailgate”
script for every new incoming email.

The script takes care of connecting to your Konvergo ERP database through XML-RPC, and
send the emails via the `MailThread.message_process()` feature.

## Prerequisites

  * Administrator access to the Konvergo ERP database.

  * Your own mail server such as Postfix or Exim.

  * Technical knowledge on how to configure an email server.

## For Postfix

In you alias config (`/etc/aliases`):

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Resources</p>
<ul>
<li><p><a href="http://www.postfix.org/documentation">Postfix</a></p></li>
<li><p><a href="http://www.postfix.org/aliases.5">Postfix aliases</a></p></li>
<li><p><a href="http://www.postfix.org/virtual.8">Postfix virtual</a></p></li>
</ul>
</div>

## For Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Resources</p>
<ul>
<li><p><a href="https://www.exim.org/docs">Exim</a></p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you don’t have access/manage your email server, use <a href="../../applications/general/email_communication/email_servers#email-communication-inbound-messages"><span class="std std-ref">inbound messages</span></a>.</p>
</div>

