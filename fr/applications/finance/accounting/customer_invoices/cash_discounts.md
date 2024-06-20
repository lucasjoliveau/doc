# Escomptes et réduction d’impôt

Les **escomptes** sont des réductions du montant qu’un client doit payer pour
des biens ou des services, afin de l’inciter à payer sa facture rapidement.
Ces escomptes représentent généralement un pourcentage de la facture totale et
sont appliqués si le client paie endéans un délai déterminé. Les escomptes
peuvent aider l’entreprise à maintenir un flux de trésorerie régulier.

Example

Vous émettez une facture de 100 € le 1er janvier. Le paiement intégral est dû
endéans les 30 jours et vous offrez également une remise de 2% si le client
vous paie dans les sept jours.

Le client peut payer 98 € jusqu’au 8 janvier. Passé cette date, il devra payer
100 € avant le 31 janvier.

Une réduction d’impôt peut également s’appliquer en fonction du pays ou de la
région.

## Configuration

Pour accorder des escomptes aux clients, vous devez d’abord configurer le type
de réduction d’impôt, vérifier les comptes des gains et des pertes, et
configurer de nouvelles conditions de paiement.

### Réductions d’impôt

En fonction du pays ou de la région, le montant de base utilisé pour calculer
la taxe peut varier, ce qui peut entraîner une **réduction d’impôt**.

Pour configurer l’application de la réduction d’impôt, allez à Comptabilité ‣
Configuration ‣ Paramètres, et dans la section Taxes, dans la fonctionnalité
Réduction d’impôt pour escompte, sélectionnez l’une des trois options
suivantes :

Toujours (sur facture)

    

L’impôt est toujours réduit. Le montant de base utilisé pour calculer la taxe
est le montant escompté, que le client bénéficie de l’escompte ou non.

En cas de paiement anticipé

    

L’impôt est réduit uniquement si le client effectue un paiement anticipé. Le
montant de base utilisé pour calculer la taxe est le même que celui de la
vente : si le client bénéficie de la réduction, la taxe est réduite. Cela
signifie que, selon le client, le montant de l’impôt peut varier après
l’émission de la facture.

Jamais

    

L’impôt n’est jamais réduit. Le montant de base utilisé pour calculer la taxe
est le montant intégral, que le client bénéficie de l’escompte ou non.

Example

Vous émettez une facture de 100 € (hors taxes) le 1er janvier, avec une taxe
de 21%. Le paiement intégral est dû endéans les 30 jours et vous offrez
également une remise de 2% si votre client vous paie endéans les sept jours.

Always (upon invoice)On early paymentNever

Date d’échéance | Montant total dû | Calcul  
---|---|---  
8 janvier | 118,58 € | (98 € + (21% de 98 €))  
31 janvier | 120,58 € | (100 € + (21% de 98 €))  
  
Date d’échéance | Montant total dû | Calcul  
---|---|---  
8 janvier | 118,58 € | (98 € + (21% de 98 €))  
31 janvier | 121,00 € | (100 € + (21% de 100 €))  
  
Date d’échéance | Montant total dû | Calcul  
---|---|---  
8 janvier | 119,00 € | (98 € + (21% de 100 €))  
31 janvier | 121,00 € | (100 € + (21% de 100 €))  
  
Note

  * Les [grilles fiscales](../reporting/tax_returns.html#tax-returns-tax-grids), qui sont utilisées pour la déclaration de TVA, sont calculées correctement en fonction du type de réduction d’impôt que vous avez configuré.

  * Le **type de réduction d’impôt pour escompte** peut être correctement préconfiguré, en fonction de votre [package de localisation fiscale](../../fiscal_localizations.html#fiscal-localizations-packages).

### Comptes des pertes/gains d’escompte

Dans le cas d’un escompte, le montant que vous gagnez dépend du fait que le
client bénéficie ou non de l’escompte. Cela entraîne inévitablement des gains
et des pertes, qui sont enregistrés sur des comptes par défaut.

Pour modifier ces comptes, allez à Comptabilité ‣ Configuration ‣ Paramètres,
et dans la section Comptes par défaut, sélectionnez les comptes que vous
souhaitez utiliser pour le Compte des gains d’escompte et le Compte des pertes
d’escompte.

### Délais de paiement

Les escomptes sont définis sur les [conditions de
paiement](payment_terms.html). Configurez-les à votre guise en allant à
Comptabilité ‣ Configuration ‣ Conditions de paiement, et assurez-vous de
compléter les champs % de remise et Jours d’escompte.

![Configuration des conditions de paiement nommées "2/7 Net 30". Le champ
"Description sur les factures" indique : "Conditions de paiement : 30 jours,
2% d'escompte pour paiement anticipé endéans les 7
jours".](../../../../_images/payment-terms.png)

Pour plus d'infos

[Conditions de paiement et plans de paiement échelonné](payment_terms.html)

## Appliquer un escompte à une facture client

Appliquez un escompte à une facture client en sélectionnant les conditions de
paiement que vous avez créées. Odoo calcule automatiquement les montants
corrects, les montants de taxe, les dates d’échéance et les enregistrements
comptables.

Dans l’onglet Écritures comptables, vous pouvez afficher les détails de
l’escompte en cliquant sur le bouton de « basculement » et en ajoutant les
colonnes Date de la remise et Montant de la remise.

![Une facture de 100,00 € pour laquelle "2/7 Net 30" est sélectionnée comme
condition de paiement. L'onglet "Écritures comptables" est ouvert et les
colonnes "Date de la remise" et "Montant de la remise" sont
affichées.](../../../../_images/invoice-journal-entry.png)

Le montant de la remise et la date d’échéance s’affichent également sur la
facture générée et envoyée au client.

![Une facture de 100,00 € avec le texte suivant ajouté aux conditions
générales : "30 jours, 2% d'escompte pour paiement anticipé endéans les 7
jours. 118,58 € sont dus si paiement avant le
08/01/2023."](../../../../_images/invoice-print.png)

### Rapprochement des paiements

Lorsque vous enregistrez un paiement ou rapprochez vos relevés bancaires, Odoo
prend en compte la date du paiement du client pour définir s’il peut
bénéficier ou non de l’escompte.

Note

Si votre client paie le montant de l’escompte _après_ la date de a remise,
vous pouvez toujours décider de marquer la facture comme entièrement payée
avec une écriture d’annulation ou comme partiellement payée.

Pour plus d'infos

[Paiements](../payments.html)

