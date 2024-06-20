# Conditions de paiement et plans de paiement échelonné

Les **Conditions de paiement** précisent toutes les conditions pour payer une
vente pour aider les clients à payer leurs factures correctement et à temps.

Les conditions de paiement sont générales définies sur des documents tels que
des commandes clients, des factures clients et des factures fournisseurs. Les
conditions de paiement couvrent :

  * La (les) date(s) d’échéance

  * Les escomptes

  * Toute autre condition de paiement

Un **plan de paiement échelonné** permet aux clients de régler une facture en
plusieurs fois, les montants et les dates de paiement étant définis
préalablement par le fournisseur.

Example

Paiement immédiat

    

Le paiement intégral est dû le jour de l’émission de la facture.

15 jours (ou Net 15)

    

Le paiement intégral est dû 15 jours après la date de facturation.

21 MFI

    

Le paiement intégral est dû pour le 21ème du mois suivant la date de
facturation.

30% d’avance, fin du mois suivant

    

30% sont dus le jour de l’émission de la facture. Le solde est dû à la fin du
mois suivant.

2% 10, Net 30 EOM

    

Un [escompte](cash_discounts.html) de 2% est accordé si le paiement est reçu
dans les dix jours. Sinon, le paiement intégral est dû à la fin du mois
suivant la date de facturation.

Note

  * Il ne faut pas confondre les conditions de paiement et les [factures d’acompte](../../../sales/sales/invoicing/down_payment.html). Si vous émettez plusieurs factures à votre client pour une commande spécifique, il ne s’agit ni d’une condition de paiement, ni d’un plan de paiement échelonné, mais d’une politique de facturation.

  * Cette page parle des _conditions de paiement_ et non des [conditions générales](terms_conditions.html), qui peuvent être utilisées pour déclarer des obligations contractuelles concernant l’utilisation du contenu, les politiques de retour et d’autres politiques relatives à la vente de biens et de services.

Pour plus d'infos

  * [Tutoriels Odoo : conditions de paiement](https://www.odoo.com/slides/slide/payment-terms-1679)

  * [Escomptes et réduction d’impôt](cash_discounts.html)

## Configuration

Pour créer de nouvelles conditions de paiement, suivez les étapes suivantes :

  1. Allez à Comptabilité ‣ Configuration ‣ Conditions de paiement et cliquez sur Nouveau.

  2. Saisissez un nom dans le champ Conditions de paiement. Ce champ est le nom affiché dans la base de données et ne s’affiche pas au client.

  3. Saisissez le texte à afficher sur le document (commande, facture, etc.) dans le champ Description sur la facture.

  4. Cochez la case Afficher les conditions sur la facture pour afficher le détail de chaque paiement et sa date d’échéance sur la facture si vous le souhaitez.

  5. Dans la section Conditions, ajoutez un ensemble de règles (délais) pour définir la somme à payer et à quelle(s) date(s) d’échéance. La définition des conditions permet de calculer automatiquement la (les) date(s) d’échéance des paiements. Cette fonction est particulièrement utile pour gérer les **plans de paiement échelonné** (conditions de paiement comportant plusieurs échéances).

Pour ajouter une échéance, cliquez sur Ajouter une ligne, définissez le Type
d’échéance et la Valeur et remplissez les champs appropriés pour définir la
date d’échéance de l’échéance, y compris les éventuelles
[remises](cash_discounts.html). Les dates d’échéance sont calculées en prenant
la date de facturation, en ajoutant d’abord les Mois et puis les Jours. Si
l’option Fin de mois est activée, la date d’échéance sera alors la fin de ce
mois, plus les Jours après la fin du mois.

Astuce

Au lieu de préciser un nombre de jours _avant la fin du mois_ , utilisez une
valeur négative dans le champ Jours après la fin du mois.

Pour tester que vos conditions de paiement sont configurées correctement,
saisissez un montant et une date de facture dans la section Exemple pour
générer les paiements qui seraient dus et leurs dates d’échéance en utilisant
ces conditions de paiement.

Important

  * Les conditions sont calculées dans l’ordre de leurs échéances.

  * Le **solde** doit toujours être utilisé pour la dernière ligne.

Example

Dans l’exemple suivant, 30% sont dus le jour de l’émission de la facture et le
solde est dû à la fin du mois suivant.

![Exemple de conditions de paiement. La dernière ligne est le solde dû le
31ème du mois suivant.](../../../../_images/configuration.png)

## Utiliser des conditions de paiement

Les conditions de paiement peuvent être définies par le biais du champ
Conditions de paiement dans :

  * **Contacts :** Pour automatiquement configurer des conditions de paiement sur les nouvelles commandes, factures clients et factures fournisseurs d’un contact. Elles peuvent être modifiées dans le fiche du contact, dans l’onglet Ventes & Achats.

  * **Devis/Commandes :** Pour automatiquement définir des conditions de paiement sur toutes les factures générées à partir d’un devis ou d’une commande.

Les conditions de paiement peuvent être définies dans le champ Date
d’échéance, à l’aide de la liste déroulante Conditions sur :

  * **Factures clients :** Pour définir des conditions de paiement spécifiques sur une facture client.

  * **Factures fournisseurs :** Pour définir des conditions de paiement sur une facture fournisseur.

Astuce

La définition de conditions de paiement sur une facture fournisseur est
surtout utile pour gérer des conditions de paiement du fournisseur avec
plusieurs versements ou escomptes. Sinon, il suffit de définir manuellement la
**date d’échéance**. Si des conditions de paiement sont déjà définies, videz
le champ pour sélectionner une date.

## Pièces comptables

Les factures avec des conditions de paiement spécifiques génèrent différentes
_pièces comptables_ , avec une _écriture comptable_ pour chaque _date
d’échéance_ calculée.

Cela facilite les [suivis](../payments/follow_up.html) et le
[lettrage](../bank/reconciliation.html), car Odoo prend en compte chaque date
d’échéance, plutôt que la seule date d’échéance du solde. Cela permet
également d’obtenir une [balance âgée des
clients](../customer_invoices.html#customer-invoices-aging-report) précise.

Example

![Le montant débité du compte client est divisé en deux écritures comptables
avec des dates d'échéance distinctes](../../../../_images/journal-entry.png)

Dans cet exemple, une facture de 1.000 $ a été émise avec les conditions de
paiement suivantes : _30% sont dus le jour de l’émission et le solde est dû à
la fin du mois suivant._

Compte | Date d’échéance | Débit | Crédit  
---|---|---|---  
Compte client | 21 février | 300 |   
Compte client | 31 mars | 700 |   
Ventes de produits |  |  | 1.000  
  
Les 1.000 $ débités du compte client sont divisés en deux écritures comptables
distinctes. Les deux ont leur propre date d’échéance.

