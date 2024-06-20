# Alquiler

La aplicación **Alquiler de Odoo** es una solución exhaustiva para gestionar
sus propiedades.

Desde una única vista, puede enviar cotizaciones, confirmar órdenes, programar
alquileres, registrar cuándo se recolectan y devuelven los productos y
facturar a sus clientes.

Ver también

  * [Alquiler de Odoo: página de producto](https://www.odoo.com/app/rental)

  * [Tutoriales de Odoo: Alquiler](https://www.odoo.com/slides/rental-48)

## Precio de alquiler

### Configuración

Vaya a Alquiler ‣ Productos, seleccione o cree un producto y haga clic en la
pestaña de _Alquiler_ del producto. En _Precio de alquiler_ haga clic en
_Agregar un precio_. Posteriormente, elija una _unidad_ de tiempo (horas,
días, semanas, o meses), una _duración_ , y un _precio_. Puede agregar tantas
líneas de precio como sean necesarias, normalmente para dar descuentos para
duraciones de alquiler más largas.

![Ejemplo de la configuración de precios de alquiler en la aplicación Alquiler
de Odoo](../../_images/rental-pricing-example.png)

Truco

En _Reservaciones_ puede agregar multas por cualquier _hora extra_ o _día
extra_. También puede establecer un _tiempo de seguridad_ , que se expresa en
horas, para hacer que un producto no esté disponible de forma temporal entre
dos órdenes de alquiler.

Nota

Si desea rentar un producto que se creó fuera de la aplicación Alquiler, no
olvide seleccionar la opción de _Se puede rentar_ , la cual se encuentra
debajo del nombre del producto. Esta opción se selecciona de forma
predeterminada cuando crea un producto directamente en la aplicación Alquiler.

### Cálculo

Odoo siempre usa dos reglas para calcular el precio de un producto cuando crea
una orden de alquiler:

  1. Solo se utiliza una línea de precio.

  2. Se selecciona la línea más barata.

Exercise

Considere la siguiente configuración de precio de alquiler para un producto:

  * 1 día: $100

  * 3 días: $250

  * 1 semana: $500

Un cliente desea rentar este producto por ocho días. ¿Qué precio pagará?

Después de que se crea una orden, Odoo selecciona la segunda línea porque es
la opción más barata. El cliente tiene que pagar “3 días” tres veces para
cubrir los ocho días del alquiler, lo que da como resultado $750.

## Firma del cliente

Puede solicitar a sus clientes que firmen un acuerdo de alquiler que delimita
el arreglo entre usted y sus clientes antes de que recolecten los productos,
con el fin de asegurarse de que devuelvan sus productos a tiempo y en su
condición original. Para hacerlo, vaya a Alquiler ‣ Configuración ‣ Ajustes,
active la función de _Documentos digitales_ y haga clic en _Guardar_.

![Ajustes de documentos digitales en la aplicación Alquiler de
Odoo](../../_images/digital-documents-settings.png)

Nota

Esta función necesita la aplicación [Firma
electrónica](../productivity/sign.html). Si es necesario, Odoo la instalará
después de activar los _documentos digitales_.

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

Ver también

  * [Tutoriales de Odoo: Firma electrónica](https://www.odoo.com/slides/sign-61)

## Recibos de recolección y devolución

Puede imprimir los recibos y dárselos a sus clientes cuando recolecten o
devuelvan sus productos. Para hacerlo, abra cualquier orden de alquiler, haga
clic en _Imprimir_ y seleccione _Recibo de recolección y devolución_. Odoo
generará un PDF con toda la información sobre el estado actual de los
artículos alquilados: cuáles se recolectaron, cuándo se espera su devolución,
cuáles se devolvieron y posibles costos de retraso del alquiler.

![Imprimir un recibo de recolección y devolución en la aplicación Alquiler de
Odoo](../../_images/print-receipt1.png)

