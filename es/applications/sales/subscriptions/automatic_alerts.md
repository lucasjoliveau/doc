# Alertas automáticas

Ahora que ya tiene suscripciones funcionando, es conveniente que esté al día
con sus clientes. Sería bueno contar con algo de automatización para que evite
tener que ir revisando suscripción por suscripción para ver su estado. Para
esto es la función de _Alertas automáticas_.

Por ejemplo, cuando los clientes se suscriben a su revista, probablemente
quiera enviarles un correo electrónico para darles la bienvenida y expresar su
gratitud. O, si la tasa de satisfacción se encuentra por debajo del 50%,
querrá agendar una llamada para saber cuál fue la razón de su valoración.

Gracias a la aplicación de **Suscripción de Odoo** , puede establecer correos
electrónicos automáticos, crear una tarea de «Llamada» para que alguno de sus
vendedores sepa por qué el cliente no está satisfecho, y, por último, ¿por qué
no enviar una encuesta de satisfacción para que sus clientes puedan evaluar
sus servicios? Todo eso es posible.

## Crear una nueva alerta automática

El siguiente ejemplo muestra cómo crear una alerta automática para enviar
encuestas de satisfacción a sus clientes, por correo electrónico, una vez que
cumplan un mes suscritos. Para hacerlo, vaya a Suscripción ‣ Configuración ‣
Alertas y cree una nueva.

![Nueva alerta automática en Suscripciones de Odoo](../../../_images/create-a-
new-automatic-alert.png)

  1. En la sección de _Aplicar a_ , póngale nombre a su alerta. Después puede elegir si desea aplicar la alerta a una plantilla de suscripción, a un cliente o a un producto en específico. Si desea añadir más especificaciones, también puede especificar el valor de su MRR, el cambio de su MRR en cierto periodo de tiempo, el valor de su tasa de satisfacción e incluso la etapa en la que quiera aplicar esta alerta.

Nota

En este ejemplo, se aplicó esta alerta a un producto en específico y la etapa
cambia de _Sin definir_ a _En progreso_.

  2. En la sección de _Acción_ especifique la _acción_ y el campo _Activar en_. Si el campo _Activar en_ está configurado con _Modificación_ , entonces la acción se activa cada que hay un cambio o agrega algo a la suscripción y todas las condiciones en la sección _Aplicar en_ se cumplen. En cambio, si establece _Activar en_ en _Condición de tiempo_ , la acción se activará según el tipo de _fecha de activación_. Después puede elegir su _acción_ , que puede ser _Crear siguiente actividad_ , _Establecer una etiqueta en la suscripción_ , _Establecer una etapa en la suscripción_ , _Marcar como Por renovar_ , _Enviar un correo electrónico al cliente_ y _Enviar un mensaje de texto SMS al cliente_.

Nota

En el ejemplo anterior, se estableció _Activar en_ en _Condición de tiempo_ ,
por lo tanto, se deben especificar la _Fecha de activación_ y _Retraso después
de la activación_. Y como se aplicó la acción de _Enviar un correo electrónico
al cliente_ , debe elegir una _Plantilla de correo electrónico_.

Nota

Para enviar un mensaje de texto SMS en Odoo es necesario que cuente con
créditos o tokens de compras dentro de la aplicación (IAP). Para obtener más
información sobre IAP, visite [Compras dentro de la aplicación
(IAP)](../../essentials/in_app_purchase.html). Para obtener más información
sobre el envío de mensajes SMS, visite [Fundamentos de
SMS](../../marketing/sms_marketing/essentials/sms_essentials.html).

Como resultado, esta alerta envía una encuesta de satisfacción después de un
mes a los clientes que hayan comprado ese producto en específico. La encuesta
aparecerá en el chatter de la suscripción correspondiente.

![Encuesta de satisfacción en Suscripciones de Odoo ](../../../_images/rating-
satisfaction-survey.png)

## Modificar una alerta automática existente

De manera predeterminada, Odoo sugiere una alerta automática llamada
_Contactar a los clientes menos satisfechos_.

![Modificar una alerta automática en Suscripciones de Odoo
](../../../_images/modify-an-existing-automatic-alert.png)

Esta alerta se aplica en la _Valoración de satisfacción_ de sus clientes y se
activa por _Condición de tiempo_. Si su tasa de satisfacción está por debajo
del 50%, un vendedor contactará al cliente. Esta acción se le asigna
automáticamente al vendedor que maneja la suscripción y la fecha límite es 5
días después de haber activado la acción. Esta alerta asegura que sus clientes
estén contentos y que usted tome acciones si no lo están. Ayuda a mantener la
tasa retención de clientes muy alta.

Nota

Al editar la alerta, puede modificar las secciones _Aplicar en_ , _Acción_ y
_Actividad_ para adaptarlas a su gusto.

Ver también

  * [Suscripciones](../subscriptions.html)

  * [Planes de suscripción](plans.html)

  * [Productos de suscripción](products.html)

  * [Compras dentro de la aplicación (IAP)](../../essentials/in_app_purchase.html)

  *[IAP]: Compras dentro de la aplicación

