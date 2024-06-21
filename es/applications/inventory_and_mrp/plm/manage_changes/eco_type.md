# Tipo de ECO

A las _órdenes de cambio de ingeniería_ (ECO) se les asigna un _tipo de ECO_
para organizar y monitorear los cambios que se realizan a productos y listas
de materiales (LdM). Cada tipo de ECO separa los ECO en un proyecto en vista
de Gantt para asegurarnos que que los colaboradores y las partes interesadas
**solo** vean y asistan con las mejoras relevantes a la |LdM|.

Por ejemplo, un fabricador de chips electrónicos puede usar los tipos de ECO
“Introducción del nuevo producto”, “Mejora de producto”, “Cambio de
componente” y “Actualización de firmware”. Así, los diseñadores e ingenieros
se pueden enfocar en las ECO que estén en los proyectos “Introducción del
nuevo producto” y “Mejora de producto”, por lo que no verán los ECO de cambios
de proveedor o actualización de firmware, que no les interesan.

## Crear un tipo de ECO

Para acceder a y gestionar los tipos de ECO debe ir a la aplicación PLM ‣
Configuración ‣ Tipos de órdenes de cambio de ingeniería.

Haga clic en **Nuevo** para poder crear un nuevo tipo de orden de cambio de
ingeniería (ECO). En el nuevo formulario de **Tipos de órdenes de cambio de
ingeniería** , llene la siguiente información:

  * **Nombre** : el nombre del tipo de ECO que organizará todos los ECO de este _tipo_ en un proyecto.

  * **Alias de correo electrónico** : si se llena este campo opcional, los correos electrónicos que se envíen a esta dirección de correo harán que se generen ECO en la etapa más pegada a la izquierda de este tipo de ECO.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El tipo de <abbr title="Engineering Change Order">ECO</abbr> <code>Tipo de fórmula</code> se usa antes de organizar y rastrear los <abbr title="Engineering Change Order">ECO</abbr> relacionados en un solo proyecto. Si llena el campo <b>Dirección de correo</b> se generarán <abbr title="Engineering Change Order">ECO</abbr> en el proyecto <code>Cambio de fórmula</code> que se le envió a la dirección de correo, <code>pawlish-change@pawlished-glam.odoo.com</code>.</p>
<img alt="Ejemplo de un tipo de ECO." class="align-center" src="../../../../_images/create-eco-type.png"/>
</div>

## Editar tipo de ECO

Para modificar el nombre de tipos de ECO existentes y las direcciones de
correo vaya a la aplicación PLM ‣ Configuración ‣ Tipos de ECO. Ahí, haga clic
en el tipo de ECO deseado de la lista.

En el formulario de cada tipo de ECO edite los campos de **Nombre** y
**Seudónimo de correo electrónico**.

## Etapas

Dentro de un tipo de proyecto de ECO las _etapas_ son como objetivos y se usan
para identificar el progreso del ECO antes de que los cambios estén listos
para aplicarse (ejemplo, “Retroalimentación”, “En progreso”, “Aprobado”,
“Completado”).

Además, a cada etapa puede agregar personas responsables de la aprobación para
que se asegure que los cambios a la |LdM| en producción no se realicen sin que
antes de apruebe el ECO. Así evitamos que sucedan errores en la lista de
materiales en producción, pues al menos habrá una revisión sugerida antes de
que se apliquen los campos a la |LdM|.

Para las mejores prácticas, debe haber al menos una etapa de _verificación_ ,
que es una etapa en la que es necesario tener la aprobación. También debe
haver una etapa de _cierre_ , donde se guardan los ECO que se cancelaron o
aprobaron para usarlos en la siguiente |LdM| de producción.

### Crear etapa

Para agregar una etapa, vaya a la aplicación PLM y seleccione el proyecto para
un tipo de ECO desde el tablero **Información general de gestión de ciclo de
vida del producto**.

Después, en el flujo del proyecto **Órdenes de cambio de ingeniería** para
tipos de ECO, haga clic en el botón **\+ Etapa**. Así se mostrará un cuadro de
texto para ponerle nombre de la etapa. Después de ponerlo, haga clic en el
botón **Agregar** para terminar de agregar la etapa.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Aparecerá una nueva etapa llamada <code>Asignados</code> que separa los <abbr title="Engineering Change Order">ECO</abbr> de los que no están asignados en la etapa de <code>Nuevo</code>. Agregar una etapa nueva ayuda a que el gerente de producto pueda monitorear las tareas no asignadas.</p>
<img alt="Crear una nueva etapa en un proyecto para un tipo de ECO." class="align-center" src="../../../../_images/create-stage.png"/>
</div>

### Etapa de verificación

Haga clic en un tipo de ECO en la aplicación PLM ‣ Información general para
abrir la vista de kanban de los ECO de este tipo.

Para configurar una etapa de verificación, pase el ratón por la etapa deseada
y seleccione el icono **⚙️ (engranaje)**. Después, haga clic en **Editar**
para abrir una ventana emergente.

Configura la etapa de verificación en la ventana emergente de edición de la
etapa. Solo haga clic en la caja **Permitir aplicar cambios**.

Después, agregue una persona responsable de la aprobación en la sección
**Aprobadores** , haga clic en **Agregar una línea** y especifique la
**Función** del aprobador, el **Usuario** y el **Tipo de aprobación**.

Asegúrese de que se configuró al menos un aprobador en el **Tipo de
aprobación** : **Se requiere para aprobar**.

El aprobador enlistado recibe una notificación cuando los ECO llegan a la
etapa especificada en la ventana emergente. Una vez que termine, haga clic en
**Guardar y cerrar**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En el tipo de <abbr title="Engineering Change Order">ECO</abbr> <code>Introducción de producto nuevo</code> debe hacer clic en el icono <b>⚙️ (engranaje)</b> y luego hacer clic en <b>Editar</b> para configurar la etapa <code>Validada</code>. Así se abrirá la ventana emergente <b>Editar: validado</b>.</p>
<p>Si agregamos al <code>Gerente de ingeniería</code> como aprobador, solo los <abbr title="Engineering Change Order">ECO</abbr> que este usuario apruebe pueden pasar a la siguiente etapa y cambiar la <a href="#id9"><span class="problematic" id="id10">|lista de materiales|</span></a> en producción.</p>
<p>Además, marque la opción <b>Permitir aplicar cambios</b> para asegurar que el comportamiento sea el adecuado.</p>
<img alt="Imagen donde se muestra que la opción *Permitir aplicar cambios* está marcada." class="align-center" src="../../../../_images/verification-stage.png"/>
</div>

### Etapa de cierrre

Para configurar una etapa de cierre abra a la ventana emergente **Editar:
[etapa]**. Para hacerlo, pase el ratón encima de la etapa deseada y haga clic
en el icono **⚙️ (engranaje)** que aparece en la esquina superior derecha.
Después, haga clic en **Editar** en el menú desplegable.

En la ventana emergente **Editar: [etapa]** marque las opciones de **Plegado
en la vista de kanban** , **Permitir aplicar cambios** y **Etapa final**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La etapa de cierre, donde configuramos <code>Effectivo</code> marcando las opciones <b>Plegado en la vista de kanban</b>, <b>Permitir aplicar cambios</b> y <b>Etapa final</b>.</p>
</div> ![Imagen donde se muestra la configuración de la etapa de
cierre.](../../../../_images/closing-stage.png)

  *[ECO]: Engineering Change Order

