# Changer la taille de l’étiquette d’expédition

## Vue d’ensemble

Dans Konvergo ERP, il existe une variété de types d’étiquettes d’expédition qui
peuvent être sélectionnés pour les bons de livraison. Selon les types de colis
d’expédition utilisés, différentes tailles d’étiquettes peuvent être plus
appropriées et peuvent être configurées pour s’adapter au colis.

## Configuration

Dans le module Inventaire, allez à Configuration ‣ Livraison ‣ Modes
d’expédition. Cliquez sur un mode de livraison pour en choisir un. Dans
l’exemple suivant, nous utilisons _FedEx International_.

![Différents modes d'expédition.](../../../../../_images/shipping-options.png)

Dans l’onglet **Configuration** , dans **Type d’étiquette** , choisissez l’un
des types d’étiquette disponibles. La disponibilité varie en fonction du
transporteur.

![Sélectionnez un type d'étiquette.](../../../../../_images/label-type-
dropdown.png)

Lorsqu’une commande avec le transporteur correspondant est confirmée et un bon
de livraison est validé, l’étiquette d’expédition sera automatiquement créée
en tant que PDF et apparaîtra dans le **Chatter**.

## Créer une commande client

Dans l’application Ventes, cliquez sur **Créer** et sélectionnez un client
international. Cliquez sur **Ajouter un produit** et sélectionnez un article.
Cliquez sur **Ajouter l’expédition** , sélectionnez un mode d’expédition, puis
cliquez sur **Calculer le tarif** et enfin cliquez sur **Ajouter**.

![Ajouter un mode d'expédition et un tarif à une
commande](../../../../../_images/shipping-rate.png)

Une fois que le devis est confirmé en cliquant sur **Confirmer** , un bouton
intelligent **Livraison** apparaîtra.

![Bouton intelligent bon de livraison.](../../../../../_images/shipping-italy-
so.png)

Une fois que le bon de livraison est validé en cliquant sur **Valider** sur le
bon de livraison, les documents d’expédition apparaîtront dans le **Chatter**.

![Documents d'expédition en PDF.](../../../../../_images/shipping-pdfs.png)

## Exemples d’étiquettes

Le **Type d’étiquette** par défaut est **Paper Letter**. Voici un exemple
d’étiquette FedEx au format lettre :

![Étiquette d'expédition FedEx pleine page au format
lettre.](../../../../../_images/full-page-fedex.png)

À titre de comparaison, voici un exemple d’étiquette FedEx de la moitié
inférieure :

![Une demi-page d'étiquette d'expédition FedEx au format
lettre.](../../../../../_images/half-page-fedex.png)

