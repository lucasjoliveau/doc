# Órdenes de cambio de ingeniería

Utilice las _órdenes de cambio de ingeniería_ (_ECO)_ para monitorear,
implementar y quitar los cambios realizados a productos y [listas de
materiales](../../manufacturing/management/bill_configuration#manufacturing-
management-bill-configuration).

Estas son tres formas en las que puede crear órdenes de cambio de ingeniería:

  1. directamente en el tipo de ECO.

  2. si es un operador y desde la vista de tableta de una operación.

  3. automáticamente desde retroalimentación que haya enviado al [alias de correo electrónico del tipo de ECO](eco_type#plm-eco-eco-type).

## Crear una ECO

Para crear una |orden de cambio de ingeniería (ECO, por sus siglas en inglés)|
lo primero que tiene que hacer es ir a la aplicación _PLM_. Después,
seleccione la tarjeta de tipo de ECO que se usará para monitorear el progreso
de cambio. En la página **Órdenes de cambio de ingeniería** , haga clic en el
botón **Nuevo** que se encuentra en la esquina superior izquierda.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Aprenda a crear nuevos <a href="eco_type#plm-eco-eco-type"><span class="std std-ref">tipos de ECO</span></a> para categorizar y organizar órdenes de cambio. De esta manera, los empleados solo verán las <abbr title="Engineering Change Order">ECO</abbr> que se relacionan a sus responsabilidades, no importa si se trata de la introducción de un nuevo producto, actualizaciones específicas de las líneas de productos, o sobre el cumplimiento de la normativa.</p>
</div>

En el formulario de ECO, llene los siguientes campos como se indica:

  * **Descripción** es un resumen de la mejora.

  * **Tipo** : especifica el tipo de proyecto ECO para organizar las ECO.

  * **Aplicar en** determina si la ECO cambia la **Lista de materiales** o **Solo producto**.

  * **Producto** indica el producto que se mejorará.

  * **Lista de meteriales** indica la |LdM| que se cambió. Si el producto indicado en el campo **Producto** tiene una |LdM| existente, este campo se llenará automáticamente. Si existen varias |listas de materiales| seleccione las opciones que quiera en el menú desplegable.

  * **Empresa** este campo se usa en bases de datos multiempresa. Especifique si el cambio se aplica a productos de una empresa en específico, o déjelo en blanco si el cambio se aplica a todas las empresas.

  * **Responsable** es la persona a cargo de la ECO. (Opcional)

  * **Válida desde** este campo especifica cuándo empieza a ser válida la |orden de cambio de ingeniería|. Si se elige **Lo antes posible** significa que la |orden de cambio de ingeniería| se aplicará a la |lista de materiales| en producción tan pronto como un usuario autorizado aplique los cambios.

Por otro lado, si selecciona **En fecha** y especifica una fecha, tendrá una
fecha con la que será más fácil monitorear el historial de versiones de la
|lista de materiales|, y la fecha específica de la |lista de materiales|, que
se usan para producción.

  * Asignamos |etiquetas| a ECO para denotar la prioridad y organizarlas. Para crear una etiqueta nueva, escriba el nombre en el campo y seleccione **Crear** desde el menú desplegable. Esto es opcional.

Después de completar el formulario de la orden de cambio de ingeniería, haga
clic en el botón **Iniciar revisión** para comenzar a implementar los cambios.

Al hacer clic en **Iniciar revisión** , ocurrirán tres acciones:

  1. Aparecerá el botón inteligente **Documentos** , allí se almacenarán los archivos importantes de la lista de materiales.

  2. Se almacena una copia de la |lista de materiales| de producción en el nuevo botón inteligente **Revision** de la |orden de cambio de ingeniería|. También se asigna el siguiente número de versión disponible (por ejemplo, `V2`, `V3`, …) para realizar un seguimiento de todas las versiones de la |lista de materiales|.

  3. Las etapas de la |orden de cambio de ingeniería| **tipo** se muestran en la esquina superior derecha de la |orden de cambio de ingeniería|.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div> ![La orden de cambio de ingeniería con la vista general de
las etapas en la esquina superior derecha y el botón inteligente
*Revisión*.](../../../../_images/eco-form.png)

## Cambio de componentes

Si desea modificar los componentes de una |lista de materiales|, haga clic en
el botón inteligente **Revisión** en una |orden de cambio de ingeniería| para
acceder a la nueva versión de la |LdM|. Konvergo ERP puede diferenciar la versión de
no producción de la versión actual al marcar la versión de prueba con una
etiqueta grande con la leyenda **archivado**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Después de hacer clic en el botón <b>Comenzar revisión</b> de una <a href="#id38"><span class="problematic" id="id39">|orden de cambio de ingeniería|</span></a> para el producto, <code>[D_0045 Stool]</code>, realice cambios en la <a href="#id40"><span class="problematic" id="id41">|lista de materiales|</span></a> del producto al hacer clic en el botón inteligente <b>Revisión</b>. Cuando lo haga se abrirá la lista de materiales archivada, marcada con una etiqueta roja con la leyenda <b>archivado</b>.</p>
<img alt="Muestra de la lista de materiales archivada" class="align-center" src="../../../../_images/archived-bom.png"/>
</div>

Modifique la lista de componentes de la nueva |LdM|, para esto vaya a la
pestaña **Componentes** y cambie la **cantidad** de los componentes
existentes, puede añadir nuevos componentes al hacer clic en el botón **añadir
una línea** , y puede eliminar componentes con el icono **🗑️ (papelera)**.

<div class="alert alert-success" id="plm-eco-example-keyboard">
<p class="alert-title">
Example</p><p>En la versión dos de la <a href="#id44"><span class="problematic" id="id45">|LdM|</span></a> para el teclado, se redujeron las cantidades de componentes y se añadió un nuevo componente llamado <code>estabilizadores</code>.</p>
<img alt="Realice cambios en los componentes al acceder a la nueva lista de materiales con el botón inteligente *Revisión*." class="align-center" src="../../../../_images/version-2-bom.png"/>
</div>

### Comparar cambios

Una vez completados los cambios, vaya de nuevo a la |orden de cambio de
ingeniería| haciendo clic en `ECO00X` en las migas de pan situadas en la
esquina superior izquierda. En el formulario de la |orden de cambio de
ingeniería|, podrá ver una nueva pestaña llamada **Cambios en LdM** que
muestra las diferencias entre la |LdM| actual y la nueva versión.

El texto azul indica los nuevos componentes añadidos a la |LdM| revisada que
no están en la |LdM| de producción. El texto negro representa las
actualizaciones compartidas en ambas |listas de materiales|, mientras que el
texto rojo indica componentes eliminados en la |LdM| revisada.

Los cambios y las pruebas se encapsulan en la |LdM| revisada, y **no** afectan
a la |LdM| utilizada en producción. Al menos hasta que se apliquen los
cambios.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Consulte el resumen de las diferencias entre las <a href="#id64"><span class="problematic" id="id65">|listas de materiales|</span></a> del teclado actuales y revisadas en la pestaña <b>Cambios en LdM</b> de la <a href="#id66"><span class="problematic" id="id67">|orden de cambio de ingeniería|</span></a>.</p>
<img alt="Vea el resumen de los cambios de los componentes en la pestaña *Cambios en la LdM*." class="align-center" src="../../../../_images/bom-changes.png"/>
</div>

## Cambio de operaciones

Si desea modificar las operaciones de una |LdM|, haga clic en el botón
inteligente **Revisión** de una |orden de cambio de ingeniería| para acceder a
la nueva versión archivada de la |LdM|.

En la nueva versión de la |lista de materiales|, cambie a la pestaña
**operaciones** para ver y editar las operaciones de |LdM|. Para realizar
cambios, seleccione cada operación, esto abrirá la ventana emergente **Abrir:
operaciones** correspondiente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La pestaña <b>operaciones</b> no está disponible de forma predeterminada. Para activarla, vaya a la aplicación Fabricación ‣ Configuración ‣ Ajustes, y marque la casilla <b>Órdenes de trabajo</b>.</p>
</div>

Realice cambios en cualquiera de los campos de la ventana emergente **Abrir:
operaciones** y, a continuación, haga clic en **Guardar**.

Cree nuevas operaciones al hacer clic en el botón **Agregar línea** , y
elimine nuevas operaciones con el botón **Archivar operación**.

### Comparar cambios

Una vez completados los cambios, haga clic en `ECO00X` en las migas de pan
situadas en la esquina superior izquierda para ir de nuevo a la |orden de
cambio de ingeniería|.

En el formulario de la |orden de cambio de ingeniería| podrá ver una nueva
pestaña **Cambios de operación** muestra las diferencias entre la |LdM| de
producción actual y la nueva versión.

El texto azul indica las nuevas operaciones añadidas a la |LdM| revisada que
aún no existen en la |LdM| de producción. El texto negro representa
actualizaciones compartidas por ambas |listas de materiales|, mientras que el
texto rojo indica las operaciones eliminadas en la |LdM| revisada.

Las modificaciones de la |LdM| en una |orden de cambio de ingeniería| **no**
afectarán a la |LdM| utilizada en producción. Es decir, hasta que se apliquen
los cambios.

En la pestaña **Cambios de operación** , cada fila de detalles, debajo de las
columnas de la tabla, refleja la siguiente información:

  * **Operación** : Nombre de la operación que se modificó.

  * **Paso** : especifica el punto de control de calidad, visible cuando la operación incluye instrucciones detalladas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para revisar las instrucciones, haga clic en la línea de la operación en la pestaña <b>Operaciones</b> de una <a href="#id98"><span class="problematic" id="id99">|LdM|</span></a>. A continuación, en la ventana emergente <b>Abrir: operaciones</b>, busque el botón inteligente <b>Instrucciones</b> que aparece en la parte superior.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>El <code>ensamblaje</code> <b>Operación</b> incluye <code>10</code> <b>instrucciones</b> detalladas para completarlo.</p>
<img alt="Mostrar el botón inteligente *Instrucciones* para comprobar si una operación tiene instrucciones adicionales." class="align-center" src="../../../../_images/instructions-smart-button.png"/>
</div>

  * **Tipo de paso** detalla el tipo de control de calidad para más instrucciones en la operación.

  * **Tipo** corresponde al texto de color para especificar en qué difiere la |LdM| revisada de la |LdM| de producción. Los tipos de cambio de operación pueden ser **añadir** , **eliminar** o **actualizar**.

  * **Centro de trabajo** : especifica el centro de trabajo en el que se realiza la operación.

  * **Cambio manual de duración** se refiere al cambio en el campo **Duración predeterminada** de la ventana emergente **Abrir: operaciones** , que especifica el tiempo previsto para completar la operación.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La pestaña <b>cambios de operación</b> compara la producción de la <a href="#id104"><span class="problematic" id="id105">|LdM|</span></a> con la <a href="#id106"><span class="problematic" id="id107">|LdM|</span></a> revisada en la <a href="#id108"><span class="problematic" id="id109">|orden de cambio de ingeniería|</span></a>.</p>
<p>En la <a href="#id110"><span class="problematic" id="id111">|LdM|</span></a> revisada, se añade una nueva <b>Operación</b> de <code>ensamblaje</code> en la <code>línea de ensamblaje 1</code> del <code>centro de trabajo</code>. Además, la duración prevista de la operación es de <code>20.00</code> minutos, tal y como se especifica en la etiqueta <b>Cambio manual de duración</b>.</p>
<p>Para completar la operación de <code>ensamblaje</code>, se añaden dos instrucciones de puntos de control de calidad:</p>
<ol class="arabic simple">
<li><p>El primero es el <b>paso</b> <code>QCP00039</code>, un <b>tipo de paso</b> para <b>registrar la producción</b> de componentes.</p></li>
<li><p>El segundo <b>paso</b> es <code>QCP00034</code>, un <b>tipo de paso</b> de <code>instrucciones</code> que proporciona detalles adicionales de ensamblaje.</p></li>
</ol>
<img alt="Mostrar la pestaña *cambios de operación* en una |orden de cambio de ingeniería|." class="align-center" src="../../../../_images/operation-changes.png"/>
</div>

## Aplicar cambios

Después de verificar los cambios, mueva la |orden de cambio de ingeniería| a
una [etapa de verificación](eco_type#plm-eco-stage-config), estas etapas
requieren aprobación antes de que los cambios revisados se puedan aplicar a la
|orden de cambio de ingeniería| de producción.

Una vez que los aprobadores aceptan los cambios, verá el botón **aplicar
cambios**. Haga clic en él y la |orden de cambio de ingeniería| pasará
automáticamente a la fase de cierre. Una vez que se aplican los cambios, se
archivará la |LdM| de producción original, y la |LdM| revisada se convertirá
en la nueva |LdM| de producción.

### Verificar cambios

Puede verificar que los cambios están activos desde la |orden de cambio de
ingeniería| en la que hizo clic en el botón **aplicar cambios**. Vuelva a la
|LdM| revisada haciendo clic en el botón inteligente **Revisión**.

Ya no verá la etiqueta roja con la leyenda **archivado** en la |LdM| revisada.

Si desea comprobar los cambios, vaya a la aplicación Fabricación ‣ Productos ‣
Productos y seleccione el producto para ver la |LdM| de producción.

A continuación, en el formulario del producto, haga clic en el botón
inteligente **lista de materiales** y seleccione la |LdM| de la lista. En la
pestaña **Varios** de la |LdM|, el campo **Versión** se actualiza para
coincidir con el número de versión que aparece en el botón inteligente
**Revisión** de la última |orden de cambio de ingeniería|.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Después de aplicar los cambios de la <a href="#id138"><span class="problematic" id="id139">|orden de cambio de ingeniería|</span></a> para el <a href="#plm-eco-example-keyboard"><span class="std std-ref">teclado</span></a>, vea la versión de la <a href="#id140"><span class="problematic" id="id141">|LdM|</span></a> actual del teclado en la pestaña <b>varios</b>. Aquí, el número de <b>versión</b> se ha actualizado a <code>2</code>, que coincide con la <code>V2</code> que aparece en el botón inteligente <b>Revisión</b> de la <a href="#id142"><span class="problematic" id="id143">|orden de cambio de ingeniería|</span></a>.</p>
<img alt="Vista de la versión actual de la *LdM* en la pestaña Varios." class="align-center" src="../../../../_images/bom-version.png"/>
</div>

## Crear una orden de cambio de ingeniería desde la vista de tableta

Los operadores pueden sugerir directamente instrucciones de operación más
claras, mientras ejecutan órdenes de fabricación en la aplicación
_Fabricación_.

Si desea crear órdenes de fabricación de este modo, vaya a la aplicación
Fabricación ‣ Operaciones ‣ Órdenes de fabricación. A continuación, seleccione
la orden de fabricación) deseada y vaya a la pestaña **órdenes de trabajo**.
Después, haga clic en el icono **📱 (teléfono móvil)** de la orden de trabajo
deseada para abrir la _vista de tableta_ de la operación.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div>0 ![Busque el icono de tableta para cada operación, es el
segundo del extremo derecho.](../../../../_images/tablet-icon.png)

A continuación, añada un paso de instrucción, haga clic en el icono **☰ (tres
líneas horizontales)** en la vista de tableta de una operación. Al hacerlo, se
abrirá el **menú** de elementos de acción para una orden de fabricación.
Después haga clic en el botón **añadir un paso**.

![Abra la ventana emergente *añadir un paso* al hacer clic en el icono de las
tres líneas horizontales en la vista de
tableta.](../../../../_images/additional-options-menu.png)

Si hace clic en el botón, aparecerá la ventana emergente **añadir un paso** ,
donde se envían los cambios propuestos.

En el campo **Título** , escriba una breve descripción del paso. Luego, en el
campo de texto **Instrucción** , escriba las instrucciones del paso con más
detalle. De manera opcional, puede agregar una imagen en el campo
**Documento**. Una vez que está completo, haga clic en el botón **Proponer
cambios**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div>1

Con base en las entradas de la ventana emergente de **Agregar un paso** , se
creará una orden para cambio de ingeniería con la siguiente información:

  1. La **Descripción** es el nombre de la operación, seguido del número de referencia de la orden de fabricación.

  2. El **Tipo** de la orden para cambio de ingeniería se le asigna automáticamente a los `Cambios en la LdM`.

  3. Los campos de **Producto** y **Lista de materiales** se completan de manera automática de acuerdo con la LdM que se utilizó en la orden de fabricación.

  4. El **Responsable** es el operador que envió la retroalimentación.

### Ver orden para cambio de ingeniería

Para revisar los cambios propuestos, vaya a la Aplicación PLM ‣ Información
general. En la tarjeta `Actualizaciones de la lista de materiales`, el botón
**X Cambios de ingeniería** representa la cantidad de cambios operacionales
que se crearon dese la vista de tableta.

Haga clic en el botón de **X Cambios de ingeniería** para abrir la vista
kanban para ver el tipo de orden para cambio de ingeniería. Para ver la
sugerencia, seleccione una orden para cambio de ingeniería en etapa de
`Nuevo`.

En la orden para cambio de ingeniería, aparecerá un resumen de los cambios
propuestos en la pestaña **Cambios de operación**. Haga clic en el botón
inteligente de **Revisión** para ir a la lista de materiales editada y revise
los cambios propuestos con más detalle.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div>2

En la LdM actualizada, vaya a la pestaña **Operaciones** y seleccione el icono
**☰ (tres líneas horizontales)**. Al hacerlo, aparecerá una lista de **Pasos**
a seguir para la operación con la instrucción recientemente agregada llamada
`Sugerencia de nuevo paso:`, seguida del título que puso el usuario. Haga clic
en la línea para ver los cambios sugeridos.

![Icono "Mostrar instrucciones" en la pestaña *Operaciones* de una
LdM.](../../../../_images/show-instructions.png)

En el formulario de [punto de control de
calidad](../../quality/quality_management/quality_control_points#quality-
quality-management-quality-control-points) asegúrese de llenar los siguientes
campos para que los operadores cuenten con instrucciones detalladas:

  * **Título** : cambie el nombre para dar una descripción concisa de la nueva instrucción.

  * **Control por** : utilice el menú desplegable para determinar si esta instruccion aplica de manera general para todo el **Producto** , _solo_ para esta **Operación** en específico o para una **Cantidad** particular del producto.

  * **Tipo** : categoriza el tipo de punto de control. Desde el menú desplegable, seleccione las **Instrucciones** para aclararle las instrucciones al trabajador. Para que el trabajador pueda ingresar información, seleccione **Tomar una foto** , **Registrar materiales consumidos** , **Imprimir etiqueta** , u otras [opciones de control de calidad](../../quality/quality_management/quality_control_points#quality-quality-management-quality-control-points).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div>3

Una vez que el punto de calidad esté configurado, regrese a la lista de
**Pasos** usando las migas de pan. Finalmente, arrastre el último elemento de
la línea del control de calidad a su orden de instrucciones correspondiente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente <b>Revisión</b> estará disponible <b>solo</b> si selecciona la opción <b>lista de materiales</b> en el campo <b>aplicar en</b>, y se ha hecho clic en el botón <b>Comenzar revisión</b>.</p>
</div>4

  *[ECO]: Engineering Change Order

