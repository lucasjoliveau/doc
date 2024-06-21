# Información básica

Cuando abre por primera vez su aplicación Contabilidad, la página _Información
general de contabilidad_ le da la bienvenida con un panel de integración paso
a paso, un asistente que le ayuda a empezar. Este panel de integración se
muestra hasta que decide cerrarlo.

Los ajustes visibles en el panel de integración podrán modificarse más tarde
en Contabilidad ‣ Configuración ‣ Ajustes.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La aplicación Contabilidad instala de manera automática el <b>paquete de localización fiscal</b> correspondiente a su empresa dependiendo del país que se seleccionó en la base de datos. Las cuentas, los reportes y los impuestos correctos estarán disponibles de inmediato. <a href="../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Haga clic aquí</span></a> para aprender más sobre los paquetes de localización fiscal.</p>
</div>

## Panel de integración de Contabilidad

El panel de integración de Contabilidad se compone de cuatro pasos:

![Panel de integración paso a paso en la aplicación Contabilidad de
Konvergo ERP](../../../_images/setup_accounting_onboarding.png)

  1. Datos de la empresa

  2. Cuenta bancaria

  3. Periodos contables

  4. Plan de cuentas

### Datos de la empresa

Este menú le permite agregar los detalles de su empresa como el nombre,
dirección, logo, sitio web, teléfono, correo electrónico y NIF. Estos detalles
se muestran en sus documentos, como las facturas.

![Agregue los detalles de su empresa en las aplicaciones Contabilidad y
Facturación de Konvergo ERP](../../../_images/setup_company.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede cambiar estos ajustes en Ajustes‣ Ajustes generales ‣ Ajustes ‣ Empresas al hacer clic en <b>Actualizar información</b>.</p>
</div>

### Cuenta bancaria

Conecte su cuenta bancaria a su base de datos y sincronice automáticamente sus
estados de cuenta bancarios. Para hacerlo, busque su banco en la lista, haga
clic en _Conectar_ , y siga las instrucciones.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><a href="bank/bank_synchronization">Haga clic aquí</a> para obtener más información sobre esta función.</p>
</div>

Si su institución bancaria no se puede sincronizar automáticamente, o si
prefiere no sincronizarla con su base de datos, también puede configurar su
cuenta bancaria de forma manual al hacer clic en _Crearla_ y completar el
formulario.

  * **Nombre** : el nombre de la cuenta bancaria, tal como se muestra en Konvergo ERP.

  * **Número de cuenta** : su número de cuenta bancaria (IBAN en Europa).

  * **Banco** : haga clic en _Crear y editar_ para configurar los detalles del banco. Añada el nombre de la entidad y su identificador (BIC o SWIFT).

  * **Código** : este código es el _código corto_ del diario, tal como se muestra en Konvergo ERP. Automáticamente Konvergo ERP crea un nuevo diario con este código corto.

  * **Diario** : Este campo se muestra si tiene un diario bancario existente que todavía no esté vinculado a una cuenta bancaria. Si es así, seleccione el «Diario» que quiera usar para registrar las transacciones financieras de esta cuenta bancaria o cree uno nuevo haciendo clic en _Crear y editar_.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Con esta herramienta puede agregar tantas cuentas como necesite en Contabilidad ‣ Configuración, al hacer clic en <em>Agregar una cuenta bancaria</em>.</p></li>
<li><p><a href="bank">Haga clic aquí</a> para obtener más información sobre las cuentas bancarias.</p></li>
</ul>
</div>

### Periodos contables

Defina aquí las fechas de apertura y cierre de sus **años fiscales** que se
usan para generar reportes automáticamente y la **periodicidad de declaración
de impuestos** , junto con un recordatorio para no olvidar las fechas límite
de declaración.

De forma predeterminada, la fecha de apertura se establece en el 1 de enero y
la de cierre en el 31 de diciembre, ya que es el uso más común.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede cambiar estos ajustes en Contabilidad ‣ Configuración ‣ Ajustes ‣ Periodos fiscales y modificando los valores.</p>
</div>

### Plan de cuentas

Con este menú, puede agregar cuentas al **plan de cuentas** e indicar sus
balances iniciales.

En esta página se muestran los ajustes básicos para ayudarle a revisar su plan
de cuentas. Para acceder a todos los ajustes de una cuenta, haga clic en el
_botón de doble flecha_ al final de la línea.

![Configuración del plan de cuentas y sus balances de apertura en la
aplicación Contabilidad de Konvergo ERP](../../../_images/setup_chart_of_accounts.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><a href="get_started/chart_of_accounts">Haga clic aquí</a> para obtener más información sobre cómo configurar su plan de cuentas.</p>
</div>

## Panel de integración de Facturación

Hay otro panel de integración paso a paso que le ayuda a aprovechar las
aplicaciones Facturación y Contabilidad de Konvergo ERP. El _panel de integración de
Facturación_ es el que le da la bienvenida si usa Facturación en lugar de
Contabilidad.

Si instaló la aplicación Contabilidad en su base de datos, puede acceder en
Contabilidad ‣ Clientes ‣ Facturas.

El panel de integración de Facturación se compone de cuatro pasos principales:

![Panel de integración paso a paso en la aplicación Facturación de
Konvergo ERP](../../../_images/setup_invoicing_onboarding.png)

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
página_. Tome en cuenta que Konvergo ERP agrega automáticamente el teléfono de la
empresa, correo electrónico, URL del sitio web y número de identificación
fiscal al pie de página, de acuerdo con los valores que usted haya configurado
en la Información de la empresa.

![Configuración del diseño del documento en la aplicación Facturación de
Konvergo ERP](../../../_images/setup_document_layout.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Añada su <b>número de cuenta bancaria</b> y un enlace a sus <b>términos y condiciones generales</b> en el pie de página. De esta manera, sus contactos pueden encontrar en línea el contenido completo de sus condiciones sin necesidad de imprimirlas en todas las facturas que emita.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Estos ajustes también se pueden modificar en Ajustes ‣ Ajustes generales, en la sección <em>Documentos empresariales</em>.</p>
</div>

### Método de pago

Este menú ayuda a configurar los métodos de pago con los que los clientes
pueden pagar.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Configurar un <em>proveedor de pago</em> con esta herramienta también activa la opción <em>Pago electrónico de factura</em> de forma automática. Con esto, los usuarios pueden pagar en línea directamente desde su portal de cliente.</p>
</div>

### Factura de muestra

Envíese una factura a sí mismo para asegurarse de que todo está configurado
correctamente.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="bank">Cuentas bancarias y de efectivo</a></p></li>
<li><p><a href="get_started/chart_of_accounts">Plan de cuentas</a></p></li>
<li><p><a href="bank/bank_synchronization">Sincronización bancaria</a></p></li>
<li><p><a href="../fiscal_localizations">Localizaciones fiscales</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/getting-started-1692">Tutoriales de Konvergo ERP: contabilidad y facturación - principios básicos [video]</a></p></li>
</ul>
</div>

  * [Hoja de referencia de Contabilidad](get_started/cheat_sheet)
  * [Plan de cuentas](get_started/chart_of_accounts)
  * [Sistema multidivisa](get_started/multi_currency)
  * [Costo promedio en bienes devueltos](get_started/avg_price_valuation)
  * [Unidades de IVA](get_started/vat_units)

