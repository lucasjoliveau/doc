# Traiter des réceptions et des livraisons en deux étapes

Selon les processus commerciaux d’une entreprise, plusieurs étapes peuvent
être nécessaires avant de recevoir ou expédier des produits. Dans le processus
de réception en deux étapes, les produits sont reçus dans une zone d’entrée,
puis transférés dans le stock. Les réceptions en deux étapes fonctionnent
mieux lorsque plusieurs emplacements de stockage sont utilisés, tels que des
zones fermées ou sécurisées, des congélateurs et des réfrigérateurs ou
diverses étagères.

Les produits peuvent être triés en fonction de l’endroit où ils seront stockés
et les employés peuvent stocker tous les produits destinés à un endroit
spécifique. Les produits ne sont pas disponibles pour être traités
ultérieurement tant qu’ils n’ont pas été transférés dans le stock.

Dans le processus de livraison en deux étapes, les produits qui font partie
d’un bon de commande sont prélevés dans l’entrepôt en fonction de leur
stratégie d’enlèvement et acheminés vers un emplacement de sortie avant d’être
expédiés.

Une situation où cela peut être utile est lorsque l’on utilise les stratégies
d’enlèvement FIFO, LIFO ou FEFO, où les produits qui sont prélevés doivent
être sélectionnés en fonction de leur date de réception ou d’expiration.

Konvergo ERP est configuré par défaut pour [recevoir et livrer des marchandises en une
étape](receipts_delivery_one_step#inventory-receipts-delivery-one-step),
donc il faut modifier le paramètre pour utiliser les réceptions et livraisons
en deux étapes. Les réceptions et les expéditions n’ont pas besoin d’être
configurées pour avoir les mêmes étapes. Par exemple, les produits peuvent
être reçus en deux étapes, mais expédiés en une étape. Dans l’exemple suivant,
deux étapes seront utilisées pour les réceptions et les livraisons.

## Configurer des routes en plusieurs étapes

Assurez-vous d’abord que l’option **Routes en plusieurs étapes** est activée
dans Inventaire ‣ Configuration ‣ Paramètres, dans la section **Entrepôt**.
Après avoir activé le paramètre, **enregistrez** les changements.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’activation du paramètre <b>Routes en plusieurs étapes</b> activera également la fonctionnalité des <b>Emplacements de stockage</b>.</p>
</div> ![Activez les routes en plusieurs étapes et les
emplacements de stockage dans les paramètres
d'inventaire.](../../../../../_images/multi-step-routes1.png)

Ensuite, l’entrepôt doit être configuré pour les réceptions et livraisons en
deux étapes. Allez à Inventaire ‣ Configuration ‣ Entrepôts et cliquez sur
l’entrepôt pour modifier les paramètres de celui-ci.

Sélectionnez ensuite **Décharger dans l’emplacement d’entrée puis aller en
stock (2 étapes)** pour les **Réceptions** , et **Amener les marchandises à
l’emplacement de sortie et ensuite livrer (2 étapes)** pour les
**Expéditions**.

![Définissez les options de réception et d'expédition sur recevoir et livrer
en deux étapes.](../../../../../_images/two-step-warehouse-config.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>En activant les réceptions et les livraisons en deux étapes, de nouveaux emplacements d”<em>entrée</em> et de <em>sortie</em>, libellés par défaut respectivement <b>WH/Input</b> et <b>WH/Output</b> sont créés dans le tableau de bord des <b>Emplacements</b>. Pour renommer ces emplacements, allez à Configuration ‣ Emplacements et sélectionnez l”<b>Emplacement</b> à modifier. Sur le formulaire de l’emplacement, mettez à jour le <b>Nom de l’emplacement</b> et faites les autres modifications (le cas échéant).</p>
</div>

## Traiter une réception en deux étapes (Emplacement d’entrée + stock)

### Créer un bon de commande

Sur le tableau de bord principal de l’application Achats, commencez par faire
un nouveau devis en cliquant sur **Nouveau**. Ensuite, sélectionnez (ou créez)
un **Fournisseur** dans le champ déroulant, ajoutez un **Produit** stockable
aux lignes de commande et cliquez sur **Confirmer la commande** pour finaliser
le devis et le transformer en bon de commande.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour les entreprises ayant plusieurs entrepôts avec des configurations d’étapes différentes, le champ <b>Livrer à</b> sur le bon de commande peut avoir besoin d’être précisé comme l”<em>emplacement d’entrée</em> correct lié à l’entrepôt en deux étapes. Pour ce faire, sélectionnez l’entrepôt dans la liste déroulante qui comprend le libellé <code>Réceptions</code> à la fin du nom.</p>
</div>

Après avoir confirmé le bon de commande, un bouton intelligent **Réception**
apparaît en haut du bon de commande — en cliquant dessus, la réception
associée au bon de commande s’affiche.

![Après avoir confirmé un bon de commande, un bouton intelligent Réception
apparaîtra.](../../../../../_images/two-step-po-receipt.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez également trouver les réceptions des bons de commande dans l’application Inventaire, cliquez sur le bouton intelligent <b># à traiter</b> sur la carte kanban <b>Réceptions</b>.</p>
<img alt="Une réception prête à être traitée dans la vue kanban de l'aperçu du stock." class="align-center" src="../../../../../_images/two-step-receipts-kanban.png"/>
</div>

### Traiter la réception

La réception et le transfert interne seront créés une fois le bon de commande
confirmé. Le statut de la réception sera **Prêt** , puisque la réception doit
être traitée en premier lieu. Le statut du transfert interne sera **En attente
d’une autre opération** , puisque le transfert ne peut pas avoir lieu avant
que la réception ne soit finalisée. Le statut du transfert interne ne passe à
**Prêt** que lorsque la réception aura été marquée comme **Fait**.

Cliquez sur la **Réception** associée au bon de commande, puis cliquez sur
**Valider** pour finaliser la réception et déplacer le produit vers
l”**Emplacement d’entrée**.

![Validez la réception en cliquant sur Valider et le produit sera transféré
vers WH/Emplacement d'entrée.](../../../../../_images/validate-two-step-
receipt.png)

### Traiter le transfert interne

Une fois le produit se trouve à l”**Emplacement d’entrée** , le transfert
interne est prêt à déplacer le produit dans le stock. Allez à l’application
Inventaire et sur le tableau de bord **Aperçu du stock** , cliquez sur le
bouton intelligent **# à traiter** sur la carte kanban des **Transferts
internes**.

![Un transfert interne prêt à être traité dans la vue kanban de l'aperçu du
stock.](../../../../../_images/transfer-two-step-kanban.png)

Cliquez sur le **Transfert** associé au bon de commande, puis cliquez sur
**Valider** pour finaliser la réception et déplacer le produit dans le stock.
Une fois le transfert validé, le produit entre dans le stock et est disponible
pour les livraisons aux clients et les ordres de fabrication.

![Validez le transfert interne pour déplacer l'article dans le
stock.](../../../../../_images/two-step-validate-transfer.png)

## Traiter un bon de livraison en deux étapes (transfert + expédition)

### Créer une commande client

Dans l’application Ventes, créez un nouveau devis en cliquant sur **Nouveau**.
Sélectionnez (ou créez) un **Client** , ajoutez un **Produit** stockable aux
lignes de commande et cliquez sur **Confirmer**.

Après avoir confirmé la commande client, un bouton intelligent **Livraison**
apparaît en haut, au dessus de la commande. En cliquant sur le bouton
intelligent **Livraison** , le bon de livraison associé à la commande
s’affiche.

![Après avoir confirmé la commande, le bouton intelligent Livraison apparaît
et affiche les deux articles qui y sont associés.](../../../../../_images/two-
step-sales-quote.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez également trouver les reçus de commande dans l’application Inventaire. Dans le tableau de bord <b>Aperçu</b>, cliquez sur le bouton intelligent <b># à traiter</b> sur la carte kanban <b>Pick</b>.</p>
<img alt="Le bon de transfert se trouve dans la vue kanban de l'Inventaire." class="align-center" src="../../../../../_images/two-step-pick-kanban.png"/>
</div>

### Traiter le transfert

Les bons de transfert et de livraison seront créés une fois la commande
confirmée. Lorsque le bouton intelligent **Livraison** apparaît, cliquez
dessus pour accéder au tableau de bord des **Transferts** , qui répertorie
tous les bons de transfert et de livraison.

Le statut du transfert sera **Prêt** , puisque le produit doit être prélevé du
stock avant qu’il puisse être expédié. Le statut du bon de livraison sera **En
attente d’une autre opération** , puisque la livraison ne peut avoir lieu
qu’après le transfert. Le statut du bon de livraison ne passera à **Prêt** que
lorsque le transfert aura été marqué comme **Fait**.

![Le statut est prêt pour l'opération de transfert, alors que l'opération de
livraison est En attente d'une autre opération.](../../../../../_images/two-
step-status.png)

Cliquez sur le bon de transfert pour commencer à le traiter. Si le produit est
en stock, Konvergo ERP réservera automatiquement le produit. Cliquez sur **Valider**
pour marquer le transfert comme **Fait** et le bon de livraison sera prêt à
être traité. Puisque les documents sont liés, les produits qui ont été
prélevés précédemment sont automatiquement réservés sur le bon de livraison.

![Validez le transfert en cliquant sur
Valider.](../../../../../_images/validate-two-step-pick.png)

### Traiter la livraison

Le bon de livraison sera prêt à être traité une fois le transfert terminé et
peut être trouvé dans l’application Inventaire dans le tableau de bord
**Aperçu du stock**. Cliquez sur le bouton intelligent **# à traiter** sur la
carte kanban **Bons de livraison** pour commencer.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est également possible d’accéder rapidement au bon de livraison associé à la commande en cliquant à nouveau sur le bouton intelligent <b>Livraison</b> et en choisissant le bon de livraison sur le page des <b>Transferts</b> (qui devrait être marqué comme <b>Prêt</b>).</p>
</div> ![Le bon de livraison se trouve dans la vue kanban de
l'Inventaire.](../../../../../_images/deliver-two-step-kanban.png)

Cliquez sur le bon de livraison associé à la commande et cliquez sur
**Valider** pour finaliser le transfert.

![Cliquez sur Valider sur le bon de livraison pour transférer le produit de
l'emplacement de sortie vers l'emplacement
client.](../../../../../_images/validate-two-step-delivery.png)

Une fois le bon de livraison validé, le produit quitte l’emplacement
**WH/Output** dans le tableau de bord des **Transferts** et se déplace vers
l’emplacement **Partners/Customers**. Ensuite, le statut du document passe à
**Fait**.

  *[FIFO]: First In, First Out
  *[LIFO]: Last In, First Out
  *[FEFO]: First Expired, First Out

