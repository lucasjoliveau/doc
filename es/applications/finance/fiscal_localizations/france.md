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
localización fiscal](../fiscal_localizations.html#fiscal-localizations-
packages) para Francia de Odoo Enterprise incluye la función **Importar FEC**
(nombre técnico: `l10n_fr_fec_import`), la cual permite importar archivos FEC
existentes desde un software antiguo.

Para habilitar esta función vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣
Importar contabilidad, active **Importar FEC** y haga clic en _guardar_.

Después, vaya a Contabilidad ‣ Configuración ‣ Importar FEC, suba el archivo
FEC y haga clic en _Importar_.

Nota

No hay una acción o cálculo particular para importar archivos FEC de un año
diferente.

Si varios archivos contienen «Reports à Nouveaux» (RAN) con el balance inicial
del año, puede que tenga que cancelar los asientos en la interfaz del usuario.
Los asientos (RAN) no son útiles en Odoo.

#### Formatos de archivo

Los archivos FEC solo pueden estar en formato CSV, ya que no son compatibles
con el formato XML.

Nota

El archivo FEC CSV tiene un formato de texto plano que representa una tabla de
datos, en la cual la primera línea es un encabezado y define la lista de
campos de cada entrada. Cada una de las líneas siguientes representa un
asiento contable y no tiene un orden predeterminado.

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

Por lo general, las cuentas en Odoo tienen un número de dígitos
predeterminados para la localización fiscal. Ya que el módulo FEC está
relacionado a la localización francesa, el número predeterminado de números
relevantes es 6.

Esto significa que, en los códigos de cuenta, los ceros finales se recortan
desde la derecha. La comparación entre los códigos en el archivo FEC y los que
ya existen en Odoo se realiza solo en los primeros seis dígitos de los
códigos.

Example

El código de la cuenta es `65800000` en el archivo se compara con una cuenta
`658000` existente en Odoo. Se utilizará esa cuenta en lugar de crear una
nueva.

##### Marcado como conciliado

Una cuenta se marca como _conciliada_ si la primera línea en la que aparece
tiene el campo `EcritureLet` lleno. Esta marca significa que el asiento
contable se conciliará con otro.

Nota

En caso de que, por algún motivo, la línea no tenga este campo completado pero
el asiento se tenga que conciliar con un pago que aún no se registra, esto no
es un problema. La cuenta se marca como conciliable tan pronto como el importe
de las líneas lo requiera.

##### Tipo de cuenta y emparejamiento de plantillas

Ya que el **tipo** de cuenta no se especifica en el formato FEC, las cuentas
**nuevas** se crean con el tipo _Activos circulantes_ predeterminado y
después, al final del proceso de importación, se emparejan con las plantillas
del plan de cuenta que ya están instaladas. La marca de _conciliado_ también
se calcula de esta manera.

El emparejamiento se realiza con los dígitos que están hasta la izquierda,
primero se usan todos los dígitos, después 3 y al final 2.

Example

Nombre | Código | Comparación completa | Comparación de 3 dígitos | Comparación de 2 dígitos  
---|---|---|---|---  
Plantilla | `400000` | `400000` | `400` | `40`  
CompteNum | `40100000` | `40100000` | `401` | `40`  
**Resultado** |  |  |  | Coincidencia **encontrada**  
  
El tipo de cuenta se marca como _por pagar_ y _conciliado_ según la plantilla
de la cuenta.

##### Diarios contables

Los diarios también se comparan con los que ya existen en Odoo para evitar
duplicados, también en caso de importación de varios archivos FEC.

Si hay un código de diario similar en el sistema, se usa el que ya existe en
lugar de crear uno nuevo.

Los nombres de los diarios nuevos empiezan con el prefijo `FEC-`.

Example

`COMPRAS` -> `FEC-COMPRAS`

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

Nota

  * Para identificar el tipo de diario se necesitan, por lo menos, tres movimientos.

  * Al menos el 70% de los movimientos deben corresponder a los criterios para poder determinar el tipo de diario.

Example

Supongamos que se están analizando los movimientos que comparten un
`journal_id` específico.

Movimientos | Número | Porcentaje  
---|---|---  
que tienen una línea de cuenta de venta y no tienen una línea de cuenta de compra | 0 | 0  
que tienen una línea de cuenta de compra y no tienen una línea de cuenta de venta | 1 | 25%  
que tienen una línea de cuenta de liquidez | 3 | **75%**  
**Total** | 4 | 100%  
  
El `tipo` de diario sería `banco`, ya que el porcentaje de movimientos
bancarios (75%) excede el umbral (70%).

##### Contactos

Cada contacto mantiene su `referencia` del campo `CompAuxNum`.

Nota

Estos campos se pueden buscar en consonancia con los FEC importados con
anterioridad en el lado del experto en contabilidad para propósitos fiscales o
de auditoría.

Truco

Los usuarios pueden fusionar contactos con la aplicación Limpieza de datos. En
esta aplicación los proveedores, clientes o contactos similares pueden
fusionarse con ayuda del sistema que los agrupa por asientos similares.

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

Example

`ACH` \+ `2021/05/01` –> nuevo movimiento en el diario `ACH` con el nombre
`20210501`.

Si este intento falla, el usuario verá un mensaje de error con todas las
líneas de movimiento que no están balanceadas.

##### Información del contacto

Si una línea tiene la información del contacto especificada, la información se
copia al movimiento contable si el tipo de diario al que se importará es _por
pagar_ o _conciliable_.

### Exportar

Si instaló el [paquete de localización
fiscal](../fiscal_localizations.html#fiscal-localizations-packages) para
Francia, debería poder descargar el FEC. Para hacerlo, vaya a Contabilidad ‣
Reportes ‣ Francia ‣ FEC.

Truco

Si no puede ver el submenú **FEC** , vaya a Aplicaciones, elimine el filtro de
_aplicaciones_ y busque el módulo llamado **Francia - FEC** y verifique que
está instalado.

Ver también

  * [Especificación oficial técnica (en francés)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775)

  * [Test-Compta-Demat (Herramienta de prueba oficial de FEC)](https://github.com/DGFiP/Test-Compta-Demat)

## Reportes contables franceses

Si instaló la contabilidad francesa, podrá acceder a algunos reportes de
contabilidad específicos para Francia:

  * Bilan comptable (balance general)

  * Compte de résultats (estado de resultados)

  * Plan de impuestos de Francia

## Obtener la certificación antifraude del IVA con Odoo

A partir del primero de enero de 2018, entró en vigencia una nueva legislación
antifraude en Francia y los territorios de ultramar. Esta nueva legislación
estipula ciertos criterios sobre inalterabilidad, seguridad, almacenamiento y
archivado de los datos de ventas. Estos requisitos legales se implementan en
Odoo, a partir de la versión 9, con un módulo y un certificado de conformidad
que se debe descargar.

### ¿Mi empresa necesita usar un software antifraude?

Su empresa necesita usar un software antifraude de caja registradora como Odoo
(CGI art. 286, I. 3° bis) si:

  * Está sujeto a impuestos (no está exento de IVA) en Francia o en cualquier territorio de ultramar,

  * Algunos de sus clientes son personas físicas (B2C).

Esta regla aplica para cualquier empresa de cualquier tamaño. Los empresarios
independientes están exentos del IVA y, por tanto, no se ven afectados.

### Obtenga la certificación con Odoo

Cumplir las reglas con Odoo es muy fácil.

La autoridad financiera le pide a su empresa que proporcione un certificado de
conformidad en el que aparezca que su software cumple con la legislación
antifraude. Odoo SA otorga este certificado a los usuarios de Odoo Enterprise
[aquí](https://www.odoo.com/my/contract/french-certification/). Si usa la
versión Community de Odoo, debería [actualizar a la versión
Enterprise](../../../administration/on_premise/community_to_enterprise.html) o
contactar a su proveedor.

En caso de que no cumpla con la legislación, su empresa corre el riesgo de
recibir una multa por 7,500 euros.

Para obtener el certificado solo siga estos pasos:

  * Si usa el **Punto de venta de Odoo** [instale](../../general/apps_modules.html#general-install) el módulo **Francia - Certificación antifraude del IVA para Punto de venta (CGI 286 I-3 bis)**. Vaya a Aplicaciones, elimine el filtro de _aplicaciones_ , busque _l10n_fr_pos_cert_ e instale el módulo.

  * Asegúrese de que su país está configurado en su empresa, de lo contrario sus asientos no se encriptarán para la comprobación de inalterabilidad. Para editar la información de su empresa, vaya a Ajustes ‣ Usuarios y empresas ‣ Empresas. Seleccione un país de la lista, no necesita crear uno nuevo.

  * Descargue el certificado de conformidad obligatorio que le proporciona Odoo SA [aquí](https://www.odoo.com/my/contract/french-certification/).

Nota

  * Para instalar el módulo en cualquier sistema creado antes del 18 de diciembre de 2017, debe actualizar la lista de módulos. Para hacerlo, active el [modo de desarrollador](../../general/developer_mode.html#developer-mode). Vaya al menú _Aplicaciones_ y de clic en _Actualizar lista de módulos_ en la parte superior del menú.

  * En caso de que use Odoo de forma local, primero debe actualizar su instalación y reiniciar su servidor.

  * Si instaló la versión inicial del módulo antifraude (anterior al 18 de diciembre de 2017), necesita actualizarlo. El nombre del módulo es _Francia - Contabilidad - CGI 286 I-3 bis certificado_. Después de la actualización de la lista de módulos, busque la actualización del módulo en _Aplicaciones_ , selecciónela y haga clic en _actualizar_. Por último, asegúrese de que el módulo _l10n_fr_sale_closing_ esté instalado.

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

Nota

Si ejecuta un entorno multiempresas, solo se verán afectados los documentos de
dichas empresas.

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

Nota

  * Los cierres calculan los totales para los asientos contables de los diarios de venta (tipo de diario = ventas).

  * Para entornos multiempresas, estos cierres se realizan para cada empresa por separado.

  * Las órdenes del PdV se publican como asientos contables al cerrar la sesión del PdV y esta se puede cerrar en cualquier momento. Para invitar a que los usuarios hagan esto todos los días, el módulo no permite volver a iniciar una sesión que se abrió hace más de 24 horas. Esta sesión se debe cerrar antes de volver a vender.

  * El total de un periodo se calcula a partir de todos los asientos contables que se publicaron después del cierre previo del mismo tipo, sin importar su fecha de publicación. Si registra una nueva transacción de venta para un periodo que ya se cerró, se contará en el cierre más cercano.

Truco

  * Para pruebas y auditorías, puede generar estos cierres de forma manual en el [modo de desarrollador](../../general/developer_mode.html#developer-mode).

  * Después vaya a Ajustes ‣ Técnico ‣ Automatización ‣ Acciones planeadas.

### Responsabilidades

¡No desinstale el módulo! Si lo hace, los hashes se resetearán y no será
posible garantizar que su información previa sea inalterable.

Los usuarios son responsables de su instancia de Odoo y deben usarla con su
debida diligencia. No se permite modificar el código fuente, ya que este
garantiza la inalterabilidad de los datos.

Odoo no se hace responsable de cualquier cambio que las aplicaciones externas
que Odoo no haya certificado puedan realizar en las funciones de los módulos.

### Más información

Encontrará más información sobre esta legislación en los documentos oficiales.

Ver también

  * [Preguntas frecuentes](https://www.economie.gouv.fr/files/files/directions_services/dgfip/controle_fiscal/actualites_reponses/logiciels_de_caisse.pdf)

  * [Comunicado oficial](http://bofip.impots.gouv.fr/bofip/10691-PGP.html?identifiant=BOI-TVA-DECLA-30-10-30-20160803)

  * [Artículo 88 de las leyes financieras de 2016](https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=JORFARTI000031732968&categorieLien=id&cidTexte=JORFTEXT000031732865)

