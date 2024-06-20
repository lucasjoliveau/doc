# Configuración del conector de Amazon

Odoo permite que los usuarios registren una cuenta de vendedor de Amazon en la
base de datos, pero el usuario **debe** tener una cuenta de vendedor de Amazon
pagada antes de completar la cofiguración.

Para configurar una cuenta de vendedor de Amazon primero inicie sesión en la
plataforma de Aamazon y vaya a Cuenta y listas ‣ Iniciar una cuenta de
vendedor desde el menú desplegable que se encuentra en el encabezado.

Después, en la página Vende con Amazon siga el proceso de registro y después
siga las instrucciones a continuación para registrar y vincular su cuenta de
vendedor de Amazon con Odoo.

Ver también

[Vender con Amazon](https://www.amazon.com/b/?node=12766669011)

## Contecte su cuenta de vendedor de Amazon con Odoo

Para conectar su cuenta de vendedor de Amazon con Odoo, vaya a la aplicación
Ventas ‣ Configuración ‣ Ajustes ‣ sección de Conectores. Allí active la
función Sincronización con Amazon y haga clic en Guardar.

Después, regrese a la aplicación Ventas ‣ Configuración ‣ Ajustes ‣ sección de
Conectores y haga clic en el enlace Cuentas de Amazon en los ajustes de
Sincronización con Amazon.

![Las cuentas de Amazon vinculadas en los ajustes de la aplicación Ventas de
Odoo](../../../../_images/amazon-accounts-link-setting.png)

Hacer esto lo llevará a la página Cuentas de Amazon. Desde aquí, haga clic en
Nuevo para crear y vicular una nueva cuenta de Amazon.

En el campo en Cuenta de Amazon de la página, primero elija el nombre de la
cuenta (por ejemplo, `Marketplace estadounidense`). Después, en la pestaña
Credenciales seleccione el marketplace en el que la cuenta de vendedor se creó
desde el menú desplegable País del Marketplace.

![Un formulario común para una cuenta de Aamazon en la aplicación de
ventas.](../../../../_images/amazon-accounts-form-page.png)

Después de guardar, el campo en la pestaña Credenciales cambiará por un botón
llamado Vincular con Amazon.

![La página de un formulario usual para una cuenta de Amazon y el botón de
Vincular con Amazón en la aplicación de Ventas.](../../../../_images/amazon-
accounts-form-link-button.png)

Al hacer clic en este botón se le redirigirá a la página de inicio de sesión
de Amazon, o, si el usuario ya inició sesión en Amazon, a la página de
consentimiento.

En la página de inicio de sesión, ingrese a la cuenta de vendedor de Amazon
deseada.

En la página de consentimiento, confirme que Amazon puede permitir que Odoo
tenga acceso a la cuenta y toda la información relacionada.

Al confirmarlo, Amazon redirigirá al usuario de vuelta a Odoo y la cuenta
estará registrada.

Ya que haya logrado registrar la cuenta de Amazon, los marketplaces
disponibles para esta cuenta en específico se sincronizarán con Odoo y se
enlistarán en la pestaña Marketplaces.

Si lo desea, quite elementos de la lista de marketplaces sincronizados para
deshabilitar la sincronización.

## Órdenes de Amazon en Odoo

Al sincronizar una orden de Amazon, se crearán hasta tres líneas de artículos
en la orden de venta de Odoo. Cada una representa un producto vendido en
Amazon: una línea por el producto que se vendió en el marketplace de Amazon,
una por los cargos de envío (si los hay) y una por la envoltura de regalo (si
hay).

Para seleccionar un producto de la base de datos para un artículo de orden de
ventas lo que se hace es vincular la Referencia interna (una referencia
personalizable del producto dentro de Odoo, por ejemplo `FURN001`) con el
_SKU_ de Aamazon para artículos del marketplace, el _código de envío_ de
Amazon para cargos de envío y el código de _envoltura de regalo_ de Amazon
para los cambios de envoltura.

Para productos del marketplace, todo esto se guarda como _Ofertas de Amazon_ ,
las cuales se enlistan en el botón inteligente de Ofertas del formulario del
contacto.

![El botón inteligente de Ofertas de Amazon en el formulario de la aplicación
Ventas de Odoo.](../../../../_images/amazon-offers-button.png)

Las ofertas se crean de forma automática si se establece una coincidencia,
además de que se usan para órdenes subsecuentes para buscar SKU. Si no se
encuentra ninguna oferta con un SKU que coincida, en su lugar se usará la
referencia interna.

Truco

Es posible forzar la vinculación de un artículo del marketplace con un
producto específico, solo se tiene que cambiar ya sea el producto o el SKU de
una oferta para asegurarse que coincide. La oferta se puede crear de forma
manual si todavía no se creó de forma automática.

Esto es útil si la referencia interna no se usa como el SKU, o si el producto
se vende en condiciones diferentes.

Si no se encontró ningún producto de la base de datos con una referencia
interna que coincida para un SKU o código de envoltura de Amazon, entonces se
usará un producto de la base de datos predeterminado, _Venta de Amazon_ , se
usará. Lo mismo se hace con el producto predeterminado _Envío de Amazon_ si no
se encuentra un producto en la base de datos para un código de envío de
Amazon.

Nota

Para modificar los productos predeterminados, active el [modo de
desarrollador](../../../general/developer_mode.html#developer-mode) y vaya a
la aplicación de Ventas ‣ Configuración ‣ Ajustess ‣ Conectores ‣
Sincronización de Amazon ‣ Productos predeterminados.

## Configuración de impuestos de productos

Para permitir el reporte de impuestos de ventas de Amazon, los impuestos
aplicados a los artículos de la orden de venta son los que se configuran en el
producto, o se determinan por la posición fiscal.

Asegúrese de tener los impuestos correctos configurados en sus productos en
Odoo, o hágalo por posiciones fiscales, para evitar discrepancias en los
subtotales de _la central de vendedores de Amazon_ y Odoo.

Nota

Como Amazon no siempre aplica los mismos impuestos que los configurados en
Odoo, es posible que los totales de la orden difieran entre _la central de
vendedores de Amazon_ y _Odoo_ por algunos centavos. Esas diferencias se
pueden resolver con una cancelación al conciliar los pagos en Odoo.

## Agregar un nuevo Marketplace

Todos los marketplaces son compatibles con el conector de Amazon. Para agregar
un nuevo marketplace, siga los siguientes pasos:

  1. Active el [modo de desarrollador](../../../general/developer_mode.html#developer-mode).

  2. Vaya a Ventas ‣ Configuración ‣ Ajustes ‣ Conectores ‣ Sincronización con Amazon ‣ Plataformas de venta de Amazon.

  3. Haga clic en Nuevo para crear un nuevo registro de marketplace.

  4. Ingrese el ID del marketplace en el campo Identificador API y seleccione la región de Amazon correspondiente tal y como se describe en la [documentación de Amazon sobre los ID y regiones del marketplace](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). Escriba la URL de la Seller Central como se especifica en la [documentación de Amazon para las URL de la Seller Central](https://developer-docs.amazon.com/sp-api/docs/seller-central-urls).

  5. Establezca el nombre del registro como `Amazon.<country code>` para acceder con facilidad (por ejemplo, `Amazon.se`). Los campos identificador API, región y URL de Seller Central deben contener respectivamente los valores de _Marketplace ID_ , la región de Amazon seleccionada y la _URL de Seller Central_ de la documentación de Amazon.

  6. Una vez hecho esto, actualice la configuración de la cuenta de Amazon en Ventas ‣ Configuración ‣ Ajustes ‣ Conectores ‣ Sincronización de Amazon ‣ Cuentas de Amazon.

  7. Seleccione la cuenta en la que quiere usar el marketplace nuevo, para eso vaya a la pestaña Marketplaces y haga clic en actualizar los marketplaces disponibles; aparecerá una animación donde se confirmará que la operación se realizó con éxito. Los marketplaces nuevos se agregarán de forma automática a la lista de marketplaces sincronizados. Si un marketplace nuevo no se agrega a la lista, significa que o es incompatible o no está disponible para la cuenta del vendedor.

Ver también

  * [Funciones del Conector de Amazon](features.html)

  * [Gestión de órdenes de Amazon](manage.html)

