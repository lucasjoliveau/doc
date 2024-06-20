# Alemania

## Plan de cuentas de Alemania

Odoo es compatible con los planes de cuentas SKR03 y SKR04. Puede elegir uno
desde Contabilidad ‣ Configuración, luego seleccione el paquete que desee en
la sección de localización fiscal.

Tenga cuidado, solo puede cambiar el paquete contable siempre y cuando no haya
creado ningún asiento contable.

Truco

Al crear una nueva base de datos de Odoo en línea, se instala SKR03 de forma
predeterminada.

## Reportes contables alemanes

Esta es la lista de reportes específicos de Alemania disponibles en Odoo
Enterprise:

  * Balance general

  * Ganancias y pérdidas

  * Reporte fiscal (Umsatzsteuervoranmeldung)

  * Partner de IVA Intra

## Exportación de Odoo a Datev

Es posible exportar sus asientos contables de Odoo a Datev. Para poder
utilizar esta función, la localización de contabilidad alemana debe estar
instalada en su base de datos de Odoo Enterprise. Vaya a Contabilidad ‣
Reportes ‣ Contabilidad general y haga clic en el botón **Exportar Datev
(CSV)**.

## Punto de venta en Alemania: sistema de seguridad técnica

La **Kassensicherungsverordnung** (Ley de protección contra la manipulación de
registros digitales) requiere que los sistemas de registro electrónico (entre
ellos los sistemas del [punto de venta](../../sales/point_of_sale.html)) se
encuentren equipados con un **sistema de seguridad técnica** , también
conocido como **TSS** o **TSE**.

Odoo ofrece un sistema compatible con [fiskaly](https://fiskaly.com), una
solución _alojada en la nube_.

Importante

Ya que esta solución está alojada en la nube, necesita una conexión a internet
estable.

Nota

Las únicas tasas de IVA permitidas las proporciona fiskaly, puede consultarlas
en: [fiskaly DSFinV-K API: VAT Definition (API: definición del
IVA)](https://developer.fiskaly.com/api/dsfinvk/v0/#tag/VAT-Definition).

### Configuración

#### Instalación de módulos

  1. Si creó su base de datos antes de junio de 2021, [actualice](../../general/apps_modules.html#general-upgrade) su aplicación **Punto de venta** (`point_of_sale`) y el módulo **Restaurante** (`pos_restaurant`).

  2. [Instale](../../general/apps_modules.html#general-install) los módulos **Alemania - Certificación para el Punto de Venta** (`l10n_de_pos_cert`) y **Alemania - Certificación para el Punto de Venta de tipo Restaurante** (`l10n_de_pos_res_cert`).

Truco

Si estos módulos no aparecen en la lista de aplicaciones,
[actualícela](../../general/apps_modules.html#general-install).

![Actualización de la aplicación Punto de venta de Odoo desde el tablero de
aplicaciones.](../../../_images/pos-upgrade.png)

#### Registre su empresa ante la autoridad fiscal

Para registrar a su empresa, vaya a Ajustes ‣ Ajustes generales ‣ Empresas ‣
Actualizar información, llene los campos y _guarde_.

  * **Nombre de la empresa**

  * **Dirección** válida

  * Número de **identificación fiscal**

  * **St.-Nr** (Steuernummer): este número lo asigna la oficina fiscal a cualquier persona física o moral que deba pagar impuestos, por ejemplo, `2893081508152`.

  * **W-IdNr** (Wirtschafts-Identifikationsnummer): este número se usa como un número de identificación permanente para personas económicamente activas.

Ahora puede **registrar a su empresa con fiskaly**. Para hacerlo, abra la
pestaña de _fiskaly_ y de clic en el botón de _registro de fiskaly_.

![Botón para registrar una empresa a través de fiskaly en
Odoo](../../../_images/fiskaly-registration.png)

Truco

Si no puede ver el botón de _registro de fiskaly_ , asegúrese de _guardar_ los
detalles de su empresa y que ya no se encuentre en el _modo de edición_.

Una vez que finalice el registro, aparecerán nuevos campos:

  * **ID de organización de fiskaly** , este corresponde al ID de su empresa en el sitio de fiskaly.

  * **Clave API de fiskaly** y un **secreto** , que son las credenciales que el sistema usa para acceder a los servicios que ofrece fiskaly.

![Las claves de fiskaly como se muestran en Odoo.](../../../_images/fiskaly-
keys.png)

Nota

Puede solicitar nuevas credenciales si tiene problemas con las actuales.

#### Cree y vincule un sistema de seguridad técnica a su PdV

![Opción para crear un TSS desde un punto de venta](../../../_images/create-
tss.png)

Para usar su punto de venta en Alemania, primero deberá crear un TSS.

Vaya a Punto de Venta ‣ Configuración ‣ Punto de Venta, abra el punto de venta
que quiere editar, haga clic en la casilla junto a **Crear TSS** y luego en
_Guardar_.

![Ejemplo de ID de TSS y de cliente de fiskaly en el Punto de Venta de
Odoo](../../../_images/tss-ids.png)

Una vez que haya creado el TSS, podrá encontrar su **ID de TSS y de cliente**
en la sección _API de fiskaly_.

  * El **ID de TSS** se refiere al ID de su TSS en fiskaly.

  * El **ID del cliente** se refiere al ID de su punto de venta en fiskaly.

### DSFinV-K

![Menú para exportar DSFinV-K](../../../_images/dsfinv-k-export.png)

Siempre que cierra una sesión del PdV se envían los detalles de las órdenes al
servicio DSFinV-K de fiskaly.

En caso de una auditoría, puede exportar los datos que se envían a DSFinV-K.
Para hacer esto, vaya a Punto de Venta ‣ Órdenes ‣ Exportaciones de DSFinV-k.

Los siguientes campos son obligatorios:

  * **Nombre**

  * **Fecha y hora de inicio** (datos a exportar con fechas mayores o iguales a la fecha de inicio indicada)

  * **Fecha y hora de finalización** (datos a exportar con fechas menores o iguales a la fecha de finalización indicada)

Deje el campo **Punto de Venta** vacío si quiere exportar los datos de todos
sus puntos de venta. Especifique uno si solo quiere exportar los datos de ese
PdV en específico.

La creación de una exportación de DSFinV-K se activa al exportar del lado de
fiskaly.

![Exportación DSFinV-K pendiente en Odoo](../../../_images/dsfinv-k-export-
fields.png)

Podrá ver que el **estado** se encuentra _pendiente_. Esto significa que la
exportación se activó de forma correcta y que se está procesando. Haga clic en
_Actualizar estado_ para verificar si está lista.

## Estándares para la contabilidad tributaria alemana: la guía de Odoo para la
conformidad con las normas GoBD

**GoBD** significa [Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung
von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum
Datenzugriff](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf).
En resumen, es una **guía para la gestión y almacenamiento adecuados de
libros, registros y documentos en formato electrónico, así como para el acceso
a datos** , que es relevante para las autoridades tributarias alemanas, las
declaraciones de impuestos y el balance general.

Estos principios los escribió y publicó el Ministerio Federal de Finanzas
(BMF, por sus siglas en alemán) en noviembre de 2014. Desde enero de 2015,
**se han convertido en la norma** y reemplazaron a las practicas previamente
aceptadas que se encontraban ligadas a la contabilidad computarizada. El BMF
realizó varios cambios durante el 2019 y enero de 2020 para especificar el
contenido y debido al desarrollo de soluciones electrónicas (alojamiento en la
nube, empresas que están dejando de usar papel, etcétera).

Importante

Odoo le proporciona **los medios para cumplir con GoBD**.

### ¿Qué necesita saber sobre GoBD al confiar en un software de contabilidad?

Nota

Si tiene la posibilidad, la mejor forma de comprender el GoBD es leer el
[Texto oficial del
GoBD](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf).
Es un poco largo, pero fácil de leer para quienes no son expertos. En resumen,
esto es lo que debe esperar:

El **GoBD es vinculante para empresas que tienen cuentas presentes, esto
incluye pymes, profesionales independientes y emprendedores**. Debido a esto,
**el contribuyente es el único responsable** de la conservación completa y
exhaustiva de los datos con relevancia fiscal (los datos financieros y
relacionados antes mencionados).

Además de los requisitos del software, es esencial que el usuario asegure los
sistemas de control interno (_en cumplimiento con la sección 146 del Código
Fiscal_):

  * Control de los derechos de acceso;

  * Separación de deberes y separación funcional;

  * Controles de entrada (notificaciones de error, comprobaciones de factibilidad);

  * Comprobación de conciliación al registrar los datos;

  * Controles de procesamiento;

  * Medidas para prevenir la manipulación intencional o no intencional del software, información o documentos.

El usuario debe distribuir tareas dentro de su organización a las posiciones
relevantes (_control_) y verificar que las tareas se realicen en su totalidad
y de manera correcta (_supervisión_). Se debe registrar el resultado de estos
controles (_documentación_) y si se llegan a encontrar errores durante estos
controles, se deben llevar a cabo las acciones correspondientes para corregir
la situación (_prevención_).

### ¿Qué hay de la seguridad de los datos?

**El contribuyente debe asegurar el sistema contra cualquier pérdida de datos
resultado de eliminación, retiro o robo de cualquier información**. Si los
asientos no están bien asegurados, se concluirá que la teneduría de libros no
cumple con las normas GoBD.

Una vez que se publique el registro de libros, ya no se pueden modificar o
eliminar por medio de la aplicación.

  * Si utiliza Odoo en la nube, las copias de seguridad periódicas forman parte del servicio de Odoo en línea. Además, puede descargar y realizar respaldos periódicos en sistemas externos.

Ver también

[Alojamiento en la nube de Odoo - Acuerdo de nivel de
servicio](https://www.odooo.com/cloud-sla)

  * Si el servidor funciona a nivel local, es responsabilidad del usuario crear la infraestructura de respaldo necesaria.

Importante

En algunos casos, es necesario conservar los datos durante diez años o más,
así que siempre tenga copias de seguridad almacenadas ya que son aún más
importantes si decide cambiar de proveedor de software.

### Responsabilidad del editor del software

Considerando que GoBD solo aplica entre el contribuyente y la autoridad
tributaria, **el editor del software de ninguna manera puede ser responsable
de la documentación correcta y conforme de los datos financieros
transaccionales de sus clientes**. Solo puede brindar las herramientas
necesarias para que el usuario respete las normas relacionadas al software que
se describen en GoBD.

### ¿Cómo puede ir en conformidad con las normas con la ayuda de Odoo?

Las palabras clave al hablar de GoBD son: **trazable, verificable, verdadero,
claro y continuo**. En resumen, debe contar con un almacenamiento a prueba de
auditoría y Odoo le brinda los medios para lograr todos esos objetivos:

  1. **Trazable y verificable**

Cada registro en Odoo tiene la marca de la persona que creó el documento, la
fecha de creación, la fecha de modificación y quién lo modificó. Además, se
lleva un registro de los campos relevantes y puede observar qué valores
cambiaron y quién los cambió en el chatter del objeto relevante.

  2. **Completo**

Debe registrar todos los datos financieros en el sistema, no puede faltar
nada. Odoo se asegura de que no haya espacios en la numeración de las
transacciones financieras. Es responsabilidad del usuario codificar todos los
datos financieros en el sistema. Como la mayoría de los datos en Odoo se
generan en automático, sigue siendo responsabilidad del usuario codificar
todas las facturas de proveedor y operaciones misceláneas.

  3. **Precisión**

Odoo se asegura de que se usen las cuentas correctas con la información
correcta. Además, los mecanismos de control entre órdenes de compra y órdenes
de venta y sus respectivas facturas refleja la realidad del negocio. Es
responsabilidad del usuario escanear y y adjuntar facturas impresas del
proveedor a su respectivo registro de Odoo. _La aplicación Documentos le ayuda
a automatizar esta tarea_.

  4. **Contabilización y registros puntuales**

Ya que la mayoría de la información financiera en Odoo se genera con objetos
transaccionales (por ejemplo, la factura se registra al confirmarla), Odoo
garantiza la puntualidad en el mantenimiento de los registros. Es
responsabilidad del usuario codificar puntualmente todas las facturas del
proveedor entrantes, así como las operaciones misceláneas.

  5. **Orden**

Los datos financieros almacenados en Odoo se ordenan por definición y se
pueden reordenar de acuerdo con la mayoría de los campos presentes en el
modelo. El GoBD no impone ningún orden específico, pero el sistema debe
garantizar que cualquier transacción dada se pueda encontrar rápidamente por
un tercero. Odoo garantiza esto de forma inmediata.

  6. **Inalterabilidad**

Al instalar la localización alemana, Odoo se configura de tal manera que se
podrá adherir a la cláusula de inalterabilidad sin tener que realizar más
personalizaciones.

### ¿Necesita un archivo de exportación GoBD?

En caso de control fiscal, la autoridad tributaria puede pedirle al sistema de
contabilidad tres niveles de acceso (Z1, Z2, Z3). Estos niveles varían de
acceso directo a la interfaz, hasta la entrega de datos financieros en un
dispositivo de almacenamiento.

En caso de transferir datos financieros a un dispositivo de almacenamiento, el
GoBD **no** impone un formato específico. Pueden tener, por ejemplo, formato
XLS, CSV, XML, Lotus 123, SAP, AS/400 u algún otro. Odoo admite la exportación
CSV y XLS de datos financieros listos para usar. El GoBD **recomienda** que se
exporten en un formato GoBD específico basado en XML (consulte la Sección 3 de
«Ergänzende Informationen zur Datenntträgerüberlassung»), pero no es
vinculante.

### ¿Cuál es la función y el significado del certificado de conformidad?

El GoBD deja en claro que debido a la naturaleza de un software de
contabilidad vanguardista, las posibilidades de configuración, su naturaleza
cambiante y las diversas formas de uso, **no se puede otorgar una
certificación legalmente vinculante** así como el software tampoco se puede
hacer responsable ante una autoridad pública. Los certificados de terceros sí
pueden tener un **valor informativo** para que los clientes tomen la decisión
de comprar el software, pero estos certificados no son legalmente vinculantes
ni tienen ningún otro valor legal (A. 12, § 181).

Lo único que indica un certificado de GoBD es que si usa el software de
acuerdo con sus reglas, el software no le impedirá respetar el GoBD. Estas
certificaciones son muy costosas en cuanto a tiempo y costo, además de que su
valor es relativo. Por lo tanto, podemos concentrarnos en asegurar que
cumplimos con las normas GoBD en lugar de pagar por una herramienta de
marketing que de ninguna forma le proporciona a nuestro cliente seguridad
legal.

Importante

El BMF indica lo siguiente en el [texto oficial de
GoBD](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf):

  * 180\. Positive attestations on the correctness of the bookkeeping - and thus on the correctness of IT-based bookkeeping systems - are not issued either in the context of a tax field audit or in the context of binding information.

  * 181\. «Certificates» or «attestations» from third parties can serve as a decision criterion for the company when selecting a software product, but develop from the in margin no. 179 is not binding on the tax authorities.

Nota

El contenido previo [se tradujo al español desde una traducción del alemán al
inglés que se realizó usando Google
Translate](https://translate.google.com/?sl=de&tl=en&text=180.%0APositivtestate%20zur%20Ordnungsm%C3%A4%C3%9Figkeit%20der%20Buchf%C3%BChrung%20-%20und%20damit%20zur%20Ordnungsm%C3%A4%C3%9Figkeit%20DV-
gest%C3%BCtzter%20Buchf%C3%BChrungssysteme%20-%20werden%20weder%20im%20Rahmen%20einer%20steuerlichen%20Au%C3%9Fenpr%C3%BCfung%20noch%20im%20Rahmen%20einer%20verbindlichen%20Auskunft%20erteilt.%0A%0A181.%0A%E2%80%9EZertifikate%E2%80%9C%20oder%20%E2%80%9ETestate%E2%80%9C%20Dritter%20k%C3%B6nnen%20bei%20der%20Auswahl%20eines%20Softwareproduktes%20dem%20Unternehmen%20als%20Entscheidungskriterium%20dienen%2C%20entfalten%20jedoch%20aus%20den%20in%20Rz.%20179%20genannten%20Gr%C3%BCnden%20gegen%C3%BCber%20der%20Finanzbeh%C3%B6rde%20keine%20Bindungswirkung.%20&op=translate).

### ¿Qué pasa si no cumple con las normas adecuadas?

En caso de que ocurra una infracción, puede recibir una multa, así como una
orden judicial en la que le solicitarán que implemente medidas específicas.

  *[TSS]: Sistema de seguridad técnica
  *[DSFinV-K]: Digitale Schnittstelle der Finanzverwaltung für Kassensysteme

