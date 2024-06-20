# Bélgica

## Configuración

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Bélgica que
cumplen con las Normas Internacionales de Información Financiera.

Nombre | Nombre técnico | Descripción  
---|---|---  
Bélgica - Contabilidad | `l10n_be` | [Paquete de localización fiscal](../fiscal_localizations.html#fiscal-localizations-packages) predeterminado.  
Bélgica - Reportes contables | `l10n_be_reports` | Acceso a reportes contables específicos para Bélgica.  
Bélgica - Reportes contables (asistente de publicación) | `l10n_be_reports_post_wizard` | Habilita el asistente de IVA al registrar un asiento contable de declaración de impuestos.  
Bélgica - Importar estados de cuenta bancarios CODA | `l10n_be_coda` | Importa estados de cuenta bancarios CODA.  
Bélgica - Importar archivos SODA | `l10n_be_soda` | Importa archivos SODA.  
Bélgica - Datos de gastos no permitidos | `l10n_be_disallowed_expenses` | Acceso al uso de funciones de gastos no permitidos.  
Bélgica - Nómina | `l10n_be_hr_payroll` | Acceso a las funciones básicas de nómina de Bélgica.  
Bélgica - Nómina y contabilidad | `l10n_be_hr_payroll_account` | Integración de los datos de contabilidad con la nómina.  
Bélgica - Nómina - Dimona | `l10n_be_hr_payroll_dimona` | Acceso a las funciones de Dimona para la nómina.  
Bélgica - Nómina - Flota | `l10n_be_hr_payroll_fleet` | Funciones de flota para la nómina.  
Configurador de sueldo (Bélgica) | `l10n_be_hr_contract_salary` | Acceso a la función del configurador de sueldo.  
  
## Plan de cuentas

Puede acceder al Plan de cuentas mediente Contabilidad ‣ Configuración ‣
Contabilidad: plan de cuentas.

El plan de cuentas de Bélgica incluye cuentas preconfiguradas como se describe
en el PCMN. Para agregar una nueva cuenta, haga clic en Nuevo. Aparecerá una
nueva línea, complétela, haga clic en Guardar y luego en Configurar para
continuar.

Ver también

[Plan de cuentas](../accounting/get_started/chart_of_accounts.html)

## Impuestos

Los impuestos belgas predeterminados se crean automáticamente cuando se
instalan los módulos Bélgica - Contabilidad y Bélgica - Reportes contables.
Cada impuesto afecta al Reporte de impuestos belga, disponible en Contabilidad
‣ Reportes ‣ Reportes de estados financieros: reporte de impuestos.

En Bélgica, la tasa estándar del impuesto es del **21%** , pero hay tasas más
bajas para algunas categorías de bienes y servicios. Se aplica una tasa
intermedia del **12%** a las viviendas sociales y a los alimentos servidos en
restaurantes, mientras que se aplica una tasa reducida del **6%** a la mayoría
de los bienes básicos, como alimentos, suministro de agua, libros y
medicamentos. Para algunos bienes y servicios excepcionales, como algunas
publicaciones diarias y semanales (como bienes reciclados) se aplica una tasa
del **0%**.

### Impuestos no deducibles

En Bélgica, algunos impuestos no son deducibles en su totalidad, por ejemplo,
los impuestos sobre el mantenimiento de automóviles. Esto significa que una
parte de estos impuestos se considera un gasto.

En Odoo, puede configurar impuestos no deducibles mediante la creación de
reglas impositivas para estos y las vincula a las cuentas correspondientes. De
esta manera, el sistema calcula los impuestos en automático y los asigna a las
cuentas apropiadas.

Para configurar un nuevo impuesto no deducible, vaya a Contabilidad ‣
Configuración ‣ Contabilidad: impuestos, y haga clic en Nuevo:

  1. Agregue una línea y seleccione Base en la columna Con base en.

  2. Agregue una línea, luego seleccione en el impuesto en la columna Con base en e ingrese el porcentaje **no deducible** en la columna % .

  3. En la línea en el impuesto, seleccione las tablas de impuestos relacionadas a su impuesto.

  4. Agregue una línea con el porcentaje **deducible** en la columna %.

  5. Establezca en el impuesto en Con base en.

  6. Seleccione 411000 IVA recuperable como cuenta y seleccione la tabla de impuestos relacionada.

Una vez que haya creado un impuesto no deducible, puede aplicarlo a sus
transacciones si selecciona el impuesto correspondiente durante la
codificación de facturas y notas de crédito. El sistema calcula el importe del
impuesto de forma automática y lo asigna a las cuentas correspondientes según
las reglas de impuestos configuradas.

Example

Con la localización belga, el impuesto del **21% sobre automóviles** se crea
de forma predeterminada (50% no deducible).

![Ejemplo de un impuesto no deducible en su
totalidad](../../../_images/deductible-tax.png)

Ver también

  * [Impuestos](../accounting/taxes.html)

  * [Declaración de impuestos](../accounting/reporting/tax_returns.html)

## Reportes

Esta es la lista de reportes específicos de Alemania disponibles:

  * Balance general;

  * Estado de resultados;

  * Reporte de impuestos;

  * Listado de IVA del contacto,

  * Declaración recapitulativa de operaciones intracomunitarias,

  * Intrastat.

Puede acceder a las versiones para Bélgica de los reportes si hace clic en el
icono de **libro** de un reporte y selecciona su versión belga: **(BE)**.

![Versión para Bélgica de los reportes](../../../_images/belgian-reports.png)

Ver también

[Reportes](../accounting/reporting.html)

### Reporte de gastos rechazados

Los **gastos rechazados** son gastos que pueden deducirse de su resultado
contable pero no de su resultado fiscal.

El **reporte de gastos rechazados** está disponible en Contabilidad ‣ Reportes
‣ Gestión: gastos rechazados y este permite obtener sus resultados financieros
en tiempo real, así como cambios periódicos. Este reporte se genera según las
**categorías de gastos rechazados** que puede consultar desde Contabilidad ‣
Configuración ‣ Gestión: categorías de gastos rechazados. Algunas categorías
ya existen de forma predeterminadas pero no tienen tarifas. Haga clic en
Establecer tarifas para actualizar una categoría específica.

Truco

  * Puede agregar varias tarifas para distintas fechas. En ese caso, la tasa que se utiliza para calcular el gasto depende de la fecha en que se calcula y la tasa establecida para esa fecha.

  * Si tiene instalada la aplicación **Flota** , marque la casilla Categoría del vehículo cuando corresponda. Esto hace que el vehículo sea obligatorio al reservar una factura de proveedor.

Para vincular una categoría de gastos rechazados a una cuenta específica, vaya
a Contabilidad ‣ Configuración ‣ Contabilidad: plan de cuentas. Encuentre la
cuenta deseada y haga clic en Configurar. Agregue la categoría de gastos
rechazados al campo gastos rechazados. A partir de ahora, cuando se crea un
gasto con esta cuenta, se calcula el gasto rechazado en función de la tasa
mencionada en la categoría de gastos rechazados.

A continuación presentaremos un ejemplo que refleja los gastos de
**restaurante** y **automóvil**.

#### Gastos de restaurante

En Bélgica, el 31% de los gastos de **restaurante** no son deducibles. Cree
una nueva **categoría de gastos rechazados** y establezca las cuentas
relacionadas y la tasa actual.

![Categorías de gastos rechazados](../../../_images/restaurant-expenses.png)

#### Gastos de automóviles: separación de vehículos

En Bélgica, el porcentaje deducible varía de un automóvil a otro, por lo
tanto, se debe indicar para cada vehículo. Abra Flota y seleccione un
vehículo. En la pestaña Información fiscal vaya a la sección Tasa de gastos
rechazados y haga clic en Agregar una línea. Agregue una fecha de inicio y un
%. Los importes van a la misma cuenta para todos los gastos del automóvil.

Cuando crea una factura para los gastos del automóvil, puede vincular cada
gasto a un automóvil específico si completa la columna Vehículo para que se
aplique el porcentaje correcto.

![Categorías de gastos rechazados](../../../_images/car-bill.png)

La opción Separación de vehículos disponible en el reporte de gastos
rechazados le permite ver la tasa y el importe rechazado para cada automóvil.

![Categorías de gastos rechazados](../../../_images/vehicle-split.png)

## Formulario de impuestos 281.50 y formulario 325

### Formulario de impuestos 281.50

Cada año, se debe presentar un **formulario de impuestos 281.50** a las
autoridades fiscales. Para ello, debe agregar la etiqueta `281.50` al
formulario de contacto de las entidades afectadas por la tarifa **281.50**.
Para agregar la etiqueta, abra Contactos, seleccione la persona o empresa para
la que desea crear un **formulario de impuestos 281.50** y agregue la etiqueta
`281.50` al campo correspondiente.

![Agregar la etiqueta 281.50 a un formulario de
contacto.](../../../_images/281-50.png)

Nota

Asegúrese de que la **calle, código postal, país** y el **número de
identificación fiscal** también estén presentes en el **formulario de
contacto**.

Luego, según el tipo de gasto, agregue la etiqueta `281.50` correspondiente a
las cuentas afectadas. Vaya a Contabilidad ‣ Configuración ‣ Contabilidad:
plan de cuentas y haga clic en Configurar para agregar la etiqueta `281.50` en
las cuentas correspondientes, por ejemplo: 281.50 - Comisiones.

### Formulario 325

Puede crear un **formulario 325** desde Contabilidad ‣ Reportes ‣ Bélgica:
crear formulario 325. Aparecerá una nueva página, seleccione las opciones
correctas y haga clic en Generar formulario 325. Para abrir un **formulario
325** ya generado, vaya a Contabilidad ‣ Reportes ‣ Bélgica: abrir formularios
325.

![Agregar la etiqueta 281-50 a un formulario de
contacto.](../../../_images/325-form.png)

## Estados de cuenta CODA y SODA

### CODA

El formato XML electrónico **CODA** se utiliza para importar extractos
bancarios de Bélgica. Puede descargar archivos CODA de su banco e importarlos
directamente a Odoo, solo debe hacer clic en Importar estado de cuenta desde
el diario denominado banco en su tablero.

![Importar archivos CODA](../../../_images/coda-import.png)

Nota

El módulo Bélgica - Importar estados de cuenta bancarios CODA se instala de
forma predeterminada al instalar los módulos Bélgica - Contabilidad y Bélgica
- Reportes contables.

Ver también

[Importar archivos de estados de cuenta
bancarios](../accounting/bank/transactions.html#transactions-import)

### SODA

El formato XML electrónico **SODA** se utiliza para importar asientos
contables relacionados con los salarios. Los archivos SODA se pueden importar
al diario que utiliza para registrar sueldos desde su **tablero** de
Contabilidad, haga clic en Subir en el formulario de la tarjeta del diario
correspondiente.

Una vez que se importan sus archivos **SODA** , los asientos se crean de forma
automática en su diario “sueldos”.

![Importar archivos SODA](../../../_images/soda-import.png)

## Facturación electrónica

Odoo es compatible con los formatos de facturación electrónica **E-FFF** y
**Peppol BIS 3.0 (UBL)**. Para habilitarlos, vaya a Contabilidad ‣
Configuración ‣ Diarios ‣ Facturas de clientes ‣ Ajustes avanzados ‣
Facturación electrónica y marque E-FFF (BE) y Peppol BIS 3.0.

Ver también

[Facturación electrónica
(EDI)](../accounting/customer_invoices/electronic_invoicing.html)

## Descuento por pronto pago

En Bélgica, si se ofrece un descuento por pronto pago en una factura, el
impuesto se calcula sobre la base del importe total descontado, ya sea que el
cliente se beneficie del descuento o no.

Para aplicar el importe correcto al impuesto y colocarlo en su declaración
fiscal, seleccione Siempre (al facturar) al elegir la reducción de impuestos .

Ver también

[Descuentos por pronto pago y reducción de
impuestos](../accounting/customer_invoices/cash_discounts.html)

## Certificación fiscal: restaurante en PdV

Por ley, los propietarios de negocios de cocina como restaurantes o food
trucks en Bélgica deben utilizar un **sistema de caja registradora**
certificado por el gobierno para sus recibos. Esto aplica si sus ganancias
anuales (sin incluir IVA, bebidas y órdenes para llevar) exceden los 25 mil
euros.

Este sistema certificado por el gobierno requiere el uso de un sistema PdV
certificado, junto con un dispositivo denominado módulo de datos fiscales (o
**caja negra**) y una tarjeta de firma de IVA.

Importante

No olvide registrarse como _gerente en el sector de servicios de alimentos_ en
el [formulario de registro del Servicio Público Federal de
Finanzas](https://www.systemedecaisseenregistreuse.be/fr/enregistrement).

### Sistema PdV certificado

El sistema PdV de Odoo cuenta con certificación para las versiones principales
de bases de datos con alojamiento en **Odoo en línea** y **Odoo.sh**. Consulte
la siguiente tabla para asegurarse de que su sistema PdV cuenta con la
certificación.

| Odoo en línea | Odoo.sh | Local  
---|---|---|---  
Odoo 16.0 | Certificado | Certificado | Sin certificación  
Odoo 15.2 | Sin certificación | Sin certificación | Sin certificación  
Odoo 15.0 | Certificado | Certificado | Sin certificación  
Odoo 14.0 | Certificado | Certificado | Sin certificación  
  
Ver también

[Versiones compatibles](../../../administration/supported_versions.html)

Un [sistema PdV
certificado](https://www.systemedecaisseenregistreuse.be/systemes-certifies)
debe acatar la rigurosa normatividad gubernamental, lo que significa que opera
de forma distinta a los PdV que no tienen certificación.

  * Si su PdV está certificado, no puede:

    * Configurar y utilizar la función **descuentos globales** (el módulo `pos_discount` se agrega a la lista negra y no se puede activar).

    * Configurar y utilizar la función **programas de fidelidad** (el módulo `pos_loyalty` se agrega a la lista negra y no se puede activar).

    * Volver a imprimir recibos (el módulo `pos_reprint` se agrega a la lista negra y no se puede activar).

    * Modificar precios en las líneas de la orden.

    * Modificar o eliminar líneas en las órdenes de PdV.

    * Vender productos sin un número de IVA válido.

    * Utilizar un PdV que no esté conectado a una caja IoT.

  * La función [redondeo de efectivo](../../sales/point_of_sale/pricing/cash_rounding.html) debe estar activada y ajustada con una precisión de redondeo de `0,05` y un método de redondeo establecido como hacia arriba.

  * Debe configurar los impuestos para que estén incluidos en el precio. Para hacerlo, vaya a Punto de venta ‣ Configuración ‣ Ajustes. En la sección Contabilidad, abra el formulario de impuestos de venta predeterminados al hacer clic en la flecha junto al campo correspondiente. Ahí, haga clic en opciones avanzadas y habilite la función incluido en el precio.

  * Al iniciar una sesión de PdV, los usuarios deben hacer clic en empezar a trabajar para registrar su hora de entrada. Esto permite el registro de órdenes en el PdV. Si los usuarios no registran su hora de entrada, no podrán crear órdenes. Del mismo modo, deben hacer clic en terminar de trabajar para registrar su hora de salida al finalizar la sesión.

Advertencia

Si configura que un PdV trabaje con un Modulo de Datos Contables, no puede
usarlo de nuevo sin él.

### Módulo de datos fiscales (FDM, por sus siglas en inglés)

Un FDM o **caja negra** es un dispositivo certificado por el gobierno que
funciona en conjunto con la aplicación Punto de Venta y almacena la
información de sus órdenes del PdV. De forma más concreta, genera un **hash**
(código único) para cada orden del PdV y se agrega a su recibo. Esto permite
que el gobierno pueda verificar que se declaran todos los ingresos.

Advertencia

Solo el FDM de **Boîtenoire.be** con el [número de certificado FDM
BMC04](https://www.systemedecaisseenregistreuse.be/fr/systemes-
certifies#FDM%20certifiés) es compatible con Odoo. [Póngase en contacto con el
fabricante (GCV BMC)](https://www.boîtenoire.be/contact) para adquirir uno.

#### Configuración

Antes de configurar su base de datos para que utilice un FDM, asegúrese de
contar con los siguientes dispositivos:

  * un FDM **Boîtenoire.be** (número de certificado BMC04);

  * un cable de módem nulo serie RS-232 por cada FDM,

  * un adaptador de cable serie RS-232 a USB por cada FDM,

  * una Caja IoT (una caja IoT por FDM); y

  * una impresora de recibos.

##### Módulo de caja negra

Como requisito previo, debe [activar](../../general/apps_modules.html#general-
install) el módulo `Sistema de Bélgica de registro de pagos en efectivo`
(nombre técnico: `pos_blackbox_be`).

![Módulos de caja negra para la certificación fiscal de
Bélgica](../../../_images/be-modules.png)

Una vez que active el módulo, agregue su número de identificación fiscal a la
información de su empresa. Para configurarlo, vaya a Ajustes ‣ Empresas ‣
Actualizar información y complete el campo IVA. Después, introduzca un número
de registro nacional para cada trabajador que operará el sistema PdV. Para
hacerlo, vaya a Empleados y abra el formulario de un empleado. Ahí, vaya a la
pestaña de Ajustes RR. HH. ‣ Asistencia/Punto de venta y complete el campo
número INSZ o BIS.

![Campo de número ISNZ o BIS en el formulario del
empleado](../../../_images/bis-number.png)

Truco

Para ingresar su información, haga clic en su avatar, vaya a Mi perfil ‣
pestaña Preferencias y escriba su número INSZ o BIS en el campo
correspondiente.

Advertencia

Debe configurar el módulo de datos fiscales directamente en la base de datos
de producción. Si lo utiliza en un entorno de prueba puede ocasionar que se
almacenen datos incorrectos en el FDM.

##### Caja IoT

Para usar un Modulo de datos fiscales, necesita una caja IoT registrada. Para
hacerlo, debe ponerse en contacto con nosotros a través de nuestro [formulario
de contacto de asistencia](https://www.odoo.com/help) y proporcionar la
siguiente información:

  * su número de identificación fiscal,

  * el nombre, dirección y estructura legal de su empresa y

  * la dirección MAC de su caja IoT.

Una vez que su caja IoT esté certificada,
[conéctela](../../general/iot/config/connect.html) a su base de datos. Para
verificar que la caja IoT reconoce el FDM, vaya a la página de inicio de IoT y
busque la sección dispositivo IoT, el FDM debería aparecer ahí.

![Página de estado de hardware en una caja IoT
registrada](../../../_images/iot-devices.png)

Después, agregue la caja IoT a su PdV. Para hacerlo, vaya a Punto de venta ‣
Configuración ‣ Punto de venta, seleccione su PdV, baje a la sección
dispositivo conectado y habilite la caja IoT. Por último, agregue el FMD en el
campo módulo de datos fiscales.

Nota

Para utilizar un FDM debe conectar por lo menos una impresora de recibos.

### Tarjeta de firma de IVA

Cuando abre una sesión de PdV y realiza la transacción inicial, es necesario
que escriba el NIP de su tarjeta de firma de IVA. La tarjeta la entrega el
Servicio Público Federal de Finanzas al
[registrarse](https://www.systemedecaisseenregistreuse.be/fr/enregistrement).

  *[PCMN]: Plan Comptable Minimum Normalisé

