# AsiaPay

[AsiaPay](https://www.asiapay.com/) es un proveedor de pago en línea
establecido en Hong Kong y cubre varios países asiáticos y métodos de pago.

## Configuración en el tablero de AsiaPay

  1. Inicie sesión en el [Tablero de AsiaPay](https://www.paydollar.com/b2c2/eng/merchant/index.jsp) y vaya a Perfil ‣ Información de contabilidad. Copie los valores de los campos Divisa y Asegurar Hash y guárdelos para después.

  2. Vaya a Perfil ‣ Configuración de pago de la cuenta y active las opciones Enlace del valor de retorno (Datefeed)

Ingrese la URL de su base de datos de Odoo seguido de
`/payment/asiapay/webhook` en el campo de texto Enlace del valor de retorno
(Datefeed).

Por ejemplo: `https://yourcompany.odoo.com/payment/asiapay/webhook`.

Haga clic en Probar para comprobar que el webhook está funcionando
correctamente.

  3. Haga clic en Actualizar para finalizar con la configuración.

## Configuración en Odoo

  1. [Vaya al proveedor de pago AsiaPay](../payment_providers.html#payment-providers-add-new) y cambie su estado a Habilitado.

  2. En la pestaña de Credenciales , llene los campos ID del comerciante, Divisa y Hash secreto seguro con los valores que guardo en el paso Configuración en el tablero de AsiaPay.

De manera predeterminada, el proveedor de pago AsiaPay está configurado para
verificar el hash secreto con la función hash `SHA1`. Si una función diferente
está establecida en su cuenta, active el [modo
desarrollador](../../general/developer_mode.html#developer-mode) y establezca
el mismo valor en el campo Función hash segura en Odoo.

  3. Configure el resto de las opciones como guste.

Ver también

  * [Pagos en línea](../payment_providers.html)

