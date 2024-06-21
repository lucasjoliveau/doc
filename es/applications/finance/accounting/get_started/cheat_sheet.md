# Hoja de referencia de Contabilidad

El **balance general** es una captura de las finanzas de una empresa en una
fecha específica, contrario a las pérdidas y ganancias que es un análisis que
se realiza durante un periodo.

  * Los **activos** representan la riqueza de una empresa y los bienes que le pertenecen. Los edificios y oficinas son activos fijos, mientras que las cuentas de banco y el efectivo son activos circulantes. Un empleado no es un activo.

  * Las **responsabilidades** son obligaciones de eventos pasados por las que la empresa tendrá que pagar en un futuro (facturas de servicios públicos, deudas, proveedores a los que no se les ha pagado). También podemos definir estas responsabilidades como una forma de financiamiento que se le ofrece a la empresa llamada «aprovechamiento de recursos».

  * Los **recursos propios** son los fondos que los dueños de la empresa (fundadores o accionistas) contribuyen, más los recursos acumulados (o pérdidas). Cada año, las guanacias (o pérdidas) netas se pueden reportar como recursos acumulados, o se pueden distribuir a los accionistas (como dividendo).

Lo que se posee (un activo) se ha financiado a través del reembolso de deudas
(pasivos) o del capital (ganancias, capital).

Se hace una diferencia entre **activos** y **gastos** :

    

  * Un **activo** es un recurso con valor económico que le pertenece a un individuo, corporación o país y se controlan con la esperanza de obtener un beneficio futuro. Los bienes se reportan en el balance general y se compran o crean para aumentar el valor de una empresa o mejorar sus operaciones.

  * Un **gasto** son los costos de operaciones en los que incurre una empresa para generar ganancias.

El reporte de **pérdidas y ganancias** muestra el rendimiento de la empresa
durante un periodo específico, que usualmente son tres meses o un año fiscal

>   * Las **ganancias** son el dinero que gana la empresa al vender bienes o
> brindar servicios.
>
>   * El **costo de los bienes vendidos** (COGS por sus siglas en inglés) se
> refiere a los costos de la venta de bienes (por ejemplo, el costo de los
> materiales y el trabajo que se requirió para crear bienes).
>
>     * Las **ganancias brutas** son los ingresos de las venas menos el costo
> de los bienes vendidos.
>
>     * Los **OPEX** (Gastos operativos) incluyen administración, ventas y
> salarios de investigación y desarrollo, rentas y utilidades, costos
> misceláneos, costos y todo lo que vaya más allá de los costos de productos
> vendidos o el costo de las ventas.
>
>

> Activos = Pasivos + Capital

## Plan de cuentas

El **plan de cuentas** enlista todas las cuentas de la empresa: tanto la
cuenta del balance general como la cuenta de ganancias y pérdidas. Cada
transacción se registra al cargar y abonar a diferentes cuentas en un asiento
contable. Vea el plan de cuentas como el ADN de una empresa.

Cada cuenta que se enlista en el plan de cuentas pertenece a una categoría
específica. En Konvergo ERP, cada cuenta tiene un código único que pertenece a una de
estas categorías:

  * **Deuda subordinada y deuda de capital**
    
    * El **capital** es la cantidad de dinero que los accionistas invierten para financiar las actividades de una empresa

    * Las **deudas subordinadas** son la cantidad de dinero que un tercero le prestó a la empresa para financiar sus actividades. En caso de que la empresa se disuelva, primero se les reembolsará a estos terceros antes de reembolsarle a los accionistas.

  * Los **activos fijos** son elementos o propiedades tangibles (es decir, físicos) que una empresa compra y usa para producir bienes y servicios. Los activos fijos son activos a largo plazo, lo que significa que tienen una vida útil de más de un año. También incluye propiedades, plantas y equipos, (como equipo de protección individual) que se registran en el balance general con esa clasificación.1

  * **Activos circulantes y pasivos**
    
    * La cuenta de **activos circulantes** es la línea de un apunte contable del balance general que se enlista en la sección de Activos. En esta cuenta se encuentran todos los activos que se pueden convertir en efectivo en menos de un año. Los activos circulantes son el efectivo, equivalentes de efectivo, cuentas por cobrar, existencias del inventario, valores negociables, pasivos prepagados y otros activos líquidos.

    * Los **pasivos circulantes** son las obligaciones financieras a corto plazo de la empresa, o sea que se deben liquidar en menos de un año. Un ejemplo de un pasivo circulante es el dinero que le debemos a los proveedores como cuentas por pagar.

  * **Cuentas bancarias y de efectivo**
    
    * Una **cuenta bancaria** es una cuenta financiera que un banco u otra institución financiera mantiene. En esta cuenta se registran las transacciones financieras entre un banco y el cliente.

    * Un **libro de cuentas** se puede referir a un libro en el que se registran todas las transacciones en efectivo. Este registro incluye los momentos en los que se recibe efectivo y los diarios de pagos de efectivo.

  * **Gastos e ingresos**
    
    * Un **gasto** son los costos de las operaciones que la empresa realiza para generar ganancias. Es el gasto que se tiene que realizar para obtener algo. Los gastos comunes incluyen lo pagos de a proveedores, salarios de los empleados, arrendamiento de fábricas y depreciación del equipo.

    * Los **ingresos** son la cantidad de dinero, las propiedades u otras transferencias de valor que se reciben en un periodo a cambio de servicios o productos.

### Ejemplo

*: Las cajas Reembolso de cliente y Pago del cliente no se pueden seleccionar al mismo tiempo ya que se contradicen.

> Balance = Débito - Crédito

## Asientos contables

Todos los documentos financieros de la empresa (como una factura, estados de
cuenta, recibos de pago, un contrato de aumento de capital) se registran como
asiento contable e impactan a varias cuentas.

Para que un asiento contable esté balanceado, la suma de todos sus cargos debe
ser igual a la suma de todos sus abonos.

ejemplos de asientos contables para varias transacciones. (véase entries.js)

## Conciliación

La [conciliación](../bank/reconciliation) es el proceso de enlazar los
apuntes contables de una cuenta específica con los cargos y abonos
respectivos.

El propósito principal es relacionar los pagos con las facturas relacionadas y
marcarlos como pagados. Esto se hace con la conciliación de la cuenta de
cuentas por paga y las cuentas por cobrar.

La conciliación la realiza el sistema automáticamente cuando:

  * El pago se registra directamente en la factura.

  * Los vínculos entre los pagos y las facturas se detectan en el proceso de emparejamiento del banco.

Ejemplo de un estado de cuenta de cliente

Cuentas por cobrar | Débito | Crédito  
---|---|---  
Factura 1 | 100 |   
Pago parcial 1/2 |  | 70  
Factura 2 | 65 |   
Pago parcial 2/2 |  | 30  
Pago 2 |  | 65  
Factura 3 | 50 |   
|  |   
Total a pagar | 50 |   
  
## Conciliación bancaria

La conciliación bancaria es el emparejamiento de las líneas de los estados de
cuenta bancarios (proporcionados por el banco) con transacciones registradas
internamente (pagos a proveedores o de clientes). Para cada línea en un estado
de cuenta bancario, puede ser:

  * **se concilió con un pago previamente registrado** : un pago se registra cuando se recibe el cheque del cliente, después se concilia con el estado de cuenta.

  * **se registró como pago nuevo** : se crea el asiento de diario del pago y se concilia con la factura relacionada al procesar el estado de cuenta.

  * **se registró como otra transacción** transferencia bancaria, cambio directo, etc.

Konvergo ERP conciliará de manera automática la mayoría de las transacciones, solo
necesitará revisar algunas personalmente. Cuando se termina el proceso de
conciliación bancaria, el balance de la cuenta bancaria de Konvergo ERP debe ser el
mismo que el balance del estado de cuenta bancario

## Gestión de cheques

Hay dos enfoques para gestionar cheques y transferencias bancarias internas:

  * Dos asientos contables y una conciliación

  * Un asiento contable y una conciliación bancaria

El primer asiento contable se crea al registrar el pago en la factura. El
segundo se crea cuando se registra el estado de cuenta bancario.

Cuenta | Débito | Crédito | Conciliación  
---|---|---|---  
Cuenta a cobrar |  | 100 | Factura ABC  
Fondos sin depositar | 100 |  | Cheque 0123  
Cuenta | Débito | Crédito | Conciliación  
---|---|---|---  
Fondos sin depositar |  | 100 | Cheque 0123  
Banco | 100 |  |   
  
El primer asiento contable se crea al registrar el pago en la factura. Cuando
se concilie el estado de cuenta bancario, la línea del estado de cuenta se
vincula al asiento contable existente.

Cuenta | Débito | Crédito | Conciliación | Estado de cuenta bancario  
---|---|---|---|---  
Cuenta a cobrar |  | 100 | Factura ABC |   
Banco | 100 |  |  | Estado de cuenta XYZ

