# Traiter des livraisons en trois étapes

Certaines entreprises traitent chaque jour un grand nombre de livraisons, dont
beaucoup comprennent plusieurs produits ou nécessitent un emballage spécial.
Pour que cela soit efficace, une étape de colisage est nécessaire avant
d’expédier les produits. Konvergo ERP propose donc un processus de livraison des
marchandises en trois étapes.

Dans le processus de livraison en trois étapes par défaut, les produits qui
font partie d’un bon de livraison sont prélevés dans l’entrepôt en fonction de
leur stratégie d’enlèvement et acheminés vers une zone de colisage. Après que
les articles sont emballés dans les différents colis dans la zone de colisage,
ils sont acheminés vers un emplacement de sortie avant d’être expédiés. Ces
étapes ne peuvent pas être modifiées si elles ne correspondent pas aux besoin
de l’entreprise.

## Configuration

Konvergo ERP est configuré par défaut pour [recevoir et livrer des marchandises en une
étape](receipts_delivery_one_step#inventory-receipts-delivery-one-step),
donc il faut modifier les paramètres pour pouvoir utiliser les livraisons en
trois étapes. Assurez-vous d’abord que l’option _Routes en plusieurs étapes_
est activée dans Inventaire ‣ Configuration ‣ Paramètres ‣ Entrepôt. Notez que
l’activation de l’option **Routes en plusieurs étapes** activera également les
_Emplacements de stockage_.

![Activez les routes en plusieurs étapes et les emplacements de stockage dans
les paramètres d'inventaire.](../../../../../_images/multi-step-routes.png)

Next, the warehouse needs to be configured for three step deliveries. To do
this, go to Inventory app ‣ Configuration ‣ Warehouses, and click on the
**warehouse** to edit. Then, select **Pack goods, send goods in output and
then deliver (3 steps)** for **Outgoing Shipments**.

![Définissez l'option d'expédition sur livrer en trois
étapes.](../../../../../_images/three-step-warehouse-config.png)

Activating three-step receipts and deliveries creates two new internal
locations: a _Packing Zone_ (WH/Packing Zone), and _Output_ (WH/Output). To
rename these locations, go to Inventory app ‣ Configuration ‣ Locations, click
on the **Location** to change, and update the name.

## Deliver in three steps (pick + pack + ship)

### Créer une commande client

To create a new quote, navigate to Sales app ‣ Create, which reveals a blank
quotation form. On the blank quotation form, select a **Customer** , add a
storable **Product** , and click **Confirm**.

A **Delivery** smart button appears in the top right of the quotation form.
Clicking it shows the picking order, packing order, and the delivery order
associated with the sales order.

![Après avoir confirmé la commande, le bouton intelligent Livraison apparaît
et affiche les trois articles qui y sont
associés.](../../../../../_images/three-step-delivery-so.png)

### Traiter un transfert

Les bons de transfert, de colisage et de livraison sont créés une fois la
commande confirmée. Pour visualiser ces transferts, allez à Inventaire ‣
Opérations ‣ Transferts.

![Le statut est prêt pour l'opération de transfert, alors que les opérations
de colisage et de livraison sont en attente d'une autre
opération.](../../../../../_images/three-step-delivery-transfers.png)

Le statut du transfert sera **Prêt** , puisque le produit doit être prélevé du
stock avant qu’il puisse être emballé. Le statut des bons de colisage et de
livraison sera **En attente d’une autre opération** , puisque le colisage et
la livraison ne peuvent avoir lieu qu’après le transfert. Le statut du bon de
livraison ne passera à **Prêt** que lorsque le colisage aura été marqué comme
**Fait**.

Vous pouvez également trouver la réception dans l’application _Inventaire_.
Dans le tableau de bord **Aperçu** , cliquez sur le bouton intelligent **1 à
traiter** sur la carte kanban **Pick**.

![Le bon de transfert se trouve dans la vue kanban de
l'Inventaire.](../../../../../_images/three-step-kanban-pick.png)

Cliquez sur le transfert à traiter. Si le produit est en stock, Konvergo ERP réservera
automatiquement le produit. Cliquez sur **Valider** pour marquer le transfert
comme fait et finalisez le transfert vers la **Zone de colisage**. Le bon de
colisage sera ensuite prêt. Puisque les documents sont liés, les produits qui
ont été transférés précédemment sont automatiquement réservés sur le bon de
colisage.

![Validez le transfert en cliquant sur
Valider.](../../../../../_images/validate-three-step-pick.png)

### Traiter un colisage

Le bon de colisage sera prêt à être traité une fois que le prélèvement est
finalisé et peut être trouvé dans le tableau de bord **Aperçu** de
l’application Inventaire. Cliquez sur le bouton intelligent **1 à traiter**
sur la carte kanban **Pack**.

![Le bon de colisage se trouve dans la vue kanban de
l'inventaire.](../../../../../_images/three-step-kanban-pack.png)

Cliquez sur le bon de colisage associé à la commande et cliquez sur
**Valider** pour finaliser le colisage.

![Cliquez sur Valider sur le bon de colisage pour transférer le produit de la
zone de colisage vers l'emplacement de
sortie.](../../../../../_images/validate-three-step-pack.png)

Une fois le bon de colisage validé, le produit quitte l’emplacement
**WH/Packing Zone** et se déplace vers l’emplacement **WH/Output**. Ensuite,
le statut du document passe à **Fait**.

### Traiter une livraison

Le bon de livraison sera prêt à être traité une fois le colisage finalisé et
peut être trouvé dans le tableau de bord **Aperçu** de l’application
Inventaire. Cliquez sur le bouton intelligent **1 à traiter** sur la carte
kanban **Bons de livraison**.

![Le bon de livraison se trouve dans la vue kanban des Bons de
livraisons.](../../../../../_images/three-step-kanban-delivery.png)

Cliquez sur le bon de livraison associé à la commande et cliquez sur
**Valider** pour finaliser le transfert.

![Cliquez sur Valider sur le bon de livraison pour transférer le produit de
l'emplacement de sortie vers l'emplacement
client.](../../../../../_images/three-step-delivery-out.png)

Une fois le bon de livraison validé, le produit quitte l’emplacement
**WH/Output** et se déplace vers l’emplacement **Partners/Customers**.
Ensuite, le statut du document passe à **Fait**.

