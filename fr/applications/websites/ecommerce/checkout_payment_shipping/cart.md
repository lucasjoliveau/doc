# Ajouter au panier

Le bouton **Ajouter au panier** peut être personnalisé de plusieurs façons.
Vous pouvez :

  * Choisir vers quelle page les clients sont redirigés après avoir cliqué sur le bouton “Ajouter au panier” ;

  * Masquer le bouton “Ajouter au panier” pour empêcher les ventes ;

  * Ajouter un bouton “Acheter maintenant” pour sauter l’étape du panier et rediriger les clients directement vers le paiement ;

  * Créer des boutons “Ajouter au panier / Acheter maintenant” supplémentaires ;

  * Ajouter un bouton “Recommander” au portail client.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><span class="xref std std-doc">paiement</span></p>
</div>

## Personnalisation de l’action “Ajouter au panier”

Lorsque les clients cliquent sur le bouton **Ajouter au panier** , le produit
est ajouté à leur panier et les clients restent **par défaut** sur la page des
produits. Toutefois, les clients peuvent soit être **redirigés** immédiatement
vers leur panier, soit choisir ce qu’ils veulent faire dans une **boîte de
dialogue**.

Pour changer le comportement par défaut, allez à Site Web ‣ Configuration ‣
Paramètres Sous la section **Boutique - Processus de paiement** , cherchez
**Ajouter au panier** et sélectionnez une des options.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un produit propose des <a href="../managing_products/cross_upselling">produits optionnels</a>, la <b>boîte de dialogue</b> s’affichera toujours.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../managing_products/catalog">Catalogue</a></p>
</div>

## Remplacer le bouton “Ajouter au panier” par le bouton “Contactez-nous”

Vous pouvez remplacer le bouton “Ajouter au panier” par un bouton “Contactez-
nous” qui redirige les utilisateurs vers l’URL de votre choix.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les entreprises B2B masquent souvent le bouton <b>Ajouter au panier</b>, car elles doivent limiter les achats aux seuls <a href="checkout#checkout-sign"><span class="std std-ref">clients disposant d’un compte</span></a>, malgré leur souhait d’afficher un catalogue de produits en ligne pour ceux qui n’en ont pas.</p>
</div>

Pour ce faire, allez à Site Web ‣ Configuration ‣ Paramètres ‣ Boutique -
Produits et cochez la case à côté de **Prévenir la vente de produits à prix
nul**. Ceci crée un nouveau champ **Bouton URL** où vous pouvez saisir l”**URL
de redirection** que vous voulez utiliser. Ensuite, définissez le prix du
produit sur `0.00` soit à partir du **modèle du produit** , soit à partir
d’une [liste de
prix](../../../sales/sales/products_prices/prices/pricing).

![Le bouton 'Contactez-nous' sur la page produit](../../../../_images/cart-
contactus.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le bouton “Contactez-nous” et le texte “<em>Pas disponible à la vente</em>” peuvent être modifiés avec le <b>constructeur de site web</b> sur la page du produit (Modifier ‣ Personnaliser) en cliquant dessus.</p>
</div>

## Personnaliser le bouton “Ajouter au panier”

Vous pouvez également créer un bouton “Ajouter au panier” personnalisé et le
lier à un produit spécifique. Le **bouton personnalisé** peut être ajouté sur
n’importe quelle page du site web comme un bloc de construction de **contenu
interne** et est un bouton _additionnel_ au bouton normal **Ajouter au
panier**.

Pour l’ajouter, allez à la page **Boutique** de votre choix, cliquez sur
Modifier ‣ Blocs et déposez le bloc de construction. Une fois celui-ci placé,
vous avez plusieurs options :

  * **Produit** : sélectionnez le produit auquel le bouton doit être associé. La sélection d’un produit rend le champ **Action** disponible ;

  * **Action** : choisissez si le bouton doit **Ajouter au panier** ou **Acheter maintenant** (paiement instantané).

![Personnaliser le bouton 'Ajouter au panier'](../../../../_images/cart-
add.png)

## Le bouton “Acheter maintenant”

Vous pouvez activer le bouton “Acheter maintenant” pour rediriger le client
instantanément vers le **paiement** au lieu d’ajouter le produit au panier. Le
bouton **Acheter maintenant** est un bouton _supplémentaire_ et ne remplace
pas le bouton **Ajouter au panier**. Pour l’activer, allez à Site Web ‣
Configuration ‣ Paramètres ‣ Boutique - Processus de paiement et cochez la
case à côté d”**Acheter maintenant**.

![Le bouton 'Acheter maintenant'](../../../../_images/cart-buy-now.png)

## Renouveler la commande depuis le portail

Les clients ont la possibilité de **recommander** des articles à partir de
**commandes précédentes** sur le portail client. Pour ce faire, allez à Site
Web ‣ Configuration ‣ Paramètres ‣ Boutique - Processus de paiement et activez
**Renouveler la commande depuis le portail**. Les clients peuvent trouver le
bouton **Recommander** sur leur **commande** dans le **portail client**.

![Le bouton 'Recommander'](../../../../_images/cart-reorder.png)

