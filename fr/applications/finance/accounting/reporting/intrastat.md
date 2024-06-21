# Intrastat

Intrastat est le système utilisé pour la production de statistiques et la
collecte de données relatives aux échanges de biens au sein de l’Union
européenne. Il collecte des données sur :

  * Les transactions commerciales de marchandises destinées à l’utilisation, à la consommation, aux investissements ou à la revente impliquant un changement de propriété ;

  * Les déplacements de marchandises sans changement de propriété (par ex. le déplacement de stock ou des mouvements de marchandises avant ou après un travail à façon et après un entretien ou une réparation) ;

  * Les retours de marchandises.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Même si le système Intrastat continue à être utilisé, le terme Intrastat n’est pas utilisé dans le <a href="https://eur-lex.europa.eu/eli/reg/2019/2152/2022-01-01">dernier règlement</a>, faisant plutôt référence aux <em>statistiques sur le commerce intracommunautaire de marchandises</em>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Intrastat">Eurostat Statistics Explained - Glossaire : Intrastat</a></p>
</div>

## Configuration générale

Activez le rapport Intrastat en allant à Comptabilité ‣ Configuration ‣
Paramètres. Dans la section **Factures clients** , cochez **Intrastat** et
cliquez sur **Enregistrer**.

### Codes de transaction par défaut : facture et remboursement

Vous pouvez définir un code de transaction par défaut pour toutes les
transactions de facture et de remboursement nouvellement créées. Dans
Comptabilité ‣ Configuration ‣ Paramètres, sélectionnez un **Code de
transaction de facture par défaut** et/ou un **Code de transaction de
remboursement par défaut** et cliquez sur **Enregistrer**. Le code sera
automatiquement défini sur toutes les lignes de facture respectives.

### Code de région

Le code de région est **uniquement utilisé par les sociétés belges**. Dans
Comptabilité ‣ Configuration ‣ Paramètres, sélectionnez la **Région Intrastat
de la société** dans laquelle la société se situe et cliquez sur
**Enregistrer**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vos entrepôts se situent dans plusieurs régions, vous pouvez définir le code de région au niveau de chaque entrepôt. Pour ce faire, allez à Inventaire ‣ Configuration ‣ Entrepôts, sélectionnez un entrepôt, définissez sa <b>région Intrastat</b> et cliquez sur <b>Enregistrer</b>.</p>
<img alt="Ajout de la région Intrastat à un entrepôt" class="align-center" src="../../../../_images/warehouse-region.png"/>
</div>

## Configuration du produit

Tous les produits doivent être correctement configurés pour être inclus dans
le rapport Intrastat.

### Code marchandises

Les codes marchandises sont des numéros de référence reconnus au niveau
international et sont utilisés pour classer les marchandises en fonction de
leur **nature**. Intrastat utilise la [Nomenclature
combinée](https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-
duties/customs-tariff/combined-nomenclature_fr).

Pour ajouter un code marchandises, allez à Comptabilité ‣ Clients ‣ Produits
et sélectionnez un produit. Dans l’onglet **Comptabilité** , définissez le
**Code marchandises** du produit.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.nbb.be/fr/statistiques/commerce-exterieur/nomenclature-et-codes">Banque Nationale de Belgique - Codes marchandises Intrastat</a></p>
</div>

### Quantité : poids et unités supplémentaires

En fonction de la nature des marchandises, il est nécessaire de préciser le
poids du produit en kilogrammes (sans emballage) ou l’unité supplémentaire du
produit, telle que mètres carrés (`m2`), le nombre de pièces (`p/st`), litres
(`l`), ou grammes (`g`).

Pour ajouter le poids ou l’unité supplémentaire d’un produit, allez à
Comptabilité ‣ Clients ‣ Produits et sélectionnez un produit. Dans l’onglet
**Comptabilité** , en fonction du code marchandises défini, remplissez le
**poids** du produit ou ses **Unités supplémentaires**.

### Pays d’origine

Pour ajouter le pays d’origine d’un produit, allez à Comptabilité ‣ Clients ‣
Produits et sélectionnez un produit. Dans l’onglet **Comptabilité** ,
définissez le **Pays d’origine**.

## Configuration des factures clients et fournisseurs

Une fois que les produits sont correctement configurés, plusieurs paramètres
doivent être configurés sur les factures clients et fournisseurs que vous
créez.

### Code de transaction

Les codes de transaction sont utilisés pour identifier la nature d’une
transaction. Vous pouvez définir des Codes de transaction par défaut pour les
transactions de facture et de remboursement.

Pour définir un code de transaction sur une ligne de facture, créez une
facture client ou une facture fournisseur, cliquez sur le bouton de sélection
de colonnes, cochez **Intrastat** et utilisez la colonne **Intrastat**
nouvellement ajoutée pour sélectionner un code de transaction.

![Ajout de la colonne Intrastat à une facture client ou
fournisseur](../../../../_images/intrastat-column.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.nbb.be/doc/dd/onegate/data/new_natures_of_transaction_2022_fr.pdf">Banque Nationale de Belgique - Intrastat : Natures de transactions à partir de janvier 2022</a></p>
</div>

### Pays partenaire

Le pays partenaire correspond au pays de votre fournisseur sur les factures
fournisseurs et le pays de votre client sur les factures clients. Il est
complété automatiquement par le pays défini dans le champ **Pays** de la fiche
du contact.

Pour modifier le pays partenaire manuellement, créez une facture client ou une
facture fournisseur, cliquez sur l’onglet **Autres informations** et
sélectionnez le **Pays Intrastat**.

### Code de transport

Le code de transport identifie le **mode de transport** présumé utilisé pour
envoyer les marchandises (arrivée ou expédition).

Pour ajouter le code de transport, créez une facture client ou une facture
fournisseur, allez à l’onglet **Autres informations** et sélectionnez le
**Mode de transport Intrastat**.

### Valeur des marchandises

La valeur d’une marchandise est le **sous-total** hors taxes (le **Prix**
multiplié par la **Quantité**) d’une ligne de facture.

## Configuration du partenaire

Deux champs de la fiche du partenaire sont utilisés dans Intrastat : **TVA**
et **Pays**. Le pays peut être défini manuellement sur la facture client ou la
facture fournisseur.

## Générer le rapport Intrastat

Générez le rapport en allant à Comptabilité ‣ Analyse ‣ Rapports d’audit :
Rapport Intrastat. Il est calculé automatiquement sur la base de la
configuration par défaut et les informations qui figurent sur les produits,
les factures clients et fournisseurs, et les partenaires.

Exportez le rapport au format PDF, XLSX ou XML pour l’envoyer à votre
administration juridique.

Chaque ligne du rapport fait référence à une seule ligne de facture et
contient les informations suivantes :

  * Numéro de référence de la facture client ou fournisseur ;

  * Système, c’est-à-dire un code généré automatiquement selon que le document est une facture client (expédition) ou une facture fournisseur (arrivée) ;

  * Pays, c’est-à-dire le pays du fournisseur pour les arrivées et le pays du client pour les expéditions ;

  * Code de transaction ;

  * (Si votre société se situe en Belgique) Code de région ;

  * Code marchandises ;

  * Pays d’origine ;

  * TVA partenaire ;

  * Code de transport ;

  * [Code Incoterm](../customer_invoices/incoterms) ;

  * Poids ;

  * Unités supplémentaires ; et

  * Valeur, qui s’exprime toujours en euro, même si la facture client ou fournisseur d’origine utilise une autre devise.

