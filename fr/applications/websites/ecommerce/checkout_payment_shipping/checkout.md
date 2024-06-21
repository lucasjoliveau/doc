# Paiement

Vous pouvez personnaliser les **étapes de paiement** , ajouter plus de contenu
avec le **constructeur de site web** et activer des fonctionnalités
supplémentaires telles que **paiement rapide** ou **se connecter/s’inscrire
lors du paiement**.

Vous pouvez utiliser des **blocs de construction** pour ajouter du contenu à
n’importe quelle étape du processus de paiement. Pour ce faire, à partir de
n’importe quelle **page de paiement** , allez à Modifier ‣ Blocs et glissez et
déposez des **blocs de construction** sur la page.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Notez que le contenu ajouté par le biais des blocs de construction est <b>spécifique</b> à chaque étape.</p>
</div>

## Étapes de paiement

### Vérifier la commande : code promo (et sous-total)

Si vous avez activé **Remises, Fidélité & Cartes-cadeaux** dans les paramètres
(Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Produits), vous pouvez
activer le champ **Code promo** (Modifier ‣ Personnaliser) à partir de
n’importe quelle page de paiement. Les clients peuvent ensuite saisir des
cartes-cadeaux et des codes promotionnels lors de l’étape de la **vérification
de la commande**.

De plus, vous pouvez afficher le sous-total avec les remises appliquées en
activant la fonctionnalité **Afficher la remise dans le sous-total**.

![Sous-total avec la remise](../../../../_images/checkout-subtotal.png)

### Adresse : champs B2B

Les champs optionnels **TVA** et **Nom de la société** peuvent être ajoutés au
formulaire **Adresse de facturation** pour les clients B2B, lors de l’étape
**Adresse**. Pour ajouter ces champs, allez à Modifier ‣ Personnaliser à
partir de n’importe quelle page de paiement et activez **Afficher les champs
B2B**.

### Demander des informations supplémentaires (étape additionnelle)

Vous pouvez demander des **Informations supplémentaires** au client en
ajoutant une étape **Infos supplémentaires** entre les étapes **Adresse** et
**Confirmer la commande**. Pour ce faire, allez à Modifier ‣ Personnaliser à
partir de n’importe quelle page et activez l”**Option d’étape
supplémentaire**.

![Étapes de paiement](../../../../_images/checkout-steps.png)

L’étape **Infos supplémentaires** est un formulaire en ligne lié au devis ou à
la commande du client. Les informations ajoutées pendant cette étape figurent
sur le devis ou la commande du client dans le backend, dans l’application
**Ventes**.

Une fois l’option activée, vous pouvez supprimer, ajouter et modifier les
champs du formulaire en cliquant sur **Modifier** dans le coin supérieur droit
et ensuite en cliquant sur n’importe quel champ du formulaire. Toutes les
options de personnalisation et le bouton **\+ Champ** pour ajouter de nouveaux
champs sont disponibles en bas du menu **Personnaliser** sous la section
**Champ**.

![Personnalisation de formulaire en ligne](../../../../_images/checkout-
form.png)

### Confirmer la commande : conditions générales

Vous pouvez demander aux clients d’accepter les **Conditions générales** afin
de confirmer leur commande en activant **Accepter les conditions générales**
dans Modifier ‣ Personnaliser sur n’importe quelle page de paiement.

![Conditions générales](../../../../_images/checkout-terms.png)

## Paiement rapide

Vous pouvez activer un bouton **Acheter maintenant** sur les pages des
produits qui redirige les clients instantanément vers la page de paiement
**Confirmer la commande** , au lieu d’ajouter le produit au panier. Pour ce
faire, allez à Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Processus de
paiement et cochez la case à côté d”**Acheter maintenant**. De plus, le bouton
**Acheter maintenant** peut également être activé à partir de n’importe quelle
page de produit en allant à Modifier ‣ Personnaliser, dans la section
**Panier**.

Le bouton se trouve à côté du bouton **Ajouter au panier** sur la page du
produit.

![Bouton 'Acheter maintenant' \(paiement
rapide\)](../../../../_images/checkout-express.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../managing_products/products#ecommerce-functions"><span class="std std-ref">Conception de la page produit : fonctions additionnelles</span></a></p>
</div>

## Paiement en tant qu’invité et utilisateur connecté

Il est possible de mettre en place une **politique de paiement** en vertu de
laquelle les clients peuvent passer à la caisse en tant qu”**invités** ou
**utilisateurs connectés uniquement**. Les clients peuvent également passer à
la cause en tant qu’invités et **éventuellement s’inscrire ultérieurement**
pour suivre leur commande, si cette option est activée.

Pour sélectionner une politique, allez à Site Web ‣ Configuration ‣ Paramètres
‣ Boutique - Processus de paiement. Vous avez le choix entre :

  * **Optionnel** : permet aux clients de passer à la caisse et de s’enregistrer plus tard à partir de l’email de **confirmation de la commande** pour suivre leur commande ;

  * **Désactivé (acheter en tant qu’invité)** : les clients peuvent uniquement passer à la caisse en tant qu’invités ;

  * **Obligatoire (pas de paiement en tant qu’invité)** : les clients peuvent uniquement passer à la caisse s’ils se sont connectés.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../ecommerce_management/customer_accounts">Comptes clients</a></p></li>
<li><p><a href="../../../general/users/portal">Accès au portail</a></p></li>
</ul>
</div>

### Restriction d’accès B2B

Si vous voulez limiter le paiement uniquement aux **clients B2B sélectionnés**
, activez **Obligatoire (pas de paiement en tant qu’invité)** et allez à Site
Web ‣ eCommerce ‣ Clients. Sélectionnez le client auquel vous voulez **donner
accès** , cliquez sur Action ‣ Donner accès au portail et cliquez sur **Donner
accès**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les paramètres sont <b>spécifiques au site web</b>, ce qui signifie que vous voulez configurer un site web B2C autorisant le passage en caisse des <b>invités</b> et un autre pour les clients B2B avec une <b>connexion obligatoire</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les utilisateurs ne peuvent avoir qu’un seul accès au portail par <b>email</b>. Ils ne peuvent <em>pas</em> avoir accès à deux portails différents avec la même <b>adresse email</b>.</p>
</div>

### Comptes clients partagés

Si vous activez l’option **Comptes clients partagés** sous la section Site Web
‣ Configuration ‣ Paramètres ‣ Confidentialité, vous pouvez autoriser ou
révoquer l’accès à _tous_ les sites web pour un même compte.

