# Francia

## FEC - Fichier des Écritures Comptables

Un archivo de auditoría FEC Fichier des Écritures Comptables contiene todos
los datos contables y los asientos registrados en todos los diarios contables
de un año fiscal. Las entradas en el archivo deben organizarse en orden
cronológico.

A partir del primero de enero de 2014 todas las empresas francesas deben
producir y transmitir este archivo cuando las autoridades fiduciarias lo
soliciten para fines de auditoría.

### Importar FEC

Para que la integración de nuevos usuarios sea más fácil, el [paquete de
localización fiscal](../fiscal_localizations#fiscal-localizations-
packages) para Francia de Konvergo ERP Enterprise incluye la función **Importar FEC**
(nombre técnico: `l10n_fr_fec_import`), la cual permite importar archivos FEC
existentes desde un software antiguo.

Para habilitar esta función vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣
Importar contabilidad, active **Importar FEC** y haga clic en _guardar_.

Después, vaya a Contabilidad ‣ Configuración ‣ Importar FEC, suba el archivo
FEC y haga clic en _Importar_.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><div class="line-block">
<div class="line">No hay una acción o cálculo particular para importar archivos FEC de un año diferente.</div>
<div class="line">Si varios archivos contienen «Reports à Nouveaux» (RAN) con el balance inicial del año, puede que tenga que cancelar los asientos en la interfaz del usuario. Los asientos (RAN) no son útiles en Konvergo ERP.</div>
</div>
</div>

#### Formatos de archivo

Los archivos FEC solo pueden estar en formato CSV, ya que no son compatibles
con el formato XML.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>

Se espera que los archivos que se suban al módulo cumplan con las siguientes
especificaciones técnicas:

  * **Codificación** : UTF-8, UTF-8-SIG e iso8859_15.

  * **Separador** : puede ser `;`, `|`, `,` o `TAB`.

  * **Para terminar una línea** : tanto CR+LF (`\r\n`) como LF (`\n`) son compatibles.

  * **Formato de fecha** : `%Y%m%d`

#### Descripción y uso de los campos

# | Nombre del campo | Descripción | Uso | Formato  
---|---|---|---|---  
01 | JournalCode | Código del diario | `journal.code` y `journal.name` si no cuenta con `JournalLib`. | Alfanumérico  
02 | JournalLib | Etiqueta del diario | `journal.name` | Alfanumérico  
03 | EcritureNum | Numeración específica de cada secuencia numérica del asiento en el diario | `move.name` | Alfanumérico  
04 | EcritureDate | Fecha del asiento contable | `move.date` | Fecha (aaaaMMdd)  
05 | CompteNum | Número de cuenta | `account.code` | Alfanumérico  
06 | CompteLib | Etiqueta de la cuenta | `account.name` | Alfanumérico  
07 | CompAuxNum | Número de cuenta secundario (acepta nulo) | `partner.ref` | Alfanumérico  
08 | CompAuxLib | Etiqueta de cuenta secundaria (acepta nulo) | `partner.name` | Alfanumérico  
09 | PieceRef | Referencia del documento | `move.ref` y `move.name` si no cuenta con `EcritureNum`. | Alfanumérico  
10 | PieceDate | Fecha de documento | `move.date` | Fecha (aaaaMMdd)  
11 | EcritureLib | Etiqueta de asiento de la cuenta | `move_line.name` | Alfanumérico  
12 | Débito | Importe de débito | `move_line.debit` | Número flotante  
13 | Crédito | Cantidad de crédito (no puede nombrar este campo como «crédito») | `move_line.credit` | Número flotante  
14 | EcritureLet | Referencia cruzada del asiento contable (acepta nulo) | `move_line.fec_matching_number` | Alfanumérico  
15 | DateLet | Fecha del asiento contable (acepta nulo) | No se utiliza | Fecha (aaaaMMdd)  
16 | ValidDate | Fecha de validación del asiento contable | No se utiliza | Fecha (aaaaMMdd)  
17 | Montantdevise | Importe de la divisa (acepta nulo) | `move_line.amount_currency` | Número flotante  
18 | Idevise | Identificador de la divisa (acepta nulo) | `currency.name` | Alfanumérico  
  
Estos dos campos se pueden encontrar en sustitución de los otros en el sentido
antes descrito.

12 | Montant | Importe | `move_line.debit` o `move_line.credit` | Número flotante  
---|---|---|---|---  
13 | Sens | Puede ser «C» de crédito o «D» de débito | Determina `move_line.debit` o `move_line.credit` | Carácter  
  
#### Detalles de implementación

Estas entidades contables se importan desde los archivos FEC: **cuentas,
diarios, contactos** y **movimientos**.

Nuestro módulo determina la codificación, el carácter terminador de línea y el
separador que se usa en el archivo.

Después se hace una revisión para ver si cada línea tiene el número correcto
de campos que corresponden a la cabecera.

Si pasa la revisión entonces el archivo se lee completamente, se almacena en
la memoria y se escanea. Las entidades de contabilidad se importan un tipo a
la vez en el siguiente orden.

##### Cuentas

Cada asiento contable se relaciona a una cuenta, que se debería de determinar
por el campo `CompteNum`.

##### Emparejamiento de código

Si hay un código de cuenta similar en el sistema, se usará el que ya existe en
lugar de crear uno nuevo.

Por lo general, las cuentas en Konvergo ERP tienen un número de dígitos
predeterminados para la localización fiscal. Ya que el módulo FEC está
relacionado a la localización francesa, el número predeterminado de números
relevantes es 6.

Esto significa que, en los códigos de cuenta, los ceros finales se recortan
desde la derecha. La comparación entre los códigos en el archivo FEC y los que
ya existen en Konvergo ERP se realiza solo en los primeros seis dígitos de los
códigos.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El código de la cuenta es <code>65800000</code> en el archivo se compara con una cuenta <code>658000</code> existente en Konvergo ERP. Se utilizará esa cuenta en lugar de crear una nueva.</p>
</div>

##### Marcado como conciliado

Una cuenta se marca como _conciliada_ si la primera línea en la que aparece
tiene el campo `EcritureLet` lleno. Esta marca significa que el asiento
contable se conciliará con otro.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En caso de que, por algún motivo, la línea no tenga este campo completado pero el asiento se tenga que conciliar con un pago que aún no se registra, esto no es un problema. La cuenta se marca como conciliable tan pronto como el importe de las líneas lo requiera.</p>
</div>

##### Tipo de cuenta y emparejamiento de plantillas

Ya que el **tipo** de cuenta no se especifica en el formato FEC, las cuentas
**nuevas** se crean con el tipo _Activos circulantes_ predeterminado y
después, al final del proceso de importación, se emparejan con las plantillas
del plan de cuenta que ya están instaladas. La marca de _conciliado_ también
se calcula de esta manera.

El emparejamiento se realiza con los dígitos que están hasta la izquierda,
primero se usan todos los dígitos, después 3 y al final 2.

<div class="alert alert-success">
<p class="alert-title">
Example</p><table class="table docutils">
<colgroup>
<col style="width: 14%"/>
<col style="width: 14%"/>
<col style="width: 20%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Nombre</p></th>
<th class="head"><p>Código</p></th>
<th class="head"><p>Comparación completa</p></th>
<th class="head"><p>Comparación de 3 dígitos</p></th>
<th class="head"><p>Comparación de 2 dígitos</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Plantilla</p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-odd"><td><p>CompteNum</p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>401</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-even"><td><p><b>Resultado</b></p></td>
<td></td>
<td></td>
<td></td>
<td><p>Coincidencia <b>encontrada</b></p></td>
</tr>
</tbody>
</table>
</div>

El tipo de cuenta se marca como _por pagar_ y _conciliado_ según la plantilla
de la cuenta.

##### Diarios contables

Los diarios también se comparan con los que ya existen en Konvergo ERP para evitar
duplicados, también en caso de importación de varios archivos FEC.

Si hay un código de diario similar en el sistema, se usa el que ya existe en
lugar de crear uno nuevo.

Los nombres de los diarios nuevos empiezan con el prefijo `FEC-`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><code>COMPRAS</code> -&gt; <code>FEC-COMPRAS</code></p>
</div>

Los diarios _no_ están archivados, el usuario puede gestionarlos como
prefiera.

##### Determinación del tipo de diario

El tipo de diario tampoco está especificado en el formato (según las cuentas),
por lo tanto, primero se crea con el tipo `general` predeterminado.

Al final del proceso de importación, el tipo se determina según estas reglas
de acuerdo a los movimientos y cuentas relacionadas:

  * `banco`: los movimientos en estos diarios siempre tienen una línea (de crédito o débito) que impactarán la cuenta de liquidez.

Puede intercambiar entre `efectivo` y `banco`. Este último (`banco`) se
configura en todos lados cuando se cumple esta condición.

  * `venta`: estos diarios tienen, en su mayoría, líneas de débito en cuentas por cobrar y líneas de crédito en las cuentas de ingresos de impuestos.

Los apuntes contables de los reembolsos de ventas se invierten según el débito
o crédito.

  * `compra`: los movimientos en estos diarios tienen, en su mayoría, líneas de crédito en cuentas por pagar y líneas de débito en las cuentas de gastos.

Los apuntes contables de las compras reembolsadas se invierten según el débito
o crédito.

  * `general`: para todo lo demás.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Para identificar el tipo de diario se necesitan, por lo menos, tres movimientos.</p></li>
<li><p>Al menos el 70% de los movimientos deben corresponder a los criterios para poder determinar el tipo de diario.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Supongamos que se están analizando los movimientos que comparten un <code>journal_id</code> específico.</p>
<table class="table docutils">
<colgroup>
<col style="width: 76%"/>
<col style="width: 9%"/>
<col style="width: 15%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Movimientos</p></th>
<th class="head"><p>Número</p></th>
<th class="head"><p>Porcentaje</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>que tienen una línea de cuenta de venta y no tienen una línea de cuenta de compra</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
<tr class="row-odd"><td><p>que tienen una línea de cuenta de compra y no tienen una línea de cuenta de venta</p></td>
<td><p>1</p></td>
<td><p>25%</p></td>
</tr>
<tr class="row-even"><td><p>que tienen una línea de cuenta de liquidez</p></td>
<td><p>3</p></td>
<td><p><b>75%</b></p></td>
</tr>
<tr class="row-odd"><td><p><b>Total</b></p></td>
<td><p>4</p></td>
<td><p>100%</p></td>
</tr>
</tbody>
</table>
<p>El <code>tipo</code> de diario sería <code>banco</code>, ya que el porcentaje de movimientos bancarios (75%) excede el umbral (70%).</p>
</div>

##### Contactos

Cada contacto mantiene su `referencia` del campo `CompAuxNum`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Estos campos se pueden buscar en consonancia con los FEC importados con anterioridad en el lado del experto en contabilidad para propósitos fiscales o de auditoría.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Los usuarios pueden fusionar contactos con la aplicación Limpieza de datos. En esta aplicación los proveedores, clientes o contactos similares pueden fusionarse con ayuda del sistema que los agrupa por asientos similares.</p>
</div>

##### Movimientos

Los asientos se registran de inmediato y se concilian después de su envío. Se
usa el campo `EcritureLet` para conciliar los asientos entre ellos.

El campo `EcritureNum` representa el nombre de los movimientos. Sabemos que a
veces no contiene la información completa, en este caso se usa el campo
`PieceRef`.

##### Problemas de redondeamiento

Hay una tolerancia de redondeo con precisión en la divisa en el débito y el
crédito (por ejemplo, 0.01 para EUR). Tomando en cuenta esta tolerancia, se
agrega una nueva línea al movimiento, esta línea se llamará _Diferencia de
redondeo del importe_ y se focaliza en las cuentas:

  * `658000` «Charges diverses de gestion courante», para débitos agregados

  * `758000` «Produits divers de gestion courante», para créditos agregados

##### Nombre de movimiento faltante

Si el campo `EcritureNum` no está completo, existe la posibilidad de que el
campo `PieceRef` no sea adecuado para determinar el nombre del movimiento (se
puede usar como una línea contable de referencia). En este caso, no hay manera
de encontrar qué líneas se tienen que agrupar en un mismo movimiento, por lo
que se impide la creación de movimientos balanceados.

Se realiza un último intento en el que se agrupan todas las líneas del mismo
diario y la misma fecha (`JournalLib`, `EcritureDate`). Si este agrupamiento
genera movimientos balanceados (suma(crédito) - suma(débito) = 0), entonces
cada combinación distinta de diario y fecha crea un nuevo movimiento.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>0

Si este intento falla, el usuario verá un mensaje de error con todas las
líneas de movimiento que no están balanceadas.

##### Información del contacto

Si una línea tiene la información del contacto especificada, la información se
copia al movimiento contable si el tipo de diario al que se importará es _por
pagar_ o _conciliable_.

### Exportar

Si instaló el [paquete de localización
fiscal](../fiscal_localizations#fiscal-localizations-packages) para
Francia, debería poder descargar el FEC. Para hacerlo, vaya a Contabilidad ‣
Reportes ‣ Francia ‣ FEC.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>1 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>2

## Reportes contables franceses

Si instaló la contabilidad francesa, podrá acceder a algunos reportes de
contabilidad específicos para Francia:

  * Bilan comptable (balance general)

  * Compte de résultats (estado de resultados)

  * Plan de impuestos de Francia

## Obtener la certificación antifraude del IVA con Konvergo ERP

A partir del primero de enero de 2018, entró en vigencia una nueva legislación
antifraude en Francia y los territorios de ultramar. Esta nueva legislación
estipula ciertos criterios sobre inalterabilidad, seguridad, almacenamiento y
archivado de los datos de ventas. Estos requisitos legales se implementan en
Konvergo ERP, a partir de la versión 9, con un módulo y un certificado de conformidad
que se debe descargar.

### ¿Mi empresa necesita usar un software antifraude?

Su empresa necesita usar un software antifraude de caja registradora como Konvergo ERP
(CGI art. 286, I. 3° bis) si:

  * Está sujeto a impuestos (no está exento de IVA) en Francia o en cualquier territorio de ultramar,

  * Algunos de sus clientes son personas físicas (B2C).

Esta regla aplica para cualquier empresa de cualquier tamaño. Los empresarios
independientes están exentos del IVA y, por tanto, no se ven afectados.

### Obtenga la certificación con Konvergo ERP

Cumplir las reglas con Konvergo ERP es muy fácil.

La autoridad financiera le pide a su empresa que proporcione un certificado de
conformidad en el que aparezca que su software cumple con la legislación
antifraude. Konvergo ERP SA otorga este certificado a los usuarios de Konvergo ERP Enterprise
[aquí](https://www.odoo.com/my/contract/french-certification/). Si usa la
versión Community de Konvergo ERP, debería [actualizar a la versión
Enterprise](../../../administration/on_premise/community_to_enterprise) o
contactar a su proveedor.

En caso de que no cumpla con la legislación, su empresa corre el riesgo de
recibir una multa por 7,500 euros.

Para obtener el certificado solo siga estos pasos:

  * Si usa el **Punto de venta de Konvergo ERP** [instale](../../general/apps_modules#general-install) el módulo **Francia - Certificación antifraude del IVA para Punto de venta (CGI 286 I-3 bis)**. Vaya a Aplicaciones, elimine el filtro de _aplicaciones_ , busque _l10n_fr_pos_cert_ e instale el módulo.

  * Asegúrese de que su país está configurado en su empresa, de lo contrario sus asientos no se encriptarán para la comprobación de inalterabilidad. Para editar la información de su empresa, vaya a Ajustes ‣ Usuarios y empresas ‣ Empresas. Seleccione un país de la lista, no necesita crear uno nuevo.

  * Descargue el certificado de conformidad obligatorio que le proporciona Konvergo ERP SA [aquí](https://www.odoo.com/my/contract/french-certification/).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>3

### Funciones antifraude

El módulo antifraude ofrece las siguientes funciones:

  * **Inalterabilidad** : desactivación de todas las formas de cancelar o modificar datos clave de órdenes del PdV, facturas y asientos contables;

  * **Seguridad** : algoritmo de encadenamiento para verificar la inalterabilidad;

  * **Almacenamiento** : cierres de ventas automáticos con cálculos tanto del periodo como de los totales acumulados (diario, mensual, anual).

#### Inalterabilidad

Todas las formas posibles de cancelar y modificar los datos clave de las
órdenes del PdV pagadas, las facturas confirmadas y los asientos contables se
desactivan si la empresa está ubicada en Francia o en cualquier territorio de
ultramar.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>4

#### Seguridad

Para garantizar la inalterabilidad, todas las órdenes o asientos contables se
encriptan al validarlas. Este número (o hash) se calcula a partir de los datos
clave del documento, así como a partir del hash de documentos precedentes.

El módulo introduce una interfaz para probar la inalterabilidad de los datos.
Si se edita cualquier información dentro de un documento después de su
validación, la prueba fallará. El algoritmo vuelve a calcular todos los hashes
y los compara con los iniciales. En caso de que ocurra un error, el sistema
indica el primer documento corrupto en el sistema.

Los usuarios con derechos de acceso de _gerente_ pueden iniciar la
comprobación de inalterabilidad. Para órdenes del PdV, vaya a Punto de Venta ‣
Reportes ‣ Estados de cuenta franceses.

#### Almacenamiento

El sistema también procesa cierres de venta automáticos cada día, cada mes y
cada año. Estos cierres calculan el total de ventas específicamente del
periodo indicado así como los totales generales acumulativos desde el primer
asiento de ventas registrado en el sistema.

Los cierres están disponibles en el menú _Estados de cuenta franceses_ de las
aplicaciones Punto de venta, Facturación y Contabilidad.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>6

### Responsabilidades

¡No desinstale el módulo! Si lo hace, los hashes se resetearán y no será
posible garantizar que su información previa sea inalterable.

Los usuarios son responsables de su instancia de Konvergo ERP y deben usarla con su
debida diligencia. No se permite modificar el código fuente, ya que este
garantiza la inalterabilidad de los datos.

Konvergo ERP no se hace responsable de cualquier cambio que las aplicaciones externas
que Konvergo ERP no haya certificado puedan realizar en las funciones de los módulos.

### Más información

Encontrará más información sobre esta legislación en los documentos oficiales.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El archivo FEC CSV tiene un formato de texto plano que representa una tabla de datos, en la cual la primera línea es un encabezado y define la lista de campos de cada entrada. Cada una de las líneas siguientes representa un asiento contable y no tiene un orden predeterminado.</p>
</div>7

