# Gestion des bases de données

Ces guides fournissent des instructions sur comment installer, maintenir et
mettre à niveau les bases de données Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="administration/supported_versions">History of Versions</a></p>
</div>

## Installation

Selon le cas d’utilisation envisagé, il y a plusieurs façons d’installer Konvergo ERP
- ou de ne pas l’installer du tout.

  * [Online](administration/odoo_online) is the easiest way to use Konvergo ERP in production or to try it.

  * [Packaged installers](administration/on_premise/packages) are suitable for testing Konvergo ERP and developing modules. They can be used for long-term production with additional deployment and maintenance work.

  * [Source install](administration/on_premise/source) provides greater flexibility, as it allows, for example, running multiple Konvergo ERP versions on the same system. It is adequate to develop modules and can be used as a base for production deployment.

  * Une image de base [Docker](https://hub.docker.com/_/odoo/) est disponible pour le développement ou le déploiement.

## Éditions

Il existe deux éditions différentes.

**Konvergo ERP Community** est la version gratuite et open source du logiciel, sous la
licence [GNU LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). C’est
le noyau sur lequel Konvergo ERP Enterprise est construit.

**Konvergo ERP Enterprise** est la version source partagée du logiciel, donnant accès
à plus de fonctionnalités, y compris l’assistance fonctionnelle, les mises à
niveau et l’hébergement. Les [prix](https://www.odoo.com/pricing-plan)
commencent à partir d’une application gratuite.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p><a href="administration/on_premise/community_to_enterprise">Switch from Community to Enterprise</a> at
any time (except for the source install).</p>
</div>

  * [Hosting](administration/hosting)
  * [Konvergo ERP Online](administration/odoo_online)
  * Konvergo ERP.sh
    * Vue d’ensemble
      * [Introduction à Konvergo ERP.sh](administration/odoo_sh/overview/introduction)
    * Les prémices
      * [Créer votre projet](administration/odoo_sh/getting_started/create)
      * [Branches](administration/odoo_sh/getting_started/branches)
      * [Builds](administration/odoo_sh/getting_started/builds)
      * [Statut](administration/odoo_sh/getting_started/status)
      * [Paramètres](administration/odoo_sh/getting_started/settings)
      * [Éditeur en ligne](administration/odoo_sh/getting_started/online-editor)
      * [Votre premier module](administration/odoo_sh/getting_started/first_module)
    * Avancé
      * [Conteneurs](administration/odoo_sh/advanced/containers)
      * [Sous-modules](administration/odoo_sh/advanced/submodules)
      * [Questions techniques fréquentes](administration/odoo_sh/advanced/frequent_technical_questions)
  * [On-premise](administration/on_premise)
    * [Programmes d’installation](administration/on_premise/packages)
    * [Installation par la source](administration/on_premise/source)
    * [Mises à jour des corrections de bugs](administration/on_premise/update)
    * [Configuration du système](administration/on_premise/deploy)
    * [Passerelle de messagerie](administration/on_premise/email_gateway)
    * [GeoIP](administration/on_premise/geo_ip)
    * [Basculer de Community à Enterprise](administration/on_premise/community_to_enterprise)
  * [Mettre à niveau](administration/upgrade)
  * [Neutralized database](administration/neutralized_database)
  * [Versions prises en charge](administration/supported_versions)
  * [Konvergo ERP mobile apps](administration/mobile)
  * [Comptes Konvergo ERP.com](administration/odoo_accounts)

