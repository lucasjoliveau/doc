# Tailandia

## Configuración

[Instale](../../general/apps_modules#general-install) el paquete de
localización de **🇹🇭 Tailandia** para obtener todas las funciones de la
localización tailandesa:

Nombre | Nombre técnico | Descripción  
---|---|---  
**Tailandia - Contabilidad** | `l10n_th` | [Paquete de localización fiscal](../fiscal_localizations#fiscal-localizations-packages) predeterminado  
**Tailandia - Reportes contables** | `l10n_th_reports` | Reportes contables específicos del país  
![Módulos de localización de Tailandia](../../../_images/modules2.png)

## Plan de cuentas e impuestos

El paquete de localización fiscal de Konvergo ERP para Tailandia incluye los
siguientes impuestos:

  * IVA del 7%

  * Exención de IVA

  * Retención de impuesto

  * Retención de impuesto sobre la renta

## Informe de impuestos

Konvergo ERP le permite a los usuarios generar archivos de Excel para enviar el IVA al
**Departamento de Hacienda** de Tailandia.

### Reporte de impuestos de ventas y compra

Para generar el reporte de impuestos de ventas y compra, vaya a Contabilidad ‣
Reportes ‣ Reporte de impuestos. Seleccione una hora o un rango de tiempo
específico para el reporte y haga clic en **VAT-202-01 (xlsx)** para los
impuestos de compra y en **VAT-202-02 (xlsx)** para los de ventas.

![Reportes de impuestos de compra y ventas de Tailandia.
](../../../_images/tax-report.png)

### Reporte de retención de impuestos PND

Los datos del reporte PND muestran en resumen las cantidades de la **retención
de impuestos sobre sociedades (nacional)** aplicables sobre las facturas de
proveedor en los reportes de impuestos **PND53 (TH)** y **PND3 (TH)**. Se
instala de manera predeterminada con la localización tailandesa.

![Reportes de impuestos PND ](../../../_images/pnd-report.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La retención de impuestos sobre sociedades (nacional) es el impuesto que se aplica en caso de que la empresa retenga el impuesto sobre los servicios “<b>Personales (PND3)</b>” o “<b>Empresariales (PND53)</b>” prestados como el alquiler, la contratación, el seguro, la cuota de administración, consultoría, etc.</p>
</div>

El reporte de impuestos PND le permite a los usuarios generar un archivo CSV
para las facturas y subirlas a la [aplicación de llenado electrónico RDprep
para Tailandia](https://efiling.rd.go.th/rd-cms/).

Para generar un archivo PND CSV, vaya a Contabilidad ‣ Reportes ‣ Reporte de
impuesto, seleccione una hora específica o un rango de tiempo para el reporte
de impuesto y haga clic en **PND3** o **PND53**.

Esto genera los archivos `Reporte de impuestos PND3.csv` y `Reporte de
impuestos PND53.csv` que enlistan todas las líneas de facturas de proveedor
con las retenciones fiscales aplicables.

![Archivos CSV PND3 y PND53](../../../_images/pnd3-pnd53.png)
<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Konvergo ERP no puede generar directamente el reporte PND o PDF o el <b>certificado de retenciones fiscales</b>. Los archivos <code>Reporte de impuestos PND3.csv</code> y <code>Reporte de impuestos PND53.csv</code> generados deben exportarse a una herramienta externa para convertirlos a un reporte <b>PND de retenciones</b> o a un archivo <b>PDF</b>.</p>
</div>

## Factura impositiva

El reporte **PDF de factura impositiva** se puede generar desde Konvergo ERP a través
del módulo **Facturación**. Los usuarios tienen la opción de imprimir los
reportes en PDF para facturas normales y facturas impositivas. Para imprimir
las **facturas impositivas** , haga clic en **Imprimir facturas** en Konvergo ERP. Las
facturas normales se pueden imprimir como **facturas comerciales** al hacer
clic en el Botón de engranaje (⚙️) ‣ Imprimir ‣ Factura comercial.

![Impresión de una factura comercial ](../../../_images/tax-invoice.png)

### Ajustes de la sede/número de filial

Puede poner la **sede** o el **número de sucursal** de una empresa en la
aplicación **Contactos**. Un vez dentro, abra el **formulario del contacto**
de la empresa y en la pestaña **Ventas y Compra** :

  * SI el contacto es una filial, introduzca el **Número de filial** en el campo **ID de la empresa**.

  * Si el contacto es una **Sede** , deje el campo **ID de la empresa** **en blanco**.

![Sede/número de filial de la empresa](../../../_images/contact.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Estos datos se usan en el reporte PDF de <b>factura impositiva</b> y en la exportación del PND <b>reporte de impuesto</b>.</p>
</div>

