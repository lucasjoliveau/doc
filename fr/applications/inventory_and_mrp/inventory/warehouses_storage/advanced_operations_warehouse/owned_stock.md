# Consignation : acheter et vendre du stock sans le posséder

La plupart du temps, les produits stockés dans l’entrepôt d’une entreprise
sont soit achetés à des fournisseurs, soit fabriqués en interne. Cependant,
les fournisseurs permettent parfois aux entreprises de stocker et de vendre
des produits dans leur entrepôt, sans avoir à acheter ces articles au
préalable. C’est ce qu’on appelle la _consignation_.

La consignation est un moyen utile pour les fournisseurs de lancer de nouveaux
produits et de les livrer facilement à leurs clients. C’est également un
excellent moyen pour l’entreprise qui stocke les produits (le consignataire)
de gagner quelque chose en retour pour ses efforts. Les consignataires peuvent
même facturer des frais pour la commodité du stockage des produits qu’ils ne
possèdent pas réellement.

## Activer le paramètre Consignation

Pour recevoir, stocker et vendre des produits en consignation, la
fonctionnalité doit être activée dans les paramètres. Pour ce faire, allez à
Inventaire ‣ Configuration ‣ Paramètres et dans la section **Traçabilité** ,
cochez la case à côté de **Consignation** et cliquez ensuite sur
**Enregistrer** pour terminer.

![Le paramètre de consignation activé dans la configuration
d'Inventaire.](../../../../../_images/owned-stock-enable-consignment.png)

## Recevoir (et stocker) des produits en consignation

Une fois la fonctionnalité activée dans Konvergo ERP, les produits en consignation
peuvent désormais être réceptionnés dans un entrepôt. À partir du tableau de
bord principal d”Inventaire, cliquez sur **Réceptions** et cliquez sur
**Créer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le stock en consignation n’est pas réellement acheté au fournisseur ; il est simplement réceptionné et stocké. C’est pourquoi la réception de produits en consignation n’implique ni devis, ni bon de commande. Par conséquent, <em>chaque</em> réception de stock en consignation commencera par la création de réceptions manuelles.</p>
</div>

Choisissez un fournisseur à saisir dans le champ **Recevoir de** et choisissez
ensuite le même fournisseur à saisir dans le champ **Assigner un
propriétaire**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Puisque les produits reçus du fournisseur appartiennent au même fournisseur, les champs <b>Recevoir de</b> et <b>Assigner un propriétaire</b> doivent correspondre.</p>
</div>

Une fois que les champs liés au fournisseurs sont complétés, saisissez les
produits dans les lignes **Produit** et définissez les quantités à recevoir
dans l’entrepôt dans la colonne **Fait**. Si la fonctionnalité **Unité de
mesure** est activée, l”UdM peut également être modifiée. Une fois que le
stock en consignation a été reçu, **validez** la réception.

![Correspondance des champs des fournisseurs lors de la création d'une
réception de produits en consignation.](../../../../../_images/owned-stock-
receipt-fields.png)

## Vendre et livrer un stock en consignation

Une fois que le stock en consignation a été reçu dans l’entrepôt, il peut être
vendu de la même manière que tout autre produit en stock pour lequel l’option
**Peut être vendu** est activée sur la fiche produit.

Pour créer une commande, allez à l’application Ventes et, dans la vue
d’ensemble des **Devis** , cliquez sur **Créer**. Ensuite, choisissez un
client à saisir dans le champ **Client**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le <b>Client</b> <em>doit</em> être différent du <b>Fournisseur</b> qui a fourni le stock en consignation reçu (et stocké) dans l’entrepôt.</p>
</div>

Ajoutez le produit en consignation dans la colonne **Produit** des lignes de
commande, définissez la **Quantité** et complétez tous les autres détails
pertinents sur le produit dans le formulaire. Une fois le devis terminé,
cliquez sur **Confirmer**.

![Commande d'un stock en consignation](../../../../../_images/owned-stock-
sales-order.png)

Une fois la demande de prix confirmée, elle se transforme en commande. À
partir de là, les produits peuvent être livrés en cliquant sur le bouton
intelligent **Livraison** et en sélectionnant **Valider** pour confirmer la
livraison.

## Traçabilité et analyse du stock en consignation

Même si le stock en consignation appartient au vendeur qui l’a fourni et non à
l’entreprise qui le stocke dans son entrepôt, les produits en consignation
apparaîtront _tout de même_ dans certains rapports d’inventaire.

Pour trouver les rapports d’inventaire, allez à Inventaire ‣ Analyse et
choisissez un rapport à afficher.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Puisque le consignataire ne possède pas réellement le stock en consignation, ces produits ne figurent <em>pas</em> dans le rapport de <b>Valorisation de stock</b> et n’ont aucun impact sur la valorisation des stocks du consignataire.</p>
</div>

### Rapport sur les mouvements de produits

Pour afficher toutes les informations relatives aux mouvements de stock, allez
au tableau de bord des **Mouvements de produits** en allant à Inventaire ‣
Analyse ‣ Mouvements de stock. En ce qui concerne les produits en
consignation, les informations contenues dans ce rapport sont les mêmes que
pour tout autre produit : l’historique des mouvements de produits peut être
consulté ; la **quantité faite** et le document de **référence** sont
disponibles, de même que ses **Emplacements**. Le stock en consignation
provient de l”**Emplacement partenaire/fournisseur**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour afficher les mouvements d’un produit en consignation par propriétaire, sélectionnez le filtre <b>Regrouper par</b>, choisissez le paramètre <b>Ajouter un groupe personnalisé</b> et sélectionnez ensuite <b>Propriétaire</b> et <b>Appliquer</b> pour terminer.</p>
</div> ![Historique des mouvements d'un stock en
consignation.](../../../../../_images/owned-stock-moves-history.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour voir les unités prévues du stock en consignation, allez à Inventaire ‣ Analyse ‣ Inventaire planifié.</p>
</div>

### Rapport sur le stock disponible

Affichez le tableau de bord du **Stock disponible** en allant à Inventaire ‣
Analyse ‣ Rapport d’inventaire. Ce rapport affiche les **Emplacements** de
tous les stocks disponibles, ainsi que les quantités par emplacement. Pour les
produits en consignation, la colonne **Propriétaire** sera remplie par le
propriétaire de ces produits ou par le fournisseur initial qui a fourni les
produits en premier lieu.

  *[UdM]: Unité de mesure

