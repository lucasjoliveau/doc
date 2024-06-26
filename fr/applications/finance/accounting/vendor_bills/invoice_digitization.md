# Numérisation de documents assistée par IA

La **numérisation des factures** consiste à convertir les documents papiers en
factures fournisseurs et clients dans votre comptabilité.

Konvergo ERP utilise les technologies OCR et d’intelligence artificielle pour
reconnaître le contenu des documents. Les factures fournisseurs et clients
sont créées et remplies automatiquement sur la base des factures numérisées.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/app/invoice-automation">Essayez la numérisation des factures d’Konvergo ERP</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/digitize-bills-with-ocr-1712">Tutoriels Konvergo ERP : Numérisation des factures à l’aide d’OCR</a></p></li>
</ul>
</div>

## Configuration

Dans Comptabilité ‣ Configuration ‣ Paramètres ‣ Numérisation, cochez la case
à côté de **Numérisation de documents** et choisissez si les **Factures
fournisseurs** et les **Factures clients** (y compris les avoirs clients)
doivent être traitées automatiquement ou sur demande.

Si vous activez l’option **Ligne de facturation unique par taxe** , une seule
ligne est créée par taxe dans la nouvelle facture, indépendamment du nombre de
lignes sur la facture.

## Chargement des factures

### Charger les factures manuellement

À partir du **Tableau de bord de comptabilité** , cliquez sur le bouton
**Charger** du journal de vos factures fournisseurs. Vous pouvez également
aller à Comptabilité ‣ Clients ‣ Factures clients ou Comptabilité ‣
Fournisseurs ‣ Factures fournisseurs et sélectionnez **Charger**.

### Charger des factures à l’aide d’un alias d’email

Vous pouvez configurer votre scanner connecté pour envoyer des documents
numérisés à un alias d’email. Les emails envoyés à ces alias sont convertis en
nouvelles factures clients ou fournisseurs brouillon.

Vous pouvez modifier l’alias d’email d’un journal. Pour ce faire, allez à
l’application **Paramètres**. Dans **Paramètres généraux : Discussion** ,
activez **Serveurs de messagerie personnalisés** , ajoutez un **Domaine
d’alias** , et cliquez sur **Enregistrer**.

L’alias d’email est désormais disponible dans l’onglet **Paramètres avancés**
du journal. Les emails envoyés à cette adresse seront convertis
automatiquement en nouvelles factures clients ou fournisseurs.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you use the <a href="../../../productivity/documents">Documents</a> app, you can automatically
send your scanned invoices to the <b>Finance</b> workspace (e.g.,
<code>inbox-financial@example.odoo.com</code>).</p>
</div>

Les alias d’email par défaut `vendor-bills@` et `customer-invoices@` suivis du
**Domaine d’alias** que vous définissez sont automatiquement créés pour les
journaux des **factures fournisseurs** et des **factures clients**
respectivement. Les emails envoyés à ces adresses sont convertis
automatiquement en nouvelles factures fournisseurs ou clients.

Pour modifier un alias d’email par défaut, allez à Comptabilité ‣
Configuration ‣ Comptabilité : Journaux. Sélectionnez le journal que vous
voulez modifier, cliquez sur l’onglet **Paramètres avancés** et modifiez
l”`Alias d'email`.

## Numérisation des factures

En fonction de vos paramètres, le document est soit traité automatiquement,
soit vous devez cliquer sur **Envoyer pour numérisation** pour le faire
manuellement.

Une fois les données extraites du PDF, vous pouvez les corriger si nécessaire
en cliquant sur les étiquettes respectives (disponible en mode **Édition**) et
en sélectionnant les informations appropriées.

## Reconnaissance des données avec l’IA

Il est essentiel de revoir et corriger (le cas échéant) les informations
chargées lors de la numérisation. Ensuite, vous devez valider le document en
cliquant sur **Confirmer**. De cette manière, l’IA apprend et le système
identifie les données correctes pour les numérisations futures.

## Tarification

La **numérisation des factures** est un service d’Achats In-App (IAP) qui
nécessite des crédits prépayés pour fonctionner. La numérisation d’un document
consomme un crédit.

Pour acheter des crédits, allez à Comptabilité ‣ Configuration ‣ Paramètres ‣
Numérisation et cliquez sur **Acheter des crédits** , ou allez à Paramètres ‣
Konvergo ERP IAP et cliquez sur **Voir mes services**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous êtes sur Konvergo ERP Online et vous avez la version Enterprise, vous bénéficiez de crédits d’essai gratuits pour tester la fonctionnalité.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://iap.odoo.com/privacy#header_6">Notre Politique vie privée</a></p></li>
<li><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
</ul>
</div>

  *[OCR]: reconnaissance optique de caractères

