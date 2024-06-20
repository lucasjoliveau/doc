# Base de datos neutralizada

Una base de datos neutralizada es una base de datos que no pertenece a
producción en la que se desactivan varios parámetros. Esto permite realizar
pruebas sin el riesgo de iniciar procesos automatizados específicos que
podrían afectar los datos que sí pertenecen a producción (por ejemplo, enviar
correos electrónicos a los clientes). El acceso en tiempo real se elimina y se
convierte en un entorno de prueba.

Nota

**Cualquier base de datos de prueba que cree es una base de datos
neutralizada:**

  * Bases de datos de respaldo para pruebas.

  * Bases de datos duplicadas.

  * En Odoo.sh: bases de datos de preproducción y desarrollo.

Importante

Una base de datos también se puede neutralizar en una actualización, pues es
muy importante hacer algunas pruebas antes de comenzar a usar una nueva
versión.

## Funciones desactivadas

La siguiente lista incluye algunos de los parámetros que se desactivan:

  * Todas las acciones planificadas (como la facturación automática de suscripciones, el envío de correos masivos, entre otras).

  * Correos electrónicos salientes

  * Sincronización bancaria

  * Proveedores de pago

  * Métodos de envío

  * Tokens de IAP

Nota

**En la parte superior de la pantalla, en la base de datos neutralizada,
aparece un recuadro rojo que le informa sobre esto de forma inmediata.**

  *[IAP]: Compras dentro de la aplicación

