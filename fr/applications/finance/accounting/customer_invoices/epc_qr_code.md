# Les codes QR de l’EPC

Les codes de réponse rapide du Conseil européen des paiements, ou les **Codes
QR de l’EPC** , sont des codes-barres bidimensionnels que les clients peuvent
scanner avec leurs **applications bancaires mobiles** pour initier un
**virement SEPA** et payer leurs factures instantanément.

En plus d’apporter une certaine facilité d’utilisation et de la rapidité, ces
codes réduisent considérablement les erreurs de saisie qui pourraient
entraîner des problèmes de paiement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cette fonctionnalité n’est disponible que pour les entreprises de plusieurs pays européens tels que l’Autriche, la Belgique, la Finlande, l’Allemagne et les Pays-Bas.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../bank">Comptes bancaires et d’espèces</a></p></li>
<li><p><a href="https://www.odoo.com/r/VuU">Konvergo ERP Académie : Code QR sur les factures des clients européens</a></p></li>
</ul>
</div>

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres et activez la fonctionnalité
**Codes QR** dans la section **Paiements clients**.

### Configurer le journal de votre compte bancaire

Assurez-vous que votre **Compte bancaire** est correctement configuré dans
Konvergo ERP avec votre IBAN et BIC.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux, ouvrez votre
journal de banque, puis complétez le **Numéro de compte** et la **Banque**
dans la colonne **Numéro de compte bancaire**.

![Colonne Numéro de compte bancaire dans le journal de
banque](../../../../_images/bank-journal.png)

## Émettre des factures avec des codes QR de l’EPC

Les Codes QR de l’EPC sont ajoutés automatiquement à vos factures. Les clients
dont la banque prend en charge les paiements par codes QR de l’EPC seront en
mesure de scanner le code et de payer la facture.

Allez à Comptabilité ‣ Clients ‣ Factures, et créez une nouvelle facture.

Avant de la comptabiliser, ouvrez l’onglet **Autres informations**. Konvergo ERP
remplit automatiquement le champ **Banque destinataire** avec votre IBAN.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans l’onglet <b>Autres informations</b>, le compte indiqué dans le champ <b>Banque destinataire</b> est utilisé pour recevoir le paiement de votre client. Konvergo ERP remplit automatiquement ce champ avec votre IBAN par défaut et l’utilise pour générer le code QR de l’EPC.</p>
</div>

Lorsque la facture est imprimée ou prévisualisée, le code QR figure au bas de
la facture.

![Code QR sur une facture client](../../../../_images/invoice-qr-code.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous souhaitez émettre une facture sans code QR de l’EPC, supprimez l’IBAN indiqué dans le champ <b>Banque destinataire</b> dans l’onglet <b>Autres informations</b> de la facture.</p>
</div>

