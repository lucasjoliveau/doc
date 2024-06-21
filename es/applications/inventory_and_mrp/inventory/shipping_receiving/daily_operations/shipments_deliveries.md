# Envíos entrantes y órdenes de entrega

Hay varias maneras de gestionar la forma en que un almacén recibe productos
(recepciones) y envía productos (entregas). La forma en que se gestionan los
productos al entrar y salir del almacén puede variar mucho debido a varios
factores como el tipo de productos almacenados y vendidos, el tamaño del
almacén y la cantidad de recibos y órdenes de entrega confirmadas al día,
entre otros. Puede configurar diferentes ajustes para las recepciones y las
entregas, pues no es necesario que estén configuradas para tener el mismo
número de pasos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/using-routes-1018">Uso de rutas (tutorial en eLearning)</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/push-pull-rules-1024">Reglas push y pull (tutorial en eLearning)</a></p></li>
</ul>
</div>

## Elegir el flujo de inventario adecuado para gestionar recepciones y
entregas

De forma predeterminada, Konvergo ERP gestiona el envío y la recepción de tres formas
distintas: en uno, dos o tres pasos. La configuración más simple es en un
paso, que es la estándar. Cada paso adicional necesario para un almacén para
procesar la recepción o el envío agregará una capa adicional de operaciones a
realizar antes de recibir o enviar un producto. Estas configuraciones dependen
por completo de los requisitos de los productos almacenados, como realizar
controles de calidad de los productos recibidos o utilizar embalaje especial
en los productos enviados.

### Flujo de un paso

Las reglas de recepción y envío para una configuración de un solo paso son las
siguientes:

  * **Recepción** : reciba productos directamente en sus existencias. No hay pasos intermedios entre la recepción y su colocación en existencias, como una transferencia a un lugar donde se realiza un control de calidad.

  * **Envío** : envíe productos de forma directa desde las existencias. No hay pasos intermedios entre las existencias y el envío, como un traslado a una ubicación de empaquetado.

  * Solo se puede usar si no se usan las estrategias de remoción PEPS, UEPS o FEFO.

  * Las recepciones y las entregas se gestionan con rapidez.

  * Se recomienda para almacenes pequeños con bajos niveles de existencias y para artículos no perecederos.

  * Los artículos se reciben desde o se envían directamente a las existencias.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="receipts_delivery_one_step">Procesar recepciones y entregas en un paso</a></p>
</div>

### Flujo de dos pasos

Las reglas de recepción y envío para una configuración de dos pasos son las
siguientes:

  * **Entrada + existencias** : lleve los productos a una ubicación de entrada _antes_ de que entren a las existencias. Puede organizar los productos por distintas ubicaciones de almacenamiento interno como varios estantes, congeladores y áreas cerradas, antes de guardarlos en el almacén.

  * **Recolectar + enviar** : lleve los productos a una ubicación de salida antes de enviarlos. Puede organizar los productos por diferentes transportistas o muelles de envío antes de enviarlos.

  * Como requisito mínimo, debe utilizar números de lote o serie para rastrear productos con estrategias de remoción PEPS, UEPS o FEFO.

  * Se recomienda para almacenes más grandes con altos niveles de existencias o al almacenar artículos grandes (como colchones, muebles grandes, maquinaria pesada, etc.).

  * Los productos recibidos no estarán disponibles para fabricar, enviar, etc., hasta que se transfieran a las existencias.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="receipts_delivery_two_steps#inventory-receipts-delivery-two-steps"><span class="std std-ref">Procesar recepciones y entregas en dos pasos</span></a></p>
</div>

### Flujo de tres pasos

Las reglas de recepción y envío para una configuración de tres pasos son las
siguientes:

  * **Entrada + calidad + existencias** : reciba productos en la ubicación de entrada, transfiéralos a un área de control de calidad y mueva los que pasan la inspección a sus existencias.

  * **Recolectar + empaquetar + enviar** : recolecte productos de acuerdo con su estrategia de remoción, empaquételos en un área destinada y llévelos a una ubicación de salida para enviarlos.

  * Se puede usar para rastrear productos por números de lote o serie cuando utiliza una estrategia de eliminación PEPS, UEPS o FEFO.

  * Se recomienda para almacenes muy grandes con niveles muy altos de existencias.

  * Es necesario para cualquier almacén que necesite realizar controles de calidad antes de recibir artículos en sus existencias.

  * Los productos recibidos no estarán disponibles para fabricar, enviar, etc., hasta que se transfieran a las existencias.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="receipts_three_steps#inventory-receipts-three-steps"><span class="std std-ref">Procesar recepciones en tres pasos</span></a></p></li>
<li><p><a href="delivery_three_steps#inventory-delivery-three-steps"><span class="std std-ref">Procesar entregas en tres pasos</span></a></p></li>
</ul>
</div>

  *[PEPS]: Primeras entradas, primeras salidas
  *[UEPS]: Últimas entradas, primeras salidas
  *[FEFO]: Primero en expirar, primero en salir

