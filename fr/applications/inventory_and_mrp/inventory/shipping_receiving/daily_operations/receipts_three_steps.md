# Traiter des réceptions en trois étapes

Certaines entreprises procèdent au contrôle qualité avant de recevoir les
marchandises des fournisseurs. Pour ce faire, Konvergo ERP propose un processus de
réception des marchandises en trois étapes.

Dans le processus de réception en trois étapes, les produits sont reçus dans
une zone d’entrée, puis transférés dans une zone de contrôle qualité. Les
produits qui passent le contrôle de qualité sont ensuite transférés dans le
stock. Les produits ne sont pas disponibles pour traitement ultérieur tant
qu’ils n’ont pas été transférés de la zone de contrôle qualité vers le stock.

## Configuration

Konvergo ERP est configuré par défaut pour [recevoir et livrer des marchandises en une
étape](receipts_delivery_one_step#inventory-receipts-delivery-one-step),
donc il faut modifier le paramètre pour pouvoir utiliser les réceptions en
trois étapes. Assurez-vous d’abord que l’option _Routes en plusieurs étapes_
est activée dans Inventaire ‣ Configuration ‣ Paramètres ‣ Entrepôt. Notez que
l’activation de l’option **Routes en plusieurs étapes** activera également les
_Emplacements de stockage_.

![Activez les routes en plusieurs étapes et les emplacements de stockage dans
les paramètres d'inventaire.](../../../../../_images/multi-step-routes2.png)

Next, the warehouse needs to be configured for three-step receipts. To do
that, go to Inventory app ‣ Configuration ‣ Warehouses, and select the desired
warehouse to be edited. Doing so reveals the detail form for that specific
warehouse.

On that **Warehouse** detail form page, select **Receive goods in input, then
quality and then stock (3 steps)** for **Incoming Shipments**.

![Définissez l'option de réception sur recevoir en trois
étapes.](../../../../../_images/three-step-receipt-settings.png)

Activating three-step receipts and deliveries creates two new internal
locations: _Input_ (WH/Input), and _Quality Control_ (WH/Quality Control). To
rename these locations, go to Inventory app ‣ Configuration ‣ Locations, then
click on the desired location to change (or update) the name.

## Receive in three steps (input + quality + stock)

### Créer un bon de commande

To create a new RfQ, navigate to Purchase app ‣ New, which reveals a blank RfQ
form page. On this page, select a **Vendor** , add a storable **Product** ,
and click **Confirm Order**.

Un bouton intelligent **Réception** apparaîtra dans le coin supérieur droit et
la réception sera associée au bon de commande. Le fait de cliquer sur le
bouton intelligent **Réception** affichera l’ordre de réception.

![Après avoir confirmé un bon de commande, un bouton intelligent Réception
apparaîtra.](../../../../../_images/three-step-purchase-receipt.png)

### Traiter une réception

Une réception et deux transferts internes (un transfert vers le contrôle
qualité et un transfert subséquent vers le stock) seront créés une fois que le
bon de commande est confirmé. Pour visualiser ces transferts, allez à
Inventaire ‣ Opérations ‣ Transferts.

![Le statut des trois transferts de réception indique les opérations prêtes et
celles en attente d'une autre opération. ](../../../../../_images/three-step-
transfers.png)

Le statut de la réception transférant le produit vers l’emplacement d’entrée
sera **Prêt** , puisque la réception doit être traitée avant toute autre
opération. Le statut des deux transferts internes est **En attente d’une autre
opération** , car les transferts ne peuvent pas être traités tant que l’étape
associée précédant chaque transfert n’est pas terminée.

Le statut du premier transfert interne vers le _contrôle qualité_ ne passera à
**Prêt** que lorsque la réception a été marquée comme **Fait**. Le statut du
second transfert interne vers le _stock_ ne passera à **Prêt** que lorsque le
transfert vers le contrôle qualité aura été marqué comme **Fait**.

Vous pouvez également trouver la réception dans l’application Inventaire. Dans
le tableau de bord **Aperçu** , cliquez sur le bouton intelligent **1 à
traiter** sur la carte kanban **Réceptions**.

![Une réception prête à être traitée dans la vue kanban de l'aperçu du
stock.](../../../../../_images/three-step-receive-kanban.png)

Cliquez sur la réception associée au bon de commande, cliquez ensuite sur
**Valider** pour finaliser la réception et déplacer le produit vers
l”**Emplacement d’entrée**.

![Validez la réception en cliquant sur Valider et le produit sera transféré
vers WH/Contrôle qualité.](../../../../../_images/validate-three-step-
receipt.png)

### Traiter un transfert vers le contrôle qualité

Une fois que le produit se trouve à l”**Emplacement d’entrée** , le transfert
interne est prêt à déplacer le produit vers le **Contrôle qualité**. Dans le
tableau de bord **Aperçu** de l”Inventaire, cliquez sur le bouton intelligent
**1 à traiter** sur la carte kanban des **Transferts internes**.

![Un transfert interne prêt à être traité dans la vue kanban de l'aperçu du
stock.](../../../../../_images/three-step-quality-transfer.png)

Cliquez sur le **Transfert** associé au bon de commande, cliquez sur
**Valider** pour finaliser le transfert et déplacez le produit vers
l’emplacement de **Contrôle qualité**. Une fois le transfert validé, le
produit est prêt pour le contrôle qualité, mais n’est pas disponible pour les
ordres de fabrication ou les bons de livraison.

![Validez le transfert interne pour déplacer l'article vers l'emplacement de
contrôle qualité.](../../../../../_images/validate-three-step-quality-
move.png)

## Traiter un transfert vers le stock

Une fois que le produit se trouve à l’emplacement de **Contrôle qualité** , le
transfert interne final est prêt à déplacer le produit vers le **Stock**. Dans
le tableau de bord aperçu de l”**Inventaire** , cliquez sur le bouton
intelligent **1 à traiter** sur la carte kanban des **Transferts internes**.

Cliquez sur le **Transfert** final associé au bon de commande, cliquez sur
**Valider** pour finaliser le transfert et déplacez le produit vers le stock.
Une fois le transfert validé, le produit entre dans le stock et est disponible
pour les livraisons aux clients ou les ordres de fabrication.

  *[RfQ]: Request for Quotation

