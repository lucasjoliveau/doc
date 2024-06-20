# TVA sur encaissements

La TVA sur encaissements est due lorsque le paiement est effectué,
contrairement aux taxes standards qui sont dues lorsque la facture est
confirmée. Dans certains pays et sous certaines conditions, il est obligatoire
de déclarer ses recettes et ses dépenses à l’administration selon la méthode
de la comptabilité de trésorerie.

Example

Vous vendez un produit au cours du premier trimestre de votre exercice fiscal
et vous recevez le paiement au cours du deuxième trimestre. Selon la méthode
de la comptabilité de trésorerie, vous devez payer la taxe pour le deuxième
trimestre.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres et dans la section Taxes,
activez Comptabilité de trésorerie.

Définissez ensuite le Journal basé sur la comptabilité de trésorerie. Cliquez
sur le bouton de lien externe à côté du journal afin de mettre à jour ses
propriétés par défaut telles que le Nom du journal, le Type ou le Code.

![Sélectionnez votre journal basé sur la comptabilité de trésorerie et cliquez
sur le lien externe](../../../../_images/tax_cash_basis_journal.png)

Note

Par défaut, les pièces comptables du journal basé sur la TVA sur encaissements
sont nommées à l’aide du code CABA.

Une fois que cela est fait, allez à Comptabilité ‣ Configuration ‣
Comptabilité : Taxes pour configurer vos taxes. Vous pouvez soit créer une
nouvelle taxe, soit mettre à jour une taxe existante en cliquant dessus.

La colonne Compte représente les comptes d’attente sur lesquels enregistrer
les taxes jusqu’à ce que le paiement est enregistré.

![Complétez la colonne de compte avec les comptes d'attente sur lesquels les
taxes sont enregistrés jusqu'à ce que le paiement est
enregistré](../../../../_images/account_column.png)

Dans l’onglet Options avancées, décidez de l”Exigibilité fiscale. Sélectionnez
Basé sur le paiement, pour que la taxe soit due lors de la réception du
paiement de la facture. Vous pouvez également définir le Compte d’attente pour
la TVA sur encaissements sur lequel le montant de la taxe est enregistré tant
que la facture originale n’est pas lettrée.

![Complétez le compte d'attente pour la TVA sur encaissements sur lequel le
montant des taxes est enregistré jusqu'à ce que le paiement est
lettré.](../../../../_images/advanced_options.png)

## Impact de la TVA sur encaissements sur la comptabilité

Pour illustrer l’impact de la TVA sur encaissements sur les transactions
comptables, prenons un exemple avec la vente d’un produit qui coûte 1.000 $,
avec une TVA sur encaissements de 15%.

![](../../../../_images/customer_invoice_with_cbt.png)

Les écritures suivantes sont créées dans votre comptabilité et la déclaration
de TVA est actuellement vide.

**Journal du client (INV)**  
---  
**Débit** | **Crédit**  
Créances 1.150 $ |   
| Revenus 1.000 $  
| Compte d’attente 150 $  
  
Lorsque le paiement est reçu, il est enregistré comme suit :

**Journal bancaire (BANK)**  
---  
**Débit** | **Crédit**  
Banque 1.150 $ |   
| Créances 1.150 $  
  
Note

Une fois que le paiement est enregistré, vous pouvez utiliser le bouton
intelligent Écritures de comptabilité de trésorerie sur la facture pour y
accéder directement.

Enfin, lors du lettrage de la facture avec le paiement, l’écriture suivante
est créée automatiquement :

**Journal basé sur la comptabilité de trésorerie (Caba)**  
---  
**Débit** | **Crédit**  
Compte des revenus 1.000 $ |   
Compte d’attente 150 $ |   
| Compte des revenus 1.000 $  
| Taxe reçue 150 $  
  
Les écritures comptables Compte des revenus vs. Compte des revenus sont
neutres, mais ils sont nécessaires pour assurer une déclaration de TVA
correcte dans Odoo avec des montants de base de base exacts.

Il est recommandé d’utiliser un Compte de base de la taxe perçue pour que
votre solde soit à zéro et que votre compte des revenus ne soit pas pollué par
des mouvements comptables inutiles. Pour ce faire, allez à Configuration ‣
Paramètres ‣ Taxes, et sélectionnez Compte de base de la taxe perçue sous
Comptabilité de trésorerie.

