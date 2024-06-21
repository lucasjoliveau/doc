# Crear alertas de calidad

Configurar puntos de control de calidad es una excelente manera de garantizar
que el control de calidad se haga en etapas rutinarias durante operaciones
específicas. Sin embargo, los problemas de calidad pueden aparecer
frecuentemente fuera de esos controles programados. Al usar _Calidad_ de Konvergo ERP,
los usuarios pueden crear alertas por problemas de calidad que se detectaron
durante el proceso automatizado.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="quality_control_points">Agregar puntos de control de calidad</a></p>
</div>

## Encuentre y llene el formulario de las alertas de calidad

En algunas situaciones es necesario crear manualmente las alertas de calidad
dentro del módulo _Calidad_.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un usuario que recibe un ticket de un cliente notificando un defecto en un producto puede crear una alerta para avisar al equipo de calidad correspondiente.</p>
</div>

Para crear una nueva alerta de calidad, vaya al módulo Calidad y seleccione
Control de calidad ‣ Alertas de calidad ‣ Crear. La alerta de calidad se puede
llenar de la siguiente manera:

  * **Título** : elija un título claro y descriptivo para la alerta de calidad.

  * **Producto** : el producto sobre el cual se crea la alerta de calidad

  * **Variante de producto** : la variante específica del producto que tiene un problema de calidad, solo si aplica

  * **Lote** : el número de lote que tiene asignado el producto

  * **Centro de trabajo** : el centro de trabajo donde se originó el problema de calidad

  * **Recolección** : la operación de recolección durante la cual se originó el problema de calidad

  * **Equipo** : el equipo de calidad al que se le enviará la alerta

  * **Responsable** : la persona responsable de gestionar la alerta de calidad

  * **Etiquetas** : clasifique la alerta de calidad con base en etiquetas creadas por el usuario

  * **Causa** : la causa del problema de calidad, si se sabe

  * **Prioridad** : asigne la prioridad entre uno y tres estrellas para garantizar que los problemas urgentes tengan prioridad

Las pestañas al final del formulario se pueden usar para proporcionar
infromación adicional a los equipos de calidad:

  * **Descripción** : proporcione detalles adicionales sobre el problema de calidad

  * **Acciones correctivas** : el método para arreglar los productos afectados

  * **Acciones preventivas** : procedimientos para prevenir que el problema vuelva a ocurrir

  * **Otro** : el proveedor del producto (si aplica), la empresa que produce el producto y la fecha asignada.

![Un ejemplo de un formulario de alerta de calidad configrado en su totalidad
](../../../../_images/quality-alert-form.png)

## Agregue alertas de calidad durante el proceso de fabricación

Konvergo ERP le permite a los empleados de fabricación crear alertas de calidad en una
orden de trabajo sin tener que acceder al módulo _Calidad_. Desde la vista de
tableta de una orden de trabajo, haga clic en el **☰** icono de menú tipo
hamburguesa en la esquina superior izquierda y seleccione **Alerta de
calidad**.

![Acceda al menú de la orden de trabajo ](../../../../_images/work-order-
tablet-view-menu-button.png)

El formulario de las alertas de calidad se pueden llenar tal como se detalló
en la sección anterior. Después de guardar el formulario, aparecerá una nueva
alerta en el tablero de **Alertas de calidad** al que puede acceder desde el
menú Calidad ‣ Control de calidad.

## Gestione alertas de calidad existentes

De manera predeterminada, las alertas de calidad están organizadas en una
vista kanban. Las etapas del tablero kanban son totalmente configurables y las
alertas se pueden mover de una etapa a otra arrastrando y soltando, o desde
cada alerta. Otras opciones adicionales disponibles para ver las alertas
incluyen las vistas de gráficos, calendario, y tablas dinámicas.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Filtre las alertas según diferentes criterios como la fecha asignada o la fecha finalizada. Las alertas también se pueden agrupar según el equipo de calidad, causa u otros parámetros que puede encontrar en el botón del menú <b>Filtros</b> .</p>
</div>

