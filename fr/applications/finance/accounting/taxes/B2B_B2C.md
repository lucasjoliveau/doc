# Prix B2B (hors taxes) et B2C (toutes taxes comprises)

Lorsque vous travaillez avec des consommateurs, les prix sont généralement
exprimés avec les taxes incluses dans le prix (par exemple, sur la plupart des
sites eCommerce). Mais, lorsque vous travaillez dans un environnement B2B, les
entreprises négocient généralement des prix hors taxes.

Konvergo ERP gère facilement les deux cas d’utilisation, tant que vous enregistrez vos
prix sur le produit hors taxes ou toutes taxes comprises, mais pas les deux en
même temps. Si vous gérez tous vos prix TTC (ou HT) seulement, vous pouvez
toujours faire facilement des commandes clients ayant des prix HT (ou TTC) :
c’est facile.

Cette documentation ne concerne que le cas d’utilisation spécifique où vous
devez avoir deux références de prix (toutes taxes comprises ou hors taxes),
pour le même produit. La raison de la complexité est qu’il n’y a pas une
relation symétrique entre les prix TTC et les prix HT, comme le montre ce cas
d’utilisation, en Belgique avec une taxe de 21% :

  * Votre site d’eCommerce propose un article à **10 € (TTC)**

  * Cela ferait **8,26€ (HT)** et une **TVA de 1,74€**

Mais pour le même cas d’utilisation, si vous n’enregistrez que le prix HT sur
la fiche du produit (8,26€), vous obtenez un prix TTC de 9,99 €, parce que :

  * **8,26€ * 1,21 = 9,99€**

Donc, selon la façon dont vous enregistrez vos prix sur la fiche du produit,
vous aurez des résultats différents pour le prix TTC et le prix HT :

  * Hors taxes : **8,26€ & 10,00€**

  * Toutes taxes comprises : **8,26€ & 9,99€**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous achetez 100 pièces à 10€ TTC, ça devient encore plus compliqué. Vous obtiendrez : <a href="#id1"><span class="problematic" id="id2">**</span></a>1000€ (TTC) = 826,45€ (prix) + 173,55€ (TVA) ** ce qui est très différent d’un prix à l’unité de 8,26€ HT.</p>
</div>

Cette documentation explique comment gérer le cas d’utilisation très
spécifique où vous devez gérer les deux prix (HT et TTC) sur la fiche du
produit au sein de la même entreprise.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sur le plan financier, vous n’avez pas plus de revenus en vendant votre produit à 10€ au lieu de 9,99€ (pour une taxe de 21%), parce que votre revenu sera exactement le même à 9,99€, seule la taxe est plus élevée de 0,01€. Donc, si vous gérez un site d’eCommerce en Belgique, faites une faveur à votre client et fixez votre prix à 9,99€ au lieu de 10€. Notez que cela ne s’applique pas aux prix de 20€ ou 30€, ni aux autres taux de TVA, ni à une quantité &gt;1. Vous vous rendrez également service puisque vous pouvez tout gérer hors taxes, ce qui est moins sujet aux erreurs et plus facile pour vos vendeurs.</p>
</div>

## Configuration

### Introduction

La meilleure façon d’éviter cette complexité est de choisir une seule façon de
gérer vos prix et de s’y tenir : prix hors taxes ou prix toutes taxes
comprises. Définissez lequel sera enregistré par défaut sur la fiche du
produit (sur la taxe par défaut liée au produit) et laissez Konvergo ERP calculer
l’autre automatiquement, sur la base de la liste des prix et de la position
fiscale. Négociez vos contrats avec les clients en conséquence. Cette solution
est prête à l’emploi et vous n’avez aucune configuration spécifique à faire.

Si cette solution est impossible et si vous négociez réellement certains prix
hors taxes et d’autres prix toutes taxes comprises pour d’autres clients, vous
devez :

  1. toujours sauvegarder le prix par défaut **hors taxes** sur la fiche du produit et appliquer une taxe (pris hors taxes sur la fiche du produit)

  2. créer une liste de prix avec des prix **toutes taxes comprises** pour des clients spécifiques

  3. créer une position fiscale qui permute de HT à TTC

  4. affecter à la fois la liste des prix et la position fiscale aux clients qui souhaitent bénéficier de cette liste de prix et de cette position fiscale

Dans le cadre de cette documentation, nous allons utiliser le cas d’usage
susmentionné :

  * votre prix de vente par défaut du produit est de 8,26€ HT

  * mais vous voulez le vendre à 10€ TTC dans vos boutiques ou votre eCommerce

### eCommerce

Si vous utilisez uniquement des prix B2C ou B2B sur votre site web, il vous
suffit de sélectionner le paramètre approprié dans les paramètres de
l’application **Site Web**.

Si vous avez à la fois des prix B2B et B2C sur un seul site web, suivez ces
instructions :

  1. Activez le [mode développeur](../../../general/developer_mode#developer-mode) et allez à Paramètres généraux ‣ Utilisateurs & Sociétés ‣ Groupes.

  2. Ouvrez soit `Technique / Affichage des taxes B2B` ou `Technique / Affichage des taxes B2C`.

  3. Sous l’onglet **Utilisateurs** , ajoutez les utilisateurs nécessitant un accès au type de prix. Ajoutez les utilisateurs B2C dans le groupe B2C et les utilisateurs B2B dans le groupe B2B.

### Configurer vos produits

Votre entreprise doit être configurée hors taxes par défaut. C’est
généralement la configuration par défaut, mais vous pouvez vérifier votre
**Taxe de vente par défaut** dans le menu Configuration ‣ Paramètres de
l’application Comptabilité.

![../../../../_images/price_B2C_B2B01.png](../../../../_images/price_B2C_B2B01.png)

Une fois cela fait, vous pouvez créer une liste de prix **B2C**. Vous pouvez
activer la fonction liste de prix par client dans le menu Configuration ‣
Paramètres de l’application Ventes. Choisissez l’option **Prix différents par
segment de clients**.

Ensuite, créez une liste de prix B2C dans le menu Configuration ‣ Listes de
prix. Il est également recommandé de renommer la liste de prix par défaut en
B2B pour éviter toute confusion.

Ensuite, créez un produit à 8,26€, avec une TVA de 21% (définie comme HT dans
le prix) et fixez un prix sur ce produit pour les clients B2C à 10€, depuis le
menu Ventes ‣ Produits de l’application Ventes :

![../../../../_images/price_B2C_B2B02.png](../../../../_images/price_B2C_B2B02.png)

### Configuration de la position fiscale B2C

Depuis l’application Comptabilité, créez une position fiscale B2C dans ce menu
Configuration ‣ Positions fiscales. Cette position fiscale devrait faire
correspondre la TVA de 21% (prix HT) avec une TVA de 21% (prix TTC)

![../../../../_images/price_B2C_B2B03.png](../../../../_images/price_B2C_B2B03.png)

## Tester en créant un devis

Créez un devis depuis l’application Ventes, en utilisant le menu Ventes ‣
Devis. Vous devriez obtenir le résultat suivant : 8,26€ + 1,73€ = 9,99€.

![../../../../_images/price_B2C_B2B04.png](../../../../_images/price_B2C_B2B04.png)

Ensuite, créez un devis, mais **modifiez la liste de prix à B2C et la position
fiscale à B2C** sur le devis, avant d’ajouter votre produit. Vous devriez
obtenir le résultat escompté, qui est un prix total de 10€ pour le client :
8,26€ + 1,74€ = 10,00€.

![../../../../_images/price_B2C_B2B05.png](../../../../_images/price_B2C_B2B05.png)

Ceci est le comportement attendu pour un client de votre boutique.

## Éviter de changer chaque commande client

Si vous négociez un contrat avec un client, que vous négociez un prix TTC ou
un prix HT, vous pouvez paramétrer la liste de prix et la position fiscale sur
la fiche client afin qu’elles soient appliquées automatiquement à chaque vente
de ce client.

La liste de prix est définie dans l’onglet **Ventes & Achats** de la fiche
client et la position fiscale dans l’onglet Comptabilité.

Notez que cette méthode est sujette aux erreurs : si vous définissez une
position fiscale avec des prix TTC, mais utilisez une liste de prix HT, vous
pourriez avoir des prix mal calculés. C’est pourquoi nous recommandons
généralement aux entreprises de ne travailler qu’avec une seule liste de prix.

