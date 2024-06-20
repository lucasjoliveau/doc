# Neutralized database

A neutralized database is a non-production database on which several
parameters are deactivated. This enables one to carry out tests without the
risk of launching specific automated processes that could impact production
data (e.g., sending emails to customers). Live access is removed and turned
into a testing environment.

Note

**Toutes base de données de test créée est une base de données neutralisée**

  * test des bases de données de secours

  * dupliquer les bases de données

  * pour Odoo.sh : bases de données de préproduction et de développement

Important

Une base de données peut être neutralisée pendant la migration car il est
important de faire des tests avant de basculer sur une nouvelle version.

## Fonctionnalités désactivées

Voici une liste non exhaustive des paramètres désactivés :

  * toutes les actions automatisées (par exemple les factures automatiques d’abonnements, les emails marketing etc.)

  * emails sortants

  * synchronisation bancaire

  * fournisseurs de paiements

  * modes de livraison

  * IAP tokens

Note

**A red banner at the top of the screen is displayed on the neutralized
database so that it can be seen immediately.**

  *[IAP]: In-App Purchase

