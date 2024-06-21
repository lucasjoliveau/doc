# Créer un deuxième entrepôt

Un _entrepôt_ est un bâtiment ou un espace physique où les articles sont
stockés. Dans Konvergo ERP, il est possible de configurer plusieurs entrepôts et de
transférer des articles stockés entre eux.

Par défaut, la plateforme Konvergo ERP a un entrepôt qui est déjà configuré, avec
l’adresse définie comme l’adresse de la société. Pour créer un deuxième
entrepôt, sélectionnez Configuration ‣ Entrepôts, puis cliquez sur **Créer**
et configurez le formulaire comme suit :

  * **Entrepôt** : le nom complet de l’entrepôt

  * **Nom court** : le code abrégé par lequel l’entrepôt est désigné : le nom abrégé de l’entrepôt par défaut dans Konvergo ERP est **WH**

  * **Société** : l’entreprise qui possède l’entrepôt ; il peut s’agir de la société qui possède la base de données Konvergo ERP ou de la société d’un client ou d’un fournisseur

  * **Adresse** : l’adresse où l’entrepôt est situé

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les options suivantes apparaissent uniquement si la case à cocher à côté de <b>Routes en plusieurs étapes</b> est activée dans Configuration ‣ Paramètres dans la section <b>Entrepôt</b>. Pour plus d’informations sur les routes et la manière dont elles fonctionnent dans Konvergo ERP, consultez <a href="use_routes#use-routes"><span class="std std-ref">Utiliser des routes et des règles de flux tirés/poussés</span></a>.</p>
</div>

  * **Réceptions/Expéditions** : sélectionnez les routes que les réceptions et expéditions devraient suivre

  * **Réapprovisionner les sous-traitants** : permet aux sous-traitants d’être réapprovisionnés depuis cet entrepôt

  * **Fabriquer pour réapprovisionner** : permet aux articles d’être fabriqués dans cet entrepôt

  * **Fabriquer** : sélectionnez la route à suivre pour la fabrication de marchandises dans l’entrepôt

  * **Acheter pour réapprovisionner** : cochez la case pour autoriser la livraison de produits achetés à l’entrepôt

  * **Réapprovisionner depuis** : sélectionnez des entrepôts qui peuvent être utilisés pour réapprovisionner l’entrepôt en cours de création

![Un formulaire complété pour la création d'un nouvel
entrepôt.](../../../../../_images/new-warehouse-configuration.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La création d’un deuxième entrepôt active automatiquement le paramètre <em>Emplacements de stockage</em> qui permet de suivre l’emplacement des produits dans un entrepôt. Pour activer ce paramètre, allez à Configuration ‣ Paramètres et cochez la case dans la section <b>Entrepôt</b>.</p>
</div>

Après avoir complété le formulaire, cliquez sur **Enregistrer** et le nouvel
entrepôt sera créé.

## Ajouter un inventaire au nouvel entrepôt

Si un nouvel entrepôt est créé et qu’il contient un inventaire existant,
l’inventaire doit être ajouté à Konvergo ERP pour que le stock répertorié dans la base
de données Konvergo ERP reflète ce qui se trouve dans l’entrepôt physique. Pour
ajouter l’inventaire à un nouvel entrepôt, allez à Inventaire ‣ Opérations ‣
Ajustements d’inventaire et cliquez sur **Créer**. Le formulaire de
l’ajustement d’inventaire peut être complété comme suit :

  * **Référence de l’inventaire** : le nom ou le code par lequel l’ajustement d’inventaire peut être désigné

  * **Emplacements** : le ou les emplacements où l’inventaire est stocké ; incluez le nouvel entrepôt et n’importe quel emplacement dans ce stock sera ajouté

  * **Produits** : incluez tous les produits qui seront ajoutés à l’inventaire ou laissez blanc pour sélectionner n’importe quel produit lors de l’étape suivante

  * **Inclure les produits épuisés** : incluez les produits dont la quantité est nulle ; n’affecte pas les ajustements d’inventaire pour les nouveaux entrepôts puisqu’ils n’ont pas de stock existant

  * **Date comptable** : la date utilisée par les équipes comptables pour la tenue des comptes relatifs à l’inventaire

  * **Société** : la société qui possède l’inventaire ; il peut s’agir de la société de l’utilisateur ou d’un client ou fournisseur

  * **Quantités comptées** : choisissez si les quantités comptées pour les produits ajoutés doivent correspondre par défaut au stock disponible ou à zéro ; n’affecte pas les ajustements d’inventaire pour les nouveaux entrepôts puisqu’ils n’ont pas de stock existant

![Un formulaire complété pour un ajustement
d'inventaire.](../../../../../_images/inventory-adjustment-configuration.png)

Une fois le formulaire correctement configuré, cliquez sur **Démarrer
l’inventaire** pour passer à la page suivante où des produits peuvent être
ajoutés à l’ajustement de l’inventaire. Ajoutez un nouveau produit en cliquant
sur **Créer** et complétez la ligne de produit comme suit :

  * **Produit** : le produit ajouté à l’inventaire

  * **Emplacement** : l’emplacement où le produit est actuellement stocké dans le nouvel entrepôt ; il peut s’agir de tout l’entrepôt ou d’un emplacement dans l’entrepôt

  * **Lot/Numéro de série** : le lot auquel appartient le produit ou le numéro de série utilisé pour l’identifier

  * **En stock** : la quantité totale du produit stocké dans l’emplacement pour lequel l’inventaire est ajusté ; cette valeur doit être égale à zéro pour un nouvel emplacement ou un nouvel entrepôt

  * **Quantité comptée** : la quantité des produits ajoutée à l’inventaire

  * **Différence** : la différence entre les quantités _En stock_ et _Comptées_ ; cette valeur sera automatiquement mise à jour pour refléter la valeur saisie dans la colonne **Quantité comptée**

  * **UdM** : l’unité de mesure utilisée pour compter le produit

![Il y a une ligne pour chaque produit ajouté à
l'inventaire.](../../../../../_images/product-line-configuration.png)

Après avoir ajouté tous les produits déjà stockés dans le nouvel entrepôt,
cliquez sur **Valider l’inventaire** pour finaliser l’ajustement d’inventaire.
Les valeurs dans la colonne **En stock** seront mises à jour pour refléter
celles de la colonne **Quantité comptée** et les produits ajoutés apparaîtront
dans l’inventaire du nouvel entrepôt.

