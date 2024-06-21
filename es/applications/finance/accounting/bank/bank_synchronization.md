# Sincronización bancaria

Konvergo ERP puede sincronizarse directamente con su institución bancaria para que
todos los extractos bancarios se importen automáticamente a su base de datos.

Para verificar si su banco es compatible con Konvergo ERP, vaya a [Ajustes de
Contabilidad de Konvergo ERP](https://www.odoo.com/page/accounting-features), y haga
clic en **Ver lista de instituciones compatibles**.

Konvergo ERP colabora con más de 25,000 instituciones alrededor del mundo.

Konvergo ERP utiliza múltiples servicios web para conectar con los bancos:

  * **Plaid** : Estados Unidos de América y Canadá

  * **Yodlee** : En todo el mundo

  * [Salt Edge](bank_synchronization/saltedge): Global

  * [Ponto](bank_synchronization/ponto): Europa

  * [Enable Banking](bank_synchronization/enablebanking): Países escandinavos

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><span class="xref std std-doc">transacciones</span></p>
</div>

## Configuración

### Usuarios locales

Para poder utilizar este servicio, debe tener una suscripción válida de Konvergo ERP
Enterprise. Asegúrese de que su base de datos esté registrada con su contrato
de Konvergo ERP Enterprise. También usamos un proxy entre su base de datos y el
proveedor externo, por lo que, en caso de un error de conexión, tiene que
verificar que no tenga un firewall o un proxy que bloquee esta dirección:

  * <https://production.odoofin.com/>

### Primera sincronización

Puede comenzar la sincronización ingresando a la aplicación Contabilidad y
luego a Panel de contabilidad ‣ Configuración ‣ Bancos: Agregar una cuenta
bancaria.

Ahora puede buscar su institución bancaria. Selecciónela y siga los pasos para
sincronizarla.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si tiene algún inconveniente durante la primera sincronización, verifique que su navegador web no bloquee las ventanas emergentes y que el bloqueador de anuncios esté desactivado.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Al seleccionar la fecha para la primera sincronización de los estados de cuenta bancarios, elija aquella en la que comenzó a registrar transacciones contables en su base de datos de Contabilidad de Konvergo ERP. Por ejemplo, si importa su saldo de cierre en Konvergo ERP el 31/12/2022 y comienza a registrar transacciones contables el 01/01/2023, su fecha de sincronización debería ser el 01/01/2023.</p>
</div>

En la primera sincronización deberá proporcionar un número de teléfono para
poder proteger su cuenta. Esta información es necesaria para asegurarnos de
que otras personas no puedan acceder a sus datos. Si en algún momento
detectamos movimientos sospechosos en su cuenta, bloquearemos todas las
solicitudes provenientes de la misma y tendrá que reactivarlas con su número
telefónico.

El proveedor externo puede solicitar más información para conectar con su
institución bancaria. Esta información no se almacena en los servidores de
Konvergo ERP.

De forma predeterminada, las transacciones obtenidas de una fuente en línea se
agrupan dentro del mismo extracto y se crea un extracto bancario por mes.
Puede cambiar la periodicidad de creación de extractos bancarios en la
configuración de su diario.

Puede encontrar todas sus sincronizaciones en el tablero de Contabilidad‣
Configuración ‣ Contabilidad: sincronización en línea.

### Sincronizar manualmente

Los diarios creados se sincronizan de forma predeterminada cada 12 horas luego
de la primera sincronización. Si lo desea, puede sincronizarlos de forma
manual al hacer clic en el botón **Sincronizar ahora** del tablero.

O puede ir al tablero de Contabilidad ‣ Configuración ‣ Contabilidad:
Sincronización en línea, seleccionar su institución y hacer clic en el botón
**Obtener transacciones**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Algunas instituciones no permiten que las transacciones se obtengan automáticamente. En el caso de estas instituciones usted recibe un mensaje de error en el que se le pide que desactive la sincronización automática durante la sincronización automática de la cuenta. Este mensaje se puede encontrar en el chatter de sus sincronizaciones en línea. En este caso, asegúrese de realizar sincronizaciones manuales.</p>
</div>

## Problemas

### Error de sincronización

Para reportar un error de conexión al soporte de
[Konvergo ERP](https://www.odoo.com/help), vaya a Contabilidad‣ Configuración ‣
Contabilidad: Sincronización en línea, seleccione la conexión que falló, y
copie la descripción del error y la referencia.

### Desconexión de la sincronización

Si su conexión con el proxy se desconecta, puede volver a conectarse con el
proxy mediante el botón **Recuperar cuenta**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no puede volver a conectarse con el botón <b>Obtener cuenta</b> póngase en contacto con <a href="https://www.odoo.com/help">soporte</a> directamente con su ID de cliente o la referencia del error que aparece en el chatter.</p>
</div>

## Proceso de migración para usuarios que hayan instalado Konvergo ERP antes de
diciembre de 2020

Si usa Konvergo ERP local, primero asegúrese de que su fuente esté actualizada con la
última versión de Konvergo ERP.

Los usuarios que hayan creado una base de datos antes de diciembre de 2020
deben instalar de forma manual el nuevo módulo para utilizar las nuevas
funciones.

Para ello, vaya a Aplicaciones ‣ Actualizar la lista de aplicaciones, elimine
el filtro predeterminado en la barra de búsqueda y escriba
`account_online_synchronization`. Haga clic en **Instalar** y, por último,
asegúrese de que todos sus usuarios presionen CTRL+F5 para actualizar su
página de Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Todas las sincronizaciones anteriores se desconectan durante la instalación y ya no vuelven a funcionar.</p></li>
<li><p>Puede encontrarlos directamente en el menú de sincronización (Contabilidad ‣ Configuración ‣ Contabilidad: Sincronización en línea). No es posible resincronizar estas conexiones; tiene que crear otras nuevas.</p></li>
<li><p>No desinstale el <code>account_online_sync</code>, que es el módulo anterior para la sincronización en línea. El nuevo lo anula.</p></li>
<li><p>De forma predeterminada, <code>account_online_synchronization</code> se instala en automático con Contabilidad.</p></li>
</ul>
</div>

## Preguntas frecuentes

### La sincronización no está funcionando en tiempo real, ¿es normal?

El proceso no está diseñado para funcionar en tiempo real, ya que los
proveedores externos sincronizan sus cuentas en intervalos diferentes. Para
forzar la sincronización y obtener los estados de cuenta, vaya a su **Panel de
control de contabilidad** y haga clic en el botón **Sincronizar ahora**.
También puede sincronizar y obtener transacciones a través del Panel de
control de contabilidad ‣ Configuración ‣ Contabilidad: Sincronización en
línea. También puede sincronizar y obtener transacciones a través del Panel de
control de contabilidad ‣ Configuración ‣ Contabilidad: Sincronización en
línea. Algunos proveedores solo permiten una actualización por día, por lo que
es posible que al hacer clic en **Sincronizar ahora** no se muestren sus
transacciones más recientes si ya ha realizado esa acción previamente en el
mismo día.

Una transacción puede ser visible en su cuenta bancaria pero no ser recuperada
si tiene el estado **Pendiente**. Solo se obtendrán las transacciones con el
estado **Publicado**. Si la transacción aún no ha sido **Publicada** , deberá
esperar hasta que cambie su estado.

### ¿La función de sincronización bancaria en línea está incluida en mi
contrato?

  * **Versión Community** : No, esta función no está incluida en la versión Community.

  * **Versión en línea** : Sí, incluso si se beneficia del contrato Una aplicación gratis.

  * ** Versión Enterprise**: Sí, si tiene un contrato Enterprise válido vinculado a su base de datos.

### Algunos bancos tienen un estado «Beta», ¿qué significa?

Esto significa que las instituciones bancarias aún no cuentan con el respaldo
total de nuestro proveedor externo. Pueden surgir errores u otros problemas.
Konvergo ERP no ayuda con problemas técnicos que ocurren con los bancos en la fase
beta, pero el usuario aún puede optar por conectarse. La conexión con estos
bancos contribuye al proceso de desarrollo, ya que el proveedor tendrá datos
reales y comentarios de la conexión.

### ¿Por qué mis transacciones solo se sincronizan cuando las actualizo
manualmente?

Algunos bancos tienen medidas de seguridad adicionales y requieren pasos
adicionales, como un código de autenticación por SMS/correo electrónico u otro
tipo de MFA. Debido a esto, el integrador no puede extraer transacciones hasta
que se proporcione el código de seguridad.

### No todas mis transacciones pasadas están en Konvergo ERP, ¿por qué?

Para algunas instituciones solo se pueden recuperar las transacciones de los 3
meses anteriores.

### ¿Por qué no veo ninguna transacción?

Durante su primera sincronización, usted seleccionó las cuentas bancarias que
decidió sincronizar con Konvergo ERP. Si no sincronizó ninguna de sus cuentas, puede
ir a Panel de control de contabilidad ‣ Configuración ‣ Contabilidad:
Sincronización en línea y hacer clic en el botón **Obtener cuenta** en la
conexión.

Es posible que tampoco haya nuevas transacciones.

Si su cuenta bancaria está correctamente vinculada a un diario y las
transacciones registradas no son visibles en su base de datos, por favor,
[envíe un ticket al servicio de soporte](https://www.odoo.com/help).

### ¿Cómo puedo actualizar mis credenciales bancarias?

Puede actualizar sus credenciales yendo a Panel de control de contabilidad ‣
Configuración ‣ Contabilidad: Sincronización en línea; abra la conexión en la
que desea actualizar sus credenciales y haga clic en el botón **Actualizar
credenciales**.

  * [Salt Edge](bank_synchronization/saltedge)
  * [Ponto](bank_synchronization/ponto)
  * [Enable Banking](bank_synchronization/enablebanking)

