# Australie

## Paie australienne avec Employment Hero

Le module Employment Hero synchronise automatiquement les écritures comptables
de fiche de paie (par ex. notes de frais, cotisations sociales, dettes, taxes)
entre Employment Hero et Odoo. L’administration de la paie se fait toujours
dans Employment Hero. Nous ne faisons qu’enregistrer les pièces comptables
dans Odoo.

Important

KeyPay a été rebaptisé **Employment Hero** en mars 2023.

### Configuration

  1. [Activez](../../general/apps_modules.html#general-install) le module Employment Hero Australian Payroll (nom technique : `l10n_au_keypay`).

  2. Configurez l”**API Employment Hero** en allant à Comptabilité ‣ Configuration ‣ Paramètres. D’autres champs deviennent visibles après avoir cliqué sur Activer l’intégration d’Employment Hero.

![L'activation de l'intégration d'Employment Hero dans Odoo Comptabilité
permet d'afficher de nouveaux champs dans les
paramètres](../../../_images/employment-hero-integration.png)

     * Vous trouverez la Clé API dans la section Mon compte de la plateforme Employment Hero.

![La section "Détails du compte" du tableau de bord Employment
Hero](../../../_images/employment-hero-myaccount.png)

     * L”**URL de la paie** est préremplie avec `https://keypay.yourpayroll.com.au`. _Veuillez ne pas la modifier_

     * Vous trouverez le **Business ID** dans l’URL d’Employment Hero URL. (c’est-à-dire `189241`).

![Le numéro "Business ID" d'Employment Hero se trouve dans
l'URL](../../../_images/employment-hero-business-id.png)

     * Vous pouvez choisir n’importe quel journal Odoo pour comptabiliser les écritures de fiche de paie.

### Comment fonctionne l’API ?

L’API synchronise les pièces comptables d’Employment Hero vers Odoo et les
laisse en mode brouillon. La référence inclut l’ID de l’écriture de fiche de
paie d’Employment Hero entre parenthèses pour que l’utilisateur puisse
facilement récupérer le même enregistrement dans Employment Hero et Odoo.

![Exemple d'une pièce comptable d'Employment Hero dans Odoo Comptabilité
\(Australie\)](../../../_images/employment-hero-journal-entry.png)

Par défaut, la synchronisation est effectuée une fois par semaine. Vous pouvez
récupérer les enregistrements manuellement en allant à Comptabilité ‣
Configuration ‣ Paramètres et, dans l’option Activer l’intégration
d’Employment Hero, cliquez sur Récupérer les fiches de paie manuellement.

Les écritures de fiche de paie d’Employment Hero fonctionnent également sur la
base de la comptabilité en partie double.

Les comptes utilisés par Employment Hero sont définis dans la section
Paramètres de paie.

![Menu du plan comptable dans Employment Hero](../../../_images/employment-
hero-chart-of-accounts.png)

Pour que l’API fonctionne, vous devez créer les mêmes comptes que les comptes
par défaut de votre Employment Hero business (**même nom et même code**) dans
Odoo. Vous devez également choisir les bons types de compte dans Odoo pour
générer des rapports financiers exacts.

