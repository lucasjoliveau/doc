# Positions fiscales (correspondances de taxes et de comptes)

Les taxes et les comptes par défaut sont définis sur les produits et les
clients afin de créer de nouvelles transactions à la volée. Cependant, en
fonction de la localisation et du type d’activité des clients et des
fournisseurs, il peut être nécessaire d’utiliser des taxes et des comptes
différents pour une transaction.

Les **positions fiscales** permettent de créer de règles pour automatiquement
adapter les taxes et les comptes utilisés pour une transaction.

Elles peuvent être appliquées automatiquement, manuellement, ou assignées à un
partenaire.

Note

Plusieurs positions fiscales par défaut sont disponibles dans le cadre de
votre [package de localisation
fiscale](../../fiscal_localizations.html#fiscal-localizations-packages).

## Configuration

> ### Correspondances de taxes et de comptes

Pour modifier ou créer une position fiscale, allez à Comptabilité ‣
Configuration ‣ Positions fiscales et ouvrez l’écriture à modifier ou cliquez
sur Nouveau.

La correspondance de taxes et de comptes est basée sur les taxes et les
comptes par défaut définis sur la fiche du produit.

  * Pour établir une correspondance avec une autre taxe ou compte, complétez la bonne colonne (Taxe à appliquer/ Compte à utiliser à la place).

![Exemple de la correspondance de taxe d'une position
fiscale](../../../../_images/fiscal-positions-tax-mapping.png) ![Exemple de la
correspondance de compte d'une position fiscale](../../../../_images/fiscal-
positions-account-mapping.png)

  * Pour supprimer une taxe, laissez le champ Taxe à appliquer vide.

  * Pour remplacer une taxe par plusieurs autres taxes, ajoutez plusieurs lignes avec la même Taxe sur le produit.

Note

Les correspondances ne fonctionnent qu’avec des taxes _actives_. Par
conséquent, assurez-vous qu’elles sont actives en allant à Comptabilité ‣
Configuration ‣ Taxes.

## Application

### Application automatique

Pour automatiquement appliquer une position fiscale en fonction d’un ensemble
de conditions, allez à Comptabilité ‣ Configuration ‣ Positions fiscales,
ouvrez la position fiscale à modifier et cochez Détecter automatiquement.

De là, vous pouvez activer plusieurs conditions :

  * TVA requise : le numéro de TVA du client doit figurer sur sa fiche.

  * Groupe de pays et Pays : la position fiscale s’applique uniquement au pays ou au groupe de pays sélectionné.

![Exemple des paramètres d'application automatique d'une position
fiscale](../../../../_images/fiscal-positions-automatic.png)

Note

Les taxes sur les **commandes d’eCommerce** sont automatiquement mises à jour
une fois que le client s’est connecté ou a complété ses coordonnées de
facturation.

Important

La **séquence** des positions fiscales définit la position fiscale à appliquer
si toutes les conditions définies pour plusieurs positions fiscales sont
remplies simultanément.

Par exemple, supposons que la première position fiscale d’une séquence cible
le _pays A_ alors que la deuxième position fiscale cible un _groupe de pays_
qui comprend le _pays A_. Dans ce cas, seule la première position fiscale sera
appliquée aux clients du _pays A_.

### Application manuelle

Pour sélectionner manuellement une position fiscale, ouvrez une commande
client, une facture client ou une facture fournisseur, allez à l’onglet Autres
informations et sélectionnez la Position fiscale souhaitée avant d’ajouter des
lignes de produits.

![Sélection d'une position fiscale sur une commande client, une facture client
ou une facture fournisseur](../../../../_images/fiscal-positions-manual.png)

### Assigner à un partenaire

Pour définir la position fiscale à utiliser par défaut pour un partenaire
spécifique, allez à Comptabilité ‣ Clients ‣ Clients, sélectionnez le
partenaire, ouvrez l’onglet Ventes & Achats et sélectionnez la Position
fiscale.

![Sélection d'une position fiscale sur un client](../../../../_images/fiscal-
positions-customer.png)

Pour plus d'infos

  * [Taxes](../taxes.html)

  * [Intégration TaxCloud](taxcloud.html) (déclassement de l’intégration TaxCloud dans Odoo 17+)

  * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](B2B_B2C.html)

