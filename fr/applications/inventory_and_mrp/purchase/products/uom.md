# Acheter dans une unité de mesure différente de celle utilisée pour la vente

Lorsque vous achetez un produit, il se peut que votre fournisseur utilise une
unité de mesure différente de celle que vous utilisez pour vendre. Ceci
pourrait être source de confusion entre les responsables des ventes et des
achats. Il est également fastidieux de convertir mensuellement les unités de
mesure à chaque fois. Avec Odoo, vous pouvez configurer votre produit une
seule fois et laisser Odoo se charger de la conversion.

Prenons les exemples suivants :

  1. Vous achetez du jus d’orange auprès d’un fournisseur américain qui utilise des **gallons**. Cependant, vos clients sont européens et utilisent des**litres**.

  2. Vous achetez des rideaux auprès d’un fournisseur sous forme de **rouleaux** et vous vendez des morceaux de rouleaux à vos clients qui utilisent des **mètres carrés**.

## Activer les unités de mesure

Ouvrez votre application Ventes et allez à Configuration ‣ Paramètres. Dans la
section Catalogue de produits, activez les _unités de mesure_.

![Activer l'option des unités de mesure dans Odoo
Ventes](../../../../_images/uom-enable-option.png)

## Définir des unités de mesure d’achat et de vente

### Unités de mesure standards

Une variété d’unités de mesure sont disponibles par défaut dans votre base de
données. Chacune appartient à l’une des cinq catégories d’unités de mesure
préconfigurées : _Longueur / Distance_ , _Unité_ , _Volume_ , _Poids_ et
_Temps de travail_.

Astuce

Vous pouvez créer vos propres unités de mesure et catégories d’unités de
mesure (voir la section suivante).

Pour définir des unités de mesure différentes pour les achats et les ventes,
ouvrez l’application Achats et allez à Produits ‣ Produits. Créez un produit
ou sélectionnez un produit existant. Sous l’onglet _Informations générales_ du
produit, sélectionnez d’abord l” _unité de mesure_ qui sera utilisée pour les
ventes (et pour toutes les autres applications telles qu’Inventaire).
Sélectionnez ensuite l” _unité de mesure d’achat_ qui sera utilisée pour les
achats.

Revenons au premier exemple. Si vous achetez du jus d’orange auprès de votre
fournisseur en **gallons** et vendez-le à vos clients en **litres** ,
sélectionnez d’abord _L_ (litres) comme _unité de mesure_ et _gal (US)_
(gallons) comme _unité de mesure d’achat_. Cliquez ensuite sur _Enregistrer_.

![Configurer l'unité de mesure d'un produit dans
Odoo](../../../../_images/uom-product-configuration.png)

### Créer de nouvelles unités de mesure et catégories d’unités de mesure

Parfois, vous devez créer vos propres unités et catégories, soit parce que la
mesure n’est pas préconfigurée dans Odoo, soit parce que les unités ne sont
pas liées entre elles (par ex. kilos et centimètres).

Si vous prenez le deuxième exemple où vous achetez des rideaux auprès d’un
fournisseur sous forme de **rouleaux** et vous vendez des morceaux des
rouleaux en utilisant des **mètres carrés** , vous devez créer une nouvelle
_catégorie d’unités de mesure_ afin de relier les deux unités de mesure.

Pour ce faire, allez à Configuration ‣ Catégories d’unités de mesure. Cliquez
sur _Créer_ et nommez la catégorie.

![Créer une nouvelle catégorie d'unités de mesure dans Odoo
Achats](../../../../_images/uom-new-category.png)

La prochaine étape est de créer les deux unités de mesure. Pour ce faire,
allez à Configuration ‣ Unités de mesure.

Créez d’abord l’unité de mesure utilisée comme point de référence pour la
conversion vers d’autres unités de mesure à l’intérieur de la catégorie en
cliquant sur _Créer_. Nommez l’unité et sélectionnez la catégorie d’unités de
mesure que vous venez de créer. Concernant le _Type_ , sélectionnez _Unité de
mesure de référence pour cette catégorie_. Saisissez la _précision d’arrondi_
que vous voulez appliquer. La quantité calculée par Odoo est toujours un
multiple de cette valeur.

Dans l’exemple, comme vous ne pouvez pas acheter moins d’un rouleau et que
vous n’utiliserez pas de fractions de rouleau comme unité de mesure, vous
pouvez saisir 1.

![Créer une nouvelle unité de mesure de référence dans Odoo
Achats](../../../../_images/uom-new-reference-unit.png)

Note

Si vous utilisez une _précision d’arrondi_ inférieure à 0,01, un message
d’avertissement peut apparaître indiquant qu’elle est supérieure à la
_précision décimale_ et qu’elle peut entraîner des incohérences. Si vous
souhaitez utiliser une _précision d’arrondi_ inférieure à 0,01, activez
d’abord le [mode développeur](../../../general/developer_mode.html#developer-
mode), allez ensuite à Paramètres ‣ Technique ‣ Structure de la base de
données ‣ Précision décimale, sélectionnez _Unité de mesure du produit_ et
modifiez les _chiffres_ en conséquence. Par exemple, si vous voulez appliquer
une précision d’arrondi de 0,00001, définissez les _chiffres_ sur 5.

Créez ensuite une deuxième unité de mesure, nommez-la et sélectionnez la même
catégorie d’unités de mesure comme votre unité de référence. Dans la section
_type_ , sélectionnez _plus petite_ ou _plus grande que l’unité de mesure de
référence_ , en fonction de votre situation.

Comme le rouleau de rideaux équivaut à 100 mètres carrés, vous devez
sélectionner _plus petite_.

Ensuite, vous devez saisir le _facteur_ entre votre unité de référence et la
deuxième unité. Si la deuxième unité est plus petite, le _facteur_ doit être
supérieur à 1. Si la deuxième unité est plus grande, le facteur doit être
inférieur à 1.

Pour votre rouleau de rideaux, le facteur doit être de 100.

![Créer une deuxième unité de mesure dans Odoo
Achats](../../../../_images/uom-second-unit.png)

Vous pouvez à présent configurer votre produit comme vous le feriez en
utilisant les unités de mesure standards d’Odoo.

![Définir des unités de mesure d'un produit utilisant vos propres unités dans
Odoo Achats](../../../../_images/uom-product-configuration-new-units.png)

