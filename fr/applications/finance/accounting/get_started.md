# Bien démarrer

Lorsque vous ouvrez pour la première fois votre application Comptabilité Konvergo ERP,
la page _Aperçu de la comptabilité_ vous accueille avec une bannière
d’intégration étape par étape, un assistant qui vous aide à bien démarrer.
Cette bannière d’intégration est affichée jusqu’à ce que vous choisissiez de
la fermer.

Les paramètres visibles dans la bannière d’intégration peuvent toujours être
modifiés ultérieurement en allant à Comptabilité ‣ Configuration ‣ Paramètres.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP Comptabilité installe automatiquement le <b>package de localisation fiscale</b> approprié pour votre société, selon le pays sélectionné lors de la création de la base de données. De cette façon, les bons comptes, rapports et taxes sont prêts à l’emploi. <a href="../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Cliquez ici</span></a> pour plus d’informations sur les Packages de localisation fiscale.</p>
</div>

## Bannière d’intégration Comptabilité

La bannière d’intégration de la comptabilité étape par étape est composée de
quatre étapes :

![Bannière d'intégration étape par étape dans Konvergo ERP
Comptabilité](../../../_images/setup_accounting_onboarding.png)

  1. Données sur la société

  2. Compte bancaire

  3. Périodes comptables

  4. Plan comptable

### Données sur la société

Ce menu vous permet d’ajouter les détails de votre entreprise tels que la
dénomination, l’adresse, le logo, le site web, le numéro de téléphone,
l’adresse email et le numéro d’identification fiscale ou de TVA. Ces détails
sont ensuite affichés sur vos documents, comme sur les factures.

![Ajoutez les détails de votre entreprise dans Konvergo ERP Comptabilité et Konvergo ERP
Facturation](../../../_images/setup_company.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez également modifier ces paramètres en allant à Configuration ‣ Paramètres Généraux ‣ Paramètres ‣ Sociétés et en cliquant sur <b>Mettre à jour les informations</b>.</p>
</div>

### Compte bancaire

Connectez votre compte bancaire à votre base de données et synchronisez
automatiquement vos relevés bancaires. Pour ce faire, recherchez votre
établissement bancaire dans la liste, cliquez sur _Connecter_ et suivez les
instructions à l’écran.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="bank/bank_synchronization">Cliquez ici</a> pour plus d’informations sur cette fonctionnalité.</p>
</div>

Si votre établissement bancaire ne peut pas être synchronisé automatiquement,
ou si vous préférez ne pas le synchroniser avec votre base de données, vous
pouvez également configurer votre compte bancaire manuellement en cliquant sur
_Créer_ et en remplissant le formulaire.

  * **Nom** : le nom du compte bancaire, tel qu’affiché sur Konvergo ERP.

  * **Numéro de compte** : votre numéro de compte bancaire (IBAN en Europe).

  * **Banque** : cliquez sur _Créer et Modifier_ pour configurer les coordonnées bancaires. Ajoutez le nom de l’établissement bancaire et son code d’identification (BIC ou SWIFT).

  * **Code** : ce code est le _code abrégé_ de votre journal, tel qu’il est affiché sur Konvergo ERP. Par défaut, Konvergo ERP crée un nouveau journal avec ce code abrégé.

  * **Journal** : ce champ s’affiche si vous avez un journal bancaire existant qui n’est pas encore lié à un compte bancaire. Si oui, alors sélectionnez le _Journal_ que vous souhaitez utiliser pour enregistrer les transactions financières liées à ce compte bancaire ou créez-en un nouveau en cliquant sur _Créer et Modifier_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous pouvez ajouter autant de comptes bancaires que nécessaire avec cet outil en allant à Comptabilité ‣ Configuration, et en cliquant sur <a href="#id1"><span class="problematic" id="id2">*</span></a>Ajouter un compte bancaire <a href="#id3"><span class="problematic" id="id4">*</span></a>.</p></li>
<li><p><a href="bank">Cliquez ici</a> pour plus d’informations sur les comptes bancaires.</p></li>
</ul>
</div>

### Périodes comptables

Définissez ici les dates d’ouverture et de clôture de vos **Exercices
fiscaux** , qui sont utilisées pour générer automatiquement des rapports et la
**Périodicité de la déclaration d’impôt** , ainsi qu’un rappel pour ne jamais
manquer une date limite de déclaration d’impôt.

Par défaut, la date d’ouverture est fixée au 1er janvier et la date de clôture
au 31 décembre, car il s’agit de l’utilisation la plus courante.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez également modifier ces paramètres en allant à Comptabilité ‣ Configuration ‣ Paramètres ‣ Périodes fiscales et en mettant à jour les valeurs.</p>
</div>

### Plan comptable

Avec ce menu, vous pouvez ajouter des comptes à votre **Plan comptable** et
indiquer leurs soldes d’ouverture initiaux.

Les paramètres de base sont affichés sur cette page pour vous aider à revoir
votre plan comptable. Pour accéder à tous les paramètres d’un compte, cliquez
sur le _bouton double flèche_ en fin de ligne.

![Configuration du plan comptable et leurs soldes initiaux dans Konvergo ERP
Comptabilité](../../../_images/setup_chart_of_accounts.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="get_started/chart_of_accounts">Cliquez ici</a> pour plus d’informations sur la façon de configurer votre plan comptable.</p>
</div>

## Bannière d’intégration Facturation

Il existe une autre bannière d’intégration étape par étape qui vous aide à
tirer parti de vos applications de facturation et de comptabilité d’Konvergo ERP. La
_bannière d’intégration Facturation_ est celle qui vous accueille si vous
utilisez l’application Facturation plutôt que l’application Comptabilité.

Si vous avez installé Konvergo ERP Comptabilité sur votre base de données, vous pouvez
y accéder en allant sur Comptabilité ‣ Clients ‣ Factures clients.

La bannière d’intégration Facturation se compose de quatre étapes principales
:

![Bannière d'intégration étape par étape dans Konvergo ERP
Facturation](../../../_images/setup_invoicing_onboarding.png)

  1. Données sur la société

  2. Mise en page de la facture

  3. Mode de paiement

  4. Exemple de facture

### Données sur la société

Ce formulaire est identique à celui présenté dans la bannière d’intégration
Comptabilité.

### Mise en page de la facture

Avec cet outil, vous pouvez concevoir l’apparence de vos documents en
sélectionnant le modèle de mise en page, le format de papier, les couleurs, la
police et le logo que vous souhaitez utiliser.

Vous pouvez également ajouter le _Slogan de la société_ et le contenu du _pied
de page_ des documents. Notez qu’Konvergo ERP ajoute automatiquement le numéro de
téléphone, l’adresse email, l’URL du site web et le numéro d’identification
fiscale (ou numéro de TVA) de la société au pied de page, en fonction des
valeurs que vous avez précédemment configurées dans les Données de la société.

![Configuration de la mise en page du document dans Konvergo ERP
Facturation](../../../_images/setup_document_layout.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ajoutez votre <b>numéro de compte bancaire</b> et un lien vers vos <b>Conditions générales de vente</b> dans le pied de page. Ainsi, vos contacts peuvent retrouver en ligne le contenu intégral de vos Conditions générales de vente sans avoir à les imprimer sur les factures que vous émettez.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ces paramètres peuvent également être modifiés en allant à Configuration ‣ Paramètres généraux, dans la section <em>Mise en page du document</em>.</p>
</div>

### Mode de paiement

Ce menu vous aide à configurer les modes de paiement avec lesquels vos clients
peuvent vous payer.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La configuration d’un <em>Fournisseur de paiement</em> avec cet outil active également automatiquement l’option <em>Paiement des factures en ligne</em>. Grâce à cela, les utilisateurs peuvent payer directement en ligne, depuis leur portail client.</p>
</div>

### Exemple de facture

Envoyez-vous un exemple de facture par email pour vous assurer que tout est
correctement configuré.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="bank">Comptes bancaires et d’espèces</a></p></li>
<li><p><a href="get_started/chart_of_accounts">Plan comptable</a></p></li>
<li><p><a href="bank/bank_synchronization">Synchronisation bancaire</a></p></li>
<li><p><a href="../fiscal_localizations">Localisations fiscales</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/getting-started-1692">Konvergo ERP Tutorials: Accounting and Invoicing - Getting started [video]</a></p></li>
</ul>
</div>

  * [Aide-mémoire de la comptabilité](get_started/cheat_sheet)
  * [Plan comptable](get_started/chart_of_accounts)
  * [Système multidevise](get_started/multi_currency)
  * [Average price on returned goods](get_started/avg_price_valuation)
  * [Unités TVA](get_started/vat_units)

