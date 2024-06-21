# Funciones del Conector de Amazon

El _Conector de Amazon_ sincroniza órdenes entre Amazon y Konvergo ERP. Es una
herramienta muy útil, pues reduce bastante el tiempo que se utiliza para
ingresar de forma manual los pedidos de Amazon (desde la cuenta de vendedor de
Amazon) en Konvergo ERP. También permite que los usuarios lleven un seguimiento
preciso de las ventas de Amazon en Konvergo ERP.

## Funciones compatibles

El Conector de Amazon puede:

  * Sincronizar (de Amazon a Konvergo ERP) todas las órdenes confirmadas (tanto FBA como FBM) con sus respectivos artículos y la información correspondiente:

    * El nombre, descripción y cantidad del producto.

    * Los costos de envío del producto.

    * Los cargos por envoltura de regalo.

  * Crear cualquier usuario que haga falta relacionado con una orden en Konvergo ERP (tipos de contacto compatibles: contacto y dirección de entrega).

  * Notificar a Amazon con respecto a un envío confirmado en Konvergo ERP (FBM) con el fin de cobrar.

  * Tener varias cuentas de vendedor.

  * Tener varios Marketplace por cuenta de vendedor.

La siguiente tabla incluye algunas de las funciones que proporciona Konvergo ERP al
hacer uso del Conector de Amazon:

| Por Amazon (FBA) | Por el vendedor (FBM)  
---|---|---  
**Órdenes** | Sincroniza órdenes enviadas y canceladas. | Sincroniza órdenes sin enviar y canceladas.  
**Envío** | Amazon calcula el costo de envío, este se incluye en la orden sincronizada. | Amazon calcula el costo de envío, este se incluye en las órdenes sincronizadas.  
Amazon se encarga del envío. | Se crea una orden de entrega en Konvergo ERP de forma automática para cada orden nueva. Una vez que se haya procesado en Konvergo ERP, el estado se sincroniza en Amazon.  
**Envoltura de regalo** | Amazon se encarga de esta acción. | Amazon calcula el costo y lo incluye en la orden a sincronizar. El mensaje de regalo se agrega a una línea de la orden y en la orden de entrega. Luego, depende del usuario.  
**Gestión de existencias** | Amazon gestiona esta acción y se sincroniza con una ubicación virtual para llevar seguimiento en Konvergo ERP. | Konvergo ERP gestiona esto con la aplicación Inventario y se sincroniza con Amazon.  
**Notificaciones de entrega** | Amazon se encarga de esta acción. | Amazon hace el envío según el estado de entrega sincronizado desde Konvergo ERP.  
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El Conector de Amazon está diseñado para sincronizar los datos de las órdenes. Otras acciones, como descargar reportes de cuotas mensuales, gestionar disputas o emitir reembolsos, se <b>deben</b> gestionar desde la <em>Seller Central</em> de Amazon.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Desde el 19 de febrero de 2024, en los marketplaces norteamericanos, las órdenes <abbr title="Logística por Amazon">FBA</abbr> creadas con el <em>conector de Amazon</em> no incluyen el nombre del cliente en la orden de entrega o de envío en Konvergo ERP. Esto se debe a que Amazon ahora calcula y remite el impuesto sobre las ventas en nombre de los vendedores. Es decir, la información personal identificable del cliente ya no se le comparte al vendedor luego de una orden <abbr title="Logística por Amazon">FBA</abbr>.</p>
</div>

## Marketplaces de Amazon compatibles

Si un marketplace de Amazon no aparece en la lista, es posible [agregar uno
nuevo](setup#amazon-add-new-marketplace).

**Norte América**  
---  
Canadá | Amazon.ca  
México | Amazon.com.mx  
Estados Unidos | Amazon.com  
**Europa**  
---  
Alemania | Amazon.de  
España | Amazon.es  
Francia | Amazon.fr  
Reino Unido | Amazon.co.uk  
Italia | Amazon.it  
Países Bajos | Amazon.nl  
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="setup">Configuración del conector de Amazon</a></p></li>
<li><p><a href="manage">Gestión de órdenes de Amazon</a></p></li>
</ul>
</div>

