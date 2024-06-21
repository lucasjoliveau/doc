# Facturar objetivos de proyecto

La facturación basada en hitos del proyecto se puede utilizar para proyectos
costosos o de gran escala. La serie de hitos en un proyecto representa una
secuencia clara de trabajo que inevitablemente resultará en la finalización de
un proyecto y/o contrato.

Este método de facturación garantiza que la empresa obtenga un flujo constante
de dinero durante toda la vida del proyecto. Los clientes pueden monitorear de
cerca cada fase del desarrollo del proyecto a medida que ocurre, además de
pagar una gran factura en varias cuotas, en lugar de todo de una vez.

## Crear productos de objetivo

En Konvergo ERP, cada objetivo de un proyecto se considera como un producto
individual.

Para crear y/o configurar productos para que funcionen de esta manera, primero
vaya a la aplicación Ventas ‣ Productos ‣ Productos. Luego, haga clic en un
producto, o cree uno nuevo mediante el botón **Nuevo**.

La opción de facturar según los objetivos solo está disponible para ciertos
tipos de productos.

En el formulario del producto, debajo de la pestaña **información general** ,
el campo **tipo de producto** _debe_ establecerse en una de las siguientes
opciones: **servicio** , **boleto de evento** , **estand de evento** o
**curso**.

![El menú desplegable del campo de política de facturación con opciones en el
formulario de producto.](../../../../_images/product-type-field.png)

Con cualquiera de esas opciones de **tipo de producto** seleccionadas, elija
**según los objetivos** del menú desplegable **política de facturación**.

![El menú desplegable del campo de política de facturación con opciones en el
formulario de producto.](../../../../_images/invoicing-policy-field.png)

Debajo de eso está el campo **crear en orden**.

Para garantizar que los flujos de trabajo sean lo más fluidos posible, se
recomienda seleccionar una opción en el campo **crear en orden**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Dejarlo en la opción predeterminada <b>Nada</b> no afectará negativamente el flujo de trabajo deseado. Sin embargo, <em>debe</em> crear un proyecto directamente desde un formulario de orden de venta con ese producto específico. Una vez que crea un proyecto, <em>entonces</em> se pueden crear y configurar objetivos y tareas.</p>
</div>

Una vez que haga clic en la opción predeterminada **crear en orden** de
**Nada** , verá un menú desplegable con las siguientes opciones:

  * **Tarea:** : Konvergo ERP crea una tarea relacionada con este producto de objetivo en la aplicación _Proyecto_ cuando se realiza una orden con este producto específico.

  * **Proyecto y tarea:** : Konvergo ERP crea un proyecto y una tarea relacionada con este producto de objetivo en la aplicación _Proyecto_ cuando se realiza una orden con este producto específico.

  * **Proyecto:** : Konvergo ERP crea un proyecto relacionado con este producto de objetivo en la aplicación _Proyecto_ cuando se realiza una orden con este producto específico.

Si selecciona **Tarea** , aparecerá el campo **Proyecto**. En este campo,
seleccione a qué proyecto existente en la aplicación _Proyectos_ debe estar
conectada esta tarea creada.

![El campo Proyecto aparece cuando se selecciona la opción Tarea en el campo
Crear en Orden.](../../../../_images/task-option-project-field.png)

Si selecciona **proyecto y tarea** o **proyecto** , aparecerán dos nuevos
campos: **plantilla de proyecto** y **plantilla de espacio de trabajo**.

![El campo de plantilla de proyecto y el campo de plantilla de espacio de
trabajo que aparecen en el producto de objetivo.](../../../../_images/project-
task-option-project-workspace-fields.png)

El campo **plantilla de proyecto** proporciona opciones de plantilla para usar
en el proyecto que se creará cuando se ordene este producto específico.

El campo **plantilla de espacio de trabajo** proporciona opciones de plantilla
para usar en el espacio de trabajo (en la aplicación _Documentos_ , no la
aplicación _Proyecto_) que se generará automáticamente para el proyecto cuando
se ordene este producto específico.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para fines organizativos, haga clic en la pestaña <b>Ventas</b> en el formulario del producto y escriba una descripción personalizada relacionada con los “objetivos” en el campo <b>descripción de ventas</b>. Esta información aparece en la columna <b>descripción</b> en la pestaña <b>líneas de la orden</b> de la orden de ventas.</p>
<p>También puede editar/modificar directamente el campo <b>descripción</b> en la pestaña <b>líneas de la orden</b> de la orden de venta.</p>
<p>Esto <em>no</em> es un requisito.</p>
</div>

## Facturar objetivos

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El siguiente flujo presenta un trío de productos de objetivo que tienen <b>Servicio</b> establecido como su <b>tipo de producto</b> y <b>tarea</b> establecida en su campo <b>crear en orden</b>.</p>
<blockquote>
<div><img alt='Producto con tipo de producto "servicio" y "tarea" en el campo crear en la orden del formulario.' class="align-center" src="../../../../_images/settings-for-workflow.png"/>
</div></blockquote>
<p>Esas tareas se adjuntan a un <b>proyecto</b> preexistente, que en este caso se titula <b>proyectos de cambio de marca</b>.</p>
</div>

Si desea facturar objetivos, cree una orden de venta con los productos del
objetivo. Para hacerlo, vaya a la aplicación Ventas ‣ Nuevo. Al hacerlo, se
mostrará un formulario vacío de cotización.

Desde este formulario de cotización, agregue un **cliente**. Luego, haga clic
en **agregar un producto** en la pestaña **líneas de la orden**. A
continuación, agregue los productos de objetivo a la pestaña **líneas de la
orden**.

Una vez que se hayan agregado los productos correspondientes al objetivo, haga
clic en **confirmar** para confirmar la orden, esto convierte la cotización en
una orden de venta.

Al confirmar la orden, aparecerán nuevos botones inteligentes en la parte
superior de la orden de venta según lo seleccionado en el campo **crear en la
orden** en el formulario del producto.

En la orden de venta, haga clic en el botón inteligente **objetivos**. Al
hacerlo, se mostrará una página en blanco de **objetivos**. Haga clic en
**nuevo** para agregar objetivos.

![Adición de objetivos a una orden de venta con productos de
objetivos.](../../../../_images/adding-milestones.png)

Ingrese un **nombre** para el objetivo. A continuación, aplíquelo al
**artículo en la orden de venta** correspondiente. También puede asignar una
**fecha límite** al objetivo.

Repite ese proceso para todos los elementos de la orden de venta de objetivos.

Luego, regrese a la orden de venta, a través de las migas de pan. En la orden
de venta, haga clic en el botón inteligente **tareas**. Al hacerlo, podrá ver
la página **tareas** con una tarea para cada artículo de la orden de venta con
esa opción designada en el campo **crear en la orden**.

![Página de tareas de muestra accedida a través del botón inteligente desde
una orden de venta con productos de objetivo.](../../../../_images/tasks-
page.png)

Si desea asignar manualmente un objetivo configurado a una tarea, haga clic en
la tarea deseada, lo que revela el formulario de la tarea. En el formulario de
la tarea, seleccione el objetivo apropiado al que esta tarea debe estar
conectada, en el campo **objetivo** .

![El campo de objetivo en el formulario de tarea al tratar con productos de
objetivo en la aplicación Ventas de Konvergo ERP.](../../../../_images/milestone-
field-on-task-form.png)

Repita este proceso para todas las tareas de objetivo.

Si estas tareas están configuradas correctamente, los empleados podrán
registrar su progreso mientras trabajan en la tarea, además de agregar
cualquier nota relacionada con la tarea.

Una vez que esa tarea esté completa, significa que se ha alcanzado ese
objetivo. En ese momento, es hora de facturarlo.

Si desea facturar un objetivo primero regrese a la orden de venta, ya sea a
través de los enlaces de navegación o a través de la aplicación de Ventas ->
Órdenes -> Órdenes y seleccionar la orden de venta correspondiente.

Vuelva al formulario de la orden de venta, haga clic en el botón inteligente
**objetivos** y marque la casilla en la columna **alcanzado** para esa tarea
en específico.

![Marcar un objetivo como alcanzado a través del botón inteligente de
objetivos.](../../../../_images/reached-milestone.png)

A continuación, regrese a la orden de venta mediante el botón **ver orden de
venta** en la página **objetivos** , o a través de los enlaces de navegación.

De nuevo en la orden de venta, el artículo de línea para el objetivo que se ha
alcanzado tiene su columna **entregado** completada. Esto se debe a que se ha
alcanzado el objetivo y, por lo tanto, se ha entregado.

![Un producto de objetivo que se ha alcanzado y se ha marcado como entregado
en la orden de venta en Konvergo ERP.](../../../../_images/delivered-milestone-
product-sales-order.png)

Haga clic en **crear factura** en la esquina superior izquierda. Al hacerlo,
se mostrará la ventana emergente **crear facturas**.

![La ventana emergente 'crear factura' que aparece cuando se hace clic en el
botón de crear factura.](../../../../_images/create-invoices-pop-up.png)

En la ventana emergente **crear factura** , deje la opción **crear factura**
en la selección predeterminada **factura normal** y haga clic en el botón
**crear borrador de factura**.

Al hacer clic en **crear borrador de factura** , Konvergo ERP mostrará el **borrador
de factura de cliente** , que muestra _solo_ el objetivo alcanzado en la
pestaña **líneas de la factura**.

![Un borrador de factura del cliente que muestra solo el producto de objetivo
que se alcanzó.](../../../../_images/invoice-draft-milestone.png)

Desde esta página de factura, haga clic en el botón **confirmar** para
confirmar la factura. Luego, cuando el cliente haya pagado por este objetivo,
haga clic en **registrar pago**.

Cuando haga clic en **registrar pago** , aparecerá la ventana emergente de
**registrar pago**.

![La ventana emergente registro de pago que aparece cuando se hace clic en
registro de pago.](../../../../_images/register-payment-pop-up.png)

En esta ventana emergente, confirme la precisión de los campos autocompletados
y luego haga clic en **crear pago**.

Cuando se hace clic, la ventana emergente desaparece y Konvergo ERP vuelve a la
factura para ese objetivo, que ahora tiene un listón verde con la leyenda **en
proceso de pago** en la esquina superior derecha. Este listón indica que la
factura se ha pagado.

![Una factura con un producto de objetivo que se ha pagado con un listón con
la leyenda 'en proceso de pago'.](../../../../_images/in-payment-invoice.png)

Luego, regrese a la orden de venta a través de los enlaces de navegación. En
la orden de venta, vaya a la pestaña **líneas de la orden** , ahí podrá ver el
objetivo alcanzado que se ha facturado y pagado, con la columna **facturado**
completada.

![La columna 'facturado' de un producto de objetivo que ha sido pagado está
completa.](../../../../_images/invoiced-column-filled-milestone.png)

También hay un nuevo botón inteligente **Facturas** en la parte superior de la
orden de venta. Al hacer clic en él podrá ver todas las facturas vinculadas a
esta orden de venta.

![El botón inteligente de facturas que aparece en la parte superior de una
orden de venta con objetivos.](../../../../_images/invoices-smart-button.png)

Repita el proceso anterior para cada objetivo conforme se vaya trabajando en
él y, posteriormente, se complete.

Continúe ese proceso hasta que se haya completado todo el proyecto, se haya
facturado cada objetivo y se haya pagado la orden completa.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="time_materials">Facturación por tiempo y materiales</a></p></li>
<li><p><a href="proforma">Facturas proforma</a></p></li>
<li><p><a href="invoicing_policy">Facturar por cantidades entregadas u ordenadas</a></p></li>
</ul>
</div>

