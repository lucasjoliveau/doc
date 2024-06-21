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

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Plusieurs positions fiscales par défaut sont disponibles dans le cadre de votre <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">package de localisation fiscale</span></a>.</p>
</div>

## Configuration

> ### Correspondances de taxes et de comptes

Pour modifier ou créer une position fiscale, allez à Comptabilité ‣
Configuration ‣ Positions fiscales et ouvrez l’écriture à modifier ou cliquez
sur **Nouveau**.

La correspondance de taxes et de comptes est basée sur les taxes et les
comptes par défaut définis sur la fiche du produit.

  * Pour établir une correspondance avec une autre taxe ou compte, complétez la bonne colonne (**Taxe à appliquer** / **Compte à utiliser à la place**).

![Exemple de la correspondance de taxe d'une position
fiscale](../../../../_images/fiscal-positions-tax-mapping.png) ![Exemple de la
correspondance de compte d'une position fiscale](../../../../_images/fiscal-
positions-account-mapping.png)

  * Pour supprimer une taxe, laissez le champ **Taxe à appliquer** vide.

  * Pour remplacer une taxe par plusieurs autres taxes, ajoutez plusieurs lignes avec la même **Taxe sur le produit**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les correspondances ne fonctionnent qu’avec des taxes <em>actives</em>. Par conséquent, assurez-vous qu’elles sont actives en allant à Comptabilité ‣ Configuration ‣ Taxes.</p>
</div>

## Application

### Application automatique

Pour automatiquement appliquer une position fiscale en fonction d’un ensemble
de conditions, allez à Comptabilité ‣ Configuration ‣ Positions fiscales,
ouvrez la position fiscale à modifier et cochez **Détecter automatiquement**.

De là, vous pouvez activer plusieurs conditions :

  * **TVA requise** : le numéro de TVA du client doit figurer sur sa fiche.

  * **Groupe de pays** et **Pays** : la position fiscale s’applique uniquement au pays ou au groupe de pays sélectionné.

![Exemple des paramètres d'application automatique d'une position
fiscale](../../../../_images/fiscal-positions-automatic.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les taxes sur les <b>commandes d’eCommerce</b> sont automatiquement mises à jour une fois que le client s’est connecté ou a complété ses coordonnées de facturation.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La <b>séquence</b> des positions fiscales définit la position fiscale à appliquer si toutes les conditions définies pour plusieurs positions fiscales sont remplies simultanément.</p>
<p>Par exemple, supposons que la première position fiscale d’une séquence cible le <em>pays A</em> alors que la deuxième position fiscale cible un <em>groupe de pays</em> qui comprend le <em>pays A</em>. Dans ce cas, seule la première position fiscale sera appliquée aux clients du <em>pays A</em>.</p>
</div>

### Application manuelle

Pour sélectionner manuellement une position fiscale, ouvrez une commande
client, une facture client ou une facture fournisseur, allez à l’onglet
**Autres informations** et sélectionnez la **Position fiscale** souhaitée
avant d’ajouter des lignes de produits.

![Sélection d'une position fiscale sur une commande client, une facture client
ou une facture fournisseur](../../../../_images/fiscal-positions-manual.png)

### Assigner à un partenaire

Pour définir la position fiscale à utiliser par défaut pour un partenaire
spécifique, allez à Comptabilité ‣ Clients ‣ Clients, sélectionnez le
partenaire, ouvrez l’onglet **Ventes & Achats** et sélectionnez la **Position
fiscale**.

![Sélection d'une position fiscale sur un client](../../../../_images/fiscal-
positions-customer.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
<li><p><a href="taxcloud">Intégration TaxCloud</a> (déclassement de l’intégration TaxCloud dans Konvergo ERP 17+)</p></li>
<li><p><a href="B2B_B2C">Prix B2B (hors taxes) et B2C (toutes taxes comprises)</a></p></li>
</ul>
</div>

