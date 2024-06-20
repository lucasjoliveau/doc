# Passerelle de messagerie

La passerelle de messagerie Odoo vous permet d’injecter directement tous les
emails reçus dans Odoo.

Son principe est simple : votre serveur SMTP exécute le script « mailgate »
pour chaque nouvel email entrant.

Le script se charge de se connecter à votre base de données Odoo via XML-RPC,
et d’envoyer les emails via la fonction `MailThread.message_process()`.

## Conditions préalables

  * Accès administrateur à la base de données Odoo.

  * Votre propre serveur de messagerie tel que Postfix ou Exim.

  * Connaissances techniques sur la façon de configurer un serveur de messagerie.

## Pour Postfix

Dans votre configuration d’alias (`/etc/aliases`) :

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

Note

Ressources

  * [Postfix](http://www.postfix.org/documentation.html)

  * [Alias Postfix](http://www.postfix.org/aliases.5.html)

  * [Postfix virtuel](http://www.postfix.org/virtual.8.html)

## Pour Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

Note

Ressources

  * [Exim](https://www.exim.org/docs.html)

Astuce

Si vous n’avez pas accès/ne gérez pas votre serveur de messagerie, utilisez
[messages
entrants](../../applications/general/email_communication/email_servers.html#email-
communication-inbound-messages).

