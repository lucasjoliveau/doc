# Servicios de pago de Amazon

[Servicios de pago de Amazon](https://paymentservices.amazon.com/) (APS, por
sus siglas en inglés) es un proveedor de pagos en línea establecido en Dubai y
que ofrece varias opciones de pago en línea.

## Configuración en el tablero de APS

  1. Inicie sesión en su [Tablero de Servicios de pago de Amazon](https://fort.payfort.com/) y vaya a Configuración de integración ‣ Configuración de seguridad. Genere el **Código de acceso** si todavía no se genera uno. Copie los valores de los campos **Identificador de comerciante** , **Código de acceso** , **Requerimento de frase SHA** y **Frase de respuesta SHA** y guárdelos para después.

  2. Ingrese la URL de la base de datos de Konvergo ERP en **URL de origen** , por ejemplo,: `https://yourcompany.odoo.com/`. Luego, haga click en **Guardar cambios**.

  3. Vaya a Configuración de integración ‣ Configuraciones técnicas y haga clic en **Redirigir**. Asegúrese de que el **Estado** este establecido en `Activo` y seleccione sus métodos de pago preferidos en **Opciones de pago**.

  4. Establezca **Enviar parámetros de respuesta** a **Sí** e ingrese la URL de su base de datos seguido de `/payment/aps/return` en **Redirigir URL**.

Por ejemplo, `https://yourcompany.odoo.com/payment/aps/return`.

Ingrese la URL de su base de datos seguido de `/payment/aps/webhook` en los
campos de **Retroalimentación de transacción directa** y **Notificación de
URL**.

Por ejemplo, `https://yourcompany.odoo.com/payment/aps/webhook`.

Haga clic en **Guardar cambios**.

  5. En Configuración de integración ‣ Plantilla de página de pago puede personalizar la estética de la página de pagos de los Servicios de pago de Amazon (donde los clientes pueden ingresar los detalles de sus tarjetas de crédito durante el pago).

## Configuración en Konvergo ERP

  1. [Vaya al proveedor de pago Servicios de pago de Amazon](../payment_providers#payment-providers-add-new), cambie su estado a **Activado** y asegúrese de que esté **Publicado**.

  2. En la pestaña de **Credenciales** , llene los campos **Identificador del comerciante** , **Código de acceso** , **Frase de requerimento SHA** y **Frase de respuesta SHA** con los valores que guardo en el paso Configuración en el tablero de APS.

  3. Configure el resto de las opciones como guste.

