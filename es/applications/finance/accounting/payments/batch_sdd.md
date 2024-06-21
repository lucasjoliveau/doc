# Pagos por lotes: domiciliación bancaria SEPA (SDD)

La Zona única de pagos en euros (SEPA, por sus siglas en inglés) es una
iniciativa de integración de pago de parte de la Unión Europea para
simplificar las transferencias bancarias que se realizan con euros. Con la
**domiciliación bancaria SEPA** (SDD, por sus siglas en inglés) sus clientes
pueden firmar un mandato que le autoriza colectar los pagos futuros desde sus
cuentas bancarias. Esto es muy útil para pagos recurrentes basados en
suscripciones.

Puede registrar los mandatos de los clientes en Konvergo ERP y generar archivos `.xml`
que contengan pagos pendientes que se hagan con el mandato SDD.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><div class="line-block">
<div class="line">Los SDD los aceptan todos los países que forman la zona SEPA, los cuales incluyen los 27 estados miembros de la Unión Europea y otros países.</div>
<div class="line"><a href="https://www.europeanpaymentscouncil.eu/document-library/other/epc-list-sepa-scheme-countries">Lista de todos los países SEPA</a>.</div>
</div>
</div>

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes, active la **domiciliación
bancaria SEPA (SDD, por sus siglas en inglés)** y haga clic en **Guardar**.
Ingrese el **identificador de acreedor** de su empresa, este es un número que
le brindó su institución bancaria, o la autoridad responsable de entregar este
número.

![Agregar un número de identificador de acreedor SEPA a contabilidad de
Konvergo ERP](../../../../_images/creditor-identifier.png)

## Mandatos de adeudos directos SEPA

### Crear un mandato

El mandato de SDD es el documento que sus clientes firman para que usted pueda
recolectar dinero directamente de sus cuentas bancarias.

Para crear un mandato nuevo vaya a Contabilidad ‣ Clientes ‣ Mandatos de
domiciliación bancaria y llene el formulario que se encuentra en **Crear**.
Para exportar el archivo PDF haga clic en **Imprimir** y ya solo necesita que
su cliente firme este documento. Una vez que lo haya hecho, suba el documento
firmado y haga clic en **Validar** para empezar a ejecutar el mandato.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de que los <b>datos de cuentas bancarias IBAN</b> que se registraron en el formulario de contacto del deudor sean correctos, tanto en la pestaña <b>Contabilidad</b> y en sus ajustes de <a href="../bank">Cuenta bancaria</a>.</p>
</div>

### Domiciliación bancaria SEPA como método de pago

La domiciliación bancaria SEPA se puede usar como método de pago en **Comercio
electrónico** o en el **Portal del cliente** , solo tiene que activar la SDD
como método de pago. De esta forma, sus clientes podrán crear y firmar sus
mandatos ellos mismos.

Para hacerlo vaya a Contabilidad ‣ Configuración ‣ Proveedores de pagos, haga
clic en _Domiciliación bancaria SEPA_ y realice la configuración de acuerdo a
sus necesidades. Para hacerlo vaya a Contabilidad ‣ Configuración ‣ Métodos de
pago y haga clic en **Domiciliación bancaria SEPA**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de cambiar el campo <b>Estado</b> a <b>Activado</b> y después active la <b>Firma electrónica</b>, necesaria para que los clientes puedan firmar sus mandatos.</p>
</div>

A los clientes que utilizan el SDD como método de pago se les pide que añadan
su IBAN, su dirección de correo electrónico y que firmen su mandato de adeudo
directo SEPA.

### Cerrar o revocar un mandato.

Los mandatos de domiciliación bancaria se cierran de manera automática cuando
llega su **Fecha de finalización**. Si deja este campo en blanco, el mandato
seguirá **Activo** hasta que se **Cierre** o **Revoque**.

Si hace clic en **Cerrar** la fecha de finalización del mandato cambiará a la
fecha de hoy. Esto significa que las facturas con fecha posterior a hoy no se
procesarán con un pago SDD.

Si hace clic en **Revocar** el mandato se deshabilitará de inmediato. Ya no
podrá registrar pagos de SDD, sin importar la fecha de la factura. Sin
embargo, los pagos que ya se registraron todavía incluirán en el siguiente
archivo `.xml` de SDD.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Una vez que el mandato se haya <b>cerrado</b> o <b>revocado</b> ya no se podrá volver a activar.</p>
</div>

## Reciba pagos por lote mediante la domiciliación bancaria SEPA

### Facturas de cliente

Puede registrar los pagos por SDD para las facturas emitidas a clientes que
cuenten con un mandato SDD activo.

Para hacerlo, abra la factura, haga clic en **Registrar pago** y elija
**Domiciliación bancaria SEPA** como su método de pago.

### Generar archivos `.XML` de domiciliación bancaria SEPA para adjuntar
pagos

Los archivos `.xml` que incluyen todas las instrucciones de pago SDD se pueden
subir a su interfaz de banca en línea para que se puedan procesar todos los
pagos al mismo tiempo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los archivos que Konvergo ERP generan siguen las especificaciones de domiciliación bancaria SEPA <b>PAIN.008.001.02</b>, como lo requieren las <a href="https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-credit-transfer-customer-psp-implementation">reglas de implementación</a>, de esta forma nos aseguramos de que sea compatible con otros bancos.</p>
</div>

Para generar un archivo `.xml` de varios pagos pendientes SDD, puede crear un
pago por lotes. Para hacerlo, vaya a Contabilidad ‣ Clientes ‣ Pagos,
seleccione los pagos que se necesitan, después haga clic en Acción y después
en Crear un pago por lotes. Una vez que haga clic en Validar, el archivo
`.xml` estará disponible para descargar de manera inmediata.

![Genere un archivo .XML para sus pagos de SDD en nuestra aplicación
Contabilidad.](../../../../_images/xml.png)

Por último, suba este archivo a su interfaz bancaria en linea para procesar
los pagos.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede recuperar todos los archivos SDD <code>.xml</code> que se generaron en Contabilidad ‣ clientes ‣ Pagos por lote.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="batch">Pagos por lote para depósitos bancarios</a></p></li>
<li><p><a href="../bank">Cuentas bancarias y de efectivo</a></p></li>
<li><p><a href="https://www.europeanpaymentscouncil.eu/document-library/other/epc-list-sepa-scheme-countries">Lista completa de los países que forman la zona SEPA</a></p></li>
<li><p><a href="https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-credit-transfer-inter-psp-implementation-guidelines">Reglas SEPA</a></p></li>
</ul>
</div>

  *[SDD]: domiciliación bancaria SEPA

