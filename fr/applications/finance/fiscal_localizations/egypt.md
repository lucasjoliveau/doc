# Égypte

## Installation

[Installez](../../general/apps_modules#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation égyptienne
:

Nom | Nom technique | Description  
---|---|---  
**Égypte - Comptabilité** | `l10n_eg` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut  
**Intégration de la facturation électronique égyptienne** | `l10n_eg_edi_eta` | Autorité fiscale égyptienne (ETA) intégration de la facturation électronique  
  
## Facturation électronique égyptienne

Konvergo ERP est conforme aux exigences de l”**Autorité fiscale égyptienne (Egyptian
Tax Authority - ETA) en matière de facturation électronique**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La facturation électronique égyptienne est disponible à partir d’Konvergo ERP 15.0. Le cas échéant, <a href="../../../administration/upgrade">mettez à niveau</a> votre base de données.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Vidéo : Facturation électronique égyptienne</a></p></li>
<li><p><a href="../../../administration/upgrade">Mettre à niveau</a></p></li>
</ul>
</div>

### Enregistrer Konvergo ERP sur votre portail ETA

Vous devez enregistrer votre système ERP Konvergo ERP sur votre portail ETA pour
obtenir les identifiants de votre API. Vous avez besoin de ces codes pour
configurer votre application Comptabilité d’Konvergo ERP.

Accédez au profil de votre société sur le portail ETA en cliquant sur **Voir
le profil du contribuable**.

![Cliquez sur "Voir le profil du contribuable" sur le portail de facturation
ETA](../../../_images/taxpayer-profile.png)

Allez ensuite à la section **Représentants** et cliquez sur **Enregistrer un
ERP**. Complétez le **Nom de l’ERP** (par ex. `Konvergo ERP`) et laissez les autres
champs vides.

![Complétez le formulaire pour enregistrer un système ERP sur le portail
ETA.](../../../_images/add-erp-system.png)

Une fois l’enregistrement réussi, le site web affiche vos identifiants API :

  * ID client

  * Secret client 1

  * Secret client 2

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>L’ETA devrait vous donner un nom d’utilisateur et un mot de passe pour accéder à leur portail en ligne.</p></li>
<li><p>Demandez à l’ETA de vous donner également un accès au portail de préproduction.</p></li>
<li><p>Ces codes sont confidentiels et doivent être conservés en toute sécurité.</p></li>
</ul>
</div>

### Configuration dans Konvergo ERP

Pour connecter votre base de données Konvergo ERP à votre compte de portail ETA, allez
à Comptabilité ‣ Configuration ‣ Paramètres ‣ Paramètres facturation
électroniques ETA et configurez le **ETA ID client** et **ETA Secret** que
vous avez récupérés lorsque vous avez enregistré Konvergo ERP sur votre portail ETA.
Définissez un seuil de facturation si nécessaire.

![Configuration des identifiants de la facturation électronique ETA dans Konvergo ERP
Comptabilité](../../../_images/eta-api-integration.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p><b>Effectuez des tests sur votre portail de préproduction</b> avant d’émettre de vraies factures sur le portail ETA de production.</p></li>
<li><p>Les <b>Identifiants</b> pour les environnements de préproduction et de production sont différents. Veillez à les mettre à jour dans Konvergo ERP avant de passer d’un environnement à un autre.</p></li>
<li><p>Si ce n’est pas encore fait, complétez les coordonnées de votre entreprise avec l’adresse complète, le pays et l’ID fiscale.</p></li>
</ul>
</div>

#### Codes ETA

La facturation électronique fonctionne avec un ensemble de codes fournis par
l’ETA. Consultez la [documentation de
l’ETA](https://sdk.preprod.invoicing.eta.gov.eg/codes/) pour coder vos
caractéristiques commerciales.

Konvergo ERP gère automatiquement la plupart de ces codes, à condition que vos
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

La plupart des codes fiscaux sont déjà configurés dans Konvergo ERP dans le champ
**Code ETA (Égypte)**. Nous vous conseillons de vous assurer que ces codes
correspondent aux taxes de votre entreprise.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://sdk.preprod.invoicing.eta.gov.eg/codes/">Facturation électronique et reçu électronique SDK en Égypte - Tableaux de codes</a></p></li>
<li><p><a href="../accounting/taxes">Taxes</a></p></li>
</ul>
</div>

#### Branches

Créez un contact et un journal pour chaque branche de votre entreprise et
configurez ses paramètres ETA.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux, puis cliquez
sur **Créer**.

Nommez le journal en fonction de la branche de votre entreprise et définissez
le **Type** sur **Ventes**. Ouvrez ensuite l’onglet Paramètres avancés et
complétez la section **Paramètres ETA Égyptien** :

  * Dans le champ **Branche** , sélectionnez le contact de la branche ou créez-le.

  * Définissez le **Code d’activité ETA**.

  * Définissez l”**ID de la branche ETA** (utilisez `0` si vous n’avez qu’une seule branche).

![Configuration d'un journal des ventes d'une branche d'une entreprise
égyptienne](../../../_images/branch-journal.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le contact sélectionné dans le champ <b>Branche</b> doit être défini sur <b>Société</b> (<b>pas</b> sur <b>Particulier</b>) et les champs <b>Adresse</b> et <b>ID fiscal</b> doivent être complétés.</p>
</div>

#### Clients

Assurez-vous que les formulaires de contact de vos clients sont correctement
remplis afin que vos factures électroniques soient valides :

  * Type de contact : **Particulier** : ou **Société** :

  * **Pays** :

  * **ID fiscal** : Numéro fiscal ou registre des sociétés pour les entreprises. Numéro de carte d’identité pour les particuliers.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier les fiches de contact de vos clients en allant à Comptabilité ‣ Clients ‣ Clients.</p>
</div>

#### Produits

Assurez-vous que vos produits sont correctement configurés pour que vos
factures électroniques soient valides :

  * **Type de produit** : produits stockables, produits consommables ou services.

  * **Unit of Measure** : if you also use Konvergo ERP Inventory and have enabled [Units of Measure](../../inventory_and_mrp/inventory/product_management/product_replenishment/uom).

  * **Code-barres** : code-barres **GS1** ou **EGS**

  * **Code d’article ETA** (dans l’onglet Comptabilité) : si le code-barres ne correspond pas à votre code d’article ETA.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier vos produits en allant à Comptabilité ‣ Clients ‣ Produits.</p>
</div>

### Authentification par USB

Chaque personne qui doit signer des factures de manière électronique a besoin
d’une clé USB spécifique pour s’authentifier et envoyer des factures au
portail ETA par le biais d’un ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez contacter l”<abbr title="Autorité fiscale égyptienne">ETA</abbr> ou <a href="https://www.egypttrust.com/">Egypt Trust</a> pour obtenir ces clés USB.</p>
</div>

#### Installer Konvergo ERP en tant que proxy local sur votre ordinateur

Un serveur local Konvergo ERP fonctionne comme une passerelle entre votre ordinateur
et votre base de données Konvergo ERP hébergée en ligne.

Téléchargez l’installateur Konvergo ERP Community de la page
<https://www.odoo.com/page/download> et lancez l’installation sur votre
ordinateur.

Sélectionnez **Local Proxy Mode** en tant que type d’installation.

![Sélection de "Local Proxy Mode" pendant l'installation d'Konvergo ERP
Community.](../../../_images/install-odoo-local-proxy.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cette installation d’Konvergo ERP ne fonctionne que comme un serveur et n’installe aucune application Konvergo ERP sur votre ordinateur.</p>
</div>

Une fois que l’installation est finalisée, l’installateur affiche votre
**jeton d’accès** au proxy local Konvergo ERP. Copiez le jeton et enregistrez-le dans
un endroit sûr pour l’utiliser plus tard.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Vidéo : Facturation électronique égyptienne</a></p></li>
<li><p><a href="../../../administration/upgrade">Mettre à niveau</a></p></li>
</ul>
</div>0

#### Configurer la clé USB

Une fois que le serveur proxy local est installé sur votre ordinateur, vous
pouvez le lier à votre base de données Konvergo ERP.

  1. Allez à Comptabilité ‣ Configurations ‣ Clé USB et cliquez sur **Créer**.

  2. Saisissez un nom de **Société** , le **Pin USB ETA** qui vous a été donné par le fournisseur de votre clé USB et le **Jeton d’accès** fourni à la fin de l”installation du proxy local, puis cliquez sur **Enregistrer**.

  3. Cliquez sur **Obtenir le certificat**.

![Créer une nouvelle clé USB pour la facturation électronique d'une entreprise
égyptienne.](../../../_images/thumb-drive.png)

