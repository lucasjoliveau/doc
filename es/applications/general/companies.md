# Empresas

Un entorno de gestión centralizada le permite seleccionar varias empresas de
manera simultanea y configurar sus almacenes, clientes, equipos y contactos
específicos. Le brinda la capacidad de generar reportes de cifras agregadas
sin cambiar de interfaz, lo que facilita las tareas diarias y el proceso de
gestión general.

## Gestionar empresas y registros

Vaya a Ajustes ‣ Administrar empresas y complete el formulario con la
información de su empresa. Si selecciona una _Empresa matriz_ , los registros
se compartirán entre las dos empresas (siempre que ambos entornos estén
activos).

![Vista general del formulario de una nueva empresa en
Konvergo ERP](../../_images/create_js_store_us.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Active el <a href="developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> para elegir un <em>favicon</em> para cada una de sus empresas y así poder diferenciarlas con facilidad desde las pestañas de su navegador. Establezca el tamaño de los archivos de sus favicon en 16x16 o 32x32 pixeles. Se aceptan las extensiones JPG, PNG, GIF e ICO.</p>
<img alt="Vista de un navegador web y el favicon para una empresa específica elegida en Konvergo ERP" class="align-center" src="../../_images/favicon.png" style="height: 200px;"/>
</div>

Cambie o seleccione varias empresas habilitando sus casillas de selección para
activarlas. La empresa en gris es la que está en uso. Para cambiar de empresa,
haga clic en su nombre. En el siguiente ejemplo, el usuario tiene acceso a
tres empresas, dos están activadas y la que se está usando es _JS Store US_.

![Vista del menú de empresas a través del tablero principal en
Konvergo ERP](../../_images/multi_companies_menu_dashboard.png)

Los datos como productos, contactos y equipos se pueden compartir o configurar
para que se muestren solo para una empresa específica. Para ello, en sus
formularios, elija entre:

  * _Un campo en blanco_ : el registro se comparte con todas las empresas.

  * _Agregar una empresa_ : el registro es visible para los usuarios conectados a esa empresa específica.

![Vista del formulario de un producto enfatizando el campo de la empresa en
Ventas de Konvergo ERP](../../_images/product_form_company.png)

## Acceso de empleados

Una vez que haya creado las empresas puede gestionar los [permisos de
acceso](users/access_rights) de sus empleados para _Multiempresas_.

![Vista de un formulario de usuario enfatizando el campo de multiempresas bajo
las pestañas de permisos de acceso en
Konvergo ERP](../../_images/access_rights_multi_companies.png)

Si un usuario tiene varias empresas _activas_ en su base de datos y está
**editando** un registro, la edición se realiza en la empresa relacionada del
registro.

Ejemplo: si edita una orden de venta emitida en JS Store US mientras trabaja
en JS Store Belgium, los cambios se aplicarán en JS Store US (la empresa desde
la que se emitió la orden de venta).

Al **crear** un registro, la empresa que se toma en cuenta es:

  * La empresa actual (la que se encuentra activa) o,

  * No se establece ninguna empresa (en formularios de productos y contactos, por ejemplo) o,

  * La empresa establecida es la que está vinculada al documento (lo mismo que si se está editando un registro).

## Formato de los documentos

Para configurar los formatos de los documentos según la empresa, _active_ y
_seleccione_ el correspondiente y en _Ajustes_ , haga clic en _Configurar
diseño de documento_.

![Vista de la página de ajustes enfatizando el campo de diseño del documento
en Konvergo ERP](../../_images/document_layout.png)

## Transacciones dentro de la empresa

Primero, asegúrese de que cada una de sus empresas esté configurada
correctamente en lo referente a:

  * [Plan de cuentas](../finance/accounting/get_started/chart_of_accounts)

  * [Impuestos](../finance/accounting/taxes)

  * [Posiciones fiscales](../finance/accounting/taxes/fiscal_positions)

  * [Diarios](../finance/accounting/bank)

  * [Localizaciones fiscales](../finance/fiscal_localizations)

  * [Listas de precios](../sales/sales/products_prices/prices/pricing)

Active la opción _Transacciones entre empresas_ en _Ajustes_. Con la empresa
correspondiente _activada_ y _seleccionada_ , elija si desea que las
operaciones entre las empresas se sincronicen a nivel de facturas o a nivel de
órdenes.

![Vista de la página de ajustes enfatizando el campo de transacción entre
empresas en Konvergo ERP](../../_images/inter_company_transactions.png)

  * **Sincronizar facturas** : genera una factura cuando una empresa confirma una factura para la empresa seleccionada.

_Ejemplo:_ una factura registrada en JS Store Belgium, para JS Store US, crea
una factura de proveedor en JS Store US de forma automática desde JS Store
Belgium.

![Vista de una factura para JS Store US creada en JS Store Belgium en
Konvergo ERP](../../_images/invoice_inter_company.png)

  * **Sincronizar orden de compra o venta** : genera un borrador de orden de compra o venta utilizando el almacén de la empresa seleccionada cuando se confirma una orden de compra o venta para la empresa seleccionada. Si en lugar de un borrador de orden de compra o venta prefiere que se valide, active _Validación automática_.

_Ejemplo:_ cuando se confirma una orden de venta para JS Store US en JS Store
Belgium, se crea una orden de compra de forma automática en JS Store Belgium
(también se confirma si la función _Validación automática_ está activa).

![Vista de la compra creada en JS Store US desde JS Store Belgium en
Konvergo ERP](../../_images/purchase_order_inter_company.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los productos se tienen que configurar como <em>Se puede vender</em> y se deben compartir entre las empresas.</p>
</div>
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Recuerde probar todos los flujos de trabajo como un usuario que no sea administrador.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../developer/howtos/company">Lineamientos multiempresa</a></p></li>
<li><p><a href="../finance/accounting/get_started/multi_currency">Sistema multidivisa</a></p></li>
</ul>
</div>

  * [Correos electrónicos de resumen](companies/digest_emails)
  * [Plantillas de correo electrónico](companies/email_template)

