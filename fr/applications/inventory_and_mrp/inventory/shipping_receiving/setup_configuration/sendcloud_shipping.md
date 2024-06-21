# Sendcloud configuration

Sendcloud est un agrégateur de services d’expédition qui facilite
l’intégration des transporteurs européens avec Konvergo ERP. Après l’intégration des
transporteurs, les utilisateurs peuvent les sélectionner sur les opérations
d’inventaire dans leur base de données Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/360059470491-Konvergo ERP-integration">Documentation sur l’intégration de Sendcloud documentation</a></p>
</div>

## Configuration dans Sendcloud

### Créer un compte et activer les transporteurs

Pour démarrer, allez à la [plateforme Sendcloud](https://www.sendcloud.com)
pour configurer le compte et générer les identifiants du connecteur.
Connectez-vous avec le compte Sendcloud ou créez-en un nouveau si nécessaire.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour créer un nouveau compte, Sendcloud demandera un numéro de <abbr title="taxe sur la valeur ajoutée">TVA</abbr> ou un numéro <abbr title="Economic Operators' Registration and Identification">EORI</abbr>. Après avoir configuré le compte, activez (ou désactivez) les transporteurs qui seront utilisés dans la base de données Konvergo ERP.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP integration of Sendcloud works on free Sendcloud plans <em>only</em> if a bank account is linked,
since Sendcloud won’t ship for free. To use shipping rules, or individual custom carrier
contacts, a paid plan of Sendcloud is <b>required</b>.</p>
</div>

### Configuration de l’entrepôt

Une fois connecté au compte Sendcloud, allez aux Paramètres ‣ Expédition ‣
Adresses et complétez le champ **Adresse de l’entrepôt**.

![Ajouter les adresses dans les paramètres de
Sendcloud.](../../../../../_images/settings-shipping.png)

Pour permettre à Sendcloud de traiter également les retours, une **adresse de
retour** est nécessaire. Sous la **section divers** , il y a un champ **Nom
d’adresse (optionnel)**. Vous devez saisir le nom de l’entrepôt Konvergo ERP ici et
les caractères doivent être identiques.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><b>Configuration SendCloud</b></div>
<div class="line"><b>Divers</b></div>
<div class="line"><b>Nom d’adresse (optionnel)</b> : <code>Warehouse #1</code></div>
<div class="line"><b>Marque</b> : <code>Par défaut</code></div>
</div>
<div class="line-block">
<div class="line"><b>Configuration de l’entrepôt Konvergo ERP</b></div>
<div class="line"><b>Entrepôt</b> : <code>Warehouse #1</code></div>
<div class="line"><b>Nom court</b> : <code>WH</code></div>
<div class="line"><b>Société</b> : <code>My company (San Francisco)</code></div>
<div class="line"><b>Adresse</b> : <code>My Company (San Francisco)</code></div>
</div>
<p>Notez que le champs <b>Entrepôt</b> doit être identique pour la configuration Konvergo ERP et pour la configuration Sendcloud.</p>
</div>

### Générer des identifiants Sendcloud

Dans le compte Sendcloud, naviguez vers Paramètres ‣ Intégrations dans le menu
de droite. Ensuite, recherchez **Konvergo ERP Native**. Cliquez ensuite sur
**Connecter**.

Après avoir cliqué sur **Connecter** , la page redirige vers la page des
paramètres **Sendcloud API** , où les **clés publiques et secrètes** sont
générées. L’étape suivante consiste à nommer l”**intégration**. La règle
d’affectation des noms est la suivante : `Konvergo ERP CompanyName`, avec le nom de
l’entreprise de l’utilisateur remplaçant `CompanyName` (par ex. `Konvergo ERP
StealthyWood`).

Ensuite, cochez la case à côté de **Points relais** et sélectionnez les
services d’expédition pour cette intégration. Après sauvegarde, les **clés
publiques et secrètes** sont générées.

![Configuration de l'intégration Sendcloud et réception des
identifiants.](../../../../../_images/public-secret-keys.png)

## Configuration dans Konvergo ERP

To ensure seamless Sendcloud integration with Konvergo ERP, install and link the
Sendcloud shipping connector to the Sendcloud account. Then, configure Konvergo ERP
fields, so Sendcloud can accurately pull shipping data to generate labels.

### Install Sendcloud shipping module

After the Sendcloud account is set up and configured, it’s time to configure
the Konvergo ERP database. To get started, go to Konvergo ERP’s **Apps** module, search for
the `Sendcloud Shipping` integration, and install it.

![Module d'expédition Sendcloud dans le module Applications
d'Konvergo ERP.](../../../../../_images/sendcloud-mod.png)

### Configuration du connecteur d’expédition Sendcloud

Une fois installé, activez le module **Expédition Sendcloud** dans Inventaire
‣ Configuration ‣ Paramètres. Le paramètre **Connecteur SendCloud** se trouve
sous la section **Connecteurs d’expédition**.

Après avoir activé le **Connecteur SendCloud** , cliquez sur le lien **Modes
d’expédition Sendcloud** sous le connecteur répertorié. Une fois sur la page
des **modes d’expédition** , cliquez sur **Créer**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est également possible d’accéder aux <b>modes d’expédition</b> en allant à Inventaire ‣ Configuration ‣ Livraison ‣ Modes d’expédition.</p>
</div>

Complétez les champs suivants dans le formulaire du **Nouveau mode
d’expédition** :

  * **Mode d’expédition** : écrivez `Sendcloud DPD`.

  * **Fournisseur** : sélectionnez **Sendcloud** dans le menu déroulant.

  * **Produit de livraison** : définissez le produit qui a été configuré pour ce mode d’expédition ou créez un nouveau produit.

  * Dans l’onglet **Configuration SendCloud** , saisissez la **Clé publique Sendcloud**.

  * Dans l’onglet **Configuration SendCloud** , saisissez la **Clé secrète Sendcloud**.

  * **Enregistrez** le formulaire manuellement en cliquant sur l’icône du nuage à côté du fil d’Ariane **Modes d’expédition / Nouveau**.

Après avoir configuré et sauvegardé le formulaire, suivez ces étapes pour
charger les produits d’expédition :

  * Dans l’onglet **Configuration SendCloud** du formulaire **Nouveau mode d’expédition** , cliquez sur le lien **Chargez vos produits d’expédition SendCloud**.

  * Sélectionnez les produits d’expédition que la société souhaite utiliser pour les livraisons et les retours.

  * Cliquez sur **Sélectionner**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Exemple de produits d’expédition Sendcloud configurés dans Konvergo ERP :</p>
<div class="line-block">
<div class="line"><b>LIVRAISON</b></div>
<div class="line"><b>Produit d’expédition</b> : <code>DPD Home 0-31.5kg</code></div>
<div class="line"><b>Transporteur</b> : <code>DPD</code></div>
<div class="line"><b>Poids minimum</b> : <code>0.00</code></div>
<div class="line"><b>Poids maximum</b> : <code>31.50</code></div>
</div>
<p><b>Pays</b> : <code>Autriche</code> <code>Belgique</code> <code>Bosnie-Herzégovine</code> <code>Bulgarie</code> <code>Croatie</code> <code>République tchèque</code> <code>Danemark</code> <code>Estonie</code> <code>Finlande</code> <code>France</code> <code>Allemagne</code> <code>Grèce</code> <code>Hongrie</code> <code>Islande</code> <code>Irlande</code> <code>Italie</code> <code>Lettonie</code> <code>Liechtenstein</code> <code>Lituanie</code> <code>Luxembourg</code> <code>Monaco</code> <code>Pays-Bas</code> <code>Norvège</code> <code>Pologne</code> <code>Portugal</code> <code>Roumanie</code> <code>Serbie</code> <code>Slovaquie</code> <code>Slovénie</code> <code>Espagne</code> <code>Suède</code> <code>Suisse</code></p>
<div class="line-block">
<div class="line"><b>RETOUR</b></div>
<div class="line"><b>Produit d’expédition de retour</b> : <code>DPD Return 0-20kg</code></div>
<div class="line"><b>Transporteur de retour</b> : <code>DPD</code></div>
<div class="line"><b>Poids minimum du retour</b> : <code>0.00</code></div>
<div class="line"><b>Poids maximum du retour</b> : <code>20.00</code></div>
<div class="line"><b>Pays de retour</b> : <code>Belgique</code> <code>Pays-Bas</code></div>
</div>
</div> ![Exemple des produits d'expédition configurés dans
Konvergo ERP.](../../../../../_images/sendcloud-example.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Sendcloud ne fournit pas de clés d’essai lorsqu’une entreprise teste l’envoi d’un colis dans Konvergo ERP. Ceci signifie que si un colis est créé, le compte Sendcloud sera facturé, à moins que le colis associé ne soit annulé dans les 24 heures suivant sa création.</p>
<p>Konvergo ERP has a built-in layer of protection against unwanted charges when using test environments.
Within a test environment, if a shipping method is used to create labels, then those labels are
immediately canceled after the creation — this occurs automatically. The test and production
environment settings can be toggled back and forth from their respective smart buttons.</p>
</div>

### Shipping information

To use Sendcloud to generate shipping labels, the following information
**must** be filled out accurately and completely in Konvergo ERP:

  1. **Customer information** : when creating a quotation, ensure the selected **Customer** has a valid phone number, email address, and shipping address.

To verify, select the **Customer** field to open their contact page. Here, add
their shipping address in the **Contact** field, along with their **Mobile**
number and **Email** address.

  2. **Product weight** : ensure all products in an order have a specified **Weight** in the **Inventory** tab of their product form. Refer to the [Product weight section](third_party_shipper#inventory-shipping-receiving-configure-weight) of this article for detailed instructions.

  3. **Warehouse address** : ensure the warehouse name and address in Konvergo ERP match the previously defined warehouse in the Sendcloud setup. For details on warehouse configuration in Konvergo ERP, refer to the [warehouse configuration section](third_party_shipper#inventory-shipping-receiving-configure-source-address) of the third-party shipping documentation.

## Generate labels with Sendcloud

Lors de la création d’un devis dans Konvergo ERP, ajoutez l’expédition et un **produit
d’expédition Sendcloud**. Ensuite, **validez** la livraison. Les documents
d’étiquettes d’expédition sont générés automatiquement dans le chatter, qui
comprennent les éléments suivants :

  1. **Étiquette(s) d’expédition** selon le nombre de colis.

  2. **Étiquette(s) de retour** si le connecteur Sendcloud est configuré pour les retours.

  3. **Document(s) de douane** si le pays de destination les exige.

De plus, le numéro de suivi est maintenant disponible.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Lorsque les étiquettes de retour sont créées, Sendcloud débitera automatiquement le compte Sendcloud configuré.</p>
</div>

## FAQ

### L’envoi est trop lourd

Si l’envoi est trop lourd pour le service Sendcloud configuré, le poids est
divisé pour simuler plusieurs colis. Les produits devront être mis en
différents **colis** pour **valider** le transfert et générer les étiquettes.

Il est possible de configurer des **règles** dans Sendcloud pour utiliser
d’autres modes d’expédition quand le poids est trop lourd. Cependant, notez
que ces règles ne s’appliquent pas au calcul du prix d’expédition sur le
calcul du bon de commande.

### Personal carrier contract

Use custom prices from a direct carrier contract, via CSV upload, by first
logging into Sendcloud, navigating to Settings ‣ Carriers ‣ My contracts, and
then selecting the intended contract.

![Navigate to the contracts section in
Sendcloud.](../../../../../_images/contracts.png)

Under the **Contract prices** section, click **Download CSV** and fill out the
contract prices in the **price** column of the CSV file template.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Ensure the CSV file includes the correct prices to avoid any inaccuracies.</p>
</div> ![Show sample contract CSV from Sendcloud, highlighting
the price column.](../../../../../_images/price-csv.png)

**Upload** the completed CSV file to Sendcloud, then click **Save these
prices**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/5163547066004">Sendcloud: How to upload contract prices with carriers</a></p>
</div>

### Calcul du poids volumétrique

De nombreux transporteurs ont plusieurs mesures pour le poids. Il y a le poids
réel des produits contenus dans le colis et il y a le _poids volumétrique_ (Le
poids volumétrique est la place que le colis prend en transit. En d’autres
termes, c’est la taille physique d’un colis).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour créer un nouveau compte, Sendcloud demandera un numéro de <abbr title="taxe sur la valeur ajoutée">TVA</abbr> ou un numéro <abbr title="Economic Operators' Registration and Identification">EORI</abbr>. Après avoir configuré le compte, activez (ou désactivez) les transporteurs qui seront utilisés dans la base de données Konvergo ERP.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour créer un nouveau compte, Sendcloud demandera un numéro de <abbr title="taxe sur la valeur ajoutée">TVA</abbr> ou un numéro <abbr title="Economic Operators' Registration and Identification">EORI</abbr>. Après avoir configuré le compte, activez (ou désactivez) les transporteurs qui seront utilisés dans la base de données Konvergo ERP.</p>
</div>1

### Impossible de calculer les frais d’expédition

First, verify that the product being shipped has a weight that is supported by
the selected shipping method. If this is set, then verify that the destination
country (from the customer address) is supported by the carrier. The country
of origin (warehouse address) should also be supported by the carrier.

