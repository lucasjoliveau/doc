# Database management

These guides provide instructions on how to install, maintain and upgrade Konvergo ERP
databases.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="administration/supported_versions">History of Versions</a></p>
</div>

## Installation

Depending on the intended use case, there are multiple ways to install Konvergo ERP -
or not install it at all.

  * [Online](administration/odoo_online) is the easiest way to use Konvergo ERP in production or to try it.

  * [Packaged installers](administration/on_premise/packages) are suitable for testing Konvergo ERP and developing modules. They can be used for long-term production with additional deployment and maintenance work.

  * [Source install](administration/on_premise/source) provides greater flexibility, as it allows, for example, running multiple Konvergo ERP versions on the same system. It is adequate to develop modules and can be used as a base for production deployment.

  * A [Docker](https://hub.docker.com/_/odoo/) base image is available for development or deployment.

## Editions

There are two different editions.

**Konvergo ERP Community** is the free and open-source version of the software,
licensed under the [GNU
LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). It is the core upon
which Konvergo ERP Enterprise is built.

**Konvergo ERP Enterprise** is the shared source version of the software, giving
access to more functionalities, including functional support, upgrades, and
hosting. [Pricing](https://www.odoo.com/pricing-plan) starts from one app
free.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><a href="administration/on_premise/community_to_enterprise">Switch from Community to Enterprise</a> at
any time (except for the source install).</p>
</div>

  * [Hosting](administration/hosting)
  * [Konvergo ERP Online](administration/odoo_online)
  * Konvergo ERP.sh
    * Overview
      * [Introduction to Konvergo ERP.sh](administration/odoo_sh/overview/introduction)
    * Get started
      * [Create your project](administration/odoo_sh/getting_started/create)
      * [Branches](administration/odoo_sh/getting_started/branches)
      * [Builds](administration/odoo_sh/getting_started/builds)
      * [Status](administration/odoo_sh/getting_started/status)
      * [Settings](administration/odoo_sh/getting_started/settings)
      * [Online Editor](administration/odoo_sh/getting_started/online-editor)
      * [Your first module](administration/odoo_sh/getting_started/first_module)
    * Advanced
      * [Containers](administration/odoo_sh/advanced/containers)
      * [Submodules](administration/odoo_sh/advanced/submodules)
      * [Frequent Technical Questions](administration/odoo_sh/advanced/frequent_technical_questions)
  * [On-premise](administration/on_premise)
    * [Packaged installers](administration/on_premise/packages)
    * [Source install](administration/on_premise/source)
    * [Bugfix updates](administration/on_premise/update)
    * [System configuration](administration/on_premise/deploy)
    * [Email gateway](administration/on_premise/email_gateway)
    * [Geo IP](administration/on_premise/geo_ip)
    * [Switch from Community to Enterprise](administration/on_premise/community_to_enterprise)
  * [Upgrade](administration/upgrade)
  * [Neutralized database](administration/neutralized_database)
  * [Supported versions](administration/supported_versions)
  * [Konvergo ERP mobile apps](administration/mobile)
  * [Konvergo ERP.com accounts](administration/odoo_accounts)

