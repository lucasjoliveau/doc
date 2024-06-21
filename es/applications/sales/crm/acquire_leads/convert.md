# Convertir leads en oportunidades

Los _leads_ funcionan como pasos de calificación antes de crear una
oportunidad. Esto proporciona tiempo adicional antes de asignar una
oportunidad potencial a alguien del equipo de ventas.

## Configuración

Para activar la función de _leads_ , vaya a aplicación CRM ‣ Configuración ‣
Ajustes, seleccione la casilla con el nombre **Leads** y luego haga clic en
**Guardar**.

![Ajustes de leads en la página de configuración de
CRM.](../../../../_images/convert-leads-leads-setting.png)

Al activar esta función aparece el nuevo menú **Leads** en la barra ubicada en
la parte superior de la pantalla.

![Menú de leads en la aplicación CRM.](../../../../_images/convert-leads-
leads-menu.png)

Una vez habilitó la función de _leads_ , esta se aplica de forma
predeterminada a todos los equipos de ventas. Para desactivar los leads en un
equipo específico, vaya a la aplicación CRM ‣ Configuración ‣ Equipos de
ventas. Seleccione un equipo de la lista para abrir su registro, desmarque la
casilla **Leads** y luego haga clic en **Guardar**.

![Menú de leads en la aplicación CRM.](../../../../_images/convert-leads-
leads-button.png)

## Convierta un lead en una oportunidad

Para convertir un lead en una oportunidad, vaya a CRM ‣ Leads y haga clic en
un **lead** de la lista para abrirlo.

Haga clic en el botón **Convertir en oportunidad** que está ubicado en la
esquina superior izquierda de la pantalla. Esta acción abrirá la ventana
emergente correspondiente.

![Botón para crear oportunidad en el registro de un
lead.](../../../../_images/convert-leads-convert-opp-button.png)

En la ventana emergente **Convertir a oportunidad** seleccione la opción
**Convertir a oportunidad** en el campo **Acciones de conversión**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si ya existe un lead o una oportunidad en la base de datos para este cliente, de forma automática Konvergo ERP sugerirá fusionarlos. Para obtener más información sobre cómo fusionar leads y oportunidades, consulte la sección sobre cómo <a href="#sales-crm-acquire-leads-merge-leads"><span class="std std-ref">fusionar leads</span></a> a continuación.</p>
</div>

Luego, seleccione un **vendedor** y un **equipo de ventas** al que se debe
asignar la oportunidad.

Estos campos se completarán de forma automática con la información
correspondiente si el lead ya estaba asignado a un vendedor o a un equipo.

![Ventana emergente para convertir a
oportunidad.](../../../../_images/convert-leads-conversion-action.png)

Elija alguna de las siguientes opciones en la sección **Cliente** :

  * **Crear un nuevo cliente** : elija esta opción para usar la información del lead para crear un nuevo cliente.

  * **Vincular a un cliente existente** : para vincular esta oportunidad al registro de un cliente existente elija esta opción y luego seleccione uno del menú desplegable.

  * **No vincular a un cliente** : elija esta opción para convertir el lead, pero no vincularlo a un cliente nuevo o existente.

Por último, al completar todas las configuraciones, haga clic en **Crear
oportunidad**.

## Fusionar leads y oportunidades

Konvergo ERP detecta leads y oportunidades similares de forma automática al comparar
las direcciones de correo electrónico de los contactos asociados. En la parte
superior del registro del lead u oportunidad aparece un botón inteligente
**Lead similar** en caso de que encuentre uno parecido.

![El botón inteligente de leads similares.](../../../../_images/convert-leads-
similar-leads.png)

Haga clic en el botón **Leads similares** para comparar los detalles de los
leads y oportunidades parecidas. Esta acción abre una vista de kanban con que
solo muestra los leads y las oportunidades similares, haga clic en cada
tarjeta para ver los detalles correspondientes y confirme si deben fusionarse.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Al fusionar, Konvergo ERP prioriza el lead u oportunidad que se creó primero en el sistema y fusiona la información en donde se creó primero. Si fusiona un lead y una oportunidad el registro resultante se denomina oportunidad, sin importar lo que se creó primero.</p>
</div>

Después de confirmar que los leads y las oportunidades deben fusionarse
regrese a la vista de kanban con las migas de pan o haga clic en el botón
inteligente **Lead similar**. Haga clic en el icono **☰ (tres líneas
verticales)** para cambiar a la vista de lista.

Seleccione la casilla ubicada en el lado izquierdo de la página para los leads
y las oportunidades que se fusionarán. Luego, haga clic en el icono **Acción
⚙️ (engranaje)** que se encuentra la parte superior de la página para abrir el
menú desplegable y allí seleccione la opción **Fusionar** para fusionar las
oportunidades (o leads) que seleccionó.

Al seleccionar **Fusionar** en el menú desplegable **Acción ⚙️ (engranaje)**
aparece la ventana emergente **Fusionar**. Allí deberá **asignar oportunidades
a** un **vendedor** o a un **equipo de ventas**.

Debajo de esos campos aparecen los leads y las oportunidades a fusionar, así
como su información relacionada. Haga clic en **Fusionar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>No se pierde información al fusionar oportunidades. Los datos de la otra oportunidad se registran en el chatter y en los campos de información como referencia.</p>
</div> ![Opción para fusionar en el menú de acción desde la vista
de lista.](../../../../_images/convert-leads-merge.png)

