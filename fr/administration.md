# Gestion des bases de données

Ces guides fournissent des instructions sur comment installer, maintenir et
mettre à niveau les bases de données Odoo.

Pour plus d'infos

[History of Versions](administration/supported_versions.html)

## Installation

Selon le cas d’utilisation envisagé, il y a plusieurs façons d’installer Odoo
- ou de ne pas l’installer du tout.

  * [Online](administration/odoo_online.html) is the easiest way to use Odoo in production or to try it.

  * [Packaged installers](administration/on_premise/packages.html) are suitable for testing Odoo and developing modules. They can be used for long-term production with additional deployment and maintenance work.

  * [Source install](administration/on_premise/source.html) provides greater flexibility, as it allows, for example, running multiple Odoo versions on the same system. It is adequate to develop modules and can be used as a base for production deployment.

  * Une image de base [Docker](https://hub.docker.com/_/odoo/) est disponible pour le développement ou le déploiement.

## Éditions

Il existe deux éditions différentes.

**Odoo Community** est la version gratuite et open source du logiciel, sous la
licence [GNU LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). C’est
le noyau sur lequel Odoo Enterprise est construit.

**Odoo Enterprise** est la version source partagée du logiciel, donnant accès
à plus de fonctionnalités, y compris l’assistance fonctionnelle, les mises à
niveau et l’hébergement. Les [prix](https://www.odoo.com/pricing-plan)
commencent à partir d’une application gratuite.

Astuce

[Switch from Community to
Enterprise](administration/on_premise/community_to_enterprise.html) at any
time (except for the source install).

  * [Hosting](administration/hosting.html)
  * [Odoo Online](administration/odoo_online.html)
  * Odoo.sh
    * Vue d’ensemble
      * [Introduction à Odoo.sh](administration/odoo_sh/overview/introduction.html)
    * Les prémices
      * [Créer votre projet](administration/odoo_sh/getting_started/create.html)
      * [Branches](administration/odoo_sh/getting_started/branches.html)
      * [Builds](administration/odoo_sh/getting_started/builds.html)
      * [Statut](administration/odoo_sh/getting_started/status.html)
      * [Paramètres](administration/odoo_sh/getting_started/settings.html)
      * [Éditeur en ligne](administration/odoo_sh/getting_started/online-editor.html)
      * [Votre premier module](administration/odoo_sh/getting_started/first_module.html)
    * Avancé
      * [Conteneurs](administration/odoo_sh/advanced/containers.html)
      * [Sous-modules](administration/odoo_sh/advanced/submodules.html)
      * [Questions techniques fréquentes](administration/odoo_sh/advanced/frequent_technical_questions.html)
  * [On-premise](administration/on_premise.html)
    * [Programmes d’installation](administration/on_premise/packages.html)
    * [Installation par la source](administration/on_premise/source.html)
    * [Mises à jour des corrections de bugs](administration/on_premise/update.html)
    * [Configuration du système](administration/on_premise/deploy.html)
    * [Passerelle de messagerie](administration/on_premise/email_gateway.html)
    * [GeoIP](administration/on_premise/geo_ip.html)
    * [Basculer de Community à Enterprise](administration/on_premise/community_to_enterprise.html)
  * [Mettre à niveau](administration/upgrade.html)
  * [Neutralized database](administration/neutralized_database.html)
  * [Versions prises en charge](administration/supported_versions.html)
  * [Odoo mobile apps](administration/mobile.html)
  * [Comptes Odoo.com](administration/odoo_accounts.html)

