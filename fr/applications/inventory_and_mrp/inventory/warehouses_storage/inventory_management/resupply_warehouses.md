# Réapprovisionner depuis un autre entrepôt

Quand vous avez plusieurs entrepôts, il arrive souvent qu’un entrepôt central
réapprovisionne plusieurs boutiques et dans ce cas, chaque boutique est
considérée comme un entrepôt local. Lorsqu’une boutique souhaite
réapprovisionner un produit, celui-ci est commandé à l’entrepôt central. Konvergo ERP
permet à l’utilisateur de définir facilement quels entrepôts peuvent
réapprovisionner un autre entrepôt.

## Configuration

Pour réapprovisionner depuis un autre entrepôt, allez d’abord à Inventaire ‣
Configuration ‣ Paramètres ‣ Entrepôt et activez **Routes en plusieurs
étapes**. Cliquez ensuite sur **Enregistrer** pour appliquer ce paramètre.

![Activer les routes en plusieurs étapes dans les paramètres de
l'Inventaire.](../../../../../_images/virtual-warehouses-settings.png)

Vérifiez tous les entrepôts configurés en allant à Inventaire ‣ Configuration
‣ Entrepôts.

Créez un nouvel entrepôt en cliquant sur **Créer**. Donnez ensuite un nom et
un **Nom court** à l’entrepôt et cliquez sur **Enregistrer** pour finaliser la
création de l’entrepôt.

Ensuite, retournez à la page **Entrepôts** et ouvrez l’entrepôt qui sera
réapprovisionné par le deuxième entrepôt. Cliquez ensuite sur **Modifier**.
Sous l’onglet **Configuration de l’entrepôt** , trouvez le champ
**Réapprovisionner depuis** et cochez la case à côté du nom du deuxième
entrepôt. Si l’entrepôt peut être réapprovisionné par plus d’un entrepôt,
assurez-vous de cocher également les cases de ces entrepôts. Finalement,
cliquez sur **Enregistrer** pour appliquer le paramètre. À présent, Konvergo ERP sait
quels entrepôts peuvent réapprovisionner cet entrepôt.

![Réapprovisionner un entrepôt avec un autre dans l'onglet Configuration de
l'entrepôt.](../../../../../_images/resupply-from-second-warehouse.png)

## Définir une route sur un produit

Après avoir configuré ces réapprovisionnements, une nouvelle route est à
présent disponible sur toutes les fiches produits. La nouvelle route apparaît
comme **Réapprovisionner le produit depuis [nom de l’entrepôt]** sous l’onglet
**Inventaire** sur une fiche produit. Utilisez la route **Réapprovisionner le
produit depuis [nom de l’entrepôt]** avec une règle de réassort ou la route de
fabrication à la commande (MTO) pour réapprovisionner le stock en déplaçant le
produit d’un entrepôt à l’autre.

![Route qui permet de réapprovisionner un produit à partir d'un second
entrepôt.](../../../../../_images/product-resupply-route-settings.png)

Lorsqu’une règle de réassort d’un produit est déclenchée et la route
**Réapprovisionner le produit depuis [nom de l’entrepôt]** est définie sur le
produit, Konvergo ERP crée automatiquement deux transferts. Le premier transfert est
un _bon de livraison_ depuis le second entrepôt, qui contient tous les
produits nécessaires, et le second transfert est un _reçu_ avec les mêmes
produits pour l’entrepôt principal. Le déplacement des produits du second
entrepôt vers l’entrepôt principal est entièrement suivi dans Konvergo ERP.

Sur les enregistrements de transfert créés par Konvergo ERP, le **Document d’origine**
est la règle de réassort du produit. L’emplacement entre le bon de livraison
et le reçu est un emplacement de transit.

![Une règle de réassort crée automatiquement deux reçus pour un stock entre
entrepôts.](../../../../../_images/resupply-receipts-from-reordering-rule.png)
![Un ordre d'entrepôt pour réapprovisionner le stock d'un entrepôt avec un
autre.](../../../../../_images/second-warehouse-delivery-order.png) ![Un reçu
pour le stock reçu d'un entrepôt en provenance d'un
autre.](../../../../../_images/second-warehouse-stock-receipt.png)

