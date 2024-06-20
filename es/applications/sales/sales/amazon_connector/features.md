# Funciones del Conector de Amazon

El _Conector de Amazon_ sincroniza órdenes entre Amazon y Odoo. Es una
herramienta muy útil, pues reduce bastante el tiempo que se utiliza para
ingresar de forma manual los pedidos de Amazon (desde la cuenta de vendedor de
Amazon) en Odoo. También permite que los usuarios lleven un seguimiento
preciso de las ventas de Amazon en Odoo.

## Funciones compatibles

El Conector de Amazon puede:

  * Sincronizar (de Amazon a Odoo) todas las órdenes confirmadas (tanto FBA como FBM) con sus respectivos artículos y la información correspondiente:

    * El nombre, descripción y cantidad del producto.

    * Los costos de envío del producto.

    * Los cargos por envoltura de regalo.

  * Crear cualquier usuario que haga falta relacionado con una orden en Odoo (tipos de contacto compatibles: contacto y dirección de entrega).

  * Notificar a Amazon con respecto a un envío confirmado en Odoo (FBM) con el fin de cobrar.

  * Tener varias cuentas de vendedor.

  * Tener varios Marketplace por cuenta de vendedor.

La siguiente tabla incluye algunas de las funciones que proporciona Odoo al
hacer uso del Conector de Amazon:

| Por Amazon (FBA) | Por el vendedor (FBM)  
---|---|---  
**Órdenes** | Sincroniza órdenes enviadas y canceladas. | Sincroniza órdenes sin enviar y canceladas.  
**Envío** | Amazon calcula el costo de envío, este se incluye en la orden sincronizada. | Amazon calcula el costo de envío, este se incluye en las órdenes sincronizadas.  
Amazon se encarga del envío. | Se crea una orden de entrega en Odoo de forma automática para cada orden nueva. Una vez que se haya procesado en Odoo, el estado se sincroniza en Amazon.  
**Envoltura de regalo** | Amazon se encarga de esta acción. | Amazon calcula el costo y lo incluye en la orden a sincronizar. El mensaje de regalo se agrega a una línea de la orden y en la orden de entrega. Luego, depende del usuario.  
**Gestión de existencias** | Amazon gestiona esta acción y se sincroniza con una ubicación virtual para llevar seguimiento en Odoo. | Odoo gestiona esto con la aplicación Inventario y se sincroniza con Amazon.  
**Notificaciones de entrega** | Amazon se encarga de esta acción. | Amazon hace el envío según el estado de entrega sincronizado desde Odoo.  
  
Nota

El Conector de Amazon está diseñado para sincronizar los datos de las órdenes.
Otras acciones, como descargar reportes de cuotas mensuales, gestionar
disputas o emitir reembolsos, se **deben** gestionar desde la _Seller Central_
de Amazon.

Advertencia

Desde el 19 de febrero de 2024, en los marketplaces norteamericanos, las
órdenes FBA creadas con el _conector de Amazon_ no incluyen el nombre del
cliente en la orden de entrega o de envío en Odoo. Esto se debe a que Amazon
ahora calcula y remite el impuesto sobre las ventas en nombre de los
vendedores. Es decir, la información personal identificable del cliente ya no
se le comparte al vendedor luego de una orden FBA.

## Marketplaces de Amazon compatibles

Si un marketplace de Amazon no aparece en la lista, es posible [agregar uno
nuevo](setup.html#amazon-add-new-marketplace).

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
  
Ver también

  * [Configuración del conector de Amazon](setup.html)

  * [Gestión de órdenes de Amazon](manage.html)

  *[FBA]: Logística por Amazon

