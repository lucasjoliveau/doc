# Puerta de enlace del correo electrónico

La puerta de enlace del correo electrónico le permite inyectar directamente
todos los correos recibidos en Odoo.

El principio es directo: su servidor SMTP ejecuta el script «mailgate» para
cada correo entrante.

El script se encarga de conectarlo con la base de datos de Odoo a través de
XML-RPC y enviar correos a través de la función
`MailThread.message_process()`.

## Prerrequisitos

  * Acceso de administrador a la base de datos de Odoo.

  * Su propio servidor de correo como Postfix o Exim.

  * El conocimiento técnico sobre cómo configurar un servidor de correo.

## Para Postfix

En su configuración de alias (`/etc/aliases`):

    
    
    email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
    

Nota

Recursos

  * [Postfix](http://www.postfix.org/documentation.html)

  * [Alias Postfix](http://www.postfix.org/aliases.5.html)

  * [Postfix virtual](http://www.postfix.org/virtual.8.html)

## Para Exim

    
    
    *: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
    

Nota

Recursos

  * [Exim](https://www.exim.org/docs.html)

Truco

Si no tiene acceso/no puede gestionar su servidor de correo, use [imensajes
entrantes](../../applications/general/email_communication/email_servers.html#email-
communication-inbound-messages).

