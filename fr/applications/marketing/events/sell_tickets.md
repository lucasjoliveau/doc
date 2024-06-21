# Vendre des tickets

Créez des types de tickets personnalisés (avec des prix différents) parmi
lesquels les participants potentiels pourront choisir, directement sur le
formulaire du modèle d’événement, sous l’onglet **Tickets**. Konvergo ERP simplifie la
procédure d’achat de tickets en proposant plusieurs modes de paiement.

## Configuration

Tout d’abord, afin d’activer la création (et la vente) de tickets d’événement,
allez à Configuration ‣ Paramètres et activez les fonctionnalités **Tickets**
et **Billetterie en ligne**.

La fonctionnalité **Tickets** vous permet de vendre des tickets pour un
événement.

La fonctionnalité **Billetterie en ligne** vous permet de vendre des tickets
sur le site web.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si ces options ne sont <em>pas</em> activées, un bouton <b>S’inscrire</b> par défaut sera disponible pour les inscriptions gratuites.</p>
</div> ![Vue de la page des paramètres d'Konvergo ERP
Événements.](../../../_images/events-settings-tickets.png)

## Utiliser les bons de commande pour vendre des tickets

Dans l’application **Ventes** , ajoutez une inscription à l’événement créée
précédemment (comme s’il s’agissait d’un produit) au bon de commande en tant
que ligne de la commande. Lors de l’ajout de l’inscription, une fenêtre
contextuelle apparaît et permet de sélectionner un événement spécifique (et le
type de ticket). Ce ticket d’événement spécifique est alors lié au bon de
commande.

![Vue d'un bon de commande et de l'option de choisir l'événement spécifique
dans Konvergo ERP Événements.](../../../_images/events-through-sales-order.png)

Les événements dont les tickets se vendent en ligne ou par le biais de bons de
commande disposent d’un **bouton intelligent Ventes** , situé en haut du
formulaire du modèle d’événement (dans l’application **Événements**).

Le fait de cliquer sur le **bouton intelligent Ventes** fait apparaître une
page contenant tous les bons de commande liés à cet événement.

![Vue d'un formulaire d'événement et du bouton intelligent des ventes dans
Konvergo ERP Événements.](../../../_images/events-sales-smartbutton.png) ![Vue d'un
formulaire d'événement mettant en évidence la colonne des produits sous
l'onglet tickets dans Konvergo ERP Événements.](../../../_images/events-tickets-
registration-product.png)

## Utiliser le site web pour vendre des tickets

Pour les tickets achetés sur le site web, la procédure est similaire à la
création d’un **bon de commande** avec un produit **Inscription** spécifique.
Dans ce cas, les tickets sont ajoutés à un panier virtuel et la transaction
peut être complétée comme d’habitude - en utilisant n’importe quel mode de
paiement préconfiguré qui a été mis en place sur le site web.

L’achat effectué fait automatiquement l’objet d’un **bon de commande** , qui
peut être facilement consulté depuis le backend de la base de données.

![Vue de la transaction sur le site web pour Konvergo ERP
Événements.](../../../_images/events-online-ticket-purchase.png)

