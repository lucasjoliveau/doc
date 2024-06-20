# Uso de AvaTax

AvaTax es un software para calcular impuestos que se puede integrar con Odoo
en los Estados Unidos y Canadá. Una vez que haya terminado la [configuración
de la integración](../avatax.html), el cálculo de los impuestos es fácil y
automático.

## Cálculo de impuestos

Para poder calcular impuestos en las cotizaciones y facturas de Odoo con
AvaTax primero debe confirmar los documentos en el flujo de ventas. También
puede calcular los impuestos de forma manual con el botón Calcular impuestos
con AvaTax cuando los documentos estén en borrador.

Truco

Si hace clic en el botón Calcular impuestos con AvaTax los impuestos se
volverán a calcular si cualquiera de las líneas de producto se editan en la
factura.

![Una cotización de venta con los botones para confirmar y calcular impuestos
con AvaTax resaltados.](../../../../../_images/calculate-avatax.png)

El cálculo de impuestos se activa durante la siguiente activación automática y
la siguiente activación manual.

### Activaciones automáticas

  * Cuando el representante de ventas envía la cotización por correo electrónico con el botón :guilabel:` Enviar por correo electrónico` (ventana emergente).

  * Cuando el cliente ve la cotización en línea desde el portal.

  * Cuando la cotización se confirma y se convierte en una orden de venta.

  * Cuando el cliente ve la cotización en el portal.

  * Cuando se valida un borrador de factura.

  * Cuando el cliente ve la suscripción en el portal.

  * Cuando una suscripción genera una factura.

  * Cuando el cliente llega a la última página del proceso de pago de comercio electrónico.

### Activaciones manuales

  * El botón Calcular impuestos con AvaTax en la parte inferior de la cotización.

  * El botón Calcular impuestos con AvaTax en la parte superior de la factura.

Truco

Use el campo Código de contacto Avalara que está disponible en los registros,
cotizaciones y facturas del cliente para confirmar información entre Odoo y
AvaTax. Este campo se ubica en la pestaña :menuselection:` Otra información`
de la orden de venta o la cotización en la sección Ventas.

On the customer record, navigate to _Contacts app_ and select a contact. Then
open the Sales & Purchase tab and the Avalara Partner Code under the Sales
section.

Importante

La posición fiscal Automatic Tax Mapping (AvaTax) también se aplica en esos
documentos de Odoo, como en las suscripciones.

Ver también

  * [Posiciones fiscales (mapeo de impuestos y cuentas)](../fiscal_positions.html)

## Sincronización con AvaTax

La sincronización se hace con AvaTax cuando la _factura_ se crea en Odoo. Esto
significa que el impuesto de ventas se registra con Avalara (el desarrollador
del software AvaTax).

Para hacerlo vaya a Ventas ‣ Órdenes ‣ Cotizaciones y seleccione una
cotización de la lista.

Después de confirmar una cotización y validar la entrega, haga clic en Crear
factura, Indique si será una Factura normal, Anticipo (porcentaje), o Anticipo
(cantidad fija).

Después, haga clic en Crear y ver factura. Para ver los impuestos registrados
vaya a la pestaña Apuntes contables de la factura. Aquí verá diferentes
impuestos dependiendo de la ubicación de la Dirección de entrega.

![Asientos de diario resaltados en una factura de
Odoo.](../../../../../_images/journal-items.png)

Finalmente, haga clic en el botón Confirmar para completar la factura y hacer
la sincronización con el portal de AvaTax.

Advertencia

No puede Restablecer a borrador una factura ya que esto afecta la
sincronización con el portal de AvaTax. Mejor haga clic en :guilabel:` Agregar
nota de crédito` y declare: `Sincronización con el portal AvaTax`. Para más
información consulte esta documentación: [Notas de crédito y
reembolsos](../../customer_invoices/credit_notes.html).

## Descuentos sobre el precio establecido

Para agregar un descuento sobre el precio establecido a un cliente importante,
haga clic en Agregar una línea cuando esté en la factura del cliente. Agregue
un producto de descuento y configure el Precio a un valor ya sea positivo o
negativo. Para volver a calcular los impuestos, haga clic en Calcular
impuestos con AvaTax.

Truco

El cálculo de impuestos no se puede hacer en subtotales negativos o en notas
de crédito.

## Registro

Es posible registrar las acciones de Avalara/_AvaTax_ en Odoo para poder
analizarlas más, o para verificar la función. Puede iniciar sesión con los
ajustes de _AvaTax_.

Para empezar a registrar las acciones de _AvaTax_ primero vaya a Contabilidad
‣ Configuración ‣ Ajustes.

Después, en la sección Impuestos de los ajustes de AvaTax haga clic en Empezar
a registrar por 30 minutos.

Al iniciar el proceso de registro, Odoo registrará todas las acciones que
Avalara/_AvaTax_ realice en la base de datos.

Para ver los registros haga clic en Mostrar registros a la derecha del botón
Empezar a registrar por 30 minutos. Esto mostrará una lista detallada de
acciones Avalara/_AvaTax_. Puede organizar esta lista por las siguientes
columnas:

  * Creado el: hora del cálculo de _AvaTax_.

  * Creado por: valor numérico del usuario en la base de datos.

  * Nombre de la base de datos: nombre de la base de datos.

  * Tipo: en este campo tendrá la opción de seleccionar dos valores Servidor o Cliente.

  * Nombre: el nombre del servicio de Avalara. En este caso sería _AvaTax_.

  * Nivel: por defecto será `INFO`.

  * Ruta: indica la ruta que se utiliza para realizar el cálculo.

  * Línea: indica en qué línea se realizó el cálculo.

  * Función: indica el cálculo que se realizó en la línea.

![La página de inicio de sesión de Avalara con la hilera superior de la lista
resaltada.](../../../../../_images/logging.png)

Haga clic en la línea de registro para mostrar otro campo llamado Mensaje.

En este campo verá una transcripción sin editar de la transacción, que
involucra la creación (o ajuste) de la factura de ventas usando el API de
_AvaTax_ de Avalara.

La transacción incluirá detalles como direcciones de envío del remitente y el
destinatario, líneas en las que se describirán los productos o servicios,
códigos de impuestos, cantidades de impuestos y otra información relevante.

El Mensaje contiene los impuestos calculados para diferentes jurisdicciones y
confirma la creación (o el ajuste) de la transacción.

Truco

Puede crear campos personalizados con la aplicación _Studio_ de Odoo. Haga
clic en el menú __(puntos suspensivos) a la derecha de la columna de
encabezado y haga clic en __ Agregar campo personalizado. Esta acción hará que
se abra _Studio_.

Importante

La aplicación _Studio_ requiere un plan de cobro _personalizado_. Consulte al
gerente de la cuenta de la base de datos para obtener más información sobre
cambiar su plan, o para saber si _Studio_ viene incluida con el plan actual de
la base de datos. Vea esta documentación: [Studio](../../../../studio.html).

Ver también

  * [Integración con AvaTax](../avatax.html)

  * [Portal de Avalara (AvaTax)](avalara_portal.html)

  * [Cumplimiento fiscal en Estados Unidos: video de eLearning sobre AvaTax](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)

  * [Posiciones fiscales (mapeo de impuestos y cuentas)](../fiscal_positions.html)

