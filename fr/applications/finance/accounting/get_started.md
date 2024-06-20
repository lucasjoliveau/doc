# Bien démarrer

Lorsque vous ouvrez pour la première fois votre application Comptabilité Odoo,
la page _Aperçu de la comptabilité_ vous accueille avec une bannière
d’intégration étape par étape, un assistant qui vous aide à bien démarrer.
Cette bannière d’intégration est affichée jusqu’à ce que vous choisissiez de
la fermer.

Les paramètres visibles dans la bannière d’intégration peuvent toujours être
modifiés ultérieurement en allant à Comptabilité ‣ Configuration ‣ Paramètres.

Note

Odoo Comptabilité installe automatiquement le **package de localisation
fiscale** approprié pour votre société, selon le pays sélectionné lors de la
création de la base de données. De cette façon, les bons comptes, rapports et
taxes sont prêts à l’emploi. [Cliquez
ici](../fiscal_localizations.html#fiscal-localizations-packages) pour plus
d’informations sur les Packages de localisation fiscale.

## Bannière d’intégration Comptabilité

La bannière d’intégration de la comptabilité étape par étape est composée de
quatre étapes :

![Bannière d'intégration étape par étape dans Odoo
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

![Ajoutez les détails de votre entreprise dans Odoo Comptabilité et Odoo
Facturation](../../../_images/setup_company.png)

Note

Vous pouvez également modifier ces paramètres en allant à Configuration ‣
Paramètres Généraux ‣ Paramètres ‣ Sociétés et en cliquant sur **Mettre à jour
les informations**.

### Compte bancaire

Connectez votre compte bancaire à votre base de données et synchronisez
automatiquement vos relevés bancaires. Pour ce faire, recherchez votre
établissement bancaire dans la liste, cliquez sur _Connecter_ et suivez les
instructions à l’écran.

Note

[Cliquez ici](bank/bank_synchronization.html) pour plus d’informations sur
cette fonctionnalité.

Si votre établissement bancaire ne peut pas être synchronisé automatiquement,
ou si vous préférez ne pas le synchroniser avec votre base de données, vous
pouvez également configurer votre compte bancaire manuellement en cliquant sur
_Créer_ et en remplissant le formulaire.

  * **Nom** : le nom du compte bancaire, tel qu’affiché sur Odoo.

  * **Numéro de compte** : votre numéro de compte bancaire (IBAN en Europe).

  * **Banque** : cliquez sur _Créer et Modifier_ pour configurer les coordonnées bancaires. Ajoutez le nom de l’établissement bancaire et son code d’identification (BIC ou SWIFT).

  * **Code** : ce code est le _code abrégé_ de votre journal, tel qu’il est affiché sur Odoo. Par défaut, Odoo crée un nouveau journal avec ce code abrégé.

  * **Journal** : ce champ s’affiche si vous avez un journal bancaire existant qui n’est pas encore lié à un compte bancaire. Si oui, alors sélectionnez le _Journal_ que vous souhaitez utiliser pour enregistrer les transactions financières liées à ce compte bancaire ou créez-en un nouveau en cliquant sur _Créer et Modifier_.

Note

  * Vous pouvez ajouter autant de comptes bancaires que nécessaire avec cet outil en allant à Comptabilité ‣ Configuration, et en cliquant sur *Ajouter un compte bancaire *.

  * [Cliquez ici](bank.html) pour plus d’informations sur les comptes bancaires.

### Périodes comptables

Définissez ici les dates d’ouverture et de clôture de vos **Exercices
fiscaux** , qui sont utilisées pour générer automatiquement des rapports et la
**Périodicité de la déclaration d’impôt** , ainsi qu’un rappel pour ne jamais
manquer une date limite de déclaration d’impôt.

Par défaut, la date d’ouverture est fixée au 1er janvier et la date de clôture
au 31 décembre, car il s’agit de l’utilisation la plus courante.

Note

Vous pouvez également modifier ces paramètres en allant à Comptabilité ‣
Configuration ‣ Paramètres ‣ Périodes fiscales et en mettant à jour les
valeurs.

### Plan comptable

Avec ce menu, vous pouvez ajouter des comptes à votre **Plan comptable** et
indiquer leurs soldes d’ouverture initiaux.

Les paramètres de base sont affichés sur cette page pour vous aider à revoir
votre plan comptable. Pour accéder à tous les paramètres d’un compte, cliquez
sur le _bouton double flèche_ en fin de ligne.

![Configuration du plan comptable et leurs soldes initiaux dans Odoo
Comptabilité](../../../_images/setup_chart_of_accounts.png)

Note

[Cliquez ici](get_started/chart_of_accounts.html) pour plus d’informations sur
la façon de configurer votre plan comptable.

## Bannière d’intégration Facturation

Il existe une autre bannière d’intégration étape par étape qui vous aide à
tirer parti de vos applications de facturation et de comptabilité d’Odoo. La
_bannière d’intégration Facturation_ est celle qui vous accueille si vous
utilisez l’application Facturation plutôt que l’application Comptabilité.

Si vous avez installé Odoo Comptabilité sur votre base de données, vous pouvez
y accéder en allant sur Comptabilité ‣ Clients ‣ Factures clients.

La bannière d’intégration Facturation se compose de quatre étapes principales
:

![Bannière d'intégration étape par étape dans Odoo
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
de page_ des documents. Notez qu’Odoo ajoute automatiquement le numéro de
téléphone, l’adresse email, l’URL du site web et le numéro d’identification
fiscale (ou numéro de TVA) de la société au pied de page, en fonction des
valeurs que vous avez précédemment configurées dans les Données de la société.

![Configuration de la mise en page du document dans Odoo
Facturation](../../../_images/setup_document_layout.png)

Astuce

Ajoutez votre **numéro de compte bancaire** et un lien vers vos **Conditions
générales de vente** dans le pied de page. Ainsi, vos contacts peuvent
retrouver en ligne le contenu intégral de vos Conditions générales de vente
sans avoir à les imprimer sur les factures que vous émettez.

Note

Ces paramètres peuvent également être modifiés en allant à Configuration ‣
Paramètres généraux, dans la section _Mise en page du document_.

### Mode de paiement

Ce menu vous aide à configurer les modes de paiement avec lesquels vos clients
peuvent vous payer.

Important

La configuration d’un _Fournisseur de paiement_ avec cet outil active
également automatiquement l’option _Paiement des factures en ligne_. Grâce à
cela, les utilisateurs peuvent payer directement en ligne, depuis leur portail
client.

### Exemple de facture

Envoyez-vous un exemple de facture par email pour vous assurer que tout est
correctement configuré.

Pour plus d'infos

  * [Comptes bancaires et d’espèces](bank.html)

  * [Plan comptable](get_started/chart_of_accounts.html)

  * [Synchronisation bancaire](bank/bank_synchronization.html)

  * [Localisations fiscales](../fiscal_localizations.html)

  * [Odoo Tutorials: Accounting and Invoicing - Getting started [video]](https://www.odoo.com/slides/slide/getting-started-1692)

  * [Aide-mémoire de la comptabilité](get_started/cheat_sheet.html)
  * [Plan comptable](get_started/chart_of_accounts.html)
  * [Système multidevise](get_started/multi_currency.html)
  * [Average price on returned goods](get_started/avg_price_valuation.html)
  * [Unités TVA](get_started/vat_units.html)

