# Utilizar una caja IoT con un PdV

## Prerrequisitos

Antes de comenzar, asegúrese de que el siguiente equipo está disponible:

  * Una caja IoT con su adaptador de corriente.

  * Una computadora o tableta con un navegador web actualizado.

  * Odoo en línea o una instancia de Odoo con las aplicaciones _Punto de venta_ e _IoT_ instaladas.

  * Una red local configurada con un DHCP (esta es la configuración predeterminada).

  * Un cable ethernet RJ45 (opcional, pero tiene preferencia sobre Wi-Fi, que ya está incorporado).

  * Cualquier hardware compatible (impresora de recibos, lector de código de barras, caja registradora, terminal de pago, báscula, pantalla de cliente, etc.). Puede consultar la lista de hardware compatible en la [página de hardware de PdV](https://www.odoo.com/page/point-of-sale-hardware).

## Configurar

![../../../../_images/pos-connections.png](../../../../_images/pos-
connections.png)

Una configuración sugerida para un sistema de punto de venta.

Para conectar el hardware al PdV, el primer paso es conectar una caja IoT a la
base de datos. Para ello, siga estas instrucciones: [Conectar una caja de
internet de las cosas (IoT) a la base de datos de Odoo](connect.html).

Luego, conecte los dispositivos periféricos a la caja IoT.

Nombre del dispositivo | Instrucciones  
---|---  
Impresora | Conecte una impresora de recibos compatible a un puerto USB o a la red y enciéndala. Consulte [Impresión de órdenes](../../../sales/point_of_sale/restaurant/kitchen_printing.html).  
Caja registradora | La caja registradora debe estar conectada a la impresora con un cable RJ25.  
Lector de código de barras | Para que el lector de códigos de barras sea compatible debe terminar los códigos de barras con un carácter `ENTER` (código de clave 28). Es posible que esta sea la configuración predeterminada del lector de códigos de barras.  
Báscula | Conecte la báscula y enciéndala. Consulte [Conectar una báscula](../devices/scale.html).  
Pantalla del cliente | Conecte la pantalla a la caja IoT para mostrar la orden del PdV. Consulte [Conectar una pantalla](../devices/screen.html).  
Terminal de pago | El proceso de conexión depende de la terminal. Consulte la [documentación sobre terminales de pago](../../../sales/point_of_sale/payment_methods.html).  
  
Una vez que haya completado los pasos anteriores, conecte la caja IoT a la
aplicación Punto de venta. Vaya a Punto de venta ‣ Configuración ‣ PdV, marque
la opción Caja IoT, seleccione los dispositivos que se utilizarán en este PdV
y guarde los cambios.

![Configuración de los dispositivos conectados en la aplicación Punto de venta
de Odoo.](../../../../_images/iot-connected-devices.png)

Cuando todo esté configurado podrá iniciar una nueva sesión en el PdV.

  *[IoT]: Internet de las cosas
  *[DHCP]: Protocolo de configuración dinámica de host
  *[USB]: Bus serie universal
  *[PdV]: Punto de venta

