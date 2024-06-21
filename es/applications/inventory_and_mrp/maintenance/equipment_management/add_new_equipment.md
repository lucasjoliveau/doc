# Agregar equipo nuevo

En Konvergo ERP, un _equipo_ es cualquier artículo que se utilice en operaciones
cotidianas, esto incluye la fabricación de productos. Puede ser una máquina en
una línea de producción, una herramienta que se utiliza en varios lugares o
una computadora en una oficina. Los equipos registrados en Konvergo ERP pueden ser
propiedad de la empresa que utiliza la base de datos de Konvergo ERP, o de un tercero,
como un proveedor (en caso de alquilar los equipos).

Si usa la aplicación **Mantenimiento** de Konvergo ERP, puede realizar un seguimiento
de las partes individuales de un equipo junto con la información sobre sus
requisitos de mantenimiento. Para agregar un nuevo equipo, vaya al módulo de
**Mantenimiento** y seleccione Equipos ‣ Máquinas y herramientas ‣ Nuevo,
configure el equipo de la siguiente manera:

  * **Nombre del equipo** : el nombre de producto del equipo.

  * **Categoría del equipo** : la categoría a la que pertenece el equipo; por ejemplo, computadoras, maquinaria, herramientas, etc. También puede crear nuevas categorías, vaya a Configuración ‣ Categorías de equipo y haga clic en **Nuevo**.

  * **Empresa** : la empresa propietaria del equipo, puede ser la que utiliza la base de datos de Konvergo ERP o una empresa externa.

  * **Usado por** : especifique si un empleado específico, departamento, o ambos utilizan el equipo. Seleccione **Otro** si se comparte entre un empleado y un departamento.

  * **Equipo de mantenimiento** : el equipo responsable del mantenimiento del equipo. Puede crear nuevos equipos, vaya a Configuración ‣ Equipos de mantenimiento y seleccione **Nuevo**. Los miembros de cada equipo también se pueden asignar desde esta página.

  * **Técnico** : la persona responsable del mantenimiento del equipo. Esto puede utilizarse para asignar a una persona específica en caso de que no se asigne ningún equipo de mantenimiento o cuando un miembro específico del equipo asignado siempre sea responsable del equipo. Cualquier persona agregada a Konvergo ERP como usuario puede ser asignada como técnico.

  * **Usado en la ubicación** : la ubicación donde se utiliza el equipo. Este campo de texto simple se puede utilizar para especificar ubicaciones que no son centros de trabajo (por ejemplo, una oficina).

  * **Centro de trabajo** : especifique aquí si el equipo se utiliza en un centro de trabajo. El equipo también se puede asignar a un centro de trabajo, vaya a Mantenimiento ‣ Equipos ‣ Centros de trabajo y seleccione un centro de trabajo o cree uno con el botón **Nuevo** , luego haga clic en la pestaña **Equipo** en el formulario del centro de trabajo.

![Un ejemplo de un formulario de equipo nuevo configurado en su
totalidad.](../../../../_images/new-equipment-form.png)

## Incluir información adicional del producto

La pestaña **Información del producto** en la parte inferior del formulario se
puede utilizar para proporcionar más detalles sobre el equipo:

  * **Proveedor** : el proveedor al que se compró el equipo.

  * **Referencia del proveedor** : el código de referencia asignado al proveedor.

  * **Modelo** : el modelo específico del equipo.

  * **Número de serie** : el número de serie único del equipo.

  * **Fecha efectiva** : la fecha en que el equipo estuvo disponible para su uso, se utiliza para calcular el MTBF.

  * **Costo** : la cantidad por la que se compró el equipo.

  * **Fecha en la que expira la garantía** : la fecha en la que vence la garantía del equipo.

![La pestaña de información del producto para el nuevo
equipo.](../../../../_images/new-equipment-product-information.png)

## Agregar detalles de mantenimiento

La pestaña **Mantenimiento** incluye información que puede ser útil para los
equipos de mantenimiento:

  * **Frecuencia del mantenimiento preventivo** : especifica con qué frecuencia debe realizarse el mantenimiento para evitar fallas en el equipo.

  * **Duración de mantenimiento** : la cantidad de tiempo necesaria para reparar el equipo cuando falla.

  * **Tiempo medio esperado entre fallos** : la cantidad promedio de tiempo que se espera que el equipo funcione antes de fallar.

![La pestaña de mantenimiento para el nuevo equipo.](../../../../_images/new-
equipment-maintenance.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La pestaña de <b>mantenimiento</b> también incluye secciones para el <b>tiempo medio entre fallos</b>, <b>próximo fallo estimado</b>, <b>último fallo</b> y <b>tiempo medio de reparación</b>. Estos valores se calculan de forma automática según las solicitudes de mantenimiento, si las hay.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para ver las solicitudes de mantenimiento de un equipo, vaya a la página del equipo y seleccione <b>Mantenimiento</b> en la esquina superior derecha del formulario.</p>
</div>

  *[MTBF]: Tiempo medio entre fallos

