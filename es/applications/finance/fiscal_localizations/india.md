# India

## Instalación

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para obtener todas las funciones de la localización de la India:

Nombre | Nombre técnico | Descripción  
---|---|---  
India - Contabilidad | `l10n_in` | [Paquete de localización fiscal](../fiscal_localizations.html#fiscal-localizations-packages) predeterminado  
India - Facturación electrónica | `l10n_in_edi` | India - Integración de facturación electrónica  
India - Guía de embarque electrónica | `l10n_in_edi_ewaybill` | India - Integración de guía de embarque electrónica  
India - Declaración electrónica de impuestos GSTR para la India | `l10n_in_reports_gstr` | India - Declaración de impuestos GST  
India - Reportes contables | `l10n_in_reports` | India - Reportes de impuestos  
India - Reporte de compra (GST) | `l10n_in_purchase` | India - Reporte de compra GST  
India - Reporte de ventas (GST) | `l10n_in_sale` | India - Reporte de ventas GST  
India - Reporte de existencias (GST) | `l10n_in_stock` | India - Reporte de existencias GST  
![Módulos de localización de la India](../../../_images/india-modules.png)

## Sistema de facturación electrónica

Odoo cumple con los requisitos del **sistema de facturación electrónica del
Impuesto sobre Bienes y Servicios (GST) de la India**.

### Configurar

#### Registro de facturación electrónica NIC

Para obtener sus **credenciales API** debe registrarse en el portal de
facturación electrónica NIC. Necesita estas credenciales para configurar su
aplicación Contabilidad de Odoo.

  1. Inicie sesión en el [portal de facturación electrónica NIC](https://einvoice1.gst.gov.in/) , haga clic en Iniciar sesión (Login) y escriba su usuario y contraseña;

Nota

Si ya se registró con anterioridad en el portal NIC, puede usar las mismas
credenciales para iniciar sesión.

![Registro del sistema Odoo ERP en el portal web de facturación
electrónica](../../../_images/e-invoice-system-login.png)

  2. Desde el tablero, vaya a Registro de API ‣ Credenciales de usuario ‣ Crear usuario API;

  3. Después recibirá un código OTP en el número de teléfono celular que tiene registrado. Escriba el código OTP y haga clic en Verificar OTP.

  4. Seleccione Mediante GSP para la interfaz API, seleccione Tera Software Limited como GSP y escriba el usuario y contraseña para su API. Una vez listo, haga clic en Enviar.

![Ingresar usuario y contraseña específicos de la
API](../../../_images/submit-api-registration-details.png)

#### Configuración en Odoo

Para habilitar el servicio de facturación electrónica en Odoo, vaya a
Contabilidad ‣ Configuración ‣ Ajustes ‣ India - Facturación electrónica y
escriba el nombre de usuario y contraseña previamente establecidos para la
API.

![Configuración del servicio de facturación
electrónica](../../../_images/e-invoice-setup.png)

##### Diarios contables

Para enviar facturas electrónicas de forma automática al portal de facturación
electrónica NIC, primero debe configurar su diario de _ventas_. Vaya a
Contabilidad ‣ Configuración ‣ Diarios, abra su diario de _ventas_ y en la
pestaña Ajustes avanzados, en intercambio electrónico de datos, habilite
Facturación electrónica (IN) y guarde.

### Flujo de trabajo

#### Validación de la factura

Una vez validada una factura, aparece un mensaje de confirmación en la parte
superior. Odoo carga de forma automática el archivo JSON firmado con las
facturas validadas al portal de facturación electrónica NIC después de un
tiempo. Si desea procesar la factura de inmediato, haga clic en Procesar
ahora.

![Mensaje de confirmación de facturación electrónica para la
India](../../../_images/e-invoice-process.png)

Nota

  * Puede encontrar el archivo JSON firmado en los archivos adjuntos en el chatter.

  * Puede consultar el estado del EDI del documento en la pestaña Documento EDI o en el campo Facturación electrónica de la factura.

#### Reporte la de factura en PDF

En cuanto valida y envía una factura, puede imprimir su reporte en PDF. El
reporte incluye el IRN, Ack. No (número de confirmación), Ack. Date (fecha de
confirmación) y código QR. Estos certifican que la factura es un documento
fiscal válido.

![IRN y código QR](../../../_images/invoice-report.png)

#### Cancelar una factura electrónica

Si desea cancelar una factura electrónica, vaya a la pestaña Otra información
de la factura y complete los campos Motivo de la cancelación y Comentarios de
la cancelación. Después, haga clic en Solicitar cancelación de EDI. El estado
del campo Factura electrónica cambia a Por cancelar.

Importante

Al hacer esto cancela la factura electrónica y la guía de embarque
electrónica.

![Motivo de la cancelación y comentarios](../../../_images/e-invoice-
cancellation.png)

Nota

  * Si desea suspender la cancelación antes de procesar la factura, haga clic en Suspender la cancelación del EDI.

  * Una vez que solicite cancelar la factura electrónica, Odoo envía de forma automática el archivo JSON firmado al portal de facturación electrónica NIC. Puede hacer clic en Procesar ahora si desea procesar la factura al instante.

#### Verificación de facturación electrónica GST

Después de enviar una factura electrónica, puede verificar si la factura está
firmada desde el propio sitio web del sistema de facturación electrónica GST.

  1. Descargue el archivo JSON de los archivos adjuntos, este se encuentra en el chatter de la factura relacionada;

  2. Abra el [portal de facturación electrónica NIC](https://einvoice1.gst.gov.in/) y vaya a Buscar ‣ Verificar factura firmada;

  3. Seleccione el archivo JSON y envíelo;

![seleccione el archivo JSON para verificar la
factura](../../../_images/verify-invoice.png)

Aparecerá un mensaje de confirmación si el archivo está firmado.

![Factura electrónica verificada](../../../_images/signed-invoice.png)

## Guía de embarque electrónica

### Configurar

Odoo cumple con los requisitos del **sistema de guía de embarque electrónica
del Impuesto sobre bienes y servicios (GST) de la India**.

#### Registro de la API en la guía de embarque electrónica NIC

Debe registrarse en el portal de guía de embarque electrónica NIC para obtener
sus **credenciales API**. Necesita estas credenciales para configurar su
aplicación Contabilidad de Odoo.

  1. Inicie sesión en el [portal de guía de embarque electrónica NIC](https://ewaybillgst.gov.in/) , haga clic en Iniciar sesión y escriba su usuario y contraseña.

  2. Desde su tablero, vaya a Registro ‣ Para GSP.

  3. Haga clic en Enviar OTP. Una vez que haya recibido el código en su númerode teléfono celular registrado, introdúzcalo y haga clic en :guilabel:`Verificar OTP;

  4. Verifique si Tera Software Limited ya se encuentra en la lista de GSP/ERP registrados. Si es así, utilice el mismo usuario y contraseña que usa para iniciar sesión en el portal NIC. De lo contrario, siga los siguientes pasos:

![Lista de guía de embarque electrónica de GSP/ERP
registrados](../../../_images/e-waybill-gsp-list.png)

  5. Seleccione Agregar/nuevo, elija Tera Software Limited como su nombre GSP, cree un usuario y contraseña para su API y haga clic en Agregar.

![Enviar los datos de registro de la API del GSP](../../../_images/e-waybill-
registration-details.png)

#### Configuración en Odoo

Para configurar el servicio de guía de embarque electrónica, vaya a
Contabilidad ‣ Configuración ‣ Ajustes ‣ Guía de embarque electrónica para la
India ‣ Configurar guía de embarque electrónica, e ingrese su usuario y
contraseña.

![Configuración de la guía de embarque electrónica en
Odoo](../../../_images/e-waybill-configuration.png)

### Flujo de trabajo

#### Enviar una guía de embarque electrónica

Puede enviar una guía de embarque electrónica de forma manual al hacer clic en
Enviar guía de embarque electrónica. Para enviar la guía de embarque
electrónica en automático al confirmar una factura, habilite Guía de embarque
electrónica (IN) en su Diario de ventas o compras.

![Botón de enviar guía de embarque electrónica en las
facturas](../../../_images/e-waybill-send-button.png)

#### Validación de la factura

Después de emitir y enviar una factura a través de Enviar guía de embarque
electrónica, aparece un mensaje de confirmación.

![Mensaje de confirmación de guía de embarque electrónica de la
India](../../../_images/e-waybill-process.png)

Nota

  * Puede encontrar el archivo JSON firmado en los archivos adjuntos en el chatter.

  * De forma automática, Odoo sube el archivo JSON firmado al portal gubernamental después de un tiempo. Haga clic en Procesar ahora si desea procesar la factura en ese instante.

#### Reporte la de factura en PDF

Puede imprimir el reporte PDF de la factura una vez que haya enviado la guía
de embarque electrónica, este incluye el **número de guía de embarque
electrónica** y la **fecha de validez de la guía de embarque electrónica**.

![Número y fecha de confirmación de la guía de embarque
electrónica](../../../_images/e-waybill-invoice-report.png)

#### Cancelar una guía de embarque electrónica

Si desea cancelar una guía de embarque electrónica, vaya a la pestaña Guía de
embarque electrónica de la factura relacionada y complete los campos Motivo de
la cancelación y Comentarios de la cancelación. Después, haga clic en
Solicitar cancelación de EDI.

Importante

Hacer esto cancela la factura electrónica (en caso de que aplique) y la guía
de embarque electrónica.

![Motivo de la cancelación y comentarios](../../../_images/e-waybill-
cancellation.png)

Nota

  * Si desea suspender la cancelación antes de procesar la factura, haga clic en Suspender cancelación de EDI.

  * Una vez que haya solicitado la cancelación de la guía de embarque electrónica, Odoo envía de forma automática el archivo JSON firmado al portal gubernamental. Puede hacer clic en Procesar ahora si desea procesar la factura en ese instante.

## Declaración de impuestos GST en la India

### Habilitar acceso a la API

Antes de presentar declaraciones de impuestos GST en Odoo, debe habilitar el
acceso a la API en el portal GST.

  1. Inicie sesión en el [portal GST](https://services.gst.gov.in/services/login) con su usuario y contraseña, vaya a Mi perfil (My profile) en su **menú de perfil**.

![Haga clic en Mi perfil desde su perfil](../../../_images/gst-portal-my-
profile.png)

  2. Seleccione Administrar el acceso a la API (Manage API Access) y haga clic en Sí (Yes) para habilitar el acceso.

![Hacer clic en sí](../../../_images/gst-portal-api-yes.png)

  3. Esta acción habilitará un menú desplegable de duración (Duration). Seleccione la duración de su preferencia y haga clic en confirmar (Confirm).

### Servicio GST de la India en Odoo

Una vez que haya habilitado el acceso a la API en el portal GST, puede
configurar el Servicio GST de la India en Odoo.

Vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Servicio GST de la India y
escriba su usuario GST. Haga clic en Enviar OTP, introduzca el código y
valídelo.

> ![Introduzca su nombre de usuario del portal GST como
> usuario](../../../_images/gst-setup.png)

### Presentar declaraciones GST

Puede presentar su declaración GST cuando el Servicio GST de la India está
configurado. Vaya a Contabilidad ‣ Reportes ‣ India ‣ Periodo de declaración
GST, cree un nuevo **periodo de declaración GST** si no hay uno. En Odoo, la
declaración de impuestos GST se realiza en **tres pasos** :

Nota

La **periodicidad de la declaración de impuestos** se puede
[configurar](../accounting/reporting/tax_returns.html) según las necesidades
del usuario.

#### Enviar el GSTR-1

  1. El usuario puede verificar el reporte GSTR-1 antes de subirlo al **portal GST** , solo debe hacer clic en Reporte GSTR-1.

  2. Si el reporte **GSTR-1** es correcto, haga clic en Cargar a GSTN para enviarlo al **portal GST**. El estado del reporte GSTR-1 cambia a Enviando.

![GSTR-1 en el estado "Enviando"](../../../_images/gst-gstr-1-sending.png)

  3. Tras unos segundos, el estado del reporte **GSTR-1** cambia a En espera del estado, esto significa que el reporte **GSTR-1** ha sido enviado al Portal GST y está siendo verificado allí mismo.

![GSTR-1 en espera del estado](../../../_images/gst-gstr-1-waiting.png)

  4. Una vez más, después de unos segundos, el estado cambia a Enviado o Error en la factura. El estado Error en la factura indica que algunas de las facturas no están completas de forma correcta, así que el **portal GST** no las puede validar.

     * Si el estado del **GSTR-1** es Enviado, significa que ahora puede declarar su reporte **GSTR-1** en el **portal GST**.

![GSTR-1 enviado](../../../_images/gst-gstr-1-sent.png)

     * Si el estado del **GSTR-1** es Error en la factura, se deberán revisar las facturas para detectar errores en el registro de notas. Una vez resueltos los problemas, el usuario puede hacer clic en Cargar a GSTN para volver a enviar el archivo al **portal GST**.

![Error en la factura en GSTR-1](../../../_images/gst-gstr-1-error.png)

![Registro de errores en la factura en GSTR-1](../../../_images/gst-
gstr-1-error-log.png)

  5. Haga clic en Marcar como declarado tras presentar el reporte **GSTR-1** en el **portal GST**. El estado del reporte cambia a Declarado en **Odoo**.

![GSTR-1 en estado "Declarado"](../../../_images/gst-gstr-1-filed.png)

#### Recibir el GSTR-2B

Los usuarios pueden obtener el **reporte GSTR-2B** desde el **portal GST** ,
esto hace que el reporte se concilie de manera automática con sus facturas de
Odoo.

  1. Haga clic en Obtener resumen de GSTR-2B. Después de unos segundos, el estado del reporte cambia a En espera de la recepción. Esto significa que Odoo está intentando recibir el reporte **GSTR-2B** del **portal GST**.

![En espera de la recepción del GSTR-2B](../../../_images/gst-
gstr-2b-waiting.png)

  2. Una vez más, tras unos segundos, el estado del **GSTR-2B** cambia a En proceso. Odoo está conciliando el reporte **GSTR-2B** con sus facturas de Odoo.

![En espera de la recepción del GSTR-2B](../../../_images/gst-
gstr-2b-processed.png)

  3. Después de esto, el estado del reporte **GSTR-2B** cambia a Conciliado o Parcialmente conciliado.

     * Si el estado está Conciliado:

> ![GSTR-2B conciliado](../../../_images/gst-gstr-2b-matched.png)

     * Si el estado está Parcialmente conciliado puede hacer cambios en las facturas. Haga clic en Ver facturas conciliadas y después en Volver a conciliar.

> ![GSTR-2B parcialmente conciliado](../../../_images/gst-
> gstr-2b-partially.png) ![Facturas conciliadas del reporte
> GSTR-2B](../../../_images/gst-gstr-2b-reconcile.png)

#### Reporte GSTR-3

El reporte GSTR-3 es un resumen mensual de **ventas** y **compras**. Esta
devolución se genera de forma automática al extraer la información de
**GSTR-1** y **GSTR-2**.

  1. Los usuarios pueden comparar el reporte **GSTR-3** con el mismo reporte que se encuentra disponible en el **portal GST** para verificar si coinciden, haga clic en Reporte GSTR-3.

  2. Una vez que el usuario verificó el reporte **GSTR-3** y se pagó el importe del impuesto en el **portal GST** , puede **cerrar** el reporte si hace clic en Asiento de cierre.

![GSTR-3](../../../_images/gst-gstr-3.png)

  3. En Asiento de cierre, agregue el monto del impuesto pagado en el **portal GST** mediante challan y haga clic en REGISTRAR para registrarlo;

![Registrar asiento GSTR-3](../../../_images/gst-gstr-3-post.png)

  4. Una vez registrado, el estado del reporte **GSTR-3** cambia a declarado.

![GSTR-3 declarado](../../../_images/gst-gstr-3-filed.png)

## Reportes de impuestos

### Reporte GSTR-1

El reporte GSTR-1 se divide en secciones. Muestra el importe base, CGST, SGST,
IGST y CESS para cada sección.

> ![Reporte GSTR-1](../../../_images/gst-gstr-1-sale-report.png)

### Reporte GSTR-3

El reporte GSTR-3 incluye distintas secciones:

  * Detalles de suministro interno y externo sujetos a un **cobro revertido** ;

  * ITC elegible;

  * Valores de suministro interno **externo** , **sin gravar** y **no sujetos a GST** ;

  * Detalles de suministros interestatales a personas **no registradas**.

> ![Reporte GSTR-3](../../../_images/gst-gstr-3-report.png)

  *[NIC]: National Informatics Centre
  *[OTP]: Contraseña de un solo uso
  *[EDI]: Intercambio electrónico de datos
  *[IRN]: Número de referencia de la factura
  *[CGST]: Impuesto central sobre bienes y servicios
  *[SGST]: Impuesto estatal sobre bienes y servicios
  *[IGST]: Impuesto integrado sobre bienes y servicios
  *[ITC]: Crédito fiscal de impuesto sobre la renta

