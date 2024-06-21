# Modes d’expédition

En fonction de votre stratégie d’expédition, vous pouvez soit utiliser vos
propres modes d’expédition, soit utiliser une intégration avec un fournisseur
d’expédition existant.

<div class="alert alert-secondary" id="ecommerce-own-shipping">
<p class="alert-title">
Pour plus d'infos</p><p><a href="checkout">Paiement</a></p>
</div>

## Vos propres modes d’expédition

Vous pouvez créer vos propres modes d’expédition et définir des règles pour
calculer les frais d’expédition. Pour ce faire, allez à Site Web ‣
Configuration ‣ Modes d’expédition, et soit sélectionner un mode d’expédition
**existant** , soit en **créer** un. Lors de la création d’un mode
d’expédition, vous pouvez choisir entre [Prix
fixe](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method),
[Fondé sur des
règles](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method),
et **Enlèvement en magasin**.

### Enlèvement en magasin

Le **Enlèvement en magasin** doit d’abord être **activé** dans les paramètres
(Site Web ‣ Configuration ‣ Paramètres ‣ Expédition) en cochant **Paiements &
Retrait sur site**. Une fois l’option activée, vous pouvez sélectionner et
**Personnaliser les sites d’enlèvement**. Les **sites de retrait** peuvent
être **spécifiques au site web** , mais sont par défaut disponibles pour
_tous_ les sites web.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/delivery_method">Delivery methods</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing">Shipping cost invoicing</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack">Expédition de plusieurs colis</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/cancel">Comment annuler une demande d’expédition envoyée à un transporteur ?</a></p></li>
</ul>
</div>

## Fournisseurs d’expédition

Une autre option est d’utiliser une des intégrations avec un fournisseur
d’expédition existant. L’avantage d’utiliser une intégration est que les frais
de livraison sont automatiquement calculés sur la base de chaque commande et
que les étiquettes d’expédition sont générées.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Third-party shipping carriers</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials">Comment obtenir des identifiants UPS pour l’intégration avec Konvergo ERP ?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials">Comment obtenir des identifiants DHL pour l’intégration avec Konvergo ERP ?</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels">Print shipping labels</a></p></li>
</ul>
</div>

## Disponibilité sur le site web

Les modes d’expédition sont rendus disponibles sur des sites web
**spécifiques** _uniquement_ , si vous le souhaitez. Pour ce faire, allez à
Site Web ‣ Configuration ‣ Paramètres ‣ Modes d’expédition et sélectionnez le
**mode d’expédition** souhaité. Dans le champ **Site web** , indiquez le site
web auquel le mode d’expédition doit être restreint. Laissez le champ **vide**
pour que le mode soit disponible sur _tous_ les sites web.

## Mode de livraison lors du paiement

Les clients peuvent choisir le mode de livraison à la fin du processus de
paiement, à l’étape **Confirmer la commande**.

![Choix du mode de livraison lors du paiement](../../../../_images/shipping-
checkout.png)

