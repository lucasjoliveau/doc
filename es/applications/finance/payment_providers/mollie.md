# Mollie

[Mollie](https://www.mollie.com/) es una plataforma de pagos establecida en
los Países Bajos.

## Configuración

Ver también

  * [Activar un proveedor de pago](../payment_providers.html#payment-providers-add-new)

### Pestaña de credenciales

Odoo necesita sus **credenciales API** para conectarse a su cuenta de Mollie,
que comprenden:

  * **Calve API** : La clave API de prueba o en vivo dependiendo de la configuración del proveedor.

Puede copiar las credenciales de su cuenta de Mollie y pegarlas en los campos
relacionados en la pestaña de **Credenciales**.

Para obtener sus claves API, inice sesión en su cuenta de Mollie, vaya a
Desarrolladores ‣ Clave API, y copie su **clave API** de prueba o real.

Importante

Si está probando Mollie, con la clave API de prueba, cambie el **Estado** a
_Modo de prueba_. Le recomendamos hacer esto en una base de datos de prueba en
lugar de su base de datos principal.

Ver también

  * [Pagos en línea](../payment_providers.html)

