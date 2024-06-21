# Productos de suscripción

Al integrar las aplicaciones _Ventas_ y _Suscricpiones_ de Konvergo ERP, los usuarios
pueden vender productos de suscripción junto con productos normales. Mientras
que los productos normales se venden una vez, los productos de suscripción se
venden por renovación, y así se genera un ingreso recurrente.

En Konvergo ERP, a los productos de suscripción también se les llama productos
_recurrentes_.

## Configurar periodos recurrentes

Para iniciar con las suscripciones, primero asegúrese de que los _periodos
recurrentes_ estén configurados como lo necesite.

Los periodos recurrentes son los periodos de tiempo en los que las
suscripciones se renuevan. Designan cada cuánto el cliente debe pagar por (y
recibir) los productos de suscripción.

Para configurar los periodos recurrentes, vaya a Suscripciones ‣ Configuración
‣ Periodos Recurrentes.

![La página de periodos recurrentes en Suscripciones de
Konvergo ERP.](../../../_images/recurrence-periods-page.png)

La aplicación _Suscripciones_ ya tiene configurados algunos periodos de
recurrencia básicos.

  * **Mensual**

  * **Trimestral**

  * **Semanal**

  * **Cada 2 semanas**

  * **Anual**

  * **Cada 3 años**

  * **Cada 5 años**

Puede agregar nuevos periodos de recurrencia o editarlo en cualquier momento.

Para crear un nuevo periodo de recurrencia, haga clic en **Nuevo** en la
página de **Periodos de recurrencia** , y de esta forma, se abrirá un
formulario en blanco para un periodo de recurrencia.

![Un formulario de periodo de recurrencia en la aplicación Suscripciones de
Konvergo ERP.](../../../_images/recurrence-period-form.png)

Luego, escriba el **Nombre** y la **Duración** del periodo de recurrencia y
seleccione la **Unidad** que definirá la duración.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p><em>No</em> podrá usar la unidad de <b>Días</b> como un periodo de recurrencia en las suscripciones, pues este tipo de recurrencia está hecha para los alquileres y <b>no</b> se puede agregar a las órdenes de ventas de suscripciones recurrentes.</p>
<p>Esta limitación existe para evitar que las órdenes de ventar generen facturas diarias.</p>
</div>

## Configuración del formulario del producto

Para crear un nuevo producto de suscripción vaya a Suscripciones ‣ Productos ‣
Productos y haga clic en **Nuevo**.

Aparecerá un formulario de producto en blanco que podrá configurar y
personalizar de varias formas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El nuevo producto tendra automáticamente seleccionada la casilla de <b>Recurrente</b>,. esto le permite a Konvergo ERP reconocerlo como un producto de suscripción. Asegúrese de dejar activadas las opciones <b>Recurrente</b> y <b>Se puede vender</b>.</p>
<p>El campo <b>Tipo de producto</b> está configurado como <b>Servicio</b> de forma predeterminada, pero <em>puede</em> configurar los productos de suscripción con otros tipos en caso de que sea necesario.</p>
</div> ![Un formulario de un producto de suscripción básico en
Suscripciones de Konvergo ERP.](../../../_images/subscription-product-form.png)

### Precio basado en tiempo

Una vez que haya completado los campos que desee en la pestaña **Información
general** , haga clic en la pestaña **Precio según el tiempo**.

![Pestaña tiempo según el precio en un formulario de un producto de
suscripción en Suscripciones de Konvergo ERP. ](../../../_images/time-based-pricing-
tab.png)

Desde aquí, haga clic en **Agregar un precio** para empezar a definir los
precios recurrentes.

En la columna **Periodo** , seleccione el periodo de recurrencia que desee. Si
lo requiere, puede seleccionar una lista de precios en la columna **Lista de
precios**. Luego, en la columna **Precio** , escriba el precio para ese
periodo recurrente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los periodos <b>Diario</b> y <b>Por hora</b> no se pueden usar en los productos recurrentes.</p>
<img alt="La ventana emergente de error de validación que aparece en Suscripciones de Konvergo ERP." class="align-center" src="../../../_images/validation-error-popup.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><em>No hay límite</em> para las líneas que puede agregar a la tabla de <b>Precio según el tiempo</b>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Un producto existente se puede convertir a producto de suscripción si lo marca como <b>Recurrente</b> y lo configura con <b>Precio basado en tiempo</b> en el formulario del producto.</p>
</div>

#### Listas de precios

[Listas de precio](../sales/products_prices/prices/pricing) can be used
with subscription products to give special pricing to customers included in
pricelists.

Esto se puede configurar en la pestaña **Precio según el tiempo** en el
formulario del producto, o en el formulario de la lista de precios en la
aplicación _Ventas_.

Para crear reglas de precio recurrentes para listas de precios específicas en
la pestaña **Precio basado en tiempo** del formulario de producto, seleccione
una lista de precios en la columna **Listas de precios**.

![Listas de precios en la pestaña "Precios basados en tiempo".
](../../../_images/pricelist-time-based-pricing.png)

Cuando las lista de precios se agregan a la pestaña **Precios basados en
tiempo** , el formulario de la lista de precios en la aplicación _Ventas_ se
actualiza automáticamente.

Las reglas de los precios según el tiempo también se pueden configurar
directamente en el formulario de la lista de precios.

Para hacerlo, vaya a Ventas ‣ Productos ‣ Listas de precio y seleccione una
lista de precios (o haga clic en **Nuevo** para crear una nueva lista).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede acceder a las listas de precios mediante la aplicación Suscripciones con los mismos del menú.</p>
</div>

Luego, en el formulario de la lista de precios, en la pestaña **Reglas según
el tiempo** , haga clic en **Agregar una línea**.

![La pestaña de reglas según el tiempo en un formulario de lista de precios en
Ventas de Konvergo ERP.](../../../_images/pricelist-form-time-based-rules-tab.png)

Luego, seleccione un producto de suscripción en la columna **Productos** y
seleccione un periodo recurrente en la columna **Periodo**. Introduzca un
**Precio** para ese producto y periodo particulares. Agregue tantas líneas
como lo necesite.

La pestaña **Precios por tiempo** del formulario del producto se actualiza en
automático cuando agrega **reglas por tiempo** al formulario de la lista de
precios.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="ecommerce">Use las suscripciones en la tienda de su comercio electrónico</a></p>
</div>

