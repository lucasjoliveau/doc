# Égypte

## Installation

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation égyptienne
:

Nom | Nom technique | Description  
---|---|---  
Égypte - Comptabilité | `l10n_eg` | Le [package de localisation fiscale](../fiscal_localizations.html#fiscal-localizations-packages) par défaut  
Intégration de la facturation électronique égyptienne | `l10n_eg_edi_eta` | Autorité fiscale égyptienne (ETA) intégration de la facturation électronique  
  
## Facturation électronique égyptienne

Odoo est conforme aux exigences de l”**Autorité fiscale égyptienne (Egyptian
Tax Authority - ETA) en matière de facturation électronique**.

Important

La facturation électronique égyptienne est disponible à partir d’Odoo 15.0. Le
cas échéant, [mettez à niveau](../../../administration/upgrade.html) votre
base de données.

Pour plus d'infos

  * [Vidéo : Facturation électronique égyptienne](https://www.youtube.com/watch?v=NXuBPLR4pVw)

  * [Mettre à niveau](../../../administration/upgrade.html)

### Enregistrer Odoo sur votre portail ETA

Vous devez enregistrer votre système ERP Odoo sur votre portail ETA pour
obtenir les identifiants de votre API. Vous avez besoin de ces codes pour
configurer votre application Comptabilité d’Odoo.

Accédez au profil de votre société sur le portail ETA en cliquant sur Voir le
profil du contribuable.

![Cliquez sur "Voir le profil du contribuable" sur le portail de facturation
ETA](../../../_images/taxpayer-profile.png)

Allez ensuite à la section Représentants et cliquez sur Enregistrer un ERP.
Complétez le Nom de l’ERP (par ex. `Odoo`) et laissez les autres champs vides.

![Complétez le formulaire pour enregistrer un système ERP sur le portail
ETA.](../../../_images/add-erp-system.png)

Une fois l’enregistrement réussi, le site web affiche vos identifiants API :

  * ID client

  * Secret client 1

  * Secret client 2

Note

  * L’ETA devrait vous donner un nom d’utilisateur et un mot de passe pour accéder à leur portail en ligne.

  * Demandez à l’ETA de vous donner également un accès au portail de préproduction.

  * Ces codes sont confidentiels et doivent être conservés en toute sécurité.

### Configuration dans Odoo

Pour connecter votre base de données Odoo à votre compte de portail ETA, allez
à Comptabilité ‣ Configuration ‣ Paramètres ‣ Paramètres facturation
électroniques ETA et configurez le ETA ID client et ETA Secret que vous avez
récupérés lorsque vous avez enregistré Odoo sur votre portail ETA. Définissez
un seuil de facturation si nécessaire.

![Configuration des identifiants de la facturation électronique ETA dans Odoo
Comptabilité](../../../_images/eta-api-integration.png)

Important

  * **Effectuez des tests sur votre portail de préproduction** avant d’émettre de vraies factures sur le portail ETA de production.

  * Les **Identifiants** pour les environnements de préproduction et de production sont différents. Veillez à les mettre à jour dans Odoo avant de passer d’un environnement à un autre.

  * Si ce n’est pas encore fait, complétez les coordonnées de votre entreprise avec l’adresse complète, le pays et l’ID fiscale.

#### Codes ETA

La facturation électronique fonctionne avec un ensemble de codes fournis par
l’ETA. Consultez la [documentation de
l’ETA](https://sdk.preprod.invoicing.eta.gov.eg/codes/) pour coder vos
caractéristiques commerciales.

Odoo gère automatiquement la plupart de ces codes, à condition que vos
branches, vos clients, et vos produits soient configurés correctement.

  * Informations relatives à l’entreprise :

    * ID fiscal de l’entreprise

    * ID de la branche

Si vous n’avez qu’une seule branche, utilisez `0` comme code de la branche.

    * Code du type d’activité

  * Autres informations :

    * Codes des produits

Les produits de votre société doivent être codés et correspondre à leurs codes
**GS1** ou **EGS**.

    * Codes fiscaux

La plupart des codes fiscaux sont déjà configurés dans Odoo dans le champ Code
ETA (Égypte). Nous vous conseillons de vous assurer que ces codes
correspondent aux taxes de votre entreprise.

Pour plus d'infos

  * [Facturation électronique et reçu électronique SDK en Égypte - Tableaux de codes](https://sdk.preprod.invoicing.eta.gov.eg/codes/)

  * [Taxes](../accounting/taxes.html)

#### Branches

Créez un contact et un journal pour chaque branche de votre entreprise et
configurez ses paramètres ETA.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux, puis cliquez
sur Créer.

Nommez le journal en fonction de la branche de votre entreprise et définissez
le Type sur Ventes. Ouvrez ensuite l’onglet Paramètres avancés et complétez la
section Paramètres ETA Égyptien :

  * Dans le champ Branche, sélectionnez le contact de la branche ou créez-le.

  * Définissez le Code d’activité ETA.

  * Définissez l”ID de la branche ETA (utilisez `0` si vous n’avez qu’une seule branche).

![Configuration d'un journal des ventes d'une branche d'une entreprise
égyptienne](../../../_images/branch-journal.png)

Important

Le contact sélectionné dans le champ Branche doit être défini sur Société
(**pas** sur Particulier) et les champs Adresse et ID fiscal doivent être
complétés.

#### Clients

Assurez-vous que les formulaires de contact de vos clients sont correctement
remplis afin que vos factures électroniques soient valides :

  * Type de contact : Particulier: ou Société:

  * Pays:

  * ID fiscal: Numéro fiscal ou registre des sociétés pour les entreprises. Numéro de carte d’identité pour les particuliers.

Note

Vous pouvez modifier les fiches de contact de vos clients en allant à
Comptabilité ‣ Clients ‣ Clients.

#### Produits

Assurez-vous que vos produits sont correctement configurés pour que vos
factures électroniques soient valides :

  * Type de produit : produits stockables, produits consommables ou services.

  * Unit of Measure: if you also use Odoo Inventory and have enabled [Units of Measure](../../inventory_and_mrp/inventory/product_management/product_replenishment/uom.html).

  * Code-barres : code-barres **GS1** ou **EGS**

  * Code d’article ETA (dans l’onglet Comptabilité) : si le code-barres ne correspond pas à votre code d’article ETA.

Note

Vous pouvez modifier vos produits en allant à Comptabilité ‣ Clients ‣
Produits.

### Authentification par USB

Chaque personne qui doit signer des factures de manière électronique a besoin
d’une clé USB spécifique pour s’authentifier et envoyer des factures au
portail ETA par le biais d’un ERP.

Note

Vous pouvez contacter l”ETA ou [Egypt Trust](https://www.egypttrust.com/) pour
obtenir ces clés USB.

#### Installer Odoo en tant que proxy local sur votre ordinateur

Un serveur local Odoo fonctionne comme une passerelle entre votre ordinateur
et votre base de données Odoo hébergée en ligne.

Téléchargez l’installateur Odoo Community de la page
<https://www.odoo.com/page/download> et lancez l’installation sur votre
ordinateur.

Sélectionnez Local Proxy Mode en tant que type d’installation.

![Sélection de "Local Proxy Mode" pendant l'installation d'Odoo
Community.](../../../_images/install-odoo-local-proxy.png)

Note

Cette installation d’Odoo ne fonctionne que comme un serveur et n’installe
aucune application Odoo sur votre ordinateur.

Une fois que l’installation est finalisée, l’installateur affiche votre
**jeton d’accès** au proxy local Odoo. Copiez le jeton et enregistrez-le dans
un endroit sûr pour l’utiliser plus tard.

Pour plus d'infos

  * [Odoo : Télécharger Odoo](https://www.odoo.com/page/download)

  * [On-premise](../../../administration/on_premise.html)

#### Configurer la clé USB

Une fois que le serveur proxy local est installé sur votre ordinateur, vous
pouvez le lier à votre base de données Odoo.

  1. Allez à Comptabilité ‣ Configurations ‣ Clé USB et cliquez sur Créer.

  2. Saisissez un nom de Société, le Pin USB ETA qui vous a été donné par le fournisseur de votre clé USB et le Jeton d’accès fourni à la fin de l”installation du proxy local, puis cliquez sur Enregistrer.

  3. Cliquez sur Obtenir le certificat.

![Créer une nouvelle clé USB pour la facturation électronique d'une entreprise
égyptienne.](../../../_images/thumb-drive.png)

  *[ETA]: Autorité fiscale égyptienne

