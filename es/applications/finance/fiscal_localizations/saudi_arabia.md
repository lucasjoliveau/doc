# Arabia Saudita

## Configuración

[Instale](../../general/apps_modules#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Arabia Saudita:

Nombre | Nombre técnico | Descripción  
---|---|---  
Arabia Saudita - Contabilidad | `l10n_sa` | [Paquete de localización fiscal](../fiscal_localizations#fiscal-localizations-packages) predeterminado  
Arabia Saudita - Facturación electrónica | `l10n_sa_edi` | Implementación de las facturas electrónicas ZATCA  
Arabia Saudita - Facturación electrónica (simplificada) | `l10n_sa_edi_simplified` | Implementación de facturas electrónicas ZATCA simplificadas (Punto de Venta)  
Arabia Saudita - Punto de venta | `l10n_sa_pos` | Cumplimiento con el punto de venta  
  
## Facturas electrónicas ZATCA

El sistema de facturas electrónicas ZATCA esta diseñado para optimizar y
digitalizar el proceso de facturación para empresas que operan en Arabia
Saudita.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx">Página web de facturación electrónica ZATCA</a></p>
</div>

### Información de la empresa

Vaya a Ajustes ‣ Ajustes generales ‣ Empresas, haga clic en **Actualizar
información** y asegúrese de que los siguientes datos de su empresa estén
completos y actualizados.

  * El **Nombre completo de la empresa**.

  * Todos los campos relevantes para **Dirección** , incluyendo el **Número exterior** y la **Clave catastral** (cada uno de cuatro dígitos).

  * Seleccione un **Esquema de identificación** empresarial. Le recomendamos usar el **Número comercial de registro**.

  * Introduzca el **Número de Identificación** para el **Esquema de identificación**.

  * El **NIF**.

  * Asegúrese que la **Divisa** esté establecida en **SAR**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También es necesario completar algunos datos similares para empresas que son partners.</p>
</div>

### Modo de prueba

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Le recomendamos que haga pruebas exhaustivas en los flujos de trabajo para facturar usando el portal de <b>simulación</b> Fatoora primero, pues <b>cualquier</b> factura que se envíe al portal normal de Fatoora será registrada y puede costarle multas y penalizaciones.</p>
</div>

#### Portal de simulación de Fatoora

Inicie sesión en el [portal de Fatoora](https://fatoora.zatca.gov.sa/) usando
las credenciales ZATCA de la empresa. Luego, haga clic en el botón de **Portal
de simulación de Fatoora** para cambiar al portal de simulación.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf">Manual de usuario  para el portal de ZACTA Fatoora versión 3 (Mayo 2023)</a></p>
</div>

#### Integración API con ZATCA

En Konvergo ERP, vaya a Contabilidad ‣ Configuración ‣ Ajustes. En **Integración API
con ZATCA** , seleccione **Simulación (Pre-Producción)** **Modo API** y haga
clic en **Guardar**.

#### Diarios de ventas

Cada diario de ventas en Konvergo ERP necesita una configuración. Para ello, vaya a
Contabilidad ‣ Configuración ‣ Diarios, abra cualquier diario de ventas (por
ejemplo, Facturas de clientes), y vaya a la pestaña de **ZATCA**. Una vez ahí,
introduzca cualquier **Número de serie** para identificar el diario.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede usar el mismo número de serie para todos los diarios de ventas de la empresa.</p>
</div>

Luego, haga clic en **Diario de integración**. En el cuadro de diálogo
emergente, se requiere un código OTP. Para obtenerla, abra el [Portal de
simulación Fatoora](https://fatoora.zatca.gov.sa/), haga clic en **Integrar
nueva unidad/dispositivo de solución** , escoja el número de los códigos de la
contraseña de un solo uso para generar (uno por diario para configurar), y
haga clic en **Generar código OTP**. Copie un código OTP, pegue en la ventana
de diálogo en Konvergo ERP y haga clic en **Solicitar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El código OTP vence después de una hora.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si ocurre algún error durante la integración, haga clic en  <b>Regenerar CSR</b> para iniciar de nuevo.</p>
</div>

#### Prueba

Al confirmar una factura, ahora tiene la opción de procesar la factura
enviándola directamente al portal de simulación de Fatoora. Konvergo ERP muestra la
respuesta del portal después de cada envío. Solo las facturas rechazadas se
pueden cambiar a estado de borrador y editarse en Konvergo ERP. Además, al final de
cada día, Konvergo ERP envía todas las facturas sin procesar al portal.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Se recomienda hacer pruebas en todos los flujos de trabajo para facturas, de preferencia con facturas reales y por una cantidad razonable de tiempo.</p></li>
<li><p>Compare la página de estadísticas de las facturas recibidas en el portal de simulación de Fatoora con una lista de facturas en Konvergo ERP para asegurarse de que ambas coinciden.</p></li>
</ul>
</div>

#### Impuestos

Al usar un **impuesto del 0%** en una factura de cliente, es necesario que
especifique el por qué de su uso. Para configurar los impuestos, vaya a
Contabilidad ‣ Configuración ‣ Ajustes ‣ Impuestos, y abra el importe que
desea editar. En la sección de **Opciones avanzadas** , seleccione un **Código
de razón de la excepción** y haga clic en **Guardar**.

Al usar **retención** o **retener una cantidad** en una factura de cliente,
necesita especificar el importe usado para retener la cantidad.

### Modo de producción

Cuando esté listo para la producción, cambie el modo API a **Producción** y
haga clic en **Guardar**.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Establecer el <b>modo API</b> a <b>Producción</b> es <b>irreversible</b>.</p>
</div>

Los diarios de ventas que estaban inicialmente vinculados al portal de
simulación, ahora necesitan vincularse al portal normal. Para hacerlo, vuelva
a los diarios de integración asegurándose de usar el [portal normal de
Fatoora](https://fatoora.zatca.gov.sa/) esta vez.

  *[OTP]: Contraseña de un solo uso

