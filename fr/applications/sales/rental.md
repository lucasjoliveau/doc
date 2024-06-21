# Location

**Konvergo ERP Location** est une solution complète pour gérer vos locations.

À partir d’une vue unique, vous pouvez envoyer des devis, confirmer des
commandes, planifier des locations, enregistrer quand les produits sont
enlevés et retournés et facturer vos clients.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/app/rental">Konvergo ERP Location : page produit</a></p></li>
<li><p><a href="https://www.odoo.com/slides/rental-48">Konvergo ERP Tutoriels : Location</a></p></li>
</ul>
</div>

## Prix ​​de location

### Configuration

Allez à Location ‣ Produits, sélectionnez ou créez un produit et cliquez sur
l’onglet _Location_ d’un produit. Sous _Prix de location_ , cliquez sur
_Ajouter un prix_. Choisissez ensuite une _Unité_ de temps (heures, jours,
semaines ou mois), une _Durée_ , et un _Prix_. Vous pouvez ajouter autant de
lignes de prix que nécessaire, généralement pour accorder des remises pour des
durées de location plus longues.

![Exemple d'une configuration de prix de location dans Konvergo ERP
Location](../../_images/rental-pricing-example.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Sous <em>Réservations</em>, vous pouvez ajouter des amendes pour chaque <em>Heure supplémentaire</em> ou <em>Jour supplémentaire</em>. Vous pouvez également définir une <em>Durée de sécurité</em>, exprimée en heures, pour rendre le produit temporairement indisponible entre deux bons de location.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous souhaitez louer un produit créé en dehors de l’application Location, n’oubliez pas de cocher <em>Peut être loué</em> sous le nom du produit. Par défaut, cette option est cochée lorsque vous créez un produit directement depuis l’application Location.</p>
</div>

### Calculs

Konvergo ERP utilise toujours deux règles pour calculer le prix d’un produit lorsque
vous créez un bon de location :

  1. Une seule ligne de prix est utilisée.

  2. La ligne la moins chère est sélectionnée.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Considérez la configuration de prix de location suivante pour un produit :</p>
<ul>
<li><p>1 jour : 100 $</p></li>
<li><p>3 jours : 250 $</p></li>
<li><p>1 semaine : 500 $</p></li>
</ul>
<p>Un client souhaite louer ce produit pendant 8 jours. Quel prix devrait-il payer ?</p>
<p>Après la création d’une commande, Konvergo ERP sélectionne la deuxième ligne car c’est l’option la moins chère. Le client doit payer trois fois “3 jours” pour couvrir les huit jours de location, pour un total de 750 $.</p>
</div>

## Signature du client

Vous pouvez demander à vos clients de signer un contrat de location décrivant
l’accord entre vous et vos clients avant que ces derniers enlèvent les
produits, pour vous assurer que vos produits sont retournés à temps et dans
leur état d’origine. Pour ce faire, allez à Location ‣ Configuration ‣
Paramètres, activez _Documents numériques_ et _Enregistrer_.

![Paramètre de documents numériques dans Konvergo ERP Location](../../_images/digital-
documents-settings.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature requires the <a href="../productivity/sign">Sign</a> app. If necessary, Konvergo ERP installs it
after activating <em>Digital Documents</em>.</p>
</div>

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

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/slides/sign-61">Tutoriels Konvergo ERP : Signature</a></p></li>
</ul>
</div>

## Bon d’enlèvement et de retour

Vous pouvez imprimer et remettre à vos clients des reçus lorsqu’ils viennent
chercher et/ou retournent des produits. Pour ce faire, ouvrez n’importe quel
bon de location, cliquez sur _Imprimer_ et sélectionnez _Bon d’enlèvement et
de retour_. Konvergo ERP génère ensuite un PDF détaillant toutes les informations sur
l’état actuel des articles loués : lesquels ont été enlevés, quand ils
devraient être retournés, lesquels ont été retournés et les éventuels coûts de
retard de location.

![Imprimer un bon d'enlèvement et de retour dans Konvergo ERP
Location](../../_images/print-receipt1.png)

