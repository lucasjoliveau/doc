# Configuration du connecteur eBay

## Aperçu

Le connecteur eBay d’Konvergo ERP permet aux annonces d’eBay de se connecter aux
produits d’Konvergo ERP. Une fois qu’eBay est connecté, vous pouvez [mettre à jour les
annonces](linking_listings) dans Konvergo ERP et dans eBay. Lorsqu’un article est
vendu sur eBay, des _commandes_ brouillon sont créées dans Konvergo ERP que
l’utilisateur peut contrôler et confirmer. Une fois que la commande est
confirmée, les applications _Inventaire_ et _Ventes_ d’Konvergo ERP fonctionnent comme
d’habitude pour retirer des produits des stocks et permettre à l’utilisateur
de créer des factures.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour en apprendre plus sur le connecteur eBay, consultez également ces pages :</p>
<ul>
<li><p><a href="manage">Comment répertorier un produit ?</a></p></li>
<li><p><a href="linking_listings">Associer des annonces existantes</a></p></li>
<li><p><a href="troubleshooting">Dépannage du connecteur eBay</a></p></li>
</ul>
</div>

### Champs liés eBay - Konvergo ERP

Les champs suivants sont des détails de produit eBay. Chacun de ces champs
eBay mettent à jour les champs correspondants dans Konvergo ERP.

  * URL eBay

  * Statut eBay

  * Quantité vendue

  * Date de début

  * Titre

  * Sous-titre

  * État de l’article

  * Catégorie

  * Catégorie 2

  * Catégorie de magasin

  * Catégorie de magasin 2

  * Politique de paiement

  * Profiles vendeur

  * Code postal

  * Politique d’expédition

  * Type d’annonce (prix fixe ou vente aux enchères)

    * Enchère de départ

    * Prix Buy it now

    * Montant du prix fixe

  * Utiliser la quantité en stock

  * Quantité sur eBay

  * Durée

  * Autoriser la meilleure offre

  * Annonce privée

  * Description eBay

  * Image produit eBay

  * Pays

### Conditions eBay

Les _Versions_ permettent de regrouper plusieurs produits en un seul, avec
plusieurs versions (ou variantes). Les versions peuvent être synchronisées
avec les attributs et les valeurs d’Konvergo ERP. Les versions apparaissent dans les
menus déroulants situés en haut de la page lors de la consultation d’une
annonce eBay. Elles sont comparables aux variantes de produits dans Konvergo ERP.

![Un exemple sur eBay des versions qui peuvent être ajoutées à un
produit.](../../../../_images/ebay-variation.png)

Les _Caractéristiques de l’objet_ , situés au bas de l’annonce, fournissent
des informations spécifiques au produit. Ces caractéristiques ne sont pas
automatiquement synchronisés avec les champs d’Konvergo ERP, car un développement est
nécessaire pour lier ces champs.

![Les caractéristiques de l'objet sur un produit
eBay.](../../../../_images/item-specifics.png)

_Sandbox_ et _Production_ sont des termes utilisés pour catégoriser les
environnements eBay comme soit encore en développement/test (_Sandbox_), soit
destinés à être utilisés dans l’instance réelle de la base de données avec des
informations/ensembles de données de clients réels (_Production_). Il est
recommandé de commencer par le _Sandbox_ pour tester, puis de créer une
instance de _Production_ en suivant les processus ci-dessous.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La sélection de l’environnement <b>doit</b> rester inchangée pour tous les paramètres d’environnement sur eBay et sur Konvergo ERP tout au long de cette configuration.</p>
</div>

### Actions eBay disponibles dans Konvergo ERP

Les actions suivantes sont intégrées dans Konvergo ERP et permettent d’ajouter ou de
mettre à jour les annonces eBay :

  * **Liste** / **Lien** : générer une nouvelle annonce eBay avec un produit Konvergo ERP en cliquant sur **Vendre l’article sur eBay** ou **Associer à une annonce eBay existante**.

  * Le bouton **Modifier l’article** : après avoir modifié une annonce eBay dans Konvergo ERP, enregistrez l’enregistrement et cliquez sur **Modifier l’article** dans Konvergo ERP pour mettre à jour l’annonce eBay.

  * **Remettre en vente** : si l’annonce d’un article a pris fin prématurément ou si la fonction **remettre en vente automatiquement** n’est pas sélectionnée, un utilisateur peut remettre en vente l’article à partir d’Konvergo ERP. La date de début sera réinitialisée.

  * Le bouton **Terminer l’annonce d’un article** : mettre fin à une annonce sur eBay directement depuis Konvergo ERP.

  * **Dissocier les annonces de produits** : les utilisateurs peuvent dissocier un produit de l’annonce eBay ; l’annonce restera intacte sur eBay.

## Configuration requise dans Konvergo ERP avant la configuration d’eBay

Pour associer eBay à Konvergo ERP, installez le module eBay en allant au tableau de
bord d’Konvergo ERP et en cliquant sur l’application **Apps**. Recherchez le terme
`eBay` et installez le module `Connecteur eBay`.

Les éléments suivants doivent être configurés avant qu’eBay soit configuré :

  * Dans Konvergo ERP, créez et configurez les produits destinés à être listés sur eBay. eBay n’importe pas de nouveaux produits dans Konvergo ERP. Tous les produits doivent d’abord être créés dans Konvergo ERP, puis liés à des annonces.

    * Konvergo ERP ne permet pas d’associer plusieurs annonces eBay par produit dans Konvergo ERP. Si la société vend le même produit dans plusieurs annonces, suivez ces instructions :

      * Configurez un produit de _base_ (noté dans le champ **Composant** de la nomenclature à partir de laquelle toutes les annonces eBay seront tirées. Il s’agit d’un produit stockable qui permet de conserver des stocks. Surligné en vers ci-dessous, ce produit sera inclut dans le kit pour chaque produit “associé” suivant.

      * Configurez plus de deux produits _associés_ (notés dans le champ **Produit** de la nomenclature), un pour chaque annonce eBay. Le type de produit sera déterminé par les paramètres de comptabilité de la société, comme il est expliqué dans la documentation d’Konvergo ERP. Surligné en jaune ci-dessous, chaque produit doit avoir un **type de nomenclature** équivalent au **Kit** et le produit de base en tant que **Composant** du kit. Lorsque ce produit eBay associé est vendu, le bon de livraison créé indiquera le produit de base au lieu du produit associé.

![Configurer une nomenclature avec un produit de base et des produits
associés.](../../../../_images/products-odoo.png)

> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/manufacturing/management/bill_configuration">Bill of materials</a></p>
</div>

  * eBay ne crée pas automatiquement des factures pour les commandes eBay qui sont transférées dans Konvergo ERP. Définir la politique de facturation pour les produits eBay : la politique de facturation dictera lorsque le produit peut être facturé. Puisque la plupart des utilisateurs d’eBay encaissent le paiement avant l’expédition du produit, « facturer sur commande » permettra aux utilisateurs de créer en masse des factures pour les commandes eBay tous les jours.

  * Définissez la route **Expéditions** pour l’entrepôt afin de **Livrer les marchandises directement (1 étape)**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Lorsque la route des <b>Expéditions</b> est définie sur deux ou trois étapes, un problème connu se produit : eBay marque à tort les commandes comme livrées lorsque l’opération de transfert dans Konvergo ERP est confirmée. Le comportement attendu est de marquer les commandes comme livrées <b>après</b> la configuration du <em>bon de livraison</em>. Cette erreur d’étiquetage empêche les numéros de suivi dans eBay d’être importés dans le bon de livraison.</p>
</div>

  * Si les applications Comptabilité/Facturation sont installées, entraînez-vous à enregistrer les paiements et à lettrer les factures créées à partir des commandes eBay avec l’argent reçu d’eBay.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/accounting/bank/reconciliation">Rapprochement bancaire</a></p>
</div>

  * Générez un jeton de notification de suppression/clôture de compte de marketplace. Pour commencer, allez à l’application Ventes ‣ Configuration ‣ Paramètres. Dans l’en-tête **eBay** , modifiez le mode en **Production** et saisissez des valeurs de texte aléatoires pour la **Cert Key production**. Cliquez ensuite sur le bouton **Générer le jeton** dans la section **Notifications de suppression/clôture de compte eBay Marketplace**. Ce jeton sera utilisé pendant la configuration dans eBay pour la configuration des notifications de suppression/clôture.

![Générez un jeton de vérification dans Konvergo ERP.](../../../../_images/generate-
token.png)

## Configuration dans eBay

### Configurer un compte de développeur eBay

Pour commencer, créez un compte de développeur eBay via le [portail
développeur d’eBay](https://go.developer.ebay.com/). Ce site demande un login
et un mot de passe différents du compte eBay, même si la même adresse email
peut être utilisées pour vous inscrire. Le délai de vérification pour la
création d’un compte de développeur est d’environ 24 heures.

### Configurer un ensemble de clés eBay

Une fois le compte de développeur eBay créé, configurez une application sur le
[portail développeur d’eBay](https://go.developer.ebay.com/). Allez ensuite à
la rubrique **Bonjour [nom d’utilisateur]** en haut à droite de l’écran, puis,
dans le menu déroulant, cliquez sur **Ensembles de clés de l’application**.
Cette opération ouvre une fenêtre contextuelle qui invite l’utilisateur à
**Saisir le titre de l’application** (jusqu’à cinquante caractères), et
choisissez un environnement de développement (**Sandbox** ou **Production**).
Ces deux champs génèrent un premier ensemble de clés. Le titre de cette
application n’est pas enregistré jusqu’à ce que l’ensemble de clés soit
généré. Cliquez sur **Créer un ensemble de clés** pour générer l’ensemble de
clés.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>L”<em>ensemble de clés de production</em> nouvellement créé est désactivé par défaut. Activez-le en vous abonnant aux “notifications de suppression ou de clôture de compte” de la Marketplace eBay ou en demandant une dérogation à eBay. Une fois activée, la base de données peut passer 5000 appels par jour à l’aide de cet ensemble de clés.</p>
</div> ![Ensemble de clés désactivé après avoir créé un ensemble
de clés.](../../../../_images/disabled-keyset.png)

#### Configurer les paramètres de suppression de compte / de notification
(Production)

Pour configurer les notifications ou supprimer la base de données dans un
environnement de production, allez au [portail développeur
d’eBay](https://go.developer.ebay.com/). Configurez les paramètres de
suppression de compte/notification dans eBay en allant à la rubrique `Bonjour
[nom d'utilisateur]` en haut à droite de l’écran, puis à **Ensembles de clés
de l’application**.

Cliquez ensuite sur l’option **notification de suppression de la
marketplace/clôture du compte** dans la colonne de l’ensemble de clés
**Production**. Saisissez un email dans la section **Email à notifier si le
point de terminaison de notification de suppression de compte de la
marketplace est interrompu**. Cliquez sur **Enregistrer** pour activer
l’email.

Suite à cette action, saisissez l’URL du **Point de terminaison de la
notification de suppression du compte de la marketplace** fournie par Konvergo ERP. Ce
point de terminaison HTTPs se trouve dans Konvergo ERP en allant à l’application
Ventes ‣ Configuration ‣ Paramètres, dans le champ **Notifications de
suppression/clôture de compte eBay Marketplace**.

Le fait de cliquer sur le bouton **Générer le jeton** dans Konvergo ERP en dessous de
ce champ crée un jeton de vérification pour l’environnement de production
d’eBay. Dans Konvergo ERP, **copiez** le jeton nouvellement créé et allez à eBay pour
compléter le champ **Jeton de vérification**. Cliquez sur **Enregistrer** pour
activer la **Méthode de livraison des notifications d’événement**.

![Configurer les paramètres de notification/suppression de compte dans
eBay.](../../../../_images/account-closure.png)

Après avoir rempli les champs ci-dessus, cliquez sur **Envoyer une
notification de test** pour tester les nouvelles notifications. Procédez à
l’étape suivante lorsque la coche verte apparaît. Revenez sur les paramètres
ci-dessus si la notification test ne répond pas aux attentes.

Après avoir configuré les paramètres de notification, retournez à la page Clés
de l’application pour générer les ensembles de clés de production.

#### Créer l’ensemble de clés

Une configuration réussie des notifications permet de créer des Jeux de clés
de production qui sont nécessaires pour le reste de la configuration d’Konvergo ERP.
Retournez à la page Clés de l’application pour générer un jeu de clés de
production.

L’administrateur est invité à Confirmer le contact prinipal. Saisissez ou
confirmez le propriétaire du compte (la personne légalement responsable de
l’accord de licence API d’eBay). Remplissez les champs **Prénom** , **Nom de
famille** , **Email** , **Téléphone**. Sélectionnez ensuite l’option
**Particulier** ou **Entreprise**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’adresse email ou le numéro de téléphone fournis ne doivent <b>pas</b> nécessairement correspondre à ceux du compte. eBay utilise ces informations pour contacter l’entreprise ou le particulier en cas de problèmes avec les jetons d’utilisateurs. Vous pouvez ajouter des contacts supplémentaires à partir de la page <b>Profil &amp; Contacts</b> d’eBay.</p>
</div>

Cliquez sur **Continuer à créer des clés** pour confirmer le contact
principal. Les **Clés de l’application** s’affichent dans un nouvel écran et
un email est envoyé au compte de développeur. Les champs **ID App (ID
Client)** , **ID Dev** , et **ID Cert (Secret client)** se remplissent
automatiquement.

![Les clés de l'application sont renseignées après la création de
l'application dans eBay.](../../../../_images/application-keys.png)

Copiez ces valeurs, car elles sont saisies dans Konvergo ERP plus tard dans le
processus.

### Créer le jeton d’utilisation d’eBay

Créez à présent un _jeton d’utilisateur_ dans eBay en allant à la section
`Bonjour [nom d'utilisateur]` en haut à droite de l’écran, puis à **Jetons
d’accès utilisateur**.

![Générer des jetons d'utilisateur dans la console développeur
d'eBay.](../../../../_images/user-tokens.png)

Sélectionnez le bon **Environnement** : **Sandbox** pour les tests ou
**Production** pour la base de données live. Gardez la même sélection pour
tous les paramètres d’environnement dans eBay et dans Konvergo ERP.

Sélectionnez ensuite le bouton radio libellé **Auth’n’Auth**.

Choisissez **Connectez-vous à Production** ou **Connectez-vous à Sandbox**
pour obtenir un jeton d’utilisateur dans l’environnement choisi. Le bouton
change en fonction de la sélection faite : **Sandbox** ou **Production**.

Cette opération fait apparaître une fenêtre contextuelle permettant de
**Confirmer votre adresse légale**. Complétez les champs requis, tels que
**Prénom** , **Nom de famille** , **Email principal** , **Adresse légale** ,
et **Type de compte**. En ce qui concerne le **Type de compte** , sélectionnez
soit **Particulier** , soit **Entreprise**. Pour compléter la confirmation,
cliquez sur **Connectez-vous à eBay pour obtenir un jeton**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>eBay contactera ce particulier ou cette entreprise si un problème survient avec les clés de l’application. Vous pouvez ajouter d’autres contacts à la page Profil &amp; Contacts d’eBay.</p>
</div>

L’administrateur sera redirigé à une page de connexion sandbox ou production.
Ce login est différent du login de la console développeur d’eBay, il s’agit du
compte eBay sur lequel les articles seront vendus. Cet email et/ou login
peuvent différer du compte de développeur d’eBay.

Saisissez l”**Email** ou le **Nom d’utilisateur** pour le compte eBay et
connectez-vous au compte eBay.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si un utilisateur additionnel est nécessaire pour la simulation sandbox, vous devez créer un utilisateur test. Consultez le <a href="https://developer.ebay.com/sandbox/register">formulaire d’inscription à Sandbox d’eBay</a>. Vous trouverez des instructions détaillées sur les pages d’assistance d’eBay : <a href="https://developer.ebay.com/api-docs/static/gs_create-a-test-sandbox-user">Create a test Sandbox user</a>.</p>
</div>

### Accorder l’accès à l’application

Après s’être connecté à l’environnement de production ou sandbox, eBay propose
à l’administrateur d’autoriser l’accès aux données eBay de l’utilisateur.

Le fait de cliquer sur **Accepter** permet à eBay d’associer le compte eBay à
l” _interface de programmation d’application_ (API). Ce consentement peut être
modifié à tout moment en allant aux préférences du compte eBay.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div>0

Un **Jeton d’utilisateur** s’affiche à l’écran. Veillez à copier ce jeton, car
il sera utilisé dans les étapes suivantes avec le **Jeu de clés de
l’appliation**.

![Le jeton d'utilisateur généré et le lien de l'explorateur de l'API sur la
console développeur d'eBay.](../../../../_images/user-token.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div>1

### Explorateur de l’API

À présent que le **Jeu des clés de l’application** et un **Jeton
d’utilisateur** ont été créés, un test peut être exécuté via l”[Explorateur de
l’API](https://developer.ebay.com/DevZone/build-test/test-tool/default.aspx)
afin de s’assurer que l”API est correctement configuré. Ce test effectuera une
simple recherche à l’aide de l”API.

Pour lancer le test API, cliquez sur **Obtenir le jeton d’application OAuth**.
La clé sera alors remplie dans le champ **Jeton**.

Une fonction de recherche de base s’exécutera. Cliquez sur **Exécuter** pour
finaliser le test. Un test réussi répondra avec une **Réponse à l’appel** de
`200 OK` et l”**Heure** correspondante.

## Saisir les identifiants dans Konvergo ERP

Le **Jeton d’utilisateur** et le **Jeu de clés d’application** précédemment
copiés peuvent désormais être saisis dans la base de données d’Konvergo ERP.

Retournez aux paramètres d’eBay dans Konvergo ERP (application Ventes ‣ Configuration
‣ Paramètres ‣ eBay) et collez les identifiants suivants d’eBay dans les
champs correspondants dans Konvergo ERP.

Plateforme | Clé/ID Dev | Jeton | Clé/ID App | Clé/ID Cert  
---|---|---|---|---  
eBay | ID Dev | Jeton d’utilisateur | ID App (ID client) | ID Cert (Secret client)  
Konvergo ERP | Clé développeur | Jeton Production/Sandbox | Clé App Production/Sandbox | Clé Cert Production/Sandbox  
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div>2

Confirmez que la configuration est correcte en enregistrant les identifiants
dans Konvergo ERP. Une fois que la configuration initiale est terminée, un nouvel
onglet de menu intitulé `eBay` apparaît dans les produits avec l’option de
**Vendre sur eBay**. Consultez la documentation gérer sur la façon de lister
les produits.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez accéder à l’environnement sandbow d’eBay en allant au <a href="https://sandbox.ebay.com/">portail sandbox d’eBay</a> via <code>https://sandbox.ebay.com/</code>. Vous pouvez accéder à l’environnement de production d’eBay en allant au <a href="https://www.ebay.com/">portail eBay.com</a> ou <code>https://www.ebay.com/</code>.</p>
</div>5

  *[API]: Interface de programmation d'application

