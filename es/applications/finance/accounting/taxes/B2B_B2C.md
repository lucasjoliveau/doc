# Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)

Cuando se trabaja con consumidores, normalmente se muestran los precios con
impuestos incluidos (por ejemplo, en la mayoría de los comercios
electrónicos). Pero, cuando se trabaja en un entorno B2B, las empresas suelen
negociar los precios sin incluir los impuestos.

Konvergo ERP permite el uso de ambos, siempre y cuando registre sus precios en el
producto, sin impuestos o con impuestos incluidos, pero no los dos al mismo
tiempo. Si usted maneja todos sus precios con impuestos incluidos (o
excluidos), aún puede crear fácilmente una orden de venta con un precio que
tenga impuestos excluidos (o incluidos), es así de fácil.

Esta documentación es solo para el caso de uso específico donde se necesita
tener dos referencias en el precio (con o sin impuestos incluidos), para el
mismo producto. La complejidad se debe a que no existe una relación simétrica
entre los precios con impuestos incluidos y los precios sin impuestos
incluidos, en este caso de uso, en Bélgica, con un impuesto del 21%:

  * Su comercio electrónico tiene un producto a **10€ (impuestos incluidos)**.

  * Es decir, **8.26€ (sin impuestos)** con un **impuesto de 1.74€**.

Por otro lado, en el mismo caso de uso, si se registra el precio sin impuestos
en el formulario del producto (8.26€), se obtiene un precio con impuestos
incluidos de 9.99€:

  * **8.26€ * 1.21 = 9.99€**

Por lo tanto, dependiendo de cómo haya registrado sus precios en el formulario
del producto, tendrá diferentes resultados para el precio con impuestos
incluidos y el precio sin impuestos:

  * Impuestos excluidos: **8.26€ & 10.00€**

  * Impuestos incluidos: **8.26€ & 9.99€**

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si compra 100 piezas a 10€ con impuestos incluidos, el asunto se complica todavía más. Obtendrá: <b>1000€ (impuestos incluidos) = 826.45€ (precio) + 173.55€ (impuestos)</b> Lo cual es muy diferente a una pieza a 8.26€ sin impuestos.</p>
</div>

Esta documentación explica cómo manejar un caso de uso muy específico en el
que se necesitan manejar los dos tipos de precios (con y sin impuestos) en el
formulario de un producto dentro de la misma empresa.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En términos financieros, no obtendrá más ingresos si vende su producto a 10 euros en lugar de 9.99 euros (con un impuesto del 21%), pues sus ingresos serán exactamente los mismos a 9.99 euros, solo que el impuesto será más alto por 0.01 euros. Por lo tanto, si tiene su comercio electrónico en Bélgica, ayúdele a sus clientes y establezca el precio en 9.99 EUR en lugar de 10 EUR. Tenga en cuenta que esto no aplica a 20 o 30 euros, otras tasas impositivas o una cantidad mayor a 1. También facilitará las cosas para usted, ya que podrá gestionar todo sin incluir impuestos, lo cual implicará menos errores y será más fácil para sus vendedores.</p>
</div>

## Configuración

### Introducción

La mejor manera de evitar esta complejidad es elegir solo una forma de
gestionar sus precios y atenerse a ella: usar el precio sin impuestos o con
impuestos incluidos. Defina cuál es el valor predeterminado almacenado en el
formulario del producto, deje que Konvergo ERP calcule el otro en automático según la
lista de precios y la posición fiscal y negocie sus contratos con los clientes
según corresponda. Esto funciona a la perfección y no tiene que hacer ninguna
configuración específica.

Si no puede hacerlo y debe hacer negocios tanto con precios sin impuestos como
con precios con impuestos incluidos, deberá:

  1. siempre guardar el precio predeterminado **con impuestos no incluidos** en el formulario del producto, y aplicar un impuesto (precio no incluido en el formulario del producto).

  2. crear una lista de precios con precios que tengan **impuestos incluidos** para clientes específicos

  3. crear una posición fiscal que cambie un precio sin impuestos por un precio con impuestos

  4. asignar tanto la lista de precios como la posición fiscal a los clientes que quieran beneficiarse de esta lista de precios y posición fiscal

Con el fin de ejemplificar esta documentación, utilizaremos el caso de uso
anterior:

  * el precio de venta predeterminado de su producto es de 8.26€ sin impuestos

  * pero queremos venderlo a 10€, con impuestos incluidos, en nuestras tiendas o sitio web de comercio electrónico

### Comercio electrónico

Si solo utiliza precios B2C o B2B en su sitio web, seleccione los ajustes
adecuados en los ajustes de la aplicación **Sitio web**.

Si utiliza tanto precios B2B como B2C en un solo sitio web, siga estas
instrucciones:

  1. Active el [modo de desarrollador](../../../general/developer_mode#developer-mode) y vaya a Ajustes generales ‣ Usuarios y empresas ‣ Grupos.

  2. Abra `Técnico/Impuesto B2B` o `Técnico/Impuesto B2C`.

  3. En la pestaña **usuarios** , agregue los usuarios que necesitan acceso al tipo de precio. Agregue usuarios B2C en el grupo B2C y usuarios B2B en el grupo B2B.

### Gestionar productos

Debe configurar los precios de su empresa sin impuestos incluidos de forma
predeterminada. Por lo general esta es la configuración estándar, pero puede
comprobar su **Impuesto de venta predeterminado** desde el menú Configuración
‣ Ajustes de la aplicación Contabilidad.

![../../../../_images/price_B2C_B2B01.png](../../../../_images/price_B2C_B2B01.png)

Una vez que lo haya hecho, podrá crear una lista de precios **B2C**. Puede
activar la función de lista de precios por cliente desde el menú:
Configuración ‣ Ajustes en la aplicación Venta. Elija la opción **diferentes
precios por segmento de clientes**.

Ahora, cree una lista de precios B2C desde el menú Configuración ‣ Listas de
precios. También es bueno cambiar el nombre de la lista de precios
predeterminada a B2B para evitar confusiones.

Después, cree un producto a 8.26€, con un impuesto del 21% (definido como
impuesto no incluido en el precio) y establezca un precio en este producto
para clientes B2C a 10€, desde el menú Ventas ‣ Productos en la aplicación
Ventas:

![../../../../_images/price_B2C_B2B02.png](../../../../_images/price_B2C_B2B02.png)

### Fijar la posición fiscal del B2C

Desde la aplicación de contabilidad, cree una posición fiscal B2C desde este
menú: Configuración ‣ Posiciones fiscales. Esta posición fiscal debe asignar
un IVA del 21% (impuesto excluido del precio) con un IVA del 21% (impuesto
incluido en el precio)

![../../../../_images/price_B2C_B2B03.png](../../../../_images/price_B2C_B2B03.png)

## Realizar una cotización de prueba

Cree una cotización desde la aplicación Ventas, a través del menú Ventas ‣
Cotizaciones. Debería obtener el siguiente resultado: 8.26€ + 1.73€ = 9.99€.

![../../../../_images/price_B2C_B2B04.png](../../../../_images/price_B2C_B2B04.png)

Después, cree una cotización pero **cambie la lista de precios a B2C y la
posición fiscal a B2C** antes de añadir su producto. Debería obtener el
resultado esperado, que es un precio total de 10€ para el cliente: 8.26€ +
1.74€ = 10.00€.

![../../../../_images/price_B2C_B2B05.png](../../../../_images/price_B2C_B2B05.png)

Este es el comportamiento esperado para un cliente de su negocio.

## Evite cambiar cada orden de ventas

Si negocia un contrato con un cliente, ya sea con o sin impuestos incluidos,
puede establecer la lista de precios y la posición fiscal en el formulario del
cliente para que se aplique automáticamente en cada venta de este cliente.

La lista de precios se encuentra en la pestaña **ventas y compras** del
formulario del cliente, y la posición fiscal se encuentra en la pestaña de
contabilidad.

Tenga en cuenta que esta opción es propensa a errores: si establece una
posición fiscal con impuestos incluidos en los precios, pero utiliza una lista
de precios en la que no están incluidos, podría obtener resultados erróneos en
el cálculo de los precios. Por eso solemos recomendar a las empresas que solo
trabajen con una referencia de precios.

