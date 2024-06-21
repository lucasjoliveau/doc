# Configuración de Sendcloud

Sendcloud es un agregador de servicio de envío que facilita la integración de
transportistas europeos en Konvergo ERP. Una vez integrado, los usuarios pueden
seleccionar transportistas en las operaciones de inventario de su base de
datos de Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/360059470491-Konvergo ERP-integration">Documentación de Sendcloud sobre la integración</a></p>
</div>

## Configuración en Sendcloud

### Crear una cuenta y activar transportistas

Para empezar, vaya a la [plataforma de Sendcloud](https://www.sendcloud.com)
para configurar su cuenta y generar las credenciales de conector. Inicie
sesión con su cuenta de Sendcloud, o cree una si es necesario.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para crear una nueva cuenta, Sendcloud le solicitará un número de identificación tributaria o un número <abbr title="Registro e identificación de operadores económicos">EORI</abbr>. Tras completar la configuración de la cuenta, active (o desactive) los transportistas que utilizará en la base de datos de Konvergo ERP.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La integración de Konvergo ERP con Sendcloud funciona en los planes gratuitos de Sendcloud <em>solo</em> si vincula una cuenta bancaria, pues Sendcloud no realiza envíos de forma gratuita. <b>Necesita</b> un plan de pago de Sendcloud para poder utilizar reglas de envío o contactos de transportistas personalizados.</p>
</div>

### Configuración del almacén

Una vez que inice sesión en la cuenta de Sendcloud, vaya a Ajustes ‣ Envío ‣
Direcciones y complete el campo **dirección de almacén**.

![Agregar direcciones en los ajustes de
Sendcloud.](../../../../../_images/settings-shipping.png)

Para permitir que Sendcloud también procese devoluciones se necesita de una
**dirección de devolución**. En la sección **varios** , hay un campo
denominado **nombre de la dirección (opcional)**. Ahí debe ingresar el nombre
del almacén en Konvergo ERP, y los caracteres deben ser exactamente los mismos.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><b>Configuración en Sendclould</b></div>
<div class="line"><b>Varios</b></div>
<div class="line"><b>Nombre de la dirección (opcional)</b>: <code>Almacén #1</code></div>
<div class="line"><b>Marca</b>: <code>Predeterminada</code></div>
</div>
<div class="line-block">
<div class="line"><b>Configuración del almacén en Konvergo ERP</b></div>
<div class="line"><b>Almacén</b>: <code>Almacén #1</code></div>
<div class="line"><b>Nombre corto</b>: <code>WH</code></div>
<div class="line"><b>Empresa</b>: <code>Mi empresa (San Francisco)</code></div>
<div class="line"><b>Dirección</b>: <code>Mi empresa (San Francisco)</code></div>
</div>
<p>Observe como la información ingresada en el campo <b>almacén</b> para ambas configuraciones es exactamente igual.</p>
</div>

### Generar credenciales de Sendcloud

En su cuenta de Sendcloud, vaya a Ajustes ‣ Integraciones en el menú a la
derecha. A continuación, busque **Konvergo ERP nativo** y después haga clic en
**conectar**.

Tras hacer clic en **conectar** , la página lo redirigirá a la página de
ajustes **API de Sendcloud** en donde se generan las **claves pública y
secreta**. El siguiente paso es darle un nombre a la **integración**. La
convención para los nombres es la siguiente: `Konvergo ERP NombredelaEmpresa`, en
donde `NombredelaEmpresa` es el nombre de la empresa del usuario (por ejemplo,
`Konvergo ERP StealthyWood`).

Después, seleccione la casilla a lado de **Puntos de servicio** y seleccione
los servicios de envío para esta integración. Después de guardar, se generan
las **claves pública y secreta**.

![Configuración de la integración con Sendcloud para recibir las
credenciales.](../../../../../_images/public-secret-keys.png)

## Configuración en Konvergo ERP

Para garantizar una integración fluida de Sendcloud con Konvergo ERP, instale y
vincule el conector de envío de Sendcloud a la cuenta de Sendcloud. Después,
configure los campos de Konvergo ERP para que Sendcloud pueda extraer con precisión
los datos de envío para generar etiquetas.

### Instalar el módulo Envío por Sendcloud

Después de que haya configurado la cuenta de Sendcloud, es momento de
configurar la base de datos de Konvergo ERP. Para empezar, vaya al módulo
**Aplicaciones** de Konvergo ERP, busque la integración de `Envío por Sendcloud` e
instálela.

![Módulo de envío por Sendcloud en el módulo Aplicaciones de
Konvergo ERP.](../../../../../_images/sendcloud-mod.png)

### Configuración del conector de envío por Sendcloud

Una vez instalado, active el módulo **Envío por Sendcloud** en Inventario ‣
Configuración ‣ Ajustes. El ajuste **conector de Sendcloud** se encuentra en
la sección **conectores de envío**.

Después de activar el **conector de Sendcloud** , haga clic en el enlace de
**métodos de envío de Sendcloud** que se encuentra debajo del conector. Una
vez que esté en la página de **métodos de envío** , haga clic en **crear**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede acceder a los <b>métodos de envío</b> en Inventario ‣ Configuración ‣ Entrega ‣ Métodos de envío.</p>
</div>

Complete los siguientes campos del formulario del **nuevo método de envío**
form:

  * **Método de envío** : escriba `Sendcloud DPD`.

  * **Proveedor** : seleccione **Sendcloud** en el menú desplegable.

  * **Producto de envío** : establezca el producto que se configuró para este método de envío o cree un nuevo producto.

  * En la pestaña **configuración de SendCloud** , introduzca la **clave pública de Sendcloud**.

  * En la pestaña **configuración de SendCloud** , introduzca la **clave secreta de Sendcloud**.

  * **Guarde** el formulario de forma manual al hacer clic en el icono de nube a lado de las migas de pan **Métodos de envío / Nuevo**.

Después de configurar y guardar el formulario, siga los siguientes pasos para
guardar los productos de envío:

  * En la pestaña **configuración de SendCloud** del formulario del **nuevo método de envío** haga clic en el enlace que dice **Cargar sus productos de envío de Sendcloud**.

  * Seleccione los productos de envío que la empresa desea usar para entregas y devoluciones.

  * Haga clic en **Seleccionar**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Ejemplo de productos enviados por Sendcloud configurados en Konvergo ERP:</p>
<div class="line-block">
<div class="line"><b>ENVÍO</b></div>
<div class="line"><b>Tipo de envío</b>: <code>DPD Home 0-31.5kg</code></div>
<div class="line"><b>Transportista</b>: <code>DPD</code></div>
<div class="line"><b>Peso mínimo</b>: <code>0.00</code></div>
<div class="line"><b>Peso máximo</b>: <code>31.50</code></div>
</div>
<p><b>Países</b>: <code>Austria</code> <code>Bélgica</code> <code>Bosnia y Herzegovina</code> <code>Bulgaria</code> <code>Croacia</code> <code>República Checa</code> <code>Dinamarca</code> <code>Estonia</code> <code>Finlandia</code> <code>Francia</code> <code>Alemania</code> <code>Grecia</code> <code>Hungría</code> <code>Islandia</code> <code>Irlanda</code> <code>Italia</code> <code>Letonia</code> <code>Liechtenstein</code> <code>Lituania</code> <code>Luxemburgo</code> <code>Mónaco</code> <code>Países Bajos</code> <code>Noruega</code> <code>Polonia</code> <code>Portugal</code> <code>Rumanía</code> <code>Serbia</code> <code>Eslovaquia</code> <code>Eslovenia</code> <code>España</code> <code>Suecia</code> <code>Suiza</code></p>
<div class="line-block">
<div class="line"><b>DEVOLUCIÓN</b></div>
<div class="line"><b>Tipo de devolución</b>: <code>DPD Return 0-20kg</code></div>
<div class="line"><b>Transportista</b>: <code>DPD</code></div>
<div class="line"><b>Peso mínimo</b>: <code>0.00</code></div>
<div class="line"><b>Peso máximo</b>: <code>20.00</code></div>
<div class="line"><b>Países</b>: <code>Bélgica</code> <code>Países Bajos</code></div>
</div>
</div> ![Ejemplo de productos de envío configurados en
Konvergo ERP:](../../../../../_images/sendcloud-example.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Sendcloud no proporciona claves de prueba cuando una empresa prueba el envío de productos desde Konvergo ERP. Esto supone que, si crea un paquete, se le hará un cargo a su cuenta de Sendcloud, a menos que cancele el envío en las primeras 24 horas de su creación.</p>
<p>Konvergo ERP tiene una capa de protección incorporada contra cargos no deseados al usar entornos de prueba. Si se encuentra dentro de un entorno de prueba y utiliza un método de envío para crear etiquetas, esas etiquetas se cancelan de forma automática después de su creación. Es posible alternar entre los ajustes del entorno de prueba y de producción con sus respectivos botones inteligentes.</p>
</div>

### Información de envío

Si quiere usar Sendcloud para generar etiquetas de envío, **debe** llenar la
siguiente información de forma correcta y total en Konvergo ERP:

  1. **Información del cliente** : al crear una cotización, asegúrese que el número telefónico, la dirección de correo electrónico y la dirección de envío del **cliente** sean válidas.

Para verificar, seleccione el campo **Cliente** para abrir su página de
contacto. Ahí agregue la dirección de envío en el campo **Contacto** , el
número de **celular** y la dirección de **correo electrónico**.

  2. **Peso del producto** : asegúrese de que todos los productos de una orden tengan un **peso** especificado en la pestaña **Inventario** de su formulario de producto. Consulte la [sección Peso del producto](third_party_shipper#inventory-shipping-receiving-configure-weight) de este artículo para obtener instrucciones detalladas.

  3. **Dirección del almacén** : asegúrese de que el nombre y la dirección del almacén en Konvergo ERP coincidan con el almacén definido con anterioridad en la configuración de Sendcloud. Consulte la [sección de configuración del almacén](third_party_shipper#inventory-shipping-receiving-configure-source-address) de la documentación externa de envíos para obtener detalles sobre la configuración del almacén en Konvergo ERP.

## Generar etiquetas con Sendcloud

Al crear una cotización en Konvergo ERP, agregue el envío y elija **Producto de envío
de Sendcloud** , luego **valide** la entrega. Los documentos de la etiqueta de
envío se generan de forma automática en el chatter e incluyen lo siguiente:

  1. **Etiqueta(s) de envío** según el número de paquetes.

  2. **Etiqueta(s) de devolución** si el conector de Sendcloud está configurado para devoluciones.

  3. **Documento(s) aduanero(s)** si el país de destino lo(s) requiere.

Además, ahora está disponible el número de rastreo.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Sendcloud hace un cargo automático a la cuenta configurada cuando se crean etiquetas de devolución.</p>
</div>

## Preguntas frecuentes

### El envío es demasiado pesado

Si el envío es demasiado pesado para el servicio de Sendcloud que se
configuró, entonces el peso se divide para simular varios paquetes. Los
productos tendrán que ser puestos en distintos **paquetes** para **validar**
el traslado y generar etiquetas.

También se pueden configurar **reglas** en Sendcloud para usar otros métodos
de envío cuando la carga es muy pesada. Sin embargo, tenga en cuenta que estas
reglas no se aplicarán al cálculo del precio de envío en el cálculo de la
orden de venta.

### Contratos de transportista

Para hacer uso de los precios personalizados de un contrato directo con los
transportistas puede subir un archivo CSV. Inicie sesión en Sendcloud, vaya a
Ajustes ‣ Transportistas ‣ Mis contratos y luego seleccione el contrato
correspondiente.

![Ir a la sección de contratos en
Sendcloud.](../../../../../_images/contracts.png)

En la sección **Precios del contrato** , haga clic en **Descargar CSV** y
complete los precios del contrato en la columna **Precio** de la plantilla del
archivo CSV.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Asegúrese de que el archivo CSV incluye los precios correctos para evitar cualquier error.</p>
</div> ![Visualización de un archivo CSV de contrato de muestra
desde Sendcloud, la columna de precios aparece con una flecha
roja.](../../../../../_images/price-csv.png)

Una vez que haya terminado de completarlo, **Suba** el archivo CSV a Sendcloud
y luego haga clic en **Guardar estos precios**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/5163547066004">Sendcloud: Cómo subir los precios de contrato con transportistas</a></p>
</div>

### Medición del peso volumétrico

Muchos transportistas tienen varias medidas de peso. Está el peso real de los
productos en el paquete y el _peso volumétrico_ (El peso volumétrico es el
volumen que ocupa un paquete cuando está en tránsito. Es decir, el tamaño
físico de un paquete).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para crear una nueva cuenta, Sendcloud le solicitará un número de identificación tributaria o un número <abbr title="Registro e identificación de operadores económicos">EORI</abbr>. Tras completar la configuración de la cuenta, active (o desactive) los transportistas que utilizará en la base de datos de Konvergo ERP.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para crear una nueva cuenta, Sendcloud le solicitará un número de identificación tributaria o un número <abbr title="Registro e identificación de operadores económicos">EORI</abbr>. Tras completar la configuración de la cuenta, active (o desactive) los transportistas que utilizará en la base de datos de Konvergo ERP.</p>
</div>1

### No es posible calcular la tarifa de envío

Primero verifique que el producto a enviar tenga un peso compatible con el
método de envío seleccionado. Si el peso es correcto, entonces verifique que
el país de destino (desde la dirección del cliente) sea compatible con el
transportista, lo mismo debe suceder con el país de origen (dirección del
almacén).

