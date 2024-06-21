# Mollie

[Mollie](https://www.mollie.com/) es una plataforma de pagos establecida en
los Países Bajos.

## Configuración

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
</ul>
</div>

### Pestaña de credenciales

Konvergo ERP necesita sus **credenciales API** para conectarse a su cuenta de Mollie,
que comprenden:

  * **Calve API** : La clave API de prueba o en vivo dependiendo de la configuración del proveedor.

Puede copiar las credenciales de su cuenta de Mollie y pegarlas en los campos
relacionados en la pestaña de **Credenciales**.

Para obtener sus claves API, inice sesión en su cuenta de Mollie, vaya a
Desarrolladores ‣ Clave API, y copie su **clave API** de prueba o real.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está probando Mollie, con la clave API de prueba, cambie el <b>Estado</b> a <em>Modo de prueba</em>. Le recomendamos hacer esto en una base de datos de prueba en lugar de su base de datos principal.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

