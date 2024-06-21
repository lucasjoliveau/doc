# Plantillas de cotización

En _Ventas_ de Konvergo ERP, los vendedores pueden crear plantillas que pueden volver
a usar para productos en común o servicios que ofrece el negocio.

Al usar estas plantillas, las cotizaciones se pueden hacer y enviar mucho más
rápido a los clientes sin tener que crear cotizaciones nuevas desde cero cada
vez que se realiza una negocioación de ventas.

## Configuración

Primero, active estos ajustes en Ventas ‣ Configuración ‣ Ajustes y baje a la
sección de **Cotizaciones y órdenes**.

En esa sección, marque la casilla junto a la opción **Plantillas de
cotización**. Aparecerá un nuevo campo con el nombre **Plantilla
predeterminada** en el que podrá elegir una plantilla de cotización
predeterminada desde el menú desplegable.

![Cómo habilitar las plantillas de cotización en la aplicación Ventas de
Konvergo ERP.](../../../../_images/quotations-templates-setting.png)

También, al activar la función de **Plantilla de cotización** , aparecerá un
enlace interno de **➡️ Plantillas de cotización** debajo del campo **Plantilla
predeterminada**.

Al hacer clic en el enlace, aparecerá una página de **Plantillas de
cotización** desde donde podrá crear, ver y editar plantillas.

Antes de salir de la página de **Ajustes** , no olvide hacer clic en el botón
**Guardar** para guardar todos los cambios que realizó durante la sesión.

## Crear plantillas de cotización

Haga clic en el enlace de **Plantillas de cotización** en la página de
**Ajustes** o vaya a la Aplicación Ventas ‣ Configuración ‣ Plantillas de
cotización. Ambas opciones mostrarán la página de las **Plantillas de
cotización** donde podrá crear, ver y editar las plantillas de cotización.

![Página de plantillas de cotización en la aplicación Ventas de
Konvergo ERP.](../../../../_images/quotation-templates-page.png)

Para crear una nueva plantilla de cotización, haga clic en el botón **Nuevo**
ubicado en la esquina superior izquierda. Al hacerlo, aparecerá un formulario
en blanco de la plantilla de cotización que puede personalizar de muchas
maneras.

![Cree una nueva plantilla de cotización en Ventas de Konvergo ERP.
](../../../../_images/blank-quotation-form.png)

Comience escribiendo un nombre para la plantilla en el campo **Plantilla de
cotización**.

Luego, en el campo **La cotización vence después de** , escriba por cuántos
días será válida la plantilla, o puede dejar el campo con su valor
predeterminado de `0` para mantener su validez de manera indefinida.

Si las funciones **Firma electrónica** y/o **Pago en línea** están activadas
en los **Ajustes** (Ventas ‣ Configuración ‣ Ajustes), estas opciones estarán
disponibles en el campo **Confirmación en línea**.

En el campo **Confirmación en línea** , seleccione la casilla junto a
**Firma** para solicitar una firma electrónica del cliente para confirmar una
orden. Seleccione la casilla junto a **Pago** para solicitar un pago en línea
del cliente para confirmar una orden.

Ambas opciones se pueden activar de manera simultánea, en cuyo caso, el
cliente debe proporcionar una firma **y** un pago para confirmar una orden.

Luego, en el campo **Correo electrónico de confirmación** , haga clic en el
campo en blanco para que aparezca un menú desplegable. Desde ahí, seleccione
una plantilla de correo electrónico ya configurada para enviarla a los
clientes al confirmar una orden.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para crear una nueva plantilla de correo electrónico directamente desde el campo <b>Correo electrónico de confirmación</b>, comience a escribir el nombre de la nueva plantilla de correo electrónico en el campo y seleccione: <b>Crear</b> o <b>Crear y editar…</b> del menú desplegable que aparece.</p>
<p>Al seleccionar la opción <b>Crear</b>, se crea la plantilla de correo electrónico, la cual podrá editar después. Al seleccionar <b>Crear y editar…</b> se crea la plantilla de correo electrónico y aparece una ventana emergente para <b>Crear un correo electrónico de confirmación</b>, en donde podrá personalizar y configurar la plantilla de correo de manera inmediata.</p>
<img alt="Ventana emergente para crear un correo electrónico de confirmación desde la plantilla de la cotización en Ventas de Konvergo ERP." class="align-center" src="../../../../_images/create-confirmation-mail-popup.png"/>
<p>Una vez que haya realizado todas las modificaciones necesarias, haga clic en <b>Guardar y cerrar</b> para almacenar la plantilla de correo electrónico y regresar al formulario de cotización.</p>
</div>

Si trabaja en un ambiente multiempresa, utilice el campo **Empresa** para
asignar la empresa a la cual aplicará está plantilla de cotización.

En el campo **Recurrencia** , podrá elegir de una variedad de cantidades de
tiempo ya configuradas (por ejemplo, **Mensual** , **Trimestral**) para
asignar qué tan seguido debe ocurrir esa plantilla de cotización.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El campo <b>Recurrenncia</b> <b>solo</b> aplica a los planes de suscripción. Para obtener más información, consulte la documentación en <a href="../../subscriptions/plans">Planes de suscripción</a>.</p>
</div>

### Pestaña de líneas

En la pestaña **Líneas** , puede agregar los productos a la plantilla de
cotización al hacer clic en **Agregar un producto** , organizarlos al hacer
clic en `Agregar sección` (y puede arrastrar/soltar los encabezados de las
secciones), y puede agregar mas información discrecional (como detalles de
garantía, términos, etc.) al hacer clic en **Agregar una nota**.

![Pestaña de líneas completada en un formulario de plantilla de cotización en
Ventas de Konvergo ERP.](../../../../_images/lines-tab-quotation-template.png)

Haga clic en **Agregar un producto** en la pestaña **Líneas** de un formulario
de plantilla de cotización para agregar uno a la plantilla de cotización. Al
hacerlo, aparecerá un campo vacío en la columna **Producto**.

Si hace clic ahí, aparecerá un menú desplegable con todos los productos
disponibles en la base de datos. Seleccione los productos que desee desde ese
menú para agregarlos a la plantilla de cotización.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si el producto que desea no está visible, escriba el nombre del producto en el campo <b>Producto</b> y la opción aparecerá en la lista desplegable. También puede encontrar los productos si hace clic en <b>Buscar más…</b> en el menú desplegable.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Al agregar un producto, la <b>cantidad</b> predeterminada es <code>1</code>, pero puede editarlo cuando quiera.</p>
</div>

Luego, arrastre y suelte el producto a dónde desee mediante el icono de **seis
cuadros** que se ubica del lado izquierdo de cada línea de artículo.

Para agregar una _sección_ , que funcione como un encabezado para organizar
las líneas de la orden de ventas, haga clic en **Agregar sección** en la
pestaña **Líneas**. Al hacerlo, aparecerá un campo en blanco, en donde podrá
escribir el nombre que quiera para la sección. Luego, haga clic en otra parte
para asegurar el nombre de la sección.

Luego, arrastre y suelte el producto a dónde desee mediante el icono de **seis
cuadros** que se ubica del lado izquierdo de cada línea de artículo.

Para agregar una nota, la cual aparecerá como un texto en la cotización del
cliente, haga clic en **Agregar una nota** en la pestaña **Líneas**. Al
hacerlo, aparecerá un campo en blanco, en donde podrá escribir la nota que
quiera. Luego, haga clic en otra parte para asegurar la nota.

Luego, arrastre y suelte la nota al lugar que quiera mediante el icono **seis
cuadros**.

Para eliminar cualquier línea de artículo desde la pestaña **Líneas**
(producto, sección, y/o nota), haga clic en el icono **🗑️ (papelera)** que se
ubica del lado derecho de la línea.

### Pestaña de productos opcionales

Usar _productos opcionales_ es una estrategia de marketing que implica la
venta cruzada de productos junto con un producto principal. El objetivo es
ofrecer productos útiles y relacionados a los clientes, lo que puede resultar
en un aumento de ventas.

Por ejemplo, si un cliente desea comprar un automóvil tiene la opción de
ordenar asientos con función de masaje o puede ignorar la oferta y solo
comprar el vehículo. La experiencia del cliente mejora si le proporciona la
opción de comprar productos opcionales.

Los productos opcionales aparecen como una sección al final de las órdenes de
ventas y de las página de comercio electrónico. Los clientes pueden agregarlos
ellos mismos de manera inmediata a sus órdenes de ventas en línea.

![Los productos opcionales en una orden de ventas típica en Ventas de
Konvergo ERP.](../../../../_images/optional-products-on-sales-order.png)

En la pestaña **Productos opcionales** , puede **Agregar una línea** para cada
producto de venta cruzada relacionado a los artículos principales en la
pestaña **Líneas** , si aplica. Es ideal que los productos que se agregan aquí
sean un complemento de la oferta original como un valor agregado para el
comprador potencial.

![Pestaña de productos opcionales completada en una plantilla de cotización en
Ventas de Konvergo ERP.](../../../../_images/optional-products-tab-quotation-
template1.png)

Al hacer clic en **Agregar una línea** muestra un campo en blanco en la
columna **Producto**.

Si hace clic sobre el campo, aparecerá una lista desplegable con productos de
la base de datos y podrá seleccionar el que desee para agregarlo como un
producto opcional a la plantilla de la cotización.

Para eliminar cualquier línea de artículo desde la pestaña **Productos
opcionales** , haga clic en el icono **🗑️ (papelera)**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los productos opcionales <b>no</b> son obligatorios para crear una plantilla de cotización</p>
</div>

### Pestaña de términos y condiciones

La pestaña **Términos y condiciones** le da la oportunidad para agregar
términos y condiciones a la plantilla de la cotización. Para agregarlos, solo
debe escribir (o copiar y pegar) los términos y condiciones deseadas en esta
pestaña.

![La pestaña de términos y condiciones en un formulario de la plantilla de una
cotización en Ventas de Konvergo ERP.](../../../../_images/terms-and-conditions-
tab.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../finance/accounting/customer_invoices/terms_conditions">Términos y condiciones predeterminados</a></p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Términos y condiciones <b>no</b> son obligatorios para crear una plantilla de cotización.</p>
</div>

## Diseñar plantillas de cotización

En la esquina superior izquierda del formulario de la plantilla de una
cotización, hay un botón para **Diseñar una plantilla**.

![Botón para diseñar una plantilla en la esquina superior izquierda del
formulario de la plantilla de una cotización.](../../../../_images/design-
template-button.png)

Al hacer clic sobre él, Konvergo ERP mostrará una vista previa de la plantilla de la
cotización a través de la aplicación _Sitio Web_ de Konvergo ERP, y aparecerá en el
frontend del sitio web del cliente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta función <b>solo</b> estará disponible si tiene instalada la aplicación <em>Sitio web</em>.</p>
</div>

Konvergo ERP utiliza varios bloques azules de marcador de posición para resaltar dónde
aparecen ciertos elementos y lo que contienen (por ejemplo, **Encabezado de la
plantilla** , **Producto**).

Para editar el contenido, la apariencia y el diseño general de la plantilla de
la cotización mediante la aplicación _Sitio web_ , haga clic en el botón
**Editar** que se ubica en la esquina superior derecha.

![Botón de editar en la esquina superior derecha de la página para diseñar una
plantilla de cotización.](../../../../_images/design-template-edit-button.png)

Al hacer clic en **Editar** , Konvergo ERP aparecerá una barra lateral llena de varios
elementos de diseño y bloques de creación. Puede arrastrar y soltar estos
bloques en el lugar que desee del diseño de la plantilla de una cotización.

![Barra lateral con bloques de creación para el diseño de la plantilla de una
cotización en Sitio web de Konvergo ERP.](../../../../_images/design-quotation-
building-blocks.png)

Después de soltar un bloque en la posición que desee, lo puede personalizar y
configurar para que se ajuste a cualquier necesidad, diseño o estilo único.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El diseño de las plantillas de cotización usa la misma metodología y funcionalidad con los bloques de creación que una página web típica de <em>Sitio web</em> de Konvergo ERP. Para obtener más información, asegúrese de consultar la documentación sobre <a href="../../../websites/website">Sitio web</a>.</p>
</div>

Cuando la personalización y los bloques estén completos, haga clic en
**Guardar** para aplicar todos los cambios.

También aparecerá un panel azul en la parte superior del diseño de la
plantilla de cotización con un enlace para regresar rápidamente al **Modo
editar**. Al hacer clic sobre él, Konvergo ERP regresa al formulario de la plantilla
de cotización en el backend de la aplicación _Ventas_.

## Usar plantillas de cotización

Al crear una cotización (Aplicación Ventas ‣ Crear), seleccione una plantilla
preconfigurada en el menú desplegable del campo **Plantilla de cotización**.

![El campo de vencimiento en una cotización estándar en Ventas de Konvergo ERP.
](../../../../_images/quotation-templates-field.png)

Para ver lo que el cliente verá, haga clic en el botón inteligente de **Vista
previa** que se ubica en la parte superior de la página para ver el aspecto
que tendría la cotización desde el frontend del sitio web mediante el portal
del cliente de Konvergo ERP.

![VIsta previa del cliente de una plantilla de cotización en Ventas de
Konvergo ERP.](../../../../_images/quotations-templates-preview.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="get_signature_to_validate">Firmas electrónicas para la confirmación de órdenes.</a></p></li>
<li><p><a href="get_paid_to_validate">Confirmación de orden de pago en línea</a></p></li>
</ul>
</div>

