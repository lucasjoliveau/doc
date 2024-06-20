# Conectar una báscula

Puede conectar una báscula a la Caja IoT de una base de datos de Odoo en unos
cuantos pasos muy fáciles. Después de la configuración, puede usar la
aplicación _Punto de Venta_ para pesar productos, lo que resulta muy útil si
sus precios se calculan con base en su peso.

Importante

  * En los estados miembros de la UE [es legalmente obligatorio contar con una certificación](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG) para utilizar una báscula como dispositivo integrado.

  * Odoo no está certificado en varios países, incluyendo Francia, Alemania y Suiza. Si se encuentra en uno de estos países, todavía puede usar la escala sin integrarla a su base de datos de Odoo.

  * También puede obtener una báscula certificada _no integrada_ que imprima etiquetas certificadas, después podrá escanearlas a su base de datos de Odoo.

Ver también

[Directiva 2014/31/UE del Parlamento Europeo](https://eur-lex.europa.eu/legal-
content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)

## Conexión

Para vincular una báscula a una Caja IoT, conéctela con un cable USB.

Nota

En algunos casos, es posible que necesite un adaptador para puerto USB.

Si la báscula es [compatible con la Caja IoT de
Odoo](https://www.odoo.com/page/iot-hardware), no es necesario que configure
otra cosa porque Odoo la detectará automáticamente en cuanto la conecte.

![Detección automática de Caja IoT.](../../../../_images/iot-choice.png)

Es posible que en algunos casos sea necesario reiniciar la Caja IoT y
descargar los controladores de la báscula a la caja. Para actualizar los
controladores, vaya a la página de inicio de la Caja IoT y haga clic en Lista
de controladores. Luego, haga clic en Cargar controladores.

![Vista de los ajustes de la Caja IoT y la lista de
controladores.](../../../../_images/driver-list.png)

Si cargar los controladores no permite un buen funcionamiento de la báscula,
es posible que la báscula no sea compatible con la Caja IoT de Odoo. En este
caso, deberá usar una báscula diferente.

## Usar una báscula en el sistema del punto de venta (PdV)

Para usar la báscula en la aplicación _Punto de Venta_ , vaya a la aplicación
Punto de venta ‣ Menú de 3 puntos en el PdV ‣ Ajustes, luego active la función
de la Caja IoT. Después de que todo esté completo, puede configurar el
dispositivo de la báscula.

Seleccione la báscula desde el menú desplegable de Báscula electrónica. Luego
haga clic en Guardar para guardar los cambios.

![Lista de las herramientas externas que se pueden utilizarcon el PdV y la
Caja IoT.](../../../../_images/electronic-scale-feature.png)

La báscula ahora estará disponible en todas las sesiones de Punto de Venta. Si
un producto tiene establecido un precio de acuerdo a su peso, al hacer clic en
él en la pantalla del PdV, hará que aparezca la pantalla de la báscula, dónde
el cajero puede pesar el producto y agregar el precio correcto al carrito de
compra.

![Vista de tablero de la báscula electrónica cuando no se está pesando
nada.](../../../../_images/scale-view.png)

