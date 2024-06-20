# Sistema multidivisa

Odoo le permite emitir facturas, recibirlas y registrar transacciones en
divisas distintas a la divisa principal que configuró para su empresa. También
puede configurar cuentas bancarias en otras divisas y ejecutar reportes de sus
actividades en divisas extranjeras.

Ver también

  * [Gestione una cuenta bancaria en una moneda extranjera](../bank/foreign_currency.html)

## Configuración

### Divisa principal

La **divisa principal** se define de forma predeterminada según el país de la
empresa. Puede cambiarla en Contabilidad ‣ Configuración ‣ Ajustes ‣ Divisas y
cambiar la divisa en el ajuste Divisa principal.

### Habilitar divisas extranjeras

Vaya a Contabilidad ‣ Configuración ‣ Divisas, y habilite las divisas que
desea utilizar al alternar el botón de Activar.

![Habilitar las divisas que desea utilizar.](../../../../_images/enable-
foreign-currencies.png)

### Tasas de cambio

#### Actualización manual

Para crear y establecer una tasa de cambio de forma manual, vaya a
Contabilidad ‣ Configuración ‣ Divisas, haga clic en la divisa a la que desea
cambiar la tasa, y en la pestaña de Tasas, haga clic en Agregar una línea para
crear una nueva tasa.

![Creación o modificación de la tasa de cambio.](../../../../_images/manual-
rate-update.png)

#### Actualización automática

Al activar una segunda divisa por primera vez, aparece la opción Tasas de
cambio automáticas en Contabilidad Tablero ‣ Configuración ‣ Ajustes ‣
Divisas. De forma predeterminada, debe hacer clic en el botón de **Actualizar
ahora** (🗘) para actualizar la tasa.

Odoo puede actualizar las tasas en intervalos regulares. Para hacerlo, cambie
el Intervalo de Manualmente a Diariamente, Semanalmente, o Mensualmente.
También puede seleccionar el servicio web del que desea obtener las tasas de
cambio más actuales al hacer clic en el campo Servicio.

### Asientos de diferencia de cambio

Odoo registra en un diario dedicado los asientos de diferencias de cambio en
cuentas dedicadas de forma automática.

Puede definir en qué diario y cuentas **publicar los asientos de diferencia de
cambio** en Contabilidad ‣ Configuración ‣ Ajustes ‣ Cuentas predeterminadas y
editar los Diarios, Cuenta de ganancias y Cuenta de pérdidas.

Example

Si recibe un pago de una factura de cliente un mes después de su emisión, la
tasa de cambio probablemente es diferente a la inicial. Por lo tanto, esta
fluctuación implica una ganancia o pérdida debido a la diferencia en la tasa
de cambio, la cual Odoo registra de forma automática en el diario **Diferencia
de cambio** predeterminado.

### Plan de cuentas

Cada cuenta puede tener una divisa establecida. De esta forma, todos los
movimientos relevantes a la cuenta se ven obligados a tener la divisa de esa
cuenta.

Para hacerlo, vaya a Contabilidad ‣ Configuración ‣ Plan de cuentas y
seleccione una divisa en el campo Divisa de la cuenta. Si se deja en blanco,
se pueden utilizar todas las divisas activas en lugar de solo una.

### Diarios contables

Si se establece una divisa en un **diario** , dicho diario solo puede
gestionar transacciones en esa divisa.

Para hacerlo, vaya a Contabilidad ‣ Configuración ‣ Diarios, abra el diario
que quiere editar y seleccione la divisa en el campo Divisa.

![Seleccionar la divisa que el diario utilizará.](../../../../_images/journal-
currency.png)

## Contabilidad multidivisa

### Facturas de cliente, de proveedor y otros documentos

Para todos los documentos, puede seleccionar la divisa y el diario que quiere
usar para las transacciones en el documento en sí.

![Selección de la divisa y diarios a utilizar.](../../../../_images/currency-
field.png)

### Registro de pagos

Para registrar un pago en una divisa distinta a la divisa principal de la
empresa, haga clic en el botón de pago Registrar pago de su documento y, en la
ventana emergente, selecciona una **divisa** en el campo Importe.

![Selección de la divisa y diario a utilizar antes de registrar el
pago.](../../../../_images/register-payment.png)

### Transacciones bancarias

Al crear o importar transacciones bancarias, la cantidad se mostrará en la
divisa principal de la empresa. Para ingresar una **divisa extranjera** ,
seleccione una divisa en Divisa extranjera. Una vez que lo seleccione, ingrese
la cantidad en la divisa principal para que se convierta, de manera
automática, en una divisa extranjera cuando se muestre en el campo Importe en
divisa.

![Los campos adicionales relacionados con divisas
extranjeras.](../../../../_images/foreign-fields.png)

Al conciliar, Odoo muestra el importe en la divisa extranjera y su equivalente
en la divisa principal de la empresa.

### Asientos contables de tipo de cambio

Para ver los **asientos contables de tasa de cambio** , vaya a Tablero de
Contabilidad ‣ Contabilidad ‣ Diarios: Varios.

![Asiento contable de tipo de cambio.](../../../../_images/exchange-journal-
currency.png)

