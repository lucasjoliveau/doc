# Luxemburgo

## Configuración

[Instale](../../general/apps_modules#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Luxemburgo:

Nombre | Nombre técnico | Descripción  
---|---|---  
**Luxemburgo - Contabilidad** | `l10n_lu` | [Paquete de localización fiscal](../fiscal_localizations#fiscal-localizations-packages) predeterminado  
**Luxemburgo - Reportes contables** | `l10n_lu_reports` | Reportes específicos del país  
**Luxemburgo - Reporte anual de IVA** | `l10n_lu_reports_annual_vat` | Reportes específicos del país  
![Los tres módulos para el paquete de localización fiscal de Luxemburgo en
Konvergo ERP](../../../_images/modules1.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Cuando instala el módulo <b>Luxemburgo - Reportes contables</b> se instalan los tres módulos a la vez.</p>
</div>

## Plan de cuentas estándar - PCN 2020

El [paquete de localización fiscal](../fiscal_localizations#fiscal-
localizations-packages) de Luxemburgo incluye el **Plan de cuentas estándar
(PCN 2020)** actual, vigente desde enero de 2020.

## Declaración fiscal eCDF

Las declaraciones fiscales en Luxemburgo necesitan un archivo XML específico
para subir al eCDF.

Para descargarlo, vaya a Contabilidad ‣ Reportes ‣ Reportes de auditoría ‣
Declaración de impuestos y haga clic en **Exportar la declaración de eCDF**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../accounting/reporting/tax_returns">Declaración de impuestos</a></p></li>
<li><p><a href="http://www.ecdf.lu">Plataforma de recolección electrónica de datos financieros (eCDF)</a></p></li>
</ul>
</div>

## Declaración fiscal anual

Puede generar un archivo XML para entregar su declaración de impuesto anual
electrónicamente a la autoridad fiscal.

Para hacerlo, vayan a Contabilidad ‣ Reporte ‣ Luxemburgo ‣ Declaración fiscal
anual, haga clic en **Crear** , después defina el periodo anual en el campo
**Año**.

La **declaración anual simplificada** se genera automáticamente. Puede agregar
valores manualmente en todos los campos para obtener una **declaración anual
completa**.

![La aplicación Contabilidad de Konvergo ERP \(con la localización de Luxemburgo\)
genera una declaración anual de impuestos.](../../../_images/annual-tax-
report.png)

Para ayudarle a completarlo, puede usar la información que tiene en el
**Reporte de impuestos**. Vaya a Contabilidad ‣ Reportes ‣ Reportes de
auditoría ‣ Reportes de impuestos, después haga clic en el menú desplegable de
**Reportes de impuestos** y seleccione el tipo de reporte que desea mostrar.

![Menú desplegable para seleccionar el tipo de reporte de
impuestos](../../../_images/tax-report-types.png)

Por último, haga clic en **Exportar XML** para descargar el archivo XML.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta función requiere que el módulo <b>Luxemburgo - Declaración de IVA anual</b> esté instalado.</p>
</div>

## FAIA (SAF-T)

**FAIA (Fichier d’Audit Informatisé AED)** es un archivo estandarizado y
estructurado que facilita el intercambio de información entre el sistema de
contabilidad del contribuyente y la autoridad fiscal. Es la versión
luxemburguesa del SAF-T (Standard Audit File for Tax) recomendado por la OCDE.

Konvergo ERP puede generar un archivo XML que contenga todo el contenido de un periodo
contable según las reglas que las autoridades de Luxemburgo imponen en
archivos digitales de auditoría.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta función requiere que el módulo <b>Luxemburgo - Reportes de contabilidad</b> esté instalado.</p>
</div>

### Exportar el archivo FAIA

Vaya a Contabilidad ‣ Reportes ‣ Reportes de auditoría ‣ Libro mayor general
después haga clic en **FAIA**.

