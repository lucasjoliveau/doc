# Configure los registros DNS para enviar correos en Odoo

## Resumen de las etiquetas SPAM

De vez en cuando, los proveedores de correo clasifican mal los correos de Odoo
y los mandan a la carpeta de spam. Por el momento, Odoo no puede controlar
algunos ajustes, sobre todo la forma en la que los proveedores de correo
electrónico clasifican los correos provenientes de Odoo según sus propias
políticas de restricción o sus limitaciones.

En Odoo es estándar recibir correos de `"nombre del autor"
<notifications@mycompany.odoo.com>``, que se puede traducir a `"nombre del
autor" <{ICP.mail.from.filter}@{mail.catchall.domain}>`. En este caso, ICP son
las siglas de `ir.config.parameters`, que son los parámetros del sistema.
Gracias a la [configuración de notificaciones](email_servers.html#email-
servers-notifications) mejoramos las entregas.

Para que sea más fácil que los servidores acepten correos de Odoo, una de las
soluciones es que el cliente cree reglas deontro de su propia bandeja de
entrega. Se puede agregar un filtro a la bandeja de entrada de manera que
cuando se reciba un correo de Odoo (`notifications@mycompany.odoo.com`) este
se mueva a la bandeja de entrada. También es posible agregar el dominio de la
base de datos de Odoo a la lista de remitentes seguros o a la lista blanca del
proveedor de correos.

Si el servidor de correo de Odoo aparece en una lista negra, notifíquenos
mediante un [ticket de soporte nuevo](https://www.odoo.com/help) y el equipo
de soporte técnico trabajará para que el servidor ya no esté en la lista
negra.

Si la base de datos usa un dominio personalizado para enviar correos desde
Odoo, entonces debe implementar tres registros en el DNS del dominio
personalizado para asegurar la entrega del correo. Es necesario que configure
registros para el SPF, DKIM y DMARC. Sin embargo, todo depende del correo que
recibe los mensajes.

## Cumplimiento SPF

El protocolo del Convenio de remitentes (SPF, por sus siglas en inglés)
permite que el dueño del nombre de dominio especifique qué servidores pueden
enviar correos desde ese dominio. Cuando un servidor recibe un correo, revisa
si la dirección IP del servidor saliente está en la lista de IP permitidas
según el registro SPF del remitente.

Nota

La verificación del SPF se realiza en el dominio que aparece en el campo
`Return-Path` del correo electrónico. En caso de que se trate de un correo
electrónico enviado por Odoo, este dominio corresponde al valor de la clave
`mail.catchall.domain` en los parámetros de sistema de la base de datos.

La política SPF de un dominio se establece mediante un registro TXT y la
creación o modificación de un registro TXT depende del proveedor que aloja a
la zona DNS de su nombre de dominio. Para que la verificación funcione de
forma adecuada, cada dominio puede tener solo un registro SPF.

Si el nombre del dominio todavía no tiene un registro SPF, escriba `v=spf1
include:_spf.odoo.com ~all` para crear uno.

Si el nombre de dominio ya tiene un registro SPF, debe actualizar el registro
(no cree uno nuevo).

Example

Si el registro TXT es `v=spf1 include:_spf.google.com ~all`, edítelo para
agregar `include:_spf.odoo.com`: `v=spf1 include:_spf.odoo.com
include:_spf.google.com ~all`

Verifique si el registro SPF es válido con una herramienta gratuita como
[MXToolbox SPF](https://mxtoolbox.com/spf.aspx).

## Habilitar DKIM

El correo identificado con claves de dominio (DKIM, mejor conocido como
DomainKeys Identified Mail) permite que los usuarios autentiquen sus correos
electrónicos con una firma digital.

Al enviar un correo electrónico, el servidor de Odoo incluye una firma DKIM
única en los encabezados. El servidor del destinatario descifra esta firma
mediante el registro DKIM en el nombre de dominio de la base de datos. Si la
firma y la clave en el registro coinciden, confirma que el mensaje es
auténtico y que no se alteró durante el transporte.

Para habilitar el DKIM, agregue un registro CNAME en la zona DNS del nombre de
dominio:

`odoo._domainkey IN CNAME odoo._domainkey.odoo.com.`

Truco

Si el nombre de dominio es `mycompany.com`, asegúrese de crear un subdominio
`odoo._domainkey.mycompany.com` cuyo nombre canónico sea
`odoo._domainkey.odoo.com.`.

La creación o modificación de un registro CNAME depende del proveedor que da
alojamiento a la zona DNS del nombre de dominio. Puede consultar una lista de
los proveedores más comunes aquí.

Verifique si el registro DKIM es válido con una herramienta gratuita como
[DKIM Core](https://dkimcore.org/tools/). Escriba `odoo` en caso de que se le
solicite un selector.

## Verificar la política DMARC

El registro de autenticación basada en dominios para mensajes, reportes y
conformidad (DMARC) es un protocolo que unifica el SPF y el DKIM. Las
instrucciones en el registro DMARC de un nombre de dominio indican al servidor
de destino lo que debe hacer con un correo entrante que no cumple con las
verificaciones del SPF o el DKIM.

Example

DMARC: registro TXT

`v=DMARC1; p=none;`

Hay tres políticas DMARC:

  * `p=none`

  * `p=quarantine`

  * `p=reject`

`p=quarantine` y `p=reject` le indican al servidor que recibe un correo
electrónico que debe ponerlo en cuarentena o ignorarlo si no cumple con las
verificaciones de SPF o DKIM.

Si el nombre de dominio utiliza la DMARC y tiene definida una de estas
políticas, entonces el dominio debe cumplir con el SPF o debe tener activo el
DKIM.

Advertencia

Yahoo y AOL son ejemplos de proveedores de correo electrónico con una política
de DMARC configurada con `p=reject`. Odoo le recomienda que no use direcciones
_@yahoo.com_ o _@aol.com_ para los usuarios de la base de datos, ya que estos
correos nunca llegarán a su destinatario.

El propiertario del dominio utiliza `p=none` para recibir reportes sobre
entidades que utilizan su dominio. No pasar la verificación DMARC no debería
afectar la entrega.

Los registros DMARC están compuestos por etiquetas en forma registros DNS.
Estas etiquetas o parámetros permiten generar reportes, como RUA y RUF, junto
con otras especificaciones más precisas como el PCT, P, SP ADKIM y ASPF. Como
buena práctica, la política DMARC no debe ser demasiado restrictiva desde el
inicio.

La siguiente tabla muestra las etiquetas disponibles:

Nombre de etiqueta | Finalidad | Ejemplo  
---|---|---  
v | Versión de protocolo | `v=DMARC1`  
pct | Porcentaje de mensajes que se someten a filtrado | `pct=20`  
ruf | Reportar un URI para reportes forenses | `ruf=mailto:authfail@example.com`  
rua | Reportar un URI de reportes agregados | `rua=mailto:aggrep@example.com`  
p | Política para el dominio organizacional | `p=quarantine`  
sp | Política para los subdominios del dominio organizacional | `sp=reject`  
adkim | Modo de alineación para DKIM | `adkim=s`  
aspf | Modo de alineación para SPF | `aspf=r`  
  
Verifique el registro DMARC de un nombre de dominio con una herramienta como
[MXToolbox DMARC](https://mxtoolbox.com/DMARC.aspx).

Ver también

[DMARC.org es un excelente recurso para aprender más sobre los registros
DMARC.](https://dmarc.org/overview/)

## Documentación de SPF, DKIM y DMARC de los proveedores más comunes

  * [OVH DNS](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/)

  * [OVH SPF](https://docs.ovh.com/us/en/domains/web_hosting_the_spf_record/)

  * [GoDaddy TXT record](https://www.godaddy.com/help/add-a-txt-record-19232)

  * [GoDaddy SPF](https://www.godaddy.com/help/add-an-spf-record-19218)

  * [GoDaddy DKIM](https://www.godaddy.com/help/add-a-cname-record-19236)

  * [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/)

  * [CloudFlare DNS](https://support.cloudflare.com/hc/en-us/articles/360019093151)

  * [Google Domains](https://support.google.com/domains/answer/3290350?hl=en)

  * [Azure DNS](https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal)

Utilice la herramienta [Mail-Tester](https://www.mail-tester.com/) para probar
por completo su configuración. Esta herramienta le da un resumen completo del
contenido y la configuración en un único correo electrónico enviado. También
puede utilizar Mail-Tester para configurar los registros de otros proveedores
menos conocidos.

Ver también

[Usar Mail-Tester para establecer registros SPF para proveedores
determinados](https://www.mail-tester.com/spf/)

  *[SPF]: Convenio de remitentes
  *[DKIM]: DomainKeys Identified Mail
  *[DMARC]: Autenticación basada en dominios para mensajes, reportes y conformidad
  *[DNS]: Sistema de nombres de dominio
  *[CNAME]: nombre canónico
  *[RUA]: Reporte URI de reportes agregados
  *[RUF]: Reporte URI para fallos forenses
  *[PCT]: Porcentaje de mensajes sujetos a filtración
  *[P]: Política para dominio organizativo
  *[SP]: Política para subdominios del OD
  *[ADKIM]: Modo de alineamiento para DKIM
  *[ASPF]: Modo de alineamiento para SPF

