# Thaïlande

## Configuration

[Installez](../../general/apps_modules#general-install) le package de
localisation de la **🇹🇭 Thaïlande** pour obtenir toutes les fonctionnalités de
la localisation thaï :

Nom | Nom technique | Description  
---|---|---  
**Thaïlande - Comptabilité** | `l10n_th` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut  
**Thaïlande - Rapports comptables** | `l10n_th_reports` | Rapports comptables nationaux  
![Modules de la localisation thaï](../../../_images/modules2.png)

## Plan comptable et taxes

Le package de localisation fiscale d’Konvergo ERP pour la Thaïlande comprend les taxes
suivantes :

  * TVA 7%

  * Exonéré de la TVA

  * Impôt à la source

  * Retenue à la source

## Déclaration de TVA

Konvergo ERP permet aux utilisateurs de générer des fichiers Excel afin de soumettre
leur déclaration de TVA au **Département des Revenus** en Thaïlande.

### Rapport sur la taxe sur les ventes et les achats

Pour générer un rapport sur la taxe sur les ventes et les achats, allez à
Comptabilité ‣ Analyse ‣ Déclaration de TVA. Sélectionnez une date ou une
période spécifique sur la déclaration de TVA, puis cliquez sur **VAT-202-01
(xlsx)** pour la taxe sur les achats et **VAT-202-02 (xlsx)** pour la taxe sur
les ventes.

![Les rapports sur la taxe sur les ventes et les achats en
Thaïlande](../../../_images/tax-report.png)

### Retenue à la source PND

Les données du rapport PND affichent les montants récapitulatifs des **impôts
retenus par la société (au niveau national)** sur les factures fournisseurs
sous les déclarations de TVA **PND53 (TH)** et **PND3 (TH)**. Il est installé
par défaut avec la localisation thaï.

![Déclarations de TVA PND](../../../_images/pnd-report.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La déclaration des impôts retenus par la société sur les vendeurs (au niveau national) est utilisée lorsque l’entreprise a retenu l’impôt sur les services fournis par les “<b>Personnes physiques (PND3)</b>” ou les “<b>Personnes morales (PND53)</b>” tels que la location, le transport, l’assurance, les frais de gestion, la consultance, etc.</p>
</div>

La déclaration PND permet aux utilisateurs de générer un fichier CSV pour les
factures à charger sur [l’application RDprep for Thailand
e-Filling](https://efiling.rd.go.th/rd-cms/).

Pour générer un fichier PND sous format CSV, allez à Comptabilité ‣ Analyse ‣
Déclaration de TVA, sélectionnez une date ou une période spécifiques sur la
déclaration de TVA et cliquez sur **PND3** ou **PND53**.

Cela génère les fichiers `Tax Report PND3.csv` et `Tax Report PND53.csv` qui
répertorient toutes les lignes de facture fournisseur avec la retenue à la
source applicable.

![Fichiers CSV PND3 et PND53](../../../_images/pnd3-pnd53.png)
<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Konvergo ERP ne peut pas générer directement la déclaration PNC ou PDF ou le <b>certificat d’impôt à la source</b>. Les fichiers <code>Tax Report PND3.csv</code> et <code>Tax Report PND53.csv</code> générés doivent être exportés vers un outil externe pour les convertir en déclaration <b>Retenue à la source PND</b> ou en fichier <b>PDF</b>.</p>
</div>

## Facture fiscale

Le rapport PDF de la **facture fiscale** peut être généré à partir d’Konvergo ERP via
le module **Facturation**. Les utilisateurs ont la possibilité d’imprimer les
rapports PDF pour les factures normales et les factures fiscales. Pour
imprimer les **factures fiscales** , les utilisateurs peuvent cliquer sur
**Imprimer les factures** dans Konvergo ERP. Les factures normales peuvent être
imprimées en tant que **factures commerciales** en cliquant sur le bouton d”
Engrenage (⚙️) ‣ Imprimer ‣ Facture commerciale.

![Impression d'une facture commerciale](../../../_images/tax-invoice.png)

### Paramétrage du numéro de siège social/de la filiale

Vous pouvez renseigner le numéro de **siège social** et de **filiale** de la
société dans l’application **Contacts**. Dans l’application, ouvrez la **fiche
de contact** de la société et dans l’onglet **Ventes & Achats** :

  * S’il s’agit d’une filiale, saisissez le **Numéro de la filiale** dans le champ **ID de la société**.

  * S’il s’agit d’un **siège social** , laissez le champ **ID de la société** **vide**.

![Numéro du siège social/de la filiale de la
société](../../../_images/contact.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Ces informations sont utilisées dans le rapport PDF de la <b>facture fiscale</b> et dans l’exportation de la <b>déclaration de TVA</b> PND.</p>
</div>

