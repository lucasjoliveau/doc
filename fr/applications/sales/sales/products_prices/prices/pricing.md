# Listes de prix, remises et formules

Odoo _Ventes_ dispose d’une fonctionnalité utile de liste de prix qui peut
être adaptée à n’importe quelle stratégie de tarification.

Une _liste de prix_ est une liste de prix (ou de règles de prix) qu’Odoo
utilise pour déterminer le bon prix pour un client. Ces listes de prix peuvent
être définies avec des critères spécifiques (tels que des périodes de temps,
une quantité minimale vendue, et plus encore) afin d’appliquer certains prix
ou certaines remises.

Les listes de prix suggèrent certains prix, mais elles peuvent toujours être
remplacées sur la commande.

## Options de stratégie de tarification

Pour choisir une stratégie de tarification, allez d’abord à l’application
Ventes ‣ Configuration ‣ Paramètres. Dans la section Tarif, cochez la cause à
côté de la fonctionnalité Listes de prix.

Deux nouvelles options apparaissent alors : Plusieurs prix par produit et
Règles de prix avancées (remises, formules). Un lien intitulé Listes de prix
apparaît également et vous redirige vers une page séparée des listes de prix,
où vous pouvez créer et/ou modifier des listes de prix.

  * Plusieurs prix par produit : offre la possibilité de définir plusieurs prix différents par produit.

  * Règles de prix avancées (remises, formules) : offre la possibilité de créer des règles de prix détaillées et d’appliquer des remises, des marges et des arrondis.

![Comment se présente la fonctionnalité des listes de prix dans Odoo
Ventes.](../../../../../_images/pricelist-feature-setting.png)

Après avoir coché la case à côté de la fonctionnalité Listes de prix,
sélectionnez l’une des deux options, puis cliquez sur Enregistrer pour
enregistrer tous les changements.

## Listes de prix

Après avoir activé et enregistré la fonctionnalité Listes de prix, la page des
paramètres va s’actualiser. Sélectionnez alors le lien vers les Listes de prix
(en dessous de la fonctionnalité Listes de prix sur la page des Paramètres) ou
allez à l’application Ventes ‣ Produits ‣ Listes de prix.

Les deux options permettent d’ouvrir la page des Listes de prix où vous pouvez
modifier et/ou créer des listes de prix à tout moment.

![Comment se présente la page des listes de prix dans Odoo
Ventes.](../../../../../_images/pricelists-page.png)

Note

La Liste de prix publique est la liste de prix par défaut utilisée par Odoo
_Ventes_ et _eCommerce_.

À partir de la page Listes de prix, sélectionnez la liste de prix que vous
voulez modifier ou cliquez sur Nouveau pour créer une nouvelle liste de prix,
ce qui fait apparaître une liste de prix vierge qui peut être configurée de
plusieurs manières.

![Comment se présente le formulaire détaillé des listes de prix dans Odoo
Ventes.](../../../../../_images/pricelist-detail-form.png)

Lorsque vous créez une nouvelle liste de prix, commencez par donner un nom à
la liste de prix en haut du formulaire, dans le champ vierge. Sélectionnez
ensuite la Devise qui doit être utilisée.

Ensuite, si vous travaillez dans un environnement multi-sociétés, sélectionnez
la société à laquelle cette liste de prix doit s’appliquer dans le champ
Société. Si ce champ est laissé vide, la liste de prix s’applique
automatiquement à toutes les sociétés de la base de données.

### L’onglet des règles de prix

L’onglet Règles de prix varie en fonction du paramètre de Listes de prix
sélectionné : Plusieurs prix par produit ou Règles de prix avancées (remises,
formules).

Toutefois, les onglets Règles basées sur le temps et Configuration sont
toujours les mêmes, indépendamment du paramètre de Listes de prix sélectionné.

#### L’onglet des règles de prix (plusieurs prix par produit)

Lorsque le paramètre Plusieurs prix par produit est activé, l’onglet Règles de
prix offre la possibilité d’ajouter des produits spécifiques, avec un prix
spécifique, à une liste de prix.

Pour ajouter un produit et un prix spécifiques à une liste de prix, cliquez
sur l’onglet Règles de prix, puis cliquez sur Ajouter une ligne dans la
colonne Produits. Ensuite, sélectionnez le produit souhaité pour lequel un
prix spécifique doit être appliqué.

Ensuite, le cas échéant, sélectionnez une variante dans la colonne Variantes
(par ex. une taille spécifique, une couleur spécifique, etc.). Si aucune
variante n’est sélectionnée, ce prix s’appliquera à toutes les variantes du
produit.

Si une quantité minimale du produit doit être achetée pour que le prix
spécifique s’applique, saisissez la quantité dans la colonne Quantité
minimale.

Pour configurer le prix du produit pour cette liste de prix spécifique,
saisissez le montant souhaité dans la colonne Prix. Vous avez ensuite la
possibilité d’ajouter une Date de début et une Date de fin au prix du produit
configuré, si vous le souhaitez.

Pour ajouter une autre ligne de produit, cliquez à nouveau sur Ajouter une
ligne et répétez les mêmes étapes. Vous pouvez ajouter un nombre illimité de
produits dans l’onglet Règles de prix d’une liste de prix.

Pour plus d’informations, consultez la section suivante : Plusieurs prix par
produit.

#### L’onglet des règles de prix (règles de prix avancées)

Lorsque le paramètre Règles de prix avancées (remises, formules) est activé,
l’onglet Règles de prix offre la possibilité de configurer des règles de prix
détaillées sur la base de formules.

Consultez la section Règles de prix avancées (remises, formules) pour savoir
comment ajouter des règles de prix avancées à une liste de prix.

### L’onglet des règles basées sur le temps

Les règles basées sur le temps sont spécifiquement utilisées avec des
[produits d’abonnement](../../../subscriptions/products.html). N’oubliez pas
de consulter la [documentation](../../../subscriptions.html) relative à Odoo
Abonnements.

Dans l’onglet Règles basées sur le temps, vous trouverez les mêmes
fonctionnalités que celles de l’onglet Règles de prix, à la seule différence
qu’une période répétitive peut être appliquée dans la colonne Période.

Après avoir sélectionné un Produit et une éventuelle Variante dans l’onglet
Règles basées sur le temps, sélectionnez le champ vierge dans la colonne
Période pour faire apparaître un menu déroulant de périodes de récurrence
prédéfinies (par ex. `Mensuel`, `Trimestriel`, `Hebdomadaire`, etc.).

Vous pouvez également créer de nouvelles périodes de récurrence à partir de
cette colonne, en saisissant le nouveau nom de la Période et en sélectionnant
Créer pour créer la période, qui pourra être modifiée ultérieurement. Vous
pouvez également sélectionner Créer et modifier… pour faire apparaître un
formulaire contextuel, dans lequel vous pouvez directement configurer la
nouvelle période de récurrence.

![Formulaire contextuel permettant de personnaliser une période dans Odoo
Ventes.](../../../../../_images/time-period-popup.png)

Dans ce formulaire contextuel Créer une période, ajoutez un Nom, une Durée, et
une Unité (par ex. `Jours`, `Semaines`, etc.). Lorsque vous avez terminé,
cliquez sur Enregistrer et Fermer.

Enfin, ajoutez le prix souhaité pour cette règle basée sur le temps dans la
colonne Prix.

Pour plus d'infos

[Abonnements](../../../subscriptions.html)

### Onglet de configuration

Dans l’onglet Configuration, il y a quelques options qui vous permettent de
personnaliser davantage la liste de prix.

![L'onglet des configurations sur le formulaire des listes de prix dans Odoo
Ventes.](../../../../../_images/configuration-tab.png)

À partir de là, dans la section Disponibilité, dans le champ Groupes de pays,
vous pouvez ajouter certains groupes de pays à la liste de prix. Il n’y a pas
de limite au nombre de groupes de pays pouvant être ajoutés dans ce champ.

Note

Si aucun pays n’est défini pour le client, Odoo prend la première liste de
prix sans groupe de pays.

Dans la section Site web, il y a quelques options qui peuvent être
configurées. Dans le champ Site Web, vous pouvez appliquer cette liste de prix
à un site web spécifique si vous travaillez dans un environnement multi-sites.
Si le champ est laissé vide, la liste de prix sera appliquée à tous les sites
web de la base de données.

Cochez la case Sélectionnable pour que cette liste de prix soit une option que
les clients peuvent sélectionner lors de leurs achats. Si la case
Sélectionnable n’est pas cochée, les clients ne peuvent **pas** sélectionner
cette liste de prix lorsqu’ils font leurs achats.

Enfin, il est possible d’ajouter un code promotionnel pour l’eCommerce. Pour
ajouter un code, saisissez le code promo souhaité qui, une fois saisi lors du
passage en caisse, appliquera la liste de prix au client, même si le client
n’entre pas dans les critères spécifiés précédemment.

#### Afficher le pourcentage de remise aux clients

Avec Odoo _Ventes_ , vous avez la possibilité d’afficher le prix public _et_
le pourcentage de remise sur la catalogue de produits.

Pour ce faire, allez à l’application Ventes ‣ Configuration ‣ Paramètres, et
dans la section Tarif, cochez la cause à côté de la fonctionnalité Remises,
puis cliquez sur Enregistrer pour enregistrer tous les changements.

Après avoir activé la fonctionnalité Remises, allez à la page des listes de
prix, en cliquant sur le lien Listes de prix à partir de la page des
Paramètres ou en allant à l’application Ventes ‣ Produits ‣ Listes de prix.

Sur la page des Listes de prix, sélectionnez la liste de prix que vous voulez
modifier. Sur le formulaire, cliquez sur l’onglet Configuration et vous voyez
une section Remises en bas de la page.

![Présentation des options de remise sur l'onglet configuration d'une liste de
prix dans Odoo Ventes.](../../../../../_images/configuration-discount-
options.png)

Les options disponibles dans cette section sont :

  * Remise comprise dans le prix : montre uniquement le prix final aux clients, avec la remise déjà comprise.

  * Afficher le prix public & la remise au client : montre aux clients le prix public _et_ la remise qu’ils ont reçue.

## Application d’une liste de prix à un client

Alors que la liste de prix par défaut appliquée à tout client est la Liste de
prix publique, Odoo offre la possibilité d’appliquer directement une liste de
prix différents aux clients sur leur formulaire de contact.

Pour ce faire, ouvrez la fiche de contact du client souhaité, soit en allant à
l’application Ventes ‣ Commandes ‣ Clients et en sélectionnant le client à
partir de la page principale Clients ou en cliquant sur le nom du client sur
une commande.

![Exemple d'une fiche détaillée d'un client dans Odoo
Ventes.](../../../../../_images/customer-detail-form.png)

Sur la fiche de contact du client, dans l’onglet Ventes & Achats dans la
section Ventes, déterminez quelle liste de prix doit être appliquée à ce
client spécifique dans le menu déroulant du champ Liste de prix.

![Le champ Liste de prix sur une fiche de client dans Odoo
Ventes.](../../../../../_images/customer-form-pricelist-field.png)

## Plusieurs prix par produit

Pour appliquer plusieurs prix par produit individuel, sélectionnez l’option
Plusieurs prix par produit, après avoir activé la fonctionnalité Listes de
prix sur la page des paramètres de _Ventes_ (application Ventes ‣
Configuration ‣ Paramètres), et cliquez sur Enregistrer.

Ensuite, appliquez les listes de prix aux produits spécifiques à l’aide du
formulaire de produit. Allez à l’application Ventes ‣ Produits ‣ Produits et
sélectionnez le produit pour lequel des prix multiples doivent être appliqués.
La sélection d’un produit sur la page Produits fait apparaître la fiche
produit de ce produit sur une page séparée.

Sur la fiche du produit, cliquez sur le bouton intelligent Prix
supplémentaires en haut du formulaire.

![La présentation du bouton intelligent des prix supplémentaires dans Odoo
Ventes.](../../../../../_images/extra-prices-smartbutton.png)

Cette opération fait apparaître une page séparée affichant les Règles de prix
spécifiques à ce produit spécifique. Vous pouvezmodifier ou créer des règles
de prix à tout moment.

![La présentation des règles de prix supplémentaires par page produit dans
Odoo Ventes.](../../../../../_images/price-rules-product-page.png)

Pour créer une nouvelle règle de prix pour un produit à partir de cette page
spécifique Règles de prix, cliquez sur Nouveau pour ajouter une nouvelle ligne
personnalisée dans laquelle le produit souhaité est déjà renseigné dans la
colonne Appliqué à.

Ensuite, sélectionnez la Liste de prix à laquelle cette règle de prix
spécifique au produit doit s’appliquer, via le menu déroulant de la colonne
Liste de prix.

Note

La Liste de prix publique est la liste de prix par défaut utilisée par Odoo
_Ventes_ et _eCommerce_.

Astuce

Pour créer une nouvelle liste de prix à partir de cette page, saisissez un nom
pour la nouvelle liste de prix dans la colonne Liste de prix, puis
sélectionnez Créer dans le menu déroulant. Toutes les listes de prix peuvent
être modifiées à tout moment, en allant à l’application Ventes ‣ Produits ‣
Listes de prix. Vous pouvez également créer des listes de prix sur cette page
spécifique Listes de prix.

Après avoir ajouté la liste de prix souhaitée à la ligne, déterminez une
Quantité min. pour la règle de prix.

Example

Si la Quantité min. est définie sur `2`, le nouveau prix dans la colonne Prix
sera appliqué aux commandes de 2 produits ou plus. Donc, en théorie, si un
seul produit coûte $100, les clients peuvent être incités à acheter plus si le
Prix s’élève à $85 par produit pour une Quantité minimale de `2` produits.

Ensuite, saisissez le montant souhaité dans la colonne Prix. Ensuite, le cas
échéant, indiquez une Date de début et une Date de fin pour la règle de prix
du produit.

En fin de compte, si vous travaillez dans un environnement multi-sociétés,
sélectionnez à quelle société cette règle de pris doit s’appliquer dans le
champ Société. En laissant ce champ vide, la règle de prix s’applique à toutes
les sociétés de la base de données.

Cliquez à côté de la ligne pour activer l’option de sauvegarde automatique
d’Odoo, ce qui signifie que la règle de prix nouvellement créée est désormais
prête à être utilisée.

Ajoutez autant de règles de prix uniques par produit que vous le souhaitez. Il
n’y a aucune limite au nombre de règles de prix qui peuvent être ajoutées par
produit.

Lorsque la ou les règles de prix sont en place pour un produit spécifique, les
clients auxquels s’appliquent ces listes de prix verront automatiquement les
nouveaux prix. Le nombre de règles de prix appliquées à un produit spécifique
est également affiché dans le bouton intelligent Prix supplémentaires, situé
sur chaque fiche de produit.

Note

Lorsqu’une règle de prix/liste de prix est ajouté à un produit par le biais du
bouton intelligent Extra Prices, celle-ci est également répercutée sur la
liste de prix elle-même. De même, lorsqu’une règle de prix pour un produit
spécifique est ajoutée à une liste de prix, elle est également affichée sur la
fiche du produit via le bouton intelligent Prix supplémentaires.

## Règles de prix avancées

La fonctionnalité Règles de prix avancées (remises, formules) permet de
définir des règles de changement de prix basées sur des remises et des
formules. Ces changements peuvent être relatifs au prix de la liste de
produits/catalogue, au coût du produit ou à une autre liste de prix.

Pour utiliser des règles de prix avancées, avec des remises et des formules,
sélectionnez l’option Règles de prix avancées (remises, formules) après avoir
activé la fonctionnalité Listes de prix sur la page des paramètres de
l’application _Ventes_ (application Ventes ‣ Configuration ‣ Paramètres), et
cliquez sur Enregistrer.

Après avoir activé et enregistré la fonctionnalité Listes de prix, la page des
paramètres s’actualise. Sélectionnez alors le lien Listes de prix (en dessous
de la fonctionnalité Listes de prix sur la page des Paramètres) ou allez à
l’application Ventes ‣ Produits ‣ Listes de prix.

Les deux options permettent d’ouvrir la page des Listes de prix où vous pouvez
modifier et/ou créer des listes de prix à tout moment.

Sur la page Listes de prix, sélectionnez une liste de prix que vous voulez
modifier ou créez une nouvelle liste de prix en cliquant sur le bouton
Nouveau.

Sur le formulaire de liste de prix, dans l’onglet Règles de prix, cliquez sur
Ajouter une ligne pour ajouter une règle de prix avancée. Cette opération fait
apparaître une fenêtre contextuelle permettant de Créer des règles de liste de
prix dans laquelle vous pouvez configurer la règle avancée.

![Présentation de la fenêtre contextuelle permettant de créer des règles de
liste de prix dans Odoo Ventes.](../../../../../_images/create-pricelist-
rules-popup.png)

### Calcul du prix

Dans cette fenêtre, choisissez d’abord l’une des trois options de Calcul :

  * Prix fixe : le prix est calculé sur la base d’un prix fixe.

  * Remise : le prix est calculé sur la base d’une remise.

  * Formule : le prix est calculé sur la base d’une formule.

Note

Chaque option de calcul fait apparaître des champs qui lui sont propres.

Si vous avez sélectionné Prix fixe, vous pouvez indiquer le prix souhaité dans
le champ Prix fixe en dessous. Si vous avez sélectionné Remise, vous pouvez
indiquer le pourcentage de remise souhaité dans le champ Remise qui apparaît.

Si vous avez sélectionné Formule, un certain nombre d’options configurables
apparaissent.

![Les différentes options de calcul pour les formules présentes dans Odoo
Ventes.](../../../../../_images/formula-computation-options.png)

Pour configurer l’option de calcul Formule, commencez par sélectionner une
option dans le champ Basé sur : Prix de vente, Coût, ou Autre liste de prix.
Ce choix détermine sur quoi la formule de règle de prix avancée sera basée.

Ensuite, dans le champ Remise, déterminez le montant de la remise à appliquer.
Il convient de noter qu’une majoration peut être appliquée en définissant une
remise négative dans ce champ.

Example

Pour formuler une majoration de 100% (ou deux fois le coût du produit), avec
une marge minimale de $5, définissez le champ Basé sur sur Coût, la Remise sur
`-100`, et les Marges sur `5`. Cette méthode est souvent utilisée dans le
secteur de la vente au détail.

![Comment formuler un coût de majoration avec un marge minimale de 5 dollars
dans Odoo Ventes.](../../../../../_images/formula-markup-cost-example.png)

Ensuite, dans le champ Frais supplémentaires, indiquez un montant fixe à
ajouter (ou déduire) du montant calculé avec la remise. Ensuite, entrez le
chiffre souhaité dans le champ Méthode d’arrondi. La méthode d’arrondi définit
le prix de manière à ce qu’il soit un multiple de la valeur du champ.

Note

L’arrondi est appliqué _après_ la remise et _avant_ le supplément.

Astuce

Pour que les prix se terminent par 9,99, définissez la Méthode d’arrondi à
`10` et les Frais supplémentaires sur `-0.01`.

Enfin, précisez le montant minimum de la marge par rapport au prix de base
dans le champ Marges.

Une fois que toutes les configurations liées à la formule sont terminées, Odoo
fournit un exemple de la forme dans un bloc bleu à droite des configurations.

Example

Pour appliquer une remise de 20%, avec des pris arrondis à 9,99, définissez le
champ Basé sur sur Prix de vente, le champ Remise sur `20`, le champ Frais
supplémentaires sur `-0,01` et le champ Méthode d’arrondi sur `10`.

![Exemple d'une remise de 20% avec des prix arrondis à 9,99 dans Odoo
Ventes.](../../../../../_images/formula-discount-example.png)

### Conditions

La section Conditions se trouve au bas de la fenêtre contextuelle Créer des
règles de liste de prix.

Ici, commencez par sélectionner l’une des options dans le champ Appliquer sur.

  * Tous les produits : la règle de liste de prix avancée s’applique à tous les produits.

  * Catégorie de produits : la règle de liste de prix avancée s’applique à une catégorie de produits spécifique.

  * Produit : la règle de liste de prix avancée s’applique à un produit spécifique.

  * Variante de produit : la règle de liste de prix avancée s’applique à une variante de produit spécifique.

Si vous sélectionnez l’une de ces options, à l’exception de Tous les produits,
de nouveaux champs spécifiques à l’option sélectionnée apparaissent, dans
lesquels vous devez choisir la Catégorie de produits, le Produit ou la
Variante de produit spécifique.

Ensuite, sélectionnez une quantité minimale à appliquer à la règle de liste de
prix avancée dans le champ Quantité minimale. Enfin, sélectionnez une plage de
dates pour la validation des éléments de la liste de prix dans le champ
Validité.

Une fois que toutes les configurations sont terminées, cliquez sur Enregistrer
& Fermer pour enregistrer la règle de liste de prix avancée ou cliquez sur
Enregistrer & Nouveau pour immédiatement créer une autre règle de liste de
prix avancée dans un formulaire vierge.

Note

Si une règle de prix est définie pour un produit particulier et une autre
règle pour sa catégorie de produits, Odoo prend la règle du produit lui-même.

Pour plus d'infos

  * [Devises étrangères](currencies.html)

  * [Gestion des prix](../../../../websites/ecommerce/managing_products/price_management.html)

