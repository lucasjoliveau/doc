# Gastos diferidos y prepagos

Los **gastos diferidos** y **prepagos** son costos que ya se han pagado por
productos no entregados o servicios por recibir.

Estos costos son **activos** para la empresa que los paga, puesto que ya pagó
por productos y servicios que aún no ha recibido o utilizado. La empresa no
puede registrarlos en la **cuenta de pérdidas y ganancias** , o en la _cuenta
de resultados_ , ya que los pagos se contabilizarán en el futuro.

Estos gastos futuros deben diferirse en el balance de la empresa hasta el
momento en que puedan ser **reconocidos** , al mismo tiempo o a lo largo de un
periodo definido, en la cuenta de pérdidas y ganancias.

Por ejemplo, supongamos que pagamos $1,200 al contado por un año de seguro. Ya
pagamos el costo ahora pero aún no hemos utilizado el servicio. Por lo tanto,
contabilizamos este nuevo gasto en una _cuenta de prepago_ y decidimos
registrarlo mensualmente. Cada mes, durante los próximos 12 meses, se
reconocerán $100 como gasto.

La aplicación de contabilidad de Konvergo ERP maneja los gastos diferidos y los pagos
anticipados distribuyéndolos en múltiples asientos que se crearán
automáticamente en modo de _borrador_ y se registrarán periódicamente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El servidor comprueba una vez al día si se debe publicar un asiento. Pueden pasar hasta 24 horas antes de que se refleje el cambio de <em>borrador</em> a <em>registrado</em>.</p>
</div>

## Prerrequisitos

Estas operaciones se deben registrar en una **cuenta de gastos diferidos** en
lugar de en la cuenta de gastos predeterminada.

### Configurar una cuenta de gastos diferidos

Para configurar su cuenta en el **Plan de cuentas** , vaya a Contabilidad ‣
Configuración ‣ Plan de cuentas, haga clic en _Crear_ , y llene el formulario.

![Configuración de una cuenta de gastos diferidos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses01.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El tipo de esta cuenta debe ser <em>activo corriente</em> o <em>prepago</em>.</p>
</div>

### Contabilizar un gasto en la cuenta correcta

#### Seleccionar la cuenta en un borrador de factura

En un borrador de factura, seleccione la cuenta correcta para todos los
productos cuyos gastos se deben diferir.

![Selección de la cuenta de gastos diferidos en el borrador de una factura en
Contabilidad de Konvergo ERP](../../../../_images/deferred_expenses02.png)

#### Elija una cuenta de gastos diferente para productos específicos

Comience a editar el producto, vaya a la pestaña de _Contabilidad_ ,
seleccione la **Cuenta de gastos** correcta y guarde.

![Cambio de la cuenta de gastos para un producto en
Konvergo ERP](../../../../_images/deferred_expenses03.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Es posible automatizar la creación de asientos de gastos para estos productos (ver: <a href="#automate-the-deferred-expenses">Automatizar los gastos diferidos</a>).</p>
</div>

#### Modificar la cuenta de un apunte contable registrado

Para hacer esto, abra su diario de compras en Contabilidad ‣ Contabilidad ‣
Compras, seleccione el apunte contable que desea modificar, haga clic en la
cuenta y seleccione la correcta.

![Modificación de la cuenta de un apunte contable publicado en la aplicación
Contabilidad de Konvergo ERP](../../../../_images/deferred_expenses04.png)

## Asientos de gastos diferidos

### Crear un nuevo asiento

Un **asiento de gasto diferido** genera automáticamente todos los asientos
como tipo _borrador_. Después, se contabilizan uno por uno en el momento
adecuado hasta que se reconoce el importe total del gasto.

Para crear un nuevo asiento, vaya a Contabilidad ‣ Contabilidad ‣ Gasto
diferido, haga clic en _Crear_ , y complete el formulario.

Haga clic en **seleccione las compras relacionadas** para vincular un apunte
de diario existente a este nuevo asiento. Algunos campos se completarán
automáticamente y el apunte aparecerá en la pestaña **Gastos relacionados**.

![Asiento de gastos diferidos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses05.png)

Después de hacerlo, puede hacer clic en _calcular diferimiento_ (al lado del
botón _confirmar_) para generar todos los valores del **tablero de gastos**.
Este tablero muestra todos los asientos que Konvergo ERP registrará para reconocer su
gasto, y en qué fecha.

![Tabla de gastos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses06.png)

#### ¿Qué significa «Prorata Temporis»?

La función **Prorata Temporis** es útil para reconocer sus gastos con la mayor
precisión posible.

Con esta función, el primer asiento en el tablero de gastos se calcula en
función del tiempo que queda entre la _fecha prorata_ y la _fecha de primer
reconocimiento_ , en lugar del tiempo predeterminado entre los
reconocimientos.

Por ejemplo, el tablero de gastos anterior tiene su primer gasto con un
importe de $70.97 en lugar de $100.00. Por lo tanto, el último asiento también
es menor y tiene un importe de $29.03.

### Asiento diferido del diario de compras

Puede crear un asiento diferido desde un apunte específico en su **diario de
compras**.

Para hacerlo, abra su diario de compras yendo a Contabilidad ‣ Contabilidad ‣
Compras, y seleccione el apunte de diario que desea diferir. Asegúrese de que
esté registrado en la cuenta correcta (vea: Cambiar la cuenta de un apunte de
diario registrado).

A continuación, haga clic en _Acción_ , seleccione **Crear asiento diferido**
, y complete el formulario de la misma manera que lo haría para crear un nuevo
asiento.

![Cree un asiento diferido desde un apunte contable en Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses07.png)

## Modelos de gastos diferidos

Puede crear **Modelos de gastos diferidos** para crear sus asientos de gastos
diferidos con mayor rapidez.

Para crear un modelo, vaya a Contabilidad ‣ Configuración ‣ Modelos de gastos
diferidos, haga clic en _Crear_ , y complete el formulario de la misma manera
que lo haría para crear un nuevo asiento.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede convertir un <em>asiento de gastos diferidos confirmado</em> en un modelo abriéndolo desde Contabilidad ‣ Contabilidad ‣ Gastos diferidos y luego, haciendo clic en el botón <em>Guardar modelo</em>.</p>
</div>

### Aplicar un modelo de gasto diferido a un nuevo asiento

Cuando cree un nuevo asiento de gastos diferidos, complete la **cuenta de
gastos diferidos** con la cuenta de reconocimiento correcta.

En la parte superior del formulario aparecen nuevos botones con todos los
modelos vinculados a esa cuenta. Al hacer clic en un modelo, se completa el
formulario según dicho modelo

![Botón de modelo de gasto diferido en Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses08.png)

## Automatizar los gastos diferidos

Cuando se crea o edita una cuenta de tipo _activo corriente_ o _prepago_ , se
puede configurar para que los gastos que se abonan en ella se difieran
automáticamente.

Hay tres opciones para el campo **Automatizar gastos diferidos** :

  1. **No:** es el valor predeterminado. No pasa nada.

  2. **Crear en borrador:** cuando se valida una transacción en la cuenta se crea un borrador de _asiento de gastos diferidos_ , pero no se valida. Usted debe completar el formulario correspondiente en Contabilidad ‣ Contabilidad ‣ Gastos diferidos.

  3. **Crear y validar:** también debe seleccionar un modelo de gastos diferidos (ver: Modelos de gastos diferidos). Cada vez que se registra una operación en la cuenta, se crea un _asiento de gastos diferidos_ que se valida inmediatamente.

![Gastos diferidos automáticos en una cuenta de Contabilidad de
Konvergo ERP](../../../../_images/deferred_expenses09.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede, por ejemplo, seleccionar esta cuenta como la <b>cuenta de gastos</b> predeterminada de un producto para automatizar totalmente su compra. (ver: <a href="#choose-a-different-expense-account-for-specific-products">Elija una cuenta de gastos diferente para productos específicos</a>).</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../get_started/chart_of_accounts">Plan de cuentas</a></p></li>
</ul>
</div>

