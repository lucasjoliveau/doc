# Les codes QR de l’EPC

Les codes de réponse rapide du Conseil européen des paiements, ou les **Codes
QR de l’EPC** , sont des codes-barres bidimensionnels que les clients peuvent
scanner avec leurs **applications bancaires mobiles** pour initier un
**virement SEPA** et payer leurs factures instantanément.

En plus d’apporter une certaine facilité d’utilisation et de la rapidité, ces
codes réduisent considérablement les erreurs de saisie qui pourraient
entraîner des problèmes de paiement.

Note

Cette fonctionnalité n’est disponible que pour les entreprises de plusieurs
pays européens tels que l’Autriche, la Belgique, la Finlande, l’Allemagne et
les Pays-Bas.

Pour plus d'infos

  * [Comptes bancaires et d’espèces](../bank.html)

  * [Odoo Académie : Code QR sur les factures des clients européens](https://www.odoo.com/r/VuU)

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres et activez la fonctionnalité
Codes QR dans la section Paiements clients.

### Configurer le journal de votre compte bancaire

Assurez-vous que votre Compte bancaire est correctement configuré dans Odoo
avec votre IBAN et BIC.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux, ouvrez votre
journal de banque, puis complétez le Numéro de compte et la Banque dans la
colonne Numéro de compte bancaire.

![Colonne Numéro de compte bancaire dans le journal de
banque](../../../../_images/bank-journal.png)

## Émettre des factures avec des codes QR de l’EPC

Les Codes QR de l’EPC sont ajoutés automatiquement à vos factures. Les clients
dont la banque prend en charge les paiements par codes QR de l’EPC seront en
mesure de scanner le code et de payer la facture.

Allez à Comptabilité ‣ Clients ‣ Factures, et créez une nouvelle facture.

Avant de la comptabiliser, ouvrez l’onglet Autres informations. Odoo remplit
automatiquement le champ Banque destinataire avec votre IBAN.

Note

Dans l’onglet Autres informations, le compte indiqué dans le champ Banque
destinataire est utilisé pour recevoir le paiement de votre client. Odoo
remplit automatiquement ce champ avec votre IBAN par défaut et l’utilise pour
générer le code QR de l’EPC.

Lorsque la facture est imprimée ou prévisualisée, le code QR figure au bas de
la facture.

![Code QR sur une facture client](../../../../_images/invoice-qr-code.png)

Astuce

Si vous souhaitez émettre une facture sans code QR de l’EPC, supprimez l’IBAN
indiqué dans le champ Banque destinataire dans l’onglet Autres informations de
la facture.

