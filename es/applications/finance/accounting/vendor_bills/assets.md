# Activos no circulantes y fijos

Los **activos no circulantes** , también conocidos como **activos a largo
plazo** , son inversiones que se esperan realizar después de un año. Se
capitalizan en lugar de gastarse y aparecen en el balance general de la
empresa. Dependiendo de su naturaleza, pueden sufrir una **depreciación**.

**Los activos fijos** son un tipo de activos no circulantes e incluyen los
bienes adquiridos por sus aspectos productivos, como edificios, vehículos,
equipos, terrenos y software.

Por ejemplo, supongamos que compramos un auto por $27,000. Planeamos
amortizarlo a lo largo de cinco años, y después lo venderemos por $7,000.
Utilizando el método de depreciación lineal, se cargan $4,000 cada año como
**gastos de depreciación**. Después de cinco años, el importe de la
**depreciación acumulada** que figura en el balance es de $20,000 dólares, lo
que nos deja un total de $7,000 de **valor no depreciable** , o valor de
salvamento.

La aplicación Contabilidad de Konvergo ERP gestiona la depreciación mediante la
creación de todos los asientos de depreciación automáticamente en _modo de
borrador_. Luego se contabilizan de forma periódica.

Konvergo ERP admite los siguientes **métodos de depreciación** :

  * Línea recta

  * En declive

  * Declive y luego línea recta

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El servidor comprueba una vez al día si se debe publicar un asiento. Pueden pasar hasta 24 horas antes de que se refleje el cambio de <em>borrador</em> a <em>registrado</em>.</p>
</div>

## Prerrequisitos

Se deben contabilizar estas operaciones en una **cuenta de activos** y no en
la cuenta de gastos predeterminada.

### Configurar una cuenta de activos

Para configurar su cuenta en el **Plan de cuentas** , vaya a Contabilidad ‣
Configuración ‣ Plan de cuentas, haga clic en _Crear_ , y llene el formulario.

![Configuración de una cuenta de activos en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/assets01.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El tipo de esta cuenta debe ser <em>Activo fijo</em> o <em>Activo no circulante</em>.</p>
</div>

### Contabilizar un gasto en la cuenta correcta

#### Seleccionar la cuenta en un borrador de factura

En un borrador de factura, seleccione la cuenta correcta para todos los
activos que está comprando.

![Selección de una cuenta de activos en una factura de proveedor en estado de
borrador en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/assets02.png)

#### Elija una cuenta de gastos diferente para productos específicos

Comience a editar el producto, vaya a la pestaña de _Contabilidad_ ,
seleccione la **Cuenta de gastos** correcta y guarde.

![Cambio de la cuenta de activos para un producto en
Konvergo ERP](../../../../_images/assets03.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Es posible <a href="#assets-automation"><span class="std std-ref">automatizar la creación de asientos de activos</span></a> para estos productos.</p>
</div>

#### Modificar la cuenta de un apunte contable registrado

Para hacer esto, abra su diario de compras en Contabilidad ‣ Contabilidad ‣
Compras, seleccione el apunte contable que desea modificar, haga clic en la
cuenta y seleccione la correcta.

![Modificación de la cuenta de un apunte contable publicado en la aplicación
Contabilidad de Konvergo ERP](../../../../_images/assets04.png)

## Asientos contables de activos

### Crear un nuevo asiento

Un **asiento contable de activo** genera automáticamente todos los asientos en
_modo de borrador_. Después se contabilizan uno por uno en su debido momento.

Para crear un nuevo asiento, vaya a Contabilidad ‣ Contabilidad ‣ Activos,
haga clic en _Crear_ y complete el formulario.

Haga clic en **seleccionar compras relacionadas** para vincular un apunte
contable existente a este nuevo asiento. Algunos campos se completarán de
forma automática y el apunte contable aparecerá en la pestaña **compras
relacionadas**.

![Asiento de activos en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/assets05.png)

Una vez hecho esto, puede hacer clic en _Calcular depreciación_ (al lado del
botón _Confirmar_) para generar todos los valores de la **tabla de
depreciación**. Esta tabla le muestra todos los asientos que Konvergo ERP registrará
para depreciar su activo, y la fecha.

![Tabla de depreciación en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/assets06.png)

#### ¿Qué significa «Prorata Temporis»?

La función **Prorata Temporis** es útil para depreciar sus activos con la
mayor precisión posible.

Con esta función, el primer asiento en la tabla de depreciación se calcula en
función del tiempo que queda entre la _fecha de prorrateo_ y la _fecha de
primera depreciación_ , y no en función del tiempo predeterminado entre
depreciaciones.

Por ejemplo, la tabla de depreciación anterior tiene su primera depreciación
con un importe de $241.10 en lugar de $4,000.00. Por lo tanto, el último
asiento también es menor y tiene un importe de $3,758.90.

#### ¿Cuáles son los diferentes métodos de depreciación?

El **método de depreciación en línea recta** divide el valor depreciable
inicial entre el número de depreciaciones planeadas. Todos los asientos de
depreciación tienen el mismo importe.

El **Método de depreciación en declive** multiplica el valor depreciable por
el **factor en declive** para cada asiento. Cada asiento de depreciación tiene
un importe inferior al del asiento anterior. El último asiento de depreciación
no utiliza el factor en declive, sino que tiene un importe correspondiente al
balance del valor depreciable de modo que llegue a $0 al final de la duración
indicada.

El **Método de depreciación en declive y luego en línea recta** utiliza el
método en declive, pero con una depreciación mínima igual a la del método de
línea recta. Este método asegura una depreciación rápida al principio, seguida
de una constante después.

### Activos del diario de compras

Puede crear un asiento de activo desde un apunte específico en su **diario de
compras**.

Para hacerlo, abra su diario de compras en Contabilidad ‣ Contabilidad ‣
Compras, y seleccione el apunte contable que desea registrar como activo.
Asegúrese de que se registre en la cuenta correcta (vea: Modificar la cuenta
de un apunte contable registrado).

Posteriormente, haga clic en _Acción_ , seleccione **Crear activo** , y
complete el formulario de la misma manera que lo haría para crear un nuevo
asiento.

![Crear un asiento de activo desde un apunte contable en la aplicación
Contabilidad de Konvergo ERP](../../../../_images/assets07.png)

## Modificación de un activo

Puede modificar los valores de un activo para aumentar o disminuir su valor.

Para hacerlo, abra el activo que desea modificar y haga clic en _Modificar
depreciación_. A continuación, complete el formulario con los nuevos valores
de depreciación y haga clic en _Modificar_.

Una **disminución de valor** registra un nuevo asiento para la **disminución
de valor** y modifica todos los asientos futuros _no registrados_ que aparecen
en el tablero de depreciación.

Para un **aumento de valor** es necesario completar campos adicionales
relacionados con los movimientos de la cuenta, además de crear un nuevo
asiento de activo con el **aumento de valor**. Se puede acceder al asiento de
activo con **aumento de valor** a través de un botón inteligente.

![Botón inteligente de incremento bruto](../../../../_images/assets08.png)

## Eliminar activos fijos

**Vender** un activo o **eliminarlo** implica que se debe retirar del balance
general.

Para ello, abra el activo del que desea deshacerse, haga clic en _Vender o
eliminar_ y complete el formulario.

![Disposición de bienes](../../../../_images/assets09.png)

La contabilidad de Konvergo ERP genera entonces todos los asientos necesarios para
deshacerse del activo, incluyendo la ganancia o pérdida en la venta, que se
basa en la diferencia entre el valor contable del activo en el momento de la
venta y el importe en el que se vende.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para registrar la venta de un activo, primero debe registrar la factura de cliente relacionada para poder vincularla con la venta del activo.</p>
</div>

## Modelos de activos

Puede crear **Modelos de activos** para crear los asientos de activos de forma
más rápida. Esto resulta especialmente útil si compra de forma recurrente el
mismo tipo de activos.

Para crear un modelo, vaya a Contabilidad ‣ Configuración ‣ Modelos de
activos, haga clic en _Crear_ , y complete el formulario de la misma manera
que lo haría para crear un nuevo asiento.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede convertir un <em>asiento confirmado de activo</em> en un modelo abriéndolo desde Contabilidad ‣ Contabilidad ‣ Activos y luego, haciendo clic en el botón <em>Guardar modelo</em>.</p>
</div>

### Aplicar un modelo de activos a un nuevo asiento

Cuando cree un nuevo asiento de activo, complete la **Cuenta de activo fijo**
con la cuenta de activo correcta.

En la parte superior del formulario aparecen nuevos botones con todos los
modelos vinculados a esa cuenta. Al hacer clic en un modelo, se completa el
formulario según dicho modelo

![Botón de activos](../../../../_images/assets10.png)

## Automatizar activos

Cuando se crea o edita una cuenta cuyo tipo es _activo no corriente_ o _activo
fijo_ , se puede configurar para que se creen activos correspondientes a los
gastos que se abonan en dicha cuenta de forma automática.

Hay tres opciones para el campo **automatizar activos** :

  1. **No:** es el valor predeterminado. No pasa nada.

  2. **Crear en borrador:** cuando se registra una transacción en la cuenta se crea un borrador de _asiento de activo_ , pero no se valida. Usted debe completar el formulario correspondiente en Contabilidad‣ Contabilidad ‣ Activos.

  3. **Crear y validar:** también debe seleccionar un modelo de activos (ver: Modelos de activos). Cada vez que se registra una operación en la cuenta, se crea un _asiento de activo_ que se valida inmediatamente.

![ Automatizar activos en Contabilidad de
Konvergo ERP](../../../../_images/assets11.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede, por ejemplo, seleccionar esta cuenta como la <b>cuenta de gastos</b> predeterminada de un producto para automatizar totalmente su compra. (ver: <a href="#product-assets-account"><span class="std std-ref">Elija una cuenta de gastos diferente para productos específicos</span></a>).</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../get_started/chart_of_accounts">Plan de cuentas</a></p></li>
</ul>
</div>

