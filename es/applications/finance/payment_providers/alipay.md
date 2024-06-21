# Alipay

[Alipay](https://www.alipay.com/) es una plataforma de pago en línea
establecida en China por Alibaba Group.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El proveedor Alipay es obsoleto. En su lugar, se recomienda usar <a href="asiapay">AsiaPay</a></p>
</div>

## Configuración

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
</ul>
</div>

### Pestaña de credenciales

Konvergo ERP necesita sus **credenciales API** para conectarse a su cuenta de Alipay,
que comprenden:

  * **Cuenta** : según su ubicación: `Pago exprés` si es un comerciante chino. `Transfronterizo` si no lo es.

  * **Correo electrónico de vendedor de Alipay** : su correo electrónico público de partner de Alipay (solo para pago exprés).

  * **ID de partner comerciante** : el ID público de partner que se utiliza solo para identificar la cuenta con Alipay.

  * **Clave de firma MD5** : La clave de firma.

Puede copiar las credenciales de su cuenta de Alipay y pegarlas en los campos
relacionados en la pestaña de **Credenciales**.

Para obtenerlas, inicie sesión en su cuenta de Alipay, se encuentran en la
página principal.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está probando Alipay, en el <em>sandbox</em>, cambie el <b>Estado</b> a <em>Modo de prueba</em>. Le recomendamos hacer esto en una base de datos de prueba en lugar de su base de datos principal.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

