# Divisas extranjeras

Con Konvergo ERP, puede usar las listas de precios para gestionar sus precios en
varias divisas extranjeras. Konvergo ERP le permite trabajar con un total de 167
divisas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para utilizar varias divisas en la aplicación <em>Ventas</em> de Konvergo ERP también <b>debe</b> tener instalada la aplicación <em>Contabilidad</em>.</p>
</div>

## Ajustes

Una vez que haya instalado la aplicación _Contabilidad_ podrá agregar divisas
extranjeras a la base de datos. Vaya a la aplicación Contabilidad ‣
Configuración ‣ Ajustes, diríjase a la sección de **Divisas** y busque la
función **Divisa principal**.

![Visualización de la función de divisa principal en la página de ajustes en
la aplicación Contabilidad de Konvergo ERP.](../../../../../_images/main-currency-
setting-page.png)

De forma automática, Konvergo ERP establece la divisa principal como la moneda del
país en el que se encuentra la empresa.

Para cambiar la divisa principal de la empresa, vaya al menú desplegable del
campo **Divisa** , elija la divisa correspondiente y asegúrese de **guardar**
los cambios.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para asegurarse de que las tasas de cambio se actualicen de forma automática, habilite la función de <em>tasas de cambio automáticas</em> en la página de ajustes de <em>Contabilidad</em>. Vaya a la aplicación Contabilidad ‣ Configuración ‣ Ajustes ‣ sección de Divisas.</p>
<img alt="Visualización de la función de divisa principal en la página de ajustes en la aplicación Contabilidad de Konvergo ERP." class="align-center" src="../../../../../_images/automatic-currency-rates.png"/>
<p>Haga clic en la casilla ubicada junto a la función <b>Tasas de cambio automáticas</b>, elija un banco para obtener las tasas de cambio en el menú desplegable de <b>Servicio</b> y seleccione un <b>Intervalo</b> de tiempo para las actualizaciones. Después, determine la fecha de la <b>Siguiente ejecución</b>.</p>
<p>Para actualizar las tasas de cambio al instante, haga clic en el icono <b>🔁 (flechas circulares)</b> que está ubicado a la derecha del campo <b>Siguiente ejecución</b>.</p>
<p>Asegúrese de <b>guardar</b> todos los cambios en cuanto termine de realizar sus configuraciones.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Todos los métodos de pago <b>deben</b> estar en la misma divisa que el diario de ventas o la de la empresa, si no está configurada. Si no es la misma, aparecerá un mensaje de <b>error de validación</b>.</p>
</div>

## Ver, editar y agregar divisas

Para revisar, editar y agregar divisas a la base de datos y que estén
disponibles en las listas de precios y como opción en el menú desplegable de
**Divisa principal** , haga clic en el enlace **Divisas**. Este enlace se
encuentra abajo del campo **Divisa** en la aplicación Contabilidad ‣ página de
Ajustes.

Al hacer clic en el enlace **Divisas** se abre una página separada con la
sección **Divisas**.

![Visualización de la página principal de divisas en la aplicación
Contabilidad de Konvergo ERP.](../../../../../_images/main-currencies-page.png)

En esta página aparece la lista maestra de Konvergo ERP que incluye 167 monedas
globales. Cada fila incluye la **divisa** correspondiente, el **símbolo** , el
**nombre** , la fecha de la **última actualización** y la **tasa actual** (en
comparación con la divisa predeterminada del país en el que se encuentra la
empresa).

En la parte derecha hay dos columnas que puede activar o desactivar:

  * **Usar en eBay** : puede usar esta divisa con la cuenta de eBay conectada (si es necesario).

  * **Activo** : esta divisa está activada, así que puede agregarla a una lista de precios o utilizarla como la divisa principal de la empresa si así lo desea. Puede configurarlas desde la aplicación Contabilidad ‣ Configuración ‣ Ajustes ‣ sección Divisas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Todas las opciones de divisa <b>activas</b> están disponibles de forma predeterminada en la parte superior de la lista.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Le recomendamos crear <em>al menos</em> una lista de precios por cada divisa <b>activa</b>. Consulte <a href="pricing">Listas de precios, descuentos y fórmulas</a> para obtener más información sobre la configuración de las listas de precios.</p>
</div>

Para activar o desactivar opciones, haga clic en el interruptor en la columna
correspondiente. El color del interruptor es verde cuando la divisa está
_activa_ , pero es gris si está _desactivada_.

### Formulario de detalles de la divisa

Para editar cualquier divisa en la página de **Divisas** , haga clic en la
divisa correspondiente. Esto abrirá su formulario de detalles y podrá realizar
las modificaciones necesarias.

![Aspecto del formulario de detalles de la divisa en la aplicación
Contabilidad de Konvergo ERP.](../../../../../_images/currency-detail-form.png)

El código de la divisa aparece en el campo **Divisa** en el formulario de
detalles y abajo aparece su nombre en el campo **Nombre**.

Luego, cambie la disponibilidad de la divisa con el interruptor **Activo**. Si
la divisa está _activa_ , el interruptor aparece de color verde y si está
_inactiva_ , el color del interruptor es gris.

Del lado derecho del formulario de detalles de la divisa se encuentra la
**unidad de divisa** correspondiente (por ejemplo, `dólares`) y también la
**subunidad de divisa** (por ejemplo, `centavos`).

Si la divisa se usará en eBay, cambie la opción **Usar en eBay** según sea
necesario.

En la pestaña **Tasas** puede ver, agregar o eliminar varias tasas de
conversión. Cada fila muestra la **fecha** de esa tasa específica, la
**empresa** a la que está relacionada, seguida por la **unidad por…** y **…
por unidad**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los puntos suspensivos (<em>…</em>) en las dos últimas columnas representan la divisa principal establecida para la empresa. Por ejemplo, si la divisa principal son los <code>USD</code>, entonces las columnas se titulan <b>Unidad por USD</b> y <b>USD por unidad</b>.</p>
</div>

Para agregar una nueva tasa, haga clic en **Agregar una línea** en la pestaña
**Tasas** y luego complete la información necesaria en las columnas que se
mencionan arriba.

### Formulario de detalles de la divisa principal

Si la divisa que seleccionó es la divisa principal de la empresa, aparecerá el
texto «**Esta es la divisa de su empresa** » en un recuadro azul en la parte
superior del formulario de detalles.

![Aspecto del formulario de detalles de la divisa principal en la aplicación
Contabilidad de Konvergo ERP.](../../../../../_images/main-currency-detail-form.png)

Todos los campos son iguales a los que puede encontrar en los formularios de
detalles de otras divisas, pero la pestaña **Tasas** **no** estará disponible
porque todas las demás tasas de cambio de moneda se basan en la moneda
principal de la empresa.

## Crear una nueva divisa

Si la divisa que desea utilizar no está en la página **Divisas** , entonces
haga clic en el botón **Nuevo** para abrir un formulario de plantilla de
divisas en blanco.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El botón <b>Nuevo</b> se ubica en la esquina superior derecha de cualquier formulario de detalles de divisa.</p>
</div> ![Aspecto del formulario de detalles vacío de la divisa en
la aplicación Contabilidad de Konvergo ERP.](../../../../../_images/blank-currency-
detail-form.png)

Complete el formulario de detalles de divisa. Escriba el código de la divisa
correspondiente en el campo **Divisa**. Debajo de eso, escriba el nombre de la
divisa en el campo **Nombre**.

Cambie la disponibilidad de la divisa con el interruptor **Activo**.

Del lado derecho del formulario de detalles de la divisa escriba la **unidad
de divisa** correspondiente (por ejemplo, `dólares`) y también la **subunidad
de divisa** (por ejemplo, `centavos`).

Si usará la divisa en eBay, entonces active **Usar en eBay**.

Abra la pestaña **Tasas** y agregue una nueva, haga clic en **Agregar una
línea**. Confirme y ajuste los campos **Fecha** , **Empresa** , **Unidad
por…** y **… por unidad** para garantizar que toda la información que se
completó de forma automática sea correcta.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los puntos suspensivos (<em>…</em>) en las dos últimas columnas representan la divisa principal establecida para la empresa. Por ejemplo, si la divisa principal son los <code>USD</code>, entonces las columnas se titulan <b>Unidad por USD</b> y <b>USD por unidad</b>.</p>
</div>

## Listas de precios específicas para cada divisa

Le recomendamos crear _al menos_ una lista de precios por cada divisa activa
en la base de datos. Para crear (o asignar) una lista de precios a una divisa
en específico, vaya a la aplicación Ventas ‣ Productos ‣ Listas de precios.

En la página de **Listas de precios** , seleccione una lista existente para
editarla o haga clic en **Nuevo** para crear una nueva lista de precios.

En el formulario de detalles de la lista de precios, ya sea una lista de
precios nueva o una existente, ajuste el campo **Divisa** según sea necesario.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Consulte <a href="pricing">Listas de precios, descuentos y fórmulas</a> para obtener más información relacionada con la configuración de las listas de precios.</p>
</div>

## Conversión automática del precio público

Es importante destacar que el precio público que aparece en los productos está
directamente relacionado con la divisa principal que la empresa tiene
configurada. Vaya a la aplicación Contabilidad ‣ Configuración ‣ Ajustes ‣
sección de Divisas ‣ Divisa principal ‣ Menú desplegable de divisas.

El precio de venta se actualiza de forma automática si cambia la lista de
precios a otra que tenga una divisa distinta a la divisa principal de la
empresa. El cambio en el precio está directamente relacionado con la tasa de
cambio actualizada para esa divisa.

## Establecer precios a los productos

Para establecer precios a los productos y evitar que se modifiquen con las
tasas de cambio, vaya a la aplicación Ventas ‣ Productos ‣ Productos.

En la página de **Productos** , seleccione el producto que desea modificar o
cree uno nuevo con el botón **Nuevo**.

En el formulario de detalles del producto, haga clic en el botón inteligente
**Precios adicionales** que está ubicado en la esquina superior izquierda. Al
realizar esta acción, aparecerá una página separada de **Reglas de precio** y
es específica para ese producto en particular.

![Cómo establecer precios de productos según las listas de precios en divisas
extranjeras en la aplicación Ventas de Konvergo ERP.](../../../../../_images/price-
rules-currencies.png)

Haga clic en **Nuevo** y seleccione una de las listas de precios del menú
desplegable en la columna **Lista de precios**.

El campo **Aplicado en** se completa en automático con el producto, así que
solo debe ingresar las cifras correspondientes en los campos **Cantidad
mínima** y **Precio**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El número en el campo <b>Cantidad mínima</b> indica que el <b>precio</b> establecido se activará <b>solo</b> si se compra al menos esa cantidad del producto.</p>
</div>

Si es necesario, configure una **fecha de inicio** y una **fecha de
finalización** para los precios establecidos. Si deja esos campos en blanco,
entonces el precio que establezca será válido sin importar la fecha de la
venta.

Si trabaja en un entorno multiempresas debe seleccionar a qué empresa se debe
aplicar esta regla de precios en el campo **Empresa**. Si deja este campo
vacío, la regla de precios se aplicará a todas las empresas de la base de
datos.

Una vez que termine de realizar estas configuraciones, cada que las listas de
precios designadas se apliquen a un cliente que intente adquirir este producto
en específico, entonces aparecerán los precios establecidos sin verse
afectados por cualquier cambio o actualización en las tasas de conversión.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para asegurarse de que las tasas de cambio se actualicen de forma automática, habilite la función de <em>tasas de cambio automáticas</em> en la página de ajustes de <em>Contabilidad</em>. Vaya a la aplicación Contabilidad ‣ Configuración ‣ Ajustes ‣ sección de Divisas.</p>
<img alt="Visualización de la función de divisa principal en la página de ajustes en la aplicación Contabilidad de Konvergo ERP." class="align-center" src="../../../../../_images/automatic-currency-rates.png"/>
<p>Haga clic en la casilla ubicada junto a la función <b>Tasas de cambio automáticas</b>, elija un banco para obtener las tasas de cambio en el menú desplegable de <b>Servicio</b> y seleccione un <b>Intervalo</b> de tiempo para las actualizaciones. Después, determine la fecha de la <b>Siguiente ejecución</b>.</p>
<p>Para actualizar las tasas de cambio al instante, haga clic en el icono <b>🔁 (flechas circulares)</b> que está ubicado a la derecha del campo <b>Siguiente ejecución</b>.</p>
<p>Asegúrese de <b>guardar</b> todos los cambios en cuanto termine de realizar sus configuraciones.</p>
</div>0

