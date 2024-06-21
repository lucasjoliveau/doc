# Déclaration d’impôt

Les entreprises ayant un numéro de TVA enregistré doivent déposer une
**déclaration d’impôt** mensuellement ou trimestriellement, en fonction de
leur chiffre d’affaires et du règlement relatif à l’enregistrement. Une
déclaration d’impôt fournit aux autorités fiscales des informations sur les
transactions imposables effectuées par l’entreprise. La **taxe en aval** est
prélevée sur le nombre de biens et de services vendus par une entreprise,
alors que la **taxe en amont** est la taxe ajoutée au prix lorsque les biens
ou les services sont achetés. Sur la base de ces valeurs, l’entreprise peut
calculer le montant de la taxe qu’elle doit payer ou se faire rembourser.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous trouverez des informations complémentaires sur la TVA et son mécanisme sur cette page de la Commission européenne : <a href="https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en">« Qu’est-ce que la TVA ? »</a>.</p>
</div>

## Conditions préalables

### Périodicité de la déclaration d’impôt

La configuration de la **Périodicité de la déclaration d’impôt** permet à Konvergo ERP
de calculer correctement votre déclaration d’impôt et vous permet également de
vous envoyer un rappel pour ne jamais manquer une date limite de déclaration
d’impôt.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Paramètres. Dans la
section **Périodicité de la déclaration d’impôt** , vous pouvez définir :

  * la **Périodicité** : précisez ici si vous soumettez votre déclaration d’impôt mensuellement ou trimestriellement ;

  * le **Rappel** : précisez si Konvergo ERP doit vous rappeler de soumettre votre déclaration d’impôt ;

  * le **Journal** : sélectionnez le journal dans lequel enregistrer la déclaration d’impôt.

![Configurez la fréquence des déclarations d'impôt dans Konvergo ERP
Comptabilité](../../../../_images/tax_return_periodicity.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ces options sont généralement configurées lors de la <a href="../get_started">configuration initiale de l’application</a>.</p>
</div>

### Grilles de taxes

Konvergo ERP génère des déclarations de TVA sur la base des paramètres des **Grilles
de taxes** qui sont configurés sur vos taxes. En conséquent, vous devez vous
assurer que toutes les transactions enregistrées utilisent les bonnes taxes.
Vous pouvez voir les **Grilles de taxes** en ouvrant l’onglet **Écritures
comptables** de n’importe quelle facture client ou fournisseur.

![voir quelles grilles de taxes sont utilisées pour enregistrer des
transactions dans Konvergo ERP Comptabilité](../../../../_images/tax_return_grids.png)

Pour configurer vos grilles de taxes, allez à Comptabilité ‣ Configuration ‣
Taxes, et ouvrez la taxe que vous souhaitez modifier. Vous pouvez y modifier
les paramètres de la taxe, ainsi que les grilles de taxes qui sont utilisées
pour enregistrer des factures clients ou des avoirs.

![Configurez des taxes et leurs grilles de taxes dans Konvergo ERP
Comptabilité](../../../../_images/tax_return_taxes.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les taxes et les rapports sont généralement préconfigurés dans Konvergo ERP : un <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">package de localisation fiscale</span></a> est installé en fonction du pays que vous avez sélectionné lors de la création de votre base de données.</p>
</div>

## Clôturer une période fiscale

### Date de verrouillage de la taxe

Toute nouvelle transaction dont la date comptable est antérieure à la **Date
de verrouillage de la taxe** voit ses valeurs fiscales transférées vers la
prochaine période fiscale ouverte. Cela permet de s’assurer qu’aucune
modification ne peut être apportée à une déclaration une fois que sa période
est verrouillée.

Par conséquent, nous vous recommandons de verrouiller votre date fiscale avant
de travailler sur votre **Pièce comptable de clôture**. De cette façon, les
autres utilisateurs ne peuvent pas modifier ou ajouter des transactions qui
auraient un impact sur la **Pièce comptable de clôture** , ce qui peut vous
aider à éviter certaines erreurs de déclaration d’impôt.

Pour vérifier la **Date de verrouillage de la taxe** actuelle ou la modifier,
allez à Comptabilité ‣ Comptabilité ‣ Actions : Dates de verrouillage.

![Verrouillez vos taxes pour une période spécifique dans Konvergo ERP
Comptabilité](../../../../_images/tax_return_lock.png)

### Déclaration de TVA

Une fois que toutes les transactions impliquant des taxes ont été
comptabilisées pour la période que vous voulez déclarer, ouvrez votre
**Déclaration de TVA** en allant à Comptabilité ‣ Analyse ‣ Rapports d’audit :
Déclaration de TVA. Assurez-vous de sélectionner la bonne période que vous
voulez déclarer en utilisant le filtre de date, de cette façon vous pouvez
avoir une vue d’ensemble de votre déclaration de TVA. Dans cette vue, vous
pouvez facilement accéder aux différents formats de votre déclaration de TVA,
tels que `PDF` et XLSX. Vous y trouverez toutes les valeurs à déclarer aux
autorités fiscales, ainsi que le montant que vous devez payer ou qui vous sera
remboursé.

![Téléchargez votre déclaration de TVA au format PDF dans Konvergo ERP
Comptabilité](../../../../_images/tax_return_report.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous oubliez de verrouiller votre date fiscale avant de cliquer sur <b>Pièce comptable de clôture</b>, Konvergo ERP verrouille automatiquement votre période fiscale à la même date que la date comptable de votre pièce. Ce mécanisme de sécurité peut éviter certaines erreurs fiscales, mais il est recommandé de verrouiller votre date fiscale manuellement avant, comment il est décrit ci-dessus.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
<li><p><a href="../get_started">Bien démarrer</a></p></li>
<li><p><a href="../../fiscal_localizations">Localisations fiscales</a></p></li>
</ul>
</div>

  *[TVA]: Taxe sur la valeur ajoutée

