# Cadena de suministro

  * [Inventario](inventory_and_mrp/inventory)
    * Gestión de productos
      * Reabastecimiento de producto
        * Elegir una estrategia de reabastecimiento
          * Terminología
            * [Reporte de reabastecimiento y reglas de reordenamiento](inventory_and_mrp/inventory/product_management/product_replenishment/strategies#replenishment-report-and-reordering-rules)
            * [Fabricación sobre pedido](inventory_and_mrp/inventory/product_management/product_replenishment/strategies#make-to-order)
          * Configuración
            * Reporte de reabastecimiento y reglas de reordenamiento
              * [Campos del reporte de reabastecimiento](inventory_and_mrp/inventory/product_management/product_replenishment/strategies#replenishment-report-fields)
          * [Ruta de fabricación sobre pedido (MTO)](inventory_and_mrp/inventory/product_management/product_replenishment/strategies#make-to-order-mto-route)
        * Reabastecer sobre pedido (MTO)
          * [Desarchivar la ruta de reabastecer sobre pedido (MTO)](inventory_and_mrp/inventory/product_management/product_replenishment/mto#unarchive-the-replenish-on-order-mto-route)
          * [Configurar un producto para usar la ruta MTO](inventory_and_mrp/inventory/product_management/product_replenishment/mto#configure-a-product-to-use-the-mto-route)
          * [Completar una orden de cliente utilizando la ruta MTO](inventory_and_mrp/inventory/product_management/product_replenishment/mto#fulfill-a-sales-order-using-the-mto-route)
        * Reglas de reabastecimiento
          * [Configurar productos con reglas de reabastecimiento](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#configure-products-for-reordering-rules)
          * [Crear nuevas reglas de reordenamiento](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#create-new-reordering-rules)
          * Activador
            * [Auto](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#auto)
            * [Manual](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#manual)
          * [Días de visibilidad](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#visibility-days)
          * [Ruta preferida](inventory_and_mrp/inventory/product_management/product_replenishment/reordering_rules#preferred-route)
        * Unidades de medida
          * [Configuración](inventory_and_mrp/inventory/product_management/product_replenishment/uom#configuration)
          * [Categorías de unidades de medida](inventory_and_mrp/inventory/product_management/product_replenishment/uom#units-of-measure-categories)
          * [Especificar las unidades de medida de un producto](inventory_and_mrp/inventory/product_management/product_replenishment/uom#specify-a-product-s-units-of-measure)
          * Conversión de unidades
            * [Comprar productos en la unidad de medida de compra](inventory_and_mrp/inventory/product_management/product_replenishment/uom#buy-products-in-the-purchase-uom)
            * [Reabastecimiento](inventory_and_mrp/inventory/product_management/product_replenishment/uom#replenishment)
            * [Vender en una UdM diferente](inventory_and_mrp/inventory/product_management/product_replenishment/uom#sell-in-a-different-uom)
      * Seguimiento de productos
        * Diferencia entre lotes y números de serie
          * [Activar lotes y números de serie](inventory_and_mrp/inventory/product_management/product_tracking/differences#enable-lots-serial-numbers)
          * [Cuándo usar lotes](inventory_and_mrp/inventory/product_management/product_tracking/differences#when-to-use-lots)
          * [Cuándo usar números de serie](inventory_and_mrp/inventory/product_management/product_tracking/differences#when-to-use-serial-numbers)
          * [Trazabilidad](inventory_and_mrp/inventory/product_management/product_tracking/differences#traceability)
        * Usar números de serie para rastrear productos
          * [Activar lotes y números de serie](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#enable-lots-serial-numbers)
          * Configurar el rastreo por número de serie en los productos
            * [Crear nuevos números de serie para productos que ya están en existencias.](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#create-new-serial-numbers-for-products-already-in-stock)
          * Gestionar números de serie de envíos y recepciones
            * Gestione los números de series en recepciones
              * [Usted mismo asigne números de serie](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#assign-serial-numbers-manually)
              * [Asigne números de serie de manera automática](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#assign-serial-numbers-automatically)
              * [Copiar y pegar los números de serie desde una hoja de cálculo](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#copy-paste-serial-numbers-from-a-spreadsheet)
            * [Gestionar números de serie en órdenes de entrega](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#manage-serial-numbers-on-delivery-orders)
          * [Gestionar números de serie para distintos tipos de operaciones](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#manage-serial-numbers-for-different-operations-types)
          * [Trazabilidad del número de serie](inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers#serial-number-traceability)
        * Números de lote
          * Configuración
            * [Activar lotes y números de serie](inventory_and_mrp/inventory/product_management/product_tracking/lots#enable-lots-serial-numbers)
            * [Rastrear por lotes](inventory_and_mrp/inventory/product_management/product_tracking/lots#track-by-lots)
          * Asignar lotes para envío y recepción
            * Al recibir
              * [Asignación manual](inventory_and_mrp/inventory/product_management/product_tracking/lots#manual-assignment)
              * [Copiar y pegar](inventory_and_mrp/inventory/product_management/product_tracking/lots#copy-and-paste)
            * [Sobre órdenes de entrega](inventory_and_mrp/inventory/product_management/product_tracking/lots#on-delivery-orders)
          * Gestión de lotes
            * [Modificar lotes](inventory_and_mrp/inventory/product_management/product_tracking/lots#modify-lot)
            * [Reservar el número de lote para un producto](inventory_and_mrp/inventory/product_management/product_tracking/lots#reserve-lot-number-for-a-product)
          * [Gestione lotes para diferentes tipos de operaciones](inventory_and_mrp/inventory/product_management/product_tracking/lots#manage-lots-for-different-operations-types)
          * Trazabilidad
            * [Reporte de trazabilidad](inventory_and_mrp/inventory/product_management/product_tracking/lots#traceability-report)
        * Fechas de vencimiento
          * [Activar las fechas de caducidad](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#enable-expiration-dates)
          * [Configure fechas de caducidad en productos](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#configure-expiration-dates-on-products)
          * [Configure fechas de caducidad al momento de recibir el producto con lotes y números de serie.](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#set-expiration-dates-on-receipts-with-lots-serial-numbers)
          * [Configurar fechas de caducidad en productos fabricados](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#set-expiration-dates-on-manufactured-products)
          * [Vender productos con fechas de caducidad](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#sell-products-with-expiration-dates)
          * Ver las fechas de caducidad para lotes y números de sere.
            * [Alertas de caducidad](inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates#expiration-alerts)
        * Paquetes
          * [Configuración](inventory_and_mrp/inventory/product_management/product_tracking/package#configuration)
          * Empacar artículos
            * [Operaciones detalladas](inventory_and_mrp/inventory/product_management/product_tracking/package#detailed-operations)
            * [Incluir en el paquete](inventory_and_mrp/inventory/product_management/product_tracking/package#put-in-pack)
          * [Tipo de paquete](inventory_and_mrp/inventory/product_management/product_tracking/package#package-type)
          * [Paquetes para varias órdenes](inventory_and_mrp/inventory/product_management/product_tracking/package#cluster-packages)
        * Empaquetado
          * [Configuración](inventory_and_mrp/inventory/product_management/product_tracking/packaging#configuration)
          * Crear embalajes
            * [Desde el formulario del producto](inventory_and_mrp/inventory/product_management/product_tracking/packaging#from-product-form)
            * [Desde la página de embalajes del producto](inventory_and_mrp/inventory/product_management/product_tracking/packaging#from-product-packagings-page)
          * [Aplicar empaquetados](inventory_and_mrp/inventory/product_management/product_tracking/packaging#apply-packagings)
    * Almacenes y almacenamiento
      * Gestión de inventario
        * Reabastecer desde otro almacén
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/inventory_management/resupply_warehouses#configuration)
          * [Establecer una ruta en un producto](inventory_and_mrp/inventory/warehouses_storage/inventory_management/resupply_warehouses#set-route-on-a-product)
        * Trasladar productos entre almacenes mediante reabastecimientos
          * [Configurar los almacenes para el reabastecimiento interalmacenes](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouse_replenishment_transfer#configure-warehouses-for-inter-warehouse-replenishment)
          * [Configurar productos para reabastecimientos interalmacenes](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouse_replenishment_transfer#configure-products-for-inter-warehouse-replenishment)
          * Reabastecer de un almacén a otro
            * [Procesar la orden de entrega](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouse_replenishment_transfer#process-the-delivery-order)
            * [Procesar la recepción](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouse_replenishment_transfer#process-the-receipt)
          * [Automatizar el reabastecimiento interalmacenes](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouse_replenishment_transfer#automate-inter-warehouse-replenishment)
        * Gestionar almacenes y ubicaciones
          * Terminología
            * [Almacén](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations#warehouse)
            * [Ubicación](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations#location)
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations#configuration)
          * [Crear un nuevo almacén](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations#create-a-new-warehouse)
          * [Crear una nueva ubicación](inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations#create-a-new-location)
        * Crear un segundo almacén
          * [Agregar inventario a un nuevo almacén](inventory_and_mrp/inventory/warehouses_storage/inventory_management/create_a_second_warehouse#add-inventory-to-a-new-warehouse)
        * Rutas y reglas push y pull
          * [Dentro del almacén](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#inside-the-warehouse)
          * [Reglas pull](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#pull-rules)
          * [Reglas push](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#push-rules)
          * Usar rutas y reglas
            * [Rutas preconfiguradas](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#pre-configured-routes)
            * Rutas personalizadas
              * [Reglas](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#rules)
          * [Flujo de ejemplo](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes#example-flow)
        * Ubicaciones
          * [Crear una nueva ubicación dentro de un almacén](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations#create-a-new-location-inside-a-warehouse)
          * [Crear jerarquías de ubicación](inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations#create-location-hierarchies)
        * Ajustes de inventario
          * Página de ajustes de inventario
            * [Crear un ajuste de inventario](inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products#create-an-inventory-adjustment)
          * [Conteo de productos](inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products#count-products)
          * Cambiar la frecuencia de los recuentos de inventario
            * [Planeación de recuentos de inventario grandes](inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products#plan-big-inventory-counts)
        * Conteo por ciclos
          * [Activar ubicaciones de inventario](inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts#activate-storage-locations)
          * [Cambiar la frecuencia del recuento de inventario por ubicación](inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts#change-inventory-count-frequency-by-location)
          * [Recuento de inventario por ubicación](inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts#count-inventory-by-location)
          * [Cambiar la frecuencia de los recuentos de todo el inventario](inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts#change-full-inventory-count-frequency)
        * Desechar inventario
          * [Desechar de las existencias](inventory_and_mrp/inventory/warehouses_storage/inventory_management/scrap_inventory#scrap-from-stock)
          * [Desechar en una recepción, traslado o entrega](inventory_and_mrp/inventory/warehouses_storage/inventory_management/scrap_inventory#scrap-from-a-receipt-transfer-or-delivery)
      * Valoración del inventario
        * Configuración de la valoración de inventario
          * [Tipos de contabilidad](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#types-of-accounting)
          * Configuración
            * [Metodo de costo](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#costing-method)
            * Valoración del inventario
              * [Cuenta de gastos](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#expense-account)
              * [Entrada y salida de existencias (solo automatizadas)](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#stock-input-output-automated-only)
          * [Reporte de la valoración del inventario](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#inventory-valuation-reporting)
        * Usar la valoración de inventario
          * Valoración automática de inventario
            * [Recibir un producto](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation#receive-a-product)
            * [Entregar un producto](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation#deliver-a-product)
          * Reporte de valoración de inventario
            * [Actualizar el precio unitario de un producto](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation#update-product-unit-price)
            * [Asientos contables de valoración de inventario](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation#inventory-valuation-journal-entries)
        * Integrar costos adicionales con productos (costos en destino)
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs#configuration)
          * Agregar costos a productos
            * [Recibir la factura de proveedor](inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs#receive-the-vendor-bill)
      * Opciones avanzadas
        * Consignación: compra y venta de mercancía sin que le pertenezca
          * [Activar la configuración de consignación](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock#enable-the-consignment-setting)
          * [Reciba (y almacene) inventario consignado](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock#receive-and-store-consignment-stock)
          * [Vender y entregar bienes consignados](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock#sell-and-deliver-consignment-stock)
          * Trazabilidad y reportes de las existencias consignadas
            * [Reportes de movimiento de productos](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock#product-moves-report)
            * [Reporte de existencias disponibles](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock#stock-on-hand-report)
        * Recolección por lotes
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/batch_transfers#configuration)
          * Crear traslados por lote
            * [Añadir un lote de la lista de traslados](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/batch_transfers#add-batch-from-transfers-list)
          * Procesar traslados en lote
            * [Crear orden parcial](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/batch_transfers#create-backorder)
          * [Procesar traslado por lote: aplicación Código de barras](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/batch_transfers#process-batch-transfer-barcode-app)
        * Procesar traslados por olas
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/wave_transfers#configuration)
          * [Agregar productos a la ola](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/wave_transfers#add-products-to-a-wave)
          * [Ver traslados por olas](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/wave_transfers#view-wave-transfers)
        * Organizar un cross-dock en un almacén
          * [Configuración](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cross_dock#configuration)
          * [Configurar productos con una ruta sin almacenaje intermedio](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cross_dock#configure-products-with-cross-dock-route)
        * Vender las existencias de varios almacenes mediante ubicaciones virtuales
          * [Crear una ubicación principal virtual](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/stock_warehouses#create-virtual-parent-location)
          * [Crear almacenes secundarios](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/stock_warehouses#create-child-warehouses)
          * [Vincular almacenes secundarios a las existencias virtuales](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/stock_warehouses#link-child-warehouses-to-virtual-stock)
          * [Establecer la ubicación virtual de existencias como «Vista»](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/stock_warehouses#set-virtual-stock-location-as-view)
          * [Ejemplos: vender productos de un almacén virtual](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/stock_warehouses#example-sell-products-from-a-virtual-warehouse)
        * Reglas de almacenamiento
          * Configuración
            * [Definir reglas de almacenamiento](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/putaway#define-putaway-rule)
            * [Prioridad de las reglas de almacenamiento](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/putaway#putaway-rule-priority)
          * Categorías de almacenamiento
            * [Configuración](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/putaway#id1)
            * [Definir categorías de almacenamiento](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/putaway#define-storage-category)
            * [Usar categorías de almacenamiento en reglas de almacenamiento](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/putaway#storage-categories-in-putaway-rules)
        * Estrategias de remoción (PEPS, UEPS, LIFO)
          * [¿Qué sucede dentro del almacén?](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#what-happens-inside-the-warehouse)
          * Funcionamiento de cada estrategia de remoción
            * [Primeras entradas, primeras salidas (PEPS)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#first-in-first-out-fifo)
            * [Últimas entradas, primeras salidas (UEPS)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#last-in-first-out-lifo)
            * [Primero en expirar, primero en salir (FEFO)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#first-expired-first-out-fefo)
          * Uso de las estrategias de remoción
            * [Ubicación más cercana](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#closest-location)
          * Utilizar estrategias de remoción
            * [PEPS (Primeras entradas, primeras salidas)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#fifo-first-in-first-out)
            * [UEPS (Últimas entradas, primeras salidas)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#lifo-last-in-first-out)
            * [FEFO (primero en expirar, primero en salir)](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/removal#fefo-first-expired-first-out)
        * Preparación de varios pedidos
          * Configuración
            * [Configuración de los paquetes](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cluster_picking#packages-setup)
          * [Creación de un lote de varios pedidos](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cluster_picking#create-cluster-batch)
          * Procesar lotes
            * [En Código de barras](inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cluster_picking#in-barcode)
    * Envío y recepción
      * Configuración y ajustes
        * Métodos de envío
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#configuration)
          * Agregar métodos de envío
            * [Precio fijo](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#fixed-price)
            * Por reglas
              * [Crear reglas de precios](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#create-pricing-rules)
              * [Calcular costos de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#calculate-delivery-cost)
            * [Recoger en tienda](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#pickup-in-store)
          * Agregar un envío
            * [Orden de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method#delivery-order)
        * Transportistas externos
          * Configuración
            * [Instalar conectores de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#install-shipping-connector)
            * [Método de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#delivery-method)
            * [Entorno de producción](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#production-environment)
            * [Configuración del almacén](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#warehouse-configuration)
            * [Peso del producto](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#product-weight)
          * Aplicar transportistas externos para envíos
            * [Orden de venta](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#sales-order)
            * [Orden de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#delivery-order)
          * Solución de problemas
            * [Registro de depuración](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper#debug-log)
        * Imprimir etiquetas de envío
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels#configuration)
          * Imprimir etiquetas de rastreo
            * [Agregar un envío en la cotización.](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels#add-shipping-on-quotation)
            * [Validar la orden de entrega](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels#validate-delivery-order)
        * Configuración de Sendcloud
          * Configuración en Sendcloud
            * [Crear una cuenta y activar transportistas](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#create-an-account-and-activate-carriers)
            * [Configuración del almacén](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#warehouse-configuration)
            * [Generar credenciales de Sendcloud](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#generate-sendcloud-credentials)
          * Configuración en Konvergo ERP
            * [Instalar el módulo Envío por Sendcloud](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#install-sendcloud-shipping-module)
            * [Configuración del conector de envío por Sendcloud](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#sendcloud-shipping-connector-configuration)
            * [Información de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#shipping-information)
          * [Generar etiquetas con Sendcloud](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#generate-labels-with-sendcloud)
          * Preguntas frecuentes
            * [El envío es demasiado pesado](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#shipment-is-too-heavy)
            * [Contratos de transportista](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#personal-carrier-contract)
            * [Medición del peso volumétrico](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#measuring-volumetric-weight)
            * [No es posible calcular la tarifa de envío](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping#unable-to-calculate-shipping-rate)
        * ¿Cómo obtener las credenciales de UPS para la integración con Konvergo ERP?
          * [Crear una cuenta UPS](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials#create-a-ups-account)
          * [Obtener una llave de acceso](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials#get-an-access-key)
        * ¿Cómo obtener las credenciales de DHL para la integración con Konvergo ERP?
          * [Obtener el identificador del sitio y la contraseña para países que no son Estados Unidos (Reino Unido y el resto del mundo)](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials#getting-siteid-and-password-for-countries-other-than-united-states-uk-and-rest-of-the-world)
          * [Obtener el identificador del sitio y la contraseña para los Estados Unidos](inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials#getting-siteid-and-password-for-united-states)
      * Operaciones diarias
        * Envíos entrantes y órdenes de entrega
          * Elegir el flujo de inventario adecuado para gestionar recepciones y entregas
            * [Flujo de un paso](inventory_and_mrp/inventory/shipping_receiving/daily_operations/shipments_deliveries#one-step-flow)
            * [Flujo de dos pasos](inventory_and_mrp/inventory/shipping_receiving/daily_operations/shipments_deliveries#two-step-flow)
            * [Flujo de tres pasos](inventory_and_mrp/inventory/shipping_receiving/daily_operations/shipments_deliveries#three-step-flow)
        * Procesar recepciones y entregas en un paso
          * [Configure el almacén](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step#configure-the-warehouse)
          * Recibir bienes directamente (1 paso)
            * [Crear una orden de compra](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step#create-a-purchase-order)
            * [Procesar la recepción](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step#process-the-receipt)
          * Entregar bienes directamente (1 paso)
            * [Crear una orden de venta](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step#create-a-sales-order)
            * [Procesar la entrega](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step#process-the-delivery)
        * Procesar recepciones y entregas en dos pasos
          * [Configure rutas multietapa](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#configure-multi-step-routes)
          * Procesar un recibo en dos pasos (entrada + inventario)
            * [Crear una orden de compra](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#create-a-purchase-order)
            * [Procesar la recepción](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#process-the-receipt)
            * [Procesar el traslado interno](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#process-the-internal-transfer)
          * Procesar una orden de envío en dos pasos (recolección + envío)
            * [Crear una orden de venta](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#create-a-sales-order)
            * [Procesar la recolección](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#process-the-picking)
            * [Procesar la entrega](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps#process-the-delivery)
        * Procesar recepciones en tres pasos
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps#configuration)
          * Recibir en 3 pasos (entrada + control de calidad + existencias)
            * [Crear una orden de compra](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps#create-a-purchase-order)
            * [Procesar una recepción](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps#process-a-receipt)
            * [Procesar un traslado a Control de calidad](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps#process-a-transfer-to-quality-control)
          * [Procesar un traslado a existencias](inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps#process-a-transfer-to-stock)
        * Procesar entregas en tres pasos
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps#configuration)
          * Entregar en 3 pasos (recolección, empaquetado y envío)
            * [Crear una orden de venta](inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps#create-a-sales-order)
            * [Procesar una recolección](inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps#process-a-picking)
            * [Procesar un empaquetado](inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps#process-a-packing)
            * [Procesar una entrega](inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps#process-a-delivery)
      * Opciones avanzadas
        * Fechas de los envíos planeados
          * [Tipos de plazos de entrega](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#lead-time-types)
          * Plazos de entrega para ventas
            * [Plazo de entrega para el cliente](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#customer-lead-time)
            * [Plazo de entrega de seguridad para ventas](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#sales-security-lead-time)
            * [Entregar varios productos](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#deliver-several-products)
          * Plazos de entrega para compras
            * [Plazo de entrega del proveedor](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#vendor-lead-time)
            * [Plazo de entrega seguro para compras](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#purchase-security-lead-time)
          * Plazos de entrega de fabricación
            * [Plazo de fabricación](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#manufacturing-lead-time)
            * [Plazo seguro de fabricación](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#manufacturing-security-lead-time)
          * [Ejemplo general](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/scheduled_dates#global-example)
        * Facturación del costo de envío
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing#configuration)
          * [Agregar métodos de envío](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing#add-shipping-method)
          * [Facturar costo en la orden de venta](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing#invoice-cost-on-sales-order)
          * [Facturar los precios de envío reales](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing#invoice-real-shipping-costs)
        * Envío en varios paquetes
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack#configuration)
          * [Enviar artículos en varios paquetes](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack#ship-items-in-multiple-packages)
          * [Crear una orden parcial con los artículos a enviar después](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack#create-a-backorder-for-items-to-be-shipped-later)
        * Cambiar el tamaño de la etiqueta de envío
          * [Información general](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/label_type#overview)
          * [Configuración](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/label_type#configuration)
          * [Crear una orden de venta](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/label_type#create-a-sales-order)
          * [Etiquetas de ejemplo](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/label_type#example-labels)
        * Uso de triangulación de envíos para enviar de proveedores a clientes
          * [Configurar productos para realizar una triangulación de envío](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/dropshipping#configure-products-to-be-dropshipped)
          * [Completar órdenes mediante el uso de triangulación de envíos](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/dropshipping#fulfill-orders-using-dropshipping)
        * ¿Cómo cancelar una solicitud de envío a un transportista?
          * [Información general](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel#overview)
          * [¿Cómo cancelar una solicitud de envío?](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel#how-to-cancel-a-shipping-request)
          * [¿Cómo enviar una solicitud de envío después de cancelar una?](inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel#how-to-send-a-shipping-request-after-cancelling-one)
  * [Fabricación](inventory_and_mrp/manufacturing)
    * Flujos de trabajo de fabricación
      * Lista de materiales
        * Configurar una lista de materiales (LdM)
          * [Establezca una lista de materiales (LdM) para una variante de producto](inventory_and_mrp/manufacturing/management/bill_configuration#specify-a-bill-of-materials-bom-for-a-product-variant)
        * [Crear operaciones](inventory_and_mrp/manufacturing/management/bill_configuration#set-up-operations)
        * [Agregar subproductos a una lista de materiales (LdM)](inventory_and_mrp/manufacturing/management/bill_configuration#add-by-products-to-a-bill-of-materials-bom)
      * Gestionar listas de materiales para variantes de productos
        * [Activar variantes de producto](inventory_and_mrp/manufacturing/management/product_variants#activate-product-variants)
        * [Crear atributos personalizados para productos](inventory_and_mrp/manufacturing/management/product_variants#create-custom-product-attributes)
        * [Agregar las variantes de producto al formulario](inventory_and_mrp/manufacturing/management/product_variants#add-product-variants-on-the-product-form)
        * [Aplicar componentes de LdM a las variantes de producto](inventory_and_mrp/manufacturing/management/product_variants#apply-bom-components-to-product-variants)
        * Vender y fabricar variantes de productos de la lista de materiales
          * [Vender variantes de productos de la lista de materiales](inventory_and_mrp/manufacturing/management/product_variants#sell-variant-of-bom-product)
          * [Fabricar variantes de productos de la lista de materiales](inventory_and_mrp/manufacturing/management/product_variants#manufacture-variant-of-bom-product)
      * Usar kits
        * [Crear un kit como producto](inventory_and_mrp/manufacturing/management/kit_shipping#create-the-kit-as-a-product)
        * [Configurar la LdM para un kit](inventory_and_mrp/manufacturing/management/kit_shipping#set-up-the-kit-bom)
        * Usar kits para gestionar LdM complejas
          * [Estructura y costo](inventory_and_mrp/manufacturing/management/kit_shipping#structure-cost)
      * Gestionar productos semielaborados
        * [Configurar productos semielaborados](inventory_and_mrp/manufacturing/management/sub_assemblies#configure-semi-finished-products)
        * [Crear la lista de materiales (LdM) del nivel superior](inventory_and_mrp/manufacturing/management/sub_assemblies#create-the-top-level-bill-of-materials-bom)
        * [Gestionar la planificación de producción](inventory_and_mrp/manufacturing/management/sub_assemblies#manage-production-planning)
      * Subcontratar la fabricación
        * [Configuración](inventory_and_mrp/manufacturing/management/subcontracting#configuration)
        * [Flujo básico de subcontratación](inventory_and_mrp/manufacturing/management/subcontracting#basic-subcontracting-flow)
        * [Valoración del inventario](inventory_and_mrp/manufacturing/management/subcontracting#inventory-valuation)
        * [Trazabilidad](inventory_and_mrp/manufacturing/management/subcontracting#traceability)
        * Automatizar el reabastecimiento para los subcontratistas
          * [Reabastecimiento manual](inventory_and_mrp/manufacturing/management/subcontracting#manual-replenishment)
      * Utilizar el programa maestro de producción
        * [Configuración](inventory_and_mrp/manufacturing/management/use_mps#configuration)
        * [Calcule su demanda e inicie el reabastecimiento](inventory_and_mrp/manufacturing/management/use_mps#estimate-your-demand-and-launch-replenishment)
        * Significado del color de las celdas
          * [¿Qué pasa si subestimé la demanda?](inventory_and_mrp/manufacturing/management/use_mps#what-if-i-have-underestimated-the-demand)
          * [¿Y si sobrestimé la demanda?](inventory_and_mrp/manufacturing/management/use_mps#what-if-i-have-overestimated-the-demand)
          * [¿Qué pasa si me equivoco y agrego un producto que no debería ir en el programa maestro de producción?](inventory_and_mrp/manufacturing/management/use_mps#what-if-i-wrongly-added-a-product-to-the-mps)
      * Gestionar órdenes de trabajo usando los centros de trabajo
        * Crear un centro de trabajo
          * [Establezca estándares para la productividad del centro de trabajo](inventory_and_mrp/manufacturing/management/using_work_centers#set-standards-for-work-center-productivity)
          * [Asignar equipo a un centro de trabajo](inventory_and_mrp/manufacturing/management/using_work_centers#assign-equipment-to-a-work-center)
          * [Integración de dispositivos IoT](inventory_and_mrp/manufacturing/management/using_work_centers#integrate-iot-devices)
        * [Caso de uso: configure un centro de trabajo alternativo](inventory_and_mrp/manufacturing/management/using_work_centers#use-case-configure-an-alternative-work-center)
        * [Monitoree el rendimiento del centro de trabajo](inventory_and_mrp/manufacturing/management/using_work_centers#monitor-work-center-performance)
      * Desactivar centros de trabajo mediante la aplicación Tiempo personal
        * [Configuración](inventory_and_mrp/manufacturing/management/work_center_time_off#configuration)
        * [Utilizar la función tiempo personal en un centro de trabajo](inventory_and_mrp/manufacturing/management/work_center_time_off#add-time-off-for-a-work-center)
        * [Envie órdenes a un centro de trabajo alterno](inventory_and_mrp/manufacturing/management/work_center_time_off#route-orders-to-an-alternative-work-center)
      * Desechar durante la fabricación
        * [Desechar componentes de fabricación](inventory_and_mrp/manufacturing/management/scrap_manufacturing#scrap-manufacturing-components)
        * [Componentes de desecho vistos desde una tableta](inventory_and_mrp/manufacturing/management/scrap_manufacturing#scrap-components-from-tablet-view)
        * [Desechar productos terminados](inventory_and_mrp/manufacturing/management/scrap_manufacturing#scrap-finished-products)
      * Fabricar órdenes parciales
        * [Crear una orden parcial de fabricación](inventory_and_mrp/manufacturing/management/manufacturing_backorders#create-a-manufacturing-backorder)
        * Crear una orden parcial desde la vista de tableta
          * [Una sola orden de trabajo](inventory_and_mrp/manufacturing/management/manufacturing_backorders#single-work-order)
          * [Varias órdenes de trabajo](inventory_and_mrp/manufacturing/management/manufacturing_backorders#multiple-work-orders)
      * Configuración del producto a fabricar
        * [Activar la ruta de fabricación](inventory_and_mrp/manufacturing/management/configure_manufacturing_product#activate-the-manufacture-route)
        * [Configurar una lista de materiales (LdM)](inventory_and_mrp/manufacturing/management/configure_manufacturing_product#configure-a-bill-of-materials-bom)
      * Dividir y fusionar órdenes de fabricación
        * [Dividir órdenes de fabricación](inventory_and_mrp/manufacturing/management/split_merge#split-manufacturing-orders)
        * [Fusionar órdenes de fabricación](inventory_and_mrp/manufacturing/management/split_merge#merge-manufacturing-orders)
      * Dependencias de la orden de trabajo
        * [Configuración](inventory_and_mrp/manufacturing/management/work_order_dependencies#configuration)
        * [Añadir dependencias a la lista de materiales](inventory_and_mrp/manufacturing/management/work_order_dependencies#add-dependencies-to-bom)
        * Planificar órdenes de trabajo con dependencias
          * [Planeación por centro de trabajo](inventory_and_mrp/manufacturing/management/work_order_dependencies#planning-by-workcenter)
      * Fabricación en dos pasos
        * [Crear una orden de fabricación](inventory_and_mrp/manufacturing/management/two_step_manufacturing#create-manufacturing-order)
        * [Proceso de traslado de componentes de recolección](inventory_and_mrp/manufacturing/management/two_step_manufacturing#process-pick-components-transfer)
        * Proceso de orden de fabricación
          * [Flujo básico](inventory_and_mrp/manufacturing/management/two_step_manufacturing#basic-workflow)
          * [Flujo en vista de tableta](inventory_and_mrp/manufacturing/management/two_step_manufacturing#tablet-view-workflow)
      * Fabricación en un paso
        * [Crear una orden de fabricación](inventory_and_mrp/manufacturing/management/one_step_manufacturing#create-manufacturing-order)
        * Proceso de orden de fabricación
          * [Flujo básico](inventory_and_mrp/manufacturing/management/one_step_manufacturing#basic-workflow)
          * [Flujo en vista de tableta](inventory_and_mrp/manufacturing/management/one_step_manufacturing#tablet-view-workflow)
      * Fabricación en tres pasos
        * [Crear una orden de fabricación](inventory_and_mrp/manufacturing/management/three_step_manufacturing#create-manufacturing-order)
        * [Proceso de traslado de componentes de recolección](inventory_and_mrp/manufacturing/management/three_step_manufacturing#process-pick-components-transfer)
        * Proceso de orden de fabricación
          * [Flujo básico](inventory_and_mrp/manufacturing/management/three_step_manufacturing#basic-workflow)
          * [Flujo en vista de tableta](inventory_and_mrp/manufacturing/management/three_step_manufacturing#tablet-view-workflow)
        * [Proceso de traslado de productos terminados](inventory_and_mrp/manufacturing/management/three_step_manufacturing#process-finished-product-transfer)
    * Taller
      * Información general de Taller
        * Navegación
          * Página «todos»
            * [Tarjeta de información de la orden de fabricación](inventory_and_mrp/manufacturing/shop_floor/shop_floor_overview#mo-information-card)
          * Páginas de los centros de trabajo
            * [Panel de información de la orden de trabajo](inventory_and_mrp/manufacturing/shop_floor/shop_floor_overview#work-order-information-card)
          * [Panel de operador](inventory_and_mrp/manufacturing/shop_floor/shop_floor_overview#operator-panel)
  * [Compra](inventory_and_mrp/purchase)
    * Productos
      * Configurar reglas de reordenamiento
        * [Configure productos para abastecerlos](inventory_and_mrp/purchase/products/reordering#configure-products-for-reordering)
        * [Agregue una regla de abastecimiento a un producto](inventory_and_mrp/purchase/products/reordering#add-a-reordering-rule-to-a-product)
        * [Active manualmente las reglas de abastecimiento usando el planificador](inventory_and_mrp/purchase/products/reordering#manually-trigger-reordering-rules-using-the-scheduler)
        * [Gestione las reglas de abastecimiento](inventory_and_mrp/purchase/products/reordering#manage-reordering-rules)
      * Compre en unidades de medida diferentes a las de venta
        * [Habilitar las unidades de medida](inventory_and_mrp/purchase/products/uom#enable-units-of-measure)
        * Especificar las unidades de medida de compra y venta
          * [Unidades de medida estándar](inventory_and_mrp/purchase/products/uom#standard-units-of-measure)
          * [Crear nuevas unidades y categorías de medida.](inventory_and_mrp/purchase/products/uom#create-new-units-of-measure-and-units-of-measure-categories)
    * Gestionar ofertas
      * Utilice las órdenes abiertas para crear contratos de compra con los proveedores
        * [Crear una nueva orden abierta](inventory_and_mrp/purchase/manage_deals/blanket_orders#create-a-new-blanket-order)
        * [Crear una nueva solicitud de cotización a partir de una orden abierta.](inventory_and_mrp/purchase/manage_deals/blanket_orders#create-a-new-rfq-from-the-blanket-order)
        * [Crear una orden abierta desde una solicitud de cotización](inventory_and_mrp/purchase/manage_deals/blanket_orders#create-a-new-blanket-order-from-an-rfq)
        * [Órdenes abiertas y reabastecimiento](inventory_and_mrp/purchase/manage_deals/blanket_orders#blanket-orders-and-replenishment)
      * Cree solicitudes de cotización alternas para varios proveedores.
        * [Configure los ajustes de los contratos de compra](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#configure-purchase-agreement-settings)
        * [Crear una solicitud de cotización](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#create-an-rfq)
        * [Crear alternativas a una solicitud de cotización](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#create-alternatives-to-an-rfq)
        * [Vincular una nueva solicitud de cotización a cotizaciones existentes.](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#link-a-new-rfq-to-existing-quotations)
        * [Compare líneas de producto](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#compare-product-lines)
        * [Cancele (o guarde) alternativas](inventory_and_mrp/purchase/manage_deals/calls_for_tenders#cancel-or-keep-alternatives)
      * Políticas de control de facturación
        * Configuración
          * [Flujo de ejemplo: cantidades ordenadas](inventory_and_mrp/purchase/manage_deals/control_bills#example-flow-ordered-quantities)
          * [Flujo de ejemplo: cantidades recibidas](inventory_and_mrp/purchase/manage_deals/control_bills#example-flow-received-quantities)
        * Conciliación de tres vías
          * [Pagar las facturas de proveedor con la conciliación de tres vías](inventory_and_mrp/purchase/manage_deals/control_bills#pay-vendor-bills-with-3-way-matching)
        * [Ver el estado de facturación de una orden](inventory_and_mrp/purchase/manage_deals/control_bills#view-a-purchase-order-s-billing-status)
      * Gestionar facturas de proveedor
        * Políticas de control de facturación
          * [Conciliación de tres vías](inventory_and_mrp/purchase/manage_deals/manage#way-matching)
        * Crear y gestionar facturas de proveedor al recibir productos
          * [Con la política de control de facturas establecida sobre cantidades ordenadas.](inventory_and_mrp/purchase/manage_deals/manage#with-the-bill-control-policy-set-to-ordered-quantities)
          * [Con la política de control de facturas establecida sobre cantidades recibidas](inventory_and_mrp/purchase/manage_deals/manage#with-the-bill-control-policy-set-to-received-quantities)
        * [Crear y gestionar facturas de proveedor desde Contabilidad](inventory_and_mrp/purchase/manage_deals/manage#create-and-manage-vendor-bills-in-accounting)
        * [Facturación por lotes](inventory_and_mrp/purchase/manage_deals/manage#batch-billing)
    * Avanzado
      * Analice el rendimiento de sus compras
        * Generar reportes personalizados
          * Uso de filtros para seleccionar los datos necesarios
            * [Añadir filtros personalizados](inventory_and_mrp/purchase/advanced/analyze#add-custom-filters)
          * Seleccionar las medidas deseadas
            * [Visualizar datos](inventory_and_mrp/purchase/advanced/analyze#visualize-your-data)
            * [Analizar datos](inventory_and_mrp/purchase/advanced/analyze#explore-your-data)
  * [Código de barras](inventory_and_mrp/barcode)
    * Configuración
      * Configuración del escáner de código de barras
        * [Tipos de escáner](inventory_and_mrp/barcode/setup/hardware#scanner-types)
        * Configuración
          * [Distribución del teclado](inventory_and_mrp/barcode/setup/hardware#keyboard-layout)
          * [Retorno de carro automático](inventory_and_mrp/barcode/setup/hardware#automatic-carriage-return)
          * [Escáner Zebra](inventory_and_mrp/barcode/setup/hardware#zebra-scanner)
      * Activar los códigos de barras en Konvergo ERP
        * [Configuración](inventory_and_mrp/barcode/setup/software#configuration)
        * [Establecer códigos de barras de productos](inventory_and_mrp/barcode/setup/software#set-product-barcodes)
        * [Establecer códigos de barras de ubicaciones](inventory_and_mrp/barcode/setup/software#set-locations-barcodes)
        * [Formatos de código de barras](inventory_and_mrp/barcode/setup/software#barcode-formats)
    * Operaciones diarias
      * Aplicar ajustes de inventario con códigos de barra
        * [Activar la aplicación Código de barras](inventory_and_mrp/barcode/operations/adjustments#enable-barcode-app)
        * [Realizar un ajuste de inventario](inventory_and_mrp/barcode/operations/adjustments#perform-an-inventory-adjustment)
        * [Agregar productos al ajuste de inventario de forma manual](inventory_and_mrp/barcode/operations/adjustments#manually-add-products-to-inventory-adjustment)
      * Procesar recepciones y entregas con códigos de barras
        * [Activar la aplicación Código de barras](inventory_and_mrp/barcode/operations/receipts_deliveries#enable-barcode-app)
        * [Escanear códigos de barras para recepciones](inventory_and_mrp/barcode/operations/receipts_deliveries#scan-barcodes-for-receipts)
        * [Escanear códigos de barra para órdenes de entrega](inventory_and_mrp/barcode/operations/receipts_deliveries#scan-barcodes-for-delivery-orders)
      * Cree y procese las transferencias con código de barras
        * [Activar la aplicación Código de barras](inventory_and_mrp/barcode/operations/transfers_scratch#enable-barcode-app)
        * Escanear códigos de barra para transferencias internas
          * [Crear un traslado interno](inventory_and_mrp/barcode/operations/transfers_scratch#create-an-internal-transfer)
          * [Escanear los códigos de barras para transferencias internas](inventory_and_mrp/barcode/operations/transfers_scratch#scan-barcodes-for-internal-transfer)
        * [Crear una transferencia desde cero](inventory_and_mrp/barcode/operations/transfers_scratch#create-a-transfer-from-scratch)
      * Información general
        * Crear una nomenclatura de código de barras
          * [Configure su producto](inventory_and_mrp/barcode/operations/barcode_nomenclature#configure-your-product)
          * [Tipos de reglas](inventory_and_mrp/barcode/operations/barcode_nomenclature#rule-types)
      * Nomenclatura de código de barras GS1
        * [Configurar una nomenclatura de código de barras](inventory_and_mrp/barcode/operations/gs1_nomenclature#set-up-barcode-nomenclature)
        * Uso de los códigos de barras GS1 en Konvergo ERP
          * [Creación de reglas](inventory_and_mrp/barcode/operations/gs1_nomenclature#create-rules)
        * [Solución de problemas en códigos de barras](inventory_and_mrp/barcode/operations/gs1_nomenclature#barcode-troubleshooting)
        * [Lista de nomenclatura GS1](inventory_and_mrp/barcode/operations/gs1_nomenclature#gs1-nomenclature-list)
      * Uso del código de barras GS1
        * Configuración de códigos de barras por producto, cantidad y lotes
          * [Configuración](inventory_and_mrp/barcode/operations/gs1_usage#configuration)
          * [Escanear el código de barras de un producto al recibirlo](inventory_and_mrp/barcode/operations/gs1_usage#scan-barcode-on-receipt)
        * Configuración de códigos de barras para productos y cantidades sin unidad
          * [Escanear el código de barras de un producto al recibirlo](inventory_and_mrp/barcode/operations/gs1_usage#id1)
        * [Verificar los movimientos de productos](inventory_and_mrp/barcode/operations/gs1_usage#verify-product-moves)
  * [Calidad](inventory_and_mrp/quality)
    * Principios básicos de los controles de calidad
      * Puntos de control de calidad
        * [Configure los puntos de control de calidad](inventory_and_mrp/quality/quality_management/quality_control_points#configure-quality-control-points)
      * Crear alertas de calidad
        * [Encuentre y llene el formulario de las alertas de calidad](inventory_and_mrp/quality/quality_management/quality_alerts#find-and-fill-out-the-quality-alerts-form)
        * [Agregue alertas de calidad durante el proceso de fabricación](inventory_and_mrp/quality/quality_management/quality_alerts#add-quality-alerts-during-the-manufacturing-process)
        * [Gestione alertas de calidad existentes](inventory_and_mrp/quality/quality_management/quality_alerts#manage-existing-quality-alerts)
      * Controles de calidad
        * [Control de calidad manual](inventory_and_mrp/quality/quality_management/quality_checks#manual-quality-check)
        * Procesar un control de calidad
          * [Página del control de calidad](inventory_and_mrp/quality/quality_management/quality_checks#quality-check-page)
          * [Control de calidad en la orden](inventory_and_mrp/quality/quality_management/quality_checks#quality-check-on-order)
          * [Control de calidad en una orden de trabajo](inventory_and_mrp/quality/quality_management/quality_checks#quality-check-on-work-order)
    * Tipos de control de calidad
      * Control de calidad con instrucciones
        * Procesar un control de calidad de tipo instrucciones
          * [Proceso desde la página del control de calidad](inventory_and_mrp/quality/quality_check_types/instructions_check#process-from-the-quality-check-s-page)
          * [Procesar control de calidad en una orden](inventory_and_mrp/quality/quality_check_types/instructions_check#process-quality-check-on-an-order)
          * [Procesamiento de un control de calidad en una orden de trabajo](inventory_and_mrp/quality/quality_check_types/instructions_check#process-work-order-quality-check)
      * Control de calidad tipo aprueba o falla
        * Crear un control de calidad tipo Aprobar - Fallar
          * [Control de calidad](inventory_and_mrp/quality/quality_check_types/pass_fail_check#quality-check)
          * [Punto de control de calidad](inventory_and_mrp/quality/quality_check_types/pass_fail_check#quality-control-point-qcp)
        * Control de calidad tipo Aprobar - Fallar
          * [Desde la página de controles](inventory_and_mrp/quality/quality_check_types/pass_fail_check#from-the-check-s-page)
          * [En una orden](inventory_and_mrp/quality/quality_check_types/pass_fail_check#on-an-order)
          * [En una orden de trabajo](inventory_and_mrp/quality/quality_check_types/pass_fail_check#on-a-work-order)
      * Control de calidad de medición
        * Crear un control de calidad de Medida
          * [Control de calidad](inventory_and_mrp/quality/quality_check_types/measure_check#quality-check)
          * [Punto de control de calidad](inventory_and_mrp/quality/quality_check_types/measure_check#quality-control-point-qcp)
        * Procesar un control de calidad tipo Medida
          * [Desde la página de controles](inventory_and_mrp/quality/quality_check_types/measure_check#from-the-check-s-page)
          * [En una orden](inventory_and_mrp/quality/quality_check_types/measure_check#on-an-order)
          * [En una orden de trabajo](inventory_and_mrp/quality/quality_check_types/measure_check#on-a-work-order)
      * Control de calidad tipo tomar una foto
        * Crear el control de calidad “Tomar una foto”
          * [Control de calidad](inventory_and_mrp/quality/quality_check_types/picture_check#quality-check)
          * [Punto de control de calidad](inventory_and_mrp/quality/quality_check_types/picture_check#quality-control-point-qcp)
        * Procesar un control de calidad tipo Tomar una foto
          * [Desde la página de controles](inventory_and_mrp/quality/quality_check_types/picture_check#from-the-check-s-page)
          * [En una orden](inventory_and_mrp/quality/quality_check_types/picture_check#on-an-order)
          * [En una orden de trabajo](inventory_and_mrp/quality/quality_check_types/picture_check#on-a-work-order)
        * [Revisar una imagen adjunta a un control de calidad](inventory_and_mrp/quality/quality_check_types/picture_check#review-a-picture-attached-to-a-check)
  * [Mantenimiento](inventory_and_mrp/maintenance)
    * Gestión de equipos
      * Agregar equipo nuevo
        * [Incluir información adicional del producto](inventory_and_mrp/maintenance/equipment_management/add_new_equipment#include-additional-product-information)
        * [Agregar detalles de mantenimiento](inventory_and_mrp/maintenance/equipment_management/add_new_equipment#add-maintenance-details)
  * [Gestión del ciclo de vida del producto](inventory_and_mrp/plm)
    * Gestión de cambio
      * Órdenes de cambio de ingeniería
        * [Crear una ECO](inventory_and_mrp/plm/manage_changes/engineering_change_orders#create-eco)
        * Cambio de componentes
          * [Comparar cambios](inventory_and_mrp/plm/manage_changes/engineering_change_orders#compare-changes)
        * Cambio de operaciones
          * [Comparar cambios](inventory_and_mrp/plm/manage_changes/engineering_change_orders#id1)
        * Aplicar cambios
          * [Verificar cambios](inventory_and_mrp/plm/manage_changes/engineering_change_orders#verify-changes)
        * Crear una orden de cambio de ingeniería desde la vista de tableta
          * [Ver orden para cambio de ingeniería](inventory_and_mrp/plm/manage_changes/engineering_change_orders#view-eco)
      * Tipo de ECO
        * [Crear un tipo de ECO](inventory_and_mrp/plm/manage_changes/eco_type#create-eco-type)
        * [Editar tipo de ECO](inventory_and_mrp/plm/manage_changes/eco_type#edit-eco-type)
        * Etapas
          * [Crear etapa](inventory_and_mrp/plm/manage_changes/eco_type#create-stage)
          * [Etapa de verificación](inventory_and_mrp/plm/manage_changes/eco_type#verification-stage)
          * [Etapa de cierrre](inventory_and_mrp/plm/manage_changes/eco_type#closing-stage)
      * Control de versiones
        * [Versión actual de la LdM](inventory_and_mrp/plm/manage_changes/version_control#current-bom-version)
        * [Historial de la versión](inventory_and_mrp/plm/manage_changes/version_control#version-history)
        * Archivos de diseño
          * [Gestione archivos de diseño en una orden para cambio de ingeniería](inventory_and_mrp/plm/manage_changes/version_control#manage-design-files-in-an-eco)
        * [Aplicar transferencia de base](inventory_and_mrp/plm/manage_changes/version_control#apply-rebase)
    * Gestión de proyectos
      * Aprobaciones
        * [Agregar un aprobador](inventory_and_mrp/plm/management/approvals#add-approver)
        * Gestionar aprobaciones
          * [Aprobar órdenes de cambio de ingeniería](inventory_and_mrp/plm/management/approvals#approve-ecos)
          * Actividades automatizadas
            * [Actividades de seguimiento](inventory_and_mrp/plm/management/approvals#follow-up-activities)

