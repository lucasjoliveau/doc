# Authorize.Net

[Authorize.Net](https://www.authorize.net) est un fournisseur de solutions de
paiement en ligne basé aux États-Unis, permettant aux entreprises d’accepter
les **cartes de crédit**.

## Configuration

Pour plus d'infos

  * [Enable a payment provider](../payment_providers.html#payment-providers-add-new)

### Onglet des identifiants

Odoo a besoin de vos **identifiants & clés API** pour se connecter à votre
compte Authorize.Net, qui inclut :

  * **ID de connexion API** : L’identifiant utilisé uniquement pour identifier le compte auprès d’Authorize.Net.

  * **Clé de transaction API**

  * **Clé de signature API**

  * **Clé client API**

Pour les récupérer, connectez-vous à votre compte Authorize.Net, allez à
Compte ‣ Paramètres ‣ Paramètres de sécurité ‣ Identifiants & clés API,
générez votre **Clé de transaction** et votre **Clé de signature** et collez-
les dans les champs associés dans Odoo. Ensuite, cliquez sur **Générer la clé
client**.

Important

Pour tester Authorize.Net avec un compte _sandbox_ , passez le Statut en Mode
test. Nous vous recommandons de le faire sur une base de données Odoo de test,
plutôt que sur votre base de données principale.

Si vous utilisez le Mode test avec un compte régulier, vous verrez le message
d’erreur suivant : _L’identifiant de connexion du marchand ou le mot de passe
est invalide ou le compte est inactif_.

### Onglet de configuration

#### Faire une réservation sur une carte

With Authorize.Net, you can enable the [manual
capture](../payment_providers.html#payment-providers-manual-capture). If
enabled, the funds are reserved for 30 days on the customer’s card, but not
charged yet.

Avertissement

Après **30 jours** , la transaction est **automatiquement annulée** par
Authorize.Net.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

## Paiements ACH (uniquement les USA)

ACH est un système de transfert électronique de fonds utilisé entre des
comptes bancaires aux États-Unis.

### Configuration

Pour donner aux clients la possibilité de payer par ACH, [inscrivez-vous au
service eCheck
d’Authorize.Net](https://www.authorize.net/payments/echeck.html). Une fois que
eCheck est activé, dupliquez le fournisseur de paiement Authorize.Net
précédemment configuré sur Odoo en allant à Comptabilité ‣ Configuration ‣
Fournisseurs de paiement ‣ Authorize.net ‣ ⛭ Action ‣ Dupliquer. Modifiez
ensuite le nom du fournisseur pour différencier les deux versions (par ex.
`Authorize.net - Banques`).

Ouvrez l’onglet Configuration, définissez le champ Autoriser les paiements de
sur Compte bancaire (uniquement les USA).

Lorsque vous êtes prêt, modifiez le Statut du fournisseur en Activé pour un
compte normal et en Mode test pour un compte sandbox.

## Importer un relevé Authorize.Net

### Exporter depuis Authorize.Net

Modèle

[Téléchargez le modèle d’importation
Excel](https://docs.google.com/spreadsheets/d/1CMVtBWLLVIrUpYA92paw-
cL7-WdKLbaa/edit?usp=share_link&ouid=105295722917050444558&rtpof=true&sd=true)

Pour exporter un relevé :

  * Connectez-vous à Authorize.Net.

  * Allez à Compte ‣ Relevés ‣ Relevé de règlement eCheck.Net.

  * Définissez une plage d’exportation en utilisant un règlement par lot d” _ouverture_ et de _clôture_. Toutes les transactions comprises dans les deux règlements par lot seront exportées vers Odoo.

  * Sélectionnez toutes les transactions dans la plage souhaitée, copiez-les et collez-les dans la feuille Report 1 Download du modèle d’importation Excel.

![Sélection des transactions Authorize.Net à
importer](../../../_images/authorize-report1.png)

Example

![Lot de règlement d'un relevé Authorize.Net](../../../_images/authorize-
settlement-batch.png)

Dans ce cas, le premier lot (01/01/2021) de l’année correspond au règlement du
31/12/2020, donc le règlement d”**ouverture** date du 31/12/2020.

Une fois que les données se trouvent dans la feuille Report 1 Download :

  * Allez à l’onglet Recherche de transaction sur Authorize.Net.

  * Dans la section Date de règlement, sélectionnez la plage de dates de règlement par mot précédemment utilisée dans les champs Du : et Au : et cliquez sur Rechercher.

  * Lorsque la liste a été générée, cliquez sur Télécharger vers fichier.

  * Dans la fenêtre contextuelle, sélectionnez Champs élargis avec réponse CAVV/séparés par des virgules, activez Inclure les en-têtes de colonne et cliquez sur Soumettre.

  * Ouvrez le fichier texte, sélectionnez Tout, copiez les données et collez-les dans la feuille Report 2 Download du modèle d’importation Excel.

  * Les lignes de transit sont automatiquement complétées et mises à niveau dans les feuilles transit for report 1 et transit for report 2 du modèle d’importation Excel. Assurez-vous que toutes les écritures s’y trouvent et **si ce n’est pas le cas** , copiez la formule des lignes complétées précédemment des feuilles transit for report 1 ou 2 et collez-les dans les lignes vides.

Important

Pour obtenir le bon solde de clôture, **ne supprimez aucune** ligne dans les
feuilles Excel.

### Importer dans Odoo

Pour importer les données dans Odoo :

  * Ouvez le modèle d’importation Excel.

  * Copiez les données de la feuille transit for report 2 et utilisez le _collage spécial_ pour uniquement coller les valeurs dans la feuille Odoo Import to CSV.

  * Recherchez les cellules _bleues_ dans la feuille Odoo Import to CSV. Ce sont des écritures de rétrofacturation sans numéro de référence. Étant donné qu’elles ne peuvent pas être importées en tant que telles, allez à Authorize.Net ‣ Compte ‣ Relevés ‣ Relevé de règlement eCheck.Net.

  * Recherchez Charge transaction/rétrofacturation et cliquez dessus.

  * Copiez la description de la facture, copiez-la dans la cellule Libellé de la feuille Odoo Import to CSV et ajoutez `Rétrofacturation /` devant la description.

  * S’il y a plusieurs factures, ajoutez une ligne dans le modèle d’importation Excel pour chaque facture et copiez/collez la description dans chaque ligne de Libellé respective.

Note

Pour les **rétrofacturations/retours combinés** dans les paiements, créez une
nouvelle ligne dans le modèle d’importation Excel pour chaque facture.

Example

![Description de la rétrofacturation](../../../_images/authorize-chargeback-
desc.png)

  * Ensuite, supprimez les lignes _transaction nulle_ et _transaction annulée_ et modifiez le format de la colonne Montant de la feuille Odoo Import to CSV en _Nombre_.

  * Retournez à Relevé de règlement eCheck.Net ‣ Rechercher une transaction et recherchez à nouveau les dates de règlement des lots précédemment utilisées.

  * Vérifiez que les dates de règlement des lots sur eCheck.Net correspondent aux dates des paiements associés trouvées dans la colonne Date de la feuille Odoo Import to CSV.

  * Si ce n’est pas le cas, remplacez la date par celle d’eCheck.Net. Triez la colonne par _date_ et assurez-vous que le format est `MM/DD/YYYY`.

  * Copiez les données - y compris les en-têtes de colonne - de la feuille Odoo Import to CSV, collez-les dans un nouveau fichier Excel et enregistrez-les en utilisant le format CSV.

  * Ouvrez l’application Comptabilité, allez à Configuration ‣ Journaux, cochez la case Authorize.Net et cliquez sur Favoris ‣ Importer des enregistrements ‣ Télécharger le fichier. Sélectionnez le fichier CSV et chargez-le dans Odoo.

Astuce

Liste des [codes de retour
eCheck.Net](https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293)

  *[ACH]: automated clearing house

