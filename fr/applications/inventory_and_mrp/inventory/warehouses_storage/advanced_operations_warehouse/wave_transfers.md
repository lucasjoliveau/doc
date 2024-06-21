# Traiter les transferts par vague

Alors qu’un transfert par lot est un groupe de plusieurs transferts, un
**transfert par vague** ne contient que certaines parties de différents
transferts. Les deux méthodes sont utilisées pour préparer des commandes dans
un entrepôt et, selon la situation, une méthode peut être plus adaptée que
l’autre.

Pour traiter les commandes d’une catégorie de produits spécifique ou pour
aller chercher des produits qui se trouvent dans le même emplacement, les
transferts par vague sont parfaits.

Dans Konvergo ERP, les transferts par vague sont en fait des transferts par lot avec
une étape supplémentaire : les transferts sont fractionnés avant d’être
regroupés dans un lot.

## Configuration

Avant de créer un transfert par vague, les options **Transferts par lot** et
**Transferts par vague** doivent être activées.

Tout d’abord, allez à Inventaire ‣ Configuration ‣ Paramètres. Dans la section
**Opérations** , activez **Transferts par lot** et **Transferts par vague**.
Cliquez ensuite sur **Enregistrer** pour appliquer les paramètres.

![Vue des paramètres d'Konvergo ERP Inventaire pour activer l'option des transferts
par vague.](../../../../../_images/wave-transfers-setting.png)

## Ajouter des produits à une vague

Maintenant que les paramètres sont activés, lancez un transfert par vague en
ajoutant des produits à une vague.

Les transferts par vague ne peuvent contenir que des lignes de produit
provenant de transferts du même type d’opération. Pour afficher tous les
transferts et lignes de produit d’une opération spécifique, allez d’abord au
tableau de bord d”**Inventaire** et localisez la carte du type d’opération
souhaité. Ouvrez ensuite les options (l’icône des trois points dans le coin de
la carte du type d’opération) et cliquez sur **Opérations**.

![Comment obtenir la liste des opérations d'un type
d'opération.](../../../../../_images/list-of-operations.png)

Sur la page des opérations, sélectionnez les lignes du produit que vous voulez
ajouter à une vague nouvelle ou existante. Cliquez ensuite sur **Ajouter à une
vague**.

![Sélectionnez des lignes à ajouter à la
vague.](../../../../../_images/select-lines.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Utilisez les <b>Filtres</b> dans la barre de recherche pour regrouper les lignes avec le même produit, emplacement, transporteur, etc.</p>
</div>

Une fenêtre contextuelle apparaîtra ensuite.

Pour ajouter les lignes sélectionnées à un transfert par vague existant,
sélectionnez l’option **un transfert par vague existant** et sélectionnez le
transfert par vague existant dans le menu déroulant.

Pour créer un nouveau transfert par vague, sélectionnez l’option **un nouveau
transfert par vague**. Lors de la création d’un nouveau transfert par vague,
il est aussi possible de définir un employé dans le champ optionnel
**Responsable**. Une fois les options souhaitées sélectionnées, cliquez sur
**Confirmer** pour ajouter les lignes de produit à une vague.

## Voir les transferts par vague

Pour voir tous les transferts par vague et leurs statuts, allez à Inventaire ‣
Opérations ‣ Transferts par vague. Il est aussi possible de voir les
transferts par vague dans l’application **Code-barres** en allant à Code-
barres ‣ Transferts par lot.

