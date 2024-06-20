# Alipay

[Alipay](https://www.alipay.com/) es una plataforma de pago en línea
establecida en China por Alibaba Group.

Advertencia

El proveedor Alipay es obsoleto. En su lugar, se recomienda usar
[AsiaPay](asiapay.html)

## Configuración

Ver también

  * [Activar un proveedor de pago](../payment_providers.html#payment-providers-add-new)

### Pestaña de credenciales

Odoo necesita sus **credenciales API** para conectarse a su cuenta de Alipay,
que comprenden:

  * **Cuenta** : según su ubicación: `Pago exprés` si es un comerciante chino. `Transfronterizo` si no lo es.

  * **Correo electrónico de vendedor de Alipay** : su correo electrónico público de partner de Alipay (solo para pago exprés).

  * **ID de partner comerciante** : el ID público de partner que se utiliza solo para identificar la cuenta con Alipay.

  * **Clave de firma MD5** : La clave de firma.

Puede copiar las credenciales de su cuenta de Alipay y pegarlas en los campos
relacionados en la pestaña de **Credenciales**.

Para obtenerlas, inicie sesión en su cuenta de Alipay, se encuentran en la
página principal.

Importante

Si está probando Alipay, en el _sandbox_ , cambie el **Estado** a _Modo de
prueba_. Le recomendamos hacer esto en una base de datos de prueba en lugar de
su base de datos principal.

Ver también

  * [Pagos en línea](../payment_providers.html)

