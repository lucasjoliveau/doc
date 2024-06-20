# Identificador de llamadas dinámico

El _Caller ID_ identifica la llamada cuando se hace una llamada telefónica.
Permite que la persona que reciba la llamada vea el número desde que se está
marcando. El identificador de llamadas le muestra a los usuarios y a los
clientes quién está llamando, así pueden decidir si responder o colgar la
llamada.

Axivox ofrece una opción de identificador de llamadas dinámico con el que se
puede elegir qué número se muestra en las llamadas salientes.

Se pueden comprar números internacionales para hacer transacciones de negocios
internacionales, a través de una llamada telefónica, desde un número que tenga
un código de área o un código de país del destino al que se está llamando. Si
se muestra un número local es más probable que el cliente responda la llamada.

Algunas empresas tienen muchos empleados que hacen llamadas desde un centro de
llamadas. Estos empleados no siempre están disponibles para recibir una
llamada regresada de un cliente potencial. En este caso puede configurar el
:abbr:`VoIP (voz sobre protocolo de internet)`de manera que el identificador
de llamadas dinámico muestre el número de la empresa principal, así que
cualquier número de empleados dentro del grupo puede responder la llamada. Así
nunca se pierden las llamadas.

## Número de salida automático

En Axivox se puede configurar un _número predeterminado_ , este será el número
principal de la empresa. Esto significa que cuando alguien de la empresa
(usuario/empleado) llama a un número fuera de la empresa, el número automático
de salida se muestra como identificador de llamada.

Si alguien de afuera de la empresa intenta regresar la llamada al
usuario/empleado se les canalice a través de la línea principal (número
automático). Si hay un plan de marcación configurado, se les pide que hagan
unas selecciones. Esto es muy útil en caso donde los empleados cambien de
puestos frecuentemente, o si dejan la empresa.

Ver también

  * [Información básica de los planes de marcación](dial_plan_basics.html)

  * [Planes de marcado avanzados](dial_plan_advanced.html)

Para acceder al número automático, vaya a la [consola de gestión de
Axivox](https://manage.axivox.com) e inicie sesión. Después, haga clic en
Settings (ajustes) en el menú izquierdo y vaya a Default outgoing number
(número de salida automático).

Desde aquí, puede cambiar el Default outgoing number (número de salida
automático) haciendo clic en el menú desplegable y seleccionándolo desde los
números entrantes disponibles en Axivox.

Asegúrese de Guardar los cambios, después haga clic en Apply changes (aplicar
cambios) en la esquina superior derecha de la página General Settings (ajustes
generales) para implementar el cambio.

El Default outgoing number (número automático de salida) es lo que se muestra
en automático en el portal de gestión de Axivox. Sin embargo, el número de
salida también se puede configurar de forma diferente a nivel de usuario.

### Usuarios

Para configurar el número saliente a nivel de usuario, acceda a la [consola de
gestión Axivox](https://manage.axivox.com). A continuación, haga clic en Users
(usuario) en el menú de la izquierda y, a continuación, haga clic en Edit
(editar) a la derecha del usuario que desea configurar.

En Número saliente, haga clic en el menú desplegable para seleccionar el
Número saliente predeterminado (como se especifica aquí: Número de salida
automático) o cualquiera de los números entrantes de la cuenta de Axivox.

La selección de Default (automático) en el menú desplegable Outgoing number
(número saliente) garantiza que este usuario tenga el Default outgoing number
(número saiente predeterminado) mostrado en su identificador de llamadas al
realizar llamadas.

Si se escoge un número específico y ese número ya se le asignó a otro usuario
como Incoming numbers (números entrantes) (en el menú de la consola de
Axivox), esto significa que este usuario tiene una línea directa para que los
clientes se pongan en contacto con ellos.

Una vez que los cambios deseados estén completos, asegúrense de hacer clic en
Save (guardar) y después haga clic en Aplicar cambios en la esquina superior
derecha para implementar el cambio.

Truco

De forma predeterminada, al crear un nuevo usuario en Axivox, el número
saliente está configurado como Predeterminado.

### Opciones avanzadas

Para ingresar a las Advanced options (opciones avanzadas), vaya a la opción
Ajustes en el menú de la izquierda de la [consola de gestión
Axivox](https://manage.axivox.com). Después, haga clic en Advanced options
(opciones avanzadas) a la derecha del Default outgoing number (número
automático de salida).

No hay reglas avanzadas configuradas de forma predeterminada. Para crear una
haga clic en el icono verde \+ (más), esto hace que aparezca una línea con dos
campos vacíos. Desde aquí puede configurar diferentes identificadores de
llamadas, dependiendo de la ubicación desde la que está hablando el usuario o
empleado.

Para crear una regla, primero configure un Destination prefix (prefijo de
destino) en el primer campo vacío. Este es el código del país completo,
incluyendo los ceros frente a él. Después, en el segundo campo vacío,
seleccione el número de teléfono que se debe usar para hacer llamadas
salientes de ese código de país.

Importante

Marque la casilla de Apply advanced rules even for users with a default
outgoing number configured (aplicar reglas avanzadas incluso para usuarios con
un número predeterminado configurado) para permitir que estas reglas tengan
prioridad sobre todas las demás configuraciones de salida.

Truco

Para modificar el orden de las reglas solo tiene que arrastrarlas y soltarlas
en otro orden. La regla que se aplica primero es la primera que coincida.

Example

Por ejemplo, una empresa quiere que todos sus usuarios o empleados utilicen el
número configurado para Inglaterra al llamar desde el código de país `0044`
(Inglaterra).

Para ello, basta con escribir `0044` en el campo Destination prefix (Prefijo
de destino) y seleccionar el número que empieza por el prefijo de país `+44`.
Ordene las reglas según sea necesario, y seleccione la casilla de verificación
para reemplazar todas las demás reglas, si es necesario.

![Las opciones avanzadas para el número de salida
predeterminado.](../../../../_images/advanced-callerid.png)

Una vez que las configuraciones deseadas estén completas, asegúrense de hacer
clic en Save (guardar) y después haga clic en Aplicar cambios en la esquina
superior derecha para implementar el cambio.

