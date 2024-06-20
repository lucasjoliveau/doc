# Intégrer des coûts additionnels aux produits (coûts logistiques)

La fonctionnalité des coûts logistiques dans Odoo permet à l’utilisateur
d’inclure des coûts additionnels (expédition, assurance, droits de douane,
etc.) dans le coût du produit.

## Configuration

Allez d’abord à Inventaire ‣ Configuration ‣ Paramètres ‣ Valorisation et
activez la fonctionnalité Coûts logistiques. Odoo donne également la
possibilité de définir un journal par défaut dans lequel les écritures
comptables des coûts logistiques seront enregistrées.

![Activer la fonctionnalité des coûts logistiques dans les paramètres de
l'inventaire.](../../../../../_images/landed-costs-setting.png)

## Ajouter les coûts aux produits

### Recevoir la facture fournisseur

Après qu’un fournisseur a rempli un bon de commande et envoyé une facture,
cliquez sur Créer une facture sur le bon de commande pour créer une facture
fournisseur dans Odoo. Si la facture fournisseur contient des coûts
logistiques, tels que les droits de douane, cochez la case dans la colonne
Coûts logistiques sur la ligne de la facture fournisseur.

![Activer l'option des coûts logistiques sur une ligne d'une facture
fournisseur.](../../../../../_images/landed-costs-field-vendor-bill.png)

Pour les frais qui sont toujours des coûts logistiques, créez un produit coût
logistique dans Odoo. De cette façon, le produit coût logistique peut être
facilement ajouté à la facture fournisseur en tant que ligne de facture au
lieu de saisir manuellement les informations relatives aux coûts logistiques
chaque fois qu’une facture fournisseur arrive.

Créez d’abord un nouveau produit dans Inventaire ‣ Produits ‣ Produits ‣
Créer. Ensuite, donnez un nom au produit coût logistique et définissez le type
de produit sur Service. Un produit coût logistique doit toujours être un type
de produit service. Après cela, allez à l’onglet Achat et cochez la case à
côté de Est un coût logistique. Finalement, cliquez sur Enregistrer pour
finaliser la création d’un produit coût logistique.

Si ce produit est toujours un coût logistique, vous pouvez également le
définir sur le produit et éviter de devoir cocher la case sur chaque facture
fournisseur.

![Option pour définir un produit comme un coût
logistique.](../../../../../_images/product-is-landed-cost.png)

Une fois le coût logistique ajouté à la facture fournisseur (soit en cochant
l’option Coût logistique sur la ligne de facture ou en ajoutant un produit de
coût logistique à la facture), cliquez sur le bouton Créer des coûts
logistiques en haut de la facture. Odoo crée automatiquement un enregistrement
de coût logistique avec le coût logistique prérempli dans les lignes de
produit Coûts additionnels. À partir de là, décidez à quel transfert les coûts
additionnels s’appliquent en cliquant sur Modifier et en sélectionnant le
numéro de référence du transfert dans le menu déroulant Transferts. Cliquez
finalement sur Enregistrer.

![Utiliser un transfert d'entrepôt pour couvrir un coût logistique dans le
journal comptable.](../../../../../_images/warehouse-transfer-landed-
costs.png)

Après avoir défini le transfert, cliquez sur Calculer sur l’enregistrement du
coût logistique. Ensuite, allez à l’onglet Correction de valorisation pour
voir l’impact des coûts logistiques. Finalement, cliquez sur Valider pour
enregistrer l’écriture de coût logistique dans le journal comptable.

L’utilisateur peut accéder à la pièce comptable qui a été créée par le coût
logistique en cliquant sur Pièce comptable.

Note

Le produit auquel le coût logistique s’applique doit avoir une catégorie de
produit définie sur une méthode FIFO ou AVCO.

![Pièce comptable d'un coût logistique](../../../../../_images/landed-cost-
journal-entry.png)

Note

Les enregistrements de coût logistique peuvent être créés directement dans
Inventaire ‣ Opérations ‣ Coûts logistiques, il n’est pas nécessaire de créer
un enregistrement de coût logistique à partir de la facture fournisseur.

  *[FIFO]: First In, First Out
  *[AVCO]: coût moyen

