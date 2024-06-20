# Gérer des commandes

Lorsqu’un client passe une commande auprès de votre eCommerce, **trois** types
d’enregistrements nécessaires doivent être gérés dans Odoo :

  * Bons de commande ;

  * Bons de livraison ;

  * Factures & exigences légales.

## Bons de commande

### Statut de la commande et du paiement

La première chose à faire lorsqu’un client ajoute un produit à son panier est
de créer un devis. Il est possible de gérer les commandes à partir de
l’application **Site Web** ou [Ventes](../../../sales/sales.html). Les
commandes eCommerce peuvent être assignées automatiquement à une équipe
commerciale spécifique en allant à Site Web ‣ Configuration ‣ Paramètres. Dans
la section **Boutique - Processus de paiement** , sélectionnez une Équipe
commerciale ou un Vendeur pour gérer les commandes eCommerce.

![Assignation des commandes en ligne à une équipe commerciale ou un
vendeur](../../../../_images/handling-salesteam.png)

Vous pouvez trouver les commandes dans Site Web ‣ eCommerce ‣
Commandes/Commandes non payées. Chaque commande passe par un statut différent
:

  * **Devis** : un nouveau produit est ajouté au panier, mais le client n’a _pas_ encore procédé au paiement ;

  * **Devis envoyé** : le client a procédé au paiement et a confirmé la commande, mais le paiement n’est pas encore confirmé ;

  * **Commande** : le client a procédé au paiement, confirmé la commande et le paiement est reçu.

![Statuts des commandes eCommerce](../../../../_images/handling-status.png)

### Paniers abandonnés

Un **panier abandonné** représente une commande pour laquelle le client **n’a
pas terminé** le processus de paiement. Pour ces commandes, il est possible
d’envoyer automatiquement un **rappel par email** au client. Pour activer
cette fonctionnalité, allez à Site Web ‣ Configuration ‣ Paramètres et dans la
section Email & Marketing, activez Envoyer automatiquement des emails en cas
de paiement abandonné. Une fois cette option activée, vous pouvez définir le
**laps de temps** après lequel l’email est envoyé et vous pouvez personnaliser
le **modèle d’email** utilisé.

Note

En ce qui concerne les emails envoyés en cas de panier abandonné, le client
doit avoir donné ses coordonnées pendant le processus de paiement ou il doit
être connecté quand il a ajouté le produit à son panier.

## Bons de livraison

### Flux de livraison

Une fois qu’un devis a été confirmé, un bon de livraison est créé
automatiquement. La prochaine étape consiste à procéder à la livraison.

L’emballage des commandes eCommerce demande également le transfert du produit,
la préparation du colisage, l’impression de la ou des étiquettes d’expédition
et l’expédition au client. En fonction du nombre de commandes, de la stratégie
ou des ressources, ces étapes peuvent être considérées comme une ou plusieurs
actions dans Odoo.

Un email automatique peut être envoyé au client lorsque le statut du transfert
dans Odoo est « fait ». Pour ce faire, activez la fonctionnalité dans les
paramètres de l’application
[Inventaire](../../../inventory_and_mrp/inventory.html).

Note

Si les clients sont autorisés à payer lors du retrait de leur commande en
boutique ou par virement bancaire, le devis n’est **pas** confirmé et le stock
n’est **pas** réservé. Les commandes doivent être confirmées manuellement pour
réserver des produits en stock.

Pour plus d'infos

  * [Shipping cost invoicing](../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing.html)

  * [Print shipping labels](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels.html)

  * [Expédition de plusieurs colis](../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack.html)

### Retours et remboursements

Les clients ne peuvent retourner une commande que par l’intermédiaire d’un
formulaire en ligne. Il se peut qu’il ne soit pas possible de retourner des
produits en fonction de la stratégie de retour ou du type de produit.

Les remboursements intégraux peuvent être envoyés directement aux clients à
partir de l’interface de commande. Un fournisseur de paiement compatible avec
les remboursements doit d’abord être activé.

Pour plus d'infos

  * [Retours et remboursements](../../../sales/sales/products_prices/returns.html)

  * [Services après-vente](../../../services/helpdesk/advanced/after_sales.html)

  * [Paiements en ligne](../../../finance/payment_providers.html)

## Facture et exigences légales

La dernière étape d’une commande eCommerce consiste à générer la facture et à
l’envoyer au client. En fonction du type d’entreprise (B2B ou B2C), une
facture peut être générée automatiquement (B2B) ou à la demande du client
(B2C). Ce processus peut être automatisé si (et quand) le paiement en ligne
est confirmé.

Pour automatiser la facturation, allez à Site Web ‣ Configuration ‣ Paramètres
et dans la section Facturation, activez la fonctionnalité Facture automatique.

