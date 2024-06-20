# México

## Webinarios

Contamos con un video que explica la localización mexicana, el cual cubre cómo
implementarla desde cero, cómo configurarla, cómo completar flujos de trabajo
comunes, y también proporciona un análisis más profundo de varios casos de uso
específicos.

  * [Webinar de una demostración completa](https://www.youtube.com/watch?v=5cdogjm0GCI).

## Introducción

Los módulos de Odoo para la localización mexicana son compatibles con la firma
electrónica de facturas de acuerdo con las regulaciones del SAT para [la
versión 4.0 del
CFDI](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo_20_Guia_de_llenado_CFDI.pdf),
el cual es un requisito legal desde el 1° de enero del 2022. Estos módulos
también incluyen reportes contables relevantes (como el DIOT, que admite el
comercio exterior y la creación de guías de envío).

Nota

Para firmar de manera electrónica cualquier documento en Odoo, asegúrese de
tener instalada la aplicación _Firma_.

## Configuración

### Requisitos

Es necesario que cumpla los siguientes requisitos antes de configurar los
módulos de localización mexicana en Odoo:

  1. Estar registrado en el SAT y tener un RFC válido.

  2. Tener un [Certificate of Digital Seal](https://www.gob.mx/sat/acciones-y-programas/certificado-de-sello-digital) (CSD).

  3. Escoger un PAC (Proveedor Autorizado de Certificación). Por el momento, Odoo trabaja con los siguientes PACs: [Solución Factible](https://solucionfactible.com/), [Quadrum (antes Finkok)](https://cfdiquadrum.com.mx/) y [SW Sapien - Smarter Web](https://sw.com.mx/).

  4. Contar con conocimiento y experiencia en facturación, ventas y contabilidad en Odoo. Esta documentación solo contiene la información necesaria para usar Odoo.

### Instalación de los módulos

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para tener todas las funciones de la localización mexicana. Los
módulos de [contabilidad](../accounting.html) y _contactos_ son obligatorios
para esta configuración:

Nombre | Nombre técnico | Descripción  
---|---|---  
México - Contabilidad | `l10n_mx` | El [paquete de localización fiscal](../fiscal_localizations.html) predeterminado agrega características contables para la localización mexicana, por ejemplo: los impuestos más usados y el plan de cuentas, de acuerdo con el [código de agrupación de cuentas del SAT](https://www.gob.mx/cms/uploads/attachment/file/151586/codigo_agrupador.pdf).  
EDI para México | `l10n_mx_edi` | Incluye todos los requisitos técnicos y funcionales para generar y validar [documentos electrónicos](../accounting/customer_invoices/electronic_invoicing.html) según la documentación técnica publicada por el SAT. Esto le permite enviar facturas (con o sin adendas) y complementos de pago al gobierno.  
EDI v4.0 para México | `l10n_mx_edi_40` | Es necesario para crear documentos XML con las especificaciones necesarias del CFDI 4.0.  
Reportes de la localización mexicana de Odoo | `l10n_mx_reports` | Adapta los reportes para la contabilidad electrónica mexicana: plan de cuentas, balanza de comprobación y DIOT.  
México - Reportes de la localización para el cierre | `l10n_mx_reports_closing` | Es necesario para crear el asiento de cierre (también conocido como _mes 13_).  
Exportación en XML de pólizas mexicanas de Odoo | `l10n_mx_xml_polizas` | Permite la exportación de archivos XML de sus asientos de diario para las auditorías obligatorias.  
Módulo de enlace para la exportación de pólizas mexicanas en XML a EDI | `l10n_mx_xml_polizas_edi` | Complementa el módulo `l10n_mx_xml_polizas`.  
  
Nota

Si crea una base de datos desde cero y elige México como país, Odoo instalará
automáticamente los siguientes módulos: México - Contabilidad, EDI para
México, y EDI v4.0 para México.

Los siguientes módulos son opcionales pero se recomienda instalarlos _solo si_
los necesita para satisfacer una necesidad empresarial específica.

Nombre | Nombre técnico | Descripción  
---|---|---  
EDI para México (funciones avanzadas) | `l10n_mx_edi_extended` | Añade el complemento de comercio exterior a las facturas: un requisito legal para vender productos en el extranjero.  
EDI v4.0 para México (COMEX) | `l10n_mx_edi_extended_40` | Adapta el módule `l10n_mx_edi_extended` para CFDI 4.0.  
México - Guía electrónica de entrega | `l10n_mx_edi_stock` | Le permite crear una _Carta Porte_ : es un conocimiento de embarque que le prueba al gobierno que está enviando bienes entre A&B con un documento electrónico firmado.  
Guía electrónica de entrega para México CFDI 4.0 | `l10n_mx_edi_stock_40` | Adapta el módule `l10n_mx_edi_stock` para CFDI 4.0  
Localización mexicana de Odoo para las existencias y el embarque | `l10n_mx_edi_landing` | Permite gestionar los números de identificación comercial (NICO) relacionados con los costos de embarque en documentos electrónicos.  
  
### Configure su empresa

Después de instalar los módulos correctos, debe verificar que la empresa se
haya configurado con los datos correctos. Para hacerlo vaya a Ajustes ‣
Ajustes generales ‣ Empresas y seleccione Actualizar información debajo del
nombre de su empresa.

Escriba su dirección completa en el formulario que aparecerá y no olvide
incluir el código postal, el estado, el país, y el RFC (número de
identificación fiscal).

Según los requisitos del CFDI 4.0, el nombre del contacto principal **debe**
coincidir con el nombre de la empresa registrado en el SAT sin la abreviatura
de persona moral.

![Requisitos principales de la empresa para facturar
correctamente](../../../_images/mx-company-info.png)

Importante

Desde un punto de vista legal, una empresa mexicana **debe** usar la divisa
local (MXN). Por lo tanto, Odoo no brinda funciones para gestionar una
configuración alterna. Si desea gestionar otra divisa, deje que MXN sea la
divisa predeterminada y use una [lista de
precios](../../sales/sales/products_prices/prices/pricing.html) en su lugar.

Luego, vaya a Ajustes ‣ Contabilidad ‣ Facturación electrónica (MX) ‣ Régimen
fiscal, y seleccione el régimen que usa su empresa desde la lista desplegable
y haga clic en Guardar.

![Configuración del régimen fiscal en los ajustes de Contabilidad.
](../../../_images/mx-fiscal-regime.png)

Truco

Si desea probar la localización mexicana, puede establecer una dirección real
de México en su empresa (recuerde completar todos los campos), añada
`EKU9003173C9` como RFC y `ESCUELA KEMPER URGATE` como el nombre de empresa.
Para el Régimen fiscal, use General de Ley Personas Morales.

### Contactos

Si desea crear un contacto para enviarle facturas, vaya a Contactos ‣ Crear.
Ingrese el nombre del contacto y dirección completa. No olvide incluir el
código postal, estado, país, y RFC (número de identificación fiscal).

Importante

Dentro de su empresa, asegúrese de que sus contactos tengan escrito su nombre
de forma correcta en el SAT. Lo mismo aplica para el régimen fiscal, el cual
debe agregar en la pestaña EDI MX.

### Impuestos

También es necesario configurar el tipo factor y los objetos fiscales para
poder firmar correctamente las facturas.

#### Tipo factor

El campo _tipo de factor_ ya viene con los impuestos predeterminados. Si crea
nuevos impuestos, asegúrese de configurar este campo. Para hacerlo, vaya a
Contabilidad‣ Configuración ‣ Impuestos, luego active el campo tipo de factor
en la pestaña Opciones avanzadas para todos los registros con el Tipo de
impuesto configurado como Ventas.

![Configuración del tipo de impuesto tipo de factor de
ventas.](../../../_images/mx-factor-type.png)

Truco

México trabaja con dos tipos diferentes de IVA 0% para amoldarse a dos
escenarios:

  * _IVA 0%_ establece el Tipo de factor como Tasa

  * _Exento de IVA_ establece el Tipo de factor como Exento

#### Objeto de impuestos

Uno de los requisitos del CFDI 4.0 es que el archivo XML resultante necesita
(o no) desglosar los impuestos de la operación. Hay tres posibles valores
diferentes que se agregan al archivo XML:

  * `01`: No está sujeto a impuestos - este valor se añade de manera automática si su línea contable no contiene impuestos.

  * `02`: Sujeto a impuestos - está es la configuración predeterminada de cualquier línea contable que contenga impuestos.

  * `03`: Sí objeto del impuesto y no obligado al desglose. Puede activar este valor si es necesario reemplazar el valor 02 para ciertos clientes.

Vaya a Contactos ‣ la factura de su cliente ‣ pestaña MX EDI para usar el
valor `03` y seleccione la casilla Sin desglose de impuestos.

![La opción "Sin desglose de impuestos" en la pestaña MX EDI de la factura del
cliente.](../../../_images/mx-tax-breakdown.png)

Importante

El valor Sin desglose de impuestos aplica **solo** a algunos regímenes
fiscales o impuestos específicos. Le recomendamos que consulte a su contador
antes de hacer cualquier modificación, así sabrá si es necesario para su
negocio.

#### Otras configuraciones fiscales

Al registrar un pago, Odoo realizará el movimiento de impuestos desde la
_Cuenta transitoria de base de efectivo_ a la cuenta que estableció en la
pestaña Definición. Para tal movimiento, se utilizará una cuenta de base
imponible (`Base imponible de Impuestos en Base a Flujo de Efectivo`) en el
asiento contable al reclasificar impuestos. **No elimine esta cuenta**.

Si crea un nuevo impuesto en Contabilidad ‣ Configuración ‣ Impuestos, también
debe agregar las tablas de impuesto correspondientes (`IVA`, `ISR` o `IEPS`).
Odoo **solo** es compatible con estos tres grupos de impuestos.

![Cuentas disponibles en Odoo.](../../../_images/mx-taxes-config.png)

### Productos

Para configurar los productos, vaya a Contabilidad ‣ Clientes ‣ Productos y
seleccione el producto a configurar o cree uno nuevo. Diríjase a la pestaña
Contabilidad y busque el campo Categoría de producto UNSPSC, allí seleccione
la categoría que representa al producto. Puede realizar este proceso de forma
manual o mediante [una importación
masiva](../../essentials/export_import_data.html).

Nota

Todos los productos deben tener asociada una clave del SAT para evitar errores
de validación.

### Facturación electrónica

#### Credenciales del proveedor autorizado de certificación

Después de que haya procesado su [certificado de sello digital
(CSD)](https://www.sat.gob.mx/aplicacion/16660/genera-y-descarga-tus-archivos-
a-traves-de-la-aplicacion-certifica) con el SAT, **debe** registrarse
directamente con el PAC de su elección antes de empezar a crear facturas con
Odoo.

Una vez que haya creado su cuenta con cualquiera de estos proveedores, vaya a
Ajustes‣ Contabilidad ‣ Facturación electrónica (MX). En la sección PAC MX
escriba el nombre de su PAC con sus credenciales (Nombre de usuario PAC y
Contraseña del PAC).

![Configuración de las credenciales del PAC desde los ajustes de
Contabilidad.](../../../_images/mx-pac-account.png)

Truco

En caso de que no cuente con estas credenciales pero desee probar las
funciones de facturación electrónica, marque la casilla Entorno de prueba PAC
MX y seleccione Solución factible como PAC. No es necesario que escriba un
nombre de usuario o contraseña para un entorno de prueba.

#### Certificados .cer y .key

Los [certificados de sello digital de la
empresa](https://www.gob.mx/tramites/ficha/certificado-de-sello-
digital/SAT139) deben estar en la sección Certificados MX. Vaya a Ajustes ‣
Contabilidad ‣ Facturación electrónica (MX) y, desde la sección Certificados
MX, seleccione Agregar una línea. Aparecerá una ventana, allí haga clic en
Crear y suba su certificado (el archivo `.cer`), la llave del certificado (el
archivo `.key`) y la contraseña del certificado. Por último, haga clic en
Guardar y cerrar.

![Campos para subir el certificado y la llave del
certificado.](../../../_images/mx-certificates.png)

Truco

Si aún no ha contratado algún PAC y desea probar la función de facturación
electrónica, puede utilizar los siguientes certificados de prueba del SAT:

  * [`Certificado`](../../../_downloads/b59328d6458977aebd30f2f8286679e1/certificate.cer)

  * [`Clave del certificado`](../../../_downloads/19f36789d1d2bc50ef639d1141721304/certificate.key)

  * **Contraseña** : `12345678a`

## Flujos de trabajo

### Facturación electrónica

El proceso de facturación en Odoo está basado en la versión 4.0 del [Anexo
20](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm) de la
facturación electrónica del SAT.

#### Facturas de cliente

Es necesario que cree una factura de cliente con el [flujo de facturación
estándar](../accounting/customer_invoices.html) para comenzar a facturar desde
Odoo.

Puede realizar cualquier modificación necesaria si el documento se encuentra
en modo borrador. Por ejemplo, puede agregar la forma de pago adecuada o el
uso correspondiente que el cliente podría necesitar.

Tras confirmar la factura del cliente, aparece el siguiente mensaje en color
azul: Este servicio de facturación electrónica procesará la factura de forma
asíncrona: CFDI (4.0).

Cuando presiona el botón Procesar ahora envía el documento al gobierno para
que puedan firmarlo. Después de que el gobierno se lo devuelve firmado,
aparece el campo folio fiscal y el archivo XML se adjunta al chatter.

Truco

Puede confirmar si el archivo XML es válido en el SAT si hace clic en
Reintentar en el campo Estado del SAT de la factura.

Si se encuentra en un entorno de prueba, siempre recibirá el mensaje No se
encuentra.

Para enviar la factura firmada a su cliente, puede enviar ambos archivos, XML
y PDF, desde Odoo si hace clic en el botón Enviar e imprimir. También puede
descargar el archivo PDF a su computadora si hace clic en el botón Imprimir y
selecciona la opción correspondiente.

#### Notas de crédito

El tipo de documento de una factura es «I» (Ingreso), el de una nota de
crédito es «E» (Egreso).

Lo único que cambia para el [flujo estándar de las notas de
crédito](../accounting/customer_invoices/credit_notes.html) es que, como
requisito del SAT, debe haber una relación entre una nota de crédito y una
factura mediante el folio fiscal.

Debido a este requisito, el campo Origen del CFDI agrega esta relación
mediante `01|`, seguido del folio fiscal de la factura original.

![Número de origen del CFDI de ejemplo.](../../../_images/mx-creating-credit-
note.png)

Truco

Utilice el botón Agregar nota de crédito que se encuentra en la factura en
lugar de crearla de forma manual, así el campo Origen del CFDI se agregará en
automático.

#### Complementos de pago

##### Política de pago

Además, la localización mexicana ahora cuenta con el campo Política de pago.
La [documentación del SAT](https://www.sat.gob.mx/consultas/92764/comprobante-
de-recepcion-de-pagos) menciona que puede haber 2 tipos de pagos:

  * `PUE` \- Pago en una Sola Exhibición

  * `PPD` \- Pago en Parcialidades o Diferido

> Ver también
>
> [Integrar costos adicionales con productos (costos en
> destino)](../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs.html)

La diferencia depende de la _fecha de vencimiento_ o las _condiciones de pago_
de la factura.

Vaya a Contabilidad ‣ Clientes ‣ Facturas para configurar facturas PUE. Allí,
elija una factura con fecha de vencimiento dentro del mismo mes o una
condición de pago que no implique cambiar el mes de vencimiento (pago
inmediato, 15 días, 21 días, todo dentro del mes en curso).

![Ejemplo de una factura con los requisitos de PUE.](../../../_images/mx-pue-
payment.png)

Truco

Algunas condiciones de pago están instaladas de forma predeterminada y puede
gestionarlas en Contabilidad ‣ Configuración ‣ Condiciones de pago.

Vaya a Contabilidad ‣ Clientes ‣ Facturas para configurar facturas para
configurar facturas PPD. Allí, elija una factura con la fecha de vencimiento
después del primer día del siguiente mes. Esto también aplica si sus
condiciones de pago vencen el siguiente mes.

![Ejemplo de una factura con los requisitos de PPD.](../../../_images/mx-ppd-
payment.png)

Importante

Como la política PPD implica que una factura no será pagada en ese momento, la
forma de pago adecuada para las facturas de PPD es 99 - Por Definir.

##### Flujo de pago

En ambos casos, el proceso de pago en Odoo [es el
mismo](../accounting/customer_invoices.html). La diferencia principal es que
los pagos relacionados con las facturas PPD hacen que se origine un documento
de tipo «P» (Pago).

Si un pago está relacionado a una factura PUE puede registrarlo con el
asistente y asociarlo a la factura correspondiente. Vaya a Contabilidad ‣
Clientes ‣ Facturas, seleccione una factura y haga clic en el botón Registrar
pago. El estado de la factura cambia a En proceso de pago, ya que el pago se
validará cuando el banco lo concilie.

Ver también

[Conciliación bancaria](../accounting/bank/reconciliation.html)

Si bien este proceso es el mismo para las facturas PPD, el tener que crear un
[documento
electrónico](../accounting/customer_invoices/electronic_invoicing.html) indica
que es necesario cumplir con algunos requisitos adicionales para poder enviar
el documento al SAT de forma correcta.

Desde una factura, es necesario que confirme la forma de pago específica donde
recibió el pago y por este motivo **no** puede establecer 99 - Por Definir en
el campo forma de pago.

Si agregará el número de cuenta bancaria a la pestaña Contabilidad en la
tarjeta de contacto de su cliente, debe ser un número válido.

Nota

Las forma de configuración exacta se encuentra en el [Anexo 20 del
SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm). Por lo
general, la cuenta bancaria debe tener 10 o 18 dígitos para las transferencias
y 16 para las tarjetas de crédito o débito.

Si un pago está relacionado con una factura firmada con `PPD` como política de
pago, Odoo genera el complemento de pago correspondiente en automático cuando
hace clic en Procesar ahora.

![Mensaje para procesar ahora el pago en el servicio de facturación CFDI
\(4.0.\).](../../../_images/mx-signed-complement.png)

Advertencia

Un pago en MXN **no** se puede utilizar para pagar varias facturas en USD. El
pago se debe separar en varios pagos, para esto use el botón Registrar pago
que se ubica en las facturas correspondientes.

#### Cancelar facturas

Es posible cancelar los documentos EDI que envió al SAT. Según la [Reforma
Fiscal 2022](https://www.sat.gob.mx/consultas/91447/nuevo-esquema-de-
cancelacion), desde el 1 de enero de 2022 existen dos requisitos para ello:

  * **Debe** especificar un _motivo de cancelación_ en todas las solicitudes de cancelación.

  * 24 horas después de la creación de la factura **debe** solicitarle al cliente que acepte la cancelación.

Hay cuatro motivos de cancelación distintos. En Odoo puede cancelar facturas
con los motivos _01 - Comprobantes emitidos con errores con relación_ y _02 -
Comprobantes emitidos con errores sin relación_.

Las siguientes secciones desglosan el proceso de cancelación de facturas para
cada motivo de cancelación en Odoo.

Importante

Odoo tiene algunas limitaciones para cancelar facturas en el SAT y, por el
momento, no es compatible con los motivos 03 y 04 (que corresponden a _No se
llevó a cabo la operación_ y _Operación nominativa relacionada en la factura
global_). Si necesita usarlos debe cancelar la factura desde el SAT y
presionar Reintentar en el campo Estado del SAT.

##### 01 - Comprobante emitido con errores con relación

Este motivo de cancelación se debe utilizar cuando necesita sustituir la
factura original con una nueva debido a un error en cualquier campo.

Vaya a Contabilidad ‣ Clientes ‣ Facturas, seleccione la factura anterior y
copie su folio fiscal. Luego, vaya a la nueva factura y en el campo Origen del
CFDI agregue el valor `04|`, pegue el folio fiscal de la factura anterior
junto a ese valor y, por último, firme el nuevo documento.

Vaya a la factura anterior, ahora aparece el campo Sustituida por. Haga clic
en el botón Solicitar la cancelación de EDI en esa factura, aparecerá una
sección azul, allí haga clic en Procesar ahora. El estado de la factura cambia
a Cancelado y la confirmación de esta acción se registra en el chatter.

La factura también debería estar cancelada en el SAT. Para confirmar que no
ocurrió ningún error presione Reintentar en el campo de estado del SAT.

Si canceló el documento luego de 24 horas después de su creación quizás deba
solicitarle al cliente que acepte la cancelación en su Buzón Tributario desde
el [sitio web del SAT](https://www.sat.gob.mx/home).

Nota

El código `04|` solo tiene la finalidad de ayudar a Odoo a realizar este
proceso y no tiene relación con el método «04 motivo de cancelación».

![Factura antigua con origen del CFDI.](../../../_images/mx-01-invoice-
cancellation-substitute.png) ![Una factura con el campo "Sustituida por"
completado con el Origen del CFDI de la
factura.](../../../_images/mx-01-invoice-cancellation.png)

##### 02 - Comprobante emitido con errores sin relación

Este motivo de cancelación debe utilizarse cuando una factura se emitió con un
error en algún campo y no debe reemplazarse con otra.

Vaya a Contabilidad ‣ Clientes ‣ Facturas y seleccione la factura anterior.
Luego solo debe hacer clic en el botón Solicitar la cancelación de EDI y
después en el botón Procesar ahora.

El campo Sustituido por no aparece al elegir este motivo de cancelación, por
lo que el SAT debe detectar de forma automática que el motivo de cancelación
es 02.

##### Cancelaciones de pago

También puede cancelar los _complementos de pago_. Vaya al pago desde
Contabilidad ‣ Clientes ‣ Pagos y seleccione Solicitar la cancelación de EDI.
Al igual que con las facturas, aparecerá un botón azul. Haga clic en Procesar
ahora, esta acción enviará el documento al SAT. Presione Reintentar luego de
unos segundos para confirmar el estado actual en el SAT.

Por último, el estado del pago se mueve a Cancelado.

Nota

Al igual que en las facturas, puede agregar la relación del documento original
al crear un nuevo _complemento de pago_ si agrega el código `04|` y el folio
fiscal al campo Origen del CFDI.

#### Facturación de casos de uso especial

##### CFDI al público

Si el cliente al que vende sus bienes o servicios no requiere una factura,
entonces debe crear un _CFDI al público_.

Ocurrirá un error si utiliza `PUBLICO EN GENERAL` como nombre del Cliente.
Este es cambio más importante para el CFDI 4.0, necesita campos adicionales
para facturas con ese nombre específico y, por el momento, Odoo no es
compatible con estos campos. Para crear un _CFDI para el público en general_
debe usar cualquier otro nombre de cliente que **no** sea `PUBLICO EN GENERAL`
(por ejemplo, puede usar `CLIENTE FINAL`).

Además de esto, es necesario que agregue el código postal de su empresa, que
use el RFC genérico `XAXX010101000` y que configure el régimen fiscal de su
cliente como `Sin obligaciones fiscales`.

![Configuración del campo CFDI al público.](../../../_images/mx-cfdi-to-
public.png)

##### Multidivisa

La moneda principal en México es el peso mexicano, MXN. Aunque su uso es
obligatorio para todas las empresas mexicanas, también es posible enviar y
recibir facturas (y pagos) en otras divisas. Para habilitar el uso de
[multidivisa](../accounting/get_started/multi_currency.html) vaya a
Contabilidad ‣ Ajustes ‣ Divisas y seleccione Banco mexicano como servicio en
la sección Tasas de cambio automáticas. Luego, en el campo Intervalo elija la
frecuencia con la que desea actualizar las tasas de cambio.

De esta manera, en el archivo XML del documento aparecerá el tipo de cambio
correcto y el importe total tanto en la divisa extranjera como en MXN.

Le recomendamos que use [una cuenta bancaria para cada
divisa](../accounting/bank/foreign_currency.html).

Nota

Las únicas divisas que actualizan su tipo de cambio a diario de forma
automática son USD, EUR, GBP y JPY.

![Configuración multidivisa en los ajustes de
Contabilidad.](../../../_images/mx-multicurrency-1.png)

##### Anticipos

Es posible que en algún caso reciba un anticipo de un cliente y que después
deba aplicarlo a una factura. Para hacer esto en Odoo, debe vincular las
facturas entre sí de forma adecuada con el campo Origen del CFDI. Es necesario
que tenga la aplicación [Ventas](../../sales.html) instalada.

Ver también

[La documentación oficial para el registro de anticipos en
México](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Caso_uso_Anticipo.pdf).

Vaya a la aplicación Ventas para crear el producto `Anticipo` y configúrelo.
El tipo de producto debe ser servicio, seleccione la categoría UNSPSC
`84111506 Servicios de facturación`.

Después, vaya a Ventas ‣ Ajustes ‣ Facturación ‣ Anticipos y agregue
_Anticipo_ como producto predeterminado.

Cree una orden de venta con el importe total y cree un anticipo (ya sea
mediante un porcentaje o un importe fijo), firme el documento y registre el
pago.

Cuando deba emitir la factura final al cliente, vuelva a crearla a partir de
la misma orden de venta. En el asistente para Crear facturas seleccione
Factura normal y desmarque Deducir anticipos.

Luego, copie el folio fiscal de la primera factura y péguelo en el origen del
CDFI de la segunda. Agregue el prefijo `07|` antes del valor y después firme
el documento.

Después, cree una nota de crédito para la primera factura. Copie el folio
fiscal de la segunda y péguelo en el campo Origen del CFDI de la nota de
crédito. Agregue el prefijo `07|` y firme el documento.

Ahora todos los documentos electrónicos están vinculados entre sí. El último
paso es pagar la nueva factura en su totalidad. En la parte inferior de la
nueva factura se encuentra la nota de crédito en la sección créditos
pendientes, agréguela como pago. Registre el importe restante con el asistente
Registrar pago.

### Comercio exterior

La factura de comercio exterior es un complemento para una factura regular que
agrega algunos valores al XML y el PDF para las facturas de un cliente
extranjero de acuerdo con los [reglamentos del
SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/complemento_comercio_exterior.htm).
Entre estos valores se encuentran:

  * La dirección específica del destinatario y el remitente.

  * La adición de una fracción arancelaria que identifica el tipo de producto.

  * El Incoterm (Términos de comercio internacional), correcto, entre otros (_certificado de origen_ y _unidades especiales de medida_).

Esto permite identificar de forma correcta a los exportadores e importadores,
además de ampliar la descripción de la mercancía vendida.

Desde el 1° de enero del 2018, el comercio externo es un requisito para
aquellos contribuyentes que realizan operaciones de exportación de tipo A1. Si
bien el CFDI actual es la versión 4.0, la versión actual del comercio externo
es la 1.1.

Para utilizar esta función, debe instalar los módulos l10n_mx_edi_extended y
l10n_mx_edi_extended_40.

Importante

Asegúrese de que su negocio necesita utilizar esta función antes de
instalarlos. Le recomendamos que primero consulte a su contador antes de
instalar cualquier modulo.

#### Configuración

##### Contactos

Para configurar el contacto de su empresa para comercio externo, vaya a
Contabilidad‣ Clientes ‣ Clientes, y seleccione su Empresa. Mientras que los
requisitos del CFDI 4.0 le piden que agregue un código postal válido a su
contacto, el complemento de comercio externo le pide que su ciudad y estado
también deben ser válidos. Todos esos campos deben coincidir con el [Catálogo
oficial del
SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/catalogos_emision_cfdi_complemento_ce.htm),
o aparecerá un error.

Advertencia

Agregue la ciudad y el estado al _contacto_ de la empresa, no a la empresa
como tal. Puede encontrar el contacto de su empresa en Contabilidad ‣ Clientes
‣ Clientes.

Los campos entidad federativa y código postal son opcionales y puede
agregarlos a la empresa directamente desde Ajustes ‣ Ajustes generales ‣
Empresas. Estos dos deben coincidir con los datos del SAT.

![Campos opcionales de comercio exterior para la
empresa.](../../../_images/mx-external-trade-rescompany.png)

Para configurar los datos de contacto de un cliente receptor extranjero, vaya
a Contabilidad ‣ Clientes‣ Clientes, y seleccione el contacto del cliente
extranjero. El contacto debe tener completos los siguientes campos para evitar
que aparezcan errores:

  1. La dirección completa de la empresa, con un código postal válido y el país extranjero.

  2. El formato del NIF (número de identificación fiscal) extranjero. Por ejemplo: Colombia `123456789-1`.

  3. En la pestaña EDI MX debe mencionar si el cliente recibe los bienes de forma temporal (Temporal) o permanente (Definitiva).

Importante

Si el nuevo contacto se creo al duplicar otro contacto existente de México,
asegúrese de eliminar cualquier información transferida del campo régimen
fiscal. Además, no debe activar la opción Sin desglose fiscal, de lo
contrario, no aparecerán campos obligatorios que son necesarios para
configurar contactos de comercio externo.

![Campos necesarios para clientes de comercio exterior.](../../../_images/mx-
external-trade-customer-contact.png)

Nota

En los archivos XML y PDF resultantes, el NIF se sustituye de manera
automática por un NIF genérico para transacciones al extranjero:
`XEXX010101000`.

##### Productos

Todos los productos relacionados con comercio exterior tienen cuatro campos
obligatorios, dos de ellos solo pertenecen a comercio externo.

  1. La referencia interna del producto se encuentra en la pestaña Información general.

  2. El peso del producto debe ser superior a `0`.

  3. La fracción arancelaria [correcta](https://www.ventanillaunica.gob.mx/vucem/Clasificador.html) del producto en la pestaña Contabilidad.

  4. UMT Aduana corresponde a la fracción arancelaria.

![Campos necesarios para los productos de comercio
exterior.](../../../_images/mx-external-trade-product.png)

Truco

  * Si el código de UdM de la fracción arancelaria es `01`, la UMT Aduana correcta es `kg`.

  * Si el código de UdM de la fracción arancelaria es `06`, la UMT Aduana correcta es `Unidades`.

#### Flujo de facturación

Antes de crear una factura, es importante tener en cuenta que para las
facturas de comercio exterior es necesario convertir el importe de su producto
a USD. Por lo tanto, **debe** tener activadas las
[multidivisas](../accounting/get_started/multi_currency.html) y _USD_ en la
sección de Divisas. El servicio correcto que debe ejecutar es :guilabel:`Banco
mexicano.

Después, con la tasa de cambio correcta configurada en Contabilidad ‣ Ajustes
‣ Divisa, los únicos campos que faltan son Incoterm y el opcional Origen del
certificado en la pestaña Otra información.

![Pestaña de otra información de un producto para comercio
exterior.](../../../_images/mx-external-trade-other-info.png)

Por último, firme la factura de la misma forma en la que firma una factura
normal y haga clic en el botón Procesar ahora.

### Guía de entrega

Una [Carta Porte](https://www.sat.gob.mx/consultas/68823/complemento-carta-
porte-) es una guía de embarque, es decir, un documento que indica el tipo,
cantidad y destino de las mercancías que se transportan.

El 1° de diciembre del 2021, se implementó la versión 2.0 de este CFDI para
todos los proveedores de transporte, intermediarios y propietarios de bienes.
Odoo puede generar un documento tipo «T» (traslado) el cual, a diferencia de
otros documentos, se crea en una orden de envío y no en una factura o pago.

Odoo puede crear archivos XML y PDF con (o sin) transporte terrestre y puede
procesar materiales etiquetados como _Peligrosos_.

Para utilizar esta función, debe instalar los módulos l10n_mx_edi_extended,
l10n_mx_edi_extended_40, l10n_mx_edi_stock and l10n_mx_edi_stock_40.

Además, debe tener instaladas las aplicaciones
[Inventario](../../inventory_and_mrp/inventory.html) y
[Ventas](../../sales/sales.html).

Importante

Odoo no es compatible con la Carta Porte tipo «I» (Ingreso), transporte
marítimo o aéreo. Consulte con su contador primero si necesita esta función
antes de hacer cualquier modificación.

#### Configuración

Odoo maneja dos tipos diferentes de CFDI:

  * **No excede el tramo de carretera federal** : se usa cuando la _distancia hacia el destino_ es [menos de 30km](http://omawww.sat.gob.mx/cartaporte/Paginas/documentos/PreguntasFrecuentes_Autotransporte.pdf).

  * **Transporte por carretera federal** : se usa cuando la _distancia hacia el destino_ excede los 30km.

Además de los requisitos estándar de una factura normal (el RFC del cliente,
el código UNSPSC, etc.) no es necesario ningún otro ajuste si utiliza _No
excede el tramo de carretera federal_.

Por otro lado, para _Transporte por carretera federal_ , necesita una
configuración adicional para los contactos, los vehículos y los productos.
Esta configuración se agrega en los archivos XML y PDF.

##### Contactos y vehículos

Así como con la función de comercio exterior, la dirección de su empresa y la
de su cliente final debe estar completa. El código postal, la ciudad y el
estado deben coincidir con el [Catálogo Oficial del
SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/catalogos_emision_cfdi_complemento_ce.htm)

Truco

El campo entidad federativa es opcional para ambas direcciones.

![Configuración de la guía de entrega del producto.](../../../_images/mx-
delivery-guide-contacts.png)

Importante

La dirección de origen que se usa para la guía de entrega se configura en
Inventario ‣ Configuración ‣ Gestión de almacenes ‣ Almacenes. Aunque se
establece como la dirección de la empresa predeterminada, la puede cambiar de
acuerdo a la dirección correcta del almacén.

Otra adición a esta función es el menú Configuración del vehículo en
Inventario ‣ Ajustes ‣ México. Este menú le permite agregar toda la
información relacionada al vehículo que usa la orden de envío.

Es obligatorio que complete todos los campos para crear una guía de entrega
completa.

Truco

Los campos Número de placa vehicular and Número de placa, deben contener entre
5 y 7 caracteres.

En la sección Intermediarios debe agregar al operador del vehículo. Los únicos
campos obligatorios para este contacto son el NIF y Licencia de operador.

![Configuración de la guía de entrega del producto.](../../../_images/mx-
delivery-guide-vehicle.png)

##### Productos

Como con cualquier otra factura normal, todos los productos deben tener una
categoría UNSPSC. Además, hay dos ajustes adicionales para los productos que
se incluyen en las guías de entrega:

  * El Tipo de producto debe estar establecido como Producto almacenable para los movimientos de existencias que se creen.

  * En la pestaña de Inventario, el campo Peso debe ser de más de `0`.

Advertencia

Si crea una guía de entrega para un producto con valor `0` se activará un
error. Como el Peso ya se guardó en la orden de entrega, es necesario para
regresar los productos y para crear la orden de entrega (y guía de entrega) de
nuevo con las cantidades correctas.

![Configuración de la guía de entrega del producto.](../../../_images/mx-
delivery-guide-products.png)

#### Flujo de ventas e inventario

Para crear una guía de entrega, primero tiene que crear y confirmar una orden
de venta desde Ventas ‣ Orden de venta. Esto genera un botón inteligente
Entrega en el que puede hacer clic y después Validar la transferencia.

Después de que el estado se cambia a Hecho, podrá editar la transferencia y
seleccionar el Tipo de transporte (ya sea No excede el tramo de carretera
federal o Transporte por carretera federal).

Si su envío tiene el tipo No excede el tramo de carretera federal, puede
guardar la transferencia y hacer clic en Generar guía de entrega. Puede
encontrar el archivo XML que se genera en el chatter.

Nota

Además del código UNSPSC en todos los productos, las guías de entrega que usan
el tipo No excede el tramo de carretera federal, no necesitan otros ajustes
especiales que deba enviar al gobierno.

Si su guía de entregan es del tipo Transporte por carretera federal, aparecerá
la pestaña MX EDI. Ahí deberá ingresar un valor en Distancia hacia el destino
(KM) que sea mayor a `0`, y debe seleccionar la Configuración del vehículo que
se usará para ese envío.

![Pestaña de configuración MX EDI para la guía de
entrega.](../../../_images/mx-delivery-guide-federal-transport.png)

##### Materiales peligrosos

Algunos valores dentro de las categorías UNSPSC se consideran _peligrosos_ de
acuerdo al [catálogo oficial del
SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/complemento_carta_porte.htm).
Estas categorías necesitan consideraciones adicionales al momento de crear una
guía de envío tipo Transporte por carretera federal.

Primero, seleccione el formulario de su producto Inventario ‣ Productos ‣
Productos. Después, en la pestaña de Contabilidad debe llenar los campos
Hazardous Material Designation Code (MX) y Hazardous Packaging (MX) se deben
llenar con la clave correcta del catálogo del SAT.

![Campos necesarios para la guía de entrega para materiales peligrosos
](../../../_images/mx-delivery-guide-hazards-designation.png)

En Inventario ‣ Ajustes ‣ México ‣ Configuración de vehículo debe llenar la
información de la Aseguradora medioambiental y la Póliza de seguro
medioambiental también. Después de esto, continue con el proceso regular para
crear una guía de entrega.

![Campos obligatorios medioambientales en la guía de
envío.](../../../_images/mx-delivery-guide-hazards-environment.png)

### Números de pedimento

Un pedimento aduanero es un documento fiscal que certifica que todas las
contribuciones al SAT se pagaron por la importación/exportación de bienes.

De acuerdo con el [Anexo
20](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm) del CFDI
4.0, los documentos en donde los bienes facturados vienen de una operación de
importación de primera mano, deben tener un Número de pedimento en todas las
líneas de producto involucradas en la operación.

Para esto debe instalar el módulo l10n_mx_edi_landing, así como las
aplicaciones [Inventario](../../inventory_and_mrp/inventory.html),
[Compra](../../inventory_and_mrp/purchase.html) y
[Ventas](../../sales/sales.html).

Importante

No debe confundir esta función con comercio externo. Los números de pedimento
están directamente relacionados con la importación de bienes, mientras que el
comercio externo está relacionado con las exportaciones. Consulte con su
contador primero si necesita esta función antes de hacer cualquier
modificación.

#### Configuración

Para rastrear el número de pedimento correcto para una factura en específico
Odoo utiliza los [costes en
destino](../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs.html).
Vaya a Inventario ‣ Configuración ‣ Ajustes ‣ Valoración. Asegúrese de que la
opción Costes en destino esté activada.

Primero, debe crear un producto de tipo _servicio_ que se llame `Pedimento`.
En la pestaña Compra, seleccione la casilla Es un coste en destino y
seleccione un Método de división predeterminado.

Después, configure todos los _producto almacenables_ que tengan los números de
pedimento. Para hacerlo, cree productos almacenables y asegúrese de que la
categoría del producto tenga la siguiente configuración:

  * Método de coste: debe ser FIFO o AVCO

  * Valoración del inventario: Automático

  * Cuenta de la valoración de las existencias: 115.01.01 Inventario

  * Diario de las existencias: Valoración del inventario

  * Cuenta de entrada de las existencias: 115.05.01 Mercancías en tránsito

  * Cuenta de salida de las existencias: 115.05.01 Mercancías en tránsito

![Configuración general de los productos almacenables. ](../../../_images/mx-
landing-configuration.png) ![Configuración de la categoría de los productos
almacenables.](../../../_images/mx-landing-configuration-category.png)

#### Flujo de compra y ventas

Después de configurar su producto, siga el [flujo de
compra](../../inventory_and_mrp/purchase.html) estándar.

Cree una orden de compra desde Compra ‣ Órdenes ‣ Órdenes de compra. Después,
confirme la orden para mostrar el botón inteligente de Recepción para Validar
la recepción del envío.

Vaya a Inventario ‣ Operaciones ‣ Costes en destino y cree un nuevo registro.
Agregue la transferencia que acaba de crear y el producto de `Pedimento` y
Número de pedimento.

De manera opcional, puede agregar un importe de coste. Después, valide el
coste en destino. Una vez Publicado, todos los productos relacionados con esa
recepción tendrán el número de pedimento asignado.

Advertencia

Solo puede agregar un número de _pedimentos_ **a la vez** , así que tenga
cuidado al asociar el número correcto con las transferencias (o
transferencia).

![Número de pedimento en costos de destino en el registro de
inventario.](../../../_images/mx-landing-inventory.png)

Ahora cree una orden de ventas y confírmela. Deberá aparecer un botón
inteligente de Envío. Haga clic en validar.

FInalmente, cree una factura desde la orden de ventas y confírmela. La línea
de factura relacionada a su producto tendrá un número de pedimento en ella.
Este número debe ser acorde con el número de pedimento en el registro _Costos
de destino_ que creó antes.

![Número de pedimento en un producto de una orden de venta confirmada.
](../../../_images/mx-landing-invoice.png)

### Contabilidad electrónica

En Mexico, la [contabilidad
electrónica](https://www.sat.gob.mx/aplicacion/42150/envia-tu-contabilidad-
electronica) se refiere a la obligación de llevar los registros y asientos
contables a través de medios electrónicos y de ingresar mensualmente la
información contable en el sitio web del SAT.

Consta de tres archivos XML principales:

  1. La lista actualizada del plan de cuentas que usa actualmente.

  2. Un balance general mensual, además de un reporte de asiento de cierre conocido como _Balanza de comprobación 13_

  3. Una exportación de los asientos en su libro mayor, ya sea de manera opcional o para una auditoría obligatoria.

El archivo XML que se genera cumple con los requisitos del [Anexo Técnico de
Contabilidad Electrónica
1.3](https://www.gob.mx/cms/uploads/attachment/file/151135/Anexo24_05012015.pdf).

Además, puede generar el archivo
[DIOT](https://www.sat.gob.mx/declaracion/74295/presenta-tu-declaracion-
informativa-de-operaciones-con-terceros-\(diot\)-): un reporte de los asientos
del diario de proveedores que incluye el IVA que se puede exportar en un
archivo `.txt`.

Para usar estos reportes, necesita instalar los módulos l10n_mx_reports,
l10n_mx_reports_closing, l10n_mx_xml_polizas and l10n_mx_xml_polizas_edi, así
como la aplicación [Contabilidad](../accounting/get_started.html).

Puede rencontrar el _Plan de cuentas_ , _Balanza de comprobación 13_ y
reportes _DIOT_ en Accounting ‣ Reporting ‣ Mexico.

Importante

Las características y obligaciones específicas de los reportes que envíe
pueden cambiar de acuerdo a su régimen fiscal. Consulte a su contador antes de
enviar cualquier documento al gobierno.

#### Plan de cuentas

El [plan de cuentas](../accounting/get_started/chart_of_accounts.html) de
México tiene un patrón específico basado en el [Código agrupador de
cuentas](http://omawww.sat.gob.mx/fichas_tematicas/buzon_tributario/Documents/codigo_agrupador.pdf)
del SAT.

Puede crear cualquier cuenta siempre y cuando respete el formato de clave del
SAT. El formato es `NNN.YY.ZZ` o `NNN.YY.ZZZ`.

Example

Algunos ejemplos son `102.01.99` o `401.01.001`.

Cuando crea un nueva cuenta en Contabilidad ‣ Configuración ‣ Plan de cuentas,
con el patrón de codificación de grupo del SAT, el código de agrupación
correcto aparecerá en las Etiquetas y su cuenta aparecerá en el reporte _COA_.

Una vez que ha creado todas sus cuentas asegúrese de agregar las Etiquetas
correctas.

Nota

No puede usar un formato que termine una sección con 0 (por ejemplo,
`100.01.01`, `301.00.003` o `604.77.00`). Esto causará errores en el reporte.

Una vez que haya configurado todo, puede ir a Contabilidad ‣ Reportes ‣ México
‣ COA

#### Balanza de comprobación

La balanza de comprobación es un reporte del balance inicial, el crédito y el
balance total de sus cuentas que se genera si agrega correctamente su grupo de
codificación.

Este reporte se puede generar mensualmente y puede crear una versión en
archivo XML si va a Contabilidad ‣ Reportes ‣ México ‣ Balanza de comprobación
y hace clic en el botón SAT (XML). Seleccione el mes que desea descargar con
antelación.

![Reporte de la comprobación del balance.](../../../_images/mx-reports-trial-
balance.png)

Nota

Odoo no genera la _Balanza de Comprobación Complementaria_.

Otro reporte adicional es el de _Mes 13_. Se trata de una hoja de balance de
cierre que muestra cualquier ajuste o movimiento que se haya hecho en
contabilidad para cerrar el año fiscal.

Para generar este documento XML, va a Contabilidad ‣ Contabilidad ‣ Varios ‣
Asiento contables y cree un documento nuevo. Aquí agrege todas las cantidades
a modificar y puede saldar el deber o el haber de cada uno.

Una vez hecho esto, haga clic en Marcar como asiento de cierre. El reporte que
se encuentra en Contabilidad ‣ Reportes ‣ México ‣ Balanza de comprobación 13
contiene el importe total del año además de todas las adiciones de los
asientos contables.

Haga clic en el botón SAT (XML) para generar el archivo XML.

![Configuración del la balanza de comprobación 13.  ](../../../_images/mx-
reports-trial-balance-13.png) ![Reporte de la balanza de comprobación
13.](../../../_images/mx-reports-trial-balance-13-report.png)

#### Libro mayor

Por ley, todas las transacciones en México se deben registrar de manera
digital. Puesto que Odoo crea automáticamente todos los asientos contables
subyacentes de sus facturas y pagos, puede exportar sus asientos para cumplir
con las auditorías del SAT o las devoluciones de impuestos.

Truco

Puede aplicar filtros por periodo o diarios de acuerdo con sus necesidades.

Pra crear el XML vaya a Contabilidad ‣ Reportes ‣ Reportes de auditoría ‣
Libro mayor general y haga clic en XML (Polizas). Aquí puede seleccionar entre
cuatro tipos de Exportación:

  * Auditoría de impuestos

  * Certificación de auditoría

  * Devolución de bienes

  * Compensación

Para Auditoría fiscal o Certificación de auditoría necesita escribir el Número
de orden que le proporciona el SAT. Para la Devolución de bienes o para
Compensación, debe escribir el Número de proceso que también le proporciona el
SAT.

Nota

Si desea ver este reporte sin enviarlo, utilice `ABC6987654/99` para el campo
Número de orden y `AB123451234512` para Número de proceso.

#### Reporte DIOT

El reporte DIOT (Declaración Informativa de Operaciones con Terceros) es una
obligación adicional con el SAT donde se proporciona el estado actual de los
pagos acreditables y no acreditables, retenciones y devoluciones de IVA de sus
facturas de proveedor se envían al SAT.

A diferencia de otros reportes, el DIOT se sube a un software que proporciona
el SAT y que contiene el formulario A-29. En Odoo, puede descargar los
registros de sus transacciones en un archivo tipo `.txt` que puede subir al
formulario y así evita capturar directamente estos datos.

El archivo de transacciones contiene el importe total de sus pagos registrados
en las facturas de proveedor desglosados en los tipos correspondientes de IVA.
Los campos NIIF y País son obligatorios para todos los proveedores.

Para generar el DIOT, vaya a Contabilidad ‣ Reportes ‣ México ‣ Transacciones
con terceros [DIOT]. Seleccione el mes que desee y haga clic en DIOT (TXT)
para descargar el archivo `.txt`.

![Una factura de proveedor se está pagando.](../../../_images/mx-reports-diot-
example.png) ![Botón para descargar el DIOT \(TXT\)](../../../_images/mx-
reports-diot-example-download.png)

Importante

Debe completar el campo Tipo de operación L10N Mx en la pestaña de
Contabilidad de cada uno de sus proveedores para prevenir errores de
validación. Asegúrese de que sus clientes extranjeros tengan su configuración
establecida correctamente para que aparezca automáticamente la Nacionalidad
L10N Mx.

![Información del DIOT en el contacto del proveedor.](../../../_images/mx-
reports-diot-contact.png)

  *[SAT]: Servicio de Administración Tributaria
  *[DIOT]: Declaración Informativa de Operaciones con Terceros
  *[RFC]: Registro Federal de Contribuyentes
  *[PAC]: Proveedor Autorizado de Certificación / Authorized Certification Provider
  *[PUE]: Pago en una Sola Exhibición/Payment in a Single Exhibition
  *[PPD]: Pago en Parcialidades o Diferido/Payment in Installements or Deferred

