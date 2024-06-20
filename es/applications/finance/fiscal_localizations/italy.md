# Italia

## Configuración

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Italia:

Nombre | Nombre técnico | Descripción  
---|---|---  
Italia - Contabilidad | `l10n_it` | [Paquete de localización fiscal](../fiscal_localizations.html#fiscal-localizations-packages) predeterminado  
Italia - Facturación electrónica | `l10n_it_edi` | Implementación de la factura electrónica  
Italia - Facturación electrónica | `l10n_it_edi_withholding` | Retención de la factura electrónica  
Italia - Reportes contables | `l10n_it_reports` | Reportes específicos del país  
Italia - DDT de existencias | `l10n_it_stock_ddt` | Documentos de transporte - Documento di Trasporto (DDT)  
![Módulos de localización italianos](../../../_images/italy-modules.png)

### Información de la empresa

Configurar la información de la empresa garantiza que su base de datos de
Contabilidad esté configurada de forma correcta. Para agregar información,
vaya a Ajustes ‣ Ajustes generales, y en la sección Empresas haga clic en
Actualizar información. Complete los siguientes campos:

  * Dirección: la dirección de la empresa.

  * NIF: NIF de la empresa.

  * Código fiscal: el código fiscal de la empresa.

  * Sistema tributario: el sistema tributario bajo el que se encuentra la empresa.

![Información de la empresa a proporcionar](../../../_images/italy-
company.png)

### Facturación electrónica

El SdI es el sistema de facturación electrónica que se utiliza en Italia.
Permite enviar y recibir facturas electrónicas a y de los clientes. Los
documentos deben estar en formato XML y el sistema debe validarlos formalmente
antes de entregarlos.

Para poder recibir facturas y notificaciones, debe notificar al servicio del
SdI sobre el envío de los archivos del usuario a **Odoo** y que deben
procesarse en su nombre. Para ello, debe configurar el Codice Destinatario en
el portal de la **Agenzia Delle Entrate**.

  1. Vaya a <https://ivaservizi.agenziaentrate.gov.it/portale/> y autentifíquese.

  2. Vaya a la sección Fatture e Corrispettivi.

  3. Configure el usuario como Parte Legal para el número de NIF que desea configurar a la dirección electrónica.

  4. Vaya a Servizi Disponibili ‣ Fatturazione Elettronica ‣ Registrazione dell’indirizzo telematico dove ricevere tutte le fatture elettroniche, escriba el Codice Destinatario `K95IV18` de Odoo y confirme.

#### Intercambio electrónico de datos (EDI)

Odoo utiliza el formato EDI de **FatturaPA** para la localización italiana y
está habilitado en los diarios de forma predeterminada cuando se instala.
Cuando se ha configurado la **autorización para el procesamiento de archivos**
, las **facturas** se envían en automático.

Nota

Puede [habilitar la facturación electrónica para otros diarios de ventas y
compras](../accounting/customer_invoices/electronic_invoicing.html#e-invoicing-
configuration) que no son los predeterminados.

Puede verificar el estado actual de una factura en el campo factura
electrónica. El archivo XML se encuentra en el **chatter** de la factura.

![Estado de facturación electrónica \(en espera de
confirmación\)](../../../_images/italy-test.png)

Ver también

[Facturación electrónica
(EDI)](../accounting/customer_invoices/electronic_invoicing.html)

### Autorización para el procesamiento de archivos (Odoo)

Debido a que los archivos se transmiten a través del servidor de Odoo antes de
ser enviados al SdI o recibidos por su base de datos, debe autorizar que Odoo
procese sus archivos desde su base de datos. Vaya a Contabilidad ‣
Configuración ‣ Ajustes ‣ Facturación de documentos electrónicos.

Hay **tres** modos disponibles:

Demo

    

Este modo simula un entorno en el que las facturas se envían al gobierno. En
este modo, las facturas se deben descargar _de manera manual_ como archivos
XML y cargar en el sitio web de la **Agenzia delle Entrate**.

Prueba (experimental)

    

Este modo envía las facturas a un servicio que no es de producción (es decir,
de prueba) facilitado por la **Agenzia delle Entrate**. Guardar este cambio
hace que todas las empresas en la base de datos utilicen esta configuración.

Oficial

    

Este es un modo de producción que envía sus facturas directamente a la
**Agenzia delle Entrate**.

Una vez que seleccionó un modo, debe aceptar los **términos y condiciones**.
Marque la casilla Permitir que Odoo procese las facturas y después haga clic
en Guardar, ahora puede registrar sus transacciones en Contabilidad de Odoo.

Advertencia

**No puede revertir** la selección de Prueba (experimental) u Oficial. Una vez
que se encuentra en el modo Oficial no puede seleccionar Prueba (experimental)
o Demo, lo mismo sucede con Prueba (experimental). Le recomendamos crear una
base de datos separada solo con fines de prueba.

Nota

Cuando el modo Prueba (experimental) está activo, todas las facturas enviadas
_deben_ tener un contacto que utilice uno de los siguientes Codice
Destinatario falsos proporcionados por la **Agenzia Delle Entrate** :
`0803HR0` \- `N8MIMM9` \- `X9XX79Z`. Cualquier Codice Destinario de producción
real perteneciente a sus clientes no será reconocido como válido por el
servicio de prueba.

![Opciones de facturación de documentos electrónicos de
Italia](../../../_images/italy-edi.png)

## Configuración de impuestos

Muchas de las funciones de facturación electrónica se implementan mediante el
sistema tributario de Odoo, por lo que es muy importante que los impuestos se
configuren de manera adecuada para generar las facturas de forma correcta y
poder gestionar otros casos de uso de facturación. Por ejemplo, se necesitan
configuraciones específicas para el tipo de impuestos de **cobro revertido**.
En ese caso, el vendedor _no_ le cobra el IVA al cliente, sino que el cliente
le paga el IVA al gobierno _por su cuenta_. Hay **dos** tipos principales:

  * cobro revertido externo;

  * cobro revertido interno.

### Cobro revertido externo

#### Facturas

Para realizar una factura de exportación, asegúrese de que todas las líneas de
factura utilicen un impuesto configurado para **cobro revertido**. La
localización **italiana** contiene un **ejemplo** de un impuesto de cobro
revertido para la exportación en la UE que se utilizará como referencia (`0%
UE`, etiqueta de factura `00eu`), está disponible en Contabilidad ‣
Configuración ‣ Impuestos. Las exportaciones están exentas del IVA, por lo que
los impuestos de **cobro revertido** requieren la opción Tiene exoneración de
impuestos (Italia) marcada, junto a las opciones de tipo de exoneración y
Referencia legal completadas.

![Ajustes de cobro revertido externo](../../../_images/italy-tax.png)

Nota

Si necesita usar un tipo distinto de exoneración, haga clic en Acción ‣
Duplicar dentro del menú de impuestos para crear una copia de un impuesto
similar existente. Después, seleccione otra exoneración y haga clic en
Guardar. Repita este proceso tantas veces según necesite diferentes tipos de
Exoneración de impuestos.

Truco

**Renombre** sus impuestos en el campo Nombre según su exoneración para
diferenciarlos con facilidad.

En su factura, seleccione el impuesto correspondiente que necesita en el campo
Impuestos. Puede encontrar la siguiente **información adicional** al abrir el
archivo **XML** de la factura emitida:

  * Dirección del SdI (Codice Destinatario): este campo se debe completar si pertenece a la **UE** y también si **no pertenece a la UE**.

  * ID del país: debe contener el país del vendedor extranjero en el código ISO de dos letras (Alfa-2) (por ejemplo, `IT` para «Italia»).

  * CAP: debe completar este campo con `00000`.

  * Partita Iva (**NIF**): debe contener el **NIF** para las **empresas en la UE** y `OO99999999999` (dos **letras** “O”, no “cero”) para las **empresas que no están en la UE**. En el caso de clientes privados sin **NIF** utilice `0000000`.

  * Código fiscal: para entidades extranjeras sin un **Codice Fiscale** cualquier identificador reconocible es válido.

Nota

Odoo no admite el envío de archivos XML modificados por el usuario.

Para las **facturas** , varias configuraciones están técnicamente
identificadas por un código Tipo Documento:

  * `TD02` \- Anticipos;

  * `TDO7` \- Factura simplificada;

  * `TD08` \- Nota de crédito simplificada;

  * `TD09` \- Nota de débito simplificada;

  * `TD24` \- Factura diferida.

`TD02``TD07`, `TD08`, and `TD09``TD24`

> Anticipos.
>
> Las facturas de **anticipos** se importan o exportan con un código `TDO2` de
> Tipo Documento distinto a las facturas regulares. Al importar la factura, se
> crea una factura de vendedor regular.
>
> Odoo exporta los movimientos como `TD02` si se cumplen las siguientes
> condiciones:

  * Es una factura,

  * Todas las líneas de la factura están relacionadas con las **líneas de órdenes de venta** que tienen el indicador `is_downpayment` establecido como `True`.

Facturas simplificadas y notas de crédito y débito.

Las facturas simplificadas y las notas de crédito se pueden utilizar para
certificar **transacciones nacionales** menores a **400 euros** (IVA
incluido). Su estado es el mismo que el de una factura normal, pero con menos
requisitos de información.

Para establecer una factura **simplificada** , debe incluir los siguientes
datos:

  * Referencia de la factura del cliente: secuencia de numeración **única sin espacios** ;

  * Fecha de la factura: **fecha** de emisión de la factura;

  * Información de la empresa: las credenciales completas del **vendedor** (NIF/TIN, nombre, dirección completa) en Ajustes generales ‣ Empresas (sección);

  * NIF: el NIF/TIN del **comprador** (en su tarjeta de perfil);

  * Total: el **importe** total (con IVA incluido) de la factura.

In the EDI, Odoo exporta facturas de forma simplificada si:

  * Es una transacción **nacional** (es decir, el contacto es de Italia);

  * Los datos del comprador son **insuficientes** para crear una factura ordinaria;

  * Se proporcionan los **campos obligatorios** para una factura ordinaria (dirección, código postal, ciudad, país);

  * El importe total con IVA incluido es **menor** a **400 euros**.

Nota

El límite de 400 euros se definió en [el decreto del 10 de mayo de 2019 de la
Gazzetta
Ufficiale](https://www.gazzettaufficiale.it/eli/id/2019/05/24/19A03271/sg).
Recomendamos que verifique el valor oficial actual.

Facturas diferidas.

La **factura diferida** es una factura **emitida después** de la venta de
bienes o la prestación de servicios. Una **factura diferida** deberá emitirse
a más tardar el **quinceavo día** del mes siguiente a la entrega cubierta por
el documento.

Suele ser una **factura recapitulativa** que incluye una lista de varias
ventas de bienes o servicios realizadas en el mes. La empresa puede
**agrupar** las ventas en **una factura** y por lo general se emite al **final
del mes** a efectos contables. Las facturas diferidas son, de forma
predeterminada, para el **distribuidor** que tiene clientes recurrentes.

Si un **transportista** se encarga del traslado de los bienes, cada entrega
tiene un **Documento di Transporto (DDT)** o **documento de transporte**. La
factura diferida **debe** indicar los detalles de toda la información del
**DDT** para tener un mejor seguimiento.

Nota

La facturación electrónica de las facturas diferidas necesita del módulo
`l10n_it_stock_ddt` . En este caso, se utiliza el Tipo Documento específico
`TD24` para la factura electrónica.

Odoo exporta los movimientos como `TD24` si se cumplen las siguientes
condiciones:

  * Es una factura,

  * Está asociada a entregas cuyos **DDT** tienen una fecha **distinta** a la fecha de emisión de la factura.

#### Facturas de proveedor

Las empresas italianas que compren bienes o servicios de países de la UE (o
servicios de países que no pertenecen a la UE) deben enviar la información
incluida en la factura recibida a la **Agenzia delle Entrate**. De esta forma
podrá completar la información relacionada con los impuestos en su factura y
enviarla. Se debe colocar al vendedor como Cedente/Prestatore y al comprador
como Cessionario/Committente. En el documento **XML** de la factura del
vendedor, las credenciales del vendedor se aparecen como Cedente/Prestatore y
las credenciales de su empresa como Cessionario/Committente.

Nota

Las autofacturas o las integraciones de facturas con IVA se deben emitir y
enviar a la agencia tributaria.

Al ingresar los impuestos en una factura de proveedor puede seleccionar los de
**cobro revertido** , estos se activan de forma automática en la posición
fiscal italiana. Vaya a Contabilidad ‣ Configuración ‣ Impuestos, los ámbitos
fiscales de bienes y servicios del `10%` y `22%` deben estar activados y
preconfigurados con las tablas de impuestos correctas. También se configura en
automático para garantizar el registro de los asientos contables y la
visualización del reporte de impuestos.

Para las **facturas de proveedor** , hay **tres** tipos de configuración que
se identifican técnicamente mediante un código conocido como Tipo Documento:

  * `TD17` \- Compra de servicios a países de la **UE** y que **no pertenecen a la UE** ;

  * `TD18` \- Compra de **bienes** de la **UE** ;

  * `TD19` \- Compra de **bienes** a un proveedor **extranjero** , pero los **bienes** se encuentran en **Italia** en un **almacén donde se aprovisionan sin estar sujetos al IVA**.

`TD17``TD18``TD19`

> Compra de **servicios** a países de la **UE** y que **no pertenecen a la
> UE** :
>
> El _vendedor_ extranjero factura un servicio con un precio **sin IVA** ya
> que no es imponible en el país. El IVA lo paga el _comprador_ en Italia;
>
>   * Dentro de la UE: el _comprador_ integra la factura recibida con la
> **información IVA** que se debe presentar en Italia (es decir, **integración
> fiscal de la factura del proveedor**);
>
>   * Fuera de la UE: el _comprador_ se envía a sí mismo la factura (es decir,
> se **autofactura**).
>
>

>
> Odoo exporta la transacción como `TD17` si se cumplen las siguientes
> condiciones:
>
>   * Es una factura de proveedor;
>
>   * Al menos un impuesto en las líneas de la factura está dirigido a las
> tablas de impuestos VJ;
>
>   * Todas las líneas de la factura tienen servicios como **productos** o un
> impuesto con servicios como **ámbito del impuesto**.
>
>

Compra de **bienes** de la **UE** :

Las facturas emitidas en la UE cumplen con un **formato estándar** , por lo
que solo se requiere una integración de la factura existente.

Odoo exporta la transacción como `TD18` si se cumplen las siguientes
condiciones:

  * Es una factura de proveedor;

  * Al menos un impuesto en las líneas de la factura está dirigido a las tablas de impuestos VJ;

  * Todas las líneas de la factura tienen consumibles como **productos** o un impuesto con bienes como **ámbito del impuesto**.

Compra de **bienes** a un proveedor **extranjero** , pero los **bienes** se
encuentran en **Italia** en un **almacén donde se aprovisionan sin estar
sujetos al IVA** :

  * De la UE: el _comprador_ integra la factura recibida con la **información IVA** que se debe presentar en Italia (es decir, **integración fiscal de la factura del proveedor**);

  * Fuera de la UE: el _comprador_ se envía a sí mismo la factura (es decir, se **autofactura**).

Odoo exporta el movimiento como `TD19` si se cumplen las siguientes
condiciones:

  * Es una factura de proveedor;

  * Al menos un impuesto en las líneas de la factura está dirigido a la tabla de impuestos VJ3;

  * Todas las líneas de la factura tienen productos consumibles o un impuesto con bienes como **ámbito del impuesto**.

Advertencia

Odoo no ofrece los requisitos de la [Conservazione
Sostitutiva](https://www.agid.gov.it/index.php/it/piattaforme/conservazione).
Otros proveedores y la **Agenzia delle Entrate** suministran almacenamiento
gratuito y certificado para cumplir con las condiciones solicitadas.

### Cobro revertido interno

Advertencia

Por el momento, Odoo no es compatible con los procesos nacionales de **cobro
revertido interno**.

### Tablas de impuestos de “cobro revertido”

La localización italiana tiene una sección específica de **tablas de
impuestos** para los de **cobro revertido** y se pueden identificar mediante
la etiqueta VJ. Están disponibles en Contabilidad ‣ Reportes ‣ Reportes de
auditoría: Reporte de impuestos.

![Tablas italianas de impuestos de cobro revertido](../../../_images/italy-
grids.png)

## San Marino

### Facturas

San Marino e Italia tienen acuerdos especiales con respecto a las operaciones
de facturación electrónica. Las **facturas** siguen las reglas habituales de
**cobro revertido**. Odoo no aplica los requisitos adicionales, sin embargo,
el **Estado** le pide al usuario que:

  * Seleccione un impuesto con la opción Tiene exoneración de impuestos (Italia) marcada y la exoneración establecida como `N3.3`.

  * Utilice el Codice Destinatario `2R4GT08` en el SdI. Después, una oficina especializada en San Marino la envía a la empresa correspondiente.

### Facturas

Cualquier empresa italiana **debe** presentar las **facturas no electrónicas**
que recibe de San Marino a la **Agenzia delle Entrate**. Además, debe indicar
el valor especial `TD28` en el campo Tipo Documento de la factura electrónica.

`TD28`

Odoo exporta el movimiento como `TD28` si se cumplen las siguientes
condiciones:

  * Es una factura de proveedor;

  * Al menos un impuesto en las líneas de la factura está dirigido a las tablas de impuestos VJ;

  * El **país** del contacto es **San Marino**.

## Pubblica amministrazione (B2G)

Advertencia

Odoo **no** envía facturas directamente al gobierno, pues estas deben
firmarse. Si observamos que el codice destinatario es de 6 dígitos, entonces
no se envía a la PA de manera automática, pero puede descargar el XML,
firmarlo con un programa externo y enviarlo a través del portal.

### Firma digital calificada

Para las facturas destinadas a la **Pubblica Amministrazione (B2G)** , se
necesita una **firma electrónica calificada** para todos los archivos enviados
a través del SdI. El archivo **XML** debe certificarse mediante alguna de las
siguientes opciones:

  * una **tarjeta inteligente** ;

  * un **token USB** ;

  * un **módulo de seguridad de hardware** (HSM, por sus siglas en inglés).

### CIG, CUP, DatiOrdineAcquisto

Para garantizar el seguimiento correcto de los pagos de las administraciones
públicas, las facturas electrónicas que se les expiden deben contener:

  * El CIG, exceptuando los casos de exclusión de las obligaciones de seguimiento previstas por la Ley número 136 del 13 de agosto de 2010;

  * El CUP en el caso de las facturas relacionadas con obras públicas.

Si el archivo **XML** lo requiere, la **Agenzia Delle Entrate** _solo_ puede
realizar pagos de facturas electrónicas cuando el archivo **XML** contiene un
CIG y un CUP. Para cada factura electrónica, es **necesario** indicar el CUU,
que representa el código identificador único que permite al SdI entregar
correctamente la factura electrónica a la oficina receptora.

Nota

  * El CUP y el CIG deben incluirse en uno de los bloques de información **2.1.2** (DatiOrdineAcquisto), **2.1.3** (Dati Contratto), **2.1.4** (DatiConvenzione), **2.1.5** (Date Ricezione) o **2.1.6** (Dati Fatture Collegate). Estos corresponden a los elementos CodiceCUP y CodiceCIG del archivo **XML** de la factura electrónica, puede consultar su tabla en el [sitio web](http://www.fatturapa.gov.it/) del gobierno.

  * El CUU debe incluirse en la factura electrónica correspondiente al elemento **1.1.4** (Codice Destinario).

  *[SdI]: Sistema di Interscambio
  *[EDI]: Intercambio electrónico de datos
  *[CIG]: Codice Identificativo Gara
  *[CUP]: Codice Unico di Progetto
  *[CUU]: Codice Univoco Ufficio

