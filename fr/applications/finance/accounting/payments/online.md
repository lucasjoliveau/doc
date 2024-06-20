# Paiements en ligne

  * Installer le patch pour désactiver le paiement des factures en ligne
    * [Mettre à jour Odoo à la dernière version](online/install_portal_patch.html#update-odoo-to-the-latest-release)
    * [Mettre à jour la liste des modules disponibles](online/install_portal_patch.html#update-the-list-of-available-modules)
    * [Installez le module Patch de paiement des factures en ligne.](online/install_portal_patch.html#install-the-module-invoice-online-payment-patch)

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
configured](../../payment_providers.html).

Note

By default, « [Wire Transfer](../../payment_providers/wire_transfer.html) » is
the only payment provider activated, but you still have to fill out the
payment details.

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
client.](../../../../_images/pay-now.png)

Pour plus d'infos

  * [Paiements en ligne](../../payment_providers.html)

