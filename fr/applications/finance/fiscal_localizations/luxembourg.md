# Luxembourg

## Configuration

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation
luxembourgeoise :

Nom | Nom technique | Description  
---|---|---  
Luxembourg - Comptabilité | `l10n_lu` | Le [package de localisation fiscale](../fiscal_localizations.html#fiscal-localizations-packages) par défaut  
Luxembourg - Rapports comptables | `l10n_lu_reports` | Rapports nationaux  
Luxembourg - Déclaration TVA annuelle | `l10n_lu_reports_annual_vat` | Rapports nationaux  
![Les trois modules du package de localisation fiscale luxembourgeoise dans
Odoo](../../../_images/modules1.png)

Astuce

L’installation du module Luxembourg - Rapports comptables installe les trois
modules en une fois.

## Plan comptable normalisé - PCN 2020

Le [package de localisation fiscale](../fiscal_localizations.html#fiscal-
localizations-packages) d’Odoo pour le Luxembourg inclut le **Plan comptable
normalisé (PCN 2020)** actuel, en vigueur depuis janvier 2020.

## Déclaration de TVA eCDF

Les déclarations de TVA au Luxembourg demandent un fichier XML spécifique à
charger sur la plateforme eCDF.

Pour la télécharger, allez à Comptabilité ‣ Analyse ‣ Rapports d’audit ‣
Déclaration de TVA et cliquez sur Exporter la déclaration eCDF.

Pour plus d'infos

  * [Déclaration d’impôt](../accounting/reporting/tax_returns.html)

  * [Plateforme électronique de collecte des données financières (eCDF)](http://www.ecdf.lu)

## Déclaration de TVA annuelle

Vous pouvez générer un fichier XML pour déposer votre déclaration de TVA
annuelle de manière électronique auprès de l’administration fiscale.

Pour ce faire, allez à Comptabilité ‣ Analyse ‣ Luxembourg ‣ Déclaration de
TVA annuelle, cliquez sur Créer, puis définissez la période annuelle dans le
champ Année.

La **déclaration annuelle simplifiée** est générée automatiquement. Vous
pouvez manuellement ajouter des valeurs dans tous les champs pour obtenir une
**déclaration annuelle complète**.

![Odoo Comptabilité \(localisation luxembourgeoise\) génère une déclaration de
TVA annuelle.](../../../_images/annual-tax-report.png)

Pour vous aider à la compléter, vous pouvez utiliser les informations fournies
dans la Déclaration de TVA. Pour ce faire, allez à Comptabilité ‣ Analyse ‣
Rapports d’audit ‣ Déclaration de TVA, cliquez sur le menu déroulant
Déclaration de TVA et sélectionnez le type de déclaration que vous souhaitez
afficher.

![Menu déroulant permettant de sélectionner le type de déclaration de
TVA](../../../_images/tax-report-types.png)

Enfin, cliquez sur Exporter XML pour télécharger le fichier XML.

Note

Cette fonctionnalité nécessite l’installation du module Luxembourg -
Déclaration de TVA annuelle.

## FAIA (SAF-T)

Le **FAIA (Fichier d’audit informatisé AED)** est un fichier standardisé et
structuré qui facilite l’échange d’informations entre le système comptable des
contribuables et l’administration fiscale. Il s’agit de la version
luxembourgeoise du SAF-T (Standard Audit File for Tax) recommandé par l’OCDE.

Odoo peut générer un fichier XML qui contient tous les contenus d’une période
comptable conformément aux règles imposées par les autorités fiscales
luxembourgeoises sur les fichiers d’audit numériques.

Note

Cette fonctionnalité nécessite l’installation du module Luxembourg - Rapports
comptables.

### Exporter le fichier FAIA

Allez à Comptabilité ‣ Analyse ‣ Rapports d’audit ‣ Grand livre, puis cliquez
sur FAIA.

