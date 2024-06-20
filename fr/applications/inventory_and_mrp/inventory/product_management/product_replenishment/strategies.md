# Sélectionner une stratégie de réassort

Dans Odoo, il existe deux stratégies pour automatiquement réapprovisionner
l’inventaire : les _règles de réassort_ et la route _Fabrication à la commande
(MTO)_. Bien que ces stratégies soient légèrement différentes, elles ont
toutes deux des conséquences similaires : déclencher la création automatique
d’un bon de commande ou d’un ordre de fabrication. Le choix de la stratégie à
utiliser dépend des processus de fabrication et de livraison de l’entreprise.

## Terminologie

### Rapport de réassort et règles de réassort

Le rapport de réassort est une liste de tous les produits dont la quantité
prévue est négative.

Les _règles de réassort_ sont utilisées pour s’assurer qu’il y ait toujours
une quantité minimale d’un produit en stock, afin de fabriquer des produits
et/ou d’exécuter des commandes clients. Lorsque le niveau de stock d’un
produit atteint son minimum, Odoo génère automatiquement un bon de commande
avec la quantité requise pour atteindre le niveau de stock maximum.

Les règles de réassort peuvent être créées et gérées dans le rapport de
réassort ou à partir de la fiche du produit.

### Fabrication à la commande

La _Fabrication à la commande (MTO)_ est une route d’approvisionnement qui
crée un bon de commande (ou un ordre de fabrication) brouillon chaque fois
qu’une commande est confirmée, **quel que soit le niveau de stock actuel**.

Contrairement aux produits qui sont réapprovisionnés grâce aux règles de
réassort, Odoo associe automatiquement la commande client au bon de commande
ou à l’ordre de fabrication généré par la route MTO.

Une autre différence entre les règles de réassort et MTO est qu’avec la route
MTO, Odoo génère un bon de commande ou un ordre de fabrication brouillon
immédiatement après la confirmation de la commande client. Avec les règles de
réassort, Odoo génère un bon de commande ou un ordre de fabrication brouillon
lorsque le stock prévu du produit tombe en dessous de la quantité minimale
définie.

De plus, Odoo ajoute automatiquement des quantités au bon de commande ou à
l’ordre de fabrication au fur et à mesure que les prévisions changent, tant
que le bon de commande ou l’ordre de fabrication n’est pas confirmé.

La route MTO est la meilleure stratégie de réassort pour les produits
personnalisés et/ou pour des produits qui ne sont pas en stock.

## Configuration

### Rapport de réassort et règles de réassort

Pour accéder au rapport de réassort, allez à l’application Inventaire ‣
Opérations ‣ Réassort.

Par défaut, le tableau de bord des rapports de réassort affiche chaque produit
qui doit être réapprovisionné manuellement. Si aucune règle spécifique n’est
définie pour un produit, Odoo considère que la Quantité minimale et la
Quantité maximale sont toutes deux `0,00`.

Note

Pour les produits qui n’ont pas de règle de réassort définie, Odoo calcule les
prévisions sur la base des commandes client, des livraisons et des réceptions
confirmées. Pour les produits qui ont une règle de réassort définie, Odoo
calcule les prévisions normalement, mais prend également en compte le délai
des achats/de fabrication et le délai de sécurité.

Important

Avant de créer une nouvelle règle de réassort, assurez-vous qu’un
_fournisseur_ et une _nomenclature_ sont configurés sur la fiche du produit.
Pour le vérifier, allez à l’application Inventaire ‣ Produits ‣ Produits, et
sélectionnez le produit pour ouvrir sa fiche. Vous pouvez voir le fournisseur,
s’il est configuré, dans l’onglet Achats et la nomenclature, si elle est
configuré, en cliquant sur le bouton intelligent Nomenclatures en haut de la
fiche.

Le Type de produit, situé dans l’onglet Informations générales sur la fiche de
produit, **doit** être défini sur Produit stockable. Par définition, un
produit consommable ne fait pas l’objet d’un suivi de ses niveaux de stock,
donc Odoo ne peut pas tenir compte d’un produit consommable dans le rapport de
réassort.

![Le rapport de réassort répertoriant tous les articles à acheter pour
répondre aux besoins actuels.](../../../../../_images/replenishment-report-
dashboard.png)

Pour créer une nouvelle règle de réassort à partir du rapport de réassort,
allez à l’application Inventaire ‣ Opérations ‣ Réassort, cliquez sur Créer,
et sélectionnez le produit souhaité dans le menu déroulant dans la colonne
Produit. Le cas échéant, vous pouvez également configurer une Quantité min et
une Quantité max dans les colonnes appropriées sur la page du rapport de
Réassort.

Pour créer une nouvelle règle de réassort à partir de la fiche du produit,
allez à l’application Inventaire ‣ Produits ‣ Produits, et sélectionnez un
produit pour ouvrir sa fiche. Cliquez sur le bouton intelligent Règles de
réassort, cliquez sur Créer et remplissez les champs.

#### Champs du rapport de réassort

Les champs suivants figurent sur le rapport de Réassort. Si l’un de ces champs
n’est pas visible, cliquez sur l’icône ⋮ (options supplémentaires) à l’extrême
droite du rapport, puis cochez la case à côté d’un champ pour le rendre
visible.

  * Produit : le produit qui doit être réapprovisionné.

  * Emplacement : l’emplacement spécifique où le produit est stocké.

  * Entrepôt : l’entrepôt où le produit est stocké.

  * En stock : la quantité de produit actuellement disponible.

  * Prévision : la quantité de produits disponible après avoir pris en compte toutes les commandes en cours (ventes, fabrication, achats, etc.).

  * Route préférée : mode d’approvisionnement du produit : Acheter, Fabriquer, Dropshipping, etc.

  * Fournisseur : l’entreprise auprès de laquelle le produit est acheté.

  * Nomenclature : la nomenclature du produit (si elle est configurée).

  * Déclencheur : mode de création du réapprovisionnement : Automatique (dès que la quantité en stock passe en dessous de la Quantité minimale) ou Manuel (uniquement lorsque le réassort est demandé).

  * Groupe d’approvisionnement : le numéro de référence du mode d’acquisition du produit, tel qu’une commande client, un bon de commande ou un ordre de fabrication.

  * Quantité min : la quantité minimale de produit qui doit être disponible. Lorsque le niveau du stock est inférieur à cette quantité, le réassort est déclenché.

  * Quantité max : la quantité de produits qui doit être disponible après le réassort.

  * Quantité multiple : si le produit doit être commandé en quantités spécifiques, saisissez le nombre de produits à commander. Par exemple, si la Quantité multiple est définie sur `5` et seuls 3 produits sont nécessaires, 5 produits sont réapprovisionnés.

  * À commander : la quantité de produits actuellement nécessaire et qui sera commandée lorsque l’on clique sur Commander une fois ou Automatiser les commandes.

  * UdM : l’unité de mesure utilisée pour acheter le produit.

  * Société : la société pour laquelle le produit est acheté.

Par défaut, la quantité du champ À commander est la quantité requise pour
atteindre la Quantité max. Cependant, la quantité À commander peut être
modifiée en cliquant sur le champ et en modifiant la valeur. Pour
réapprovisionner un produit manuellement, cliquez sur Commander une fois.

Pour automatiser un réapprovisionnement à partir de la page des Réassorts,
cliquez sur le bouton Automatiser des commandes à l’extrême droite de la
ligne, représenté par une icône 🔄 (flèches circulaires).

Lorsque vous cliquez sur ce bouton, Odoo génère automatiquement un bon de
commande ou un ordre de fabrication brouillon chaque fois que le niveau de
stock prévu tombe en dessous de la Quantité min définie sur la règle de
réassort.

Sur la page des réassorts, il est possible de temporairement désactiver une
règle de réassort ou un réassort manuel pendant une certaine période de temps
en cliquant sur l’icône 🔕 (reporter) à l’extrême droite de la ligne.

![Les options de report pour désactiver les notifications du réassort pendant
une certaine période de temps.](../../../../../_images/reordering-rule-snooze-
settings.png)

Le document source d’un bon de commande ou d’un ordre de fabrication créé par
un réassort manuel est le Rapport de réassort. Le document source d’un bon de
commande ou un ordre de fabrication créé par une règle de réassort automatisée
est le numéro de référence de la commande client qui a déclenché la règle.

![Liste des demandes de prix dont les devis proviennent directement du rapport
de réassort.](../../../../../_images/rfq-source-document.png)

## Route Fabrication à la commande (MTO)

Puisque la route MTO est recommandée pour les produits personnalisés, elle est
masquée par défaut.

Pour activer la route MTO dans Odoo :

    

  1. Allez à l’application Inventaire ‣ Configuration ‣ Paramètres.

  2. Activez le paramètre Routes en plusieurs étapes situé dans la section Entrepôt et cliquez sur Enregistrer.

  3. Allez ensuite à l’application Inventaire ‣ Configuration ‣ Routes.

  4. Cliquez sur Filtres ‣ Archivé pour afficher les routes archivées.

  5. Cochez la case à côté de Réapprovisionner sur commande (MTO), et cliquez sur Action ‣ Désarchiver.

Note

L’activation du paramètre Routes en plusieurs étapes active également le
paramètre Emplacements de stockage. Si ces fonctionnalités ne sont pas
applicables à l’entrepôt, désactivez ces paramètres après avoir désarchivé la
route MTO.

Pour définir la route d’approvisionnement d’un produit sur MTO, allez à
l’application Inventaire ‣ Produits ‣ Produits et cliquez sur le produit
souhaité pour ouvrir sa fiche.

Cliquez ensuite sur l’onglet Inventaire et dans la section Routes,
sélectionnez Réapprovisionner sur commande (MTO).

Pour les produits directement achetés auprès d’un fournisseur, assurez-vous
que la route Acheter est sélectionnée en plus de la route Réapprovisionner sur
commande (MTO). Assurez-vous également qu’un fournisseur est configuré dans
l’onglet Achats d’une fiche de produit.

Pour les produits fabriqués en interne, assurez-vous que la route Fabriquer
est sélectionnée, en plus de la route Réapprovisionner sur commande (MTO).
Assurez-vous également qu’une nomenclature est configurée pour le produit, qui
est accessible via le bouton intelligent Nomenclature sur la fiche du produit.

Note

Il n’est pas possible d’uniquement sélectionner la route MTO. MTO fonctionne
**uniquement** si la route Fabriquer ou Acheter est également sélectionnée.

![Route Réapprovisionner sur commande sélectionnée sur la fiche du
produit.](../../../../../_images/acoustic-block-screen-replenish.png)

  *[MTO]: Make to Oder

