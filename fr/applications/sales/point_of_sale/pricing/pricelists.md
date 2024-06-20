# Listes de prix

Les listes de prix vous permettent d’ajuster automatiquement les prix des
produits en fonction de divers critères. Par exemple, vous pouvez fixer des
prix spécifiques aux points de vente, créer des périodes de remise
temporaires, récompenser des clients spécifiques ou offrir des remises lorsque
des quantités déterminées sont commandées.

## Configuration

Allez aux [paramètres généraux de l’application
PdV](../configuration.html#configuration-settings) et activez l’option Listes
de prix flexibles dans la section Tarif.

Plusieurs prix par produit est l’option de liste de prix par défaut pour
définir des règles de prix fixes simples par produit. Sélectionnez Règles de
prix avancées (remises, formules) pour appliquer des règles de prix à
plusieurs produits à la fois et pour calculer les prix de manière dynamique en
utilisant des remises en pourcentage ou des formules plus complexes, en plus
de fixer des prix fixes.

![Activez les listes de prix dans les paramètres généraux du point de
vente](../../../../_images/settings1.png)

Note

Le type de liste de prix sélectionné s’applique à toute la base de données, y
compris aux applications
[Ventes](../../sales/products_prices/prices/pricing.html) et
[eCommerce](../../../websites/ecommerce/managing_products/price_management.html#ecommerce-
pricelists).

### Créer des listes de prix

Allez au Point de Vente ‣ Produits ‣ Listes de prix et cliquez sur Nouveau ou
sélectionnez une liste de prix existante. La configuration de la liste de prix
dépend de l”option de liste de prix sélectionnée.

#### Plusieurs prix par produit

Lorsque les listes de prix sont configurées pour utiliser l’option Plusieurs
prix par produit, il est possible d’utiliser plusieurs prix fixes pour
différents produits ou leurs variantes en fonction, si nécessaire, d’une ou
plusieurs conditions. Pour ajouter une nouvelle règle de prix à une liste de
prix :

  1. Cliquez sur Ajouter une ligne, et sélectionnez un **produit** et sa **variante** si nécessaire.

  2. Ajoutez la (les) condition(s) :

     * une quantité de produit à atteindre en utilisant la colonne Quantité min ;

     * une période déterminée pendant laquelle la liste de prix est appliquée en utilisant les colonnes Date de début et Date de fin.

  3. Ajoutez le Prix à appliquer lorsque les conditions sont remplies (le cas échéant).

![Formulaire de configuration d'une liste de prix à prix
multiples](../../../../_images/multiple-prices.png)

#### Règles de prix avancées

Lorsque les listes de prix sont configurées pour utiliser l’option Règles de
prix avancées (remises, formules), il est possible d’utiliser des
remises/majorations en pourcentage et des formules en plus des prix fixes.
Pour ajouter une nouvelle règle de prix à une liste de prix, cliquez sur
Ajouter une ligne. Dans la fenêtre contextuelle :

  1. Sélectionnez un mode de calcul :

     * Prix fixe pour définir un nouveau prix fixe (similaire à l’option Plusieurs prix par produit).

     * Remise pour calculer un pourcentage de remise (par ex. `10,00` %) ou majoration (par ex. `-10,00` %).

     * Formule pour calculer le prix en fonction d’une formule. Il est nécessaire de définir sur quoi le calcul est **basé** (Prix de vente, Coût, ou Autre liste de prix). Vous pouvez ensuite :

       * Appliquer un pourcentage de Remise ou de majoration.

       * Ajouter des Frais supplémentaires (par ex. $ `5.00`) ou soustraire un montant fixe (par ex. $ `-5.00`).

       * Définir une [Méthode d’arrondi](cash_rounding.html) en forçant le prix après la Remise à être un multiple de la valeur définie. Les Frais supplémentaires sont ajoutés par la suite.

Example

Pour que le prix final se termine par `,99`, définissez la Méthode d’arrondi à
`1,00` et les Frais supplémentaires à `-0,01`.

       * Précisez les Marges bénéficiaires minimale (par ex. $ `20,00` ) et maximale (par ex. $ `50,00` ) pour les calculs basés sur le Coût.

  2. Sélectionnez sur quel(s) produit(s) la règle de prix doit **s’appliquer** :

     * Tous les produits

     * une Catégorie de produits

     * un Produit

     * une Variante de produit

  3. Ajoutez des conditions, telles qu’une quantité spécifique à atteindre pour que le prix change en utilisant le champ Quantité min. ou une période spécifique pendant laquelle la liste de prix doit être appliquée en utilisant les champs Validité.

![Formulaire de configuration d'une liste de prix
avancée](../../../../_images/price-rules.png)

### Sélectionner des listes de prix

Allez aux [paramètres spécifiques du PdV](../configuration.html#configuration-
settings) et ajoutez toutes les listes de prix valables dans le champ
Disponible. Ensuite, définissez sa **liste de prix par défaut** dans le champ
Par défaut.

Lorsque vous [ouvrez une session PdV](../../point_of_sale.html#pos-session-
start), cliquez sur le bouton **listes de prix** et sélectionnez la liste de
prix souhaitée dans la liste.

![Bouton pour sélectionner une liste de prix dans le frontend du point de
vente.](../../../../_images/pricelist-button.png)

Note

  * Plusieurs listes de prix doivent être sélectionnées pour que le **bouton de liste de prix** s’affiche.

  * Si une liste de prix est sélectionnée sur une commande du point de vente, alors que ses conditions ne sont **pas** réunies, le prix ne sera **pas** ajusté.

Astuce

Vous pouvez également définir une liste de prix à sélectionner automatiquement
dès qu’un [client spécifique est défini](../../point_of_sale.html#pos-
customers). Pour ce faire, allez à la fiche client et passez à la liste de
prix préférée dans le champ Liste de prix de l’onglet Ventes & Achats.

Pour plus d'infos

  * [Listes de prix, remises et formules](../../sales/products_prices/prices/pricing.html)

  * [Comment utiliser des listes de prix dans un environnement d’e-commerce](../../../websites/ecommerce/managing_products/price_management.html#ecommerce-pricelists)

