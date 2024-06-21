# Authorize.Net

[Authorize.Net](https://www.authorize.net) est un fournisseur de solutions de
paiement en ligne basé aux États-Unis, permettant aux entreprises d’accepter
les **cartes de crédit**.

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Onglet des identifiants

Konvergo ERP a besoin de vos **identifiants & clés API** pour se connecter à votre
compte Authorize.Net, qui inclut :

  * **ID de connexion API** : L’identifiant utilisé uniquement pour identifier le compte auprès d’Authorize.Net.

  * **Clé de transaction API**

  * **Clé de signature API**

  * **Clé client API**

Pour les récupérer, connectez-vous à votre compte Authorize.Net, allez à
Compte ‣ Paramètres ‣ Paramètres de sécurité ‣ Identifiants & clés API,
générez votre **Clé de transaction** et votre **Clé de signature** et collez-
les dans les champs associés dans Konvergo ERP. Ensuite, cliquez sur **Générer la clé
client**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour tester Authorize.Net avec un compte <em>sandbox</em>, passez le <b>Statut</b> en <b>Mode test</b>. Nous vous recommandons de le faire sur une base de données Konvergo ERP de test, plutôt que sur votre base de données principale.</p>
<p>Si vous utilisez le <b>Mode test</b> avec un compte régulier, vous verrez le message d’erreur suivant : <em>L’identifiant de connexion du marchand ou le mot de passe est invalide ou le compte est inactif</em>.</p>
</div>

### Onglet de configuration

#### Faire une réservation sur une carte

With Authorize.Net, you can enable the [manual
capture](../payment_providers#payment-providers-manual-capture). If
enabled, the funds are reserved for 30 days on the customer’s card, but not
charged yet.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Après <b>30 jours</b>, la transaction est <b>automatiquement annulée</b> par Authorize.Net.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

## Paiements ACH (uniquement les USA)

ACH est un système de transfert électronique de fonds utilisé entre des
comptes bancaires aux États-Unis.

### Configuration

Pour donner aux clients la possibilité de payer par ACH, [inscrivez-vous au
service eCheck
d’Authorize.Net](https://www.authorize.net/payments/echeck). Une fois que
eCheck est activé, dupliquez le fournisseur de paiement Authorize.Net
précédemment configuré sur Konvergo ERP en allant à Comptabilité ‣ Configuration ‣
Fournisseurs de paiement ‣ Authorize.net ‣ ⛭ Action ‣ Dupliquer. Modifiez
ensuite le nom du fournisseur pour différencier les deux versions (par ex.
`Authorize.net - Banques`).

Ouvrez l’onglet **Configuration** , définissez le champ **Autoriser les
paiements de** sur **Compte bancaire (uniquement les USA)**.

Lorsque vous êtes prêt, modifiez le **Statut** du fournisseur en **Activé**
pour un compte normal et en **Mode test** pour un compte sandbox.

## Importer un relevé Authorize.Net

### Exporter depuis Authorize.Net

<div class="admonition-template alert" id="authorize-import-template">
<p class="alert-title">
Modèle</p><p><a href="https://docs.google.com/spreadsheets/d/1CMVtBWLLVIrUpYA92paw-cL7-WdKLbaa/edit?usp=share_link&amp;ouid=105295722917050444558&amp;rtpof=true&amp;sd=true">Téléchargez le modèle d’importation Excel</a></p>
</div>

Pour exporter un relevé :

  * Connectez-vous à Authorize.Net.

  * Allez à Compte ‣ Relevés ‣ Relevé de règlement eCheck.Net.

  * Définissez une plage d’exportation en utilisant un règlement par lot d” _ouverture_ et de _clôture_. Toutes les transactions comprises dans les deux règlements par lot seront exportées vers Konvergo ERP.

  * Sélectionnez toutes les transactions dans la plage souhaitée, copiez-les et collez-les dans la feuille **Report 1 Download** du modèle d’importation Excel.

![Sélection des transactions Authorize.Net à
importer](../../../_images/authorize-report1.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Lot de règlement d'un relevé Authorize.Net" class="align-center" src="../../../_images/authorize-settlement-batch.png"/>
<p>Dans ce cas, le premier lot (01/01/2021) de l’année correspond au règlement du 31/12/2020, donc le règlement d”<b>ouverture</b> date du 31/12/2020.</p>
</div>

Une fois que les données se trouvent dans la feuille **Report 1 Download** :

  * Allez à l’onglet **Recherche de transaction** sur Authorize.Net.

  * Dans la section **Date de règlement** , sélectionnez la plage de dates de règlement par mot précédemment utilisée dans les champs **Du :** et **Au :** et cliquez sur **Rechercher**.

  * Lorsque la liste a été générée, cliquez sur **Télécharger vers fichier**.

  * Dans la fenêtre contextuelle, sélectionnez **Champs élargis avec réponse CAVV/séparés par des virgules** , activez **Inclure les en-têtes de colonne** et cliquez sur **Soumettre**.

  * Ouvrez le fichier texte, sélectionnez **Tout** , copiez les données et collez-les dans la feuille **Report 2 Download** du modèle d’importation Excel.

  * Les lignes de transit sont automatiquement complétées et mises à niveau dans les feuilles **transit for report 1** et **transit for report 2** du modèle d’importation Excel. Assurez-vous que toutes les écritures s’y trouvent et **si ce n’est pas le cas** , copiez la formule des lignes complétées précédemment des feuilles **transit for report 1** ou **2** et collez-les dans les lignes vides.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour obtenir le bon solde de clôture, <b>ne supprimez aucune</b> ligne dans les feuilles Excel.</p>
</div>

### Importer dans Konvergo ERP

Pour importer les données dans Konvergo ERP :

  * Ouvez le modèle d’importation Excel.

  * Copiez les données de la feuille **transit for report 2** et utilisez le _collage spécial_ pour uniquement coller les valeurs dans la feuille **Konvergo ERP Import to CSV**.

  * Recherchez les cellules _bleues_ dans la feuille **Konvergo ERP Import to CSV**. Ce sont des écritures de rétrofacturation sans numéro de référence. Étant donné qu’elles ne peuvent pas être importées en tant que telles, allez à Authorize.Net ‣ Compte ‣ Relevés ‣ Relevé de règlement eCheck.Net.

  * Recherchez **Charge transaction/rétrofacturation** et cliquez dessus.

  * Copiez la description de la facture, copiez-la dans la cellule **Libellé** de la feuille **Konvergo ERP Import to CSV** et ajoutez `Rétrofacturation /` devant la description.

  * S’il y a plusieurs factures, ajoutez une ligne dans le modèle d’importation Excel pour chaque facture et copiez/collez la description dans chaque ligne de **Libellé** respective.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour les <b>rétrofacturations/retours combinés</b> dans les paiements, créez une nouvelle ligne dans le <a href="#authorize-import-template"><span class="std std-ref">modèle d’importation Excel</span></a> pour chaque facture.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Description de la rétrofacturation" src="../../../_images/authorize-chargeback-desc.png"/>
</div>

  * Ensuite, supprimez les lignes _transaction nulle_ et _transaction annulée_ et modifiez le format de la colonne **Montant** de la feuille **Konvergo ERP Import to CSV** en _Nombre_.

  * Retournez à Relevé de règlement eCheck.Net ‣ Rechercher une transaction et recherchez à nouveau les dates de règlement des lots précédemment utilisées.

  * Vérifiez que les dates de règlement des lots sur eCheck.Net correspondent aux dates des paiements associés trouvées dans la colonne **Date** de la feuille **Konvergo ERP Import to CSV**.

  * Si ce n’est pas le cas, remplacez la date par celle d’eCheck.Net. Triez la colonne par _date_ et assurez-vous que le format est `MM/DD/YYYY`.

  * Copiez les données - y compris les en-têtes de colonne - de la feuille **Konvergo ERP Import to CSV** , collez-les dans un nouveau fichier Excel et enregistrez-les en utilisant le format CSV.

  * Ouvrez l’application Comptabilité, allez à Configuration ‣ Journaux, cochez la case **Authorize.Net** et cliquez sur Favoris ‣ Importer des enregistrements ‣ Télécharger le fichier. Sélectionnez le fichier CSV et chargez-le dans Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Liste des <a href="https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293">codes de retour eCheck.Net</a></p>
</div>

  *[ACH]: automated clearing house

