# Transferts par lot

Le _transfert par lot_ permet à un seul préparateur de commandes de traiter
plusieurs commandes à la fois, réduisant ainsi le temps nécessaire pour se
rendre au même emplacement dans un entrepôt.

Pour les transferts par lot, les ordres sont regroupés et consolidés dans une
liste de transferts. Après le transfert, le lot est acheminé vers un
emplacement de sortie, où les produits sont triés dans leurs emballages de
livraison respectifs.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="#inventory-management-barcode-picking"><span class="std std-ref">Utiliser l’application Code-barres pour les transferts</span></a></p>
</div>

Puisque les ordres _doivent_ être triés à l’emplacement de sortie après avoir
été transférés, cette méthode de transfert convient aux entreprises qui
commandent peut de produits. Le stockage des articles très demandés dans des
emplacements facilement accessibles permet d’augmenter le nombre d’ordres
satisfaits de manière efficace.

## Configuration

Pour activer l’option de transfert par lot, allez à l’application Inventaire ‣
Configuration ‣ Paramètres. Dans la section **Opérations** , cochez la case
**Transferts par lot**.

![Activez la fonctionnalité *Transferts par lot* dans Inventaire >
Configuration > Paramètres.](../../../../../_images/batch-transfer-
checkbox.png)

Puisque le transfert par lot est une méthode permettant d’optimiser
l’opération de _transfert_ dans Konvergo ERP, les fonctionnalités **Emplacements de
stockage** et **Routes en plusieurs étapes** dans la section **Entrepôt**
doivent également être activées sur la page des paramètres. Lorsque vous avez
terminé, cliquez sur **Enregistrer**.

![Activez les fonctionnalités *Emplacements de stockage* et *Routes en
plusieurs étapes* dans Inventaire > Configuration >
Paramètres.](../../../../../_images/locations-routes-checkbox.png)

Enfin, activez la fonctionnalité du transfert dans l’entrepôt, en allant à la
page des paramètres de l’entrepôt, accessible à partir de l’application
Inventaire ‣ Configuration ‣ Entrepôts.

Sélectionnez ici l’entrepôt souhaité dans la liste. Ensuite, parmi les options
disponibles pour les **Expéditions** , sélectionnez soit **Amener les
marchandises à l’emplacement de sortie et ensuite livrer (2 étape)** ou
**Emballer les marchandises, les envoyer à l’emplacement de sortie et ensuite
livrer (3 étapes)**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps#inventory-receipts-delivery-two-steps"><span class="std std-ref">Livraison en deux étapes</span></a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/delivery_three_steps#inventory-delivery-three-steps"><span class="std std-ref">Livraison en trois étapes</span></a></p></li>
</ul>
</div> ![Configurez des expéditions en 2 ou 3
étapes.](../../../../../_images/set-2-or-3-step-shipment.png)

## Créer des transferts par lot

Vous pouvez manuellement créer des transferts par lot à partir de
l’application Inventaire ‣ Opérations ‣ Transferts par lot. Cliquez sur le
bouton **Nouveau** pour créer un transfert par lot.

Sur le formulaire du transfert par lot, complétez les champs suivants en
conséquence :

  * **Responsable** : l’employé assigné au transfert. Laissez ce champ vide si _n’importe quel_ ouvrier peut effectuer ce transfert.

  * **Type d’opération** : sélectionnez dans le menu déroulant le type d’opération sous lequel le transfert est classé.

  * **Date planifiée** : précise la date à laquelle la personne **Responsable** doit effectuer le transfert vers l’emplacement de sortie.

Ensuite, dans la liste des **Transferts** , cliquez sur **Ajouter une ligne**
pour ouvrir la fenêtre **Ajouter : Transferts**.

Si vous avez complété le champ **Type d’opération** , la liste filtrera les
enregistrements de transfert correspondant au **Type d’opération**
sélectionné.

Cliquez sur le bouton **Nouveau** pour créer un nouveau transfert.

Une fois les enregistrements de transfert sélectionnés, cliquez sur
**Confirmer** pour confirmer le transfert par lot.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un nouveau transfert par lot est assigné au <b>Responsable</b>, <code>Joel Willis</code>, pour le <b>type d’opération</b> <code>Transfert</code>. La <b>Date planifiée</b> est définie sur <code>11 août</code>.</p>
<img alt="Vue du formulaire *Transferts par lot*." class="align-center" src="../../../../../_images/batch-transfer-form.png"/>
<p>En cliquant sur le bouton <b>Ajouter une ligne</b>, la fenêtre <b>Ajouter : Transferts</b> s’ouvre et n’affiche que les transferts, étant donné que le <b>Type d’opération</b> était défini sur <code>Transfert</code> sur le formulaire du transfert par lot.</p>
<p>Cochez la case à cocher à gauche des transferts, <code>WH/PICK/00001</code> et <code>WH/PICK/00002</code>, pour les inclure dans le nouveau transfert. Cliquez ensuite sur le bouton <b>Sélectionner</b> pour fermer la fenêtre <b>Ajouter : Transferts</b>.</p>
<img alt="Sélectionnez plusieurs transferts dans la fenêtre *Ajouter : Transferts*." class="align-center" src="../../../../../_images/add-transfers-window.png"/>
</div>

### Ajouter un lot à partir de la liste des transferts

Il existe une autre méthode de créer des transferts par lot : l’option
**Ajouter au lot** dans la vue de liste. Allez à l’application Inventaire ‣
Opérations et sélectionnez n’importe quel **Transfert** dans le menu déroulant
pour ouvrir une liste filtrée de transferts.

![Afficher tous les types de transfert dans un menu déroulant : Réceptions,
Livraisons, Transferts internes,  Fabrications, Transferts par lot,
Dropshippings.](../../../../../_images/transfers-drop-down.png)

Sur la liste des transferts, cochez la case à gauche des transferts
sélectionnés pour l’ajouter à un lot. Allez ensuite au bouton **Actions ⚙️
(engrenage)** et cliquez sur **Ajouter au lot** dans le menu déroulant qui
s’ouvre.

![Utiliser le bouton *Ajouter au lot*, dans la liste du bouton
*Action*.](../../../../../_images/add-to-batch.png)

Cette action ouvre une fenêtre contextuelle **Ajouter au lot** , dans laquelle
l’employé **Responsable** du transfert peut être désigné.

Choisissez parmi les deux options radio d’ajouter à **un transfert par lot
existant** ou de créer **un nouveau transfert par lot**.

Pour commencer par un brouillon, cochez la case **Brouillon**.

Terminez le processus en cliquant sur **Confirmer**.

![Afficher la fenêtre *Ajouter au lot* pour créer un transfert par
lot.](../../../../../_images/add-to-batch-window.png)

## Traiter des transferts par lot

Traitez les transferts par lot dans l’application Inventaire ‣ Opérations ‣
Transferts par lot.

Sélectionnez le transfert souhaité dans la liste. Ensuite, sur le formulaire
du transfert par lot, saisissez les quantités **faites** pour chaque produit,
dans l’onglet **Opérations détaillées**. Cliquez enfin sur **Valider** pour
terminer le transfert.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Assurez-vous que le transfert par lot est terminé lorsque le bouton <b>Valider</b> est surligné en mauve. Si le bouton <b>Vérifier la disponibilité</b> est surligné à la place, cela signifie qu’il y a des articles dans le lot qui ne sont actuellement <em>pas</em> disponibles en stock.</p>
</div> <div class="alert alert-success" id="inventory-management-batch-transfers-example">
<p class="alert-title">
Example</p><p>Dans un transfert par lot impliquant des produits provenant des transferts, <code>WH/PICK/00001</code> et <code>WH/PICK/00002</code>, l’onglet <b>Opérations détaillées</b> montre que le produit, <code>Armoire avec portes</code>, a été transféré parce que la colonne <b>Fait</b> correspond à la valeur de la colonne <b>Réservé</b>. Cependant, des quantités de <code>0,00</code> ont été transférées pour l’autre produit, <code>Boîtier pour câbles</code>.</p>
<img alt="Afficher le transfert par lot de produits provenant de deux transferts dans l'onglet *Opérations détaillées*." class="align-center" src="../../../../../_images/process-batch-transfer.png"/>
</div>

Seuls les produits en stock sont visibles dans l’onglet **Opérations
détaillées**.

Pour afficher la liste complète des produits, allez à l’onglet **Opérations**.
Dans cette liste, la colonne **Demande** indique la quantité souhaitée pour
l’ordre. La colonne **Réservé** indique le stock disponible pour honorer
l’ordre. Enfin, la colonne **Fait** précise les produits qui ont été
transférés et qui sont prêts pour l’étape suivante.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Le produit, <code>Sous-main</code>, issu du même lot que l”<a href="#inventory-management-batch-transfers-example"><span class="std std-ref">exemple ci-dessus</span></a>, n’est visible que dans l’onglet <b>Opérations</b>, car il n’y a pas de quantités <b>réservées</b> en stock pour honorer le transfert par lot.</p>
<p>Cliquez sur le bouton <b>Vérifier la disponibilité</b> pour rechercher à nouveau les produits disponibles dans le stock.</p>
<img alt="Afficher les quantités réservées non disponibles dans l'onglet *Opérations*." class="align-center" src="../../../../../_images/operations-tab.png"/>
</div>

### Créer un reliquat

Sur le formulaire de transfert par lot, si la quantité **faite** du produit
est _inférieure_ à la quantité **réservée** , une fenêtre contextuelle
s’ouvre.

Cette fenêtre contextuelle propose l’option : **Créer un reliquat ?**.

Si vous cliquez sur le bouton **Créer un reliquat** , un nouveau lot est
automatiquement créé, contenant les produits restants.

Cliquez sur **Aucun reliquat** pour terminer le transfert _sans_ créer un
autre transfert par lot.

Cliquez sur **Ignorer** pour annuler la validation et revenir au formulaire de
transfert par lot.

![Afficher la fenêtre contextuelle *Créer un
reliquat*.](../../../../../_images/create-backorder.png)

## Traiter le transfert par lot : l’application Code-barres

Les transferts par lot créés sont également répertoriés dans l’application
Code-barres, accessible en cliquant sur le bouton **Transferts par lot**.

Par défaut, les transferts par lot confirmés apparaissent sur la page des
**Transferts par lot**. Sur cette page, cliquez sur le transfert par lot
souhaité pour ouvrir une liste détaillée des produits à transférer.

![Afficher la liste des transferts par lot à effectuer dans l'application
*Code-barres*.](../../../../../_images/barcode-batch-transfers.png)

Pour le transfert par lot choisi, suivez les instructions en haut de la page
sur fond noir. Commencez par scanner le code-barres du produit pour
enregistrer un seul produit à transférer. Pour enregistrer des quantités
multiples, cliquez sur l’icône **✏️ (crayon)** et saisissez les quantités
requises pour le transfert.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les produits du même ordre sont libellés de la même couleur à gauche. Les transferts complétés sont surlignés en vert.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Dans un transfert par lot pour 2 <code>Armoires avec portes</code>, 3 <code>Écrans anti-bruit</code>, et 4 <code>Bureaux de quatre personnes</code>, les <b>Unités</b> <code>3/3</code> et <code>4/4</code> indiquent que les deux derniers transferts de produits sont terminés.</p>
<p><code>1/2</code> unité de l”<code>Armoire avec portes</code> a déjà été transféré et après avoir scanné le code-barres du produit pour la deuxième armoire, Konvergo ERP invite l’utilisateur à <code>Scanner un numéro de série</code> pour enregistrer le numéro de série unique à des fins de <a href="../../product_management/product_tracking/serial_numbers#inventory-serial-numbers-configure"><span class="std std-ref">suivi de produits</span></a>.</p>
<img alt="Afficher les produits à transférer dans la vue Code-barres." class="align-center" src="../../../../../_images/barcode-products.png"/>
</div>

Une fois tous les produits transférés, cliquez sur **Valider** pour marquer le
transfert par lot comme **Fait**.

