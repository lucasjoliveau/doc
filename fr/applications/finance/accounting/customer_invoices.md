# Factures clients

## De la facture client à l’encaissement des paiements

Odoo prend en charge plusieurs flux de facturation et de paiement, de sorte
que vous pouvez choisir et utiliser ceux qui correspondent à vos activités.
Que vous souhaitiez accepter un seul paiement pour une seule facture ou
traiter un paiement couvrant plusieurs factures et accorder des remises pour
les paiements anticipés, vous pouvez le faire de manière efficace et précise.

### De la facture brouillon au compte de résultat

Si nous reprenons à la fin d’un scénario typique “commande à encaissement”,
après que les marchandises ont été expédiées, vous devez : émettre une facture
; recevoir le paiement ; déposer le paiement à la banque ; vous assurer que la
facture client est clôturée ; assurer le suivi si les clients accusent un
retard ; et enfin présenter vos revenus sur le compte de résultat et afficher
la diminution de l’actif sur le bilan.

Dans la plupart des pays, la facturation se produit lorsque une obligation
contractuelle est remplie. Si vous expédiez un colis à un client, vous avez
rempli les conditions du contrat et vous pouvez procéder à la facturation. Si
votre fournisseur vous envoie un colis, il a respecté les conditions du
contrat et il peut vous envoyer une facture. Par conséquent, les conditions du
contrat sont respectées lorsque le colis se déplace vers ou depuis le camion.
À ce stade, Odoo permet la création de ce qu’on appelle une facture brouillon
par le personnel de l’entrepôt.

### Création d’une facture

Les factures brouillon peuvent être générées manuellement à partir d’autres
documents tels que les commandes clients, les bons de commande, etc. Vous
pouvez également créer directement une facture brouillon si vous le souhaitez.

Une facture client doit contenir toutes les informations nécessaires pour que
le client puisse payer les marchandises et les services commandés et livrés.
Elle doit également inclure d’autres informations nécessaires au paiement de
la facture en temps voulu et de manière précise.

### Factures brouillon

The system generates invoice which are initially set to the Draft state. While
these invoices remain unvalidated, they have no accounting impact within the
system. There is nothing to stop users from creating their own draft invoices.

Créons une facture client contenant les informations suivantes :

  * Client : Agrolait

  * Produit : iMac

  * Quantité : 1

  * Prix unitaire : 100

  * Taxes : TVA 15%

![../../../_images/invoice01.png](../../../_images/invoice01.png)
![../../../_images/invoice02.png](../../../_images/invoice02.png)

Le document est composé de trois parties :

  * L’en-tête de la facture, contenant les informations relatives au client,

  * le corps principal de la facture, contenant des lignes de factures détaillées,

  * le bas de la page, contenant des détails sur les taxes, et les totaux.

### Factures ouvertes ou pro forma

Une facture comprendra généralement la quantité et le prix des biens et/ou des
services, la date, toutes les parties impliquées, le numéro de facture unique
et toute information fiscale.

« Validez » la facture lorsque vous êtes prêt à l’approuver. La facture passe
alors du statut Brouillon au Statut Ouvert.

Lorsque vous avez validé une facture, Odoo lui donne un numéro unique à partir
d’une séquence définie et modifiable.

![../../../_images/invoice03.png](../../../_images/invoice03.png)

Les pièces comptables correspondant à cette facture sont générées
automatiquement lorsque vous validez la facture. Vous pouvez voir les détails
en cliquant sur l’écriture dans le champ Pièce comptable dans l’onglet «
Autres informations ».

![../../../_images/invoice04.png](../../../_images/invoice04.png)

### Envoyer la facture au client

Après avoir validé la facture du client, vous pouvez l’envoyer directement au
client via la fonctionnalité “Envoyer par email”.

![../../../_images/invoice05.png](../../../_images/invoice05.png)

Une pièce comptable typique générée à partir d’une facture validée se présente
comme suit :

**Compte** | **Partenaire** | **Date d’échéance** | **Débit** | **Crédit**  
---|---|---|---|---  
Comptes clients | Agrolait | 07/01/2015 | 115 |   
Taxes | Agrolait |  |  | 15  
Ventes |  |  |  | 100  
  
### Paiement

Dans Odoo, une facture est considérée comme payée lorsque la pièce comptable
associée a été lettrée avec le paiement. S’il n’y a pas eu de lettrage, le
statut de la facture restera Ouvert jusqu’à ce que vous avez enregistré le
paiement.

Une pièce comptable typique générée par un paiement se présente comme suite :

**Compte** | **Partenaire** | **Date d’échéance** | **Débit** | **Crédit**  
---|---|---|---|---  
Banque | Agrolait |  | 115 |   
Comptes clients | Agrolait |  |  | 115  
  
### Recevoir un paiement partiel par le relevé bancaire

Vous pouvez manuellement saisir vos relevés bancaires dans Odoo ou vous pouvez
les importer depuis un fichier csv ou d’autres formats prédéfinis en fonction
de votre localisation comptable.

Créez un relevé bancaire depuis le tableau de bord de la comptabilité, dans le
journal approprié, et saisissez un montant de 100 $.

![../../../_images/invoice06.png](../../../_images/invoice06.png)

### Rapprocher

Passons à présent au rapprochement !

![../../../_images/invoice07.png](../../../_images/invoice07.png)

Vous pouvez maintenant passer en revue chaque transaction et la rapprocher ou
vous pouvez effectuer un rapprochement en masse en suivant les instructions
ci-dessous.

Après avoir rapproché les écritures sur la feuille, la facture correspondante
affichera alors « Vous avez des paiements en suspens pour ce client. Vous
pouvez les rapprocher pour payer cette facture. »

![../../../_images/invoice08.png](../../../_images/invoice08.png)
![../../../_images/invoice09.png](../../../_images/invoice09.png)

Appliquez le paiement. Ci-dessous, vous pouvez voir que le paiement a été
ajouté à la facture.

![../../../_images/invoice10.png](../../../_images/invoice10.png)

### Suivi du paiement

Les clients ont tendance à payer leurs factures de plus en plus tard. Par
conséquent, les agents de recouvrement doivent faire tout leur possible pour
recouvrer l’argent et le recouvrer plus rapidement.

Odoo vous aide à définir votre stratégie de suivi. Pour rappeler aux clients
de payer leurs factures impayées, vous pouvez définir différentes actions en
fonction de l’importance de retard du client. Ces actions sont regroupées dans
des niveaux de suivi qui sont déclenchés lorsque la date d’échéance de la
facture dépasse un certain nombre de jours. Si ce même client a d’autres
factures impayées, les actions de la facture la plus en retard seront
exécutées.

En allant à la fiche du client, dans les « Paiements en retard », vous verrez
le message de suivi et toutes les factures en retard.

![../../../_images/invoice11.png](../../../_images/invoice11.png)
![../../../_images/invoice12.png](../../../_images/invoice12.png)

#### Balance âgée des clients :

Le balance âgée des clients est un outil clé supplémentaire qui permet à
l’agent de recouvrement de comprendre les problèmes de crédit du client et de
prioriser son travail.

Utilisez la balance âgée des clients pour déterminer quels clients accusent
des retards et commencer vos efforts de recouvrement.

![../../../_images/invoice13.png](../../../_images/invoice13.png)

### Compte de résultat

Le compte de résultat affiche les détails de vos produits et de vos charges.
En fin de compte, il vous donne un aperçu clair de vos pertes et profits nets.
Il est parfois appelé le « compte de profits et pertes ».

![../../../_images/invoice14.png](../../../_images/invoice14.png)

### Bilan

Le bilan résume le passif, l’actif et les fonds propres de votre entreprise à
un moment précis.

![../../../_images/invoice15.png](../../../_images/invoice15.png)
![../../../_images/invoice16.png](../../../_images/invoice16.png)

Par exemple, si vous gérez vos stocks selon la méthode de l’inventaire
permanent, vous devez vous attendre à une diminution du compte « Actifs
circulants » une fois que le matériel a été expédié au client.

  * [Processus de facturation](customer_invoices/overview.html)
  * [Adresses de livraison et de facturation](customer_invoices/customer_addresses.html)
  * [Conditions de paiement et plans de paiement échelonné](customer_invoices/payment_terms.html)
  * [Conditions générales par défaut (CG)](customer_invoices/terms_conditions.html)
  * [Escomptes et réduction d’impôt](customer_invoices/cash_discounts.html)
  * [Avoirs et remboursements](customer_invoices/credit_notes.html)
  * [Arrondi des paiements en espèces](customer_invoices/cash_rounding.html)
  * [Produits constatés d’avance](customer_invoices/deferred_revenues.html)
  * [Facturation électronique (EDI)](customer_invoices/electronic_invoicing.html)
  * [Envoi postal](customer_invoices/snailmail.html)
  * [Les codes QR de l’EPC](customer_invoices/epc_qr_code.html)
  * [Incoterms](customer_invoices/incoterms.html)

  *[EDI]: échange de données informatisé

