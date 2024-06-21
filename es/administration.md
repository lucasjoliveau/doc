# Gestión de bases de datos

Estas guías proporcionan las instrucciones para instalar, dar mantenimiento y
actualizar las bases de datos de Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="administration/supported_versions">Historial de versiones</a></p>
</div>

## Instalación

Hay varias maneras de instalar (o no instalar) Konvergo ERP según el caso de uso
previsto.

  * La instalación [en línea](administration/odoo_online) es la manera más fácil de usar Konvergo ERP en producción o de probarlo.

  * Las [instalaciones en paquetes](administration/on_premise/packages) son ideales para realizar pruebas y desarrollar módulos. También son excelentes para una producción a largo plazo donde se harán despliegues adicionales y se realizará trabajo de mantenimiento.

  * La [instalación de origen](administration/on_premise/source) tiene mayor flexibilidad, pues le permite hacer cosas como ejecutar varias versiones de Konvergo ERP en el mismo sistema, por ejemplo. También es adecuada para desarrollar módulos y se puede usar como base para desplegar producción.

  * También está disponible una imagen base de [Docker](https://hub.docker.com/_/odoo/) para desarrollo o despliegue.

## Ediciones

Hay dos ediciones diferentes.

**Konvergo ERP Community** es la versión gratuita y de código abierto del software y
cuenta con la licencia [GNU
LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). Es la base con la
que construimos Konvergo ERP Enterprise.

**Konvergo ERP Enterprise** es la versión origen compartida del software que tiene
acceso a más funciones, como soporte funcional, actualizaciones y alojamiento.
Los [precios](https://www.odoo.com/pricing-plan) dependen de la cantidad de
usuarios.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p><a href="administration/on_premise/community_to_enterprise">Puede cambiar de Community a Enterprise</a> en cualquier momento, excepto en la instalación de origen.</p>
</div>

  * [Alojamiento](administration/hosting)
  * [Konvergo ERP en línea](administration/odoo_online)
  * Konvergo ERP.sh
    * Información general
      * [Introducción a Konvergo ERP.sh](administration/odoo_sh/overview/introduction)
    * Información básica
      * [Cree su proyecto](administration/odoo_sh/getting_started/create)
      * [Ramas](administration/odoo_sh/getting_started/branches)
      * [Compilaciones](administration/odoo_sh/getting_started/builds)
      * [Estado](administration/odoo_sh/getting_started/status)
      * [Ajustes](administration/odoo_sh/getting_started/settings)
      * [Editor en línea](administration/odoo_sh/getting_started/online-editor)
      * [Su primer módulo](administration/odoo_sh/getting_started/first_module)
    * Avanzado
      * [Contenedores](administration/odoo_sh/advanced/containers)
      * [Submódulos](administration/odoo_sh/advanced/submodules)
      * [Preguntas técnicas más frecuentes](administration/odoo_sh/advanced/frequent_technical_questions)
  * [Local](administration/on_premise)
    * [Paquete de instaladores](administration/on_premise/packages)
    * [Instalación desde la fuente](administration/on_premise/source)
    * [Actualizaciones para solucionar bugs](administration/on_premise/update)
    * [Configuración del sistema](administration/on_premise/deploy)
    * [Puerta de enlace del correo electrónico](administration/on_premise/email_gateway)
    * [IP de localización](administration/on_premise/geo_ip)
    * [Cambiar de Community a Enterprise](administration/on_premise/community_to_enterprise)
  * [Actualizar](administration/upgrade)
  * [Base de datos neutralizada](administration/neutralized_database)
  * [Versiones compatibles](administration/supported_versions)
  * [Aplicaciones para celular de Konvergo ERP](administration/mobile)
  * [Cuentas de Konvergo ERP.com](administration/odoo_accounts)

