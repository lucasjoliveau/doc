# Pagos con SEPA

La Zona Única de Pagos en Euros, o SEPA, es una iniciativa de integración de
pagos de la Unión Europea que busca simplificar las transferencias bancarias
en euros. Con SEPA podrá enviar órdenes de pago a su banco para automatizar
las transferencias bancarias.

Los bancos de los 27 estados miembro de la UE aceptan SEPA, así como:

Países en la Asociación Europea de Libre Comercio:

  * Islandia,

  * Liechtenstein,

  * Noruega,

  * Suiza.

Países en la SEPA que no pertenecen al Espacio Económico Europeo:

  * Andorra,

  * Monaco,

  * San Marino,

  * Reino Unido,

  * Estado de la Ciudad del Vaticano.

Territorios fuera del Espacio Económico Europeo:

  * San Pedro y Miquelón,

  * Guernsey,

  * Jersey,

  * Isla de Man.

Al pagar una factura con Odoo usted puede seleccionar los mandatos SEPA como
opción de pago. Al final del día, puede generar un archivo SEPA que contenga
todas las transferencias bancarias para enviárselo a su banco.

De forma predeterminada, el archivo sigue las especificaciones de la
transferencia de crédito SEPA **“pain.001.001.03”** , que es una práctica
estándar definida entre los bancos. Sin embargo, para empresas en Suiza o
Alemania, se usan otros formatos. Para Suiza se usa
**“pain.001.001.03.ch.02”** y para Alemania se usa **“pain.001.003.03”**.

Una vez que su banco haya procesado los pagos, puede importar el estado de
cuenta directo a Odoo. El proceso de conciliación bancaria vinculará las
órdenes SEPA que envió a su banco con los respectivos estados de cuenta.

## Configuración

### Activar la transferencia de crédito SEPA (SCT)

Para pagarle a sus proveedores con SEPA, debe activar la **Transferencia de
Crédito SEPA**. Para hacerlo vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣
Pagos de proveedor: Transferencia SEPA de crédito (SCT). Al activar esta
función y llenar los datos de su empresa, podrá usar la opción SCT al pagarle
a su proveedor.

Nota

Es posible que los módulos **Domiciliación bancaria SEPA** y **Transferencias
de crédito SEPA** ya estén instalados dependiendo del paquete de localización
que se instaló. Si no es así, necesita
[instalarlos](../../../general/apps_modules.html#general-install).

### Activar métodos de pago SEPA en bancos

Desde el tablero de contabilidad, haga clic en el menú desplegable (⋮) en su
diario contable y seleccione guilabel:`Configuración`. Haga clic en la pestaña
Pagos salientes y agregue guilabel:`Transferencia de crédito SEPA` en Método
de pago.

Asegúrese de especificar el número IBAN de la cuenta (los número de cuenta
locales no funcionan con SEPA) y el BIC (código identificador se banco, por
sus siglas en inglés) en la pestaña Asientos de diario.

### Registro de pagos

Puede registrar el pago que realizó a un proveedor mediante SEPA. Para
hacerlo, vaya a Contabilidad ‣ Proveedores ‣ Pagos. Cuando cree su pago
seleccione Transferencia de crédito SEPA como el método de pago .

La primera vez que le pague a un vendedor con SEPA, tendrá que llenar el campo
Cuenta del banco receptor con el nombre del banco, el IBAN y el BIC. Odoo
verifica de manera automática si se respetó el formato IBAN.

Para pagos futuros a este proveedor, Odoo le sugerirá de manera automática la
cuenta del banco, pero todavía puede elegir una nueva.

Una vez que registre su pago, no se le olvide confirmarlo. Para pagar las
facturas de proveedor solo tiene que hacer clic en el botón Registrar pago que
se encuentra en la parte superior de la factura. El formulario es el mismo,
pero el pago está ligado a la factura y se conciliará de manera automática.

