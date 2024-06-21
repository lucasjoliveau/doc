# Conciliación bancaria

**Conciliación Bancaria** es el proceso de conciliar sus [transacciones
bancarias](transactions) con los registros de su empresa, como las
[facturas de clientes](../customer_invoices), [de
proveedores](../vendor_bills) y [pago](../payments). No solo es
obligatorio para la mayoría de las empresas, sino que también ofrece varias
ventajas, como la reducción del riesgo de errores en los reportes financieros,
la detección de actividades fraudulentas y la mejora de la gestión del flujo
de caja.

Gracias a los modelos de [conciliación bancaria](reconciliation_models),
Konvergo ERP preselecciona automáticamente los asientos a conciliar.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/bank-reconciliation-2724">Tutoriales de Konvergo ERP: conciliación bancaria</a></p></li>
<li><p><a href="bank_synchronization">Sincronización bancaria</a></p></li>
<li><p><span class="xref std std-doc">transacciones</span></p></li>
</ul>
</div>

## Vista de conciliación bancaria

Para acceder a la **vista de conciliación** vaya al **tablero de
Contabilidad** y:

  * haga clic en el nombre del diario (por ejemplo, **banco**) para mostrar todas las transacciones, incluidas las que ya están conciliadas, o

  * haga clic en el botón **Conciliar apuntes** para mostrar todas las transacciones preseleccionadas por Konvergo ERP para la conciliación. Puede eliminar el filtro **no conciliadas** de la barra de búsqueda para incluir transacciones ya conciliadas.

![Imagen donde se muestra cómo accedar a la herramienta de conciliación
bancaria desde el tablero de contabilidad. ](../../../../_images/bank-
card.png)

La vista de la conciliación bancaria se estructura en tres secciones
diferentes: transacciones, asientos de contrapartida y el asiento resultante.

![La interfaz del usuario de la vista de una conciliación en un diario
bancario. ](../../../../_images/user-interface.png)

Transacciones

    

La sección de transacciones e la izquierda muestra todas las transacciones
bancarias, la más reciente se muestra primero. Haga clic en una transacción
para seleccionarla.

Asientos de contrapartida

    

La sección de asientos de contrapartida que se encuentra en la parte inferior
derecha muestra las opciones para conciliar la transacción bancaria
seleccionada. Tendrá disponibles varias pestañas, incluyendo conciliar
asientos existentes, conciliar pagos por lote, operaciones manuales de
conciliación y **Conversaciones** , en esta última encontrará el chatter para
la transacción bancaria que seleccione.

Asiento resultante

    

La sección de asiento resultante en la parte superior derecha muestra la
transacción bancaria seleccionada con los asientos de contrapartida e incluye
cualquier cargo o abono restante. En esta sección, puede validar la
conciliación o marcarla como **por revisar**. Todos los botones de los modelos
de conciliación también están disponibles en la sección del asiento
resultante.

## Conciliar transacciones

Las transacciones se pueden conciliar de forma automática con el uso de [los
modelos de conciliación](reconciliation_models), o se pueden conciliar
con asientos existentes, pagos por lote, operaciones manuales y botones de
modelo de conciliación.

  1. Seleccionar una transacción de entre varias transacciones bancarias no conciliadas.

  2. Defina la contrapartida. Hay varias opciones para esto, incluyendo conciliar asientos existentes, operaciones manuales, pagos por lote, y botones del modelo de conciliación.

  3. Si el asiento resultante no está totalmente saldado, puede agregar un asiento de contrapartida existente o ponerlo como una operación manual.

  4. Haga clic en el botón **Validar** para confirmar la conciliación y seguir con la siguiente transacción.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si no está seguro de cómo conciliar una transacción en particular y quiere lidiar con ella después, use el botón <b>por revisar</b>. Todas las transacciones que se marquen como <b>por revisar</b> se peden mostrar si elige el filtro <b>por revisar</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las transacciones bancarias se publican en la <b>cuenta transitoria del diario</b> hasta que se concilien. En este momento, la conciliación modifica el asiento de diario de la transacción. Para hacerlo, se reemplaza la cuenta transitoria del banco con la cuenta por cobrar, por paga o pendiente correspondiente.</p>
</div>

### Emparejar asientos existentes

Esta pestaña contiene los asientos conciliados que Konvergo ERP selecciona de manera
automática según los modelos de conciliación. El orden del asiento se basa en
los modelos de conciliación, pero los asientos sugeridos aparecerán primero.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>La barra de búsqueda dentro de la pestaña <b>emparejar asientos existentes</b> le permite buscar apuntes de diarios específicos.</p>
</div>

### Pagos por lotes

Con [los pagos por lote](payments/batch-payments) podrá agrupar diferentes
pagos para facilitar la conciliación. Use la pestaña **pagos por lote** para
encontrar los pagos por lote de clientes y proveedores. Así como la pestaña
**emparejar asientos existentes** la pestaña **pagos por lote** tiene una
barra de búsqueda que le permite buscar pagos por lotes específicos.

### Operaciones manuales

Si no hay un asiento existente para emparejar con la transacción seleccionada,
puede conciliar la transacción de manera manual, solo tiene que seleccionar la
cuenta y la cantidad correcta. Después, complete todos los campos opcionales
que sean necesarios.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede usar la opción <b>totalmente pagado</b> para conciliar un pago, incluso si solo ha recibido un pago parcial. Aparecerá una nueva línea en la sección del asiento resultante para que mostrará el saldo pendiente que se registró en la cuenta por cobrar de forma predeterminada. Para elegir otra cuenta haga clic en la línea nueva que se encuentra en la sección del asiento resultante y seleccione la <b>Cuenta</b> para registrar este saldo.</p>
<img alt="Haga clic en marcar como totalmente pagado para que la facture se marque como pagada. " src="../../../../_images/fully-paid.png"/>
</div>

### Botones del modelo de conciliación

Use el [botón del modelo de conciliación](reconciliation_models) para
operaciones manuales que se usan con frecuencia. Estos botones personalizados
le permitirán conciliar transacciones bancarias de manera eficaz y manual,
además de que se pueden usar con asientos ya existentes.

