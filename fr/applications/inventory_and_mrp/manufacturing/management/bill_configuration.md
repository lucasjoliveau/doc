# Bill of materials

A _bill of materials_ (or _BoM_ for short) is a document that defines the
quantity of each component required to make or deliver a finished product. It
can also include various operations and the individual step guidelines needed
to complete a production process.

In Konvergo ERP Manufacturing, multiple BoMs can be linked to each product, so even
product variants can have their own tailored BoMs.

La configuration correcte d’une nomenclature permet d’optimiser le processus
de fabrication et de gagner du temps.

## Configurer une nomenclature

La configuration de nomenclature la plus simple est celle où il n’y a pas
d’opérations ou d’instructions, mais uniquement des composants. Dans ce cas,
la production est uniquement gérée à l’aide d” _ordres de fabrication_.

Pour créer une nomenclature à partir du module **Fabrication** , allez à
Produits ‣ Nomenclatures. Cliquez ensuite sur **Créer**. Précisez alors le
**Produit**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une nomenclature peut également être créée directement à partir de la fiche produit, auquel cas le champ <b>Produit</b> est prérempli.</p>
</div>

Pour une nomenclature standard, définissez le **Type de nomenclature** sur
**Fabriquer ce produit**. Cliquez ensuite sur **Ajouter une ligne** pour
préciser les différents composants qui entrent dans la fabrication du produit
fini et leurs quantités respectives. De nouveaux composants peuvent être créés
rapidement par le biais de la nomenclature ou peuvent être créés au préalable
dans Fabrication ‣ Produits ‣ Produits ‣ Créer. Finalement, cliquez sur
**Enregistrer** pour finaliser la création de la nomenclature.

![La configuration d'une nomenclature.](../../../../_images/bom-form.png)

### Préciser une nomenclature pour une variante de produit

Les nomenclatures peuvent également être assignées à des _variantes de
produits_ spécifiques, avec deux options de configuration possibles.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Afin d’assigner des nomenclatures à des variantes de produits, les attributs de la variante de produit doivent déjà être configurés dans la fiche produit.</p>
</div>

La première méthode consiste à créer une nomenclature par variante en créant
une nouvelle nomenclature et en précisant la **variante de produit** La
seconde méthode consiste à créer une nomenclature principale qui contient tous
les composants et préciser la variante à laquelle chaque composant s’applique
à l’aide de la colonne **Appliquer aux variantes**

![Variantes de produit dans la nomenclature.](../../../../_images/bom-
variants.png)

## Configurer des opérations

Ajoutez une **opération** à une nomenclature pour préciser des instructions de
production et enregistrer le temps passé sur une opération. Pour utiliser
cette fonctionnalité, activez d’abord la fonctionnalité **Ordres de travail**
dans Fabrication ‣ Configuration ‣ Paramètres ‣ Opérations.

Ensuite, lors de la création d’une nouvelle nomenclature, cliquez sur l’onglet
**Opérations** et cliquez sur **Ajouter une ligne** pour ajouter une nouvelle
opération. Sur la fenêtre **Créer Opérations** , nommez l’opération, précisez
le **Poste de travail** et les paramètres de durée. À l’instar des composants,
Konvergo ERP offre la possibilité de préciser une variante de produit dans le champ
**Appliquer aux variantes** pour que l’opération s’applique uniquement à cette
variante. Finalement, cliquez sur **Enregistrer & Fermer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Chaque opération est unique, car elle est toujours exclusivement liée à une nomenclature. Les opérations peuvent être réutilisées lors de la configuration d’une nouvelle nomenclature, grâce à la fonctionnalité <b>Copier les opérations existantes</b>.</p>
</div> ![La fonctionnalité Copier les opérations
existantes.](../../../../_images/copy-existing-operations.png)

## Ajouter des sous-produits à une nomenclature

Un _sous-produit_ est un produit résiduel créé au cours de la production en
plus du produit principal d’une nomenclature. Contrairement au produit
principal, il peut y avoir plus d’un sous-produit sur une nomenclature.

Pour ajouter des sous-produits à une nomenclature, activez d’abord la
fonctionnalité **Sous-produits** dans Fabrication ‣ Configuration ‣ Paramètres
‣ Opérations.

Une fois la fonctionnalité activée, vous pouvez ajouter des sous-produits à
une nomenclature en cliquant sur l’onglet **Opérations** et en cliquant sur
**Ajouter une ligne**. Ensuite, nommez le sous-produit et indiquez la
**Quantité** et l”**Unité de mesure**. Si la nomenclature comporte des
opérations configurées, précisez exactement l’opération à partir de laquelle
le sous-produit est produit dans le champ **Produit dans l’opération**.
Finalement, cliquez sur **Enregistrer**.

  *[BoMs]: Bills of Materials

