# Puerta de enlace del correo electrónico

La puerta de enlace del correo electrónico le permite inyectar directamente
todos los correos recibidos en Konvergo ERP.

El principio es directo: su servidor SMTP ejecuta el script «mailgate» para
cada correo entrante.

El script se encarga de conectarlo con la base de datos de Konvergo ERP a través de
XML-RPC y enviar correos a través de la función
`MailThread.message_process()`.

## Prerrequisitos

  * Acceso de administrador a la base de datos de Konvergo ERP.

  * Su propio servidor de correo como Postfix o Exim.

  * El conocimiento técnico sobre cómo configurar un servidor de correo.

## Para Postfix

En su configuración de alias (`/etc/aliases`):

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Recursos</p>
<ul>
<li><p><a href="http://www.postfix.org/documentation">Postfix</a></p></li>
<li><p><a href="http://www.postfix.org/aliases.5">Alias Postfix</a></p></li>
<li><p><a href="http://www.postfix.org/virtual.8">Postfix virtual</a></p></li>
</ul>
</div>

## Para Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Recursos</p>
<ul>
<li><p><a href="https://www.exim.org/docs">Exim</a></p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si no tiene acceso/no puede gestionar su servidor de correo, use <a href="../../applications/general/email_communication/email_servers#email-communication-inbound-messages"><span class="std std-ref">imensajes entrantes</span></a>.</p>
</div>

