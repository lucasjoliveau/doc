# Emiratos Árabes Unidos

## Instalación

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para obtener todas las funciones de la localización de **Emiratos
Árabes Unidos** :

Nombre | Nombre técnico | Descripción  
---|---|---  
Emiratos Árabes Unidos - Contabilidad | `l10n_ae` | El [paquete de localización fiscal](../fiscal_localizations.html) predeterminado. Incluye todas las cuentas, impuestos y reportes.  
E.A.U - Nómina | `l10n_ae_hr_payroll` | Incluye todas las reglas, cálculos y estructuras salariales.  
E.A.U - Nómina y contabilidad | `l10n_ae_hr_payroll_account` | Incluye todas las cuentas relacionadas con el módulo de nómina.  
Emiratos Árabes Unidos - Punto de Venta | `l10n_ae_pos` | Incluye el recibo de PdV conforme a los EAU.  
![Seleccione los módulos que desea desinstalar. ](../../../_images/l10n-ae-
modules.png)

## Plan de cuentas

Vaya a Contabilidad ‣ Configuración ‣ Plan de cuentas para ver todas las
cuentas predeterminadas que están disponibles en el paquete de localización de
EAU. Puede filtrarlas por Código usando los números de la extrema izquierda o
al hacer clic en Agrupar por ‣ Tipo de cuenta. Puede Activar/Desactivar la
conciliación o **configurar** cuentas específicas de acuerdo a sus
necesidades.

Importante

  * Siempre tenga activa por lo menos una **cuenta por cobrar** y una **cuenta por pagar**.

  * También se recomienda **mantener las siguientes cuentas activas** , puesto que se usan como cuentas transitorias por Odoo o son específicas del **paquete de localización de EAU**.

Código | Nombre de la cuenta | Tipo  
---|---|---  
102011 | Cuentas por cobrar | Cuentas por cobrar  
102012 | Cuentas por cobrar (PdV) | Cuentas por cobrar  
201002 | Por pagar | Cuentas por pagar  
101004 | Banco | Banco y efectivo  
105001 | Efectivo | Banco y efectivo  
100001 | Transferencia de liquidez | Activos circulantes  
101002 | Documentos pendientes | Activos circulantes  
101003 | Pagos pendientes | Activos circulantes  
104041 | IVA acreditable | Activos circulantes  
100103 | IVA por cobrar | Activos no circulantes  
101001 | Cuenta transitoria | Pasivo circulantes  
201017 | IVA pendiente de pago | Pasivo circulantes  
202001 | Provisión por terminación de relación laboral | Pasivo circulantes  
202003 | IVA por pagar | Pasivos no circulantes  
999999 | Ganancias/pérdidas no distribuidas | Ganancias del año actual  
400003 | Salario básico total | Gastos  
400004 | Subsidio de vivienda | Gastos  
400005 | Subsidio de transporte | Gastos  
400008 | Indemnización por terminación de relación laboral | Gastos  

## Impuestos

Para acceder a sus impuestos, vaya Contabilidad ‣ Configuración ‣ Impuestos.
Active/desactive o configure los impuestos relevantes para su empresa haciendo
clic en ellos. Recuerde que solo debe establecer las cuentas fiscales en el
grupo de impuestos del **5%** , ya que otros grupos no necesitan cierre. Para
hacerlo, active el [modo desarrollador](../../general/developer_mode.html) y
vaya a Configuración ‣ Grupos de impuestos. Luego, establezca una Cuenta
corriente de impuestos (por pagar), Cuenta corriente de impuestos (por
cobrar), y una Cuenta avanzada de pago de impuestos para el grupo del **5%**.

Nota

El RCM es compatible con Odoo.

![Vista previa de los impuestos del paquete de localización de EAU.
](../../../_images/uae-localization-taxes.png)

## Tipos de cambio

Para actualizar los tipos de cambio, vaya a Contabilidad ‣ Configuración ‣
Ajustes ‣ Divisas. Haga clic en el botón de actualizar (🗘) que está junto al
campo Siguiente Ejecución .

Para iniciar la actualización automáticamente en intervalos establecidos,
cambie el Intervalo de Manual a la frecuencia deseada.

Nota

El servicio web de tasas de cambio del Banco Central de los Emiratos Árabes
Unidos se usa de forma predeterminada, pero hay otros proveedores disponibles
en el campo Servicio.

## Nómina

El módulo EAU - Nómina crea las **reglas salariales** necesarias en la
aplicación Nómina en conformidad con las normas y regulaciones de los EAU. Las
reglas salariales están vinculadas a las cuentas correspondientes en el **plan
de cuentas**.

![La estructura de la nómina de los EAU. ](../../../_images/uae-localization-
salary-rules.png)

### Reglas salariales

Para aplicar estas reglas en el contrato de un empleado, vaya a Nómina ‣
Contratos ‣ Contratos y seleccione el contrato del empleado. En el camp Tipo
de Estructura Salarial , selecciona Empleado EAU.

![Seleccione el tipo de estructura salarial que aplicará en el contrato.
](../../../_images/uae-localization-salary-structure.png)

En la pestaña Información del salario, puede encontrar detalles como:

  * Sueldo;

  * Subsidio de vivienda;

  * Subsidio de Transporte;

  * Otros subsidios;

  * Número de Dias: se usa para calcular el provisión por término de relación laboral.

Nota

  * Las **deducciones de vacaciones** se calculan usando una regla salarial vinculada al tipo de tiempo personal **vacaciones no remuneradas** ;

  * Cualquier otra deducción o devolución se hace _manualmente_ utilizando otras entradas;

  * Las **Horas extras** se agregan _manualmente_ al ir a Entradas de trabajo ‣ Entradas de trabajo;

  * Los **Archivos adjuntos de salario** se generan al Contratos ‣ Archivos adjuntos de salario. Luego, Crear un archivo adjunto y seleccionar Empleado y el Tipo (Archivo adjunto de salario, Asignación de salario, Pensión alimenticia).

Truco

Para evitar que una regla aparezca en un pago, vaya a Nómina ‣ Configuración ‣
Reglas. Haga clic en Estructura de la nómina de los EAU, seleccione la regla
que quiere ocultar y deseleccione Ver en el recibo de nómina.

### Provisión por terminación laboral

Las provisiones se definen como el subsidio total mensual _dividido_ entre 30
y luego _multiplicado_ por el número de dias establecidos en el campo Número
de dias que se encuentra al final del formulario del contrato.

Por lo tanto, las provisiones se calculan a través de una regla de salario
asociada con dos cuentas: : **Indemnización por terminación de relación
laboral (Cuenta de gastos)** y **Provisión por terminación de relación laboral
(Cuenta de pasivos no circulantes)**. Esta última se utiliza para pagar el
**finiquito** al establecerlo con las **cuentas por pagar**.

Nota

El finiquito se calcula con base en el salario bruto y las fechas de inicio y
fin del contrato del empleado.

### Facturas

El paquete de localización de EAU permite generar facturas en inglés, árabe o
ambas. La localización también incluye una línea para mostrar la **cantidad
del IVA** por línea.

  *[RCM]: Mecanismo de Cobro Revertido

