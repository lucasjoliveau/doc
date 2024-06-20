# Point de Vente

Gérez facilement vos boutiques et restaurants avec **Odoo Point de Vente**.
L’application fonctionne sur tout appareil ayant un navigateur web, même si
vous êtes temporairement hors ligne. Les mouvements de produit sont
automatiquement enregistrés dans votre stock, vous obtenez des statistiques en
temps réel et vos données sont consolidées à travers toutes les boutiques.

Pour plus d'infos

  * [Tutoriels Odoo : Tutoriels sur les points de vente](https://www.odoo.com/slides/point-of-sale-28)

  * [IoT Boxes Documentations](../general/iot.html)

## Démarrer une session

À partir du **tableau de bord du PdV** , cliquez sur Nouvelle session et sur
l’écran Contrôle des espèces à l’ouverture, cliquez sur Ouvrir la session pour
commencer une session du PdV ou cliquez sur Continuer la vente si la session
est déjà ouverte.

Note

[Plusieurs utilisateurs](point_of_sale/employee_login.html) peuvent être
connectés à la même session en même temps. Cependant, la session ne peut être
ouverte qu’une seule fois dans le même navigateur.

## Vendre des produits

Cliquez sur des produits pour les ajouter au panier. Pour changer la
**quantité** , cliquez sur Qté et saisissez le nombre de produits à l’aide du
clavier. Pour ajouter une **remise** ou modifier le **prix** du produit,
cliquez respectivement sur % de remise ou Prix et saisissez les montants.

Une fois la commande complétée, passez à la caisse en cliquant sur Paiement.
Sélectionnez le **mode de paiement** , saisissez le montant reçu, puis cliquez
sur Valider. Cliquez sur Nouvelle commande pour aider le client suivant.

![Interface d'une session du PdV.](../../_images/pos-interface.png)

Astuce

  * Vous pouvez utiliser à la fois `,` et `.` sur votre clavier comme séparateurs décimaux.

  * L’option **Cash** est sélectionnée par défaut si vous saisissez le montant sans choisir le mode de paiement.

Note

The system can only load a limited number of products for effective opening.
Click Search more if the desired product is not loaded automatically.

## Définir les clients

Il est nécessaire d’enregistrer votre client pour [collecter ses points de
fidélité et lui accorder des récompenses](point_of_sale/pricing/loyalty.html),
appliquer automatiquement la [liste de prix
attribuée](point_of_sale/pricing/pricelists.html), ou [générer et imprimer une
facture](point_of_sale/receipts_invoices.html#receipts-invoices-invoices).

Vous pouvez créer des clients à partir d’une session PdV ouverte en cliquant
sur Client ‣ Créer, et en remplissant les informations de contact. Vous pouvez
également créer des clients à partir du backend en allant au Point de Vente ‣
Commandes ‣ Clients et en cliquant sur Nouveau. Remplissez ensuite les
informations et enregistrez.

Pour définir un client pendant une commande, accédez à la liste des clients en
cliquant sur Client sur l’interface du point de vente. Vous pouvez également
définir un client sur l’écran de paiement en cliquant sur Client.

## Notes au client

Vous pouvez ajouter des **notes au client** sur des produits spécifiques
directement à partir d’une session PdV ouverte. Par exemple, des conseils de
nettoyage et d’entretien. Elles peuvent également être utilisées pour suivre
la demande particulière d’un client, par exemple s’il ne souhaite pas que le
produit soit assemblé pour lui.

Pour ce faire, sélectionnez un produit et cliquez sur Note au client sur le
pavé. Cela ouvre une fenêtre contextuelle dans laquelle vous pouvez ajouter ou
modifier le contenu de la note.

Note

Les notes de produit d’une [commande
importée](point_of_sale/shop/sales_order.html) sont affichées à l’identique
dans le panier.

![Bouton Note au client et notes \(commande et session PdV\) sur les produits
dans le panier](../../_images/customer-notes.png)

Les notes au client apparaissent sur les reçus et les factures des clients de
la même manière qu’elles apparaissent dans le panier, c’est-à-dire, sous le
produit concerné.

![Le reçu du client avec des notes provenant d'une commande et de la
fonctionnalité de note au client.](../../_images/notes-receipt.png)

## Retourner et rembourser des produits

Pour retourner et rembourser un produit,

  1. démarrez une session à partir du **tableau de bord du Point de Vente** ;

  2. cliquez sur Remboursement et sélectionnez la commande concernée ;

  3. sélectionnez le produit et la quantité à rembourser à l’aide du clavier ;

  4. cliquez sur Rembourser pour revenir à l’écran précédent ;

  5. une fois la commande terminée, cliquez sur Paiement pour procéder au remboursement ;

  6. cliquez sur Valider et Nouvelle commande pour aider le client suivant.

![Vue remboursement dans un point de vente](../../_images/refund.png)

Note

  * Vous pouvez filtrer la **liste des commandes** en fonction du numéro de reçu, de la date ou du client en utilisant la barre de recherche.

  * Vous pouvez également rembourser un produit en sélectionnant le produit retourné à partir d’une session ouverte et en définissant une quantité négative égale au nombre de produits retournés. Pour ce faire, cliquez sur Qté et +/-, puis sur la quantité de produits retournés.

## Fermer la session du PdV

Pour fermer la session, cliquez sur Fermer dans le coin supérieur droit de
votre écran ; cela permet d’ouvrir la fenêtre contextuelle Fermeture de
session. À partir de cet écran, vous pouvez récupérer diverses informations :

  * le nombre de commandes effectuées et le montant total réalisé au cours de la session ;

  * les montants attendus regroupés par mode de paiement.

Avant de fermer cette fenêtre, comptez votre argent liquide à l’aide de
l’icône de la calculatrice. Cette opération ouvre une fenêtre contextuelle qui
calcule le montant total du tiroir-caisse en fonction des pièces et des
billets comptés et ajoutés manuellement. Ensuite, cliquez sur Confirmer ou
Annuler pour fermer la fenêtre. Le montant calculé est indiqué dans la colonne
compté et les détails d’argent sont précisés dans la section **Notes**.

![Comment fermer une session du PdV.](../../_images/closing-control.png)

Une fois que vous avez fini de contrôler les montants, cliquez sur Fermer la
session pour fermer et revenir au **tableau de bord du PdV**.

Note

  * Vous pouvez laisser la session ouverte en cliquant sur Backend ou l’interrompre et continuer à vendre en cliquant sur Annuler.

  * En fonction de votre configuration, il se peut que vous ne soyez autorisé à fermer une session que si les recettes en espèces attendues sont égales aux espèces comptées. Pour la fermer quand même, cliquez sur Ok sur l’écran Écart de règlement.

Astuce

  * Il est fortement conseillé de fermer votre session de PdV à la fin de chaque journée.

  * Pour jeter un coup d’œil à vos sessions précédentes, allez à Point de vente ‣ Commandes ‣ Sessions.

  * [Gestion de plusieurs employés](point_of_sale/employee_login.html)
  * [Reçus et factures](point_of_sale/receipts_invoices.html)
  * [Configuration](point_of_sale/configuration.html)
    * [ePOS printers](point_of_sale/configuration/epos_printers.html)
    * [Connexion sécurisée (HTTPS)](point_of_sale/configuration/https.html)
    * [Certificat auto-signé pour les imprimantes ePOS](point_of_sale/configuration/epos_ssc.html)
  * Fonctionnalités de boutique
    * [Commandes clients](point_of_sale/shop/sales_order.html)
    * [Codes-barres](point_of_sale/shop/barcode.html)
    * [Numéros de série et de lot](point_of_sale/shop/serial_numbers.html)
    * [Ship later](point_of_sale/shop/ship_later.html)
    * [Écran client](point_of_sale/shop/customer_display.html)
  * [Fonctionnalités de restaurant](point_of_sale/restaurant.html)
    * [Factures fournisseurs](point_of_sale/restaurant/bill_printing.html)
    * [Gestion des salles et des tables](point_of_sale/restaurant/floors_tables.html)
    * [Imprimer des commandes](point_of_sale/restaurant/kitchen_printing.html)
    * [Pourboires](point_of_sale/restaurant/tips.html)
  * Fonctionnalités de tarification
    * [Remises](point_of_sale/pricing/discounts.html)
    * [Étiquettes de remise (lecteur de codes-barres)](point_of_sale/pricing/discount_tags.html)
    * [Programmes de fidélité](point_of_sale/pricing/loyalty.html)
    * [Listes de prix](point_of_sale/pricing/pricelists.html)
    * [Taxes flexibles (positions fiscales)](point_of_sale/pricing/fiscal_position.html)
    * [Arrondi des paiements en espèces](point_of_sale/pricing/cash_rounding.html)
  * [Modes de paiement](point_of_sale/payment_methods.html)
    * [Terminaux de paiement](point_of_sale/payment_methods/terminals.html)
      * [Adyen](point_of_sale/payment_methods/terminals/adyen.html)
      * [Ingenico](point_of_sale/payment_methods/terminals/ingenico.html)
      * [SIX](point_of_sale/payment_methods/terminals/six.html)
      * [Stripe](point_of_sale/payment_methods/terminals/stripe.html)
      * [Vantiv](point_of_sale/payment_methods/terminals/vantiv.html)
      * [Worldline](point_of_sale/payment_methods/terminals/worldline.html)
  * [Analyse](point_of_sale/reporting.html)

