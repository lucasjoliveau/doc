# Configuración del escáner de código de barras

Siga esta guía para elegir y configurar un escáner de códigos de barras que
sea compatible con las aplicaciones _Inventario_ y _Código de barras_.

![Imagen de un ejemplo de un escáner de código de
barras.](../../../../_images/barcode-scanner.png)

Imagen de un ejemplo de un escáner de código de barras.

## Tipos de escáner

Antes de configurar un escáner de código de barras, es importante determinar
que tipo de escáner se adapta mejor a las necesidades del negocio. Hay tres
tipos principales, cada uno con sus propios beneficios y casos de uso:

  * Los **escáneres USB** están conectados a una computadora y son adecuados para negocios que escanean sus productos desde una ubicación fija, como la caja de un supermercado. Asegúrese de que el escáner USB que elija sea compatible con la distribución del teclado de su computadora.

  * Los **Escáneres Bluetooth** se pueden emparejar con un teléfono inteligente o un tableta, lo que los convierte en la opción portable ideal y con el mejor costo-eficacia para escanear códigos de barras. En este escenario, Konvergo ERP se instala en el teléfono y de esa manera los operadores de los almacenes pueden trabajar y revisar las existencias directamente desde sus dispositivos móviles.

  * Los **Escáneres móviles de computadora** son dispositivos móviles que incluyen un escáner de código de barras. Primero, asegúrese que el dispositivo puede ejecutarse correctamente en la aplicación móvil de Konvergo ERP. Los módulos más recientes que usan Android OS con el navegador de Google Chrome, o Windows OS con Microsoft Edge, deben funcionar. Sin embargo, es importante que realice pruebas debido a la variedad de modelos disponibles y su configuración.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/app/inventory-hardware">Hardware compatible con Inventario de Konvergo ERP</a></p>
</div>

## Configuración

Al configurar el escáner de código de barras, asegúrese de que todo esté
correcto para que el escáner pueda interpretar adecuadamente los códigos de
barras con Konvergo ERP.

### Distribución del teclado

Al usar un escáner de código de barras USB, la distribución del teclado debe
coincidir con la del sistema operativo para poder interpretar los caracteres
de forma correcta. De manera general, el modo de escaneo debe estar
configurado para aceptar un teclado USB (HID) con el lenguaje configurado
según el teclado que utilice.

Para configurar la distribución del teclado para un escáner **Zebra** ,
escanee el código de barras que se encuentra en el teclado para el lenguaje
que desee en el manual de usuario del escáner.

![Ejemplo del manual de usuario para el acomodo del
teclado.](../../../../_images/keyboard-barcode.png)

Ejemplos de ajustes de lenguaje del teclado en el manual de usuario de Zebra.

### Retorno de carro automático

Konvergo ERP cuenta con una espera predeterminada de 100 milisegundos entre escaneos
para prevenir el doble escaneado accidental. Si desea sincronizarse con el
escáner de código de barras, configúrelo para que incluya un _retorno de
carro_ (un caracter como la tecla «Enter» en el teclado) después de cada
escaneo. Konvergo ERP interpreta el retorno de carro como el fin de la entrada del
código de barras, entonces Konvergo ERP acepta el escaneo y espera al siguiente.

Por lo general en el escáner está incluido un retorno de carro de forma
predeterminada. Escanee un código de barras específico del manual del usuario,
como `CR suffix ON` o `Apply Enter for suffix`, para asegurarse de que está
configurado.

### Escáner Zebra

Al usar los escáneres Zebra, asegúrese de que los ajustes de las siguientes
pulsaciones estén activas para prevenir errores.

Comience en la pantalla de inicio del escáner Zebra y seleccione la aplicación
**DataWedge** (el icono de la aplicación es un código de barras azul claro).
En la página de **Perfiles de DataWedge** , seleccione la opción para acceder
a los ajustes del escáner.

Diríjase hacia abajo a la opción **Salida del teclado** y asegúrese de que la
opción **Habilitar/deshabilitar la salida de pulsaciones de tecla** esté
**habilitada**.

![Aspecto de la opción de pulsación en la aplicación DataWedge para el escáner
Zebra.](../../../../_images/enable-keystroke.png)

Regrese a la página de opciones de **Perfil** y seleccione **Opciones para
eventos clave**. Asegúrese de que la opción **Enviar caracteres como eventos**
esté habilitada.

