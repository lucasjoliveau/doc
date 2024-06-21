# Cerrar tickets

Una vez que haya finalizado el trabajo del ticket de _Servicio de asistencia_
en Konvergo ERP, puede cerrarlo de varias maneras. Cerrar manualmente los tickets
resueltos mantiene el flujo de trabajo actualizado, mientras que cerrar
automáticamente los tickets inactivos previene bloqueos innecesarios. Permitir
a los clientes cerrar sus propios tickets minimiza la confusión sobre si un
problema se considera resuelto o no. El resultado es una mayor capacidad
operativa para los equipos de soporte y una mayor satisfacción del cliente.

## Cerrar de forma manual los tickets resueltos

A medida que resuelve el ticket, este pasa a la siguiente fase del proceso.
Una vez resuelto el problema, el ticket pasa a una etapa _plegada_ y se marca
como _cerrado_.

Para plegar una etapa, vaya al tablero de Servicio de asistencia y haga clic
en un equipo para abrir el flujo de trabajo. Pase el ratón por encima del
encabezado de una etapa y haga clic en el icono de engranaje que aparece en la
esquina superior derecha de la columna kanban de esa etapa.

![Vista de la etapa en el flujo de ventas de Servicio de asistencia con
énfasis en el icono de engranaje y la opción de edición de la
etapa.](../../../../_images/closing-edit-stage-gear.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si hace clic en el icono de engranaje aparecerá la opción de <b>Plegar</b> la etapa. Este ajuste plegará la etapa <em>temporalmente</em> para simplificar la vista kanban. Esto <em>no</em> cierra los tickets en esta etapa. Tampoco pliega la etapa de forma permanente. Si desea plegar una etapa para poder marcar los tickets como cerrados, siga los siguientes pasos.</p>
</div>

En el menú que aparece, seleccione **Editar etapa**. Esto abrirá la
configuración de la etapa. Marque la casilla **Plegado en kanban** en la parte
superior de la ventana y, a continuación, **Guardar y cerrar** para confirmar
los cambios. Ahora, los tickets en esta etapa se considerarán como _cerrados_.

> ![Página de ajustes de etapa](../../../../_images/closing-folded-
> setting.png)

## Cerrar automáticamente los tickets inactivos

Se pueden cerrar automáticamente los tickets que permanezcan inactivos durante
un periodo de tiempo determinado. En ese momento, pasarán a una etapa plegada.

Vaya a la página de configuración del equipo en Servicio de asistencia ‣
Configuración ‣ Equipos. En la sección **Autoservicio** , active **Cierre
automático**.

Si una de las etapas del equipo está configurada para plegarse en la vista
kanban, será la selección predeterminada en el campo **Mover a etapa**. Si el
equipo tiene más de una etapa plegada, la etapa que ocurra primero en el flujo
de trabajo será la predeterminada. Si no hay ninguna etapa plegada, la
selección predeterminada será la última etapa del flujo.

El campo **Después de días de inactividad** es `7` de forma predeterminada,
pero puede cambiarlo si así lo desea.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El campo <b>Después de días de inactividad</b> <b>no</b> tiene en cuenta el calendario laboral a la hora de registrar el tiempo que un ticket ha estado inactivo.</p>
</div>

Si solo deben utilizarse determinadas etapas para realizar un seguimiento de
los días de inactividad, pueden añadirse al campo **En etapas**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El flujo de un equipo se crea con las siguientes etapas:</p>
<ul>
<li><p><code>Nuevo</code></p></li>
<li><p><code>En progreso</code></p></li>
<li><p><code>Retroalimentación de los clientes</code></p></li>
<li><p><code>Cerrado</code></p></li>
</ul>
<p>Los tickets pueden permanecer en la etapa <b>Retroalimentación de los clientes</b>, porque una vez resuelto un problema, es posible que los clientes no respondan de inmediato. En ese momento, los tickets pueden cerrarse automáticamente. Sin embargo, los tickets en las etapas <b>Nuevo</b> y <b>En progreso</b> pueden permanecer inactivos debido a problemas de asignación o carga de trabajo. El cierre automático de estos tickets provocaría que los problemas no se resuelvan.</p>
<p>Por lo tanto, los ajustes de <b>Cierre automático</b> se configurarían de la siguiente manera:</p>
<ul>
<li><p><b>Cierre automático</b>: <em>seleccionado</em></p></li>
<li><p><b>Mover a la etapa</b>: <code>resuelto</code></p></li>
<li><p><b>Después de ``7</b><b>días de inactividad</b></p></li>
<li><p><b>En etapas</b>: <code>Retroalimentación de los clientes</code></p></li>
</ul>
<img alt="Ejemplo de configuración del cierre automático." class="align-center" src="../../../../_images/closing-automatic-settings-example.png"/>
</div>

## Permitir a los clientes cerrar sus tickets

Si habilita **Cierre por clientes** , esto permitirá a los clientes cerrar sus
propios tickets cuando determinen que su problema se ha resuelto.

Primero vaya a Servicio de asistencia ‣ Configuración ‣ Equipos y seleccione
un equipo. En la página de configuración del equipo, vaya a la sección
**Autoservicio** y seleccione la casilla **Cierre por clientes**.

![Botón de cancelación por clientes en Servicio de
asistencia.](../../../../_images/closing-by-customer-setting.png)

Una vez activados los ajustes de cierre del ticket, el botón **Cerrar ticket**
será visible para los clientes cuando vean su ticket a través del portal de
clientes.

![Vista de cierre de ticket en Servicio de
asistencia](../../../../_images/closing-customer-view.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los clientes pueden ver sus tickets al hacer clic en el enlace <b>Ver el ticket</b> que reciben por correo electrónico. El enlace se incluye en la plantilla <b>Solicitud de confirmación</b> de forma predeterminada a la primera etapa de un equipo. Este enlace no requiere que el cliente tenga acceso al portal para ver o responder su ticket.</p>
<p>Los clientes con acceso al portal podrán ver sus tickets en Mi cuenta ‣ Tickets.</p>
</div>

