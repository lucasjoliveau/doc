# Gestion des produits

Konvergo ERP vous permet de créer, d’importer et de gérer vos pages produits avec
l’application **Site Web**.

## Ajouter des produits au catalogue

Pour ajouter un produit à votre catalogue, vous avez plusieurs possibilités :

  * À partir de n’importe quelle page de votre site web, cliquez sur \+ Nouveau ‣ Produit. Saisissez le nom de votre produit et cliquez sur **Enregistrer** ;

  * Site Web ‣ eCommerce ‣ Produits ‣ Créer;

  * ou [importer des données](../../../essentials/export_import_data#import-data) en utilisant des fichiers XLSX ou CSV. Pour ce faire, allez à Site Web ‣ eCommerce ‣ Produits. Cliquez sur **Favoris** et [Importer des enregistrements](../../../essentials/export_import_data#import-data).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="catalog">Catalogue</a></p></li>
<li><p><a href="../../../sales/sales/products_prices/products/import">Importer des produits</a></p></li>
<li><p><a href="../../../sales/sales">Documentation relative aux produits</a></p></li>
</ul>
</div>

### Publier

Lors de leur création, les produits sont par défaut **non publiés** dans votre
catalogue d’eCommerce. Pour rendre un produit visible aux visiteurs, allez à
Site Web ‣ Site ‣ Page d’accueil, cliquez sur la page de votre **boutique
principale** , sélectionnez le produit et activez-le comme **publié** dans le
coin supérieur droit.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour publier <b>un grand nombre</b> de produits, la méthode la plus pratique consiste à aller à Site Web ‣ eCommerce ‣ Produits. Ici, supprimez le filtre <b>Publié</b> en cliquant sur le <b>x</b> à côté de celui-ci et sélectionnez la vue <b>Liste</b>. Cliquez ensuite sur le bouton <b>déroulant</b> (situé juste en dessous du bouton <b>Liste</b>) et activez <b>Est publié</b>. Cliquez sur la colonne <b>Est publié</b> pour la réorganiser en fonction des produits <b>publiés</b> ou <b>non publiés</b>. Enfin, sélectionnez les produits à publier en cochant leur case à l’extrême droite et cochez n’importe quelle case des produits sélectionnés dans la colonne <b>Est publié</b> pour les publier tous.</p>
</div> ![Boutons de liste et du menu
déroulant](../../../../_images/products-buttons.png)

## Conception de la page produit

Une fois un produit créé, vous pouvez accéder à la **page produit** via la
page **Boutique** de votre site web en cliquant sur le produit et ensuite sur
**Modifier**. Vous pouvez alors changer les **fonctions additionnelles** de la
page, l”**agencement** , **ajouter du contenu** , etc. Notez que les
**fonctions activées** s’appliquent à _toutes_ les pages produits.

### Fonctions additionnelles

Dans la fenêtre du **constructeur de site web** , cliquez sur
**Personnaliser** pour activer des fonctions additionnelles :

  * **Clients : Évaluation** permet aux clients de soumettre des [évaluations de produits](../ecommerce_management/customer_interaction#product-reviews) ; **Partager** ajoute des icônes des réseaux sociaux et d’email pour partager le produit via ces canaux ;

  * **Sélection quantité** : si activée, cette option permet de choisir la quantité ajoutée au panier ;

  * **Indication taxes** : indique si le prix est **toutes taxes comprises** ou **hors taxes** ;

  * **Variantes** : affiche toutes les [variantes](../../../sales/sales/products_prices/products/variants) possibles du produit sous forme de **Liste des produits** ; **Options** sous forme d’options sélectionnables pour composer soi-même la variante ;

  * **Panier** : **Acheter maintenant** ajoute un [bouton de passage en caisse](../checkout_payment_shipping/cart#cart-buy-now) qui redirige le client directement vers la page de paiement ; **Liste de souhaits** vous permet d’ajouter le produit à la liste de souhaits ;

  * **Spécification** : vous permet de sélectionner où s’affiche la section **Spécifications**. Cette option affiche une liste de tous les attributs et valeurs des variantes d’un produit, mais ne fonctionne que pour les produits _ayant_ des variantes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Pour autoriser les <b>listes de souhaits</b>, l’option doit être activée dans Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Produits ;</p></li>
<li><p>Pour accéder aux options des <b>variantes</b>, l’option <a href="../../../sales/sales/products_prices/products/variants">Variantes de produits</a> doit d’abord être activée dans Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Produits.</p></li>
</ul>
</div>

### Agencement

Dans le même onglet **Personnalier** que les fonctions, la configuration de
l’agencement peut être modifiée en fonction de vos besoins.

  * **Largeur images** : change la largeur de l’image du produit affichée sur la page ;

  * **Agencement** : l’agencement **Carrousel** affiche une grande image principale et des images plus petites en dessous, tandis que **Grille** affiche quatre images dans une disposition carrée (voir les images ci-dessous) ;

  * **Zoom d’image** : choisissez si des zooms d’image sont disponibles, soit **Pop-up au clic** , au survol de l’image (**Loupe au survol**), sur **Les deux** , ou **Aucun** ;

  * **Vignette** : décidez de la manière dont les vignettes doivent être alignées, soit **verticalement** (**Gauche**), ou **horizontalement** (:guilabel:Droite`) ;

  * **Image principale** : cliquez sur **Remplacer** pour changer l’image principale du produit ;

  * **Images extra** : cliquez sur **Ajouter** ou **Tout supprimer** pour ajouter ou supprimer des images de produit supplémentaires. Vous pouvez également ajouter des images et des vidéos via une **URL**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les images doivent avoir le format PNG ou JPG. Pour activer le zoom, l’image doit être plus grande que 1024x1024.</p>
</div> ![Agencement des images de
produit](../../../../_images/products-layout.png)

### Ajouter du contenu

Vous pouvez utiliser des **blocs de construction** (Modifier ‣ Blocs) pour
ajouter du contenu à votre page produit. Ces blocs peuvent être utilisés pour
ajouter du texte et des images supplémentaires, des fonctions telles que des
**Appels à l’action** , des **Comparaisons** , etc.

Selon l’endroit _où_ vous déposez le **bloc de construction** , il peut être
disponible soit sur la page produit _uniquement_ , soit sur _l’ensemble_ du
site web. Les **blocs de construction** déposés tout en haut ou tout en bas de
la page sont disponibles sur _l’ensemble_ du site web, alors que les **blocs
de construction** placés sous la description du produit sont uniquement
affichés sur la page du _produit_ _(voir l’image ci-dessous)_.

![Blocs de construction sur la page produit](../../../../_images/products-
blocks.png)

### Lien de téléchargement

Pour ajouter un fichier téléchargeable (par ex. manuel d’utilisation, notice
d’utilisation, etc.) à la page produit, glissez et déposez un bloc **Texte**
depuis Modifier ‣ Blocs sur la page. Une fois placé, cliquez sur le bloc
**Texte** et dans la section **Texte inline** , sélectionnez soit Insérer un
média ‣ Documents, soit **Insérer ou modifier un lien** et saisissez l’URL
dans le champ **Votre URL**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La différence avec les <a href="#ecommerce-digital-file"><span class="std std-ref">fichiers numériques</span></a> est que ces derniers ne peuvent être téléchargés qu”<em>après</em> le paiement.</p>
</div> ![Boutons média et lien](../../../../_images/products-
media.png)

### Fichiers numériques

Si votre produit est vendu avec un certificat, manuel d’utilisation ou tout
autre document pertinent, il est possible d’ajouter un lien téléchargeable à
la fin du passage en caisse. Pour ce faire, activez d’abord **Contenu
numérique** dans Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Processus
de paiement. Ensuite, sur le **modèle du produit** , cliquez sur Plus ‣
Fichiers numériques et **créez** un nouveau fichier.

![Menu des fichiers numériques](../../../../_images/products-digital-
files.png)

Pour la configuration :

  * **Nom** : le nom de votre fichier ;

  * **Type :** sélectionnez s’il s’agit d’un **fichier** ou une **URL**. En conséquence, vous disposez soit d’un champ **Contenu du fichier (base64)** pour télécharger votre fichier ou un champ **URL** pour saisir votre URL.

  * **Site web** : le site web sur lequel ce fichier est _disponible_. Si vous souhaitez qu’il soit disponible sur _tous_ les sites web, laissez ce champ vide.

Le fichier est ensuite disponible après le paiement dans la section **bon de
commande** du portail du client.

## Configuration du produit

### Langues multiples

Si plusieurs langues sont disponibles sur votre site web et vous souhaitez que
les informations relatives au produit soient traduites, il est nécessaire
d’encoder ces informations traduites dans le **modèle du produit**. Les champs
dans lesquels plusieurs langues sont disponibles sont identifiables par
l’abréviation de la langue (par ex. FR) à côté du champ.

![Champ traduction](../../../../_images/products-field-translation.png)

Les champs **relatifs à l’eCommerce* à traduire sont les suivants :

  * **Nom du produit** ;

  * **Message de rupture de stock** (sous d’onglet **Vente**) ;

  * **Description vente** (sous l’onglet **Vente**) ;

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La présence de contenu non traduit sur une page web peut nuire à l’expérience de l’utilisateur et au <a href="../../website/pages/seo">référencement</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour vérifier la ou les langues de votre site web, allez à Site Web ‣ Configuration ‣ Paramètres ‣ Infos du site web.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../website/pages/seo">Search Engine Optimization (SEO)</a></p></li>
</ul>
</div>

### Disponibilité sur le site web

Un produit peut être rendu disponible sur _un_ ou _tous_ les sites web, mais
il n’est pas possible de sélectionner _certains_ sites web et pas d’autres.
Pour définir la disponibilité d’un produit, allez à Site Web ‣ eCommerce ‣
Produits, sélectionnez votre produit et dans l’onglet **Vente** , cliquez sur
le **site web** sur lequel vous voulez que le produit soit disponible. Laissez
le champ vide pour que le produit soit disponible sur _tous_ les sites web.

## Gestion des stocks

Dans Site Web ‣ Configuration ‣ Paramètres ‣ Boutique - Produits, vous pouvez
activer et configurer des options de gestion d’inventaire.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour afficher le niveau de stock sur le page produit, le <b>type de produit</b> sur la <b>fiche produit</b> doit être défini sur <b>Stockable</b> (uniquement disponible lorsque l’application <b>Inventaire</b> est installée).</p>
</div>

### Inventaire

Dans la sous-section **Valeurs par défaut de l’inventaire** , vous pouvez
sélectionner la stratégie de vente des produits dans votre eCommerce :

  * **Entrepôt** : si vous avez plusieurs entrepôts, vous pouvez définir l’entrepôt associé à votre site web. Si vous avez plusieurs sites web, vous pouvez choisir un entrepôt différent par site web ;

  * **En rupture de stock (Continuer la vente)** : permet aux clients de continuer à placer des commandes même lorsque le produit est **en rupture de stock**. Laissez la case décochée **empêcher les commandes** ;

  * **Afficher la qté disponible** : affiche la quantité disponible restante en dessous d’un seuil précisé sur la page produit. La quantité disponible est calculée sur la base de la quantité “disponible” moins la quantité déjà réservée pour les transferts sortants.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../checkout_payment_shipping/cart#cart-prevent-sale"><span class="std std-ref">Uniquement autoriser les clients sélectionnés d’acheter</span></a></p>
</div>

### Vendre en tant que kit

Si vous vendez des kits non préemballés (c’est-à-dire, les kits sont composés
de produits individuels), nous vous recommandons de lire la documentation
correspondante pour suivre votre stock.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour publier <b>un grand nombre</b> de produits, la méthode la plus pratique consiste à aller à Site Web ‣ eCommerce ‣ Produits. Ici, supprimez le filtre <b>Publié</b> en cliquant sur le <b>x</b> à côté de celui-ci et sélectionnez la vue <b>Liste</b>. Cliquez ensuite sur le bouton <b>déroulant</b> (situé juste en dessous du bouton <b>Liste</b>) et activez <b>Est publié</b>. Cliquez sur la colonne <b>Est publié</b> pour la réorganiser en fonction des produits <b>publiés</b> ou <b>non publiés</b>. Enfin, sélectionnez les produits à publier en cochant leur case à l’extrême droite et cochez n’importe quelle case des produits sélectionnés dans la colonne <b>Est publié</b> pour les publier tous.</p>
</div>0

## Comparaison des produits

Vous pouvez activer un **outil de comparaison de produits** pour votre
eCommerce en allant à Site Web ‣ Configuration ‣ Parampètres ‣ Boutique -
Produits et en cochant la case à côté d”**Outil de comparaison de produits**.
Cet outil vous permet de enregistrer les **spécifications** des produits et de
les comparer avec d’autres sur une même page.

Sur la page produit, descendez jusqu’à la section **Spécifications** et
cliquez sur **Comparer**. Répétez le même processus pour tous les produits que
vous souhaitez comparer. Cliquez ensuite sur le bouton **Comparer** de la
fenêtre contextuelle en bas de la page pour accéder au récapitulatif de la
comparaison.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour publier <b>un grand nombre</b> de produits, la méthode la plus pratique consiste à aller à Site Web ‣ eCommerce ‣ Produits. Ici, supprimez le filtre <b>Publié</b> en cliquant sur le <b>x</b> à côté de celui-ci et sélectionnez la vue <b>Liste</b>. Cliquez ensuite sur le bouton <b>déroulant</b> (situé juste en dessous du bouton <b>Liste</b>) et activez <b>Est publié</b>. Cliquez sur la colonne <b>Est publié</b> pour la réorganiser en fonction des produits <b>publiés</b> ou <b>non publiés</b>. Enfin, sélectionnez les produits à publier en cochant leur case à l’extrême droite et cochez n’importe quelle case des produits sélectionnés dans la colonne <b>Est publié</b> pour les publier tous.</p>
</div>1 ![Fenêtre de comparaison des
produits](../../../../_images/products-compare.png)

  *[FR]: français

