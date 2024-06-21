# Configurer des règles de réassort

Pour certains produits, il est nécessaire de s’assurer qu’une quantité
minimale est disponible à tout moment. En ajoutant une règle de réassort à un
produit, il est possible d’automatiser le processus de réassort de manière à
ce qu’un bon de commande soit automatiquement créé lorsque la quantité tombe
en dessous d’un certain seuil.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le module <em>Inventaire</em> doit être installé pour utiliser les règles de réassort.</p>
</div>

## Configurer des produits à réapprovisionner

Les produits doivent être configurés d’une manière spécifique pour qu’une
règle de réassort puisse leur être ajoutée.

À partir des modules Inventaire, Fabrication, Achats ou Ventes, allez aux
Produits ‣ Produits et ensuite cliquez sur **Créer** pour créer un nouveau
produit. Vous pouvez également trouver un produit qui existe déjà dans la base
de données et cliquer sur sa fiche produit.

Ensuite, sur la fiche du produit, activez le réassort en cochant l’option
**Peut être acheté** sous le champ **Nom du produit**. Enfin, définissez le
**Type de produit** sur `Produit stockable` dans l’onglet **Informations
générales**.

![Configurez un produit à réapprovisionner dans
Konvergo ERP.](../../../../_images/product-configured-for-reordering.png)

## Ajouter une règle de réassort à un produit

Après avoir correctement configuré un produit, il est possible d’y ajouter une
règle de réassort en cliquant sur l’onglet **Règles de réassort** qui est
désormais visible en haut de la fiche produit et en cliquant ensuite sur
**Créer** dans le tableau de bord des **Règles de réassort**.

![Accédez aux règles de réassort pour un produit à partir de la fiche produit
dans Konvergo ERP.](../../../../_images/reordering-rules-tab.png)

Une fois créée, la règle de réassort peut être configurée pour générer
automatiquement des bons de commande en définissant les champs suivants :

  * **Emplacement** précise où les quantités commandées doivent être stockées une fois qu’elles ont été reçues et entrées dans le stock.

  * **Quantité min** définit le seuil inférieur de la règle de réassort, tandis que **Quantité max** définit le seuil supérieur. Si le stock disponible est inférieur à la quantité minimale, un nouveau bon de commande sera créé pour le réapprovisionner jusqu’à la quantité minimale.

> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si la <b>Quantité min</b> est fixée à <code>5</code> et la <b>Quantité max</b> est fixée à <code>25</code> et le stock disponible tombe à 4, un bon de commande sera créé pour 21 unités du produit.</p>
</div>

  * Il est possible de configurer la **Quantité multiple** de manière à ce que les produits ne soient commandés que par lots d’une certaine quantité. En fonction du chiffre saisi, cela peut entraîner la création d’un bon de commande qui ferait passer le stock disponible à un niveau supérieur à celui précisé dans le champ **Quantité max**.

> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si la <b>Quantité max</b> est fixée à <code>100</code>, mais la <b>Quantité multiple</b> est configurée pour commander le produit en lots de <code>200</code>, un bon de commande sera créé pour 200 unités du produit.</p>
</div>

  * L”**UdM** précise l’unité de mesure dans laquelle la quantité sera commandée. Pour les produits discrets, elle doit est réglée sur `Unités`. Cependant, elle peut également être définie sur des unités de mesure telle que `Volume` ou `Poids` pour les produits non discrets tels que l’eau ou les briques.

![Configurez la règle de réassort dans Konvergo ERP.](../../../../_images/reordering-
rule-configuration1.png)

## Déclencher manuellement des règles de réassort avec le planificateur

Les règles de réassort seront déclenchées automatiquement par le
planificateur, qui s’exécute une fois par jour par défaut. Pour manuellement
déclencher des règles de réassort, allez à Inventaire ‣ Opérations ‣ Lancer le
planificateur. Sur la fenêtre contextuelle, confirmez l’action manuelle en
cliquant sur **Lancer le planificateur**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les règles de réassort déclenchées manuellement déclencheront également d’autres actions planifiées.</p>
</div>

## Gérer les règles de réassort

Pour gérer les règles de réassort pour un seul produit, allez à la fiche de ce
produit et sélectionnez l’onglet **Règles de réassort** en haut du formulaire.

Pour gérer toutes les règles de réassort pour chaque produit, allez à
Inventaire ‣ Configuration ‣ Règles de réassort. Dans ce tableau de bord, vous
pouvez exécuter des actions de masse typiques, telles que l’exportation de
données ou l’archivage de règles qui ne sont plus nécessaires. En outre, les
**Filtres** , **Regrouper par** ou le menu à trois points sur le formulaire
sont disponibles pour rechercher et/ou organiser les règles de réassort comme
vous le souhaitez.

