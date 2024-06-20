# Vue d’ensemble

Il existe différentes situations dans lesquelles les nomenclatures de codes-
barres peuvent être utiles. Un cas d’utilisation bien connu est celui d’un
point de vente qui vend des produits en vrac, dans lequel les clients pèsent
eux-mêmes leurs produits et reçoivent le code-barres imprimé à coller sur le
produit. Ce code-barres contiendra le poids du produit et permettra de
calculer le prix en conséquence.

## Créer une nomenclature de codes-barres

Odoo prend en charge les nomenclatures des codes-barres, qui déterminent le
mappage et l’interprétation des informations encodées. Vous pouvez configurer
votre nomenclature de code-barres en étant en [mode
développeur](../../../general/developer_mode.html#developer-mode). Pour ce
faire, allez à Inventaire ‣ Configuration ‣ Nomenclature des code-barres.

Vous pouvez créer une nomenclature de codes-barres d’ici et ensuite ajouter
une ligne pour créer votre première règle.

![../../../../_images/barcode_nomenclature_01.png](../../../../_images/barcode_nomenclature_01.png)

La première étape consiste à préciser le **nom de la règle** , par exemple le
Code-barres Poids avec 3 décimales. Vous devez ensuite préciser le type de
nomenclature de code-barres, dans notre cas ce sera Produit pondéré.

![../../../../_images/barcode_nomenclature_02.png](../../../../_images/barcode_nomenclature_02.png)

Le modèle de code-barres est une expression régulière qui définit la structure
du code-barres. Dans cet exemple, 21 définit les produits sur lesquels la
règle sera appliquée, ce sont les numéros par lesquels le code-barres du
produit doit commencer. Les 5 “points” sont les numéros suivants du code-
barres du produit et sont là simplement pour identifier le produit en
question. Le “N” définit un nombre et le “D” définit les décimales.

L’encodage permet de préciser l’encodage du code-barres sur lequel la règle
doit être appliquée.

Note

Vous pouvez définir différentes règles et les classer par ordre de priorité
grâce à la séquence. La première règle qui correspond au code-barres scanné
sera appliquée.

### Configurer votre produit

  1. Le code-barres du produit devrait commencer par “21” ;

  2. Les 5 “points” sont les autres numéros du code-barres de votre produit, permettant d’identifier le produit ;

  3. Le code-barres doit contenir des 0 là où vous avez défini des D ou des N. Dans notre cas, nous devons mettre 5 zéros, car nous avons configuré “21…..{NNDDD}” ;

  4. En EAN-13, le dernier chiffre est un chiffre de contrôle, utilisez un générateur d’EAN13 pour savoir quel devrait être le dernier chiffre dans votre cas.

![../../../../_images/barcode_nomenclature_03.png](../../../../_images/barcode_nomenclature_03.png)

Dans le cas où vous pesez 1,5 kg de pâtes, la balance vous imprimera le code-
barres suivant 2112345015002. Si vous scannez ce code-barres dans votre point
de vente ou lorsque vous recevez des produits dans votre application de code-
barres, Odoo créera automatiquement une nouvelle ligne pour le produit Pâtes
pour une quantité de 1,5 kg. Pour le point de vente, un prix dépendant de la
quantité sera également calculé.

![../../../../_images/barcode_nomenclature_04.png](../../../../_images/barcode_nomenclature_04.png)

### Types de règle

  * **Produit à prix fixe** : vous permet d’identifier le produit et de préciser son prix, utilisé dans les points de vente.

  * **Produit en promotion** : vous permet de créer un code-barres par remise appliquée. Vous pouvez alors scanner votre produit dans le point de vente, puis scanner le code-barres de la remise et la remise sera appliquée sur le prix normal du produit.

  * **Produit pesé** : vous permet d’identifier le produit et de préciser son poids, utilisé à la fois dans les points de vente (dans lesquels le prix est calculé en fonction du poids) et dans l’inventaire.

  * **Client** : vous permet d’identifier le client, par exemple utilisé avec un programme de fidélité.

  * **Caissier** : vous permet d’identifier le caissier lors de l’entrée dans le point de vente.

  * **Emplacement** : vous permet d’identifier l’emplacement d’un transfert lorsque les emplacements multiples sont activés.

  * **Colis** : vous permet d’identifier les colis sur un transfert lorsque les colis sont activés.

  * **Carte de crédit** : ne nécessite pas de modification manuelle, existe pour les données du module Mercury.

  * **Unité de produit** : vous permet d’identifier un produit pour les points de vente et les transferts.

Note

Lorsque le modèle de code-barres contient .*, cela signifie qu’il peut
contenir un nombre quelconque de caractères, ces caractères pouvant être
n’importe quel nombre.

