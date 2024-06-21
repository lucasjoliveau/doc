# Konvergo ERP Online

[Konvergo ERP Online](https://www.odoo.com/trial) provides private databases which are
fully managed and hosted by Konvergo ERP. It can be used for long-term production or
to test Konvergo ERP thoroughly, including customizations that don’t require code.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP Online n’est pas compatible avec les modules personnalisés ou l’App Store d’Konvergo ERP.</p>
</div>

Konvergo ERP Online databases are accessed using any web browser and do not require a
local installation.

Pour essayer rapidement Konvergo ERP, des instances de [démo](https://demo.odoo.com)
partagées sont disponibles. Aucune inscription n’est nécessaire, mais chaque
instance ne vit que quelques heures.

## Gestion des bases de données

Pour gérer une base de données, allez au [gestionnaire de bases de
données](https://www.odoo.com/my/databases) et connectez-vous en tant
qu’administrateur de la base de données.

Toutes les options principales de gestion de la base de données sont
disponibles en cliquant sur le nom de la base de données, à l’exception de
l’option de mise à niveau, qui est disponible en cliquant sur l’icône **flèche
dans un cercle** à côté du nom de la base de données. Elle s’affiche
uniquement lorsqu’une mise à niveau est disponible.

![Accédez aux options de gestion de la base de données](../_images/database-
manager.png)

  * Mettre à niveau

  * Dupliquer

  * Renommer

  * Télécharger

  * Noms de domaine

  * Étiquettes

  * Supprimer

  * Contactez-nous

  * Inviter / supprimer des utilisateurs

## Mettre à niveau

Déclenchez une mise à niveau de la base de données.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour plus d’informations sur le processus de mise à niveau, consultez la <a href="upgrade#upgrade-request-test-database"><span class="std std-ref">documentation de mise à niveau d’Konvergo ERP Online</span></a>.</p>
</div>

## Dupliquer

Créez une copie exacte de la base de données, que vous pouvez utiliser pour
effectuer des tests sans compromettre les opérations quotidiennes.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>En cochant <b>À des fins de test</b>, toute action externe (emails, bons de livraison, etc.) est désactivée par défaut sur la base de données dupliquée.</p></li>
<li><p>Les bases de données dupliquées expirent automatiquement après 15 jours.</p></li>
<li><p>A maximum of five duplicates can be made per database. Under extraordinary circumstances,
contact <a href="https://www.odoo.com/help">support</a> to raise the limit.</p></li>
</ul>
</div>

## Renommer

Renommez la base de données et son URL.

## Télécharger

Téléchargez un fichier ZIP contenant une sauvegarde de la base de données.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les bases de données sont sauvegardées chaque jour conformément au <a href="https://www.odoo.com/cloud-sla">SLA Konvergo ERP Cloud Hosting</a>.</p>
</div>

## Noms de domaine

Use a custom [domain
name](../applications/websites/website/configuration/domain_names) to
access the database via another URL.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>You can <a href="../applications/websites/website/configuration/domain_names#domain-name-register"><span class="std std-ref">register a domain name for free</span></a>.</p>
</div>

## Étiquettes

Ajoutez des étiquettes pour facilement identifier vos bases de données et les
trier.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez rechercher des étiquettes dans la barre de recherche.</p>
</div>

## Supprimer

Supprimez une base de données instantanément.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Supprimer une base de données signifie que toutes les données sont perdues à jamais. La suppression est instantanée et s’applique à tous les utilisateurs. Il est recommandé de créer une sauvegarde de la base de données avant de la supprimer.</p>
</div>

Lisez attentivement le message d’avertissement et ne continuez que si vous
avez bien compris les implications de la suppression d’une base de données.

![Le message d'avertissement s'affiche avant de supprimer une base de
données](../_images/delete.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Seul un administrateur peut supprimer une base de données.</p></li>
<li><p>Le nom de la base de données est immédiatement accessible à tous.</p></li>
<li><p>Il n’est pas possible de supprimer une base de données si elle a expiré ou si elle est liée à un abonnement. Dans ce cas, contactez l”<a href="https://www.odoo.com/help">Assistance d’Konvergo ERP</a>.</p></li>
</ul>
</div>

## Contactez-nous

Accédez à la [page d’assistance d’Konvergo ERP.com](https://www.odoo.com/help) avec
les détails de votre base de données déjà préremplis.

## Inviter / supprimer des utilisateurs

Pour inviter des utilisateurs, saisissez l’adresse email du nouvel utilisateur
et cliquez sur **Inviter**. Pour ajouter plusieurs utilisateurs, cliquez sur
**Ajouter plus d’utilisateurs**.

![Inviter un utilisateur dans une base de données](../_images/invite-
users.png)

Pour supprimer des utilisateurs, sélectionnez-les et cliquez sur
**Supprimer**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../applications/general/users">Utilisateurs</a></p></li>
<li><p><a href="odoo_accounts">Comptes Konvergo ERP.com</a></p></li>
</ul>
</div>

