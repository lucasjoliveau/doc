# Point de Vente

Gérez facilement vos boutiques et restaurants avec **Konvergo ERP Point de Vente**.
L’application fonctionne sur tout appareil ayant un navigateur web, même si
vous êtes temporairement hors ligne. Les mouvements de produit sont
automatiquement enregistrés dans votre stock, vous obtenez des statistiques en
temps réel et vos données sont consolidées à travers toutes les boutiques.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/slides/point-of-sale-28">Tutoriels Konvergo ERP : Tutoriels sur les points de vente</a></p></li>
<li><p><a href="../general/iot">IoT Boxes Documentations</a></p></li>
</ul>
</div>

## Démarrer une session

À partir du **tableau de bord du PdV** , cliquez sur **Nouvelle session** et
sur l’écran **Contrôle des espèces à l’ouverture** , cliquez sur **Ouvrir la
session** pour commencer une session du PdV ou cliquez sur **Continuer la
vente** si la session est déjà ouverte.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="point_of_sale/employee_login">Plusieurs utilisateurs</a> peuvent être connectés à la même session en même temps. Cependant, la session ne peut être ouverte qu’une seule fois dans le même navigateur.</p>
</div>

## Vendre des produits

Cliquez sur des produits pour les ajouter au panier. Pour changer la
**quantité** , cliquez sur **Qté** et saisissez le nombre de produits à l’aide
du clavier. Pour ajouter une **remise** ou modifier le **prix** du produit,
cliquez respectivement sur **% de remise** ou **Prix** et saisissez les
montants.

Une fois la commande complétée, passez à la caisse en cliquant sur
**Paiement**. Sélectionnez le **mode de paiement** , saisissez le montant
reçu, puis cliquez sur **Valider**. Cliquez sur **Nouvelle commande** pour
aider le client suivant.

![Interface d'une session du PdV.](../../_images/pos-interface.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Vous pouvez utiliser à la fois <code>,</code> et <code>.</code> sur votre clavier comme séparateurs décimaux.</p></li>
<li><p>L’option <b>Cash</b> est sélectionnée par défaut si vous saisissez le montant sans choisir le mode de paiement.</p></li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The system can only load a limited number of products for effective opening. Click
<b>Search more</b> if the desired product is not loaded automatically.</p>
</div>

## Définir les clients

Il est nécessaire d’enregistrer votre client pour [collecter ses points de
fidélité et lui accorder des récompenses](point_of_sale/pricing/loyalty),
appliquer automatiquement la [liste de prix
attribuée](point_of_sale/pricing/pricelists), ou [générer et imprimer une
facture](point_of_sale/receipts_invoices#receipts-invoices-invoices).

Vous pouvez créer des clients à partir d’une session PdV ouverte en cliquant
sur Client ‣ Créer, et en remplissant les informations de contact. Vous pouvez
également créer des clients à partir du backend en allant au Point de Vente ‣
Commandes ‣ Clients et en cliquant sur **Nouveau**. Remplissez ensuite les
informations et enregistrez.

Pour définir un client pendant une commande, accédez à la liste des clients en
cliquant sur **Client** sur l’interface du point de vente. Vous pouvez
également définir un client sur l’écran de paiement en cliquant sur
**Client**.

## Notes au client

Vous pouvez ajouter des **notes au client** sur des produits spécifiques
directement à partir d’une session PdV ouverte. Par exemple, des conseils de
nettoyage et d’entretien. Elles peuvent également être utilisées pour suivre
la demande particulière d’un client, par exemple s’il ne souhaite pas que le
produit soit assemblé pour lui.

Pour ce faire, sélectionnez un produit et cliquez sur **Note au client** sur
le pavé. Cela ouvre une fenêtre contextuelle dans laquelle vous pouvez ajouter
ou modifier le contenu de la note.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les notes de produit d’une <a href="point_of_sale/shop/sales_order">commande importée</a> sont affichées à l’identique dans le panier.</p>
</div> ![Bouton Note au client et notes \(commande et session
PdV\) sur les produits dans le panier](../../_images/customer-notes.png)

Les notes au client apparaissent sur les reçus et les factures des clients de
la même manière qu’elles apparaissent dans le panier, c’est-à-dire, sous le
produit concerné.

![Le reçu du client avec des notes provenant d'une commande et de la
fonctionnalité de note au client.](../../_images/notes-receipt.png)

## Retourner et rembourser des produits

Pour retourner et rembourser un produit,

  1. démarrez une session à partir du **tableau de bord du Point de Vente** ;

  2. cliquez sur **Remboursement** et sélectionnez la commande concernée ;

  3. sélectionnez le produit et la quantité à rembourser à l’aide du clavier ;

  4. cliquez sur **Rembourser** pour revenir à l’écran précédent ;

  5. une fois la commande terminée, cliquez sur **Paiement** pour procéder au remboursement ;

  6. cliquez sur **Valider** et **Nouvelle commande** pour aider le client suivant.

![Vue remboursement dans un point de vente](../../_images/refund.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous pouvez filtrer la <b>liste des commandes</b> en fonction du <b>numéro de reçu</b>, de la <b>date</b> ou du <b>client</b> en utilisant la barre de recherche.</p></li>
<li><p>Vous pouvez également rembourser un produit en sélectionnant le produit retourné à partir d’une session ouverte et en définissant une quantité négative égale au nombre de produits retournés. Pour ce faire, cliquez sur <b>Qté</b> et <b>+/-</b>, puis sur la quantité de produits retournés.</p></li>
</ul>
</div>

## Fermer la session du PdV

Pour fermer la session, cliquez sur **Fermer** dans le coin supérieur droit de
votre écran ; cela permet d’ouvrir la fenêtre contextuelle **Fermeture de
session**. À partir de cet écran, vous pouvez récupérer diverses informations
:

  * le nombre de commandes effectuées et le montant total réalisé au cours de la session ;

  * les montants attendus regroupés par mode de paiement.

Avant de fermer cette fenêtre, comptez votre argent liquide à l’aide de
l’icône de la calculatrice. Cette opération ouvre une fenêtre contextuelle qui
calcule le montant total du tiroir-caisse en fonction des pièces et des
billets comptés et ajoutés manuellement. Ensuite, cliquez sur **Confirmer** ou
**Annuler** pour fermer la fenêtre. Le montant calculé est indiqué dans la
colonne **compté** et les **détails d’argent** sont précisés dans la section
**Notes**.

![Comment fermer une session du PdV.](../../_images/closing-control.png)

Une fois que vous avez fini de contrôler les montants, cliquez sur **Fermer la
session** pour fermer et revenir au **tableau de bord du PdV**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous pouvez laisser la session ouverte en cliquant sur <b>Backend</b> ou l’interrompre et continuer à vendre en cliquant sur <b>Annuler</b>.</p></li>
<li><p>En fonction de votre configuration, il se peut que vous ne soyez autorisé à fermer une session que si les recettes en espèces attendues sont égales aux espèces comptées. Pour la fermer quand même, cliquez sur <b>Ok</b> sur l’écran <b>Écart de règlement</b>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Il est fortement conseillé de fermer votre session de PdV à la fin de chaque journée.</p></li>
<li><p>Pour jeter un coup d’œil à vos sessions précédentes, allez à Point de vente ‣ Commandes ‣ Sessions.</p></li>
</ul>
</div>

  * [Gestion de plusieurs employés](point_of_sale/employee_login)
  * [Reçus et factures](point_of_sale/receipts_invoices)
  * [Configuration](point_of_sale/configuration)
    * [ePOS printers](point_of_sale/configuration/epos_printers)
    * [Connexion sécurisée (HTTPS)](point_of_sale/configuration/https)
    * [Certificat auto-signé pour les imprimantes ePOS](point_of_sale/configuration/epos_ssc)
  * Fonctionnalités de boutique
    * [Commandes clients](point_of_sale/shop/sales_order)
    * [Codes-barres](point_of_sale/shop/barcode)
    * [Numéros de série et de lot](point_of_sale/shop/serial_numbers)
    * [Ship later](point_of_sale/shop/ship_later)
    * [Écran client](point_of_sale/shop/customer_display)
  * [Fonctionnalités de restaurant](point_of_sale/restaurant)
    * [Factures fournisseurs](point_of_sale/restaurant/bill_printing)
    * [Gestion des salles et des tables](point_of_sale/restaurant/floors_tables)
    * [Imprimer des commandes](point_of_sale/restaurant/kitchen_printing)
    * [Pourboires](point_of_sale/restaurant/tips)
  * Fonctionnalités de tarification
    * [Remises](point_of_sale/pricing/discounts)
    * [Étiquettes de remise (lecteur de codes-barres)](point_of_sale/pricing/discount_tags)
    * [Programmes de fidélité](point_of_sale/pricing/loyalty)
    * [Listes de prix](point_of_sale/pricing/pricelists)
    * [Taxes flexibles (positions fiscales)](point_of_sale/pricing/fiscal_position)
    * [Arrondi des paiements en espèces](point_of_sale/pricing/cash_rounding)
  * [Modes de paiement](point_of_sale/payment_methods)
    * [Terminaux de paiement](point_of_sale/payment_methods/terminals)
      * [Adyen](point_of_sale/payment_methods/terminals/adyen)
      * [Ingenico](point_of_sale/payment_methods/terminals/ingenico)
      * [SIX](point_of_sale/payment_methods/terminals/six)
      * [Stripe](point_of_sale/payment_methods/terminals/stripe)
      * [Vantiv](point_of_sale/payment_methods/terminals/vantiv)
      * [Worldline](point_of_sale/payment_methods/terminals/worldline)
  * [Analyse](point_of_sale/reporting)

