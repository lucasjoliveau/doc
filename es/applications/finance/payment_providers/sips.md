# SIPS

[SIPS](https://sips.worldline.com/) es un proveedor de soluciones de pagos en
línea de la multinacional Worldline.

## Configuración

Ver también

  * [Activar un proveedor de pago](../payment_providers.html#payment-providers-add-new)

### Pestaña de credenciales

Odoo necesita sus **Credenciales API** para conectarse con su cuenta de SIPS,
que incluye:

  * **ID de comerciante** : Este ID solo se utiliza para identificar la cuenta del comerciante con SIPS.

  * **Clave secreta** : La clave para entrar a la cuenta del comerciante con SIPS.

  * **Versión de la clave secreta** : La versión de la clave, llenada previamente.

  * **Versión de la interfaz** : Llenada previamente, no la cambie.

Puede copiar sus credenciales desde la información de la documentación de su
entorno SIPS, en la sección **PROD** y pegarlas en los campos correspondientes
en la pestaña **Credenciales**.

Importante

Si está utilizando SIPS en modo prueba, con las credenciales de _PRUEBA_ ,
cambie el **Estado** a **Modo de prueba**. Le recomendamos que lo haga en una
base de datos de prueba de Odoo, en vez de hacerlo en su base de datos
principal.

Ver también

  * [Pagos en línea](../payment_providers.html)

