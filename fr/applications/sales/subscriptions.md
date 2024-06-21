# Abonnements

Konvergo ERP _Abonnements_ est utilisé pour gérer des activités récurrentes : vendre
de nouveaux contrats, [réaliser de la vente
incitative](subscriptions/upselling), maîtriser le taux d’attrition et
[générer des rapports](subscriptions/reports) sur les principaux KPIs :
MRR, ARR, rétention, attrition, etc.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/slides/subscription-20">Tutoriels Konvergo ERP : Abonnements</a></p></li>
<li><p><a href="subscriptions/products">Produits d’abonnement</a></p></li>
<li><p><a href="subscriptions/ecommerce">Utiliser des abonnements dans eCommerce</a></p></li>
<li><p><a href="subscriptions/plans">Plans d’abonnement</a></p></li>
<li><p><a href="subscriptions/upselling">Appliquer la vente incitative à un abonnement</a></p></li>
<li><p><a href="subscriptions/renewals">Renouveler un abonnement</a></p></li>
<li><p><a href="subscriptions/closing">Résilier un abonnement</a></p></li>
<li><p><a href="subscriptions/automatic_alerts">Alertes automatiques</a></p></li>
<li><p><a href="subscriptions/reports">Rapports</a></p></li>
</ul>
</div>

## Devis d’abonnement

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les commandes avec une récurrence définie se transforment en abonnements.</p>
</div>

Pour créer un nouvel abonnement, cliquez sur **Nouveau** à partir de l”
_abonnement_ ou l’application [Ventes](../sales). Vous pouvez soit :

  * Sélectionner un [plan d’abonnement](subscriptions/plans) pour préremplir le devis instantanément, ou

  * Compléter le devis normalement, veillant à sélectionner une récurrence et une date de fin si nécessaire et à ajouter des [produits récurrents](subscriptions/products).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez définir des adresses de facturation et de livraison différentes en activant la fonctionnalité <a href="../finance/accounting/customer_invoices/customer_addresses">Adresses du client</a>.</p>
</div>

## Confirmation

Envoyez le devis au client pour confirmation en cliquant sur **Envoyer par
email** ou confirmez-le immédiatement en cliquant sur **Confirmer**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cliquez sur <b>Aperçu client</b> pour afficher un aperçu du portail client où le client peut voir son devis, le signer, le payer et le communiquer avec vous.</p>
</div>

## Paiements automatiques

Vous pouvez demander au client de définir un mode de paiement automatique et
payer à l’avance la première occurrence de l’abonnement avant de pouvoir
confirmer son devis. Pour ce faire, allez à l’onglet **Autres informations**
du devis et cochez l’option **Paiement** dans le champ **Confirmation en
ligne**.

Si vous ne cochez pas l’option **Paiement** , le client ne doit pas payer à
l’avance pour démarrer l’abonnement. Cela signifie que le paiement n’est pas
automatique et que le client doit payer chaque facture manuellement.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If the online confirmation requires a pre-payment, your customer can select only the
<a href="../finance/payment_providers#payment-providers-supported-providers"><span class="std std-ref">payment providers</span></a> that have the <a href="../finance/payment_providers#payment-providers-tokenization"><span class="std std-ref">tokenization
feature</span></a>. This ensures that the customer is automatically
charged at each new period.</p>
</div>

  * [Produits d’abonnement](subscriptions/products)
  * [Utiliser des abonnements dans eCommerce](subscriptions/ecommerce)
  * [Plans d’abonnement](subscriptions/plans)
  * [Appliquer la vente incitative à un abonnement](subscriptions/upselling)
  * [Renouveler un abonnement](subscriptions/renewals)
  * [Résilier un abonnement](subscriptions/closing)
  * [Alertes automatiques](subscriptions/automatic_alerts)
  * [Rapports](subscriptions/reports)

  *[KPIs]: Key Performance Indicators
  *[MRR]: Revenu mensuel récurrent
  *[ARR]: Revenu annuel récurrent

