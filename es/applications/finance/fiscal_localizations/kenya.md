# Kenia

## Configuración

[Instale](../../general/apps_modules.html#general-install) los siguientes
módulos para obtener todas las funciones de la localización de Kenia:

Nombre | Nombre técnico | Descripción  
---|---|---  
Kenia - Contabilidad | `l10n_ke` | La instalación de este módulo le proporciona acceso a la lista de cuentas que se utilizan en los principios contables locales y a la lista de impuestos comunes como IVA, entre otros.  
Kenia - Reportes contables | `l10n_ke_reports` | La instalación de este módulo le proporciona acceso a reportes contables actualizados para Kenia, como el estado de resultados y el balance general.  
  
También debe instalar el paquete **Integración con dispositivos Tremol para el
intercambio electrónico de datos en Kenia** para poder declarar sus impuestos
ante la **Autoridad Fiscal de Kenia (KRA)** mediante la unidad de control
Tremol G03:

Nombre | Nombre técnico | Descripción  
---|---|---  
Integración con dispositivos Tremol para el intercambio electrónico de datos en Kenia | `l10n_ke_edi_tremol` | La instalación de este módulo integra la unidad de control Tremol G03 de Kenia con su base de datos para declarar sus impuestos ante la KRA con el sistema de gestión de facturas de impuestos (TIMS).  
![Los tres módulos para el paquete de localización fiscal de Kenia en
Odoo](../../../_images/modules.png)

## Integración con el TIMS de Kenia

La Autoridad Fiscal de Kenia (KRA) decidió digitalizar el cobro de impuestos
mediante el **sistema de gestión de facturas de impuestos (TIMS)**. Desde el 1
de diciembre de 2022, todos los sujetos pasivos deben utilizar el TIMS. Esto
con el objetivo de reducir los fraudes por IVA, aumentar los ingresos fiscales
y mejorar el cumplimiento del IVA mediante la estandarización, validación y
transmisión de facturas a la KRA en tiempo real o casi real.

Todos los contribuyentes pasivos deben usar un **registro de impuestos
conforme a la ley**. Odoo decidió desarrollar la integración de la **unidad de
control Tremol G03 (tipo C)** , la cual se puede ejecutar de forma local
mediante una conexión USB. Este dispositivo valida las facturas para
garantizar que los documentos financieros cumplan con las nuevas regulaciones
y envía las facturas de impuestos validadas directamente a la KRA. Es
necesario instalar un servidor proxy que proporcione un portal entre los
usuarios y el internet.

### Instalar el servidor proxy en un dispositivo Windows

Vaya a [odoo.com/download](https://www.odoo.com/page/download), complete la
información solicitada y haga clic en Descargar.

![Instalación del servidor proxy en un dispositivo
Windows](../../../_images/download.png)

Se abrirá un asistente después de que su computadora lo cargue. Debe leer y
aceptar los términos del acuerdo. En la siguiente página, seleccione IoT de
Odoo como el tipo de instalación. A continuación, haga clic en Siguiente y
luego en instalar. Después de realizar estos pasos, haga clic en siguiente.
Seleccione la casilla Iniciar Odoo para que se le redireccione a Odoo de forma
automática y luego haga clic en click Finalizar.

La nueva página que se despliega confirma que su [Caja
IoT](../../general/iot/config/connect.html) está funcionando. Conecte su
dispositivo físico **unidad de control Tremol G03 (tipo C)** a su computadora
portátil mediante USB. Compruebe que la unidad anterior aparece en la sección
Dispositivo IoT para confirmar la conexión entre el dispositivo y su
computadora.

![Su caja IoT está en funcionamiento](../../../_images/iot-box.png)

Nota

Si no se detecta el dispositivo, desconéctelo y vuélvalo a conectar o haga
clic en el botón reiniciar en la esquina superior derecha.

Ver también

[Conectar una caja IoT a su base de
datos](../../general/iot/config/connect.html)

### Envío de los datos a la KRA mediante la unidad de control Tremol G03

Como requisito previo, revise que los módulos contables de Kenia estén
instalados en su base de datos. Después, vaya a Contabilidad ‣ Configuración ‣
Ajustes ‣ sección de Integración con el TIMS de Kenia y verifique que la
dirección proxy de la unidad de control coincida con la dirección de la caja
IoT.

Para enviar datos a la KRA debe crear una nueva factura, vaya a tablero de
Contabilidad ‣ Factura de cliente y haga clic en nueva factura. Cuando se
confirma una nueva factura, aparece el botón enviar factura al dispositivo
fiscal. Hacer clic en él envía los detalles de la factura al dispositivo, y el
dispositivo los envía al gobierno. El campo número de factura de unidad de
control ahora está completo en su factura, lo que confirma que se envió la
información.

La pestaña del dispositivo fiscal Tremol G03 contiene campos que se completan
de forma automática en cuanto la factura se envía al gobierno:

  * Código QR de la unidad de control: URL del portal de la KRA que refleja un código QR.

  * Número de serie de unidad de control: refleja el número de serie del dispositivo.

  * Fecha y hora de firma de la unidad de control: la fecha y hora en las que se envió la factura a la KRA.

Si hace clic en enviar e imprimir se genera un archivo .pdf de la factura. La
información del dispositivo fiscal de Kenia aparece en el documento.

Nota

Para verificar que el KRA ha recibido la información de facturación, ponga su
CUI en la sección Verificador de número de facturas del [sitio web de la
autoridad de Kenia](https://itax.kra.go.ke/KRA-Portal). Haga clic en Validar y
busque los detalles de la factura.

