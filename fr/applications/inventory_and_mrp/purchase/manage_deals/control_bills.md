# Politiques de contrôle des factures

Dans Odoo, la politique de _contrôle des factures_ détermine les quantités
facturées par les fournisseurs sur chaque bon de commande, pour les quantités
commandées et reçues. La politique sélectionnée dans les paramètres sera la
valeur par défaut et s’appliquera à chaque nouveau produit créé.

## Configuration

Pour afficher la politique de contrôle des factures et effectuer des
changements, allez à Achats ‣ Configuration ‣ Paramètres et descendez jusqu’à
la section Facturation. Vous y trouverez deux options de politique de Contrôle
des factures : Quantités commandées et Quantités reçues.

La politique sélectionnée sera la politique par défaut pour chaque nouveau
produit créé. Les politiques sont définies comme suit :

  * Quantités commandées : crée une facture fournisseur dès qu’un bon de commande est confirmé. Les produits et les quantités du bon de commande sont utilisés pour générer une facture brouillon.

  * Quantités reçues : une facture fournisseur n’est créée qu” _après_ la réception d’une partie de la commande totale. Les produits et les quantités _reçus_ sont utilisés pour générer une facture brouillon. Un message d’erreur apparaîtra si l’on tente de créer une facture fournisseur sans avoir reçu quoi que ce soit.

![Message d'erreur concernant la politique de contrôle des
factures.](../../../../_images/bill-control-policy-error-message.png)

Note

Si un ou deux produits nécessitent une politique de contrôle différente, le
paramètre de contrôle des factures par défaut peut être remplacé en allant à
l’onglet Achats du modèle d’un produit et en modifiant le champ Politique de
contrôle.

### Exemple de flux : Quantités commandées

Pour réaliser un exemple de flux de travail utilisant la politique de contrôle
des factures des _quantités commandées_ , allez d’abord à Achats ‣
Configuration ‣ Paramètres, descendez jusqu’à la section Facturation et
sélectionnez Quantités commandées. Ensuite, cliquez sur Enregistrer pour
enregistrer les changements.

Dans l’application Achats, créez une nouvelle demande de prix. Complétez les
informations du formulaire de devis, ajoutez des produits aux lignes de la
facture et cliquez sur Confirmer la commande. Cliquez ensuite sur Créer une
facture fournisseur. Puisque la politique est définie sur _quantités
commandées_ , la facture brouillon peut être confirmée dès sa création, sans
qu’aucun produit n’ait été reçu.

### Exemple de flux : Quantités reçues

Pour réaliser un exemple de flux de travail utilisant la politique de contrôle
des factures des _quantités reçues_ , allez d’abord à Achats ‣ Configuration ‣
Paramètres, descendez jusqu’à la section Facturation et sélectionnez Quantités
reçues. Ensuite, cliquez sur Enregistrer pour enregistrer les changements.

Dans l’application Achats, créez une nouvelle demande de prix. Complétez les
informations du devis, ajoutez des produits aux lignes de la facture et
cliquez sur Confirmer la commande. Cliquez ensuite sur le bouton intelligent
Réception. Définissez les quantités dans la colonne Fait pour correspondre aux
quantités dans la colonne Demande et validez les changements. Ensuite, dans le
bon de commande, cliquez sur Créer une facture fournisseur et confirmez.
Puisque la politique est définie sur _quantités reçues_ , la facture brouillon
ne sera confirmée _que_ lorsqu’au moins une partie des quantités est reçue.

## Correspondance à trois voies

L’activation de la correspondance à trois voies assure que les factures
fournisseurs ne sont payées que lorsque certains produits ou tous les produits
du bon de commande ont été reçus. Pour l’activer, allez à Achats ‣
Configuration ‣ Paramètres et descendez jusqu’à la section Facturation.
Ensuite, cliquez sur Correspondance à trois voies : achats, réceptions et
factures.

Note

La correspondance à trois voies est _uniquement_ conçue pour fonctionner
lorsque la politique de contrôle des factures est définie sur _quantités
reçues_.

### Payer des factures fournisseurs avec la correspondance à trois voies

Lorsque la correspodance à trois voies est activée, les factures fournisseurs
seront affichées dans le champ Doit être payée dans l’onglet Autres
informations. Lorsqu’une nouvelle facture fournisseur est créée, ce champ sera
défini sur Oui, puisqu’il n’est pas possible de créer une facture avant qu’au
moins une partie des produits du bon de commande ait été reçue.

![Statut Doit être payée d'une facture brouillon.](../../../../_images/vendor-
bill-should-be-paid.png)

Note

Si la quantité totale de produits d’un bon de commande n’a pas été reçue, Odoo
n’inclut que les produits qui _ont_ été reçus dans la facture fournisseur
brouillon.

Les factures brouillon peuvent être éditées pour augmenter la quantité
facturée, changer le prix des produits sur la facture et ajouter des produits
additionnels à la facture. Une fois cela fait, le statut du champ Doit être
payée sera défini sur Exception. Ceci signifie que Odoo remarque l’anomalie,
mais ne bloque pas les modifications ou n’affiche pas de message d’erreur,
puisqu’il pourrait y avoir une raison valide pour apporter des modifications à
la facture brouillon.

Une fois que le paiement a été enregistré pour une facture fournisseur et
qu’elle affiche la bannière verte Payé, le statut de champ Doit être payée
sera défini sur Non.

Astuce

Le statut Doit être payée sur les factures est défini automatiquement par
Odoo. Cependant, le statut peut être modifié manuellement en cliquant sur le
menu déroulant du champ dans l’onglet Autres informations.

## Vue du statut de facturation d’un bon de commande

Lorsqu’un bon de commande est confirmé, son Statut de facturation peut
s’afficher sous l’onglet Autres informations sur le formulaire du bon de
commande.

![Statut de facturation du bon de commande.](../../../../_images/billing-
status-nothing-to-bill.png)

Vous trouverez ci-dessous la liste des statuts différents que peut revêtir un
Statut de facturation et du moment où ils sont affichés, en fonction de la
politique de contrôle des factures utilisée.

Statut de facturation | **Conditions**  
---|---  
_Quantités reçues_ | _Quantités commandées »_  
Rien à facturer | Bon de commande confirmé ; aucun produit reçu | _Non applicable_  
Factures en attente | Tous/quelques produits reçus ; facture non créée | Bon de commande confirmé  
Entièrement facturé | Tous/quelques produits reçus ; facture brouillon créée | Facture brouillon créée

