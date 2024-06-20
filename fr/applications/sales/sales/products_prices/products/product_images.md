# Images de produits avec Google Images

Il est utile d’avoir des images de produits appropriées dans Odoo pour un
certain nombre de raisons. Toutefois, si un grand nombre de produits a besoin
d’images, cette tâche devient rapidement fastidieuse.

Heureusement, en configurant l’APU _Google Custom Search_ dans une base de
données Odoo, la recherche d’images de produits (sur la base de leur code-
barres) est extrêmement efficace.

## Configuration

Afin d’utiliser _Google Custom Search_ dans une base de données Odoo, la base
de données et l’API Google doivent être correctement configurées.

Note

Les comptes Google gratuits permettent aux utilisateurs de sélectionner
jusqu’à 100 images gratuites par jour. Si vous avez besoin de plus d’images,
procédez à une mise à jour de la facturation.

### Tableau de bord de l’API Google

  1. Allez à la page [API & Services de la plateforme de Google Cloud](https://console.developers.google.com/) afin de générer les identifiants de l’API Google Custom Search. Ensuite, connectez-vous avec un compte Google. Acceptez alors leurs Conditions d’utilisation en cochant la case et en cliquant sur Accepter et continuer.

  2. De là, sélectionnez (ou créez) un projet API pour enregistrer les identifiants. Commencez par lui donner un Nom de projet mémorable, sélectionnez un Emplacement (s’il y en a), puis cliquez sur Créer.

  3. Lorsque vous avez sélectionné l’option Identifiants dans la barre latérale de gauche, cliquez sur Créer les identifiants et sélectionnez la Clé API dans le menu déroulant.

![Page API & Services de la plateforme Google
Cloud.](../../../../../_images/credentials-api-key.png)

  4. Cette opération fait apparaître une fenêtre contextuelle Clé API créée, contenant une Clé API personnalisée. Copiez et enregistrez Votre clé API dans la fenêtre contextuelle – elle sera utilisée plus tard. Une fois la clé copiée (et enregistrée pour plus tard), cliquez sur Fermer pour fermer la fenêtre contextuelle.

![La fenêtre contextuelle de création de la clé API qui
s'affiche.](../../../../../_images/api-key-pop-up.png)

  5. Sur cette page, recherchez `API Custom Search` et sélectionnez-la.

![Barre de recherche contenant "API Custom Search" sur la plateforme Google
Cloud.](../../../../../_images/custom-search-api-search-bar.png)

  6. Sur la page API de la recherche personnalisée, activez l’API en cliquant sur Activer.

![Page "API de la recherche personnalisée" avec le bouton Activer mis en
évidence sur la plateforme de Google Cloud.](../../../../../_images/gcp-
custom-search-api-page.png)

### Tableau de bord de Google Programmable Search

  1. Allez ensuite à [Google Programmable Search Engine](https://programmablesearchengine.google.com/), et cliquez sur le bouton Premiers pas. Connectez-vous avec un compte Google si vous n’êtes pas encore connecté.

![Page Google Programmable Search Engine avec les boutons Premiers
pas.](../../../../../_images/google-pse-get-started.png)

  2. Sur le formulaire Créer un nouveau moteur de recherche, complétez le nom du moteur de recherche, ainsi que ce qu’il doit chercher, et veillez à activer la Recherche d’images et SafeSearch.

![Le formulaire Créer un nouveau moteur de recherche s'affiche avec les
configurations du moteur de recherche.](../../../../../_images/create-new-
search.png)

  3. Validez le formulaire en cliquant sur Créer.

  4. Cette opération fait apparaître une nouvelle page intitulée : Votre nouveau moteur de recherche a été créé.

![La page Votre nouveau moteur de recherche a été créé qui s'affiche avec la
copie du code.](../../../../../_images/new-search-engine-has-been-created.png)

  5. À partir de cette page, cliquez sur Personnaliser pour ouvrir la page Vue d’ensemble ‣ Basique. Copiez ensuite l’ID dans le champ ID de moteur de recherche. Cet ID est nécessaire pour la configuration d’Odoo.

![Page de la vue d'ensemble de base avec le champ ID du moteur de
recherche.](../../../../../_images/basic-overview-search-engine-id.png)

### Odoo

  1. In the Odoo database, go to the Settings app and scroll to the Integrations section. From here, check the box beside Google Images. Then, click Save.

![The Google Images setting in the Odoo Settings app
page.](../../../../../_images/google-images-setting.png)

  2. Next, return to the Settings app, and scroll to the Integrations section. Then, enter the API Key and Search Engine ID in the fields beneath the Google Images feature.

  3. Cliquez sur Enregistrer.

## Product images in Odoo with Google Custom Search API

Adding images to products in Odoo can be done on any product or product
variant. This process can be completed in any Odoo application that provides
access to product pages (e.g. _Sales_ app, _Inventory_ app, etc.).

Below is a step-by-step guide detailing how to utilize the _Google Custom
Search API_ to assign images to products in Odoo using the Odoo _Sales_
application:

  1. Navigate to the Products page in the _Sales_ app (Sales app ‣ Products ‣ Products). Or, navigate to the Product Variants page in the _Sales_ app (Sales app ‣ Products ‣ Product Variants).

  2. Select the desired product that needs an image.

Note

Only products (or product variants) that have a barcode, but **not** an image,
are processed.

If a product with one or more variants is selected, each variant that matches
the aforementioned criteria is processed.

  3. Click the Action ⚙️ (gear) icon on the product page, and select Get Pictures from Google Images from the menu that pops up.

![The Get Pictures from Google Images option from the Action drop-down menu in
Odoo.](../../../../../_images/get-pictures-from-google-action.png)

  4. On the pop-up window that appears, click Get Pictures.

![The pop-up that appears in which the user should click Get Picture in Odoo
Sales.](../../../../../_images/click-get-picture-from-pop-up.png)

  5. Once clicked, the image(s) will appear incrementally.

Note

Only the first 10 images are fetched immediately. If you selected more than
10, the rest are fetched as a background job.

The background job processes about 100 images in a minute. If the quota
authorized by Google (either with a free or a paid plan) is reached, the
background job puts itself on hold for 24 hours. Then, it will continue where
it stopped the day before.

Pour plus d'infos

[Créer, modifier ou fermer un compte de facturation Cloud en libre-
service](https://cloud.google.com/billing/docs/how-to/manage-billing-account)

