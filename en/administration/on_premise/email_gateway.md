# Email gateway

The Odoo mail gateway allows you to inject directly all the received emails in
Odoo.

Its principle is straightforward: your SMTP server executes the “mailgate”
script for every new incoming email.

The script takes care of connecting to your Odoo database through XML-RPC, and
send the emails via the `MailThread.message_process()` feature.

## Prerequisites

  * Administrator access to the Odoo database.

  * Your own mail server such as Postfix or Exim.

  * Technical knowledge on how to configure an email server.

## For Postfix

In you alias config (`/etc/aliases`):

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

Note

Resources

  * [Postfix](http://www.postfix.org/documentation.html)

  * [Postfix aliases](http://www.postfix.org/aliases.5.html)

  * [Postfix virtual](http://www.postfix.org/virtual.8.html)

## For Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

Note

Resources

  * [Exim](https://www.exim.org/docs.html)

Tip

If you don’t have access/manage your email server, use [inbound
messages](../../applications/general/email_communication/email_servers.html#email-
communication-inbound-messages).

