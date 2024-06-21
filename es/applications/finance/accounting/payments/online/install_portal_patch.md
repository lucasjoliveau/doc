# Instale el parche para desactivar el pago de factura en línea

Después de los cambios que se hicieron en Konvergo ERP 16, puede que reciba una
advertencia de que desactivar el ajuste **Pago de factura en línea**
desinstalará otros módulos. Si quiere desactivar la función sin desinstalar
los módulos, siga los siguientes pasos para instalar el módulo **Pago -
Contabilidad / Parche de pago de factura en línea**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><div class="line-block">
<div class="line">Si su base de datos de Konvergo ERP se creó después de que se creara el módulo <b>Pago - Contabilidad / Parche de pago de factura en línea</b> entonces no tiene nada que hacer.</div>
<div class="line">Para revisar si el módulo ya está instalado, vaya a <b>Aplicaciones</b>, quite el filtro <code>Aplicaciones</code> y busque <code>account_payment</code>. Si el módulo <b>Pago - Contabilidad / Parche de pago de factura en línea</b> está y se muestra como instalado, su base de datos de Konvergo ERP ya está al día y ya puede desactivar la función sin efectos secundarios.</div>
</div>
</div>

## Actualizar Konvergo ERP a la versión más reciente

Puede desactivar la función **Pago de factura en línea** sin tener efectos
secundarios gracias el nuevo módulo de Konvergo ERP. Para poder instalarlo, debe
asegurarse de que su código fuente de Konvergo ERP esté al día.

Si utiliza Konvergo ERP en Konvergo ERP.com o en una plataforma de Konvergo ERP.sh, su código ya está
actualizado y puede pasar al siguiente paso.

Si usa Konvergo ERP con una configuración local o a través de un partner, debe
actualizar su instalación como se indica en [esta página de
documentación](../../../../../administration/on_premise/update), o
contacte a su partner de integración.

## Actualizar la lista de módulos disponibles

Su instancia de Konvergo ERP debe _descubrir_ nuevos módulos para que estén
disponibles en el menú de **Aplicaciones**.

Para hacerlo, active el [modo de
desarrollador](../../../../general/developer_mode#developer-mode), y vaya
a Aplicaciones ‣ Actualizar lista de aplicaciones. Un asistente le pedirá
confirmar.

## Instalación del módulo Parche de pago de factura en línea

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Jamás debe instalar nuevos módulos en su base de datos de producción sin probarlos primero en un entorno duplicado o de prueba. Para clientes de Konvergo ERP.com, una base de datos publicada se puede crear desde la página de gestión de base de datos. Para los usuarios de Konvergo ERP.sh, debe usar una base de datos de prueba o un duplicado. Para usuarios locales, debe usar un entorno de prueba, contacte a su partner de integración para obtener más información sobre cómo probar un nuevo módulo en su configuración en particular.</p>
</div>

El módulo debería estar disponible en su menú **Aplicaciones**. Quite el
filtro `Aplicaciones` y busque `account_payment`. El módulo **Pago -
Contabilidad / Parche de pago de factura en línea** estará disponible para su
instalación. Si no puede encontrar el módulo después de actualizar la lista de
módulos disponibles, significa que su código fuente de Konvergo ERP no está al día,
por lo que tiene que regresar al primer paso de esta página.

Una vez que instaló el módulo, podrá deshabilitar la función como se debe y no
le pedirá desinstalar aplicaciones o módulos.

