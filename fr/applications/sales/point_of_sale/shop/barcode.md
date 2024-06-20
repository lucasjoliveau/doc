# Codes-barres

L’utilisation d’un lecteur de codes-barres pour traiter les commandes du point
de vente permet d’améliorer l’efficacité et la rapidité du service à la
clientèle. Les lecteurs de codes-barres peuvent être utilisés pour scanner des
produits ou pour enregistrer des employés dans une session du point de vente.

## Configuration

Pour utiliser un lecteur de codes-barres, vous devez activer la fonctionnalité
dans l’application Inventaire. Allez à Inventaire ‣ Configuration ‣
Paramètres, dans la section Code-barres, cochez la case à côté de Lecteur de
codes-barres et enregistrez.

![Le paramètre des codes-barres dans l'application
Inventaire](../../../../_images/barcode-inventory.png)

Pour plus d'infos

  * [Configurer un lecteur de codes-barres](../../../inventory_and_mrp/barcode/setup/hardware.html)

  * [Activer les lecteurs de codes-barres](../../../inventory_and_mrp/barcode/setup/software.html)

Une fois activée dans **Inventaire** , vous pouvez utiliser la fonctionnalité
des codes-barres dans **Point de Vente** sur les produits auxquels est assigné
un numéro de code-barres.

## Assigner des codes-barres

### À vos produits

Pour utiliser cette fonctionnalité dans le point de vente, il faut assigner
des codes-barres à vos produits. Pour ce faire, allez à Point de Vente ‣
Produits ‣ Produits et ouvrez une **fiche produit**. Ajoutez un numéro de
code-barres dans le champ code-barres dans l’onglet Informations générales.

### À vos employés

Pour ajouter un numéro d’identification à un employé, allez à l’application
**Employés** et ouvrez une **fiche employé**. Choisissez un numéro
d’identification à votre employé et complétez le champ Code PIN dans l’onglet
Paramètres RH.

## Utiliser des codes-barres

### Scanner des produits

Scannez le code-barres d’un produit avec un lecteur de codes-barres. Ceci
permet de l’ajouter directement au panier. Pour changer la quantité, scannez
un produit autant de fois que nécessaire ou cliquez sur Qté et saisissez le
nombre de produits à l’aide du clavier.

Vous pouvez également saisir le numéro du code-barres dans la barre de
recherche pour rechercher le produit. Cliquez ensuite sur le produit pour
l’ajouter au panier.

### Enregistrer les employés

Vous pouvez également utiliser un lecteur de code-barres pour enregistrer vos
employés. Pour ce faire, [limitez l’accès](../employee_login.html#employee-
login-configuration) au point de vente et [utilisez des codes-barres pour
enregistrer vos employés](../employee_login.html#employee-login-badge) dans
votre point de vente.

