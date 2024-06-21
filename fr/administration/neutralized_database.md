# Neutralized database

A neutralized database is a non-production database on which several
parameters are deactivated. This enables one to carry out tests without the
risk of launching specific automated processes that could impact production
data (e.g., sending emails to customers). Live access is removed and turned
into a testing environment.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Toutes base de données de test créée est une base de données neutralisée</b></p>
<ul>
<li><p>test des bases de données de secours</p></li>
<li><p>dupliquer les bases de données</p></li>
<li><p>pour Konvergo ERP.sh : bases de données de préproduction et de développement</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Une base de données peut être neutralisée pendant la migration car il est important de faire des tests avant de basculer sur une nouvelle version.</p>
</div>

## Fonctionnalités désactivées

Voici une liste non exhaustive des paramètres désactivés :

  * toutes les actions automatisées (par exemple les factures automatiques d’abonnements, les emails marketing etc.)

  * emails sortants

  * synchronisation bancaire

  * fournisseurs de paiements

  * modes de livraison

  * IAP tokens

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>A red banner at the top of the screen is displayed on the neutralized database so that it can
be seen immediately.</b></p>
</div>

  *[IAP]: In-App Purchase

