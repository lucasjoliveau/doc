# Signatures en ligne pour les confirmations de commande

L’application Konvergo ERP _Ventes_ permet aux clients de confirmer leurs commandes
par le biais d’une signature en ligne directement sur la commande. Une fois
que la commande est signée électroniquement par le client, le vendeur associé
à la commande est immédiatement notifié que la commande est confirmée.

## Activer les signatures en ligne

Pour que les clients confirment leurs commandes avec une signature en ligne,
la fonctionnalité _Signature en ligne_ **doit** être activée.

Pour activer la fonctionnalité _Signature en ligne_ , allez à l’application
Ventes ‣ Configuration ‣ Paramètres, faites défiler jusqu’à la section **Devis
& Commandes** et cochez la case à côté de la fonctionnalité **Signature en
ligne** pour l’activer.

![La fonctionnalité Signature en ligne dans les Paramètres de l'application
Konvergo ERP Ventes.](../../../../_images/signature-setting.png)

Ensuite, cliquez sur le bouton **Enregistrer** dans le coin supérieur gauche.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lors de la création d’un modèle de devis, la fonctionnalité signature en ligne est l’option <b>Signature</b>, située dans le champ <b>Confirmation en ligne</b> du formulaire de modèle de devis.</p>
<img alt="L'option signature de la confirmation en ligne figurant sur chaque modèle de devis dans Konvergo ERP." class="align-center" src="../../../../_images/signature-feature-quotation-template.png"/>
<p>Sur des devis standards, la fonctionnalité de signature en ligne est l’option <b>Signature</b> qui se trouve dans l’onglet <b>Autres informations</b> du formulaire de devis.</p>
<img alt="La fonctionnalité de signature en ligne dans l'onglet Autres informations du formulaire de devis dans Konvergo ERP." class="align-center" src="../../../../_images/signature-other-info-tab.png"/>
</div>

## Confirmer la commande par une signature en ligne

Lorsque les clients accèdent à leurs devis en ligne par le portail client, ils
trouvent un bouton **Signer & Payer** sur le devis.

![Le bouton Signer et Payer sur les devis en ligne dans Konvergo ERP
Ventes.](../../../../_images/sign-and-pay-button.png)

Lorsque vous cliquez sur ce bouton, une fenêtre contextuelle **Valider la
commande** s’ouvre. Dans cette fenêtre contextuelle, le champ **Nom complet**
est rempli automatiquement, sur la base des coordonnées dans la base de
données.

![La fenêtre contextuelle Confirmer la commande pour les signatures en ligne
dans Konvergo ERP Ventes.](../../../../_images/validate-order-popup.png)

Ensuite, les clients ont la possibilité de saisir une signature en ligne avec
l’une des options suivantes : **Automatique** , **Dessiner** , ou **Charger**.

**Automatique** permet à Konvergo ERP de générer automatiquement une signature en
ligne sur la base des informations contenues dans le champ **Nom complet**.
**Dessiner** permet au client d’utiliser le curseur pour créer une signature
personnalisée directement dans la fenêtre contextuelle. Et **Charger** permet
au client de charger un fichier de signature déjà créé à partir de son
ordinateur.

Après avoir choisi l’une des trois options de signature susmentionnées
(**Automatique** , **Dessiner** , ou **Charger**), le client peut cliquer sur
le bouton **Accepter & Signer**.

Lorsque le client clique sur le bouton **Accepter & Signer**, il peut choisir
entre plusieurs modes de paiement (si l’option _Paiement en ligne_ s’applique
à ce devis).

Ensuite, lorsque le devis est payé et confirmé, un bon de livraison est créé
automatiquement (si l’application _Inventaire_ d’Konvergo ERP est installée).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="quote_template">Modèles de devis</a></p></li>
<li><p><a href="get_paid_to_validate">Paiement en ligne pour confirmer la commande</a></p></li>
</ul>
</div>

