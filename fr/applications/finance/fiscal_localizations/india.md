# Inde

## Installation

[Installez](../../general/apps_modules#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation indienne :

Nom | Nom technique | Description  
---|---|---  
**Inde - Comptabilité** | `l10n_in` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut  
**Inde - Facturation électronique** | `l10n_in_edi` | Intégration de la facturation électronique en Inde  
**Inde - E-waybill** | `l10n_in_edi_ewaybill` | Intégration E-waybill en Inde  
**Inde - Dépôt électronique déclaration GSTR en Inde** | `l10n_in_reports_gstr` | Dépôt déclaration GST en Inde  
**Inde - Rapports comptables** | `l10n_in_reports` | Déclarations d’impôt en Inde  
**Inde - Rapport d’achats (GST)** | `l10n_in_purchase` | Rapport GST sur les achats en Inde  
**Inde - Rapport de ventes (GST)** | `l10n_in_sale` | Rapport GST sur les ventes en Inde  
**Inde - Rapport sur le stock (GST)** | `l10n_in_stock` | Rapport GST sur le stock en Inde  
![Modules de localisation indienne](../../../_images/india-modules.png)

## Système de facturation électronique

Konvergo ERP est conforme aux exigences du **Système de facturation électronique de la
taxe indienne sur les produits et les services (GST)**

### Configuration

#### Enregistrement NIC e-Invoice

Vous devez vous enregistrer sur le portail NIC e-Invoice pour obtenir vos
**identifiants API**. Vous avez besoin de ces identifiants pour configurer
votre application Comptabilité d’Konvergo ERP.

  1. Connectez-vous au [portail NIC e-Invoice](https://einvoice1.gst.gov.in/) en cliquant sur **Connexion** et en saisissant votre **Nom d’utilisateur** et **Mot de passe** ;

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous êtes déjà enregistré sur le portail NIC, vous pouvez utiliser les mêmes identifiants de connexion.</p>
</div> ![Enregistrez le système ERP Konvergo ERP sur le portail web
e-Invoice](../../../_images/e-invoice-system-login.png)

  2. À partir du tableau de bord, allez à Enregistrement API ‣ Identifiants Utilisateur ‣ Créer utilisateur API ;

  3. Ensuite, vous recevez un code OTP sur votre numéro de téléphone portable enregistré. Saisissez le code OTP et cliquez sur **Vérifier OTP** ;

  4. Sélectionnez **Via GSP** pour l’interface de l’API, choisissez **Tera Software Limited** comme GSP et saisissez un **Nom d’utilisateur** et un **Mot de passe** pour votre API. Une fois cela fait, cliquez sur **Soumettre**.

![Soumettez un nom d'utilisateur et un mot de passe spécifiques à
l'API](../../../_images/submit-api-registration-details.png)

#### Configuration dans Konvergo ERP

Pour autoriser le service e-Invoice dans Konvergo ERP, allez à Comptabilité ‣
Configuration ‣ Paramètres ‣ Facturation électronique indienne et saisissez le
**Nom d’utilisateur** et le **Mot de passe** précédemment définis pour l’API.

![Configuration du service de facturation
électronique](../../../_images/e-invoice-setup.png)

##### Journaux

Pour envoyer automatiquement des factures électroniques au portail NIC
e-Invoice, vous devez d’abord configurer votre journal de _ventes_ en allant à
Comptabilité ‣ Configuration ‣ Journaux, en ouvrant votre journal de _ventes_
et dans l’onglet **Paramètres avancés** , sous **Échange de données
informatisé** , activez **E-Invoice (IN)** et enregistrez.

### Flux de travail

#### Validation des factures

Une fois qu’une facture est validée, un message de configuration s’affiche en
haut. Konvergo ERP charge automatiquement le fichier signé JSON des factures validées
sur le portail NIC e-Invoice après un certain temps. Si vous souhaitez traiter
la facture immédiatement, cliquez sur **Traiter maintenant**.

![Message de configuration de la facturation électronique
indienne](../../../_images/e-invoice-process.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous trouverez le fichier signé JSON dans les fichiers joints dans le chatter.</p></li>
<li><p>Vous pouvez vérifier le statut <abbr title="échange de données informatisé">EDI</abbr> du document dans l’onglet <b>EDI Document</b> ou dans le champ <b>Facturation électronique</b> de la facture.</p></li>
</ul>
</div>

#### Rapport PDF de la facture

Une fois qu’une facture est validée et soumise, le rapport PDF de la facture
peut être imprimé. Le rapport comprend le IRN, le **Ack. No** (numéro d’accusé
de réception) et la **Ack. Date** (date d’accusé de réception), et le code QR.
Ces éléments certifient que la facture est un document fiscal valide.

![IRN et code QR](../../../_images/invoice-report.png)

#### Annulation de la facture électronique

Si vous voulez annuler une facture électronique, allez à l’onglet **Autres
informations** de la facture et complétez les champs **Motif de l’annulation**
et **Remarques d’annulation**. Cliquez ensuite sur **Demander l’annulation
EDI**. Le statut du champ **Facturation électronique** passe à **À annuler**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Cette opération annule à la fois la <a href="#india-e-invoicing"><span class="std std-ref">facture électronique</span></a> et l”<a href="#india-e-waybill"><span class="std std-ref">E-Way bill</span></a>.</p>
</div> ![Motif d'annulation et
remarques](../../../_images/e-invoice-cancellation.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Si vous voulez annuler l’annulation avant de traiter la facture, cliquez sur <b>Annuler l’annulation EDI</b>.</p></li>
<li><p>Une fois que vous avez demandé l’annulation de la facture électronique, Konvergo ERP soumet automatiquement le fichier signé JSON au portail NIC e-Invoice. Vous pouvez cliquer sur <b>Traiter maintenant</b> si vous voulez traiter la facture immédiatement.</p></li>
</ul>
</div>

#### Vérification de la facture électronique GST

Après avoir soumis une facture électronique, vous pouvez vérifier si la
facture a été signée à partir du site web du GST e-Invoice system.

  1. Téléchargez le fichier JSON à partir des fichiers joints. Il se trouve dans le chatter de la facture concernée ;

  2. Ouvrez le [portail NIC e-Invoice](https://einvoice1.gst.gov.in/) et allez à Rechercher ‣ Vérifier la facture signée ;

  3. Sélectionnez le fichier JSON et soumettez-le ;

![Sélectionnez le fichier JSON pour vérifier la
facture](../../../_images/verify-invoice.png)

Si le fichier est signé, un message de confirmation s’affiche.

![facture électronique vérifiée](../../../_images/signed-invoice.png)

## E-Way bill

### Configuration

Konvergo ERP est conforme aux exigences du **Système de facturation électronique de la
taxe indienne sur les produits et les services (GST)**

#### Enregistrement API sur NIC E-Way bill

Vous devez vous enregistrer sur le portail NIC E-Way bill pour générer vos
**identifiants API**. Vous avez besoin de ces identifiants pour configurer
votre application Comptabilité d’Konvergo ERP.

  1. Connectez-vous au portail [NIC E-Way bill](https://ewaybillgst.gov.in/) en cliquant sur **Connexion** et en saisissant votre **Nom d’utilisateur** et **Mot de passe** ;

  2. À partir de votre tableau de bord, allez à Enregistrement ‣ Pour GSP ;

  3. Cliquez sur **Envoyer OTP**. Une fois que vous avez reçu le code sur votre numéro de téléphone portable enregistré, saisissez-le et cliquez sur **Vérifier OTP** ;

  4. Vérifiez si **Tera Software Limited** figure déjà sur la liste des GSP/ERP enregistrés. Si c’est le cas, utilisez le nom d’utilisateur et le mot de passe utilisés pour vous connecter au portail NIC. Si ce n’est pas le cas, suivez les étapes suivantes :

![Liste des GSP/ERP enregistrés sur E-Way bill](../../../_images/e-waybill-
gsp-list.png)

  5. Sélectionnez **Ajouter/Nouveau** , choisissez **Tera Software Limited** comme votre Nom de GSP, créez un **Nom d’utilisateur** et un **Mot de passe** pour votre API et cliquez sur **Ajouter**.

![Soumettez les détails d'enregistrement API GSP](../../../_images/e-waybill-
registration-details.png)

#### Configuration dans Konvergo ERP

Pour configurer le service E-Way bill, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Electronic WayBill indien ‣ Configurer E-Way bill, et saisissez
votre **Nom d’utilisateur** et **Mot de passe**.

![Configuration E-way bill dans Konvergo ERP](../../../_images/e-waybill-
configuration.png)

### Flux de travail

#### Envoyer un E-Way bill

Vous pouvez manuellement envoyer un E-Way bill en cliquant sur **Envoyer E-Way
bill**. Pour envoyer l’E-Way bill automatiquement lorsqu’une facture client ou
une facture fournisseur est confirmée, activez **E-Way bill (IN)** dans votre
Journal de ventes ou d’achats.

![Bouton Envoyer E-Waybill sur les factures](../../../_images/e-waybill-send-
button.png)

#### Validation des factures

Une fois qu’une facture a été émise et envoyée via **Envoyer E-Way bill** , un
message de confirmation s’affiche.

![Message de confirmation de l'e-Way bill indien](../../../_images/e-waybill-
process.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous trouverez le fichier signé JSON dans les fichiers joints dans le chatter.</p></li>
<li><p>Konvergo ERP charge automatiquement le fichier signé JSON au portail du gouvernement après un certain temps. Cliquez sur <b>Traiter maintenant</b> si vous voulez traiter la facture immédiatement.</p></li>
</ul>
</div>

#### Rapport PDF de la facture

Vous pouvez imprimer le rapport PDF de la facture après avoir soumis l’E-Way
bill. Le rapport comprend le **numéro de l’E-Way bill** et la **date de
validité de l’E-Way bill**.

![Le numéro et la date de l'accusé de réception de l'E-way
bill](../../../_images/e-waybill-invoice-report.png)

#### Annulation de l’E-Way bill

Si vous voulez annuler un E-Way bill, allez à l’onglet **E-Way bill** de la
facture concernée et complétez les champs **Motif de l’annulation** et
**Remarques d’annulation**. Cliquez ensuite sur **Demander l’annulation EDI**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Cette opération annule à la fois la <a href="#india-e-invoicing"><span class="std std-ref">facture électronique</span></a> (le cas échéant) et l”<a href="#india-e-waybill"><span class="std std-ref">E-Way bill</span></a>.</p>
</div> ![Motif d'annulation et
remarques](../../../_images/e-waybill-cancellation.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Si vous voulez annuler l’annulation avant de traiter la facture, cliquez sur <b>Annuler l’annulation EDI</b>.</p></li>
<li><p>Une fois que vous avez demandé l’annulation de l’E-Way bill, Konvergo ERP soumet automatiquement le fichier signé JSON au portail du gouvernement. Vous pouvez cliquer sur <b>Traiter maintenant</b> si vous voulez traiter la facture immédiatement.</p></li>
</ul>
</div>

## Dépôt déclaration GST en Inde

### Activer l’accès API

Pour déposer des déclarations GST dans Konvergo ERP, vous devez d’abord activer
l’accès API sur le portail GST.

  1. Connectez-vous au [portail GST](https://services.gst.gov.in/services/login) en saisissant votre **Nom d’utilisateur** et **Mot de passe** et allez à **Mon profil** dans le **menu de votre profil** ;

![Cliquez sur Mon profil à partir du profil](../../../_images/gst-portal-my-
profile.png)

  2. Sélectionnez **Gérer l’accès API** et cliquez sur **Oui** pour activer l’accès API ;

![Cliquez sur Oui](../../../_images/gst-portal-api-yes.png)

  3. Cette opération fait apparaître un menu déroulant **Durée**. Sélectionnez la **Durée** de votre choix et cliquez sur **Confirmer**.

### Service GST indien dans Konvergo ERP

Une fois que vous avez activé l”accès API sur le portail GST, vous pouvez
configurer le **Service GST indien** dans Konvergo ERP.

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Service GST indien et
saisissez le **Nom d’utilisateur GST**. Cliquez sur **Envoyer OTP** ,
saisissez le code et enfin cliquez sur **Valider**.

> ![Veuillez saisir votre Nom d'utilisateur du portail GST comme Nom
> d'utilisateur](../../../_images/gst-setup.png)

### Déposer une déclaration GST

Lorsque le **Service GST indien** est configuré, vous pouvez déposer votre
déclaration GST. Allez à Comptabilité ‣ Analyse ‣ Inde ‣ Périodes de
déclaration GST et créez une nouvelle **Période de déclaration GST** si elle
n’existe pas. Le dépôt de la déclaration GST se fait en **trois étapes** dans
Konvergo ERP :

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La <b>Périodicité de la déclaration d’impôt</b> peut être <a href="../accounting/reporting/tax_returns">configurée</a> en fonction des besoins de l’utilisateur.</p>
</div>

#### Envoyer GSTR-1

  1. L’utilisateur peut vérifier le rapport GSTR-1 avant de le charger sur le **portail GST** en cliquant sur **Rapport GSTR-1** ;

  2. Si le rapport **GSTR-1** est correct, cliquez sur **Envoyer au GSTN** pour l’envoyer au **portail GST**. Le statut du rapport **GSTR-1** passe à **En cours d’envoi** ;

![GSTR-1 avec le statut En cours d'envoi](../../../_images/gst-
gstr-1-sending.png)

  3. Après quelques secondes, le statut du rapport **GSTR-1** passe à **En attente de statut**. Cela signifie que le rapport **GSTR-1** a été envoyé au **portail GST** et est examiné sur le **portail GST** ;

![GSTR-1 avec le statut En attente de statut](../../../_images/gst-
gstr-1-waiting.png)

  4. Une fois de plus, après quelques secondes, le statut passe à **Envoyé** ou **Erreur dans la facture**. Le statut **Erreur dans la facture** indique que certaines factures ne sont pas complétées correctement pour être validées par le **portail GST** ;

     * Si le statut du **GSTR-1** est **Envoyé** , cela signifie que votre rapport **GSTR-1** est prêt à être déposé sur le **portail GST**.

![GSTR-1 envoyé](../../../_images/gst-gstr-1-sent.png)

     * Si le statut du **GSTR-1** est **Erreur dans la facture** , vous pouvez vérifier les factures pour les erreurs dans la **Note de journal**. Une fois les problèmes résolus, l’utilisateur peut cliquer sur **Envoyer vers GSTN** pour soumettre à niveau le fichier sur le **portail GST**.

![GSTR-1 Erreur dans la facture](../../../_images/gst-gstr-1-error.png)

![GSTR-1 Erreur dans la facture Journal](../../../_images/gst-gstr-1-error-
log.png)

  5. Cliquez sur **Marquer comme déposé** après avoir soumis le rapport **GSTR-1** sur le **portail GST**. Le statut du rapport passé à **Déposé** dans **Konvergo ERP**.

![GSTR-1 avec le statut Déposé](../../../_images/gst-gstr-1-filed.png)

#### Recevoir GSTR-2B

Les utilisateurs peuvent récupérer le **rapport GSTR-2B** du **portail GST**.
Ceci lettre automatiquement le rapport **GSTR-2B** avec vos factures dans Konvergo ERP
;

  1. Cliquez sur **Récupérer le récapitulatif GSTR-2B** afin de récupérer le récapitulatif **GSTR-2B**. Après quelques secondes, le statut du rapport passe à **En attente de réception**. Cela signifie qu’Konvergo ERP essaie de récupérer le rapport **GSTR-2B** du **portail GST** ;

![GSTR-2B avec le Statut En attente de réception](../../../_images/gst-
gstr-2b-waiting.png)

  2. Une fois de plus, après quelques secondes, le statut du **GSTR-2B** passe à **En cours de traitement**. Cela signifie qu’Konvergo ERP est en train de lettrer le rapport **GSTR-2B** avec vos facture dans Konvergo ERP ;

![GSTR-2B avec le Statut En attente de réception](../../../_images/gst-
gstr-2b-processed.png)

  3. Une fois cela fait, le statut du rapport **GSTR-2B** passe à **Lettré** ou **Partiellement lettré** ;

     * Si le statut est **Lettré** :

> ![GSTR-2B Lettré](../../../_images/gst-gstr-2b-matched.png)

     * Si le statut est **Partiellement lettré** , vous pouvez modifier les factures en cliquant sur **Voir les factures lettrées**. Une fois cela fait, cliquez sur **lettrer à nouveau**.

> ![GSTR-2B Partiellement lettré](../../../_images/gst-gstr-2b-partially.png)
> ![GSTR-2B Factures lettrées](../../../_images/gst-gstr-2b-reconcile.png)

#### Rapport GSTR-3

Le rapport GSTR-3 est un récapitulatif mensuel des **ventes** et des
**achats**. Cette déclaration est générée automatiquement suite à l’extraction
des informations des rapports **GSTR-1** et **GSTR-2**.

  1. Les utilisateurs peuvent comparer le rapport **GSTR-3** avec le rapport **GSTR-3** disponible sur le **portail GST** pour vérifier s’ils correspondent en cliquant sur **Rapport GSTR-3** ;

  2. Une fois que le rapport **GSTR-3** a été vérifié par l’utilisateur et le montant de la taxe a été payé sur le **portail GST** , le rapport peut être **clôturé** en cliquant sur **Écriture de clôture** ;

![GSTR-3](../../../_images/gst-gstr-3.png)

  3. Dans l”**Écriture de clôture** , ajoutez le montant de la taxe payé sur le **portail GST** via Challan et cliquez sur **COMPTABILISER** pour comptabiliser l”**Écriture de clôture** ;

![Comptabiliser l'écriture GSTR-3](../../../_images/gst-gstr-3-post.png)

  4. Une fois comptabilisé, le statut du rapport **GSTR-3** passe à **Déposé**.

![GSTR-3 Déposé](../../../_images/gst-gstr-3-filed.png)

## Déclarations d’impôt

### Rapport GSTR-1

Le rapport **GSTR-1** est divisé en différentes sections. Il affiche le
montant de **Base** , la CGST, la SGST, la IGST, et la **CESS** pour chaque
section.

> ![Rapport GSTR-1](../../../_images/gst-gstr-1-sale-report.png)

### Rapport GSTR-3

Le rapport **GSTR-3** contient différentes sections :

  * Détails des livraisons entrantes et sortantes soumises à une **autoliquidation** ;

  * ITC éligible ;

  * Valeurs des livraisons entrantes **exonérées** , **non taxées** , et **non soumises à la GST** ;

  * Détails des livraisons inter-étatiques effectuées à des personnes **non enregistrées**.

> ![Rapport GSTR-3](../../../_images/gst-gstr-3-report.png)

  *[NIC]: National Informatics Centre
  *[OTP]: mot de passe à usage unique
  *[IRN]: Numéro de référence de la facture
  *[CGST]: Central Goods and Services Tax
  *[SGST]: State Goods and Service Tax
  *[IGST]: Integrated Goods and Services Tax
  *[ITC]: Income Tax Credit

