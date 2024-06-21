# Firmas electrónicas para la confirmación de órdenes.

La aplicación **Ventas** de Konvergo ERP permite que los clientes confirmen sus
órdenes con una firma electrónica desde la orden de venta. Una vez que el
cliente firma de manera electrónica la orden de venta, el vendedor asignado a
la orden recibe una notificación al instante sobre la confirmación de esa
orden de venta.

## Activar firmas electrónicas

La función _Firma en línea_ **debe** estar habilitada para que los clientes
puedan confirmar sus órdenes mediante una firma en línea.

Para activar la función de _Firma en línea_ , vaya a aplicación Ventas ‣
Configuración ‣ Ajustes, baje hasta la sección de **Cotizaciones y órdenes** y
active la función de **Firma en línea** haciendo clic en la casilla de a lado.

![La opción de la función de firma en línea en los ajustes de la aplicación
Ventas de Konvergo ERP.](../../../../_images/signature-setting.png)

Luego, haga clic en **Guardar** que se ubica en la parte superior izquierda.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Al hacer una plantilla de cotización, la función de firma en línea es la opción de <b>Firma</b> que se ubica en el campo <b>confirmación en línea</b> del formulario de la plantilla de cotización.</p>
<img alt="La opción de firma de confirmación en línea que se encuentra en cada plantilla de cotización de Konvergo ERP. " class="align-center" src="../../../../_images/signature-feature-quotation-template.png"/>
<p>En plantillas de cotización estándar, la función de firma en línea es la opción <b>Firma</b> que se ubica en la pestaña  <b>Otra información</b> en el formulario de la cotización.</p>
<img alt="La opción firma de confirmación en línea en la pestaña Otra información en un formulario de cotización en Konvergo ERP. " class="align-center" src="../../../../_images/signature-other-info-tab.png"/>
</div>

## Confirmaciones de órdenes con firmas en línea

Cuando un cliente accede a una cotización en línea a través de su portal de
cliente, podrá ver un botón para **Firmar y pagar** directamente en la
cotización.

![El botón Firmar y pagar presente en las cotizaciones en línea de Ventas de
Konvergo ERP. ](../../../../_images/sign-and-pay-button.png)

Al hacer clic sobre él, aparecerá una ventana emergente para **Validar la
orden**. El campo **Nombre completo** se completa de manera automática según
la información de contacto en la base de datos.

![La ventana emergente de Validar la orden para firmas en línea en Ventas de
Konvergo ERP.](../../../../_images/validate-order-popup.png)

Después, los clientes tienen la opción de firmar en línea con cualquiera de
las siguientes opciones: **Automático** , **Dibujar** , o **Subir**.

**Automático** permite que Konvergo ERP genere de manera automática una firma
electrónica según la información que aparece en el campo **Nombre completo**.
**Dibujar** le permite al cliente usar el cursor para crear una firma
personalizada directamente desde la ventana emergente. **Subir** deja que el
cliente suba un archivo de una firma ya creada desde su computadora.

Después de que el cliente haya elegido una de las tres opciones anteriores
para firmar (**Automático** , **Dibujar** , o **Subir**), deberán hacer clic
en **Aceptar y firmar**.

Al hacerlo, aparecerán los diferentes métodos de pago disponibles de entre los
que podrán elegir el que prefieran (solo si la opción _pago en línea_ aplica
para esta cotización).

Cuando la cotización esté pagada y confirmada, se creará de manera automática
una orden de envío (si está instalada la aplicación _Inventario_ de Konvergo ERP).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="quote_template">Plantillas de cotización</a></p></li>
<li><p><a href="get_paid_to_validate">Confirmación de orden de pago en línea</a></p></li>
</ul>
</div>

