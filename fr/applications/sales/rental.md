# Location

**Odoo Location** est une solution complète pour gérer vos locations.

À partir d’une vue unique, vous pouvez envoyer des devis, confirmer des
commandes, planifier des locations, enregistrer quand les produits sont
enlevés et retournés et facturer vos clients.

Pour plus d'infos

  * [Odoo Location : page produit](https://www.odoo.com/app/rental)

  * [Odoo Tutoriels : Location](https://www.odoo.com/slides/rental-48)

## Prix ​​de location

### Configuration

Allez à Location ‣ Produits, sélectionnez ou créez un produit et cliquez sur
l’onglet _Location_ d’un produit. Sous _Prix de location_ , cliquez sur
_Ajouter un prix_. Choisissez ensuite une _Unité_ de temps (heures, jours,
semaines ou mois), une _Durée_ , et un _Prix_. Vous pouvez ajouter autant de
lignes de prix que nécessaire, généralement pour accorder des remises pour des
durées de location plus longues.

![Exemple d'une configuration de prix de location dans Odoo
Location](../../_images/rental-pricing-example.png)

Astuce

Sous _Réservations_ , vous pouvez ajouter des amendes pour chaque _Heure
supplémentaire_ ou _Jour supplémentaire_. Vous pouvez également définir une
_Durée de sécurité_ , exprimée en heures, pour rendre le produit
temporairement indisponible entre deux bons de location.

Note

Si vous souhaitez louer un produit créé en dehors de l’application Location,
n’oubliez pas de cocher _Peut être loué_ sous le nom du produit. Par défaut,
cette option est cochée lorsque vous créez un produit directement depuis
l’application Location.

### Calculs

Odoo utilise toujours deux règles pour calculer le prix d’un produit lorsque
vous créez un bon de location :

  1. Une seule ligne de prix est utilisée.

  2. La ligne la moins chère est sélectionnée.

Exercise

Considérez la configuration de prix de location suivante pour un produit :

  * 1 jour : 100 $

  * 3 jours : 250 $

  * 1 semaine : 500 $

Un client souhaite louer ce produit pendant 8 jours. Quel prix devrait-il
payer ?

Après la création d’une commande, Odoo sélectionne la deuxième ligne car c’est
l’option la moins chère. Le client doit payer trois fois “3 jours” pour
couvrir les huit jours de location, pour un total de 750 $.

## Signature du client

Vous pouvez demander à vos clients de signer un contrat de location décrivant
l’accord entre vous et vos clients avant que ces derniers enlèvent les
produits, pour vous assurer que vos produits sont retournés à temps et dans
leur état d’origine. Pour ce faire, allez à Location ‣ Configuration ‣
Paramètres, activez _Documents numériques_ et _Enregistrer_.

![Paramètre de documents numériques dans Odoo Location](../../_images/digital-
documents-settings.png)

Note

This feature requires the [Sign](../productivity/sign.html) app. If necessary,
Odoo installs it after activating _Digital Documents_.

Une fois les paramètres de l’application enregistrés, vous avez la possibilité
de modifier le _contrat de location_ par défaut dans le menu déroulant. Vous
pouvez choisir n’importe quel document déjà téléchargé sur l’application
_Signature_ ou en télécharger un nouveau sur l’application _Signature_ en
cliquant sur _Télécharger un modèle_.

Pour demander une signature au client, sélectionnez un bon de location
confirmé, cliquez sur _Signer les documents_ , choisissez le modèle de
document à utiliser et cliquez à nouveau sur _Signer les documents_. Dans la
fenêtre suivante, sélectionnez votre client et cliquez sur _Signer_ pour
démarrer le processus de signature. Une fois le document complété, cliquez sur
_Valider & envoyer le document complété_.

Pour plus d'infos

  * [Tutoriels Odoo : Signature](https://www.odoo.com/slides/sign-61)

## Bon d’enlèvement et de retour

Vous pouvez imprimer et remettre à vos clients des reçus lorsqu’ils viennent
chercher et/ou retournent des produits. Pour ce faire, ouvrez n’importe quel
bon de location, cliquez sur _Imprimer_ et sélectionnez _Bon d’enlèvement et
de retour_. Odoo génère ensuite un PDF détaillant toutes les informations sur
l’état actuel des articles loués : lesquels ont été enlevés, quand ils
devraient être retournés, lesquels ont été retournés et les éventuels coûts de
retard de location.

![Imprimer un bon d'enlèvement et de retour dans Odoo
Location](../../_images/print-receipt1.png)

