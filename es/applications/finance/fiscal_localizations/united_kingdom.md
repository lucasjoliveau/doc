# Reino Unido

## Configuración

[Instale](../../general/apps_modules.html#general-install) los módulos Reino
Unido - Contabilidad y Reino Unido - Reportes contables para obtener todas las
funciones de la localización para Reino Unido.

Nombre | Nombre técnico | Descripción  
---|---|---  
Reino Unido - Contabilidad | `l10n_uk` | 

  * CT600-plan de cuentas listo
  * VAT100-estructura fiscal lista
  * Lista de condados de Infologic UK

  
Reino Unido - Reportes contables | `l10n_uk_reports` | 

  * Reportes contables para el Reino Unido
  * Permite enviar los reportes fiscales a través de MTD-VAT API a HMRC.

  
![Paquetes Odoo para el Reino Unido ](../../../_images/uk.png)

Nota

  * Solo las empresas que radican en el Reino Unido pueden subir reportes a HMRC.

  * Instalar el módulo Reino Unido - Reportes contables instala ambos módulos a la vez.

Ver también

  * [Hacienda del Reino Unido (HMRC, por sus siglas en inglés)](https://www.gov.uk/government/organisations/hm-revenue-customs/)

  * [Resumen de Making Tax Digital](https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/)

## Plan de cuentas

El plan de cuentas del Reino Unido está incluido en el módulo Reino Unido -
Contabilidad. Vaya a Contabilidad ‣ Configuración ‣ Contabilidad: Plan de
cuentas para tener acceso.

Configure su plan de cuentas en Contabilidad ‣ Configuración ‣ Ajustes ‣
Sección de importar contabilidad y seleccione Revisar manualmente o Importar
(recomendado) sus balances iniciales.

## Impuestos

Como parte del módulo de localización, los impuestos del Reino Unido se crean
automáticamente con sus cuentas y configuraciones financieras
correspondientes.

Vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣ Impuestos para actualizar los
Impuestos predeterminados, la Periodicidad de pagos provisionales o Configure
los impuestos de sus cuentas.

Para editar impuestos existentes o para Crear un impuesto nuevo, vaya a
Contabilidad ‣ Configuración ‣ Contabilidad: Impuestos.

Ver también

  * Impuestos

  * Tutorial: [Devolución y reporte de impuestos](https://www.odoo.com/slides/slide/tax-report-and-return-1719?fullscreen=1).

### Making Tax Digital (MTD)

En el Reino Unido, todas las empresas con RFC registrado tienen que cumplir
con las normas de MTD al usar el sfotware para subir sus devoluciones de IVA.

El módulo **Reino Unido - Reportes contables** le permite cumplir con los
requerimentos de [Hacienda del Reino
Unido](https://www.gov.uk/government/organisations/hm-revenue-customs/) en
cuanto a [Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-
digital/overview-of-making-tax-digital/).

Importante

Si tarda más de tres meses en enviar sus documentos, ya no será posible
hacerlo a través de Odoo, puesto que Odoo solo recupera bonos abiertos de los
últimos tres meses. Su envío tiene que hacerse de manera manual poniendose en
contacto con HMRC.

#### Registre su empresa ante Hacienda del Reino Unido antes de hacer su
primer envío de documentos.

Vaya a Contabilidad ‣ Reportes ‣ Reporte de impuestos y haga clic en Conectar
con HMRC. Ingrese la información de su empresa en la plataforma de HMRC. Solo
necesita hacerlo una vez.

#### Envío periodico a HMRC

Importe sus obligaciones de HMRC, filtrelo en el periodo en el que quiere
hacer el envío y envie su declaración de impuestos haciendo clic en Enviar a
HMRC.

Truco

Puede usar credenciales de prueba para demostrar el flujo de HMRC. Para
hacerlo, active el [modo de
desarrollador](../../general/developer_mode.html#developer-mode) y vaya a
Ajustes generales ‣ Técnico ‣ Parámetros del sistema. Desde aquí busque
`l10n_uk_reports.hmrc_mode` y cambie el valor en esa línea a `demo`. Puede
obtener credenciales desde el [HMRC Developer
Hub](https://developer.service.hmrc.gov.uk/api-test-user).

#### Envío periodico a HMRC para multi-empresas

Solo una empresa y un usuario se pueden conectar a HMRC de manera simultánea.
Si varias empresas que radican en Reino Unido están dentro de la misma base de
datos, el usuario que envía el reporte HMRC debe seguir las siguientes
instrucciones antes de cada envío:

  1. Inicie sesión en la empresa para la que se hará el envío.

  2. Vaya a Ajustes generales y en la sección Usuarios. haga clic en Gestionar usuarios. Seleccione el usuario que está conectado con HMRC.

  3. Vaya a la pestaña Integración con HMRC UK y haga clic en Reestablecer credenciales de autenticación o en el botón Eliminar credenciales de autenticación.

  4. Ahora puede registrar su empresa ante HMRC y enviar el reporte de impuestos para esta empresa.

  5. Repita estos pasos para otras empresas” envios HMRC.

Nota

Durante este proceso, el botón de Conectar a HMRC ya no aparece para otras
empresas que radican en el Reino Unido.

