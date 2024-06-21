# Paiement en ligne pour confirmer la commande

L’application Konvergo ERP _Ventes_ permet aux clients de confirmer les commandes par
le biais d’un paiement en ligne directement sur la commande. Une fois que la
commande est payée électroniquement par le client, le vendeur associé à la
commande est immédiatement notifié que la commande est confirmée.

## Activer les paiements en ligne

Pour que les clients confirment leurs commandes par un paiement en ligne, le
paramètre _Paiement en ligne_ **doit** être activé.

Pour activer la fonctionnalité _Paiement en ligne_ , allez à l’application
Ventes ‣ Configuration ‣ Paramètres, faites défiler jusqu’à la section **Devis
& Commandes**, cochez la case à côté de la fonctionnalité **Paiement en
ligne** et cliquez sur **Enregistrer**.

![Le paramètre de paiement en ligne dans l'application Konvergo ERP
Ventes.](../../../../_images/online-payment-setting.png)

Sous l’option **Paiement en ligne** sur la page des **Paramètres** de
l’application Ventes se trouve un champ **Validité par défaut du devis**. Dans
ce champ, vous pouvez ajouter un nombre spécifique de jours pendant lesquels
les devis restent valables par défaut.

Pour activer cette fonctionnalité sur un devis standard, cochez la case à côté
de l’option **Paiement** , dans le champ **Confirmation en ligne** dans
l’onglet **Autres informations**.

![Le paramètre paiement en ligne sur un devis standard dans Konvergo ERP
Ventes.](../../../../_images/online-payment-option-quotation.png)

Pour activer cette fonctionnalité sur un modèle de devis, cochez la case à
côté de la fonctionnalité **Paiement** , dans le champ **Confirmation en
ligne** du modèle de devis.

![Le paramètre paiement en ligne sur les modèles de devis dans Konvergo ERP
Ventes.](../../../../_images/online-payment-option-quotation-template.png)

## Fournisseurs de paiement

Après avoir activé la fonctionnalité **Paiement en ligne** , un lien
permettant de configurer les **Fournisseurs de paiement** s’affiche en
dessous.

En cliquant sur ce lien, vous accédez à une page distincte sur les
**Fournisseurs de paiement** , dans laquelle une grande variété de
fournisseurs de paiement peuvent être activés, personnalisés et publiés.

![Page des fournisseurs de paiement dans Konvergo ERP
Ventes.](../../../../_images/payment-providers-page.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/payment_providers">Paiements en ligne</a></p>
</div>

## Enregistrer un paiement

Après avoir ouvert des devis dans leur portail client, les clients peuvent
cliquez sur **Accepter & Payer** pour confirmer leur commande par le biais
d’un paiement en ligne.

![Le bouton Accepter et payer sur un devis en ligne dans Konvergo ERP
Ventes.](../../../../_images/accept-and-pay-button.png)

Après avoir cliqué sur **Accepter & Payer**, les clients se voient présenter
la fenêtre contextuelle **Confirmer la commande** qui convient différentes
options leur permettant d’effectuer des paiement sen ligne, dans la section
**Payer avec**.

![Comment enregistrer un paiement dans une fenêtre contextuelle Confirmer la
commande dans Konvergo ERP Ventes.](../../../../_images/validate-order-pay-with.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans la fenêtre contextuelle <b>Confirmer la commande</b>, Konvergo ERP propose <b>uniquement</b> les options de paiement qui ont été publiées et configurées sur la page <b>Fournisseurs de paiement</b>.</p>
</div>

Une fois que le client a sélectionné son mode de paiement, il clique sur le
bouton **Payer** de la fenêtre contextuelle pour confirmer la commande. Konvergo ERP
notifie instantanément le vendeur assigné lors de la confirmation de la
commande avec un paiement en ligne.

![Exemple de notification qui apparaît dans le chatter lorsqu'un paiement en
ligne est effectué.](../../../../_images/payment-confirmation-notification-
chatter.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="quote_template">Modèles de devis</a></p></li>
<li><p><a href="get_signature_to_validate">Signatures en ligne pour les confirmations de commande</a></p></li>
<li><p><a href="../../../finance/payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

