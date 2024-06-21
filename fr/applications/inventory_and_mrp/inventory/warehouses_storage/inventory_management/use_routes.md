# Routes and push/pull rules

Dans la gestion des stocks, la stratégie de la chaîne d’approvisionnement
détermine quand les produits doivent être achetés/fabriqués, livrés aux
centres de distribution et mis à disposition du canal de vente au détail.

Dans Konvergo ERP, une stratégie de la chaîne d’approvisionnement d’un produit peut
être configurée à l’aide des **Routes** , qui comportent des _Règles de flux
tiré et poussé_. Une fois que tout est correctement configuré, l’application
Inventaire peut générer automatiquement des transferts suivant les règles de
flux poussé/tiré configurées.

## À l’intérieur de l’entrepôt

Dans un entrepôt générique, il y a des quais de réception, une zone de
contrôle qualité, des emplacements de stockage, des zones de retrait et
d’emballage et des quais d’expédition. Tous les produits passent par tous ces
emplacements. Lorsque les produits se déplacent à travers les emplacements,
chaque emplacement déclenche la route et les règles définies sur les produits.

![Vue d'un entrepôt générique avec stock et zone de contrôle
qualité.](../../../../../_images/stock-example.png)

Dans cet exemple, les camions des fournisseurs déchargent des palettes de
produits commandés sur les quais de réception. Les opérateurs scannent ensuite
les produits dans la zone de réception. En fonction de la route et des règles
définies sur le produit, certains de ces produits sont envoyés à une zone de
contrôle qualité (par exemple, les produits qui sont des composants utilisés
dans le processus de fabrication), tandis que d’autres sont directement
stockés dans leurs emplacements respectifs.

![Vue d'une règle de flux poussé générique lors de la réception de
produits.](../../../../../_images/push-to-rule-example.png)

Here is an example of a fulfillment route. In the morning, items are picked
for all the orders that need to be prepared during the day. These items are
picked from storage locations and moved to the picking area, close to where
the orders are packed. Then, the orders are packed in their respective boxes,
and conveyor belts bring them to the shipping docks, ready to be delivered to
customers.

![Vue d'une règle de flux tiré générique lors de la préparation de
livraisons.](../../../../../_images/pull-from-rule-example.png)

## Règles de flux tiré

Avec les _Règles de flux tiré_ , une demande pour certains produits déclenche
des approvisionnements, tandis que les _Règles de flux poussé_ sont
déclenchées par l’arrivée de produits à un endroit spécifique.

Les règles de flux tiré sont utilisées pour exécuter une commande client. Konvergo ERP
génère un besoin à l” _emplacement client_ pour chaque produit de la commande.
Comme les règles de flux tiré sont déclenchées par un besoin, Konvergo ERP recherche
une règle de flux tiré définie sur l” _emplacement client_.

Dans ce cas, il trouve une règle de flux tiré de type « bon de livraison » qui
transfère les produits de la _zone d’expédition_ à l” _emplacement client_ et
un transfert entre les deux emplacements est créé.

Ensuite, Konvergo ERP trouve une autre règle de flux tiré qui tente de répondre au
besoin de la _zone d’expédition_ : la règle d“« emballage » qui transfère les
produits de la _zone d’emballage_ vers la _zone d’expédition_. Enfin, d’autres
règles de flux tiré sont déclenchées jusqu’à ce qu’un transfert entre le
_stock_ et la _zone de retrait_ soit créé.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Tous ces transferts de produit sont automatiquement générés par Konvergo ERP en fonction des règles de flux tiré, en partant de la fin (l’emplacement client) et en remontant (jusqu’à l’entrepôt de stock). Pendant qu’il travaille, l’opérateur traite ces transferts dans l’ordre inverse : d’abord le transfert, puis l’emballage et finalement, le bon de livraison.</p>
</div>

## Règles de flux poussé

D’autre part, les _Règles de flux poussé_ sont beaucoup plus faciles à
comprendre. Au lieu de générer des documents en fonction des besoins, ils sont
déclenchés en temps réel lorsque les produits arrivent à un emplacement
spécifique. Les règles de flux poussé disent en gros : « lorsqu’un produit
arrive à un emplacement spécifique, déplacez-le vers un autre emplacement ».

Un exemple d’une règle de flux poussé serait : lorsqu’un produit arrive à la
_zone de réception_ , déplacez-le vers l” _emplacement de stockage_. Comme
différentes règles de flux poussé peuvent être appliquées aux différents
produits, l’utilisateur peut assigner différents emplacements de stockage à
différents produits.

Une autre règle de flux poussé serait : lorsque des produits arrivent à un
emplacement, déplacez-les vers la _zone de contrôle qualité_. Ensuite, une
fois le contrôle qualité effectué, déplacez-les vers leur _emplacement de
stockage_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les règles de flux poussé peuvent uniquement être déclenchées si aucune autre règle de flux tiré n’a déjà généré les transferts de produits.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les ensembles de règles de flux tiré/poussé comme ceux-ci sont appelés des <em>Routes</em>. Le regroupement sur la règle décide si les produits sont regroupés dans le même transfert ou non. Par exemple, pendant l’opération de transfert, toutes les commandes et leurs produits sont regroupés dans un même transfert, tandis que l’opération d’emballage respecte le regroupement par commande client.</p>
</div>

## Utiliser des routes et des règles

Étant donné que les _Routes_ sont un ensemble de _Règles de flux tiré et
poussé_ , Konvergo ERP vous aide à gérer des configurations de route avancées telles
que :

  * Gérer les chaînes de fabrication des produits.

  * Gérer les emplacements par défaut par produit.

  * Définir les routes à l’intérieur de l’entrepôt de stock en fonction des besoins de l’entreprise, telles que le contrôle qualité, les services après-vente ou les retours des fournisseurs.

  * Aider la gestion des locations en générant des retours automatisés pour les produits loués.

Pour configurer une route sur un produit, ouvrez d’abord l’application
**Inventaire** et allez à Configuration ‣ Paramètres. Ensuite, dans la section
**Entrepôt** , activez la fonctionnalité **Routes en plusieurs étapes** et
cliquez sur **Enregistrer**.

![Activer la fonctionnalité des routes en plusieurs étapes dans Konvergo ERP
Inventaire.](../../../../../_images/multi-steps-routes-feature.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La fonctionnalité des <b>Emplacements de stockage</b> est activée automatiquement avec la fonctionnalité <b>Routes en plusieurs étapes</b>.</p>
</div>

Une fois cette première étape complétée, l’utilisateur peut utiliser des
routes préconfigurées dans Konvergo ERP ou ils peuvent créer des routes
personnalisées.

### Routes préconfigurées

Pour accéder aux routes préconfigurées d’Konvergo ERP, allez à Inventaire ‣
Configuration ‣ Entrepôts. Ensuite, ouvrez la fiche de l’entrepôt. Dans
l’onglet **Configuration de l’entrepôt** , l’utilisateur peut visualiser les
routes préconfigurées pour les **Réceptions** et les **Expéditions**.

![A pre-configured warehouse in Konvergo ERP
Inventory.](../../../../../_images/example-preconfigured-warehouse.png)

Certaines routes plus avancées, telles que picking-colisage-expédition, sont
également disponibles. L’utilisateur peut sélectionner la route qui correspond
le mieux aux besoins de son entreprise. Une fois les routes **Réceptions** et
**Expéditions** définies, allez à Inventaire ‣ Configuration ‣ Routes pour
voir les routes spécifiques générées par Konvergo ERP.

![Vue de toutes les routes préconfigurées proposées par
Konvergo ERP.](../../../../../_images/preconfigured-routes.png)

Sur la page des **Routes** , cliquez sur une route pour ouvrir sa fiche. Sur
la fiche, l’utilisateur peut voir à quels endroits la route est
**applicable**. L’utilisateur peut également définir la route pour qu’elle ne
s’applique qu’à une **société** spécifique. C’est utile pour les
environnements multi-sociétés ; par exemple, un utilisateur peut avoir une
société et un entrepôt dans le pays A et une deuxième société et un deuxième
entrepôt dans le pays B.

![Vue d'un exemple de route applicable aux catégories de produit et aux
entrepôts.](../../../../../_images/routes-example.png)

Au bas de la fiche de la route, l’utilisateur peut voir les **Règles**
spécifiques pour la route. Chaque **Règle** a une **Action** , un
**Emplacement d’origine** , et un **Emplacement de destination**.

![Un exemple de règles avec des actions pousser & tirer dans Konvergo ERP
Inventaire.](../../../../../_images/rules-example.png)

### Routes personnalisées

Pour créer une route personnalisée, allez à Inventaire ‣ Configuration ‣
Routes et cliquez sur **Créer**. Ensuite, choisissez les endroits où cette
route peut être sélectionnée. Une route peut s’appliquer à une combinaison
d’endroits.

![Vue d'une route picking-colisage-
expédition.](../../../../../_images/advanced-custom-route.png)

Chaque endroit a un comportement différent, donc il est important de ne cocher
que ceux qui sont utiles et d’adapter chaque route en conséquence. Ensuite,
configurez les **Règles** de la route.

Si la route s’applique à une catégorie de produits, la route doit toujours
être définie manuellement sur la fiche de la catégorie de produits en allant à
Inventaire ‣ Configuration ‣ Catégories de produits. Sélectionnez ensuite la
catégorie de produit et ouvrez la fiche. Cliquez sur **Modifier** et
définissez les **Routes** dans la section **Logistique**.

En appliquant la route à une catégorie de produits, toutes les règles
configurées sur la route s’appliquent à **chaque** produit de la catégorie.
Ceci peut être utile si l’entreprise utilise le dropshipping pour tous les
produits d’une même catégorie.

![Vue d'une route appliquée à la catégorie de produits
"tous".](../../../../../_images/routes-logistic-section.png)

La même logique s’applique aux entrepôts. Si la route peut s’appliquer aux
**Entrepôts** , tous les transferts au sein de l’entrepôt sélectionné qui
satisfont aux conditions des règles de la route, suivront cette route.

![Vue du menu déroulant des entrepôts en cochant la case applicable aux
entrepôts.](../../../../../_images/applicable-on-warehouse.png)

Si la route s’applique aux **lignes de bons de commande** , c’est plus ou
moins l’inverse qui se produit. La route doit être choisie manuellement lors
de la création d’un devis. C’est utile si certains produits passent par des
routes différentes.

Pensez à afficher la colonne de la **Route** sur le devis/bon de commande.
Ensuite, la route peut être sélectionnée sur chaque ligne du devis/bon de
commande.

![Vue du menu permettant d'ajouter de nouvelles lignes aux commandes
clients.](../../../../../_images/add-routes-to-sales-lines.png)

Finalement, certaines routes peuvent s’appliquer aux produits. Celles-ci
fonctionnent plus ou moins de la même façon que les catégories de produits :
une fois sélectionnée, la route doit être définie manuellement sur la fiche
produit.

Pour définir une route sur un produit, allez à Inventaire ‣ Produits ‣
Produits et sélectionnez le produit souhaité. Ensuite, allez à l’onglet
**Inventaire** et sélectionnez les **Routes** dans la section **Opérations**.

![Vue d'une fiche produit, où la route doit être
sélectionnée](../../../../../_images/on-product-route.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les règles doivent être définies sur la route pour que la route fonctionne.</p>
</div>

#### Règles

Les règles sont définies sur la fiche de la route. Tout d’abord, allez à
Inventaire ‣ Configuration ‣ Routes et ouvrez la fiche de la route souhaitée.
Ensuite, cliquez sur **Modifier** et cliquez sur **Ajouter une ligne** dans la
section **Règles**.

![Vue du menu des règles, où il est possible d'ajouter de nouvelles
règles.](../../../../../_images/add-new-rules.png)

Les règles disponibles déclenchent diverses actions. Si Konvergo ERP propose des
règles _Pousser_ et _Tirer_ , d’autres sont également disponibles. Chaque
règle a une **Action** :

  * **Tirer depuis** : cette règle est déclenchée par un besoin du produit à un emplacement précis. Le besoin peut provenir d’une commande client en cours de validation ou d’un ordre de fabrication nécessitant un composant spécifique. Lorsque le besoin apparaît dans l’emplacement de destination, Konvergo ERP génère un transfert pour répondre à ce besoin.

  * **Pousser vers** : cette règle est déclenchée par l’arrivée de certains produits à l’emplacement d’origine défini. Dans le cas où l’utilisateur déplace des produits vers l’emplacement source, Konvergo ERP génère un transfert pour déplacer ces produits à l’emplacement de destination.

  * **Tirer & Pousser** : cette règle permet la génération de transferts dans les deux situations susmentionnées. Ceci signifie que lorsque des produits sont nécessaires à un emplacement spécifique, un transfert est créé depuis l’emplacement précédent pour satisfaire à ce besoin. Ceci crée un besoin dans l’emplacement précédent et un règle est déclenchée pour y répondre. Une fois le deuxième besoin satisfait, les produits sont poussés vers l’emplacement de destination et tous les besoins sont satisfaits.

  * **Acheter** : lorsque des produits sont nécessaires à l’emplacement de destination, une demande de prix est créée pour satisfaire au besoin.

  * **Fabriquer** : lorsque des produits sont nécessaires dans l’emplacement d’origine, un ordre de fabrication est créé pour répondre au besoin.

![Aperçu d'une règle "Tirer depuis" qui crée un transfert entre le stock et la
zone d'emballage.](../../../../../_images/pull-from-rule-stock-to-packing.png)

Le **Type d’opération** doit également être défini sur la règle. Ceci définit
quel type de transfert sera créé à partir de la règle.

Si l”**Action** de la règle est définie sur **Tirer depuis** ou **Tirer &
Pousser**, une **Méthode d’approvisionnement** doit être définie. La **Méthode
d’approvisionnement** définit ce qui se passe à l’emplacement d’origine :

  * **Prendre dans le stock** : les produits sont pris dans le stock disponible de l’emplacement d’origine.

  * **Déclencher une autre règle** : le système tente de trouver une règle de stock pour amener les produits à l’emplacement d’origine. Le stock disponible est ignoré.

  * **Prendre dans le stock, si pas disponible, déclencher une autre règle** : les produits sont pris dans le stock disponible de l’emplacement d’origine. Si aucun stock n’est disponible, le système tente de trouver une règle pour amener les produits à l’emplacement d’origine.

## Example flow

Dans cet exemple, utilisons une route _Picking - Colisage - Expédition_ pour
tenter un flux complet avec une route personnalisée avancée.

Jetons d’abord un coup d’œil aux règles de la route et leurs méthodes
d’approvisionnement. Il y a trois règles, toutes des règles **Tirer depuis**.
Les **Méthodes d’approvisionnement** pour chaque règle sont les suivantes :

  * **Prendre dans le stock** : Lorsque des produits sont nécessaires dans la **WH/Zone de colisage** , des _pickings_ (transferts internes de **WH/Stock** vers **WH/Zone de colisage**) sont créés depuis **WH/Stock** pour répondre au besoin.

  * **Déclencher une autre règle** : Lorsque des produits sont nécessaires en **WH/Sortie** , des _colis_ (transferts internes depuis **WH/Zone de colisage Zone** vers **WH/Sortie**) sont créés depuis **WH/Zone de colisage** pour répondre au besoin.

  * **Déclencher une autre règle** : Lorsque des produits sont nécessaires dans des **Emplacements partenaires/clients** , des _bons de livraison_ sont créés depuis **WH/Sortie** pour répondre au besoin.

![Aperçu de tous les transferts créés par la route picking - colisage -
expédition.](../../../../../_images/transfers-overview.png)

Ceci signifie que lorsqu’un client commande des produits sur lesquels une
route _picking - colisage - expédition_ est définie, un bon de livraison est
créé pour exécuter la commande.

![Vue des opérations créées par une règle de flux tiré depuis un
transfert.](../../../../../_images/operations-on-transfers.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le document d’origine pour plusieurs transferts est la même commande client, le statut n’est pas identique. Le statut sera <b>En attente d’une autre opération</b> si le transfert précédent dans la liste n’est pas encore effectué.</p>
</div> ![Vue des différents statuts du transfert au début du
processus.](../../../../../_images/waiting-status.png)

Pour préparer un bon de livraison, des produits emballés sont nécessaires dans
la zone de sortie, donc un transfert interne est demandé depuis la zone de
colisage.

![Vue des opérations détaillées d'un transfert entre les zones de colisage et
de sortie.](../../../../../_images/detailed-operations-2.png)

Bien évidemment, la zone de colisage a besoin de produits qui sont prêts à
être emballés. Donc, un transfert interne est nécessaire vers le stock pour
que les employés puissent rassembler les produits nécessaires dans l’entrepôt.

![Vue des opérations détaillées d'un transfert entre le stock et la zone de
colisage.](../../../../../_images/detailed-operations-transfer.png)

Comme il est expliqué dans l’introduction de la documentation, la dernière
étape du processus (pour cette route, le bon de livraison) est la première à
être déclenchée et déclenchera ensuite d’autres règles jusqu’à ce que la
première étape du processus soit atteinte (en l’espèce, le transfert interne
depuis le stock vers la zone de colisage). À présent, tout est prêt à être
traité, donc le client peut recevoir les articles commandés.

Dans cet exemple, le produit est livré au client lorsque toutes les règles ont
été déclenchées et les transferts ont été effectués.

![Vue des statuts des transferts lorsque la route est
finalisée.](../../../../../_images/transfers-status.png)

