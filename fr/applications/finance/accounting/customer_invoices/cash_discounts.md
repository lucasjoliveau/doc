# Escomptes et réduction d’impôt

Les **escomptes** sont des réductions du montant qu’un client doit payer pour
des biens ou des services, afin de l’inciter à payer sa facture rapidement.
Ces escomptes représentent généralement un pourcentage de la facture totale et
sont appliqués si le client paie endéans un délai déterminé. Les escomptes
peuvent aider l’entreprise à maintenir un flux de trésorerie régulier.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Vous émettez une facture de 100 € le 1er janvier. Le paiement intégral est dû endéans les 30 jours et vous offrez également une remise de 2% si le client vous paie dans les sept jours.</p>
<p>Le client peut payer 98 € jusqu’au 8 janvier. Passé cette date, il devra payer 100 € avant le 31 janvier.</p>
</div>

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
Configuration ‣ Paramètres, et dans la section **Taxes** , dans la
fonctionnalité **Réduction d’impôt pour escompte** , sélectionnez l’une des
trois options suivantes :

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

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Vous émettez une facture de 100 € (hors taxes) le 1er janvier, avec une taxe de 21%. Le paiement intégral est dû endéans les 30 jours et vous offrez également une remise de 2% si votre client vous paie endéans les sept jours.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Always (upon invoice)</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">On early payment</button><button aria-controls="panel-0-0-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-2" name="0-2" role="tab" tabindex="-1">Never</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Date d’échéance</p></th>
<th class="head"><p>Montant total dû</p></th>
<th class="head"><p>Calcul</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 janvier</p></td>
<td><p>118,58 €</p></td>
<td><p>(98 € + (21% de 98 €))</p></td>
</tr>
<tr class="row-odd"><td><p>31 janvier</p></td>
<td><p>120,58 €</p></td>
<td><p>(100 € + (21% de 98 €))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Date d’échéance</p></th>
<th class="head"><p>Montant total dû</p></th>
<th class="head"><p>Calcul</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 janvier</p></td>
<td><p>118,58 €</p></td>
<td><p>(98 € + (21% de 98 €))</p></td>
</tr>
<tr class="row-odd"><td><p>31 janvier</p></td>
<td><p>121,00 €</p></td>
<td><p>(100 € + (21% de 100 €))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-2" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-2" name="0-2" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Date d’échéance</p></th>
<th class="head"><p>Montant total dû</p></th>
<th class="head"><p>Calcul</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 janvier</p></td>
<td><p>119,00 €</p></td>
<td><p>(98 € + (21% de 100 €))</p></td>
</tr>
<tr class="row-odd"><td><p>31 janvier</p></td>
<td><p>121,00 €</p></td>
<td><p>(100 € + (21% de 100 €))</p></td>
</tr>
</tbody>
</table>
</div></div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Les <a href="../reporting/tax_returns#tax-returns-tax-grids"><span class="std std-ref">grilles fiscales</span></a>, qui sont utilisées pour la déclaration de TVA, sont calculées correctement en fonction du <a href="#cash-discounts-tax-reductions"><span class="std std-ref">type de réduction d’impôt</span></a> que vous avez configuré.</p></li>
<li><p>Le <b>type de réduction d’impôt pour escompte</b> peut être correctement préconfiguré, en fonction de votre <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">package de localisation fiscale</span></a>.</p></li>
</ul>
</div>

### Comptes des pertes/gains d’escompte

Dans le cas d’un escompte, le montant que vous gagnez dépend du fait que le
client bénéficie ou non de l’escompte. Cela entraîne inévitablement des gains
et des pertes, qui sont enregistrés sur des comptes par défaut.

Pour modifier ces comptes, allez à Comptabilité ‣ Configuration ‣ Paramètres,
et dans la section **Comptes par défaut** , sélectionnez les comptes que vous
souhaitez utiliser pour le **Compte des gains d’escompte** et le **Compte des
pertes d’escompte**.

### Délais de paiement

Les escomptes sont définis sur les [conditions de
paiement](payment_terms). Configurez-les à votre guise en allant à
Comptabilité ‣ Configuration ‣ Conditions de paiement, et assurez-vous de
compléter les champs **% de remise** et **Jours d’escompte**.

![Configuration des conditions de paiement nommées "2/7 Net 30". Le champ
"Description sur les factures" indique : "Conditions de paiement : 30 jours,
2% d'escompte pour paiement anticipé endéans les 7
jours".](../../../../_images/payment-terms.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="payment_terms">Conditions de paiement et plans de paiement échelonné</a></p>
</div>

## Appliquer un escompte à une facture client

Appliquez un escompte à une facture client en sélectionnant les conditions de
paiement que vous avez créées. Konvergo ERP calcule automatiquement les montants
corrects, les montants de taxe, les dates d’échéance et les enregistrements
comptables.

Dans l’onglet **Écritures comptables** , vous pouvez afficher les détails de
l’escompte en cliquant sur le bouton de « basculement » et en ajoutant les
colonnes **Date de la remise** et **Montant de la remise**.

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

Lorsque vous enregistrez un paiement ou rapprochez vos relevés bancaires, Konvergo ERP
prend en compte la date du paiement du client pour définir s’il peut
bénéficier ou non de l’escompte.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si votre client paie le montant de l’escompte <em>après</em> la date de a remise, vous pouvez toujours décider de marquer la facture comme entièrement payée avec une écriture d’annulation ou comme partiellement payée.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payments">Paiements</a></p>
</div>

