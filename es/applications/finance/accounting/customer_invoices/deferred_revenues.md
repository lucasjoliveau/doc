# Ingresos diferidos

Los **ingresos diferidos** son los pagos anticipados que realizan los clientes
por productos que no se han entregado o servicios que no se han prestado.

Estos pagos son un **pasivo** para la empresa que los recibe, ya que sigue
debiendo a sus clientes estos productos o servicios. La empresa no puede
incluirlos en la **cuenta de pérdidas y ganancias** , o en el _estado de
resultados_ , ya que los pagos se devengarán efectivamente en el futuro.

Estos ingresos futuros deben diferirse en el balance de la empresa hasta el
momento en el que se puedan **reconocer** , al mismo tiempo o a lo largo de un
periodo definido, en la cuenta de pérdidas y ganancias.

Por ejemplo, supongamos que vendemos una garantía amplia de cinco años por 350
dólares. Ya recibimos el dinero, pero aún no lo hemos ganado. Por lo tanto,
contabilizamos este nuevo ingreso en una cuenta de ingresos diferidos y
decidimos reconocerlo anualmente. Cada año, durante los próximos 5 años, se
reconocerán 70 dólares como ingresos.

La contabilidad de Konvergo ERP administra los ingresos diferidos distribuyéndolos en
varios asientos que se crean de manera predeterminada como _borrador_ y luego
se contabilizan periódicamente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El servidor comprueba una vez al día si se debe publicar un asiento. Pueden pasar hasta 24 horas antes de que se refleje el cambio de <em>borrador</em> a <em>registrado</em>.</p>
</div>

## Prerrequisitos

Se deben contabilizar estas operaciones en una **cuenta de ingresos
diferidos** en lugar de la cuenta de ingresos predeterminada.

### Configurar una cuenta de ingresos diferidos

Para configurar su cuenta en el **Plan de cuentas** , vaya a Contabilidad ‣
Configuración ‣ Plan de cuentas, haga clic en _Crear_ , y llene el formulario.

![Configuración de una cuenta de ingresos diferidos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues01.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta cuenta debe ser tipo <em>Pasivo circulante</em> o <em>Pasivo no circulante</em>.</p>
</div>

### Contabilizar un ingreso en la cuenta correcta

#### Seleccionar la cuenta en un borrador de factura

En un borrador de factura, seleccione la cuenta correcta para todos los
productos cuyos ingresos se deben diferir.

![Selección de la cuenta de ingresos diferidos en el borrador de una factura
en Contabilidad de Konvergo ERP](../../../../_images/deferred_revenues02.png)

#### Elija una cuenta de ingresos diferente para productos específicos

Comience a editar el producto, vaya a la pestaña _Contabilidad_ , seleccione
la **cuenta de ingresos** correcta y guarde.

![Cambio de cuenta de ingresos para un producto dentro de
Konvergo ERP](../../../../_images/deferred_revenues03.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Es posible automatizar la creación de asientos de ingresos para estos productos ( ver: <a href="#automate-the-deferred-revenues">Automatizar los ingresos diferidos</a>).</p>
</div>

#### Modificar la cuenta de un apunte contable registrado

Para hacerlo, abra su diario de ventas yendo a Contabilidad ‣ Contabilidad ‣
Ventas, seleccione el elemento del diario que desea modificar, haga clic en la
cuenta y seleccione la correcta.

![Modificación de la cuenta de un apunte contable publicado en la aplicación
Contabilidad de Konvergo ERP](../../../../_images/deferred_revenues04.png)

## Apuntes de ingresos diferidos

### Crear un nuevo asiento

Un **ingreso diferido** genera automáticamente todos los asientos del diario
en _modo borrador_. A continuación, se contabilizan uno a uno en el momento
adecuado hasta que se reconoce el importe total de los ingresos.

Para crear un nuevo asiento, vaya a Contabilidad ‣ Contabilidad ‣ Ingresos
diferidos, haga clic en _Crear_ , y complete el formulario.

Haga clic en **selección de compras relacionadas** para vincular un apunte del
diario existente a este nuevo asiento. Algunos campos se llenarán
automáticamente y el apunte del diario aparecerá en la pestaña **Ventas
Relacionadas**.

![Asiento de ingresos diferidos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues05.png)

Una vez hecho esto, puede hacer clic en _Calcular ingresos_ (al lado del botón
_Confirmar_) para generar todos los valores del **Tablero de ingresos**. Este
tablero le muestra todos los asientos que Konvergo ERP registrará para reconocer sus
ingresos, y la fecha en que lo hará.

![Tabla de ingresos en Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues06.png)

#### ¿Qué significa «Prorata Temporis»?

La función **Pro rata Temporis** es útil para reconocer sus ingresos con la
mayor precisión posible.

Con esta función, el primer asiento en la tabla de ingresos se calcula según
el tiempo que queda entre la _fecha de prorrateo_ y la _fecha de primer
reconocimiento_ , en lugar de la cantidad de tiempo predeterminada entre los
reconocimientos.

Por ejemplo, la tabla de ingresos anterior tiene su primer ingreso con un
importe de $4.22 en lugar de $70.00. Por lo tanto, el último ingreso también
es menor y tiene un importe de $65.78.

### Asiento diferido del diario de ventas

Puede crear un asiento diferido desde un apunte específico en su **diario de
ventas**.

Para hacer esto, abra su diario de ventas en Contabilidad ‣ Contabilidad ‣
Ventas y seleccione el apunte contable que desea diferir. Asegúrese de que
está registrado en la cuenta correcta (consulte: Cambiar la cuenta de un
apunte de diario registrado).

A continuación, haga clic en _Acción_ , seleccione **Crear asiento diferido**
, y complete el formulario de la misma manera que lo haría para crear un nuevo
asiento.

![Cree un asiento diferido desde un apunte contable en Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues07.png)

## Modelos de ingresos diferidos

Se pueden crear **modelos de ingresos diferidos** para crear más rápidamente
los asientos de ingresos diferidos.

Para crear un modelo, vaya a Contabilidad ‣ Configuración ‣ Modelos de
ingresos diferidos, haga clic en _Crear_ , y complete el formulario de la
misma manera que lo haría para crear un nuevo asiento.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También se puede convertir un <em>ingreso diferido confirmado</em> en un modelo si lo abre desde Contabilidad ‣ Contabilidad ‣ Ingresos diferidos y luego, hace clic en el botón <em>Guardar modelo</em>.</p>
</div>

### Aplicar un modelo de ingresos diferidos a un nuevo asiento

Cuando cree un nuevo asiento de ingresos diferidos, complete la **cuenta de
ingresos diferidos** con la cuenta de reconocimiento correcta.

En la parte superior del formulario aparecen nuevos botones con todos los
modelos vinculados a esa cuenta. Al hacer clic en un modelo, se completa el
formulario según dicho modelo

![Botón de modelo de ingreso diferido en Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues08.png)

## Automatizar los ingresos diferidos

Cuando se crea o edita una cuenta de tipo _Pasivo corriente_ o _Pasivo no
corriente_ , se puede configurar para diferir los ingresos que se abonan
automáticamente en ella.

Hay tres opciones para el campo **Automatizar ingresos diferidos** :

  1. **No:** es el valor predeterminado. No pasa nada.

  2. **Crear en borrador:** cuando se registra una transacción en la cuenta se crea un borrador de _asiento de ingresos diferidos_ , pero no se valida. Primero debe completar el formulario correspondiente en Contabilidad ‣ Contabilidad ‣ Ingresos diferidos.

  3. **Crear y validar:** también debe seleccionar un modelo de ingresos diferidos (ver: Modelos de ingresos diferidos). Cada vez que se registra una operación en la cuenta, se crea un _ingreso diferido_ que se valida inmediatamente.

![Ingresos diferidos automáticos en una cuenta de Contabilidad de
Konvergo ERP](../../../../_images/deferred_revenues09.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede, por ejemplo, seleccionar esta cuenta como la <b>cuenta de ingresos</b> predeterminada de un producto para automatizar totalmente su venta. (ver: <a href="#choose-a-different-income-account-for-specific-products">Elija una cuenta de ingresos diferente para productos específicos</a>).</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../get_started/chart_of_accounts">Plan de cuentas</a></p></li>
<li><p><a href="https://www.odoo.com/r/EWO">Konvergo ERP Academy: Deferred Revenues (Recognition)</a></p></li>
</ul>
</div>

