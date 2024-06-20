# Belgique

## Configuration

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
belge, conformément aux normes IFRS.

Nom | Nom technique | Description  
---|---|---  
Belgique - Comptabilité | `l10n_be` | [Package de localisation fiscale](../fiscal_localizations.html#fiscal-localizations-packages) par défaut.  
Belgique - Rapports comptables | `l10n_be_reports` | Accès aux rapports comptables spécifiques pour la Belgique.  
Belgique - Rapports comptables (assistant de poste) | `l10n_be_reports_post_wizard` | Active l’assistant TVA lors de la comptabilisation d’une pièce comptable de déclaration de TVA.  
Belgique - Importer les extraits de compte CODA | `l10n_be_coda` | Import des extraits de compte CODA.  
Belgique - Importer des fichiers SODA | `l10n_be_soda` | Import des fichiers SODA.  
Belgique - Données des dépenses non admises | `l10n_be_disallowed_expenses` | Accès à l’utilisation des fonctionnalités des dépenses non admises.  
Belgique - Paie | `l10n_be_hr_payroll` | Accès aux fonctionnalités de base de la paie en Belgique.  
Belgique - Paie avec Comptabilité | `l10n_be_hr_payroll_account` | Intégration des données comptables avec la paie.  
Belgique - Paie - Dimona | `l10n_be_hr_payroll_dimona` | Accès aux fonctionnalités Dimona pour la paie.  
Belgique - Paie - Parc automobile | `l10n_be_hr_payroll_fleet` | Fonctionnalités de parc automobile pour la paie.  
Configurateur de salaire (Belgique) | `l10n_be_hr_contract_salary` | Accès à la fonctionnalité du configurateur de salaire.  
  
## Plan comptable

Vous pouvez accéder au plan comptable en allant à Comptabilité ‣ Configuration
‣ Comptabilité : Plan comptable.

Le plan comptable belge inclut des comptes préconfigurés tels que décrits dans
le PCMN. Pour ajouter un nouveau compte, cliquez sur Nouveau. Une nouvelle
ligne apparaît. Complétez-la, cliquez sur Enregistrer et puis sur
Configuration pour la configurer plus en détail.

Pour plus d'infos

[Plan comptable](../accounting/get_started/chart_of_accounts.html)

## Taxes

Les taxes belges par défaut sont créées automatiquement lors de l’installation
des modules Belgique - Comptabilité et Belgique - Rapports comptables. Chaque
taxe affecte la Déclaration de TVA, accessible via Comptabilité ‣ Analyse ‣
Rapports de relevé : Déclaration de TVA.

En Belgique, le taux de TVA normal est de **21%** , mais il existe des taux
inférieurs pour certaines catégories de biens et de services. Un taux
intermédiaire de **12%** s’applique aux logements sociaux et à la nourriture
servie dans les restaurants, alors qu’un taux réduit de **6%** s’applique à la
plupart des biens de base, tels que les denrées alimentaires,
l’approvisionnement en eau, les livres et les médicaments. Un taux de **0%**
s’applique à certains biens et services exceptionnels, tels que certaines
publications quotidiennes et hebdomadaire, ainsi qu’aux produits recyclés.

### Taxes non déductibles

En Belgique, certaines taxes ne sont pas intégralement déductibles, telles que
les taxes sur l’entretien des véhicules. Cela signifie qu’une partie de ces
taxes est considérée comme une charge.

Dans Odoo, vous pouvez configurer des taxes non déductibles en créant des
règles pour ces taxes et en les associant aux comptes appropriés. De cette
façon, le système calcule les taxes automatiquement et les affecte aux bons
comptes.

Pour configurer une nouvelle taxe non déductible, allez à Comptabilité ‣
Configuration ‣ Comptabilité : Taxes et cliquez sur Nouveau :

  1. Ajouter une ligne et sélectionnez Base dans la colonne Basé sur ;

  2. Ajouter une ligne, puis sélectionnez Sur la taxe dans la colonne Basé sur et saisissez le pourcentage **non déductible** dans la colonne % ;

  3. Sur la ligne de la taxe, sélectionnez les Grilles de taxes associées à votre taxe ;

  4. Ajouter une ligne avec le pourcentage **deductible** dans la colonne % ;

  5. Sélectionnez de la taxe dans la colonne Basé sur ;

  6. Sélectionnez 411000 TVA récupérable dans la colonne Compte et sélectionnez la grille de taxes correspondante.

Une fois que vous avez créé une taxe non déductible, vous pouvez l’appliquer à
vos transactions en sélectionnant la bonne taxe lors de l’encodage des
factures fournisseurs et des avoirs. Le système calcule automatiquement le
montant de la taxe et l’affecte aux comptes correspondants en fonction des
règles fiscales configurées.

Example

Dans le cadre de la localisation belge, la taxe **21% car** est créée par
défaut (50% non déductible).

![Exemple d'une taxe qui n'est pas intégralement
déductible](../../../_images/deductible-tax.png)

Pour plus d'infos

  * [Taxes](../accounting/taxes.html)

  * [Déclaration d’impôt](../accounting/reporting/tax_returns.html)

## Rapports

Voici la liste des rapports spécifiques à la Belgique disponibles :

  * Bilan ;

  * Compte de résultat ;

  * Déclaration de TVA ;

  * Liste annuelle des clients assujettis à la TVA ;

  * Relevé intra-communautaire ;

  * Intrastat.

Vous pouvez accédez aux rapports spécifiques à la Belgique en cliquant sur
l’icône de **livre** sur un rapport et en sélectionnant sa version belge:
**(BE)**.

![Version belge des rapports](../../../_images/belgian-reports.png)

Pour plus d'infos

[Analyse](../accounting/reporting.html)

### Rapport de dépenses non admises

Les **Dépenses non admises** sont des dépenses qui peuvent être déduites de
votre résultat comptable, mais pas de votre résultat fiscal.

Le **rapport de dépenses non admises** est accessible via Comptabilité ‣
Analyse ‣ Gestion : Dépenses non admises. Il permet d’obtenir des résultats
financiers en temps réels, ainsi que les changements périodiques. Ce rapport
est généré sur la base des **catégories de dépenses non admises** auxquelles
vous pouvez accéder en allant à Comptabilité ‣ Configuration ‣ Gestion :
Catégories des dépenses non admises. Certaines catégories existent déjà par
défaut, mais n’ont aucun taux défini. Cliquez sur Définir les taux pour mettre
à jour une catégorie spécifique.

Astuce

  * Vous pouvez ajouter plusieurs taux pour des dates différentes. Dans ce cas, le taux utilisé pour calculer la dépense dépend de la date à laquelle elle est calculée et le taux défini pour cette date.

  * Si l’application **Parc automobile** est installé, cochez la case Catégorie de véhicule si elle s’applique. Le véhicule est alors obligatoire lors de l’enregistrement d’une facture fournisseur.

Pour lier une catégorie de dépenses non admises à un compte spécifique, allez
à Comptabilité ‣ Configuration ‣ Comptabilité : Plan comptable. Cherchez le
compte que vous voulez et cliquez sur Configuration. Ajoutez la Catégorie de
dépenses non admises dans le champ Dépenses non admises. À partir de là,
lorsqu’une dépense est créée avec ce compte, la dépense non admise est
calculée sur la base du taux défini dans la catégorie de dépenses non admises.

Prenons un exemple reflétant des **frais de restaurant** et des **frais de
voiture**.

#### Frais de restaurant

En Belgique, 31% des frais de **restaurant** ne sont pas déductibles. Créez
une nouvelle **catégorie de dépenses non admises** et définissez à la fois
le(s) Compte(s) lié(s) et le Taux actuel.

![Catégories de dépenses non admises](../../../_images/restaurant-
expenses.png)

#### Frais de voiture : Répartition des véhicules

En Belgique, le pourcentage déductible d’une voiture dépend de la voiture et
il doit donc être indiqué pour chaque véhicule. Pour ce faire, ouvrez
l’application Parc automobile et sélectionnez un véhicule. Dans l’onglet
Informations fiscales, allez à la section Taux de dépenses non admises et
cliquez sur Ajouter une ligne. Ajoutez une Date de début et un %. Les montants
sont enregistrés dans le même compte pour toutes les dépenses liées aux
véhicules.

Lorsque vous créez une facture fournisseur pour les frais de voiture, vous
pouvez lier chaque dépense à un véhicule spécifique en complétant la colonne
Véhicule afin d’appliquer le bon pourcentage.

![Catégories de dépenses non admises](../../../_images/car-bill.png)

L’option Répartition des véhicules du rapport de dépenses non admises vous
permet de voir le taux et du montant non admis pour chaque voiture.

![Catégories de dépenses non admises](../../../_images/vehicle-split.png)

## Fiche fiscale 281.50 et relevé 325

### Fiche fiscale 281.50

Chaque année, une **fiche fiscale 281.50** doit être déclarée aux autorités
fiscales. Pour ce faire, l’étiquette `281.50` doit être ajoutée à la **fiche
de contact** de toutes les entités visées par la fiche **281.50**. Pour
ajouter l’étiquette, ouvrez l’application Contacts, sélectionnez la personne
ou l’entreprise pour laquelle vous voulez créer une **fiche fiscale 281.50**
et ajoutez l’étiquette `281.50` dans le champ Étiquettes.

![ajoutez l'étiquette 281.50 sur la fiche](../../../_images/281-50.png)

Note

Assurez-vous que les champs **rue, code postal, pays** , et **numéro de TVA**
sont également complétés sur la **fiche de contact**.

Ensuite, selon la nature de la dépense, ajoutez l’étiquette `281.50`
correspondante sur les comptes impactés. Pour ce faire, allez à Comptabilité ‣
Configuration ‣ Comptabilité : Plan comptable et cliquez sur Configuration
pour ajouter l’étiquette `281.50` correspondante aux comptes impactés, c’est-
à-dire 281.50 - Commissions selon la nature de la dépense.

### Relevé 325

Vous pouvez créer un **relevé 325** en allant à Comptabilité ‣ Analyse ‣
Belgique : Créer le relevé 325. Une nouvelle page s’affiche : sélectionnez les
bonnes options et cliquez sur Générer le relevé 325. Pour ouvrir un **relevé
325** déjà généré, allez à Comptabilité ‣ Analyse ‣ Belgique : Ouvrir les
relevés 325.

![Ajoutez l'étiquette 281.50 sur la fiche de
contact](../../../_images/325-form.png)

## Fichiers CODA et SODA

### CODA

**CODA** est un format électronique XML utilisé pour importer des relevés
bancaires belges. Vous pouvez télécharger des fichiers CODA depuis votre
banque et les importer directement dans Odoo en cliquant sur Importer le
relevé sur votre journal de banque de votre tableau de bord.

![Importer des fichiers CODA](../../../_images/coda-import.png)

Note

Le module Belgique - Importer les extraits de compte CODA est installé par
défaut lors de l’installation des modules Belgique - Comptabilité et Belgique
- Rapports comptables.

Pour plus d'infos

[Importer des relevés
bancaires](../accounting/bank/transactions.html#transactions-import)

### SODA

**SODA** est un format électronique XML utilisé pour importer des pièces
comptables liées aux salaires. Les fichiers SODA peuvent être importés dans le
journal que vous utilisez pour enregistrer les salaires en allant dans votre
**tableau de bord** Comptabilité et en cliquant sur Charger dans le formulaire
de la fiche journal correspondante.

Une fois que vos fichiers **SODA** sont importés, les écritures sont créées
automatiquement dans votre journal “salaire”.

![Importer des fichiers SODA](../../../_images/soda-import.png)

## Facturation électronique

Odoo prend en charge les formats de facturation électronique **E-FFF** et
**Peppol BIS Billing 3.0 (UBL)**. Pour les activer, allez à Comptabilité ‣
Configuration ‣ Journaux ‣ Factures clients ‣ Paramètres avancés ‣ Facturation
électronique et cochez E-FFF (BE) et Peppol BIS Billing 3.0.

Pour plus d'infos

[Facturation électronique
(EDI)](../accounting/customer_invoices/electronic_invoicing.html)

## Escompte

En Belgique, si un escompte est offert sur une facture, la taxe est calculée
sur la base du montant total escompté, que le client bénéficie ou non de
l’escompte.

Pour appliquer le bon montant de taxe et l’indiquer correctement dans votre
déclaration de TVA, définissez la réduction de taxe comme Toujours (sur
facture).

Pour plus d'infos

[Escomptes et réduction
d’impôt](../accounting/customer_invoices/cash_discounts.html)

## Certification fiscale : PdV restaurant

En Belgique, le propriétaire d’une entreprise de cuisine telle qu’un
restaurant ou un food truck est tenu par la loi d’utiliser une **Caisse
enregistreuse** certifiée par le gouvernement pour ses recettes. Cette
obligation s’applique si ses revenus annuels (hors TVA, boissons et plats à
emporter) sont supérieurs à 25.000 euros.

Ce système certifié par le gouvernement demande l’utilisation d’un système de
caisse certifié, d’un dispositif appelé Module pour les données fiscales (ou
**boîte noire**) et une VAT Signing Card.

Important

N’oubliez pas de vous inscrire en tant que _gestionnaire de services
alimentaires_ sur le formulaire d’inscription du [Service Public Fédéral
Finances](https://www.systemedecaisseenregistreuse.be/fr/enregistrement).

### Système de caisse certifié

Le système de caisse d’Odoo est certifié pour les versions majeures des bases
de données hébergées sur **Odoo Online** et **Odoo.sh**. Veuillez consulter le
tableau ci-dessous pour vous assurer que votre système de caisse est certifié.

| Odoo Online | Odoo.sh | On premise  
---|---|---|---  
Odoo 16.0 | Certifié | Certifié | Non certifié  
Odoo 15.2 | Non certifié | Non certifié | Non certifié  
Odoo 15.0 | Certifié | Certifié | Non certifié  
Odoo 14.0 | Certifié | Certifié | Non certifié  
  
Pour plus d'infos

[Versions prises en charge](../../../administration/supported_versions.html)

Un [système de caisse
certifié](https://www.systemedecaisseenregistreuse.be/systemes-certifies) doit
respecter des réglementations gouvernementales rigoureuses, ce qui signifie
qu’il fonctionne différemment d’une caisse non certifiée.

  * Sur une caisse certifiée, vous ne pouvez pas :

    * Configurer et utiliser la fonctionnalité **remises globales** (le module `pos_discount` est sur liste noire et ne peut pas être activé).

    * Configurer et utiliser la fonctionnalité des **programmes de fidélité** (le module `pos_loyalty` est sur liste noire et ne peut pas être activé).

    * Imprimer des reçus (le module `pos_reprint` est sur liste noire et ne peut pas être activé).

    * Modifier les prix sur les lignes de commande.

    * Modifier ou supprimer les lignes de commande des commandes du point de vente.

    * Vendre des produits sans un numéro de TVA valide.

    * Utiliser un point de vente qui n’est pas connecté à une IoT Box.

  * La fonctionnalité [Arrondi des paiements en espèces](../../sales/point_of_sale/pricing/cash_rounding.html) doit être activée et configurée sur une Précision d’arrondi de `0,05` et une Méthode d’arrondi de Arrondir à l’entité supérieure.

  * Les taxes doivent être incluses dans le prix. Pour ce faire, allez à Point de Vente ‣ Configuration ‣ Paramètres et dans la section Comptabilité, ouvrez le formulaire Taxe de vente par défaut en cliquant sur la flèche à côté du champ de taxe de vente par défaut. Cliquez alors sur Options avancées et activez Inclus dans le prix.

  * Au début d’une session du point de vente, les utilisateurs doivent cliquer sur Début du travail pour pointer leur arrivée. Cela permet d’enregistrer les commandes du point de vente. Si les utilisateurs ne se sont pas enregistrés, ils ne peuvent pas passer de commandes du point de vente. De la même manière, ils doivent cliquer sur Fin du travail pour pointer leur départ à la fin de la session.

Avertissement

If you configure a POS to work with a FDM, you cannot use it again without it.

### Fiscal Data Module (FDM)

An FDM, or **black box** , is a government-certified device that works
together with the Point of Sale application and saves your POS orders
information. Concretely, a **hash** (unique code) is generated for each POS
order and added to its receipt. This allows the government to verify that all
revenue is declared.

Avertissement

Only the FDM from **Boîtenoire.be** with the [FDM certificate number
BMC04](https://www.systemedecaisseenregistreuse.be/fr/systemes-
certifies#FDM%20certifiés) is supported by Odoo. [Contact the manufacturer
(GCV BMC)](https://www.boîtenoire.be/contact) to order one.

#### Configuration

Avant de configurer votre base de données pour qu’elle fonctionne avec un FDM,
assurez-vous de disposer du matériel suivant :

  * a **Boîtenoire.be** (certificate number BMC04) FDM;

  * un câble série null modem RS-232 par FDM ;

  * un adaptateur série RS-232 vers USB par FDM ;

  * an IoT Box (one IoT box per FDM); and

  * une imprimante de reçus.

##### Module boîte noire

Comme prérequis, [activez](../../general/apps_modules.html#general-install) le
module `Tiroir-caisse enregistré en Belgique` (nom technique :
`pos_blackbox_be`).

![Modules boîte noire pour la certification fiscale
belge](../../../_images/be-modules.png)

Une fois le module activé, ajoutez votre numéro de TVA aux informations
relatives à votre entreprise. Pour le configurer, allez aux Paramètres ‣
Sociétés ‣ Mettre à jour les informations et complétez le champ TVA. Ensuite,
saisissez un numéro de registre national pour chaque membre du personnel qui
utilise le système de point de vente. Pour ce faire, allez à l’application
Employés et ouvrez la fiche d’un employé. Allez à l’onglet Paramètres RH ‣
Présente/Point de Vente et complétez le champ numéro INSZ ou BIS.

![Champ Numéro ISNZ ou BIS sur la fiche d'un employé](../../../_images/bis-
number.png)

Astuce

Pour saisir vos informations, cliquez sur votre avatar, allez à Mon profil ‣
onglet Préférences, et saisissez votre numéro INSZ ou BIS dans le champ
approprié.

Avertissement

You must configure the FDM directly in the production database. Utilizing it
in a testing environment may result in incorrect data being stored within the
FDM.

##### IoT Box

In order to use an FDM, you need a registered IoT Box. To register your IoT
box, you must contact us through our [support contact
form](https://www.odoo.com/help) and provide the following information:

  * votre numéro de TVA ;

  * le nom, l’adresse et la structure juridique de votre société ; et

  * l’adresse Mac de votre IoT Box.

Once your IoT box is certified,
[connect](../../general/iot/config/connect.html) it to your database. To
verify that the IoT Box recognizes the FDM, go to the IoT homepage and scroll
down the IOT Device section, which should display the FDM.

![Page de statut du matériel sur une IoT box
enregistrée](../../../_images/iot-devices.png)

Ajoutez ensuite l’IoT à votre Point de vente, Pour ce faire, allez à Point de
Vente ‣ Configuration ‣ Point de Vente, sélectionnez votre Point de vente,
faites défiler jusqu’à la section Périphériques connectés et activez IoT Box.
Enfin, ajoutez le FDM dans le champ Module pour les données fiscales.

Note

Pour pouvoir utiliser un FDM, vous devez au moins connecter une Imprimante de
reçus.

### VAT signing card

Lorsque vous ouvrez une session du point de vente et effectuez votre
transaction initiale, vous êtes invité à saisir le PIN fourni avec votre VSC.
La carte est délivrée par le SPF lors de
l”[enregistrement](https://www.systemedecaisseenregistreuse.be/fr/enregistrement).

  *[IFRS]: International Financial Reporting Standards
  *[PCMN]: Plan Comptable Minimum Normalisé
  *[FDM]: Fiscal Data Module
  *[VSC]: VAT signing card
  *[SPF]: Service Public Fédéral Finances

