# Configuration du produit de fabrication

Afin de fabriquer un produit dans Konvergo ERP _Fabrication_ , le produit doit être
correctement configuré. La route _Fabrication_ doit être activée et une
nomenclature doit être configurée pour le produit. Une fois ces étapes
terminées, le produit peut être sélectionné lors de la création d’un nouvel
ordre de fabrication.

## Activer la route Fabriquer

La route Fabriquer est activée pour chaque produit sur sa propre page produit.
Pour ce faire, allez à Fabrication ‣ Produits ‣ Produits. Sélectionnez ensuite
un produit existant ou créez-en un nouveau en cliquant sur **Nouveau**.

Sur la page produit, sélectionnez l’onglet **Inventaire** et cochez la case
**Fabriquer** dans la section **Routes**. Cela indique à Konvergo ERP que le produit
peut être fabriqué.

![La route Fabriquer sur l'onglet Inventaire d'une page
produit.](../../../../_images/manufacturing-route.png)

## Configurer une nomenclature

Vous devez ensuite configurer une nomenclature pour qu’Konvergo ERP sache comment le
produit est fabriqué. Une nomenclature est une liste des composants et des
opérations nécessaires à la fabrication d’un produit.

Pour créer une nomenclature pour un produit spécifique, allez à Fabrication ‣
Produits ‣ Produits, puis sélectionnez le produit. Sur la page produit,
cliquez sur le bouton intelligent **Nomenclatures** en haut de la page, puis
sélectionnez **Nouveau** pour configurer une nouvelle nomenclature.

![Le bouton intelligent Nomenclatures sur une page
produit.](../../../../_images/bom-smart-button1.png)

Sur la nomenclature, le champ **Produit** se remplit automatiquement avec le
produit. Dans le champ **Quantité** , précisez le nombre d’unités produites
par la nomenclature.

Ajoutez un composant à la nomenclature en sélectionnant l’onglet
**Composants** et en cliquant sur **Ajouter une ligne**. Sélectionnez un
composant dans le menu déroulant **Composant** , puis saisissez la quantité
dans le champ **Quantité**. Continuez à ajouter des composants sur de
nouvelles lignes jusqu’à ce que tous les composants aient été ajoutés.

![L'onglet Composants d'une nomenclature.](../../../../_images/components-
tab.png)

Sélectionnez ensuite l’onglet **Opérations**. Cliquez sur **Ajouter une
ligne** et une fenêtre contextuelle **Créer Opérations** s’ouvre. Dans le
champ **Opération** , précisez le nom de l’opération ajoutée (par ex.
Assembler, Couper, etc.). Sélectionnez le poste de travail où l’opération sera
effectuée dans le menu déroulant **Poste de travail**. Enfin, cliquez sur
**Enregistrer & Fermer** pour terminer l’ajout d’opérations ou sur
**Enregistrer & Nouveau** pour en ajouter d’autres.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>L’onglet <b>Opérations</b> s’affiche uniquement si le paramètre <b>Ordres de travail</b> est activé. Pour ce faire, allez à Fabrication ‣ Configuration ‣ Paramètres, puis cochez la case <b>Ordres de travail</b>.</p>
</div> ![L'onglet Opérations d'une
nomenclature.](../../../../_images/operations-tab1.png) <div class="admonition-learn-more alert">
<p class="alert-title">
En savoir plus</p><p>Cette documentation vous montre comment créer une nomenclature de base qui permet de fabriquer un produit dans Konvergo ERP. Toutefois, il ne s’agit aucunement d’un résumé exhaustif de toutes les options disponibles lors de la configuration d’une nomenclature. Pour plus d’informations sur les nomenclatures, consultez la documentation sur la façon de <a href="bill_configuration#manufacturing-management-bill-configuration"><span class="std std-ref">créer une nomenclature</span></a>.</p>
</div>

