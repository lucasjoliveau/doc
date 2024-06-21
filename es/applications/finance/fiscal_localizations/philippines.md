# Filipinas

## Configuración

[Instale](../../general/apps_modules#general-install) el [paquete de
localización fiscal](../fiscal_localizations#fiscal-localizations-
packages) para **🇵🇭 Filipinas** para obtener todas las funciones de
contabilidad de manera predeterminada de esta localización; como los planes de
cuentas, impuestos y el reporte BIR 2307. Esto le proporcionará una plantilla
base para empezar a utilizar la contabilidad filipina.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Al crear una nueva base de datos y seleccionar <code>Filipinas</code> como país se instala de manera automática el módulo de localización fiscal <b>Filipinas - Contabilidad</b>.</p></li>
<li><p>Si el módulo ya está instalado en una empresa existente, entonces el <b>plan de cuentas</b> y los <b>impuestos</b> <b>no</b> se reemplazarán si ya hay asientos contables registrados.</p></li>
<li><p>Se instalará el reporte BIR 2307, pero las retenciones de impuestos deberán crearse manualmente.</p></li>
</ul>
</div>

### Plan de cuentas e impuestos

Se instala una configuración mínima predeterminada para los planes de cuentas
así como los siguientes tipos de impuestos con un enlace a su respectiva
cuenta:

  * IVA 12%

  * Exento de IVA

  * Retención fiscal

Para las retenciones de impuestos (Configuración ‣ Impuestos) hay un campo
adicional, **Philippines ATC** (Filipinas ATC), en la pestaña **Philippines**
(Filipinas).

![Campo de código Filipinas ATC establecido en impuestos.
](../../../_images/philippines-atc-code.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los códigos de Impuestos” ATC se usan para el reporte BIR 2307. Si crea un impuesto manualmente, debe agregar su código ATC.</p>
</div>

### Contactos

Cuando un contacto de una persona física o moral está ubicado en Filipinas,
debe llenar el campo **ID de impuesto** con su `Número de Identificación
Fiscal (TIN, por sus siglas en inglés)`.

Para personas físicas, identifíquelos usando los siguientes campos
adicionales:

  * **Nombre**

  * **Segundo nombre**

  * **Apellidos**

![Contacto de tipo persona física con los campos de nombre, segundo nombre y
apellidos. ](../../../_images/philippines-contact-individual.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Tanto para una <b>Persona moral</b> como para una <b>Persona física</b>, el número de identificación fiscal debe seguir el formato <code>NNN-NNN-NNN-NNNNN</code>. El código de ramificación debe tener los últimos dígitos de este número de identificación, o se puede dejar como <code>00000</code>.</p>
</div>

## Reporte BIR 2307

La información del reporte **BIR 2307** , también conocido como el
[Certificate of Creditable Tax Withheld at
Source](https://www.bir.gov.ph/index.php/bir-forms/certificates)
(Certificado de retención a cuenta del impuesto acreditable) se puede generar
para órdenes de compra y pagos a proveedores con las retenciones de impuestos
aplicables.

Para generar el reporte BIR 2307, seleccione una o varias facturas de
proveedor desde la vista de lista y haga clic en Acción ‣ Descargar BIR 2307
XLS.

![Selección de varias facturas de proveedor con la acción para "Descargar BIR
2307 XLS". ](../../../_images/philippines-multi-bill.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede ejecutar la misma acción en una factura de proveedor desde la vista de formulario.</p>
</div>

Aparecerá una ventana emergente para revisar la selección, haga clic en
**Generar**.

![Menú emergente para generar el archivo BIR 2307 XLS.
](../../../_images/philippines-generate.png)

Esto genera el archivo `Form_2307.xls` que enlista todas las líneas de
facturas de proveedor con las retenciones aplicables.

El proceso anterior también se puede hacer para _un solo_
[pago](../accounting/payments) de proveedor si se vincularon a una o más
[facturas de proveedor](../accounting/payments) con las retenciones
aplicadas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si no se aplica ninguna retención de impuesto, entonces el archivo XLS no generará registros para esas líneas de factura de proveedor.</p></li>
<li><p>Al agrupar pagos para varias facturas, Konvergo ERP divide los pagos de acuerdo al contacto. Desde un pago, al hacer clic en Acción ‣ Descargar BIR 2307 XLS, se generará un reporte que solo incluye las facturas de proveedor relacionadas a ese contacto.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Konvergo ERP no puede generar directamente el reporte BIR 2307 PDF o los archivos DAT. El archivo <code>Form_2307.xls</code> se puede exportar a una herramienta <em>externa</em> para convertirlo a BIR DAT o a formato PDF.</p>
</div>

