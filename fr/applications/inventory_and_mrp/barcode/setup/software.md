# Activer les codes-barres dans Odoo

Les fonctionnalités de lecture des codes-barres peuvent vous faire gagner un
temps considérable, habituellement perdu à alterner entre le clavier, la
souris et le lecteur. En attribuant correctement des codes-barres aux
produits, aux emplacements de retrait, etc., vous pouvez travailler plus
efficacement en contrôlant le logiciel presque exclusivement avec le lecteur
de codes-barres.

## Configuration

Pour utiliser cette fonctionnalité, vous devez d’abord activer la
fonctionnalité _Code-barres_ via Inventaire ‣ Paramètres ‣ Lecteur de codes-
barres. Une fois que vous avez coché la fonctionnalité, vous pouvez cliquer
sur enregistrer.

![../../../../_images/software_01.png](../../../../_images/software_01.png)

## Configurer les codes-barres des produits

Vous pouvez facilement attribuer des codes-barres à vos différents produits
via l’application _Inventaire_. Pour ce faire, allez aux Paramètres ‣
Configurer les codes-barres des produits.

![../../../../_images/software_02.png](../../../../_images/software_02.png)

Ensuite, vous avez la possibilité d’attribuer des codes-barres à vos produits
sur la fiche produit directement lors de la création de ce produit.

![../../../../_images/software_03.png](../../../../_images/software_03.png)
![../../../../_images/software_04.png](../../../../_images/software_04.png)

Note

Veillez à ajouter les codes-barres directement sur les variantes du produit et
non sur le modèle du produit. Sinon, vous ne serez pas en mesure de les
différencier.

## Configurer les codes-barres des emplacements

Si vous gérez plusieurs emplacements, il peut être utile d’attribuer un code-
barres à chaque emplacement et de le coller sur l’emplacement. Vous pouvez
configurer les codes-barres des emplacements dans Inventaire ‣ Configuration ‣
Emplacements.

![../../../../_images/software_05.png](../../../../_images/software_05.png)
![../../../../_images/software_06.png](../../../../_images/software_06.png)

Note

Vous pouvez facilement imprimer le code-barres que vous attribuez aux
emplacements via le menu _Imprimer_.

## Formats des codes-barres

La plupart des produits de détail utilisent des codes-barres EAN-13, également
appelés GTIN (Global Trade Identification Numbers). Les entreprises utilisent
les GTIN pour identifier leurs produits et services de manière unique. Bien
que GTIN et UPC soient souvent utilisés comme synonymes, GTIN fait référence
au numéro qu’un code-barres représente, tandis qu’UPC fait référence au code-
barres lui-même. Vous trouverez plus d’informations sur le GTIN sur le site
web de GS1.

Pour pouvoir créer des GTIN pour des articles, une entreprise doit disposer
d’un préfixe d’entreprise GS1. Ce préfixe est le numéro qui apparaît au début
de chaque GTIN et qui identifie l’entreprise en tant que propriétaire du code-
barres ou des produits sur lesquels il apparaît. Pour en savoir plus sur les
préfixes d’entreprise GS1, ou acheter une licence pour un préfixe, consultez
la page des préfixes d’entreprise GS1.

Les utilisateurs d’Odoo peuvent utilisent les codes-barres GTIN pour
identifier leurs produits. Cependant, comme Odoo prend en charge n’importe
quelle chaîne numérique comme code-barres, il est également possible de
définir un code-barres personnalisé pour un usage interne.

