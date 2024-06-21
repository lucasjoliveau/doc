# Digitalización de documentos con IA

La **digitalización de facturas** es el proceso en el que los documentos
impresos se convierten en formularios de facturas en su contabilidad en línea.

Konvergo ERP usa OCR y tecnología de inteligencia artificial para reconocer el
contenido de los documentos. Los formularios para las facturas de cliente y
proveedor se crean y se llenan según las facturas escaneadas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/app/invoice-automation">Prueba de la digitalización de facturas de Konvergo ERP</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/digitize-bills-with-ocr-1712">Tutoriales de Konvergo ERP: digitalización de facturas mediante el OCR</a></p></li>
</ul>
</div>

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Digitización, marque la
casilla **Digitalización de documentos** y defina si las **facturas de
proveedor** y **facturas de clientes** (esto incluye notas de crédito de
cliente) se deberían procesar de forma automática o manual.

Si habilita la opción **línea de factura única por impuesto** , solo se creará
una línea por impuesto en la nueva factura, sin importar el número de líneas
en la factura.

## Cargar facturas

### Cargar facturas de forma manual

Desde el **tablero de Contabilidad** , haga clic en el botón **Subir** de su
diario de facturas de proveedor. Si lo prefiere, vaya a Contabilidad ‣
Clientes ‣ Facturas o Contabilidad ‣ Proveedores ‣ Facturas y seleccione
**Subir**.

### Cargar facturas usando un seudónimo de correo electrónico

Puede configurar su escáner conectado de forma que envíe los documentos
escaneados a un seudónimo de correo electrónico. Los correos electrónicos que
se envíen a estos seudónimos se convertirán en nuevos borradores de facturas
de clientes/proveedores.

Puede modificar el seudónimo de correo electrónico de un diario desde la
aplicación **Configuración**. Solo debe ir a **Configuración General:
Conversaciones** , active **Servidores personalizados de correo electrónico**
, añada un **Dominio de seudónimo** , y **Guardar**.

El seudónimo de correo electrónico está ahora disponible en la pestaña
**Configuración avanzada** del diario. Los correos electrónicos que se envíen
a esta dirección se convertirán automáticamente en nuevas facturas o recibos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si usa la aplicación <a href="../../../productivity/documents">Documentos</a> podrá enviar de manera automática sus facturas escaneadas al espacio de trabajo compartido de <b>finanzas</b> (por ejemplo, <code>inbox-finanzas@ejemplo.odoo.com</code>).</p>
</div>

El seudónimo predeterminado de correo electrónico `facturas-proveedor@` y
`facturas-clientes@` seguido del **dominio del seudónimo** que establezca, se
crearán automáticamente para los diarios de **facturas de proveedor** y
**facturas de clientes**. Los correos electrónicos enviados a estas
direcciones se convierten automáticamente en nuevas facturas o recibos.

Si desea cambiar el seudónimo de correo electrónico predeterminado vaya a
Contabilidad ‣ Configuración ‣ Contabilidad: Diarios. Seleccione el diario a
editar y haga clic en la pestaña **Ajustes avanzados** , ahí podrá editar el
`seudónimo de correo electrónico`.

## Digitalización de facturas

Según su configuración, se podrá procesar el documento de manera automática o
manual, si es manual deberá hacer clic en **Enviar para digitalizzción**.

Una vez que se hayan extraído los datos del PDF, si lo necesita, también los
puede corregir haciendo clic en la etiqueta correspondiente (disponible en
modo de **edición**) y seleccionando la información correcta.

## Reconocimiento de datos por IA

Es necesario revisar y corregir (si es necesario) la información registrada
durante la digitalización. Después, deberá publicar el documento haciendo clic
en **Confirmar**. De esta forma, la IA aprenderá y el sistema identificará los
datos correctos para futuras digitalizaciones.

## Precios

La _digitalización de facturas*_ es un servicio de compras dentro de la
aplicación (IAP, por sus siglas en inglés) que requiere de créditos prepagados
para funcionar. Digitalizar un documento consume un crédito.

Para comprar créditos, vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣
Digitalización y haga clic en **comprar créditos** , o vaya a Ajustes ‣ Konvergo ERP
IAP y haga clic en **ver mis servicios**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si utiliza Konvergo ERP en línea y tiene la versión Enterprise, cuenta con créditos de muestra gratis para probar la función.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://iap.odoo.com/privacy#header_6">Nuestra política de privacidad</a></p></li>
<li><p><a href="../../../essentials/in_app_purchase">Compras dentro de la aplicación (IAP)</a></p></li>
</ul>
</div>

  *[OCR]: reconocimiento óptico de caracteres

