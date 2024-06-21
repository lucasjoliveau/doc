# Hosting

## Changer de solution d’hébergement

Les instructions pour changer le type d’hébergement d’une base de données
dépendent de la solution actuellement utilisée et de la solution vers laquelle
la base de données doit être déplacée.

## Transférer une base de données on premise

### Vers Konvergo ERP Online

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Konvergo ERP Online n’est <em>pas</em> compatible avec les <b>applications non standards</b>.</p></li>
<li><p>La version actuelle de la base de données doit être <a href="supported_versions">prise en charge</a>.</p></li>
</ul>
</div>

  1. Create a [duplicate of the database](on_premise#on-premise-duplicate).

  2. Dans ce doublon, désinstallez toutes les **applications non standards**.

  3. Utilisez le gestionnaire de base de données pour obtenir un _dump sans filestore_.

  4. [Soumettez un ticket d’assistance](https://www.odoo.com/help) et indiquez les éléments suivants :

     * votre **numéro d’abonnement** ,

     * l”**URL** que vous voulez utiliser pour la base de données (par ex. `company.odoo.com`), et

     * le **dump** en tant que pièce jointe ou en tant que lien vers le fichier (requis pour des fichiers de plus de 60 MB).

  5. Konvergo ERP s’assure alors que la base de données est compatible avant de la publier. Si des erreurs techniques surviennent pendant le processus, il se peut qu’Konvergo ERP vous contacte.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous avez des contraintes de temps, <a href="https://www.odoo.com/help">soumettez un ticket d’assistance</a> dès que possible pour planifier le transfert.</p>
</div>

### Vers Konvergo ERP.sh

Suivez les instructions que vous pouvez trouver dans la section [Importer
votre base de données](odoo_sh/getting_started/create#odoo-sh-import-
your-database) de la documentation Konvergo ERP.sh _Créer votre projet_.

## Transférer une base de données Konvergo ERP Online

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP Online’s <a href="supported_versions#supported-versions"><span class="std std-ref">intermediary versions</span></a> are not supported by Konvergo ERP.sh or
on-premise. Therefore, if the database to transfer is running an intermediary version, it must be
upgraded first to the next <a href="supported_versions#supported-versions"><span class="std std-ref">major version</span></a>, waiting for its release if
necessary.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Le transfert d’une base de données online fonctionnant sur Konvergo ERP 16.3 nécessiterait d’abord une mise à niveau vers Konvergo ERP 17.0.</p>
</div>
<div class="alert alert-tip">
<p class="alert-title">
Astuce</p><p>Cliquez sur l’icône d’engrenage (<b>⚙</b>) à côté du nom de la base de données sur le <a href="https://www.odoo.com/my/databases/">gestionnaire de base de données Konvergo ERP Online</a> pour afficher son numéro de version.</p>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>If there is an active Konvergo ERP subscription linked to the database being migrated, reach out to
the Customer Service Manager or <a href="https://www.odoo.com/help">submit a support ticket</a>  to
complete the subscription transfer.</p>
</div>
</div>

### Vers on premise

  1. Connectez-vous au [gestionnaire de base de données Konvergo ERP Online](https://www.odoo.com/my/databases/) et cliquez sur l’icône d’engrenage (**⚙**) à côté du nom de la base de données pour **Télécharger** une sauvegarde. Si le téléchargement échoue parce que le fichier est trop volumineux, [contactez l’assistance d’Konvergo ERP](https://www.odoo.com/help).

  2. Restaurez la base de données à partir du gestionnaire de base de données sur votre serveur local en utilisant la sauvegarde.

### Vers Konvergo ERP.sh

  1. Connectez-vous au [gestionnaire de base de données Konvergo ERP Online](https://www.odoo.com/my/databases/) et cliquez sur l’icône d’engrenage (**⚙**) à côté du nom de la base de données pour **Télécharger** une sauvegarde. Si le téléchargement échoue parce que le fichier est trop volumineux, [contactez l’assistance d’Konvergo ERP](https://www.odoo.com/help).

  2. Suivez les instructions que vous pouvez trouver dans la section [Importer votre base de données](odoo_sh/getting_started/create#odoo-sh-import-your-database) de la documentation Konvergo ERP.sh _Créer votre projet_.

## Transférer une base de données Konvergo ERP.sh

### Vers Konvergo ERP Online

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP Online n’est <em>pas</em> compatible avec les <b>applications non standards</b>.</p>
</div>

  1. Désinstallez toutes les **applications non standards** dans un build de simulation avant de le faire dans le build de production.

  2. [Créez un ticket d’assistance](https://www.odoo.com/help) et indiquez les éléments suivants :

     * votre **numéro d’abonnement** ,

     * l”**URL** que vous voulez utiliser pour la base de données (par ex. `company.odoo.com`),

     * la **branche** qui doit être migrée,

     * la **région** dans laquelle vous voulez que la base de données soit hébergée (Amériques, Europe ou Asie),

     * le ou les utilisateurs qui seront **administrateurs** , et

     * **quand** (et dans quel fuseau horaire) vous voulez que la base de données soit opérationnelle.

  3. Konvergo ERP s’assure alors que la base de données est compatible avant de la publier. Si des erreurs techniques surviennent pendant le processus, il se peut qu’Konvergo ERP vous contacte.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Si vous avez des contraintes de temps, <a href="https://www.odoo.com/help">soumettez un ticket d’assistance</a> dès que possible pour planifier le transfert.</p></li>
<li><p>Sélectionnez la <b>région</b> la plus proche de vos utilisateurs pour réduire la latence.</p></li>
<li><p>Les futurs <b>administrateurs</b> doivent avoir un compte Konvergo ERP.com.</p></li>
<li><p>La <b>date et l’heure</b> auxquelles vous voulez que la base de données soit opérationnelle sont utiles pour organiser le passage du serveur Konvergo ERP.sh aux serveurs Konvergo ERP Online.</p></li>
<li><p>Les bases de données <b>ne sont pas accessibles</b> pendant leur migration.</p></li>
</ul>
</div>

### Vers on premise

  1. Téléchargez une [sauvegarde de votre base de données de production Konvergo ERP.sh](odoo_sh/getting_started/branches#odoo-sh-branches-backups).

  2. Restaurez la base de données à partir du gestionnaire de base de données sur votre serveur local en utilisant la sauvegarde.

