# Pagos

En Odoo, los pagos se pueden vincular de manera automática con una factura o
se pueden dejar como registros separados que se usarán en otra fecha.

  * Si un pago está **vinculado a una factura** entonces la cantidad por pagar de la factura se reducirá o liquidará. Puede tener muchos pagos relacionados a la misma factura.

  * Si un pago **no está ligado a una factura**. el cliente tendrá un crédito pendiente con su empresa, o su empresa tendrá un crédito pendiente con un proveedor. Puede usar esas cantidades pendientes para reducir o liquidar facturas sin pagar.

Ver también

  * [Transferencias internas](payments/internal_transfers.html)

  * [Conciliación bancaria](bank/reconciliation.html)

  * [Tutoriales de Odoo: configuración bancaria](https://www.odoo.com/slides/slide/bank-configuration-1880)

## Registrar un pago para una factura

Cuando haga clic en el botón Registrar pago que aparece en una factura, se
genera un asiento contable y se cambia la cantidad que se debe según la
cantidad que se pagó. La contrapartida se refleja en la cuenta de **recibos**
o **pagos** [pendientes](bank.html#bank-outstanding-accounts). En este momento
es cuando se marca la factura como En proceso de pago. Después, cuando la
cuenta pendiente se concilie con la línea del estado de cuenta bancario, la
factura cambiará al estado Pagado.

El icono de información en la línea de pago muestra más información sobre el
pago. Para ver información adicional. como el diario relacionado, haga clic en
Vista.

![Ver información de pago detallada.](../../../_images/information-icon.png)

Nota

  * Para poder registrar el pago la factura debe estar en el estado Publicado.

  * Si quita la conciliación de un pago seguirá apareciendo en sus libros pero ya no estará ligado a ninguna factura.

  * Si concilia o quita la conciliación de un pago en una divisa diferente, se crea un asiento de diario de manera automática para publicar la cantidad de pérdidas y ganancias tras el cambio de divisas.

  * Si concilia o quita la conciliación de un pago y una factura si tiene impuestos con base en efectivo, se crea un asiento de diario de manera automática para publicar la cantidad de impuestos con base en efectivo.

Truco

  * Si su cuenta bancaria principal está configurada como [Cuenta pendiente](bank.html#bank-outstanding-accounts) y el pago se registra en Odoo (no a través de una cuenta bancaria relacionada), entonces las facturas se registran de manera automática con el estado Pagado.

## Registrar pagos que no están ligados a una factura

Cuando se registra un nuevo pago a través del menú Clientes / Proveedores ‣
Pagos, este pago no se vinculará de inmediato a una factura. En su lugar, las
cuentas por pagar o las cuentas por cobrar se concilian con las **cuentas
pendientes** hasta que se concilien de manera manual con la factura
relacionada.

### Vincular facturas con pagos

Cuando valida una nueva factura y hay un **pago pendiente** (ya sea que el
cliente no haya pagado o usted no haya pagado al proveedor) aparecerá una
cinta azul. Para vincular la factura solo haga clic en Añadir en Créditos
pendientes o Débitos pendientes.

![Muestra la opción AÑADIR para conciliar una factura con un
pago.](../../../_images/add-option.png)

La factura ahora se marca como En proceso de pago hasta que se haya conciliado
con el extracto bancario correspondiente.

### Pago en lote

Los pagos en lote le permiten agrupar varios pagos para facilitar la
[conciliación](bank/reconciliation.html). También ayudan mucho cuando hay que
depositar [cheques](payments/checks.html) en el banco o para [pagos
SEPA](payments/pay_sepa.html). Para crear pagos en lote vaya a Contabilidad ‣
Clientes ‣ Pagos por lote o Contabilidad ‣ Proveedores ‣ Pagos por lote. En la
vista de lista de los pagos puede seleccionarlos y agruparlos en lote, haga
clie en Acción ‣ Crear pago por lotes.

Ver también

  * [Pagos por lote para depósitos bancarios](payments/batch.html)

  * [Pagos por lotes: domiciliación bancaria SEPA (SDD)](payments/batch_sdd.html)

### Emparejamiento de pagos

La herramienta Emparejamiento de pagos abre todas las facturas sin conciliar y
podrá procesar todas individualmente, ya que podrá vincular los pagos con las
facturas a la vez en un mismo lugar. Para usar esta herramienta vaya al
Tablero de contabilidad ‣ Facturas de cliente y de proveedor, haga clic en el
menú desplegable ⋮ y seleccione Emparejamiento de pagos, o en Contabilidad ‣
Conciliación.

![Menú de conciliación de pagos en el menú
desplegable.](../../../_images/payments-journal.png)

Nota

Durante la [conciliación](bank/reconciliation.html), si la suma de los cargos
y los abonos no cuadra queda el balance restante. Este balance se tiene que
conciliar después o se tiene que borrar.

### Conciliación de pagos por lote

Puede utilizar la función de conciliación por lotes para conciliar varias
facturas o pagos pendientes de forma simultánea para un cliente o proveedor
específico. Vaya a Contabilidad ‣ Reportes ‣ Cuentas antiguas por cobrar o por
pagar. Allí podrá visualizar todas las transacciones que aún no se han
conciliado para ese contacto. Al seleccionar un cliente o proveedor aparecerá
la opción Conciliar.

![La opción de conciliación visible.](../../../_images/reconcile-option.png)

## Registrar un pago parcial

Para registrar un **pago parcial** , haga clic en Registrar pago en la factura
relacionada e ingrese el importe recibido o pagado. Al ingresar el importe
aparecerá un mensaje que le pedirá que decida si Mantener abierta la factura o
Marcar como pagado en su totalidad. Seleccione Mantener abierta y haga clic en
Crear pago y la factura se marcará como Parcial. Seleccione Marcar como pagado
en su totalidad si desea saldar la factura con una diferencia en el importe.

![Pago parcial de una factura.](../../../_images/payment-difference.png)

## Conciliar pagos con estados de cuenta bancarios

Después de registrar el pago, el estado de la factura será En proceso de pago.
Después, [concilie](bank/reconciliation.html) el pago con la línea del estado
de cuenta bancario relacionado para finalizar la transacción y hacer que la
factura se marque como Pagado.

  * [Pagos en línea](payments/online.html)
    * [Instale el parche para desactivar el pago de factura en línea](payments/online/install_portal_patch.html)
  * [Cheques](payments/checks.html)
  * [Pagos por lote para depósitos bancarios](payments/batch.html)
  * [Pagos por lotes: domiciliación bancaria SEPA (SDD)](payments/batch_sdd.html)
  * [Seguimiento en las facturas](payments/follow_up.html)
  * [Transferencias internas](payments/internal_transfers.html)
  * [Pagos con SEPA](payments/pay_sepa.html)
  * [Pagar con cheques](payments/pay_checks.html)
  * [Pronóstico de futuras facturas por pagar](payments/forecast.html)

