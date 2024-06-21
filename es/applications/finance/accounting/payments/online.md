# Pagos en línea

  * Instale el parche para desactivar el pago de factura en línea
    * [Actualizar Konvergo ERP a la versión más reciente](online/install_portal_patch#update-odoo-to-the-latest-release)
    * [Actualizar la lista de módulos disponibles](online/install_portal_patch#update-the-list-of-available-modules)
    * [Instalación del módulo Parche de pago de factura en línea](online/install_portal_patch#install-the-module-invoice-online-payment-patch)

Para que sus clientes puedan pagar las facturas emitidas con mayor facilidad,
puede activar la función **Pago de facturas en línea** , la cual añade el
botón _Pagar ahora_ en el **Portal del cliente**. De este modo, sus clientes
pueden ver sus facturas y pagar en línea con su método de pago favorito, lo
cual facilita el proceso de pago.

![Elegir proveedores de pago después de hacer clic en "Pagar
ahora"](../../../../_images/online-payment-providers.png)

## Configuración

Asegúrese de que [configuró bien los proveedores de
pago](../../payment_providers).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>De forma predeterminada, la «<a href="../../payment_providers/wire_transfer">transferencia bancaria</a>» es el único proveedor de pago activado, pero de igual manera debe completar los detalles de pago.</p>
</div>

Para activar el pago en línea de facturas, vaya a Contabilidad ‣ Configuración
‣ Ajustes ‣ Pagos de clientes, active ** Pago de factura en línea **, y haga
clic en _Guardar_.

## Portal del cliente

Después de emitir la factura, haga clic en _Enviar e imprimir_ y envíe la
factura por correo electrónico al cliente. Este recibirá un correo electrónico
con un enlace que le redirigirá a la factura en su **Portal del Cliente**.

![Correo electrónico con un enlace para ver la factura en línea dentro del
portal del cliente.](../../../../_images/view-invoice.png)

Los clientes pueden elegir qué método de pago utilizar después de hacer clic
en **Pagar ahora**.

![El botón "Pagar ahora" en una factura en el portal del
cliente.](../../../../_images/pay-now.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

