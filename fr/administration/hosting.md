# Hosting

## Changer de solution d’hébergement

Les instructions pour changer le type d’hébergement d’une base de données
dépendent de la solution actuellement utilisée et de la solution vers laquelle
la base de données doit être déplacée.

## Transférer une base de données on premise

### Vers Odoo Online

Important

  * Odoo Online n’est _pas_ compatible avec les **applications non standards**.

  * La version actuelle de la base de données doit être [prise en charge](supported_versions.html).

  1. Create a [duplicate of the database](on_premise.html#on-premise-duplicate).

  2. Dans ce doublon, désinstallez toutes les **applications non standards**.

  3. Utilisez le gestionnaire de base de données pour obtenir un _dump sans filestore_.

  4. [Soumettez un ticket d’assistance](https://www.odoo.com/help) et indiquez les éléments suivants :

     * votre **numéro d’abonnement** ,

     * l”**URL** que vous voulez utiliser pour la base de données (par ex. `company.odoo.com`), et

     * le **dump** en tant que pièce jointe ou en tant que lien vers le fichier (requis pour des fichiers de plus de 60 MB).

  5. Odoo s’assure alors que la base de données est compatible avant de la publier. Si des erreurs techniques surviennent pendant le processus, il se peut qu’Odoo vous contacte.

Note

Si vous avez des contraintes de temps, [soumettez un ticket
d’assistance](https://www.odoo.com/help) dès que possible pour planifier le
transfert.

### Vers Odoo.sh

Suivez les instructions que vous pouvez trouver dans la section [Importer
votre base de données](odoo_sh/getting_started/create.html#odoo-sh-import-
your-database) de la documentation Odoo.sh _Créer votre projet_.

## Transférer une base de données Odoo Online

Important

Odoo Online’s [intermediary versions](supported_versions.html#supported-
versions) are not supported by Odoo.sh or on-premise. Therefore, if the
database to transfer is running an intermediary version, it must be upgraded
first to the next [major version](supported_versions.html#supported-versions),
waiting for its release if necessary.

Example

Le transfert d’une base de données online fonctionnant sur Odoo 16.3
nécessiterait d’abord une mise à niveau vers Odoo 17.0.

Astuce

Cliquez sur l’icône d’engrenage (⚙) à côté du nom de la base de données sur le
[gestionnaire de base de données Odoo
Online](https://www.odoo.com/my/databases/) pour afficher son numéro de
version.

Avertissement

If there is an active Odoo subscription linked to the database being migrated,
reach out to the Customer Service Manager or [submit a support
ticket](https://www.odoo.com/help) to complete the subscription transfer.

### Vers on premise

  1. Connectez-vous au [gestionnaire de base de données Odoo Online](https://www.odoo.com/my/databases/) et cliquez sur l’icône d’engrenage (⚙) à côté du nom de la base de données pour Télécharger une sauvegarde. Si le téléchargement échoue parce que le fichier est trop volumineux, [contactez l’assistance d’Odoo](https://www.odoo.com/help).

  2. Restaurez la base de données à partir du gestionnaire de base de données sur votre serveur local en utilisant la sauvegarde.

### Vers Odoo.sh

  1. Connectez-vous au [gestionnaire de base de données Odoo Online](https://www.odoo.com/my/databases/) et cliquez sur l’icône d’engrenage (⚙) à côté du nom de la base de données pour Télécharger une sauvegarde. Si le téléchargement échoue parce que le fichier est trop volumineux, [contactez l’assistance d’Odoo](https://www.odoo.com/help).

  2. Suivez les instructions que vous pouvez trouver dans la section [Importer votre base de données](odoo_sh/getting_started/create.html#odoo-sh-import-your-database) de la documentation Odoo.sh _Créer votre projet_.

## Transférer une base de données Odoo.sh

### Vers Odoo Online

Important

Odoo Online n’est _pas_ compatible avec les **applications non standards**.

  1. Désinstallez toutes les **applications non standards** dans un build de simulation avant de le faire dans le build de production.

  2. [Créez un ticket d’assistance](https://www.odoo.com/help) et indiquez les éléments suivants :

     * votre **numéro d’abonnement** ,

     * l”**URL** que vous voulez utiliser pour la base de données (par ex. `company.odoo.com`),

     * la **branche** qui doit être migrée,

     * la **région** dans laquelle vous voulez que la base de données soit hébergée (Amériques, Europe ou Asie),

     * le ou les utilisateurs qui seront **administrateurs** , et

     * **quand** (et dans quel fuseau horaire) vous voulez que la base de données soit opérationnelle.

  3. Odoo s’assure alors que la base de données est compatible avant de la publier. Si des erreurs techniques surviennent pendant le processus, il se peut qu’Odoo vous contacte.

Note

  * Si vous avez des contraintes de temps, [soumettez un ticket d’assistance](https://www.odoo.com/help) dès que possible pour planifier le transfert.

  * Sélectionnez la **région** la plus proche de vos utilisateurs pour réduire la latence.

  * Les futurs **administrateurs** doivent avoir un compte Odoo.com.

  * La **date et l’heure** auxquelles vous voulez que la base de données soit opérationnelle sont utiles pour organiser le passage du serveur Odoo.sh aux serveurs Odoo Online.

  * Les bases de données **ne sont pas accessibles** pendant leur migration.

### Vers on premise

  1. Téléchargez une [sauvegarde de votre base de données de production Odoo.sh](odoo_sh/getting_started/branches.html#odoo-sh-branches-backups).

  2. Restaurez la base de données à partir du gestionnaire de base de données sur votre serveur local en utilisant la sauvegarde.

