# Cheques

Hay dos maneras de gestionar pagos que se recibieron en Konvergo ERP, ya sea desde las
cuentas por cobrar o si evita el proceso de conciliación.

**Recomendamos que use cuentas pendientes** ya que su cuenta bancaria se
mantiene al día y correcta solo cuando puede tomar en cuenta cheques que no se
han cambiado.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Al final del proceso ambos métodos producen los mismos datos en su contabilidad. Sin embargo, si tiene cheques que no ha cambiado, el método <b>Cuentas por cobrar</b> registra estos cheques en la cuenta <b>Recibos por cobrar</b>. De igual manera, los fondos aparecen en su cuenta bancaria sin importar si se conciliaron o no, ya que el valor del banco se refleja en el momento que recibe su estado de cuenta bancaria.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../bank#bank-outstanding-accounts"><span class="std std-ref">Cuentas pendientes</span></a></p></li>
<li><p><a href="../get_started/cheat_sheet#accounting-reconciliation"><span class="std std-ref">Conciliación bancaria</span></a></p></li>
</ul>
</div>

## Método 1: cuentas pendientes

Cuando recibe un cheque, usted [registra el pago](../bank/reconciliation)
mediante un cheque en la factura. Después, cuando a su cuenta bancaria se le
abone la cantidad del cheque, usted reconcilia el pago y el estado de cuenta
para que la cantidad se mueva de la cuenta **Pagos pendientes** a la cuenta
**Banco**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede crear un nuevo método de pago llamado <em>Cheques</em> si quiere identificar este tipo de pagos de inmediato. Para hacerlo, vaya a Contabilidad ‣ Configuración ‣ Diarios ‣ Banco, haga clic en la pestaña <b>Pagos entrantes</b> y <b>Agregue una línea</b>. Como <b>Método de pago</b> seleccione <b>Manual</b>, ingrese <code>Cheques</code> como nombre y, finalmente, haga clic en <b>Guardar</b>.</p>
</div>

## Método 2: ignorar la conciliación

Cuando recibe un cheque, usted [registra un pago](../bank/reconciliation)
en la factura relacionada. Después, la cantidad se mueve de **Cuenta por
cobrar** a la cuenta **Banco** , lo cual se salta el proceso de conciliación y
crea solo **un asiento contable**.

Para lograrlo, usted _debe_ realizar la misma configuración que le presentamos
a continuación. Vaya a Contabilidad ‣ Configuración ‣ Diarios ‣ Banco. Haga
clic en la pestaña **Pagos entrantes** y después **Agregue una línea**.
Seleccione **Manual** como **Método de pago** , e ingrese `Cheques` como el
**Nambre**. Haga clic en el botón para alternar el menú, seleccione **Cuenta
de recibos pendientes** , y en la columna **Cuenta de recibos pendientes**
seleccione la cuenta **Banco** para el método de pago **Cheques**.

![Use la cuenta Banco para ignorar la cuenta de recibos
pendientes.](../../../../_images/outstanding-payment-accounts.png)

## Registro de pagos

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>De forma predeterminada hay dos maneras de registrar pagos hechos con cheque:</p>
<ul>
<li><p><b>Manual</b>: para cheques únicos, y</p></li>
<li><p><b>Por lote</b>: para varios cheques a la vez.</p></li>
</ul>
<p>Esta documentación está enfocada en pagos para <b>cheques únicos</b>. Para <b>depósitos por lotes</b>, consulte la <a href="batch">documentación de pagos por lotes</a>.</p>
</div>

Una vez que reciba el cheque de un cliente, vaya a la factura relacionada
(Contabilidad ‣ Cliente ‣ Facturas), y haga clic en **Registrar pago**. Llene
la información de pago:

  * **Diario: Banco** ;

  * **Método de pago** : **Manual** (o **Cheques** si creó un método de pago específico);

  * **Memorando** : ingrese el número de cheque;

  * Haga clic en **Crear pago**.

![Revise la información de pago](../../../../_images/payment-checks.png)

Los asientos bancarios generados serán diferentes según el método de registro
de pago que se eligió.

## Asientos contables

### Cuentas pendientes

La factura se marca como **En proceso de pago** tan pronto como se registra el
pago. Esta operación producirá el siguiente **asiento de diario** :

Cuenta | Conciliación de estados de cuenta bancarios | Débito | Crédito  
---|---|---|---  
Cuenta a cobrar |  |  | 100.00  
Documentos pendientes |  | 100.00 |   
  
Después, ya que reciba los estados de cuenta bancarios, vincule ese estado de
cuenta con el cheque que está en la cuenta de **Recibos pendientes** , lo que
producirá el siguiente **asiento de diario** :

Cuenta | Conciliación de estados de cuenta bancarios | Débito | Crédito  
---|---|---|---  
Documentos pendientes | X |  | 100.00  
Banco |  | 100.00 |   
  
Si elige este enfoque para gestionar los cheques recibidos, obtendrá la lista
de cheques que no se han cambiado en la cuenta **Recibos pendientes** (a la
que puede entrar desde el libro mayor general, por ejemplo).

### Ignorar el paso de conciliación

La factura se marca como **Pagado** tan pronto como se registre el cheque.

Con este enfoque, no se tendrá que usar la cuenta de **recibos pendientes** ,
lo que significa que solo obtendrá un asiento de diario en sus libros y se
saltará el paso de conciliación:

Cuenta | Conciliación de estados de cuenta bancarios | Débito | Crédito  
---|---|---|---  
Cuenta a cobrar | X |  | 100.00  
Banco |  | 100.00 | 

