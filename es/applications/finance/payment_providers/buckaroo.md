# Buckaroo

[Buckaroo](https://www.buckaroo.eu/) es una empresa neerlandesa que ofrece
varias posibilidades de pago en línea.

## Configuración en Buckaroo Plaza

  1. Inicie sesión en [Buckaroo Plaza](https://plaza.buckaroo.nl), vaya a Mi Buckaroo ‣ Sitios web y seleccione la pestaña **Configuraciones push**.

  2. Seleccione la casilla **Permitir la respuesta push** en la sección **Respuestas atrasadas y push**.

  3. Ingrese la URL de su base de datos de Konvergo ERP, seguido de `/payment/buckaroo/webhook` en los campos de texto **Hacer push en URI de éxito/pendiente** y en **Hacer push en el fallo URI**. Por ejemplo: `https://yourcompany.odoo.com/payment/buckaroo/webhook`.

  4. Deje los demás campos como están y haga clic en **Guardar**.

  5. En la pestaña de **General** , copie la **Clave** (la clave que se usa únicamente para identificar su sitio web con Buckaroo) de su sitio web y guárdela para después.

  6. Vaya a Configuración ‣ Seguridad ‣ Clave secreta, ingrese o **Genere** una **Clave secreta** y haga clic en **Guiardar**. Guarde la clave para después.

## Configuración en Konvergo ERP

  1. [Vaya al proveedor de pago Buckaroo](../payment_providers#payment-providers-add-new) y cambie su estado a **Habilitado**.

  2. En la pestaña **Credenciales** , llene los campos **Clave del sitio web** y **Clave secreta** con los valores que guardo en el paso Configuración en Buckaroo Plaza.

  3. Configure el resto de las opciones como guste.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payment_providers">Pagos en línea</a></p>
</div>

