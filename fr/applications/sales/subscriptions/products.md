# Produits d’abonnement

Grâce à son intégration étroite avec l’application Odoo _Ventes_ ,
l’application _Abonnements_ permet aux utilisateurs de vendre des produits
d’abonnement en plus des produits courants. Alors que les produits courants ne
sont vendus qu’une seule fois, les produits d’abonnement sont vendus sur une
base récurrente, générant ainai des revenus récurrents.

Dans Odoo, les produits d’abonnement sont également appelés produits
_récurrents_.

## Configurer des périodes de récurrence

Pour commencer à utiliser les abonnements, les _périodes de récurrence_
doivent être configurées correctement.

Les périodes de récurrence sont les périodes au cours desquelles les
abonnements sont renouvelés. Elles désignent la fréquence à laquelle le client
paie (et reçoit) des produits d’abonnement.

Pour configurer les périodes de récurrence, allez à l’application Abonnements
‣ Configuration ‣ Périodes de récurrence.

![La page des périodes de récurrence dans l'application Odoo
Abonnements.](../../../_images/recurrence-periods-page.png)

Certaines périodes de récurrence de base sont déjà configurées dans
l’application _Abonnements_ :

  * Mensuel

  * Trimestriel

  * Hebdomadaire

  * 2 semaines

  * Annuel

  * 3 années

  * 5 années

Vous pouvez ajouter et/ou modifier de nouvelles périodes de récurrence à tout
moment.

Pour créer une nouvelle période de récurrence, cliquez sur Nouveau sur la page
des Périodes de récurrence. Un formulaire de période de récurrence vierge
s’ouvre alors.

![Un formulaire de période de récurrence dans l'application Odoo
Abonnements.](../../../_images/recurrence-period-form.png)

Saisissez ensuite le Nom et la Durée de la période de récurrence et
sélectionnez l”Unité qui définit la durée.

Important

L’unité Jours _ne peut pas_ être utilisée comme période de récurrence sur les
abonnements. La récurrence journalière est réservée aux locations et **ne peut
pas** être ajoutée aux commandes récurrentes.

Cette restriction a pour but d’éviter des commandes qui généreraient des
factures journalières.

## Configuration du formulaire de produit

Pour créer un nouveau produit d’abonnement, allez à l’application Abonnements
‣ Produits ‣ Produits, et cliquez sur Nouveau.

Un formulaire de produit vierge s’ouvre et peut être configuré et personnalisé
de plusieurs manières.

Note

Par défaut, l’option Récurrent est déjà activée, invitant à Odoo de
reconnaître le produit comme un produit d’abonnement. Veillez à ce que les
options Récurrent et Peut être vendu soient activées.

Le champ Type de produit est également défini par défaut sur Service.
Néanmoins, il est _possible_ de définir d’autres types de produits
d’abonnement, le cas échéant.

![Un formulaire de produit d'abonnement de base dans l'application Odoo
Abonnements.](../../../_images/subscription-product-form.png)

### Tarification basée sur le temps

Une fois que les champs requis dans l’onglet Informations générales ont été
saisies, cliquez sur l’onglet Tarification basée sur le temps sur le
formulaire du produit.

![L'onglet Tarification basée sur le temps d'un formulaire de produit
d'abonnement dans Odoo Abonnements.](../../../_images/time-based-pricing-
tab.png)

Cliquez alors sur Ajouter un prix pour commencer à définir des prix
récurrents.

Dans la colonne Période, sélectionnez la période de récurrence souhaitée. Dans
la colonne Liste de prix, sélectionnez une liste de prix le cas échéant.
Ensuite, dans la colonne Prix, saisissez le prix pour cette période de
récurrence.

Note

Il **n’est pas possible** d’utiliser les périodes Quotidien et Horaire pour
les produits récurrents.

![La fenêtre contextuelle d'erreur de validation qui s'ouvre dans Odoo
Abonnements.](../../../_images/validation-error-popup.png)

Note

Il n’y a _aucune limite_ au nombre de lignes qui peuvent être ajoutées à
l’onglet Tarification basée sur le temps.

Astuce

Un produit existant peut devenir un produit d’abonnement, simplement en le
marquant comme étant Récurrent, et en configurant la Tarification basée sur le
temps sur le formulaire.

#### Listes de prix

Vous pouvez utiliser des [Listes de
prix](../sales/products_prices/prices/pricing.html) avec les produits
d’abonnement pour accorder un prix spécial aux clients répertoriés sur les
listes de prix.

Elles peuvent être configurées dans l’onglet Tarification basée sur le temps
du formulaire du produit ou sans le formulaire des listes de prix dans
l’application _Ventes_.

Pour créer des règles de prix récurrentes pour des listes de prix spécifiques
dans l’onglet Tarification basée sur le temps de la fiche du produit,
sélectionnez une liste de prix dans la colonne Liste de prix.

![Listes de prix dans l'onglet "Tarification basée sur le temps" de la fiche
du produit.](../../../_images/pricelist-time-based-pricing.png)

Lorsque les listes de prix sont ajoutées à l’onglet Tarification basée sur le
temps, le formulaire de liste de prix est automatiquement mis à jour dans
l’application _Ventes_.

Il est également possible de configurer les règles de la tarification basée
sur le temps directement sur le formulaire des listes de prix.

Pour ce faire, allez à l’application Ventes -‣ Produits ‣ Listes de prix, et
sélectionnez une liste de prix (ou cliquez sur Nouveau pour créer une nouvelle
liste de prix).

Note

Les listes de prix sont également accessibles via l’application Odoo
_Abonnements_ en suivant les même étapes.

Ensuite, sur le formulaire des listes de prix, dans l’onglet Règles basées sur
le temps, cliquez sur Ajouter une ligne.

![L'onglet des règles basées sur le temps d'une liste de prix dans Odoo
Ventes.](../../../_images/pricelist-form-time-based-rules-tab.png)

Sélectionnez ensuite un produit d’abonnement dans la colonne Produits et
sélectionnez une période de récurrence dans la colonne Période. Enfin,
saisissez un Prix pour ce produit et cette période. Ajoutez autant de lignes
que nécessaire.

Lorsque les Règles basées sur le temps sont ajoutées au formulaire de liste de
prix, l’onglet Tarification basée sur le temps de la fiche du produit est
automatiquement mis à jour.

Pour plus d'infos

[Utiliser des abonnements dans eCommerce](ecommerce.html)

