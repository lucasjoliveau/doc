# Authorize.Net

[Authorize.Net](https://www.authorize.net) es un proveedor de pago establecido
en Estados Unidos que permite a las empresas aceptar **tarjetas de crédito**.

## Configuración

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
</ul>
</div>

### Pestaña de credenciales

Konvergo ERP necesita sus **claves y credenciales API** para conectarse con su cuenta
de Authorize.Net, estas son:

  * **ID de inicio de sesión API** : el ID que se usa solo para identificar la cuenta con Authorize.Net.

  * **Clave de transacción API**

  * **Clave de firma API**

  * **Clave de cliente API**

Para obtenerlas, inicie sesión en su cuenta de Authorize.Net, vaya a Cuenta ‣
Ajustes ‣ Ajustes de seguridad ‣ Credenciales y claves API, genere su **clave
de transacción** y **clave de firma** , y péguelos en los campos relacionados
en Konvergo ERP. Posteriormente, haga clic en **Generar clave de cliente**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está probando Authorize.Net con una <em>cuenta sandbox</em> , cambie el <b>Estado</b> a <b>Modo de prueba</b>. Le recomendamos hacerlo en una base de datos de prueba de Konvergo ERP, en vez de hacerlo en su base de datos principal.</p>
<p>Si estableció el <b>Modo de prueba</b> en Konvergo ERP y usa una cuenta de Authorize.Net en lugar de una cuenta sandbox, aparecerá el siguiente error: <em>El ID del comerciante o su contraseña no es válida o la cuenta está inactiva</em>.</p>
</div>

### Pestaña de configuración

#### Hacer una retención de tarjeta de crédito

Con Authorize.net, puede activar la [captura
manual](../payment_providers#payment-providers-manual-capture). Si es
así, los fondos se apartan por 30 días en la tarjeta del cliente, pero no se
hace el cargo todavía.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Después de <b>30 días</b>, Authorize.net <b>anula de forma automática</b> la transacción.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

## Pagos ACH (solo para Estados Unidos)

El ACH es un sistema electrónico de transferencia de fondos utilizado entre
cuentas bancarias en Estados Unidos.

### Configuración

Para hacer que los clientes puedan pagar con el ACH, [inicie sesión en el
servicio de eCheck de
Authorize.Net](https://www.authorize.net/payments/echeck). Una vez que
tenga activado el eCheck, duplique el proveedor de pago previamente
configurado de Authorize.Net en Konvergo ERP en Contabilidad ‣ Configuración ‣
Proveedores de pago ‣ Authorize.net ‣ ⛭ Acción ‣ Duplicar. Luego, cambie el
nombre del proveedor para diferenciar las versiones (por ejemplo,
`Authorize.net - Bancos`).

Abra la pestaña de **Configuración** , establezca el campo de **Permitir pagos
desde** en **Cuenta bancaria (solo E.U.A)**.

Cuando esté listo, cambie el **Estado** del proveedor a **Habilitado** para
una cuenta normal o en **Modo de prueba** si es para cuenta sandbox.

## Importar un estado de cuenta de Authorize.Net

### Exportar desde Authorize.Net

<div class="admonition-template alert" id="authorize-import-template">
<p class="alert-title">
Plantilla</p><p><a href="https://docs.google.com/spreadsheets/d/1CMVtBWLLVIrUpYA92paw-cL7-WdKLbaa/edit?usp=share_link&amp;ouid=105295722917050444558&amp;rtpof=true&amp;sd=true">Descargue la plantilla de Excel para realizar una importación</a></p>
</div>

Para exportar un estado de cuenta:

  * Inicie sesión en Authorize.Net

  * Vaya a Cuenta ‣ Estados de cuenta ‣ Estado de cuenta de cierre eCheck.Net.

  * Defina un rango de exportación utilizando una liquidación por lotes de _apertura_ y de _cierre_. Todas las transacciones dentro de ambas liquidaciones por lotes se exportarán a Konvergo ERP.

  * Seleccione todas las transacciones dentro del rango que desee, cópielas y péguelas en la hoja **Descarga Reporte 1** de la Plantilla de Excel de importación.

![Selección de las transacciones de Authorize.Net para
importar](../../../_images/authorize-report1.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Liquidación por lotes de un extracto de Authorize.net" class="align-center" src="../../../_images/authorize-settlement-batch.png"/>
<p>En este caso, el primer lote del año (01/01/2021) pertenece a la liquidación del 31/12/2020, entonces la liquidación de <b>apertura</b> es del 31/12/2020.</p>
</div>

Una vez que los datos estén en la hoja **Descarga Reporte 1** :

  * Vaya a la pestaña de **Búsqueda de transacciones** en Authorize.Net.

  * En la sección **Fecha de liquidación** seleccione el rango de las fechas de liquidación por lotes usado anteriormente en los campos **Desde:** y **Hasta:** y haga clic en **Buscar**.

  * Cuando se genere la lista, haga clic en **Descargar en el archivo**.

  * En la ventana emergente, seleccione **Campos expandidos con respuesta CAVV/Separados por comas** , active la opción **Incluir encabezados de las columnas** y haga clic en **Enviar**.

  * Abra el archivo de texto , seleccione **Todos** , copie los datos y péguelos en la hoja **Descarga Reporte 2** de la plantilla de Excel para importar.

  * Las líneas de tránsito se completan y actualizan automáticamente en las hojas **tránisto para el reporte 1** y **tránsito para el reporte 2** de la plantilla de Excel para importar. Asegúrese de que todas las entradas estén presentes y **si no es el caso** , copie la formula de las líneas previamente completadas de las hojas **tránsito para el reporte 1** o del **2** y péguelas en las líneas vacías.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para obtener el balance de cierre correcto, <em>no</em> elimine ninguna línea de las hojas de Excel.</p>
</div>

### Importar a Konvergo ERP

Para importar los datos a Konvergo ERP:

  * Abra la plantilla de Excel para importar.

  * Copie los datos de la hoja **tránsito para el reporte 2** y use la opción de _pegado especial_ para pegar solo los valores en la hoja **Importar de Konvergo ERP a CSV**.

  * Busque las celdas _azules_ en la hoja **Importar de Konvergo ERP a CSV**. Son asientos de devolución sin número de referencia. Puesto que no se pueden importar así, vaya a Authorize.Net ‣ Cuenta ‣ Extractos ‣ Extracto de cierre eCheck.Net.

  * Busque la opción **Cobrar transacción/Devolución** , y haga clic ahí.

  * Copie la descripción de la factura, péguela en la celda **Etiqueta** de la hoja **Importar de Konvergo ERP a CSV** y agregue `Devolución /` antes de la descripción.

  * Si hay varias facturas, agregue una línea a la Plantilla de Excel de importación por cada factura y copie y pegue la descripción en cada respectiva línea de **Etiqueta**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para <b>devoluciones/reembolsos combinados</b> en los pagos, cree una nueva línea en la <a href="#authorize-import-template"><span class="std std-ref">Plantilla de Excel de importación</span></a> para cada factura.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Descripción de un contracargo" src="../../../_images/authorize-chargeback-desc.png"/>
</div>

  * Luego, elimine las líneas de apuntes de _transacción cero_ y _transacción anulada_ , y cambie el formato de la columna **Importe** a _Número_ en la hoja **Importar de Konvergo ERP a CSV**.

  * Regrese a Extracto de cierre eCheck.Net ‣ Buscar una transacción y busque de nuevo las fechas de liquidación por lotes que uso anteriormente.

  * Verifique que las fechas de liquidación por lotes en eCheck.Net coincidan con las fechas de los pagos correspondientes que se encuentran en la columna de **Fecha** de la hoja **Importar de Konvergo ERP a Konvergo ERP CSV**.

  * Si no coinciden, reemplace la fecha con la que aparece en eCheck.Net. Filtre la columna por _fecha_ y asegúrese de que el formato sea `MM/DD/AAAA`.

  * Copie los datos, incluyendo los encabezados de la columna, de la hoja **Importar de Konvergo ERP a CSV** , péguelos en un nuevo archivo de Excel y guárdelo como formato CSV.

  * Abra la aplicación Contabilidad, vaya a Configuración ‣ Diarios, seleccione la casilla **Authorize.Net** y haga clic en Favoritos‣ Importar registros ‣ Cargar archivo. Seleccione el archivo CSV y súbalo a Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Lista de <a href="https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293">códigos de reembolso de eCheck.Net</a></p>
</div>

  *[ACH]: sistema automático de transferencia de fondos

