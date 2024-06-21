# Alquiler

La aplicación **Alquiler de Konvergo ERP** es una solución exhaustiva para gestionar
sus propiedades.

Desde una única vista, puede enviar cotizaciones, confirmar órdenes, programar
alquileres, registrar cuándo se recolectan y devuelven los productos y
facturar a sus clientes.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/app/rental">Alquiler de Konvergo ERP: página de producto</a></p></li>
<li><p><a href="https://www.odoo.com/slides/rental-48">Tutoriales de Konvergo ERP: Alquiler</a></p></li>
</ul>
</div>

## Precio de alquiler

### Configuración

Vaya a Alquiler ‣ Productos, seleccione o cree un producto y haga clic en la
pestaña de _Alquiler_ del producto. En _Precio de alquiler_ haga clic en
_Agregar un precio_. Posteriormente, elija una _unidad_ de tiempo (horas,
días, semanas, o meses), una _duración_ , y un _precio_. Puede agregar tantas
líneas de precio como sean necesarias, normalmente para dar descuentos para
duraciones de alquiler más largas.

![Ejemplo de la configuración de precios de alquiler en la aplicación Alquiler
de Konvergo ERP](../../_images/rental-pricing-example.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>En <em>Reservaciones</em> puede agregar multas por cualquier <em>hora extra</em> o <em>día extra</em>. También puede establecer un <em>tiempo de seguridad</em>, que se expresa en horas, para hacer que un producto no esté disponible de forma temporal entre dos órdenes de alquiler.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si desea rentar un producto que se creó fuera de la aplicación Alquiler, no olvide seleccionar la opción de <em>Se puede rentar</em>, la cual se encuentra debajo del nombre del producto. Esta opción se selecciona de forma predeterminada cuando crea un producto directamente en la aplicación Alquiler.</p>
</div>

### Cálculo

Konvergo ERP siempre usa dos reglas para calcular el precio de un producto cuando crea
una orden de alquiler:

  1. Solo se utiliza una línea de precio.

  2. Se selecciona la línea más barata.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Considere la siguiente configuración de precio de alquiler para un producto:</p>
<ul>
<li><p>1 día: $100</p></li>
<li><p>3 días: $250</p></li>
<li><p>1 semana: $500</p></li>
</ul>
<p>Un cliente desea rentar este producto por ocho días. ¿Qué precio pagará?</p>
<p>Después de que se crea una orden, Konvergo ERP selecciona la segunda línea porque es la opción más barata. El cliente tiene que pagar “3 días” tres veces para cubrir los ocho días del alquiler, lo que da como resultado $750.</p>
</div>

## Firma del cliente

Puede solicitar a sus clientes que firmen un acuerdo de alquiler que delimita
el arreglo entre usted y sus clientes antes de que recolecten los productos,
con el fin de asegurarse de que devuelvan sus productos a tiempo y en su
condición original. Para hacerlo, vaya a Alquiler ‣ Configuración ‣ Ajustes,
active la función de _Documentos digitales_ y haga clic en _Guardar_.

![Ajustes de documentos digitales en la aplicación Alquiler de
Konvergo ERP](../../_images/digital-documents-settings.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta función necesita la aplicación <a href="../productivity/sign">Firma electrónica</a>. Si es necesario, Konvergo ERP la instalará después de activar los <em>documentos digitales</em>.</p>
</div>

Una vez que guarde los ajustes de la aplicación, tiene la opción de cambiar el
_acuerdo de alquiler_ predeterminado en el menú desplegable. Puede elegir
cualquier documento que haya subido a la aplicación _Firma_ , o puede subir
uno nuevo a _Firma_ al hacer clic en _Subir plantilla_.

Para solicitar una firma de cliente, seleccione una orden de alquiler
confirmada, haga clic en _Firmar documentos_ , elija la plantilla de documento
y vuelva a hacer clic en _Firmar documentos_. En la siguiente ventana,
seleccione su cliente y haga clic en _Firmar ahora_ para iniciar el proceso de
firma de su cliente. Una vez que se complete el documento, haga clic en
_Validar y enviar documento completo_.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/sign-61">Tutoriales de Konvergo ERP: Firma electrónica</a></p></li>
</ul>
</div>

## Recibos de recolección y devolución

Puede imprimir los recibos y dárselos a sus clientes cuando recolecten o
devuelvan sus productos. Para hacerlo, abra cualquier orden de alquiler, haga
clic en _Imprimir_ y seleccione _Recibo de recolección y devolución_. Konvergo ERP
generará un PDF con toda la información sobre el estado actual de los
artículos alquilados: cuáles se recolectaron, cuándo se espera su devolución,
cuáles se devolvieron y posibles costos de retraso del alquiler.

![Imprimir un recibo de recolección y devolución en la aplicación Alquiler de
Konvergo ERP](../../_images/print-receipt1.png)

