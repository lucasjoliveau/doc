# SIPS

[SIPS](https://sips.worldline.com/) es un proveedor de soluciones de pagos en
línea de la multinacional Worldline.

## Configuración

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
</ul>
</div>

### Pestaña de credenciales

Konvergo ERP necesita sus **Credenciales API** para conectarse con su cuenta de SIPS,
que incluye:

  * **ID de comerciante** : Este ID solo se utiliza para identificar la cuenta del comerciante con SIPS.

  * **Clave secreta** : La clave para entrar a la cuenta del comerciante con SIPS.

  * **Versión de la clave secreta** : La versión de la clave, llenada previamente.

  * **Versión de la interfaz** : Llenada previamente, no la cambie.

Puede copiar sus credenciales desde la información de la documentación de su
entorno SIPS, en la sección **PROD** y pegarlas en los campos correspondientes
en la pestaña **Credenciales**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está utilizando SIPS en modo prueba, con las credenciales de <em>PRUEBA</em>, cambie el <b>Estado</b> a <b>Modo de prueba</b>. Le recomendamos que lo haga en una base de datos de prueba de Konvergo ERP, en vez de hacerlo en su base de datos principal.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

