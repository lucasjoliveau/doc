# Paiements en ligne

  * Installer le patch pour désactiver le paiement des factures en ligne
    * [Mettre à jour Konvergo ERP à la dernière version](online/install_portal_patch#update-odoo-to-the-latest-release)
    * [Mettre à jour la liste des modules disponibles](online/install_portal_patch#update-the-list-of-available-modules)
    * [Installez le module Patch de paiement des factures en ligne.](online/install_portal_patch#install-the-module-invoice-online-payment-patch)

Pour que vos clients puissent payer plus facilement les factures que vous
émettez, vous pouvez activer la fonctionnalité **Paiement des factures en
ligne** , qui ajoute un bouton _Payer maintenant_ sur leur **Portail client**.
Cela permet à vos clients de voir leurs factures en ligne et de payer
directement avec leur mode de paiement préféré, ce qui facilite grandement le
processus de paiement.

![Choix du fournisseur de paiement après avoir cliqué sur "Payer
maintenant"](../../../../_images/online-payment-providers.png)

## Configuration

Make sure your [payment providers are correctly
configured](../../payment_providers).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, « <a href="../../payment_providers/wire_transfer">Wire Transfer</a> » is the
only payment provider activated, but you still have to fill out the payment details.</p>
</div>

Pour activer le Paiement des factures en ligne, allez à Comptabilité ‣
Configuration ‣ Paramètres ‣ Paiements clients, activez **Paiement des
factures en ligne**et cliquez sur _Enregistrer_.

## Portail client

Après avoir émis une facture, cliquez sur _Envoyer & Imprimer_ et envoyez la
facture au client par email. Ils recevront un email contenant un lien qui les
redirige vers la facture sur leur **Portail client**.

![Email contenant un lien pour voir la facture en ligne sur le Portail
client.](../../../../_images/view-invoice.png)

Ils peuvent choisir le fournisseur de paiement qu’ils souhaitent utiliser en
cliquant sur _Payer maintenant_.

![Le bouton "Payer maintenant" sur une facture dans le Portail
client.](../../../../_images/pay-now.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

