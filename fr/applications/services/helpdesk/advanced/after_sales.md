# Services après-vente

Il est possible de configurer des services _après-vente_ dans l’application
_Assistance_ pour des _équipes_ individuelles. Une fois cette option activée,
les utilisateurs peuvent émettre des remboursements, traiter des retours,
générer des bons de réduction et/ou planifier des réparations ou des services
sur site directement à partir d’un ticket.

## Configurer les services après-vente

Commencez par activer les services après-vente sur des équipes d” _Assistance_
spécifiques, en allant à Assistance ‣ Configuration ‣ Équipes et en
sélectionnant la ou les équipes sur lesquelles ces services devraient être
actifs. Ensuite, faites défiler jusqu’à la section **Après-vente** sur la page
des paramètres de l’équipe et choisissiez l’une des options suivantes à
activer :

  * **Remboursements** : permet d’émettre des avoirs pour rembourser un client ou ajuster le montant restant dû

  * **Bons de réduction** : permet d’offrir des remises et des produits gratuits par le biais d’un programme de remises existant

  * **Retours** : permet d’initier un retour de produit de la part d’un client par le biais d’une annulation de transfert.

  * **Réparations** : permet de créer des ordres de réparation pour les produits cassés ou défectueux

  * **Services sur site** : permet de planifier une intervention sur site par le biais de l’application _Services sur site_

![../../../../_images/after-sales-enable.png](../../../../_images/after-sales-
enable.png)

Les services activés peuvent varier en fonction du type d’assistance fourni
par une équipe.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Comme tous les services d’après-vente d’Konvergo ERP nécessitent une intégration avec d’autres applications, l’activation de l’un d’entre eux peut entraîner l’installation de modules ou d’applications supplémentaires. <em>L’installation d’une nouvelle application sur une base de données Une App Gratuite déclenchera une période d’essai de 15 jours. À la fin de la période d’essai, si un abonnement payant n’a pas été ajouté à la base de données, celle-ci ne sera plus accessible.</em></p>
</div>

## Émettre un remboursement avec un avoir

Un _avoir_ est un document délivré à un client pour l’informer qu’il a été
crédité d’une certaine somme d’argent. Il peut être utilisé pour rembourser
intégralement un client ou ajuster le montant restant dû. Bien qu’ils soient
généralement créés par le biais des applications _Comptabilité_ ou
_Facturation_ , ils peuvent également être créés à partir d’un ticket d”
_Assistance_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les factures doivent être comptabilisées avant qu’un avoir puisse être généré.</p>
</div>

Pour créer un avoir, allez au ticket dans l’application Assistance et cliquez
sur le bouton **Remboursement** dans le coin supérieur gauche du tableau de
bord des tickets. Sélectionnez ensuite la facture correspondante dans le menu
déroulant **Factures à rembourser**.

![Vue d'une page de création d'un remboursement.](../../../../_images/after-
sales-refund-details.png)

Choisissez une **Méthode de crédit** parmi l’une des options suivantes :

  * **Remboursement partiel** : l’avoir est créé en brouillon et peut être édité avant d’être émis

  * **Remboursement intégral** : l’avoir est validé automatiquement et lettré avec la facture. _Il s’agit de l’option à choisir lorsqu’une facture validée doit être annulée_

  * **Remboursement intégral et nouvelle facture brouillon** : l’avoir est validé automatiquement et lettré avec la facture. La facture originale est dupliquée comme un nouveau brouillon. _Il s’agit de l’option à choisir lorsqu’une facture validée doit être modifiée_

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les options de <b>méthode de crédit</b> ne seront <b>pas</b> disponibles pour les factures qui ont déjà été payées.</p>
</div>

Apportez toutes les modifications nécessaires aux détails de l’avoir et
cliquez sur **Extourner.** Cliquez ensuite sur **Confirmer** pour
comptabiliser l’avoir.

Une fois que l’avoir a été comptabilisé, un bouton intelligent **Avoirs** sera
ajouté au ticket d” _Assistance_.

![Vue des boutons intelligents sur un ticket surlignant le bouton des
avoirs.](../../../../_images/after-sales-credit-note-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/accounting/customer_invoices/credit_notes">Avoirs et remboursements</a></p>
</div>

## Générer des bons de réduction à partir d’un ticket

Les bons de réduction peuvent être utilisés pour modifier le prix des produits
ou des commandes. Les contraintes d’utilisation d’un bon de réduction sont
définies par les règles conditionnelles. Les _programmes de bons de réduction_
sont configurés dans les applications _Ventes_ ou _Site Web_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le module <em>eCommerce</em> doit être installé afin de créer des codes promo à partir du <em>Site Web</em>.</p>
</div>

Pour générer un bon de réduction, ouvrez un ticket d” _Assistance_ et cliquez
sur le bouton **Bon de réduction** dans le coin supérieur gauche. Sélectionnez
une option dans le menu déroulant **Programme de bon de réduction** et cliquez
sur **Générer**.

![Vue d'une fenêtre de génération d'un bon de
réduction.](../../../../_images/after-sales-generate-coupon.png)

Le **Code promo** peut être copié directement à partir de la fenêtre
contextuelle (en cliquant sur le bouton **Copier**) ou envoyé par email en
cliquant sur **Envoyer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lors de l’envoi par email d’un code promo, tous les abonnés d’un ticket seront ajoutés en tant que destinataires de l’email. Il est possible d’ajouter des destinataires supplémentaires à l’email dans le champ <b>Destinataires</b> de la fenêtre contextuelle <b>Composer un email</b>.</p>
<img alt="Vue d'une fenêtre de brouillon d'email avec un code promo." class="align-center" src="../../../../_images/after-sales-coupon-email.png"/>
</div>

Une fois qu’un **Code promo** a été généré, un bouton intelligent **Bons de
réduction** sera ajouté en haut du ticket ; cliquez sur le bouton intelligent
pour afficher le code promo, la date d’expiration et d’autres informations.

![Vue des boutons intelligents sur un ticket surlignant le bouton des bons de
réduction.](../../../../_images/after-sales-coupon-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odoo.com/slides/slide/coupon-programs-640?fullscreen=1">Bons de réduction</a></p>
</div>

## Faciliter un retour de produit avec une annulation de transfert

Les retours sont effectués par le biais d” _annulations de transfert_ , qui
génèrent de nouvelles opérations d’entrepôt pour les produits retournés.
Cliquez sur le bouton **Retour** dans le coin supérieur gauche d’un ticket
pour ouvrir la fenêtre contextuelle **Annuler le transfert**.

![Vue d'un ticket d'assistance avec le bouton de retour mis en
évidence.](../../../../_images/after-sales-return-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le bouton <b>Retour</b> s’affiche uniquement sur un ticket si le client a une livraison enregistrée dans la base de données.</p>
</div>

Par défaut, la quantité correspondra à la quantité validée sur le bon de
livraison. Mettez à jour le champ **Quantité** le cas échéant.

![Vue d'une page de création d'une annulation de
transfert.](../../../../_images/after-sales-reverse-transfer.png)

Cliquez sur **Retour** pour confirmer le retour. Cette opération génère une
nouvelle opération d’entrepôt pour le ou les produits retournés entrants. Un
bouton intelligent **Retour** sera ajouté en haut du ticket.

![Vue du bouton intelligent de retour sur un ticket
d'assistance.](../../../../_images/after-sales-return-smart-button.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../sales/sales/products_prices/returns">Retours et remboursements</a></p>
</div>

## Envoyer des produits en réparation à partir d’un ticket

Si le ticket est lié à un problème avec un produit défectueux ou cassé, un
ordre de réparation peut être créé à partir du ticket d” _Assistance_ et
généré via l’application _Réparations_.

Pour créer un nouvel ordre de réparation, ouvrez un ticket d”Assistance et
cliquez sur le bouton **Réparation** dans le coin supérieur gauche.

Le fait de cliquer sur le bouton **Réparation** ouvre un formulaire
**Référence de réparation** vierge.

![Vue d'une page de référence de réparation.](../../../../_images/after-sales-
repair-reference.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un produit a été précisé dans le champ <b>Produit</b> sur le ticket, il sera automatiquement ajouté au champ <b>Produit à réparer</b>. Sinon, cliquez dans le champ pour sélectionner un produit dans la liste déroulante.</p>
</div>

Complétez le champ **Description de la réparation** en expliquant brièvement
le problème. Cliquez sur le champ **Commande client** et sélectionnez ensuite
la commande originale à partir de laquelle le produit est réparé. Si un retour
a été initié pour le produit, sélectionnez le numéro de référence dans le menu
déroulant du champ **Retour**.

Choisissez une **Méthode de facturation** dans le menu déroulant. Sélectionnez
**Avant la réparation** ou **Après la réparation** pour générer une facture
avant ou après l’achèvement du travail. Le fait de sélectionner **Pas de
facture** signifie qu’aucune facture ne sera générée pour ce service.

Si des pièces sont nécessaires pour la réparation, elles peuvent être ajoutées
dans l’onglet **Pièces**. Les services peuvent être ajoutés en tant que lignes
de produits dans l’onglet **Opérations**. Il est possible d’ajouter des
informations supplémentaires dans l’onglet **Notes de réparation**. Les
informations pour le client peuvent être ajoutées dans l’onglet **Notes sur le
devis** et seront automatiquement ajoutées au PDF des devis générés à partir
de cette **Référence de réparation**.

Un bouton intelligent **Réparations** sera ajouté au ticket, lié à l’ordre de
réparation.

![Vue des boutons intelligents mettant en évidence le bouton de
réparation.](../../../../_images/after-sales-repair-smart-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les factures doivent être comptabilisées avant qu’un avoir puisse être généré.</p>
</div>0

## Créer une tâche de service sur site à partir d’un ticket.

Les interventions sur site peuvent être planifiées à partir d’un ticket et
gérées via l’application _Services sur site_. Les clients disposant d’un
[accès au portail](../../../general/users/portal) pourront suivre la
progression d’une tâche de **services sur site** de la même manière qu’ils le
feraient pour un ticket d” _Assistance_.

Pour créer une nouvelle tâche, allez à un ticket d”Assistance. Cliquez sur
**Créer une tâche** pour ouvrir la fenêtre contextuelle **Créer une tâche de
services sur site** ou mettre à jour le **Titre** d’une tâche.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les factures doivent être comptabilisées avant qu’un avoir puisse être généré.</p>
</div>1

Cliquez sur **Créer une tâche** ou **Créer et voir la tâche**.

![Vue d'une page de création d'une tâche de services sur
site.](../../../../_images/after-sales-field-service-create.png)

Après la création de la tâche, un bouton intelligent **Tâches** sera ajouté au
ticket, liant la tâche de **Services sur site** au ticket.

![Vue des boutons intelligents d'un ticket mettant en évidant le bouton
tâches](../../../../_images/after-sales-field-service-smart-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les factures doivent être comptabilisées avant qu’un avoir puisse être généré.</p>
</div>2

