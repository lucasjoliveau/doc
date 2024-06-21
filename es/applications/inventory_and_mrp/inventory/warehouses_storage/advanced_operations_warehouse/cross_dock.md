# Organizar un cross-dock en un almacén

El cruce de andén (o cross-docking) es el proceso de enviar productos que se
reciben directamente al cliente, sin hacer que ingresen a las existencias. Los
camiones descargan en un área _sin almacenaje intermedio_ con el fin de
reorganizar productos y cargar otro camión.

![../../../../../_images/cross1.png](../../../../../_images/cross1.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para obtener más información sobre cómo organizar su almacén, consulte nuestro blog: <a href="https://www.odoo.com/blog/business-hacks-1/post/what-is-cross-docking-and-is-it-for-me-270">¿Qué es cross-docking y es lo que necesita?</a></p>
</div>

## Configuración

En la aplicación _Inventario_ , abra Configuración ‣ Ajustes y active las
_Rutas multietapa_.

![../../../../../_images/cross2.png](../../../../../_images/cross2.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Hacer esto también habilitará la función <em>Ubicaciones de almacenamiento</em>.</p>
</div>

Debe configurar los envíos _entrantes_ y _salientes_ para que funcionen con 2
pasos. Para adaptar la configuración, vaya a Inventario ‣ Configuración ‣
Almacenes y edite su almacén.

![../../../../../_images/cross3.png](../../../../../_images/cross3.png)

Esta modificación le llevará a la creación de una ruta _sin almacenaje
intermedio_ que puede encontrar en Inventario ‣ Configuración ‣ Rutas.

![../../../../../_images/cross4.png](../../../../../_images/cross4.png)

## Configurar productos con una ruta sin almacenaje intermedio

Cree el producto que utiliza la _ruta sin almacenaje intermedio_ y en la
pestaña de Inventario seleccione las rutas _Comprar_ y _Sin almacenaje
intermedio (cross dock)_. En la pestaña de compra especifique el proveedor de
quien compra el producto y establezca su precio.

![../../../../../_images/cross5.png](../../../../../_images/cross5.png)
![../../../../../_images/cross6.png](../../../../../_images/cross6.png)

Una vez hecho esto, cree una orden de venta para el producto y confírmela.
Konvergo ERP, en automático, creará dos traslados y se vincularán a la orden de venta.
El primer traslado es de la _ubicación de entrada_ a la _ubicación de salida_
, el cual corresponde al movimiento del producto en el área de _cross dock_.
El segundo es la orden de entrega de la _ubicación de salida_ a la _ubicación
de cliente_. Ambos están en el estado _En espera de otra operación_ porque aún
debemos ordenar el producto de nuestro proveedor.

![../../../../../_images/cross7.png](../../../../../_images/cross7.png)
![../../../../../_images/cross8.png](../../../../../_images/cross8.png)

Vaya a la aplicación _Compra_ , ahí encontrará la orden de compra que el
sistema activó de forma automática. Valídela y reciba los productos en la
_ubicación de entrada_.

![../../../../../_images/cross9.png](../../../../../_images/cross9.png)
![../../../../../_images/cross10.png](../../../../../_images/cross10.png)

Cuando haya recibido los productos del proveedor, puede regresar a su orden de
venta inicial y validar el traslado interno de _entrada_ a _salida_.

![../../../../../_images/cross11.png](../../../../../_images/cross11.png)
![../../../../../_images/cross12.png](../../../../../_images/cross12.png)

La orden de entrada está lista para procesarse y también se puede validar.

![../../../../../_images/cross13.png](../../../../../_images/cross13.png)
![../../../../../_images/cross14.png](../../../../../_images/cross14.png)

