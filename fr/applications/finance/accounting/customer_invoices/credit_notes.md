# Avoirs et remboursements

Un **avoir** ou une **note de débit** est un document émis à un client qui
l’informe qu’il a été _crédité/débité_ d’un certain montant.

Plusieurs cas d’utilisation peuvent donner lieu à un avoir, tels que :

>   * une erreur dans la facture
>
>   * un retour de marchandises ou un refus de services
>
>   * les marchandises livrées sont endommagées
>
>

Les notes de débit sont moins courantes, mais elles sont le plus souvent
utilisées pour suivre les dettes dues par les clients ou les fournisseurs en
raison de modifications apportées aux factures clients ou fournisseurs
confirmées.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’émission d’un avoir/d’une note de débit est le seul moyen légal d’annuler, de rembourser ou de modifier une facture validée. N’oubliez pas d”<b>enregistrer le paiement</b> par la suite si vous devez renvoyer de l’argent à votre client et/ou valider le <a href="../../../sales/sales/products_prices/returns">retour</a> si un produit stockable est retourné.</p>
</div>

## Émettre un avoir

Vous pouvez créer un avoir à partir de zéro en allant à Comptabilité ‣ Clients
‣ Avoirs, et en cliquant sur **Créer**. Le formulaire d’avoir se complète de
la même manière que le formulaire de facture.

Cependant, la plupart du temps, les avoirs sont générés directement à partir
des factures correspondantes. Pour ce faire, allez à Comptabilité ‣ Clients ‣
Factures clients, ouvrez la **facture client** correspondante et cliquez sur
**Ajouter un avoir**.

Vous disposez de trois options :

>   * **Remboursement partiel**
>
>   * **Remboursement intégral**
>
>   * **Remboursement intégral et nouvelle facture brouillon**
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une séquence d’avoir commence par <code>R</code> et est suivie du numéro du document correspondant (par ex. RINV/2019/0004 correspond à la facture INV/2019/0004).</p>
</div>

### Remboursement partiel

Lorsque vous sélectionnez l’option **Remboursement partiel** , Konvergo ERP crée un
avoir brouillon déjà prérempli avec toutes les informations nécessaires de la
facture originale. C’est l’option à choisir si vous voulez effectuer un
remboursement partiel ou si vous voulez modifier un détail quelconque de
l’avoir.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il s’agit de l’unique option pour les factures marquées comme <em>en paiement</em> ou <em>payé</em>.</p>
</div>

### Remboursement intégral

Lorsque vous sélectionnez l’option **Remboursement intégral** , Konvergo ERP crée un
avoir, le valide automatiquement et le lettre avec la facture correspondante.

![Avoir remboursement intégral.](../../../../_images/credit_notes02.png)

C’est l’option à choisir si vous voulez effectuer un remboursement intégral ou
**annuler** une facture _validée_.

### Remboursement intégral et nouvelle facture brouillon

Lorsque vous sélectionnez l’option **Remboursement intégral et nouvelle
facture brouillon** , Konvergo ERP crée un avoir, le valide automatiquement et le
lettre avec la facture correspondante et ouvre une nouvelle facture brouillon
préremplie avec les mêmes détails de la facture originale.

Cette option permet de **modifier** le contenu d’une facture _validée_.

## Émettre une note de débit

Vous pouvez créer une note de débit à partir de zéro en allant à Comptabilité
‣ Clients ‣ Factures clients ou en cliquant sur la facture correspondante pour
laquelle vous voulez émettre une note de débit. Sur la vue de formulaire de la
facture, cliquez sur **Ajouter une note de débit** , remplissez les
informations et cliquez sur **Créer**.

## Enregistrer un remboursement fournisseur

Les **remboursements fournisseurs** s’enregistrent de la même manière que les
avoirs :

Vous pouvez créer un avoir à partir de zéro en allant à Comptabilité ‣
Fournisseurs ‣ Remboursements, et en cliquant sur **Créer** ; ou en ouvrant la
**facture fournisseur** correspondante et en cliquant sur **Ajouter un
avoir**.

## Enregistrer une note de débit

Les **notes de débit** des fournisseurs s’enregistrent de la même manière que
celles émises pour les clients :

Allez à Comptabilité ‣ Fournisseurs ‣ Factures fournisseurs, ouvrez la facture
fournisseur correspondante pour laquelle vous voulez enregistrer une note de
débit et cliquez sur **Ajouter une note de débit**. Remplissez les
informations et cliquez sur **Créer une note de débit**.

## Pièces comptables

L’émission d’un avoir/d’une note de crédit à partir d’une facture
client/fournisseur crée une **écriture d’extourne** qui annule les écritures
comptables générées par la facture originale.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>L’écriture comptable d’une facture :</p>
<img alt="Écriture comptable d'une facture." src="../../../../_images/credit_notes03.png"/>
<p>Et voici l’écriture comptable de l’avoir généré pour extourner la facture original ci-dessus :</p>
<img alt="L'écriture comptable d'un avoir extourne l'écriture comptable d'une facture." src="../../../../_images/credit_notes04.png"/>
</div>

