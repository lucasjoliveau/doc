# Declaración de impuestos

Las empresas con un número de IVA registrado deben presentar una **declaración
de impuestos** mensual o trimestral, según su volumen de negocios y el
reglamento del registro. La declaración fiscal (o declaración de impuestos)
proporciona a las autoridades fiscales información relacionada con las
operaciones gravables realizadas por la empresa. El **IVA repercutido** se
impone sobre el número de bienes y servicios vendidos por una empresa,
mientras que el **IVA soportado** corresponde al impuesto que se agrega al
precio al adquirir bienes o servicios. De acuerdo con estos valores, la
empresa puede calcular el importe del impuesto que debe pagar o que se le
devolverá.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede encontrar información adicional sobre el IVA y su funcionamiento en esta página de la Comisión Europea: <a href="https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en">«¿Qué es el IVA?»</a>.</p>
</div>

## Prerrequisitos

### Periodicidad de la declaración de impuestos

La configuración de la **periodicidad de la declaración de impuestos** permite
a Konvergo ERP calcular correctamente su declaración de impuestos y además enviarle un
recordatorio para que nunca se le pase la fecha límite.

Para hacerlo, vaya a Contabilidad ‣ Configuración ‣ Ajustes y en
**periodicidad de la declaración** , puede establecer:

  * **Periodicidad** : defina si presenta la declaración de impuestos de forma mensual o trimestral;

  * **Recordatorio** : defina en qué momento Konvergo ERP debería recordarle que presente su declaración de impuestos;

  * **Diario** : seleccione el diario en el cual se registrará la declaración de impuestos.

![Frecuencia en la que deben realizarse las declaraciones de
impuestos](../../../../_images/tax_return_periodicity.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Suele configurarse durante la <a href="../get_started">instalación inicial de la aplicación</a>.</p>
</div>

### Tablas de impuestos

Konvergo ERP genera reportes de impuestos basados en los ajustes de las **tablas de
impuestos** configuradas en sus impuestos. Por lo tanto, debe asegurarse de
que todas las transacciones registradas utilizan los impuestos correctos. Para
más información, consulte las **reglas de Impuestos** en la pestaña
**artículos del diario** de cualquier factura.

![vea las tablas de impuestos que se utilizan para registrar las transacciones
en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/tax_return_grids.png)

Si desea configurar sus tablas de impuestos, vaya a Contabilidad ‣
Configuración ‣ Impuestos, y abra el impuesto que desee modificar. Una vez
ahí, podrá editar la configuración de sus impuestos, junto con las tablas de
impuestos que se utilizan para registrar facturas o notas de crédito.

![Configuración de impuestos y sus tablas de
impuestos](../../../../_images/tax_return_taxes.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Por lo general, los impuestos y los reportes ya están preconfigurados en Konvergo ERP mediante los <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">paquetes de localización fiscal</span></a> que se instalan dependiendo del país que seleccione al crear su base de datos.</p>
</div>

## Cerrar un periodo de impuestos

### Fecha de bloqueo de impuestos

Cualquier nueva transacción con fecha contable anterior a la **fecha de
bloqueo de impuestos** desplazará sus valores fiscales al siguiente periodo
fiscal abierto. Esta función es útil para evitar que se realicen cambios en un
reporte una vez que haya cerrado su periodo.

Por lo tanto, le recomendamos bloquear su fecha fiscal antes de realizar su
**asiento contable de cierre**. De esta forma, otros usuarios no podrán
modificar o añadir transacciones que repercutirían en el **asiento contable de
cierre** , lo que puede ayudarle a evitar errores en la declaración de
impuestos.

Para consultar o editar su **fecha de bloqueo de impuestos** actual, vaya a
Contabilidad ‣ Contabilidad ‣ Acciones: bloquear fechas.

![Bloquear impuestos durante un periodo específico en la aplicación
Contabilidad de Konvergo ERP](../../../../_images/tax_return_lock.png)

### Reporte de impuestos

Una vez que se hayan contabilizado todas las transacciones que incluyen
impuestos durante el periodo que desea reportar, haga clic en **Reporte de
impuestos** en :menuselection: `Contabilidad --> Reportes --> Reportes de
auditoría: reporte de impuestos`. Asegúrese de seleccionar el periodo correcto
que desea declarar mediante el filtro de fechas, de este modo podrá tener una
visión general de su reporte de impuestos. Desde esta vista, puede acceder
fácilmente a diferentes formatos de su reporte de impuestos, como `PDF` y
XLSX. En estos se incluyen todos los valores que debe declarar a Hacienda,
junto con el importe que debe pagar o que le será devuelto.

![descargue el PDF con su reporte de
impuestos](../../../../_images/tax_return_report.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si olvidó bloquear su fecha fiscal antes de hacer clic en <b>Cerrar asiento contable</b>, Konvergo ERP bloqueará automáticamente su periodo fiscal en la misma fecha que la fecha contable de su asiento. Este mecanismo de seguridad puede prevenir algunos errores fiscales, pero se aconseja bloquear su fecha fiscal de forma manual, como se describió anteriormente.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../taxes">Impuestos</a></p></li>
<li><p><a href="../get_started">Información básica</a></p></li>
<li><p><a href="../../fiscal_localizations">Localizaciones fiscales</a></p></li>
</ul>
</div>

