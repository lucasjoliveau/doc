# Egipto

## Instalación

[Instale](../../general/apps_modules#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Egipto:

Nombre | Nombre técnico | Descripción  
---|---|---  
**Egipto - Contabilidad** | `l10n_eg` | [Paquete de localización fiscal](../fiscal_localizations#fiscal-localizations-packages) predeterminado  
**Integración de la facturación electrónica para Egipto** | `l10n_eg_edi_eta` | Integración de la facturación electrónica de la Administración Tributaria Egipcia (ETA)  
  
## Facturación electrónica para Egipto

Konvergo ERP cumple con los requisitos de **facturación electrónica de la
Administración Tributaria Egipcia (ETA)**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La facturación electrónica en Egipto está disponible para Konvergo ERP 16.0. Si es necesario, <a href="../../../administration/upgrade">actualice</a> su base de datos.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Video: facturción electrónica para Egipto</a></p></li>
<li><p><a href="../../../administration/upgrade">Actualizar</a></p></li>
</ul>
</div>

### Registre Konvergo ERP en su portal ETA

Debe registrar su sistema Konvergo ERP ERP en el portal de la ETA para obtener sus
credenciales de API. Estos códigos son necesarios para configurar la
aplicación Contabilidad de Konvergo ERP.

Acceda al perfil de su empresa en el portal de la ETA, haga clic en **View
Taxpayer Profile** (Ver perfil del contribuyente).

![Clic en el botón "Ver perfil del contribuyente" en un portal de facturación
de la ETA](../../../_images/taxpayer-profile.png)

Después vaya a la sección **representantes** y haga clic en **Register ERP**
(registrar ERP). Complete el **nombre del ERP** (por ejemplo, `Konvergo ERP`) y deje
los otros campos vacíos.

![Llenado del formulario para registrar un sistema de ERP en el portal de la
ETA.](../../../_images/add-erp-system.png)

Una vez que se registró de manera exitosa, el sitio web le muestra sus
credenciales de API:

  * ID de cliente

  * Secreto de cliente 1

  * Secreto de cliente 2

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>La ETA debe proporcionarle un nombre de usuario y una contraseña para ingresar a su portal en línea.</p></li>
<li><p>Solicite a la ETA que también le otorgue acceso al portal de preproducción.</p></li>
<li><p>Estos códigos son confidenciales, almacénelos en un lugar seguro.</p></li>
</ul>
</div>

### Configuración en Konvergo ERP

Para conectar su base de datos de Konvergo ERP a su cuenta del portal de la ETA, vaya
a Contabilidad ‣ Configuración ‣ Ajustes ‣ Ajustes de facturación electrónica
de la ETA, y escriba el **ID de cliente de la ETA** y el **secreto de la ETA**
que recibió cuando registró Konvergo ERP en su portal de la ETA. En caso de ser
necesario, proporcione un límite de facturación.

![Configuración de las credenciales de facturación electrónica de la ETA en la
aplicación Contabilidad de Konvergo ERP](../../../_images/eta-api-integration.png)
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p><b>Realice pruebas en su portal de preproducción</b> antes de comenzar a emitir facturas reales en el portal de producción de la ETA.</p></li>
<li><p>Las <b>credenciales</b> para los entornos de preproducción y producción son distintas, asegúrese de actualizarlas en Konvergo ERP cuando cambie de un entorno a otro.</p></li>
<li><p>Si aún no lo ha hecho, complete los detalles de su empresa con la dirección completa, país y número de identificación fiscal.</p></li>
</ul>
</div>

#### Códigos de la ETA

La facturación electrónica trabaja con un conjunto de códigos proporcionados
por la ETA, puede utilizar la [documentación de la
ETA](https://sdk.preprod.invoicing.eta.gov.eg/codes/) para agregar códigos a
los atributos de su empresa.

Konvergo ERP se encarga de la mayoría de estos códigos de forma automática siempre que
sus sucursales, clientes y productos estén configurados de manera correcta.

  * Información de la empresa:

    * Número de identificación fiscal de la empresa:

    * ID de la sucursal

Utilice `0` como código si solo tiene una.

    * Código de tipo de actividad

  * Otra información:

    * Códigos de producto

Los productos de su empresa deben contener el código y corresponder con sus
códigos **GS1** o **EGS**.

    * Código fiscal

La mayoría de los códigos fiscales ya están configurados en Konvergo ERP, en el campo
de **Código de la ETA (Egipto)**. Le recomendamos comprobar que estos
corresponden con los impuestos de su empresa.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://sdk.preprod.invoicing.eta.gov.eg/codes/">SDK de facturación y recibos electrónicos - Tablas de código</a></p></li>
<li><p><a href="../accounting/taxes">Impuestos</a></p></li>
</ul>
</div>

#### Sucursales

Cree un contacto y un diario para cada sucursal de su empresa y configure sus
ajustes de la ETA.

Para realizar esto, vaya a Contabilidad ‣ Configuración ‣ Diarios y haga clic
en **Crear**.

Agregue un nombre para el diario según la sucursal de su empresa y como
**tipo** seleccione **ventas**. Después, abra la pestaña ajustes avanzados y
complete la sección **ajustes de la ETA (Egipto)** :

  * Seleccione al contacto de la sucursal o cree uno en el campo **sucursal**.

  * Establezca el **código de actividad ETA**.

  * Establezca el **ID de la sucursal ETA** (utilice `0` si solo tiene una).

![Configuración del diario de ventas para la sucursal de una empresa en
Egipto](../../../_images/branch-journal.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>El contacto seleccionado en el campo <b>sucursal</b> debe ser una <b>empresa</b> (<b>no</b> un <b>individuo</b>) y debe completar los campos <b>dirección</b> e <b>ID fiscal</b>.</p>
</div>

#### Clientes

Asegúrese de completar correctamente los formularios de contacto de sus
clientes para que sus facturas electrónicas sean válidas:

  * **Tipo de contacto** : **individuo** o **empresa**.

  * **País**

  * **ID fiscal** : el ID fiscal es el registro en caso de las empresas y el ID nacional para los individuos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede editar los formularios de contacto de sus clientes en Contabilidad ‣ Clientes ‣ Clientes.</p>
</div>

#### Productos

Asegúrese de configurar correctamente sus productos para que sus facturas
electrónicas sean válidas:

  * **Tipo de producto** : productos almacenables, consumibles o servicios.

  * **Unidad de medida** : si también utiliza la aplicación Inventario de Konvergo ERP y habilitó las [unidades de medida](../../inventory_and_mrp/inventory/product_management/product_replenishment/uom).

  * **Código de barras** : código de barras **GS1** o **EGS**.

  * **Código de artículo ETA** (en la pestaña Contabilidad): si el código de barras no coincide con su código de artículo ETA.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede editar sus productos en Contabilidad ‣ Clientes ‣ Productos.</p>
</div>

### Autenticación por USB

Todas las personas que necesiten firmar facturas de forma electrónica
necesitan una clave USB específica para autenticar y enviar facturas al portal
de la ETA mediante un ERP.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede contactar a la Autoridad Fiscal Egipcia o a <a href="https://www.egypttrust.com/">Egypt Trust</a> para obtener sus claves USB.</p>
</div>

#### Instalar Konvergo ERP como proxy local en su computadora

Un servidor local de Konvergo ERP funciona como enlace entre su computadora y su base
de datos de Konvergo ERP alojada en línea.

Descargue el instalador de Konvergo ERP Community desde la página
<https://www.odoo.com/page/download> y comience la instalación en su
computadora.

Seleccione **modo de proxy local** como tipo de instalación.

![Selección de "modo de proxy local" durante la instalación de Konvergo ERP
Community.](../../../_images/install-odoo-local-proxy.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La instalación de Konvergo ERP solo funciona como servidor y no instala ninguna aplicación de Konvergo ERP en su computadora.</p>
</div>

Una vez que la instalación está completa, el **token de acceso** para el proxy
local de Konvergo ERP aparece en el instalador. Cópielo y almacénelo en un lugar
seguro para usarlo después.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Video: facturción electrónica para Egipto</a></p></li>
<li><p><a href="../../../administration/upgrade">Actualizar</a></p></li>
</ul>
</div>0

#### Configurar la clave USB

Una vez que instale el servidor proxy local en su computadora, puede
vincularlo a su base de datos de Konvergo ERP.

  1. Vaya a Contabilidad ‣ Configuraciones ‣ USB y haga clic en **crear**.

  2. Escriba el nombre de la **empresa** , el **NIP en USB de la ETA** que le proporcionó su proveedor de clave USB y el **token de acceso** que se le proporcionó al final de la instalación del proxy local. Luego, haga clic en **guardar**.

  3. Haga clic en **obtener certificado**.

![Creación de un nuevo USB para la facturación electrónica de una empresa en
Egipto.](../../../_images/thumb-drive.png)

