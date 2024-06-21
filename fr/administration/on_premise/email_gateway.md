# Passerelle de messagerie

La passerelle de messagerie Konvergo ERP vous permet d’injecter directement tous les
emails reçus dans Konvergo ERP.

Son principe est simple : votre serveur SMTP exécute le script « mailgate »
pour chaque nouvel email entrant.

Le script se charge de se connecter à votre base de données Konvergo ERP via XML-RPC,
et d’envoyer les emails via la fonction `MailThread.message_process()`.

## Conditions préalables

  * Accès administrateur à la base de données Konvergo ERP.

  * Votre propre serveur de messagerie tel que Postfix ou Exim.

  * Connaissances techniques sur la façon de configurer un serveur de messagerie.

## Pour Postfix

Dans votre configuration d’alias (`/etc/aliases`) :

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ressources</p>
<ul>
<li><p><a href="http://www.postfix.org/documentation">Postfix</a></p></li>
<li><p><a href="http://www.postfix.org/aliases.5">Alias Postfix</a></p></li>
<li><p><a href="http://www.postfix.org/virtual.8">Postfix virtuel</a></p></li>
</ul>
</div>

## Pour Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ressources</p>
<ul>
<li><p><a href="https://www.exim.org/docs">Exim</a></p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous n’avez pas accès/ne gérez pas votre serveur de messagerie, utilisez <a href="../../applications/general/email_communication/email_servers#email-communication-inbound-messages"><span class="std std-ref">messages entrants</span></a>.</p>
</div>

