# Odoo Online

[Odoo Online](https://www.odoo.com/trial) provides private databases which are
fully managed and hosted by Odoo. It can be used for long-term production or
to test Odoo thoroughly, including customizations that don’t require code.

Note

Odoo Online n’est pas compatible avec les modules personnalisés ou l’App Store
d’Odoo.

Odoo Online databases are accessed using any web browser and do not require a
local installation.

Pour essayer rapidement Odoo, des instances de [démo](https://demo.odoo.com)
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

Pour plus d'infos

Pour plus d’informations sur le processus de mise à niveau, consultez la
[documentation de mise à niveau d’Odoo Online](upgrade.html#upgrade-request-
test-database).

## Dupliquer

Créez une copie exacte de la base de données, que vous pouvez utiliser pour
effectuer des tests sans compromettre les opérations quotidiennes.

Important

  * En cochant À des fins de test, toute action externe (emails, bons de livraison, etc.) est désactivée par défaut sur la base de données dupliquée.

  * Les bases de données dupliquées expirent automatiquement après 15 jours.

  * A maximum of five duplicates can be made per database. Under extraordinary circumstances, contact [support](https://www.odoo.com/help) to raise the limit.

## Renommer

Renommez la base de données et son URL.

## Télécharger

Téléchargez un fichier ZIP contenant une sauvegarde de la base de données.

Note

Les bases de données sont sauvegardées chaque jour conformément au [SLA Odoo
Cloud Hosting](https://www.odoo.com/cloud-sla).

## Noms de domaine

Use a custom [domain
name](../applications/websites/website/configuration/domain_names.html) to
access the database via another URL.

Astuce

You can [register a domain name for
free](../applications/websites/website/configuration/domain_names.html#domain-
name-register).

## Étiquettes

Ajoutez des étiquettes pour facilement identifier vos bases de données et les
trier.

Astuce

Vous pouvez rechercher des étiquettes dans la barre de recherche.

## Supprimer

Supprimez une base de données instantanément.

Danger

Supprimer une base de données signifie que toutes les données sont perdues à
jamais. La suppression est instantanée et s’applique à tous les utilisateurs.
Il est recommandé de créer une sauvegarde de la base de données avant de la
supprimer.

Lisez attentivement le message d’avertissement et ne continuez que si vous
avez bien compris les implications de la suppression d’une base de données.

![Le message d'avertissement s'affiche avant de supprimer une base de
données](../_images/delete.png)

Note

  * Seul un administrateur peut supprimer une base de données.

  * Le nom de la base de données est immédiatement accessible à tous.

  * Il n’est pas possible de supprimer une base de données si elle a expiré ou si elle est liée à un abonnement. Dans ce cas, contactez l”[Assistance d’Odoo](https://www.odoo.com/help).

## Contactez-nous

Accédez à la [page d’assistance d’Odoo.com](https://www.odoo.com/help) avec
les détails de votre base de données déjà préremplis.

## Inviter / supprimer des utilisateurs

Pour inviter des utilisateurs, saisissez l’adresse email du nouvel utilisateur
et cliquez sur Inviter. Pour ajouter plusieurs utilisateurs, cliquez sur
Ajouter plus d’utilisateurs.

![Inviter un utilisateur dans une base de données](../_images/invite-
users.png)

Pour supprimer des utilisateurs, sélectionnez-les et cliquez sur Supprimer.

Pour plus d'infos

  * [Utilisateurs](../applications/general/users.html)

  * [Comptes Odoo.com](odoo_accounts.html)

