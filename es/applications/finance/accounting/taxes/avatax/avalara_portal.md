# Portal de Avalara (AvaTax)

La consola de administración de Avalara (_AvaTax_) ofrece varias opciones para
gestionar la cuenta, como la visualización y edición de las transacciones
enviadas desde Konvergo ERP a _AvaTax_ , los detalles sobre el cálculo de los
impuestos y los reportes fiscales. Además, es posible gestionar las exenciones
fiscales y consultar recursos relacionados con la declaración de impuestos.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Avalara es el desarrollador del software fiscal <em>AvaTax</em>.</p>
</div>

Para acceder a la consola, primero vaya al entorno de
[prueba](https://sandbox.admin.avalara.com/) o de
[producción](https://admin.avalara.com/) de Avalara. Esto dependerá del tipo
de cuenta que haya configurado en la [integración](../avatax), después
inicie sesión en la consola de administración.

![Tablero de Avalara luego de iniciar sesión en el portal administrativo de
Avalara.](../../../../../_images/avalara-portal.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Consulte la documentación de Avalara para obtener más información: <a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=qvv1656594440497&amp;topicId=Activate_your_Communications_Customer_Portal_account&amp;_LANG=enus">Active su cuenta del portal del cliente de comunicaciones</a>.</p>
</div>

## Transacciones

Para acceder a las transacciones, haga clic en el enlace **Transacciones** del
tablero principal al iniciar sesión en el Portal de Avalara (AvaTax). Vaya a
Transacciones ‣ Transacciones para acceder de forma manual a la página de
_Transacciones_ luego de haber iniciado sesión en la consola de Avalara.

![Portal de Avalara con el atajo de transacciones en un recuadro
rojo.](../../../../../_images/avalara-transactions.png)

### Editar transacciones

Haga clic en una transacción para abrir sus detalles, estos incluyen secciones
como **Detalles de la factura** , **Información adicional** e **Información
del cliente**. Haga clic en __**Editar detalles del documento** para realizar
modificaciones en la transacción.

Es posible agregar un **descuento** para ajustar la factura, estos son muy
útiles cuando la transacción ya está sincronizada con Avalara / _AvaTax_ y
necesita hacer cambios después.

### Filtro

En la página **Transacciones** podrá filtrarlas. Para ello, establezca los
campos **Desde** y **Hasta** y configure otros campos para filtrar, por
ejemplo:

  * **Estado del documento** : puede elegir entre las opciones **Todos** , **Anulados** , **Confirmados** , **Sin confirmar** y **Bloqueados**.

  * **Código del documento** : puede elegir entre las opciones **Coincidencia exacta** , **Empieza con** y **Contiene**.

  * **Código del cliente o del proveedor** : el código del cliente o del proveedor en Konvergo ERP (por ejemplo,`Contacto18`).

  * **País** : el país en el que se calculó este impuesto. Es un campo de texto.

  * **Región** : la región del país. Varía según el **país** que haya seleccionado.

Haga clic en icon:`fa-plus` **Filtros** para acceder a las siguientes
condiciones de filtrado:

  * **Tipo de documento** : elija entre las siguientes opciones, estas son **Todo** , **Factura de venta** , **Factura de compra** , **Factura de devolución** , **Factura de entrada de transferencia de inventario** , **Factura de salida de transferencia de inventario** y **Factura de aduanas**.

  * **ID de importación** : representa el ID de importación del documento.

### Ordenar por

En la página **Transacciones** estas aparecerán según el Filtro establecido
que se encuentra en la mitad superior de la página. Las siguientes columnas
están disponibles de forma predeterminada y puede ordenarlas de manera
ascendente o descendente:

  * **Código del documento** : puede elegir entre las opciones **Coincidencia exacta** , **Empieza con** y **Contiene**.

  * **Estado del documento** : puede elegir entre las opciones **Todos** , **Anulados** , **Confirmados** , **Sin confirmar** y **Bloqueados**.

  * **Código del cliente o del proveedor** : este es el código del cliente o del proveedor en Konvergo ERP (por ejemplo,`Contacto18`).

  * **Región** : la región del país. Varía según el **país** seleccionado.

  * **Importe** : el importe numérico del importe total del documento de Konvergo ERP.

  * **Impuesto** : el importe numérico del impuesto aplicado al total.

![La página de transacciones en el portal de Avalara. El filtro y las opciones
de ordenación aparecen en un recuadro
rojo.](../../../../../_images/transactions.png)

#### Personalizar columnas

Puede agregar columnas adicionales al hacer clic en __**Personalizar
columnas**. Esta acción abrirá una ventana emergente, haga clic en el menú
desplegable de la **columna** que debe modificar.

Es posible agregar las siguientes columnas para obtener más información sobre
las transacciones:

  * **Calculado por AvaTax** : el importe del impuesto calculado por _AvaTax_.

  * **País** : el país en el que se calculó este impuesto. Es un campo de texto.

  * **Código del cliente o del proveedor** : el código del cliente o del proveedor en Konvergo ERP (por ejemplo,`Contacto18`).

  * **Divisa** : la abreviatura armonizada de la divisa correspondiente al importe total.

  * **Fecha del documento** : la fecha de creación del documento.

  * **Estado del documento** : puede elegir entre las opciones **Todos** , **Anulados** , **Confirmados** , **Sin confirmar** y **Bloqueados**.

  * **Tipo de documento** : elija entre las siguientes opciones, estas son **Todo** , **Factura de venta** , **Factura de compra** , **Factura de devolución** , **Factura de entrada de transferencia de inventario** , **Factura de salida de transferencia de inventario** y **Factura de aduanas**.

  * **ID de importación** : representa el ID de importación del documento.

  * **Última modificación** : marca de tiempo de la última vez que el documento fue modificado.

  * **Código de la ubicación** : el código de la ubicación utilizado para calcular el impuesto. Depende de la dirección de entrega.

  * **Número de la orden de compra** : el número de la orden de compra.

  * **Código de referencia** : el código de referencia de Konvergo ERP (por ejemplo, NV/2024/00003)

  * **Región** : la región del país. Varía según el **país** que haya seleccionado.

  * **Código del vendedor** : el ID numérico del usuario asignado a la orden de venta en Konvergo ERP.

  * **Fecha del impuesto** : el mes, día y año del cálculo del impuesto.

  * **Tipo de anulación de impuestos** : si debería aparecer una exención. Si no hay ninguna, complete el campo con **Ninguno**.

Haga clic en __**Columna** para agregar una nueva.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Consulte esta documentación de Avalara para obtener más información sobre las transacciones de <em>AvaTax</em>: <a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=qvv1656594440497&amp;topicId=transactions&amp;_LANG=enus">Transacciones</a>.</p>
</div>

### Importar y exportar

Vaya a la página Transacciones y haga clic en __**Importar transacciones** o
en __**Exportar transacciones** para realizar alguna de estas dos acciones.

### Reportes

Para acceder a los reportes vaya a Reportes en el menú superior de la consola
de administración de Avalara y luego seleccione una de las pestañas de
reportes disponibles: **Reportes de transacciones** , **Reportes de
obligaciones y declaraciones fiscales** o **Reportes de exenciones**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Además, existen las pestañas <b>Favoritos</b> y <b>Descargas</b>. La pestaña <b>Favoritos</b> incluye todas las configuraciones de reportes marcadas como favoritas por el usuario de Avalara. La pestaña <b>Descargas</b> cuenta con una vista de lista donde el usuario puede descargar los reportes de las transacciones de alto volumen creados en los últimos 30 días.</p>
</div>

Elija la **categoría del reporte** y el **nombre del reporte** en la sección
**Seleccione un reporte**.

Después, complete la sección **Seleccionar detalles del reporte**. Estas
opciones varían según la pestaña que haya seleccionado con anterioridad.

Según el tamaño del reporte, las siguientes dos opciones estarán disponibles
en la sección etiquetada como **Seleccione el número aproximado de
transacciones para su reporte** : **Crear y descargar el reporte al instante**
(para reportes pequeños) y **Crear y descargar el reporte en segundo plano**
(para reportes más grandes). Seleccione una u otra dependiendo del volumen de
transacciones correspondientes.

Por último, en la sección **Vista previa e exportación del reporte** ,
seleccione el tipo de archivo a descargar. Puede elegir entre **.PDF** o
**.XLS**. También tiene la opción de previsualizar el archivo si hace clic en
**Vista previa**.

Luego de realizar todas las configuraciones, haga clic en **Crear reporte**
para descargarlo. Haga clic en __**Agregar este reporte a favoritos** para
guardar esta configuración en los favoritos del usuario.

Haga clic en __**Descargar** después de crear el reporte, así descargará el
archivo a su dispositivo.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione un reporte preconfigurado en la sección <b>Utilizado con frecuencia</b> del tablero de reportes.</p>
<p>Haga clic en la opción de <b>Reportes</b> en el menú superior de la consola de gestión de Avalara y deslícese hasta el final de la página.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=rjq1671176624730&amp;topicId=Reports_in_AvaTax&amp;_LANG=enus">Documentación de Avalara: Reportes en AvaTax</a>.</p>
</div>

## Agregar más jurisdicciones

Puede agregar más jurisdicciones (ubicaciones de impuestos) en la consola de
gestión de Avalara. Vaya ya sea a un entorno
[sandbox](https://sandbox.admin.avalara.com/) o de
[producción](https://admin.avalara.com/) de Avalara. Esto depende de qué tipo
de cuenta configuró en la [integración](../avatax).

Después, vaya a Ajustes ‣ Where you collect tax (Dónde recolecta sus
impuestos). Tendrá que seleccionar de entre tres pestañas diferentes,
dependiendo de la necesidad de su empresa. La primera pestaña es **Sales and
use tax** (impuestos de venta y uso), con la que se pueden recolectar
impuestos para los Estados Unidos. Haga clic en __**Add to where you collect
sales and use tax** (agregar a donde recolecta impuestos de venta y uso) para
agregar otra ubicación donde la empresa recolecta impuestos de uso y venta.

La segunda opción es la pestaña **VAT/GST** (IVA/Impuesto sobre bienes y
servicios) donde puede seleccionar el icono __**Add a country or territory
where you collect VAT/GST** (agregar un país o territorio donde recolecta
IVA/Impuesto sobre bienes y servicios) para agregar otro país o territorio
donde la empresa recolecta IVA o impuesto sobre bienes y servicios.

Finalmente, hasta la derecha encontrará la pestaña **Customs duty** (impuesto
de aduana) en la que podrá agregar un país en el que la empresa recolecta
impuestos de aduana. Solo haga clic en el icono __**Add a country where you
calculate customs duty** (agregar un país donde se calcula el impuesto de
aduana) debajo de la pestaña.

![Consola de gestión de AvaTax en la página Dónde recolecta impuestos, con el
botón agregar e impuesto de usos y ventas
resaltados.](../../../../../_images/where-you-collect-tax.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=bla1700809896571_bla1700809896571&amp;topicId=nbw1698727575499&amp;_LANG=enus">Consulte la documentación de Avalara: agregar impuestos de la jurisdicción local</a>.</p>
</div>

## Certificado de exención de impuestos

Los certificados de exención de impuestos para los clientes se pueden agregar
a la consola de gestión de Avalara para que _AvaTax_ sepa qué clientes están
exentos de pagar algunos impuestos en específico. Para agregar un _certificado
de exención_ vaya a Exemptions (exenciones) ‣ Customer certificates
(certificados de clientes). Aquí, haga clic en __**Add a certificate**
(agregar un certificado) para configurar una exención.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Se requiere una suscripción Avalara a Exemption Certificate Management (ECM) (Gestión de certificados de exención) para poder adjuntar imágenes de certificado y para estar listos para una auditoría. Para más información sobre cómo suscribirse a este servicio, visite <a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=hff1682048150115_hff1682048150115&amp;topicId=fol1682356576230&amp;_LANG=enus">Avalara</a>.</p>
</div>

## Operaciones de fin de año

Los servicios de Avalara incluyen servicios de declaración de impuestos para
cuando deba presentar los impuestos al final del año. Inicie sesión en el
[portal de administración](https://admin.avalara.com/) para acceder al
registro de servicios fiscales de Avalara. Después, desde el tablero
principal, haga clic en **Declaraciones**. Avalara le solicitará al usuario
que inicie sesión por motivos de seguridad y le redirigirá al portal de
_declaraciones_.

![Portal de Avalara con los atajos para regresar
resaltados.](../../../../../_images/avalara-returns.png)

Haga clic en **Get started** (Iniciar) para iniciar el proceso de devolución
de impuestos. Para más información, vea la documentación de Avalara [About
Managed Returns](https://community.avalara.com/support/s/document-
item?language=en_US&bundleId=hps1656397152776_hps1656397152776&topicId=Learn_about_Managed_Returns&_LANG=enus)
(sobre la gestión de devoluciones).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede hacer clic en el botón Returns (devoluciones) en el menú superior de la consola de gestión Avalara.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../avatax">Integración con AvaTax</a></p></li>
<li><p><a href="avatax_use">Uso de AvaTax</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1">Cumplimiento fiscal en Estados Unidos: video de eLearning sobre AvaTax</a></p></li>
</ul>
</div>

