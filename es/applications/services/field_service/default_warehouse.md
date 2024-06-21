# Almacén predeterminado del usuario

Puede que configurar un **almacén predeterminado** sea útil para los técnicos
de campo que mantienen sus suministros en su camioneta o aquellos que siempre
se reabastecen desde el mismo almacén. También permite a los trabajadores de
campo cambiar entre almacenes desde sus perfiles.

Los productos en las órdenes de venta creadas durante las intervenciones in
situ siempre se extraen del almacén predeterminado, de esta forma el
inventario se mantiene exacto.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../inventory_and_mrp/inventory">Inventario</a></p>
</div>

## Configuración

Para configurar el almacén predeterminado de un usuario debe activar la
función [ubicaciones de
almacenamiento](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations)
en la aplicación **Inventario** y también debe tener más de un almacén en su
base de datos.

Puede configurarlo para su perfil or para todos los usuarios.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations">Gestionar almacenes y ubicaciones</a></p>
</div>

### Para su perfil

Para configurar su almacén predeterminado, haga clic en su **icono de perfil**
en la esquina superior derecha de la pantalla, luego vaya a Mi perfil ‣
Preferencias ‣ Almacén predeterminado, después seleccione uno del menú
desplegable.

### Para todos los usuarios

Para configurar un almacén automático para un usuario en específico, vaya a
Ajustes ‣ Usuarios ‣ Gestionar usuarios, seleccione a un usuario, después vaya
a la pestaña **Preferencias**. Baje a la sección **Inventario** y seleccione
un almacén predeterminado del menú desplegable.

![Selección de un almacén predeterminado en el perfil de un
usuario.](../../../_images/user-default.png)

## Uso en las tareas de servicio externo

Ya que configuró un almacén predeterminado para un usuario, los materiales que
se usen para una orden de venta que esté relacionada con una tarea de trabajo
de campo saldrán de ese almacén en específico. Abra la orden de venta
relacionada, vaya a la pestaña **Más información** , luego baje a **Entrega**
, aquí podrá revisar que el almacén automático sea el correcto.

Ya que la tarea de trabajo de campo se marque como hecha, las existencias del
almacén se actualizarán de manera automática.

