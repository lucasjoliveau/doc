# Plan de cuentas

El **plan de cuentas (COA)** es la lista de todas las cuentas que se usan para
registrar transacciones financieras en el libro mayor de una empresa. Puede
encontrar los planes de cuentas en Contabilidad‣Configuración‣Plan de cuentas.

Al buscar su plan de cuentas, puede organizarlas por Código, Nombre de la
cuenta o Tipo, pero hay más opciones disponibles en el menú desplegable (⋮).

![Agrupar las cuentas por tipo en la aplicación Contabilidad de
Odoo](../../../../_images/chart-of-accounts-sort.png)

## Configuración de una cuenta

El país que seleccione al crear sus base de datos (o una empresa adicional en
su base de datos) determina qué [paquete de localización
fiscal](../../fiscal_localizations.html) se instala de manera predeterminada.
Este paquete incluye un plan de cuentas estándar ya configurado de acuerdo con
las normas del país. Puede usarlo directamente o configurarlo según las
necesidades de su empresa.

Para crear una nueva cuenta, vaya a Contabilidad‣Configuración‣Plan de
cuentas, haga clic en Crear y complete (al mínimo) los campos requeridos
(Código, Nombre de la cuenta, Tipo).

Advertencia

No es posible modificar la **localización fiscal** de una empresa una vez que
se haya registrado un asiento contable.

### Código y nombre

Puede identificar cada cuenta con su Código y Nombre, el cual indica también
el propósito de la cuenta.

### Tipo

Es muy importante configurar de forma correcta el **tipo de cuenta**. Hacerlo
tiene varios objetivos:

  * Información del propósito y comportamiento de la cuenta

  * Generar reportes legales y financieros específicos del país

  * Establecer las reglas para cerrar el año fiscal

  * Generar asientos de apertura

Para configurar un tipo de cuenta, abra el menú desplegable del campo Tipo y
seleccione el tipo correspondiente de la siguiente lista:

Reporte | Categoría | Tipos de cuentas  
---|---|---  
Balance general | Activos | Cuentas por cobrar  
Banco y efectivo  
Activos circulantes  
Activos no circulantes  
Prepagos  
Activos fijos  
Pasivos | Cuentas por pagar  
Tarjeta de crédito  
Pasivo circulantes  
Pasivos no circulantes  
Capital | Capital  
Ganancias del año actual  
Ganancias y pérdidas | Ingresos | Ingresos  
Otros ingresos  
Gastos | Gastos  
Depreciación  
Costo de ingresos  
Otro | Otro | Hoja fuera de balance  
  
#### Automatización de activos y gastos e ingresos diferidos

Algunos **tipos de cuentas** pueden **automatizar** la creación de asientos de
[activos](../vendor_bills/assets.html#assets-automation), de [gastos
diferidos](../vendor_bills/deferred_expenses.html#deferred-expenses-
automation) y de [ingresos
diferidos](../customer_invoices/deferred_revenues.html#deferred-revenues-
automation). Para **automatizar** asientos. haga clic en Configurar en una
línea contable y vaya a la pestaña Automatización.

Hay tres opciones disponibles en la pestaña Automatización:

  1. No: es el valor predeterminado. No pasa nada.

  2. Crear en borrador: cuando se publica una transacción en la cuenta, se crea un borrador de un asiento, pero no se valida. Debe llenar el formulario correspondiente.

  3. Crear y validar: también debe seleccionar un modelo de gastos diferidos. Cuando una transacción se publica en la cuenta, se crea un asiento y se valida de inmediato.

### Impuestos predeterminados

En el menú de configuración de una cuenta, debe seleccionar un **impuesto
predeterminado** para que se aplique cuando elija esta cuenta para la venta de
un producto o una compra.

### Etiquetas

Algunos reportes contables requieren **etiquetas** que deben configurarse en
las cuentas correspondientes. Para agregar una etiqueta, en Configurar, haga
clic en el campo Etiquetas y seleccione una etiqueta correspondiente o puede
Crear una nueva.

### Grupos de cuentas

Los **grupos de cuentas** sirven para marcar varias cuentas como _subcuentas_
de una cuenta más grande y, por lo tanto, consolidar reportes como la
**Balanza de comprobación». De manera predeterminada, los grupos se gestionan
automáticamente según el código del grupo. Por ejemplo, una nueva cuenta
`131200` será parte del grupo `131000`. Puede ubicar una cuenta en un grupo
específico en el campo Grupo en Configurar.

#### Crear grupos de cuentas de forma manual

Nota

Los usuarios normales no deberían necesitar crear grupos de cuentas de forma
manual. La siguiente sección solo está pensada para casos de uso poco
frecuentes y avanzados.

Para crear un nuevo grupo de cuentas, active el [modo
desarrollador](../../../general/developer_mode.html#developer-mode) y vaya a
Contabilidad‣Configuración‣Grupos de cuentas. Desde aquí, cree un nuevo grupo
y escriba el nombre, código, prefijo y empresa para los cuales estará
disponible ese grupo. Tenga en cuenta que debe escribir el mismo prefijo de
código en los campos de y a.

![Creación de grupos de cuentas.](../../../../_images/account-groups.png)

Para mostrar su reporte de **balanza de comprobación** con sus grupos de
cuentas, vaya a Contabilidad‣Reportes‣Balanza de comprobación, luego abra el
menú de opciones y seleccione Jerarquía y subtotales.

![Grupos de cuentas en el balance de comprobación en la aplicación
Contabilidad de Odoo](../../../../_images/chart-of-accounts-groups.png)

### Permitir conciliaciones

Algunas cuentas, como las que registran transacciones de un método de pago, se
pueden usar para conciliar los asientos contables.

Por ejemplo, una factura que se pagó con una tarjeta de crédito puede marcarse
como pagada si se concilia con el pago correspondiente. Por lo tanto, la
cuenta que se utiliza para registrar pagos con tarjeta de crédito se debe
configurar para **permitir conciliaciones**.

Para hacerlo, seleccione la casilla de Permitir conciliaciones en los ajustes
de la cuenta, y haga clic en Guardar; o active el botón desde la vista del
plan de cuentas.

![Permitir la conciliación de cuentas en Contabilidad de
Odoo](../../../../_images/chart-of-accounts-reconciliation.png)

### Obsoleta

No es posible eliminar una cuenta una vez que se registró una transacción en
ella. Puede desactivarlas usando la función de **Obsoleta** : seleccione la
casilla Obsoleta en los ajustes de la cuenta y haga clic en Guardar.

Ver también

  * [Hoja de referencia de Contabilidad](cheat_sheet.html)

  * [Activos no circulantes y fijos](../vendor_bills/assets.html)

  * [Gastos diferidos y prepagos](../vendor_bills/deferred_expenses.html)

  * [Ingresos diferidos](../customer_invoices/deferred_revenues.html)

  * [Localizaciones fiscales](../../fiscal_localizations.html)

  * [Tutoriales de Odoo: plan de cuentas](https://www.odoo.com/slides/slide/chart-of-accounts-1630)

  * [Tutoriales de Odoo: actualiza tu plan de cuenta](https://www.odoo.com/slides/slide/update-your-chart-of-accounts-1658)

