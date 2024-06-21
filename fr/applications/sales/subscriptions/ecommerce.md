# Utiliser des abonnements dans eCommerce

Les produits d’abonnement peuvent être vendus dans la boutique _eCommerce_
d’Konvergo ERP, tout comme les produits de vente ordinaires.

Cependant, par défaut, la page du produit eCommerce affiche uniquement la
période de récurrence la plus courte listée dans l’onglet **Tarification basée
sur le temps** de la fiche du produit. Par exemple, si un abonnement a des
périodes de récurrence _mensuelles_ et _annuelles_ configurées, seul le prix
mensuel s’affiche par défaut sur la page eCommerce pour ce produit.

Pour ajouter d’autres périodes de récurrence à la page du produit eCommerce,
créez une _variante de produit_ pour chaque période de récurrence.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="products">Configurer des produits d’abonnement</a></p></li>
<li><p><a href="../sales/products_prices/products/variants">Variantes de produit</a></p></li>
</ul>
</div>

## Créer des périodes de récurrence en tant que variantes de produit

Pour configurer chaque période de récurrence en tant que variante de produit,
allez à Abonnements ‣ Abonnements ‣ Produits et sélectionnez un produit. Sous
l’onglet **Attributs & Variantes**, cliquez sur **Ajouter une ligne**.

Créez un **Attribut** appelé `Période de facturation` (ou quelque chose de
similaire) en saisissant le nom et en cliquant sur **Créer**. Ce nom
d’attribut apparaît comme titre d’option sur la page du produit de la boutique
eCommerce.

Ensuite, créez des **Valeurs** qui correspondent aux périodes de récurrence
qui sont configurées dans l’onglet **Tarification basée sur le temps** de la
fiche du produit. Saisissez le nom d’une période de récurrence et cliquez sur
**Créer**. Ces noms de valeurs apparaissent comme des options sélectionnables
sur la page du produit de la boutique eCommerce.

![Périodes de récurrence configurées en tant que variantes de produit dans
l'onglet "Attributs & Variantes" de la fiche du
produit.](../../../_images/recurrence-period-attributes-variants.png)

Cliquez sur l’icône **☁️ (nuage)** en haut de la page pour enregistrer
manuellement. Après avoir enregistré, une colonne **Variantes de produit**
apparaît dans l’onglet **Tarification basée sur le temps**. Assignez les
variantes de produit à leurs périodes de récurrence et prix correspondants.

![Variantes de produit dans l'onglet "Tarification basée sur le temps" de la
fiche du produit.](../../../_images/product-variants-time-based-pricing.png)

Les variantes de produit sont désormais disponibles et peuvent être
sélectionnées sur la page de produit eCommerce.

![Les périodes de récurrence configurées comme des variantes de produit sur la
page de produit eCommerce.](../../../_images/recurrence-period-ecommerce.png)

