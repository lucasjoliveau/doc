# Gestión de bases de datos

Estas guías proporcionan las instrucciones para instalar, dar mantenimiento y
actualizar las bases de datos de Odoo.

Ver también

[Historial de versiones](administration/supported_versions.html)

## Instalación

Hay varias maneras de instalar (o no instalar) Odoo según el caso de uso
previsto.

  * La instalación [en línea](administration/odoo_online.html) es la manera más fácil de usar Odoo en producción o de probarlo.

  * Las [instalaciones en paquetes](administration/on_premise/packages.html) son ideales para realizar pruebas y desarrollar módulos. También son excelentes para una producción a largo plazo donde se harán despliegues adicionales y se realizará trabajo de mantenimiento.

  * La [instalación de origen](administration/on_premise/source.html) tiene mayor flexibilidad, pues le permite hacer cosas como ejecutar varias versiones de Odoo en el mismo sistema, por ejemplo. También es adecuada para desarrollar módulos y se puede usar como base para desplegar producción.

  * También está disponible una imagen base de [Docker](https://hub.docker.com/_/odoo/) para desarrollo o despliegue.

## Ediciones

Hay dos ediciones diferentes.

**Odoo Community** es la versión gratuita y de código abierto del software y
cuenta con la licencia [GNU
LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). Es la base con la
que construimos Odoo Enterprise.

**Odoo Enterprise** es la versión origen compartida del software que tiene
acceso a más funciones, como soporte funcional, actualizaciones y alojamiento.
Los [precios](https://www.odoo.com/pricing-plan) dependen de la cantidad de
usuarios.

Truco

[Puede cambiar de Community a
Enterprise](administration/on_premise/community_to_enterprise.html) en
cualquier momento, excepto en la instalación de origen.

  * [Alojamiento](administration/hosting.html)
  * [Odoo en línea](administration/odoo_online.html)
  * Odoo.sh
    * Información general
      * [Introducción a Odoo.sh](administration/odoo_sh/overview/introduction.html)
    * Información básica
      * [Cree su proyecto](administration/odoo_sh/getting_started/create.html)
      * [Ramas](administration/odoo_sh/getting_started/branches.html)
      * [Compilaciones](administration/odoo_sh/getting_started/builds.html)
      * [Estado](administration/odoo_sh/getting_started/status.html)
      * [Ajustes](administration/odoo_sh/getting_started/settings.html)
      * [Editor en línea](administration/odoo_sh/getting_started/online-editor.html)
      * [Su primer módulo](administration/odoo_sh/getting_started/first_module.html)
    * Avanzado
      * [Contenedores](administration/odoo_sh/advanced/containers.html)
      * [Submódulos](administration/odoo_sh/advanced/submodules.html)
      * [Preguntas técnicas más frecuentes](administration/odoo_sh/advanced/frequent_technical_questions.html)
  * [Local](administration/on_premise.html)
    * [Paquete de instaladores](administration/on_premise/packages.html)
    * [Instalación desde la fuente](administration/on_premise/source.html)
    * [Actualizaciones para solucionar bugs](administration/on_premise/update.html)
    * [Configuración del sistema](administration/on_premise/deploy.html)
    * [Puerta de enlace del correo electrónico](administration/on_premise/email_gateway.html)
    * [IP de localización](administration/on_premise/geo_ip.html)
    * [Cambiar de Community a Enterprise](administration/on_premise/community_to_enterprise.html)
  * [Actualizar](administration/upgrade.html)
  * [Base de datos neutralizada](administration/neutralized_database.html)
  * [Versiones compatibles](administration/supported_versions.html)
  * [Aplicaciones para celular de Odoo](administration/mobile.html)
  * [Cuentas de Odoo.com](administration/odoo_accounts.html)

