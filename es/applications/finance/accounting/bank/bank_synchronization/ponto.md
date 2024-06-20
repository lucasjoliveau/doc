# Ponto

**Ponto** es un servicio que permite que empresas y profesionales agreguen sus
cuentas a un solo lugar y vean directamente todas sus transacciones dentro de
una aplicación. Es una solución de terceros que está expandiendo continuamente
la cantidad de instituciones bancarias que se pueden sincronizar con Odoo.

![Logo de la marca Ponto](../../../../../_images/ponto-logo.png)

**Odoo** se puede sincronizar directamente con su banco para obtener todos los
extractos bancarios importados de manera automática a su base de datos.

Ponto es un proveedor externo de pago que puede gestionar la sincronización
entre sus cuentas bancarias y Odoo. [Cuesta 4 € al mes por
cuenta/integración](https://myponto.com/en#pricing).

Ver también

  * [Sincronización bancaria](../bank_synchronization.html)

  * [Transacciones](../transactions.html)

## Configuración

### Vincule sus cuentas bancarias con Ponto

  1. Vaya al [sitio web de Ponto (https://myponto.com)](https://myponto.com).

  2. Cree una cuenta si aún no tiene una.

  3. Una vez que haya iniciado sesión, cree una _organización_.

![Complete el formulario para agregar una organización en
Ponto.](../../../../../_images/ponto-organization.png)

  4. Vaya a :menuselection: `Cuentas --> En vivo`, y haga clic en _Agregar cuenta_.

Es posible que primero deba agregar su **Información de facturación**.

  5. Seleccione su país, sus instituciones bancarias, dé su consentimiento a Ponto y siga los pasos en pantalla para vincular su cuenta bancaria con su cuenta Ponto.

![Añadir cuentas bancarias a su cuenta Ponto](../../../../../_images/ponto-
add-account.png)

  6. Asegúrese de agregar todas las cuentas bancarias que desea sincronizar con su base de datos de Odoo antes de continuar con los siguientes pasos.

### Vincule su cuenta Ponto con su base de datos Odoo

  1. Vaya a :menuselection: `Contabilidad --> Configuración --> Agregar una cuenta bancaria`.

  2. Busque su institución, asegúrese de seleccionar la institución correcta. Una vez que la haya seleccionado, puede verificar que el proveedor externo sea Ponto.

  3. Haga clic en _Conectar_ y siga los pasos.

  4. En algún momento, deberá autorizar las cuentas a las que desea acceder en Odoo. Seleccione **todas las cuentas** que desee sincronizar, incluso aquellas que pertenezcan a otras instituciones bancarias.

![Selección de las cuentas que desea sincronizar con
Odoo.](../../../../../_images/ponto-select-accounts.png)

  5. Termine el flujo.

Nota

Debe autorizar todas las cuentas a las que desea acceder en Odoo, pero
filtraremos las cuentas en función de la institución que seleccionó en el
segundo paso.

### Actualice sus credenciales de sincronización

Es posible que deba actualizar sus credenciales de Ponto o modificar la
configuración de sincronización.

Para hacerlo, vaya a :menuselection: `Contabilidad --> Configuración -->
Sincronización en línea` y seleccione la institución que desea para buscar las
otras cuentas. Haga clic en el botón _Obtener cuentas_ para iniciar el flujo.

Durante la actualización, seleccione **todas las cuentas** que desea
sincronizar, incluso las que provienen de otras instituciones bancarias.

### Obtener cuentas nuevas

Es posible que desee agregar nuevas cuentas en línea a su conexión.

Para hacerlo, vaya a :menuselection: `Contabilidad --> Configuración -->
Sincronización en línea` y seleccione la institución que desea para buscar las
otras cuentas. Haga clic en el botón _Obtener cuentas_ para iniciar el flujo.

No olvide conservar la autorización para las cuentas existentes (para todas
las instituciones que haya sincronizado con Ponto).

## Preguntas frecuentes

### Después de mi sincronización, no aparece ninguna cuenta.

Seleccionó una institución de la lista y no autorizó ninguna cuenta de esta
institución.

### Tengo un error en el que dice que mi autorización ha caducado.

Cada **3 meses** (90 días) debe volver a autorizar la conexión entre su cuenta
bancaria y Ponto. Esto debe hacerse desde el [sitio web de
Ponto](https://myponto.com). Si no lo hace, la sincronización se detendrá para
estas cuentas.

### Tengo algunos errores con mi institución en estado beta

Ponto proporciona instituciones en _beta_ , estas instituciones no cuentan con
el apoyo directo de Odoo y le recomendamos que se ponga en contacto
directamente con Ponto.

Importante

El uso de una institución en versión beta beneficia a Ponto, les permite tener
comentarios reales sobre la conexión con la institución.

