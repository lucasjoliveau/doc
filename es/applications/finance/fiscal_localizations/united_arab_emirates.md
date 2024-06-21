# Emiratos Árabes Unidos

## Instalación

[Instale](../../general/apps_modules#general-install) los siguientes
módulos para obtener todas las funciones de la localización de **Emiratos
Árabes Unidos** :

Nombre | Nombre técnico | Descripción  
---|---|---  
**Emiratos Árabes Unidos - Contabilidad** | `l10n_ae` | El [paquete de localización fiscal](../fiscal_localizations) predeterminado. Incluye todas las cuentas, impuestos y reportes.  
**E.A.U - Nómina** | `l10n_ae_hr_payroll` | Incluye todas las reglas, cálculos y estructuras salariales.  
**E.A.U - Nómina y contabilidad** | `l10n_ae_hr_payroll_account` | Incluye todas las cuentas relacionadas con el módulo de nómina.  
**Emiratos Árabes Unidos - Punto de Venta** | `l10n_ae_pos` | Incluye el recibo de PdV conforme a los EAU.  
![Seleccione los módulos que desea desinstalar. ](../../../_images/l10n-ae-
modules.png)

## Plan de cuentas

Vaya a Contabilidad ‣ Configuración ‣ Plan de cuentas para ver todas las
cuentas predeterminadas que están disponibles en el paquete de localización de
EAU. Puede filtrarlas por **Código** usando los números de la extrema
izquierda o al hacer clic en Agrupar por ‣ Tipo de cuenta. Puede **Activar**
/**Desactivar** la conciliación o **configurar** cuentas específicas de
acuerdo a sus necesidades.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Siempre tenga activa por lo menos una  <b>cuenta por cobrar</b> y una <b>cuenta por pagar</b>.</p></li>
<li><p>También se recomienda <b>mantener las siguientes cuentas activas</b>, puesto que se usan como cuentas transitorias por Konvergo ERP o son específicas del <b>paquete de localización de EAU</b>.</p>
<table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Código</p></th>
<th class="head"><p>Nombre de la cuenta</p></th>
<th class="head"><p>Tipo</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>102011</p></td>
<td><p>Cuentas por cobrar</p></td>
<td><p>Cuentas por cobrar</p></td>
</tr>
<tr class="row-odd"><td><p>102012</p></td>
<td><p>Cuentas por cobrar (PdV)</p></td>
<td><p>Cuentas por cobrar</p></td>
</tr>
<tr class="row-even"><td><p>201002</p></td>
<td><p>Por pagar</p></td>
<td><p>Cuentas por pagar</p></td>
</tr>
<tr class="row-odd"><td><p>101004</p></td>
<td><p>Banco</p></td>
<td><p>Banco y efectivo</p></td>
</tr>
<tr class="row-even"><td><p>105001</p></td>
<td><p>Efectivo</p></td>
<td><p>Banco y efectivo</p></td>
</tr>
<tr class="row-odd"><td><p>100001</p></td>
<td><p>Transferencia de liquidez</p></td>
<td><p>Activos circulantes</p></td>
</tr>
<tr class="row-even"><td><p>101002</p></td>
<td><p>Documentos pendientes</p></td>
<td><p>Activos circulantes</p></td>
</tr>
<tr class="row-odd"><td><p>101003</p></td>
<td><p>Pagos pendientes</p></td>
<td><p>Activos circulantes</p></td>
</tr>
<tr class="row-even"><td><p>104041</p></td>
<td><p>IVA acreditable</p></td>
<td><p>Activos circulantes</p></td>
</tr>
<tr class="row-odd"><td><p>100103</p></td>
<td><p>IVA por cobrar</p></td>
<td><p>Activos no circulantes</p></td>
</tr>
<tr class="row-even"><td><p>101001</p></td>
<td><p>Cuenta transitoria</p></td>
<td><p>Pasivo circulantes</p></td>
</tr>
<tr class="row-odd"><td><p>201017</p></td>
<td><p>IVA pendiente de pago</p></td>
<td><p>Pasivo circulantes</p></td>
</tr>
<tr class="row-even"><td><p>202001</p></td>
<td><p>Provisión por terminación de relación laboral</p></td>
<td><p>Pasivo circulantes</p></td>
</tr>
<tr class="row-odd"><td><p>202003</p></td>
<td><p>IVA por pagar</p></td>
<td><p>Pasivos no circulantes</p></td>
</tr>
<tr class="row-even"><td><p>999999</p></td>
<td><p>Ganancias/pérdidas no distribuidas</p></td>
<td><p>Ganancias del año actual</p></td>
</tr>
<tr class="row-odd"><td><p>400003</p></td>
<td><p>Salario básico total</p></td>
<td><p>Gastos</p></td>
</tr>
<tr class="row-even"><td><p>400004</p></td>
<td><p>Subsidio de vivienda</p></td>
<td><p>Gastos</p></td>
</tr>
<tr class="row-odd"><td><p>400005</p></td>
<td><p>Subsidio de transporte</p></td>
<td><p>Gastos</p></td>
</tr>
<tr class="row-even"><td><p>400008</p></td>
<td><p>Indemnización por terminación de relación laboral</p></td>
<td><p>Gastos</p></td>
</tr>
</tbody>
</table>
</li>
</ul>
</div>

## Impuestos

Para acceder a sus impuestos, vaya Contabilidad ‣ Configuración ‣ Impuestos.
Active/desactive o configure los impuestos relevantes para su empresa haciendo
clic en ellos. Recuerde que solo debe establecer las cuentas fiscales en el
grupo de impuestos del **5%** , ya que otros grupos no necesitan cierre. Para
hacerlo, active el [modo desarrollador](../../general/developer_mode) y
vaya a Configuración ‣ Grupos de impuestos. Luego, establezca una **Cuenta
corriente de impuestos (por pagar)** , **Cuenta corriente de impuestos (por
cobrar)** , y una **Cuenta avanzada de pago de impuestos** para el grupo del
**5%**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El <abbr title="Mecanismo de Cobro Revertido">RCM</abbr> es compatible con Konvergo ERP.</p>
</div> ![Vista previa de los impuestos del paquete de
localización de EAU. ](../../../_images/uae-localization-taxes.png)

## Tipos de cambio

Para actualizar los tipos de cambio, vaya a Contabilidad ‣ Configuración ‣
Ajustes ‣ Divisas. Haga clic en el botón de actualizar (**🗘**) que está junto
al campo **Siguiente Ejecución** .

Para iniciar la actualización automáticamente en intervalos establecidos,
cambie el **Intervalo** de **Manual** a la frecuencia deseada.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El servicio web de tasas de cambio del Banco Central de los Emiratos Árabes Unidos se usa de forma predeterminada, pero hay otros proveedores disponibles en el campo <b>Servicio</b>.</p>
</div>

## Nómina

El módulo **EAU - Nómina** crea las **reglas salariales** necesarias en la
aplicación Nómina en conformidad con las normas y regulaciones de los EAU. Las
reglas salariales están vinculadas a las cuentas correspondientes en el **plan
de cuentas**.

![La estructura de la nómina de los EAU. ](../../../_images/uae-localization-
salary-rules.png)

### Reglas salariales

Para aplicar estas reglas en el contrato de un empleado, vaya a Nómina ‣
Contratos ‣ Contratos y seleccione el contrato del empleado. En el camp **Tipo
de Estructura Salarial** , selecciona **Empleado EAU**.

![Seleccione el tipo de estructura salarial que aplicará en el contrato.
](../../../_images/uae-localization-salary-structure.png)

En la pestaña **Información del salario** , puede encontrar detalles como:

  * **Sueldo** ;

  * **Subsidio de vivienda** ;

  * **Subsidio de Transporte** ;

  * **Otros subsidios** ;

  * **Número de Dias** : se usa para calcular el provisión por término de relación laboral.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Las <b>deducciones de vacaciones</b> se calculan usando una regla salarial vinculada al tipo de tiempo personal <b>vacaciones no remuneradas</b>;</p></li>
<li><p>Cualquier otra deducción o devolución se hace <em>manualmente</em> utilizando otras entradas;</p></li>
<li><p>Las <b>Horas extras</b> se agregan <em>manualmente</em> al ir a Entradas de trabajo ‣ Entradas de trabajo;</p></li>
<li><p>Los <b>Archivos adjuntos de salario</b> se generan al Contratos ‣ Archivos adjuntos de salario. Luego, <b>Crear</b> un archivo adjunto y seleccionar <b>Empleado</b> y el <b>Tipo (Archivo adjunto de salario, Asignación de salario, Pensión alimenticia)</b>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para evitar que una regla aparezca en un pago, vaya a Nómina ‣ Configuración ‣ Reglas. Haga clic en <b>Estructura de la nómina de los EAU</b>, seleccione la regla que quiere ocultar y deseleccione <b>Ver en el recibo de nómina</b>.</p>
</div>

### Provisión por terminación laboral

Las provisiones se definen como el subsidio total mensual _dividido_ entre 30
y luego _multiplicado_ por el número de dias establecidos en el campo **Número
de dias** que se encuentra al final del formulario del contrato.

Por lo tanto, las provisiones se calculan a través de una regla de salario
asociada con dos cuentas: : **Indemnización por terminación de relación
laboral (Cuenta de gastos)** y **Provisión por terminación de relación laboral
(Cuenta de pasivos no circulantes)**. Esta última se utiliza para pagar el
**finiquito** al establecerlo con las **cuentas por pagar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El finiquito se calcula con base en el salario bruto y las fechas de inicio y fin del contrato del empleado.</p>
</div>

### Facturas

El paquete de localización de EAU permite generar facturas en inglés, árabe o
ambas. La localización también incluye una línea para mostrar la **cantidad
del IVA** por línea.

