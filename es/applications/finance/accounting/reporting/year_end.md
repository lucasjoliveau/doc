# Cierre del ejercicio

El cierre del año fiscal es de suma importancia para que las finanzas sean
correctas, cumplan con las leyes, los reportes sean transparentes y así
podamos tomar decisiones informadas.

## Años fiscales

El año fiscal dura 12 meses y termina el 31 de diciembre de forma
predeterminada, pero la duración y fecha final pueden variar debido a
cuestiones culturales, administrativas o económicas.

Para modificar estos valores, vaya a Contabilidad ‣ Configuración ‣ Ajustes.
El campo Último día se encuentra en la sección Periodos fiscales, cámbielo si
es necesario.

Si el periodo dura _más_ o _menos_ de 12 meses, habilite los años fiscales y
guarde, para esto regrese a la sección de periodos fiscales y haga clic en ➜
Años fiscales. Haga clic en Crear, póngale nombre y fechas de inicio y
finalización.

Nota

Una vez transcurrido el periodo fiscal establecido, Odoo volverá a utilizar
automáticamente la periodicidad predeterminada, considerando el valor
especificado en el campo Último día.

## Tareas a realizar antes de terminar el año fiscal

### Antes del cierre

Antes de cerrar el ejercicio, asegúrese de que todo esté al día y sea
correcto:

  * Asegúrese de que todas las cuentas bancarias estén totalmente [conciliadas](../bank/reconciliation.html) hasta final de año, a su vez, confirme que los balances contables finales coincidan con los saldos de los estados de cuenta bancarios.

  * Compruebe que todas las [facturas de clientes](../customer_invoices.html) se hayan registrado y aprobado y que no queden borradores de facturas.

  * Compruebe que se hayan registrado y aceptado todas las [facturas de proveedores](../vendor_bills.html).

  * Compruebe que todos los [gastos](../../expenses.html) sean correctos.

  * Compruebe que todos los [pagos recibidos](../payments.html) se hayan codificado y registrado correctamente.

  * Cierre todas las cuentas [transitorias](../bank.html#bank-accounts-suspense).

  * Registre todos los asientos de [depreciación](../vendor_bills/assets.html) e [ingresos diferidos](../customer_invoices/deferred_revenues.html).

### Cierre de año fiscal

Lo siguiente es cerrar el año fiscal:

  * Realice un reporte [fiscal](../reporting.html#reporting-tax-report), y verifique que toda la información fiscal sea correcta.

  * Concilie todas las cuentas en el [balance general](../reporting.html#reporting-balance-sheet):

    * Actualice los balances bancarios en Odoo de acuerdo con los balances reales encontrados en los estados de cuenta bancarios.

    * Concilie las transacciones de las cuentas bancarias y de caja al ejecutar los reportes [cuentas antiguas por cobrar](../reporting.html#reporting-aged-receivable) y [cuentas antiguas por pagar](../reporting.html#reporting-aged-payable).

    * Audite todas sus cuentas, y asegúrese de entender perfectamente todas las transacciones y su naturaleza, además, no olvide incluir préstamos y activos fijos si los tiene.

    * Si lo desea, puede ejecutar la función [conciliación de pagos](../payments.html#payments-matching) para validar las facturas de proveedores y clientes pendientes con sus pagos. Este paso es opcional, sin embargo, si se concilian todos los pagos y facturas pendientes, puede ayudar al proceso de cierre de año ya que se podrían encontrar errores en el sistema.

Es probable que su contador deseé verificar el balance general y los asientos
de diario de:

>   * ajustes manuales para el cierre de año,
>
>   * trabajo en proceso,
>
>   * asientos de amortización
>
>   * préstamos,
>
>   * ajustes fiscales,
>
>   * etc.
>
>

Si su contador está realizando la auditoría de fin de año, es probable que
quiera tener copias físicas de todos los elementos del balance (como
préstamos, cuentas bancarias, pagos anticipados, declaraciones de impuestos
sobre las ventas, etc…) para compararlos con sus balances de Odoo.

Truco

Durante este proceso, una buena práctica es establecer una fecha de bloqueo de
asientos contables en el último día (inclusive) del año fiscal anterior, si
desea hacerlo, vaya a Contabilidad ‣ Contabilidad ‣ Fechas de bloqueo. De esta
forma, su contador podrá estar seguro de que nadie modificará las
transacciones mientras realiza la auditoría de los libros. Los usuarios del
grupo de acceso _contable_ podrán seguir creando y modificando asientos.

#### Ganancias del año en curso

Odoo utiliza un tipo de cuenta único llamado **ganancias del año en curso**
para mostrar la diferencia de cantidad entre las cuentas de **ingresos** y
**gastos**.

Nota

El plan de cuentas solo puede contener una cuenta de este tipo. Como opción
predeterminada, se trata de una cuenta 999999 denominada Ganancias/pérdidas no
distribuidas.

Para asignar los beneficios del año en curso, cree un asiento diverso para
registrarlo en cualquier cuenta del capital. Después, confirme si los
beneficios del año en curso en el **balance** reportan correctamente un saldo
de cero. Si es así, establezca una fecha de bloqueo para todos los usuarios en
el último día del año fiscal en Contabilidad ‣ Contabilidad ‣ Fechas de
bloqueo.

Truco

Instale el módulo Fecha de bloqueo irreversible (`account_lock`) para que la
fecha de bloqueo para todos los usuarios sea _irreversible_ una vez
configurada.

Nota

Un asiento específico de cierre de ejercicio es **opcional** para cerrar el
**estado de resultados**. Los reportes se crean en tiempo real, lo que
significa que el estado de resultados corresponde directamente con la fecha de
cierre de año especificada en Odoo. Por lo tanto, cada vez que se genera el
**estado de resultados** , la fecha de inicio corresponde con el inicio del
**año fiscal** y todos los balances de las cuentas deben ser iguales a cero.

