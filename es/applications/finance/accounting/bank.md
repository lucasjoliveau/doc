# Cuentas bancarias y de efectivo

En su base de datos puede administrar todas las cuentas bancarias o de
efectivo que necesite. Si las configura de la manera adecuada, podrá tener
toda su información bancaria al día y lista para la
[conciliación](bank/reconciliation) con sus asientos contables.

En Contabilidad de Konvergo ERP cada cuenta bancaria tiene un diario exclusivo para
registrar todas las entradas en una cuenta específica. Tanto el diario como la
cuenta se crean y configuran de forma automática cuando se agrega una cuenta
bancaria.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los diarios y cuentas de efectivo deben configurarse manualmente.</p>
</div>

Los diarios bancarios se muestran de forma predeterminada en el panel de
control de Contabilidad en forma de tarjetas que incluyen botones de acción.

![Los diarios bancarios aparecen en el tablero Contabilidad y contienen
botones de acción.](../../../_images/card.png)

## Administre sus cuentas bancarias y de efectivo.

### Conecte su banco para la sincronización automática.

Para conectar su cuenta bancaria a su base de datos, vaya a «Contabilidad ->
Configuración -> Bancos: Agregar una cuenta bancaria», seleccione su banco en
la lista, haga clic en «Conectar» y siga las instrucciones.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="bank/bank_synchronization">Sincronización bancaria</a></p>
</div>

### Crear una cuenta bancaria

Si su institución bancaria no está disponible en Konvergo ERP, o si no desea conectar
su cuenta bancaria a su base de datos, puede configurar su cuenta bancaria de
forma manual.

Para agregar de forma manual una cuenta bancaria, vaya a «Contabilidad ->
Configuración -> Bancos: Agregar una cuenta bancaria», haga clic en «Crear»
(en la parte inferior derecha) y complete el formulario.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Konvergo ERP detecta en automático el tipo de cuenta bancaria (por ejemplo, IBAN) y, por consiguiente, habilita algunas funciones.</p></li>
<li><p>Hay disponible un diario bancario predeterminado que se puede utilizar para configurar su cuenta bancaria yendo a «Contabilidad -&gt; Configuración -&gt; Contabilidad: Diarios -&gt; Bancos». Ábralo y edite los diferentes campos para que coincidan con la información de su cuenta bancaria.</p></li>
</ul>
</div>

### Crear un diario de efectivo

Para crear un nuevo diario de efectivo, vaya a Contabilidad ‣ Configuración ‣
Contabilidad: Diarios, haga clic en **Crear** y seleccione **Efectivo** en el
campo **Tipo**.

Para obtener más información sobre los campos de información contable, lea la
sección Configuración de esta página.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Un diario de efectivo predeterminado está disponible y se puede utilizar de inmediato. Puede revisarlo yendo a Contabilidad ‣ Configuración ‣ Contabilidad: Diarios ‣ Efectivo.</p>
</div>

### Editar un diario bancario o de efectivo existente

Para editar un diario bancario existente, vaya a Contabilidad ‣ Configuración
‣ Contabilidad: Diarios y escoja el diario que desea modificar.

## Configuración

Puede editar la información contable y el número de cuenta bancaria de acuerdo
con sus necesidades.

![Configure manualmente su información bancaria](../../../_images/bank-
journal-config.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="get_started/multi_currency">Sistema multidivisa</a></p></li>
<li><p><a href="bank/transactions">Transacciones</a></p></li>
</ul>
</div>

### Cuenta transitoria

Las transacciones del extracto bancario se registran en la :guilabel:`Cuenta
transitoria hasta que la conciliación final permita encontrar la cuenta
correcta.

### Cuentas del estado de resultados

La **Cuenta de ganancias** se utiliza para registrar una ganancia cuando el
saldo final de una caja registradora difiere del que el sistema calcula,
mientras que la **Cuenta de pérdidas** se utiliza para registrar una pérdida
cuando el saldo final de una caja registradora difiere del que el sistema
calcula.

### Moneda

Puede editar la moneda utilizada para ingresar los extractos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="get_started/multi_currency">Sistema multidivisa</a></p>
</div>

### Número de cuenta

Si necesita **editar los detalles de su cuenta bancaria** , haga clic en la
flecha de enlace externo junto a su **Número de cuenta**. En la nueva página,
haga clic en la flecha de enlace externo junto a su **Banco** y actualice tu
información bancaria como corresponda. Estos detalles se utilizan al registrar
los pagos.

![Edite su información bancaria](../../../_images/bank-account-number.png)

### Conexiones bancarias

**Conexiones bancarias** define cómo se registran los estados de cuenta
bancarios. Hay tres opciones disponibles:

  * **Aún no definido** , debe seleccionarse cuando aún no se sabe si se sincronizará o no la cuenta bancaria con la base de datos.

  * **Importar (CAMT, CODA, CSV, OFX, QIF)** , debe seleccionarse si se desea importar el estado de cuenta bancario utilizando un formato diferente.

  * **Sincronización bancaria automatizada** , debe seleccionarse si su banco está sincronizado con la base de datos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="bank/bank_synchronization">Sincronización bancaria</a></p></li>
<li><p><a href="bank/transactions">Transacciones</a></p></li>
</ul>
</div>

## Cuentas pendientes

De forma predeterminada, los pagos se registran a través de cuentas
transitorias llamadas **cuentas pendientes** antes de registrarlos en su
cuenta bancaria.

  * Una **cuenta de pagos pendientes** es donde se registran los pagos salientes hasta que se vinculan con un retiro de su estado de cuenta bancario.

  * Una **cuenta de cobros pendientes** es donde se registran los pagos entrantes hasta que se vinculan con un depósito en su estado de cuenta bancario.

Estas cuentas deben ser del [tipo](get_started/chart_of_accounts#chart-
of-account-type) **Activos corrientes**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El movimiento desde una cuenta pendiente a una cuenta bancaria se realiza automáticamente cuando concilia la cuenta bancaria con un estado de cuenta bancario.</p>
</div>

### Configuración predeterminada de cuentas

Las cuentas pendientes se definen de manera predeterminada. Si es necesario,
puede actualizarlas yendo a Contabilidad ‣ Configuración ‣ Configuración ‣
Cuentas predeterminadas y actualizar su **Cuenta de cobros pendientes** y
**Cuenta de pagos pendientes**.

### Configuración de diarios bancarios y en efectivo

También puede establecer cuentas pendientes específicas para cualquier diario
del [tipo](get_started/chart_of_accounts#chart-of-account-type) **Banco**
o **Efectivo**.

Desde el **Tablero de control de Contabilidad** , haga clic en la selección de
menú ⋮ del diario que desea configurar, y haga clic en **Configuración** ,
luego abra la pestaña **Pagos entrantes/salientes**. Para mostrar la columna
de cuentas pendientes, haga clic en el botón de alternancia y marque la
casilla de **Cuentas de cobros/pagos pendientes** , luego actualice la cuenta.

![Seleccione el botón de alternancia y haga clic en Cuentas
pendientes](../../../_images/toggle-button.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si no especifica una cuenta de pagos pendientes o una cuenta de cobros pendientes para un diario específico, Konvergo ERP utilizará las cuentas pendientes predeterminadas.</p></li>
<li><p>Si su cuenta bancaria principal se agrega como una cuenta de cobros pendientes o una cuenta de pagos pendientes, cuando se registra un pago, el estado de la factura o el recibo se establece directamente en <b>Pagado</b>.</p></li>
</ul>
</div>

  * [Sincronización bancaria](bank/bank_synchronization)
    * [Salt Edge](bank/bank_synchronization/saltedge)
    * [Ponto](bank/bank_synchronization/ponto)
    * [Enable Banking](bank/bank_synchronization/enablebanking)
  * [Transacciones](bank/transactions)
  * [Conciliación bancaria](bank/reconciliation)
  * [Modelos de conciliación](bank/reconciliation_models)
  * [Gestione una cuenta bancaria en una moneda extranjera](bank/foreign_currency)
  * [Caja registradora](bank/cash_register)

