# Seguimiento en las facturas

Cuando un pago no se ha realizado es posible enviarle un mensaje de
seguimiento al cliente. Konvergo ERP le ayuda a identificar pagos atrasados y le ayuda
a programar y enviar recordatorios apropiados para realizar **acciones de
seguimiento**. Las acciones dependerán de la cantidad de días que el cliente
se ha tardado en pagar. Puede enviar mensajes de seguimiento por diferentes
medios, como correo electrónico, correo postal, o mensaje de texto.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/payment-follow-up-1682">Tutoriales de Konvergo ERP: seguimientos de pago</a></p></li>
</ul>
</div>

## Configuración

Para configurar una **acción de seguimiento** vaya a Contabilidad ‣
Configuración ‣ Niveles de seguimiento y seleccione o cree un nivel de
seguimiento (o varios). Habrá varias acciones de seguimiento disponibles de
forma predeterminada en la pestaña **Notificación** , donde podrá cambiar
tanto el **nombre** como el **número de días**. Las **acciones** disponibles
son:

  * **Enviar correo** ;

  * [Enviar una carta](../customer_invoices/snailmail#customer-invoices-snailmail);

  * [Enviar un SMS](../../../marketing/sms_marketing/pricing/pricing_and_faq#pricing-pricing-and-faq).

Para usar una plantilla prefabricada haga clic en **Plantilla de contenido**.
Para cambiar la plantilla utilizada, pase el cursor encima de **– >**. Si está
activado, los mensajes SMS tienen un campo de **Plantilla de SMS** específico.

Es posible enviar un recordatorio de manera automática, para esto tiene que
activar la opción **Automático** , para adjuntar la o las facturas _abiertas_
active **Adjuntar facturas** dentro de una acción de seguimiento específica.

Puede programar actividades (tareas) en la pestaña **Actividad**. De esa
manera, se programará una actividad de manera automática cuando se active el
seguimiento programado. Para hacerlo, active **Programar actividad** y
seleccione una persona **Responsable** de la tarea. Elija un **Tipo de
actividad** , e ingrese un **Resumen** sobre cómo se debe realizar la
actividad si así lo desea.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para enviar un recordatorio antes de la fecha límite real, configure un número negativo de días.</p>
</div>

## Reportes de seguimiento

Las facturas sin pagar a las que les tiene que dar seguimiento están
disponibles en Contabilidad ‣ Clientes ‣ Reportes de seguimiento. Konvergo ERP filtra
por **Facturas atrasadas** de forma predeterminada, pero también puede filtrar
por **Se necesita realizar una acción** en el menú **Filtros**.

Cuando seleccione una factura, puede ver todas las facturas que un cliente no
ha pagado (atrasadas o no). Las fechas de facturas retrasadas aparecerán en
rojo. Para excluir facturas de un seguimiento de un recordatorio debe hacer
clic en **Excluir de seguimientos**. Puede configurar recordatorios
**Automáticos** o **Manuales** , además de que puede escoger a una persona
**Responsable** para ese cliente.

Para enviar recordatorios, haga clic en **Seguimiento** y seleccione las
acciones (o la acción) que quiere realizar:

  * **Imprimir** ;

  * **Correo electrónico** ;

  * **SMS** ;

  * **Correo postal**.

Puede **adjuntar facturas** y cambiar las plantillas de contenido desde esta
vista. Cuando esté listo, haga clic en **Enviar** o **Enviar e imprimir**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>La información de contacto en la factura o en el formulario de contacto es lo que se usa para enviar un recordatorio.</p></li>
<li><p>Cuando se envía el recordatorio, esto se documenta en el chatter de la factura.</p></li>
<li><p>Si todavía no es momento de enviar un recordatorio, puede especificar una fecha para el <b>Siguiente recordatorio</b>. Su siguiente reporte tomará en cuenta la fecha que programó para el siguiente recordatorio.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Concilie todos los estados bancarios antes de iniciar el proceso de seguimiento para evitar enviarle un recordatorio a un cliente que ya realizó el pago.</p>
</div>

### Nivel de confianza del deudor

Para saber si un cliente paga tarde o no, puede configurar un nivel de
confianza y marcarlos como **Buen deudor** , **Deudor normal** , o **Mal
deudor** en el reporte de seguimiento del cliente. Para hacerlo, haga clic en
la casilla a un lado del nombre del cliente y seleccione un nivel de
confianza.

![Configure el nivel de confianza del deudor](../../../../_images/debtor-
level.png)

### Enviar recordatorios por lotes

Desde la página de **Reportes de seguimiento** puede enviar correos de
recordatorio por lotes. Seleccione todos los reportes que desea procesar, haga
clic en el icono de engranaje **Acción** y seleccione **Procesar
seguimientos**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../essentials/in_app_purchase">Compras dentro de la aplicación (IAP)</a></p></li>
<li><p><a href="../../../marketing/sms_marketing/pricing/pricing_and_faq">Precios de SMS y preguntas frecuentes</a></p></li>
<li><p><a href="../customer_invoices/snailmail">Correo postal</a></p></li>
</ul>
</div>

