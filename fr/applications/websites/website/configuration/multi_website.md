# Sites web multiples

Odoo vous permet de créer plusieurs sites web à partir de la même base de
données. Ceci peut être utile, par exemple, si vous avez plusieurs marques au
sein de votre organisation ou pour créer différents sites web pour différents
produits/services ou différentes audiences. Dans ces cas, le fait d’avoir des
sites web différents permet d’éviter toute confusion et facilite l’adaptation
de vos stratégies de sensibilisation numérique et l’atteinte de votre public
cible.

Each website can be designed and configured independently with its own [domain
name](domain_names.html), theme, pages, menus, [languages](translate.html),
[products](../../ecommerce/managing_products/products.html), assigned sales
team, etc. They can also share content and pages.

Astuce

La duplication de contenu (par ex. pages et contenu partagés entre plusieurs
sites web) peut avoir un impact négatif sur le [Search Engine Optimization
(SEO)](../pages/seo.html).

## Création d’un site web

Pour créer un nouveau site web, suivez les étapes suivantes :

  1. Allez à Site Web ‣ Configuration ‣ Paramètres.

  2. Cliquez sur \+ Nouveau site web.

![Bouton Nouveau site web](../../../../_images/create-website.png)

  3. Specify the Website Name and Website domain. Each website must be published under its own [domain](domain_names.html).

  4. Adaptez le Nom de la société, les Langues et la Langue par défaut si nécessaire.

  5. Cliquez sur le bouton Créer.

Vous pouvez ensuite commencer à construire votre nouveau site web.

Note

Par défaut, toutes les applications associées au site web que vous avez
installées (par ex. **eCommerce** , **Forum** , **Blog** , etc.) et leurs
pages de site web associées sont également disponibles sur le nouveau site
web. Vous pouvez les supprimer en modifiant le menu du site web.

## Passer d’un site web à un autre

Pour passer d’un site web à un autre, cliquez sur le menu à côté du bouton
+Nouveau dans le coin supérieur droit et sélectionnez le site web auquel vous
voulez passer.

![Sélecteur de site web](../../../../_images/switch-websites.png)

Note

Lorsque vous passez d’un site web à un autre, vous êtes redirigé vers l’autre
site web, à la même page (URL) que le site web actuel. Si la page que vous
affichez actuellement n’existe pas sur l’autre site web, vous êtes redirigé
vers une page d’erreur 404. Une fois que vous êtes redirigé, cliquez sur Créer
une page pour créer la page.

![Créer une page à partir d'une page d'erreur
404](../../../../_images/404-create-page.png)

## Configuration spécifique au site web

La plupart des paramètres du site web sont spécifiques au site web, ce que
signifie qu’ils peuvent être activés/désactivés par site web. Pour modifier
les paramètres, allez à Site Web ‣ Configuration ‣ Paramètres. Sélectionnez le
site web souhaité dans le champ Paramètres du site web en haut de la page
Paramètres, dans la bannière **jaune**. Ensuite, modifiez les options pour ce
site web spécifique.

Note

  * Les sites web sont créés avec les paramètres par défaut ; les paramètres ne sont pas copiés d’un site web à un autre.

  * In a [multi-company environment](../../../general/companies.html), each website can be linked to a specific company in your database so that only company-related data (e.g., products, jobs, events, etc.) is displayed on the website. To display company-specific data, set the desired company in the Company field.

### Disponibilité du contenu

Par défaut, les pages, les produits, les événements, etc. créés à partir du
frontend (en utilisant le bouton +Nouveau) sont uniquement disponibles sur le
site web à partir duquel ils ont été créés. Les enregistrements créés à partir
du backend, cependant, sont rendus disponibles sur tous les sites web par
défaut. La disponibilité du contenu peut être modifiée dans le backend, dans
le champ Site Web. Par exemple, pour les produits, allez à eCommerce ‣
Produits, sélectionnez le produit et allez à l’onglet Ventes. Pour les forums,
allez à Configuration ‣ Forums et sélectionnez le forum.

![Champ site web dans le formulaire du forum](../../../../_images/forum-multi-
website.png)

Les enregistrements et les fonctionnalités peuvent être rendus disponibles :

  * Sur tous les sites web : laissez le champ Site Web vide ;

  * Sur un seul site web: définissez le champ Site Web en fonction ;

  * Sur quelques sites web : dans ce cas, vous devez dupliquer l’article et définissez le champ Site Web.

#### Pages du site web

Pour modifier le site web sur lequel une page sera publiée, suivez les étapes
suivantes :

  1. Allez à Site Web ‣ Site ‣ Pages.

  2. Sélectionnez le site web sur lequel la page est actuellement publiée.

![Afficher les pages par site web](../../../../_images/pages-switch-
websites.png)

  3. Cochez la case à côte de la ou des pages que vous voulez modifier.

  4. Cliquez sur le champ Site Web et sélectionnez le site web ou laissez le vide pour publier la page sur tous les sites web.

Note

Chaque site web doit avoir sa propre page d’accueil ; vous ne devriez pas
utiliser la même page d’accueil pour plusieurs sites web.

## Fonctionnalités d’eCommerce

Les fonctionnalités d’eCommerce telles que produits, catégories d’eCommerce,
listes de prix, remises, fournisseurs de paiement, etc., peuvent être limitées
à un site web spécifique.

### Comptes clients

Vous pouvez [permettre à vos clients d’utiliser le même
compte](../../ecommerce/ecommerce_management/customer_accounts.html) sur tous
vos sites web en cochant la case Comptes clients partagés dans les paramètres
de Site Web.

### Tarif

Le prix des produits peut varier en fonction du site web grâce à l’utilisation
des [listes de
prix](../../ecommerce/managing_products/price_management.html#ecommerce-
pricelists). La configuration suivante est requise :

  1. Allez à Site Web ‣ Configuration ‣ Paramètres.

  2. Faites défiler jusqu’à la section Boutique - Produits et définissez Listes de prix sur Plusieurs prix par produit.

  3. Cliquez sur Listes de prix pour définir de nouvelles listes de prix ou modifier des listes de prix existantes.

  4. Sélectionnez la liste de prix ou cliquez sur Nouveau pour en créer une nouvelle, ensuite sélectionnez l’onglet Configuration et définissez le champ Site Web.

## Analyse

### Analytics

Each website has its own [analytics](../reporting/analytics.html#analytics-
plausible). To switch between websites, click the buttons in the upper right
corner.

![Passer d'un site web à un autre dans les rapports
analytiques](../../../../_images/analytics-switch-websites.png)

### Autres données de rapport

D’autres données de rapport telles que les données du tableau de bord
d’eCommerce, les analyses des ventes en ligne et les visiteurs peuvent être
regroupées par site web si nécessaire. Cliquez sur Regrouper par –> Site Web.

