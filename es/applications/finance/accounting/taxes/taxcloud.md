# Integración con TaxCloud

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Ya comenzamos a sacar de servicio la integración con TaxCloud, empezando con Konvergo ERP 17. En Konvergo ERP 17 se prohibirán nuevas instalaciones, mientras que en Konvergo ERP 18 los módulos de TaxCloud ya <b>no</b> existirán. Konvergo ERP recomienda usar mejor la plataforma Avatax</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="avatax">Integración con AvaTax</a></p>
</div>

TaxCloud calcula la tasa de impuestos de venta en tiempo real para cada
estado, ciudad y jurisdicción de los Estados Unidos. Da seguimiento a los
productos que están exentos de impuestos de venta y en qué estados aplica la
excepción.

## Registro en TaxCloud

Registre una cuenta en [TaxCloud.com](https://taxcloud.com/register) y
complete la configuración. Una vez en funcionamiento, obtenga sus **claves API
de TaxCloud** al hacer clic en **tiendas** y luego en **obtener detalles**.

![Ejemplo de claves API de TaxCloud de una
tienda](../../../../_images/taxcloud-api-keys.png)

## Habilitar TaxCloud

  1. Vaya a tablero de Contabilidad ‣ Configuración ‣ Ajustes y en la sección **impuestos** habilite la opción **TaxCloud**.

  2. Agregue el **ID de inicio de sesión** de la tienda en **ID de API** y la **clave** de la tienda en **CLAVE API**. Haga clic en **guardar**.

  3. Haga clic en el botón **actualizar** (**🗘**) que se encuentra a lado del campo **categoría predeterminada** para importar las categorías de productos de los TIC códigos de información fiscal desde TaxCloud. Algunas categorías pueden implicar tasas de impuestos o excepciones específicas.

  4. Seleccione una **categoría predeterminada** y **guardar**. La **categoría predeterminada** se aplica cuando no se establece ninguna **categoría de TaxCloud** en sus productos o categorías de productos, o cuando no se encuentra ningún producto en una orden o factura.

![Completar las claves API de TaxCloud en Konvergo ERP.](../../../../_images/taxcloud-
settings.png)

## Establecer categorías de TaxCloud en productos

Si necesita utilizar más de una categoría TIC (es decir, la **categoría
predeterminada**), vaya a la pestaña **información general** del producto y
seleccione una **categoría TaxCloud**.

Si desea configurar varios productos de forma simultánea, asegúrese de que
pertenecen a la misma **categoría de producto** y haga clic en el botón de
enlace externo (**🡕**) para establecer una **categoría de TaxCloud** en la
**categoría de producto**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si establece una <b>categoría TaxCloud</b> en un producto y otra en su <b>categoría de producto</b>, Konvergo ERP solo considera la <b>categoría TaxCloud</b> que se encuentra en el producto.</p>
<p>Una <b>categoría TaxCloud</b> establecida en una <b>categoría de producto principal</b> no se aplica a sus <b>subcategorías de producto</b>. Por ejemplo, si establece una <b>categoría TaxCloud</b> en la <b>categoría de producto</b> <em>todos</em>, no se aplica a la <b>categoría de producto</b> <em>todos/ventas</em>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de que la dirección de su empresa esté completa, incluyendo el estado y el código postal. Vaya a Ajustes ‣ Empresas: Actualizar información para abrir y editar la dirección de su empresa.</p>
</div>

## Registrar de forma automática los impuestos en la cuenta de impuestos por
pagar correcta

Para asegurarse de que los nuevos impuestos generados por la integración con
TaxCloud se crean con la cuenta de **impuestos por pagar** correcta, cree un
valor **predeterminado definido por el usuario**. Debe repetir este proceso
para cada una de sus empresas que utilicen TaxCloud.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Un valor predeterminado definido por el usuario afecta a todos los registros al momento de la creación. Significa que <b>cada</b> nuevo impuesto se configura para registrar los ingresos en la cuenta de impuestos por pagar especificada, a menos que el impuesto se edite de forma manual para especificar una cuenta de ingresos (o si otro valor predeterminado definido por el usuario tiene prioridad).</p>
</div>

Para hacerlo vaya a tablero de Contabilidad ‣ Configuración ‣ Contabilidad:
Plan de cuentas, encuentre la cuenta de **impuestos por pagar** de la empresa
y haga clic en **configuración**. Tome nota del número después de `id=` en el
URL. Es el **ID de la cuenta de impuestos por pagar** y se utilizará después.

![Ejemplo del ID de una cuenta de impuestos por pagar en el
URL](../../../../_images/tax-payable-id.png)

Active el [modo de
desarrollador](../../../general/developer_mode#developer-mode) y luego
vaya a Ajustes ‣ Técnico ‣ Acciones: Valores predeterminados del usuario y
haga clic en **crear**.

Haga clic en el menú desplegable **campo** y luego en **buscar más…**.

![Búsqueda de campos predeterminados definidos por el
usuario](../../../../_images/user-defaults-search-more.png)

Utilice la barra de búsqueda para filtrar según el modelo **línea de partición
de impuestos** y vuelva a utilizarla para filtrar según el campo **cuenta**.
Seleccione la línea mediante el modelo **línea de partición de impuestos** en
la columna **modelo**.

![Búsqueda del modelo "línea de partición de impuestos" y del campo
"cuenta".](../../../../_images/user-defaults-search-filters.png)

Una vez que regrese a la creación de **valores predeterminados definidos por
el usuario** , introduzca el **ID de la cuenta de impuestos por pagar** que
anotó antes en el campo **valor predeterminado (formato JSON)**.

Seleccione la empresa a la que debe aplicarse esta configuración en el campo
**empresa** y haga clic en **guardar**.

![Ejemplo de una configuración de valores predeterminados definidos por el
usuario](../../../../_images/user-defaults-complete-configuration.png)

## Detectar la posición fiscal de forma automática

Los impuestos de venta se calculan en Konvergo ERP según las [posiciones
fiscales](fiscal_positions). Cuando se habilita TaxCloud se crea una
posición fiscal para Estados Unidos.

Puede configurar Konvergo ERP para que detecte de forma automática a qué clientes se
debe aplicar la posición fiscal. Para hacerlo, vaya a tablero de Contabilidad
‣ Configuración ‣ Contabilidad: Posiciones fiscales y seleccione **mapeo
automático de impuestos (TaxCloud)**. Habilite la función **detectar de forma
automática** y **guardar**.

![Habilite la función "detectar de forma automática" en la posición fiscal de
TaxCloud](../../../../_images/fiscal-position-detect.png)

Esta posición fiscal se establece de forma automática en cualquier orden o
factura si el país del cliente es _Estados Unidos_. Esto activa el cálculo
automático de impuestos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para obtener los impuestos de venta de una orden de venta, confírmela o haga clic en el botón <b>actualizar impuestos</b> a lado de <b>agregar envío</b>.</p>
</div>

## Interacción con cupones y promociones

La integración con TaxCloud puede tener un comportamiento inesperado si
utiliza los **programas de promociones** o **cupones**. Como TaxCloud no
acepta líneas con importes negativos como parte del cálculo de impuestos, el
importe de las líneas agregadas por el programa de promociones se debe deducir
del total de las líneas que afecta.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Esto significa, entre otras complicaciones, que las órdenes que utilicen cupones o promociones con una posición fiscal de TaxCloud <b>deben</b> facturarse por completo, no se pueden crear facturas para entregas parciales, etc.</p>
</div>

Es posible que tenga otro resultado. Por ejemplo, si vende un producto para el
que tiene un programa de promoción que ofrece un descuento del 50%. Si la tasa
de impuestos del producto es del 7%, la tasa de impuestos calculada mediante
la integración con TaxCloud es del 3.5%. Esto sucede porque el descuento está
incluido en el precio que se envía a TaxCloud. Sin embargo, en Konvergo ERP, el
descuento está en otra línea completamente diferente. Aun así, el cálculo del
impuesto es correcto. De hecho, un impuesto del 3.5% sobre el precio total es
el equivalente a un impuesto del 7% sobre la mitad del precio, pero esto
podría ser inesperado desde el punto de vista del usuario.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="fiscal_positions">Posiciones fiscales (mapeo de impuestos y cuentas)</a></p>
</div>

