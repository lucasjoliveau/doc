# Integración con AvaTax

_AvaTax_ de Avalara es un software para impuestos basado en la nube. La
integración de _AvaTax_ con Odoo proporciona cálculos de impuestos en tiempo
real específicos para cada región cuando los usuarios venden, compran y
facturan artículos en Odoo. El cálculo del impuesto con _AvaTax_ es compatible
con todos los países de las Naciones Unidas y es posible realizar
transacciones transfronterizas.

Importante

 _AvaTax_ solo está disponible para su integración a bases de datos y empresas
ubicadas en Estados Unidos y Canadá. Esto significa que la posición fiscal o
el país de una base de datos solo puede configurarse en Estados Unidos o
Canadá. Consulte la siguiente documentación para obtener más información: País
fiscal.

_AvaTax_ contabiliza las tasas impositivas por ubicación para cada estado,
municipio o distrito y ciudad, además mejora la precisión de las remesas
gracias al uso de leyes, reglas, límites de jurisdicción y circunstancias
especiales (como exenciones fiscales y de productos). Las empresas que
integran _AvaTax_ pueden mantener el control interno del cálculo de sus
impuestos con esta sencilla integración de API.

Importante

Existen algunas limitaciones en Odoo al usar _AvaTax_ para calcular impuestos:

  * _AvaTax_ **no** es compatible con la aplicación _Punto de venta_ de Odoo. Un modelo de cálculo de impuestos dinámico es excesivo para las transacciones que corresponden a una sola dirección de entrega, como tiendas o restaurantes.

  * _AvaTax_ y Odoo usan la dirección de la empresa, **no** la del almacén.

  * El impuesto sobre el consumo **no** es compatible. Este incluye impuestos al tabaco, cigarros electrónicos, vaporizadores, combustibles y otros sectores específicos.

Ver también

Documentos de apoyo de Avalara: [Sobre
AvaTax](https://community.avalara.com/support/s/document-
item?language=en_US&bundleId=dqa1657870670369_dqa1657870670369&topicId=About_AvaTax.html&_LANG=enus)

## Configuración en AvaTax

Para usar _AvaTax_ necesita una cuenta de Avalara para su configuración. En
caso de que no haya configurado una, contacte a Avalara para comprar una
licencia: [Avalara: contacto (en inglés)](https://www.avalara.com/us/en/get-
started.html).

Truco

Luego de configurar la cuenta deberá conservar el ID de la cuenta de _AvaTax_
ya que es necesario durante el proceso de configuración en Odoo. En Odoo, este
número es el ID de la API.

Después [cree un perfil básico de la
empresa](https://community.avalara.com/support/s/document-
item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Create_a_Basic_company_profile.html&_LANG=enus).

### Crear un perfil básico de la empresa

Para el siguiente paso deberá tener a la mano detalles esenciales del negocio,
tales como las ubicaciones donde se recaudan impuestos, los productos y
servicios vendidos (y sus ubicaciones de ventas) y las exenciones de impuestos
al cliente, en caso de que las haya. Siga la documentación de Avalara para
crear un perfil básico para la empresa:

  1. [Agregar información de la empresa](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_your_company_information.html&_LANG=enus).

  2. [Lugares de recaudación y pago de impuestos de la empresa](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Tell_us_where_you_collect_and_pay_tax.html&_LANG=enus).

  3. [Verificar jurisdicciones y activar la empresa](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Verify_your_jurisdictions_and_activate_your_company.html&_LANG=enus).

  4. [Agregar otras ubicaciones en las que la empresa también declara impuestos](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_other_company_locations_for_location-based_filing.html&_LANG=enus).

  5. [Agregar un mercado al perfil de la empresa](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_marketplace_transactions_to_your_company_profile.html&_LANG=enus).

### Conexión con AvaTax

Conéctese a _AvaTax_ después de crear el perfil básico de la empresa en
Avalara. Este paso vincula a Odoo y _AvaTax_ de forma bidireccional.

Vaya al entorno de [prueba](https://sandbox.admin.avalara.com/) o de
[producción](https://admin.avalara.com/) de Avalara, este dependerá del tipo
de cuenta de Avalara que la empresa desee integrar.

Ver también

[Entorno de pruebas y de producción en
Avalara](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-
vs-production.html).

Inicie sesión para crear una clave de licencia. Vaya a Ajustes ‣ Licecia y
claves API y luego haga cic en Generar clave de licencia.

Nota

El siguiente mensaje aparece como advertencia: `Si su aplicación empresarial
está conectada a las soluciones de Avalara, la conexión no funcionará hasta
que actualice la aplicación con la nueva clave de licencia. Esta acción no se
puede deshacer.`

Generar una nueva licencia rompe la conexión con las aplicaciones
empresariales existentes que usan la integración con _AvaTax_. Asegúrese de
actualizarlas y usar la nueva clave.

Haga clic en Generar clave de licencia si esta es la primera integración API
que realiza entre _AvaTax_ y Odoo.

Asegúrese de que la conexión anterior se puede romper en caso de que se trate
de una clave de licencia adicional. **Solo** hay una clave de licencia
asociada con cada una de las cuentas de prueba y producción de Avalara.

Importante

Copie esta clave en un lugar seguro. Le **recomendamos** que almacene una
copia de la clave de licencia para futuras referencias, pues no podrá
recuperarla luego de salir de esta pantalla.

## Configuración en Odoo

Antes de usar _AvaTax_ es necesario que haga algunos ajustes adicionales en
Odoo para asegurar que los impuestos se calculen de manera precisa.

Verifique que la base de datos de Odoo contiene los datos necesarios. El país
que estableció en la base de datos determina la posición fiscal y ayuda a
_AvaTax_ a calcular los tipos impositivos exactos.

### País fiscal

Vaya a Contabilidad ‣ Configuración ‣ Ajustes para establecer el país fiscal.

Ver también

[Localizaciones fiscales](../../fiscal_localizations.html)

Seleccione Estados Unidos o Canada en la parte de País fiscal en la sección
Impuestos, después haga clic en Guardar.

### Ajustes de la empresa

Todas las empresas que operan en la base de datos de Odoo deben tener
establecida una dirección completa. Vaya a Ajustes y busque la sección
Empresas, verifique que solo haya una empresa operando la base de datos de
Odoo. Haga clic en Actualizar información para abrir otra página en la que
podrá actualizar sus detalles.

Haga clic en Administrar empresas en caso de que haya varias operando en la
base de datos. Esta acción abrirá una lista con las empresas que puede
seleccionar. Haga clic en una empresa específica para actualizar su
información.

Los administradores de la base de datos deben asegurarse de que los campos
Calle…, Calle 2…, Ciudad, Estado, Código postal y País estén actualizados en
todas las empresas.

Esto garantiza que el cálculo de los impuestos sea preciso y que no existan
errores en las operaciones contables de fin de año.

Ver también

  * [Empresas](../../../general/companies.html)

  * [Información básica](../get_started.html)

### Instalación del módulo

A continuación, asegúrese de que el módulo _AvaTax_ de Odoo está instalado.
Vaya a Aplicaciones, escriba `avatax` en la barra de búsqueda y presione
`Enter`. Aparecerán los siguientes resultados:

Nombre | Nombre técnico | Descripción  
---|---|---  
Avatax | `account_avatax` | El módulo de _AvaTax_ predeterminado. Este módulo agrega las funciones de base de _AvaTax_ para calcular impuestos.  
AvaTax para órdenes de venta | `account_avatax_sale` | Incluye la información necesaria para calcular los impuestos sobre las órdenes de venta en Odoo.  
AvaTax para suscripciones | `account_avatax_sale_subscription` | Este módulo incluye las funciones necesarias para calcular impuestos en las suscripciones en Odoo.  
Cuenta de AvaTax - Comercio electrónico | `website_sale_account_avatax` | Incluye las funciones para el cálculo de impuestos del proceso de pago en la aplicación Comercio electrónico de Odoo.  
Cuenta de AvaTax - Comercio electrónico - Entrega | `website_sale_delivery_avatax` | Incluye las funciones para el cálculo de impuestos del proceso de entrega en la aplicación Comercio electrónico de Odoo.  
  
Haga clic en el botón Instalar del módulo AvaTax: `account_avatax`. Al
hacerlo, instalará lo siguiente:

  * AvaTax: `account_avatax`

  * AvaTax para órdenes de venta: `account_avatax_sale`

  * Cuenta de AvaTax - Comercio electrónico: `website_sale_account_avatax`

Si necesita usar _AvaTax_ en la aplicación _Suscripciones_ o para los
impuestos de entrega en la aplicación _Comercio electrónico_ , haga clic en
Instalar en cada uno de esos módulos.

### Ajustes de AvaTax en Odoo

Vaya a Contabilidad ‣ Configuración ‣ Ajustes para integrar la API de _AvaTax_
con Odoo. Debe hacer los ajustes y agregar las credenciales en los campos de
AvaTax en la sección de Impuestos.

![Configuración de ajustes de AvaTax](../../../../_images/avatax-
configuration-settings.png)

#### Prerrequisitos

Primero seleccione el entorno en el que la empresa desea usar _AvaTax_. Puede
ser el entorno de prueba o el de producción.

Ver también

Consulte [el siguiente documento (en
inglés)](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-
vs-production.html) si necesita ayuda para determinar el entorno de _AvaTax_
que debe usar (si producción o prueba).

#### Credenciales

Ahora proporcione las credenciales. Escriba el ID de la cuenta de _AvaTax_ en
el campo ID de la API y la clave de la licencia en el campo Clave API.

Importante

El ID de cuenta está disponible al iniciar sesión en el portal de _AvaTax_
([entorno de prueba](https://sandbox.admin.avalara.com/) o
[producción](https://admin.avalara.com/)). En la esquina superior derecha,
haga clic en las iniciales del usuario y luego en Cuenta. El ID de cuenta es
el primero que aparece.

Consulte esta documentación: Conexión con AvaTax. Le permitirá acceder a la
clave de la licencia.

En el campo Código de la empresa deberá proporcionar el código correspondiente
de Avalara que pertenece a la empresa que está configurando. En caso de que no
lo haga, Avalara lo interpretará como `DEFAULT`, es decir, predeterminado.
Puede acceder al código de la empresa en el portal administrativo de Avalara.

Primero inicie sesión en el portal de _AvaTax_ (en el entorno de
[prueba](https://sandbox.admin.avalara.com/) o de
[producción](https://admin.avalara.com/)) y después vaya a Ajustes ‣
Administrar empresas. El valor del código de la empresa está en la fila
Empresa de la columna Código de la empresa.

![Código de la empresa de AvaTax, aparece en un recuadro rojo en la página de
detalles de la empresa.](../../../../_images/company-code.png)

#### Opciones transaccionales

Hay dos ajustes transaccionales para _AvaTax_ que puede configurar: Usar UPC y
Confirmar transacciones.

Si la casilla junto a Usar UPC está seleccionada, las transacciones usarán los
códigos universales de producto (UPC) en lugar de los códigos personalizados
definidos en Avalara. Consulte a un contador público certificado (CPA) para
recibir orientación particular.

Si la casilla Confirmar transacciones está seleccionada, entonces las
transacciones en la base de datos de Odoo se confirmarán para reportarlas en
_AvaTax_.

#### Validación de dirección

La función _Validación de la dirección_ garantiza que la dirección más
actualizada según las normas postales sea la que está establecida en un
contacto en Odoo. Esto es importante para que el cálculo de los impuestos de
los clientes sea preciso.

Importante

La función Validación de la dirección solo funciona con contactos y clientes
en América del Norte.

Seleccione la casilla junto al campo Validación de la dirección.

Importante

Para que los cálculos de los impuestos sean exactos, lo ideal sería que los
contactos que almacena en su base de datos cuenten con una dirección completa.
Sin embargo, es probable que _AvaTax_ haga un intento de implementación solo
con el país, estado y código postal., pues estos tres campos son obligatorios.

Guarde los ajustes para implementar la configuración.

Truco

Seleccione un contacto y valide su dirección de forma manual en la aplicación
Contactos. Después de que configuró el módulo _AvaTax_ en la base de datos, el
botón Validar aparece abajo de la dirección.

Haga clic en Validar, después aparecerá una ventana emergente con la dirección
validada y la dirección original. Haga clic en Guardar validada si la
dirección validada es correcta y debe usarla con propósitos fiscales.

![Ventana emergente de validación de dirección en Odoo con el botón "Guardar
validada" y "Dirección validada"  dentro de un recuadro
rojo.](../../../../_images/validate-address.png)

Advertencia

Es necesario que valide todas las direcciones de contactos en la base de datos
de Odoo que ya había proporcionado con anterioridad y deberá usar el proceso
de validación manual antes descrito. Las direcciones no se validan de forma
automática si ya las tenía configuradas, esto solo ocurre al calcular los
impuestos.

#### Probar conexión

Haga clic en Probar conexión después de introducir toda la información
anterior en los ajustes de _AvaTax_ en Odoo. Esto asegura que el ID de la API
y la clave API sean correctos, además realiza una conexión entre Odoo y la
interfaz de programación de aplicaciones (API) de _AvaTax_.

#### Sincronizar parámetros

Al finalizar la configuración y los ajustes de la sección _AvaTax_ haga clic
en el botón Sincronizar parámetros. Esta acción sincroniza los códigos de
exención de _AvaTax_.

### Posición fiscal

Vaya a Contabilidad ‣ Configuración ‣ Contabilidad: Posiciones fiscales.
Aparece una posición fiscal con el nombre Mapeo automático de impuestos
(AvaTax), haga clic en ella para abrir la página de configuración de la
posición fiscal de _AvaTax_.

Asegúrese de que la casilla Usar la API de AvaTax esté seleccionada.

También puede seleccionar la casilla junto al campo Detectar de forma
automática. En caso de que habilite esta opción, esta posición fiscal aplicará
de forma automática a las transacciones en Odoo.

Al activar Detectar de forma automática también hace que aparezcan algunos
parámetros específicos, como si se requiere número de identificación
tributaria, la identificación fiscal extranjera, el grupo de países, el país,
los estados federales o el rango postal. Al completar estos parámetros
filtrará el uso de la posición fiscal, pero si los deja vacíos todos los
cálculos se realizarán con esta posición fiscal.

Advertencia

Si no selecciona la casilla Detectar de forma automática entonces deberá
configurar la posición fiscal de cada cliente en la pestaña Ventas y compra de
su registro. Vaya a Ventas ‣ Órdenes ‣ Clientes o a Contactos ‣ Contactos y
seleccione al cliente para establecer una posición.

Vaya a la pestaña Ventas y compra y busque la sección Información fiscal. Ahí,
busque el campo Posición fiscal y establezca una.

Ver también

[Posiciones fiscales (mapeo de impuestos y cuentas)](fiscal_positions.html)

#### Cuentas de AvaTax

La pestaña AvaTax aparece al seleccionar la casilla Usar API de AvaTax. Haga
clic en esta pestaña para abrir otros dos ajustes.

El primer ajuste es para la cuenta de facturación de AvaTax y el segundo es
para la cuenta de reembolso de AvaTax. Para que su cierre contable anual sea
correcto deberá asegurarse de que ambas cuentas están configuradas. Consulte a
un contador público certificado (CPA) para recibir orientación específica
sobre cómo configurar ambas cuentas.

Haga clic en Guardar para implementar los cambios.

### Mapeo de impuestos

La integración con _AvaTax_ está disponible en las órdenes de venta y facturas
con la posición fiscal de _AvaTax_ incluida.

#### Mapeo de categorías de producto

Especifique una categoría de AvaTax en las categorías de productos antes de
usar la integración. Vaya a Inventario ‣ Configuración ‣ Categorías de
productos y seleccione aquella en la que desea agregar la Categoría de AvaTax.
Seleccione una categoría del menú desplegable del campo Categoría de AvaTax o
haga clic en Buscar más… para abrir la lista completa de opciones.

![Especificar la categoría de AvaTax en los
productos.](../../../../_images/avatax-category.png)

#### Mapeo de productos

Las categorías de _AvaTax_ también se pueden configurar en cada producto. Para
configurar la categoría de AvaTax, vaya a Inventario ‣ Productos ‣ Productos y
seleccione el producto al que desea agregar esta categoría. En la pestaña
Información general, a la derecha, hay un campo de selección etiquetado con
Categoría de AvaTax. Por último, haga clic en el menú desplegable y seleccione
una categoría o haga clic en Buscar más… para elegir una que no esté en la
lista.

Nota

Si el producto y su categoría tienen una categoría de AvaTax configurada,
entonces la categoría de AvaTax del producto tiene prioridad.

![Anule categorías de productos si es
necesario.](../../../../_images/override-avatax-product-category.png)

Importante

Es necesario que asigne una categoría de AvaTax al _producto_ o a la
_categoría de Producto_ para cada uno de estos, según la ruta que elija.

Ver también

  * [Posiciones fiscales (mapeo de impuestos y cuentas)](fiscal_positions.html)

  * [Uso de AvaTax](avatax/avatax_use.html)

  * [Portal de Avalara (AvaTax)](avatax/avalara_portal.html)

  * [Cumplimiento fiscal en Estados Unidos: video de eLearning sobre AvaTax](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)

  * [Uso de AvaTax](avatax/avatax_use.html)
  * [Portal de Avalara (AvaTax)](avatax/avalara_portal.html)

  *[API]: Interfaz de programación de aplicaciones

