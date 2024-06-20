# Información básica

Cuando abre por primera vez su aplicación Contabilidad, la página _Información
general de contabilidad_ le da la bienvenida con un panel de integración paso
a paso, un asistente que le ayuda a empezar. Este panel de integración se
muestra hasta que decide cerrarlo.

Los ajustes visibles en el panel de integración podrán modificarse más tarde
en Contabilidad ‣ Configuración ‣ Ajustes.

Nota

La aplicación Contabilidad instala de manera automática el **paquete de
localización fiscal** correspondiente a su empresa dependiendo del país que se
seleccionó en la base de datos. Las cuentas, los reportes y los impuestos
correctos estarán disponibles de inmediato. [Haga clic
aquí](../fiscal_localizations.html#fiscal-localizations-packages) para
aprender más sobre los paquetes de localización fiscal.

## Panel de integración de Contabilidad

El panel de integración de Contabilidad se compone de cuatro pasos:

![Panel de integración paso a paso en la aplicación Contabilidad de
Odoo](../../../_images/setup_accounting_onboarding.png)

  1. Datos de la empresa

  2. Cuenta bancaria

  3. Periodos contables

  4. Plan de cuentas

### Datos de la empresa

Este menú le permite agregar los detalles de su empresa como el nombre,
dirección, logo, sitio web, teléfono, correo electrónico y NIF. Estos detalles
se muestran en sus documentos, como las facturas.

![Agregue los detalles de su empresa en las aplicaciones Contabilidad y
Facturación de Odoo](../../../_images/setup_company.png)

Nota

También puede cambiar estos ajustes en Ajustes‣ Ajustes generales ‣ Ajustes ‣
Empresas al hacer clic en **Actualizar información**.

### Cuenta bancaria

Conecte su cuenta bancaria a su base de datos y sincronice automáticamente sus
estados de cuenta bancarios. Para hacerlo, busque su banco en la lista, haga
clic en _Conectar_ , y siga las instrucciones.

Nota

[Haga clic aquí](bank/bank_synchronization.html) para obtener más información
sobre esta función.

Si su institución bancaria no se puede sincronizar automáticamente, o si
prefiere no sincronizarla con su base de datos, también puede configurar su
cuenta bancaria de forma manual al hacer clic en _Crearla_ y completar el
formulario.

  * **Nombre** : el nombre de la cuenta bancaria, tal como se muestra en Odoo.

  * **Número de cuenta** : su número de cuenta bancaria (IBAN en Europa).

  * **Banco** : haga clic en _Crear y editar_ para configurar los detalles del banco. Añada el nombre de la entidad y su identificador (BIC o SWIFT).

  * **Código** : este código es el _código corto_ del diario, tal como se muestra en Odoo. Automáticamente Odoo crea un nuevo diario con este código corto.

  * **Diario** : Este campo se muestra si tiene un diario bancario existente que todavía no esté vinculado a una cuenta bancaria. Si es así, seleccione el «Diario» que quiera usar para registrar las transacciones financieras de esta cuenta bancaria o cree uno nuevo haciendo clic en _Crear y editar_.

Nota

  * Con esta herramienta puede agregar tantas cuentas como necesite en Contabilidad ‣ Configuración, al hacer clic en _Agregar una cuenta bancaria_.

  * [Haga clic aquí](bank.html) para obtener más información sobre las cuentas bancarias.

### Periodos contables

Defina aquí las fechas de apertura y cierre de sus **años fiscales** que se
usan para generar reportes automáticamente y la **periodicidad de declaración
de impuestos** , junto con un recordatorio para no olvidar las fechas límite
de declaración.

De forma predeterminada, la fecha de apertura se establece en el 1 de enero y
la de cierre en el 31 de diciembre, ya que es el uso más común.

Nota

También puede cambiar estos ajustes en Contabilidad ‣ Configuración ‣ Ajustes
‣ Periodos fiscales y modificando los valores.

### Plan de cuentas

Con este menú, puede agregar cuentas al **plan de cuentas** e indicar sus
balances iniciales.

En esta página se muestran los ajustes básicos para ayudarle a revisar su plan
de cuentas. Para acceder a todos los ajustes de una cuenta, haga clic en el
_botón de doble flecha_ al final de la línea.

![Configuración del plan de cuentas y sus balances de apertura en la
aplicación Contabilidad de Odoo](../../../_images/setup_chart_of_accounts.png)

Nota

[Haga clic aquí](get_started/chart_of_accounts.html) para obtener más
información sobre cómo configurar su plan de cuentas.

## Panel de integración de Facturación

Hay otro panel de integración paso a paso que le ayuda a aprovechar las
aplicaciones Facturación y Contabilidad de Odoo. El _panel de integración de
Facturación_ es el que le da la bienvenida si usa Facturación en lugar de
Contabilidad.

Si instaló la aplicación Contabilidad en su base de datos, puede acceder en
Contabilidad ‣ Clientes ‣ Facturas.

El panel de integración de Facturación se compone de cuatro pasos principales:

![Panel de integración paso a paso en la aplicación Facturación de
Odoo](../../../_images/setup_invoicing_onboarding.png)

  1. Datos de la empresa

  2. Diseño de factura

  3. Método de pago

  4. Factura de muestra

### Datos de la empresa

Este formulario es el mismo que el que se presenta en el panel de integración
de Contabilidad.

### Diseño de factura

Con esta herramienta, puede diseñar la apariencia de sus documentos al
seleccionar qué plantilla de diseño, formato de papel, colores, fuentes y logo
quiere usar.

También puede añadir el _lema de su empresa_ y el contenido del _pie de
página_. Tome en cuenta que Odoo agrega automáticamente el teléfono de la
empresa, correo electrónico, URL del sitio web y número de identificación
fiscal al pie de página, de acuerdo con los valores que usted haya configurado
en la Información de la empresa.

![Configuración del diseño del documento en la aplicación Facturación de
Odoo](../../../_images/setup_document_layout.png)

Truco

Añada su **número de cuenta bancaria** y un enlace a sus **términos y
condiciones generales** en el pie de página. De esta manera, sus contactos
pueden encontrar en línea el contenido completo de sus condiciones sin
necesidad de imprimirlas en todas las facturas que emita.

Nota

Estos ajustes también se pueden modificar en Ajustes ‣ Ajustes generales, en
la sección _Documentos empresariales_.

### Método de pago

Este menú ayuda a configurar los métodos de pago con los que los clientes
pueden pagar.

Importante

Configurar un _proveedor de pago_ con esta herramienta también activa la
opción _Pago electrónico de factura_ de forma automática. Con esto, los
usuarios pueden pagar en línea directamente desde su portal de cliente.

### Factura de muestra

Envíese una factura a sí mismo para asegurarse de que todo está configurado
correctamente.

Ver también

  * [Cuentas bancarias y de efectivo](bank.html)

  * [Plan de cuentas](get_started/chart_of_accounts.html)

  * [Sincronización bancaria](bank/bank_synchronization.html)

  * [Localizaciones fiscales](../fiscal_localizations.html)

  * [Tutoriales de Odoo: contabilidad y facturación - principios básicos [video]](https://www.odoo.com/slides/slide/getting-started-1692)

  * [Hoja de referencia de Contabilidad](get_started/cheat_sheet.html)
  * [Plan de cuentas](get_started/chart_of_accounts.html)
  * [Sistema multidivisa](get_started/multi_currency.html)
  * [Costo promedio en bienes devueltos](get_started/avg_price_valuation.html)
  * [Unidades de IVA](get_started/vat_units.html)

