# Uso de AvaTax

AvaTax es un software para calcular impuestos que se puede integrar con Konvergo ERP
en los Estados Unidos y Canadá. Una vez que haya terminado la [configuración
de la integración](../avatax), el cálculo de los impuestos es fácil y
automático.

## Cálculo de impuestos

Para poder calcular impuestos en las cotizaciones y facturas de Konvergo ERP con
AvaTax primero debe confirmar los documentos en el flujo de ventas. También
puede calcular los impuestos de forma manual con el botón **Calcular impuestos
con AvaTax** cuando los documentos estén en borrador.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si hace clic en el botón <b>Calcular impuestos con AvaTax</b> los impuestos se volverán a calcular si cualquiera de las líneas de producto se editan en la factura.</p>
</div> ![Una cotización de venta con los botones para confirmar y
calcular impuestos con AvaTax resaltados.](../../../../../_images/calculate-
avatax.png)

El cálculo de impuestos se activa durante la siguiente activación automática y
la siguiente activación manual.

### Activaciones automáticas

  * Cuando el representante de ventas envía la cotización por correo electrónico con el botón :guilabel:` Enviar por correo electrónico` (ventana emergente).

  * Cuando el cliente ve la cotización en línea desde el portal.

  * Cuando la cotización se confirma y se convierte en una orden de venta.

  * Cuando el cliente ve la cotización en el portal.

  * Cuando se valida un borrador de factura.

  * Cuando el cliente ve la suscripción en el portal.

  * Cuando una suscripción genera una factura.

  * Cuando el cliente llega a la última página del proceso de pago de comercio electrónico.

### Activaciones manuales

  * El botón **Calcular impuestos con AvaTax** en la parte inferior de la cotización.

  * El botón **Calcular impuestos con AvaTax** en la parte superior de la factura.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Use el campo <b>Código de contacto Avalara</b> que está disponible en los registros, cotizaciones y facturas del cliente para confirmar información entre Konvergo ERP y AvaTax. Este campo se ubica en la pestaña :menuselection:` Otra información` de la orden de venta o la cotización en la sección <b>Ventas</b>.</p>
<p>On the customer record, navigate to <em>Contacts app</em> and select a contact. Then open the
<b>Sales &amp; Purchase</b> tab and the <b>Avalara Partner Code</b> under the
<b>Sales</b> section.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La posición fiscal <b>Automatic Tax Mapping (AvaTax)</b> también se aplica en esos documentos de Konvergo ERP, como en las suscripciones.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p></li>
</ul>
</div>

## Sincronización con AvaTax

La sincronización se hace con AvaTax cuando la _factura_ se crea en Konvergo ERP. Esto
significa que el impuesto de ventas se registra con Avalara (el desarrollador
del software AvaTax).

Para hacerlo vaya a Ventas ‣ Órdenes ‣ Cotizaciones y seleccione una
cotización de la lista.

Después de confirmar una cotización y validar la entrega, haga clic en **Crear
factura** , Indique si será una **Factura normal** , **Anticipo (porcentaje)**
, o **Anticipo (cantidad fija)**.

Después, haga clic en **Crear y ver factura**. Para ver los impuestos
registrados vaya a la pestaña **Apuntes contables** de la factura. Aquí verá
diferentes impuestos dependiendo de la ubicación de la **Dirección de
entrega**.

![Asientos de diario resaltados en una factura de
Konvergo ERP.](../../../../../_images/journal-items.png)

Finalmente, haga clic en el botón **Confirmar** para completar la factura y
hacer la sincronización con el portal de AvaTax.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>No puede <b>Restablecer a borrador</b> una factura ya que esto afecta la sincronización con el portal de AvaTax. Mejor haga clic en :guilabel:` Agregar nota de crédito` y declare: <code>Sincronización con el portal AvaTax</code>. Para más información consulte esta documentación: <a href="../../customer_invoices/credit_notes">Notas de crédito y reembolsos</a>.</p>
</div>

## Descuentos sobre el precio establecido

Para agregar un descuento sobre el precio establecido a un cliente importante,
haga clic en **Agregar una línea** cuando esté en la factura del cliente.
Agregue un producto de descuento y configure el **Precio** a un valor ya sea
positivo o negativo. Para volver a calcular los impuestos, haga clic en
**Calcular impuestos con AvaTax**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El cálculo de impuestos no se puede hacer en subtotales negativos o en notas de crédito.</p>
</div>

## Registro

Es posible registrar las acciones de Avalara/_AvaTax_ en Konvergo ERP para poder
analizarlas más, o para verificar la función. Puede iniciar sesión con los
ajustes de _AvaTax_.

Para empezar a registrar las acciones de _AvaTax_ primero vaya a Contabilidad
‣ Configuración ‣ Ajustes.

Después, en la sección **Impuestos** de los ajustes de **AvaTax** haga clic en
**Empezar a registrar por 30 minutos**.

Al iniciar el proceso de registro, Konvergo ERP registrará todas las acciones que
Avalara/_AvaTax_ realice en la base de datos.

Para ver los registros haga clic en **Mostrar registros** a la derecha del
botón **Empezar a registrar por 30 minutos**. Esto mostrará una lista
detallada de acciones Avalara/_AvaTax_. Puede organizar esta lista por las
siguientes columnas:

  * **Creado el** : hora del cálculo de _AvaTax_.

  * **Creado por** : valor numérico del usuario en la base de datos.

  * **Nombre de la base de datos** : nombre de la base de datos.

  * **Tipo** : en este campo tendrá la opción de seleccionar dos valores **Servidor** o **Cliente**.

  * **Nombre** : el nombre del servicio de Avalara. En este caso sería _AvaTax_.

  * **Nivel** : por defecto será `INFO`.

  * **Ruta** : indica la ruta que se utiliza para realizar el cálculo.

  * **Línea** : indica en qué línea se realizó el cálculo.

  * **Función** : indica el cálculo que se realizó en la línea.

![La página de inicio de sesión de Avalara con la hilera superior de la lista
resaltada.](../../../../../_images/logging.png)

Haga clic en la línea de registro para mostrar otro campo llamado **Mensaje**.

En este campo verá una transcripción sin editar de la transacción, que
involucra la creación (o ajuste) de la factura de ventas usando el API de
_AvaTax_ de Avalara.

La transacción incluirá detalles como direcciones de envío del remitente y el
destinatario, líneas en las que se describirán los productos o servicios,
códigos de impuestos, cantidades de impuestos y otra información relevante.

El **Mensaje** contiene los impuestos calculados para diferentes
jurisdicciones y confirma la creación (o el ajuste) de la transacción.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede crear campos personalizados con la aplicación <em>Studio</em> de Konvergo ERP. Haga clic en el menú <i class="fa fa-ellipsis-v"></i> <b>(puntos suspensivos)</b> a la derecha de la columna de encabezado y haga clic en <i class="fa fa-plus"></i> <b>Agregar campo personalizado</b>. Esta acción hará que se abra <em>Studio</em>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La aplicación <em>Studio</em> requiere un plan de cobro <em>personalizado</em>. Consulte al  gerente de la cuenta de la base de datos para obtener más información sobre cambiar su plan, o para saber si <em>Studio</em> viene incluida con el plan actual de la base de datos. Vea esta documentación: <a href="../../../../studio">Studio</a>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../avatax">Integración con AvaTax</a></p></li>
<li><p><a href="avalara_portal">Portal de Avalara (AvaTax)</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1">Cumplimiento fiscal en Estados Unidos: video de eLearning sobre AvaTax</a></p></li>
<li><p><a href="../fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p></li>
</ul>
</div>

