# Transferencias bancarias

El método de pago **Transferencia electrónica** le permite proporcionar
instrucciones de pago a sus clientes, así como los detalles bancarios y
comunicación. Se muestran de la siguiente manera:

  * al final del proceso de pago, una vez que el cliente seleccionó **Transferencia electrónica** como método de pago e hizo clic en el botón de **Pagar ahora** :

![Instrucciones de pago al final del
proceso](../../../_images/payment_instructions_checkout.png)

  * en el portal del cliente:

![Instrucciones de pago en el portal del
cliente](../../../_images/payment_instructions_portal.png)

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si bien, este método es muy accesible y requiere una configuración mínima, es muy ineficiente en cuanto al proceso. En su lugar, le recomendamos un <a href="../payment_providers">proveedor de pago</a>.</p></li>
<li><p>Las órdenes en línea se quedan en la etapa de <b>Cotización enviada</b> (es decir, orden no pagada) hasta que reciba el pago y  <b>Confirme</b> la orden.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Las <b>Transferencias electrónicas</b> se pueden usar como plantillas para otros métodos de pago que se procesan manualmente, como los cheques, al renombrarlos o duplicarlos.</p>
</div>

## Configuración

Para configurar las **Transferencias electrónicas** , vaya a Contabilidad /
Sitio web ‣ Configuración ‣ Proveedores de pago y abra la tarjeta de
**Transferencia electrónica**. Luego, en la pestaña de **Configuración** :

  * Seleccione la **Comunicación** que usará:

    * **Con base en la Referencia de los Documentos** : órdenes de venta o el número de factura

    * **Con base en el ID del cliente** : identificador del cliente

  * Seleccione la casilla **Permitir códigos QR** para activar los [pagos con código QR](../accounting/customer_invoices/epc_qr_code).

Defina las instrucciones de pago en la pestaña **Mensajes** :

![Defina las instrucciones de pago](../../../_images/payment_instructions.png)

Si ya tiene definida una [cuenta bancaria](../accounting/bank), el número
de cuenta se agregará de manera automática al mensaje predeterminado que
genera Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payment_providers#payment-providers-journal"><span class="std std-ref">Diario de pagos</span></a></p>
</div>

