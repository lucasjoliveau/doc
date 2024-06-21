# Roumanie

## Configuration

[Installez](../../general/apps_modules#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
roumaine.

Nom | Nom technique | Description  
---|---|---  
**Roumanie - Comptabilité** | `l10n_ro` | [Package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut.  
**Romanian SAF-T Export** | `l10n_ro_saft` | Module permettant de générer la **déclaration D.406** au format SAF-T.  
![Modules pour la localisation roumaine](../../../_images/romania-modules.png)

## Déclaration D.406

À partir du 1 janvier 2023, les entreprises enregistrées à des fins fiscales
en Roumanie doivent communiquer leurs données comptables à l’Agence fiscale
roumaine tous les mois ou tous les trimestres dans la déclaration D.406.

Konvergo ERP fournit tout ce dont vous avez besoin pour exporter les données de cette
déclaration au format XML SAF-T, que vous pouvez valider et signer en
utilisant le logiciel fourni par l’Agence fiscale roumaine.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Actuellement, Konvergo ERP ne prend en charge que la génération de la déclaration mensuelle/trimestrielle D.406 (y compris les pièces comptables, les factures clients, les factures fournisseurs et les paiements). La déclaration annuelle (y compris les actifs) et la déclaration à la demande (y compris l’inventaire) ne sont pas encore prises en charge.</p>
</div>

### Configuration

#### Société

  * Dans **Paramètres – > Paramètres généraux**, dans la section **Sociétés** , cliquez sur **Mettre à jour les informations** et remplissez le **Pays** , la **Ville** , et le **Numéro de téléphone** de la société.

  * Saisissez le numéro CUI ou le numéro CIF (pour les entreprises étrangères) dans le champ **ID de la société** de la société, sans le préfixe `RO` (par ex. `18547290`).

  * Si votre entreprise est **enregistrée** à la TVA en Roumanie, remplissez le champ **N° TVA** , y compris le préfixe `RO` (par ex. `RO18547290`). Si l’entreprise n’est **pas** enregistrée à la TVA en Roumanie, vous **ne devez pas** compléter le champ **N° TVA**.

  * Ouvrez l’application **Contacts** et recherchez votre société. Ouvrez le profil de votre société et dans l’onglet **Comptabilité** , cliquez sur **Ajouter une ligne** et ajoutez votre **numéro de compte bancaire** si ce n’est pas déjà fait. Assurez-vous que le profil est défini sur **Société** au-dessus du **nom**.

    * Vous devez avoir au moins une **personne de contact** liée à votre société dans l’application **Contacts**. Si aucune **personne de contact** n’est liée, créez-en une nouvelle en cliquant sur **Nouveau** , définissez-la sur **Particulier** , et sélectionnez votre société dans le champ **Nom de la société**.

#### Plan comptable

Pour générer un dossier acceptable par l’Agence fiscale roumaine, le plan
comptable ne doit pas s’écarter d’un plan comptable officiel, tel que :

  * le plan comptable des sociétés commerciales (_PlanConturiBalSocCom_), qui est installé par défaut lors de la création d’une société avec la localisation roumaine ou ;

  * le plan comptable pour les entreprises qui suivent les normes [IFRS](https://www.ifrs.org/) (_PlanConturiIFRS_).

Dans **Paramètres – > Comptabilité**, dans la section **Localisation
roumaine** , définissez la **Base de comptabilité fiscale** afin de refléter
les règles comptables et le plan comptable utilisés par la société.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/get_started/chart_of_accounts">Plan comptable</a></p>
</div>

#### Client et fournisseur

Saisissez le **Pays** , la **Ville** et le **Code postal** de chaque
partenaire qui apparaît dans vos factures clients, factures fournisseurs ou
paiements via l’application **Contacts**.

Pour les partenaires qui sont des sociétés, vous devez remplir le numéro de
TVA (y compris le préfixe du pays) dans le champ **N° TVA**. Si le partenaire
est une société basée en Roumanie, vous pouvez indiquer le numéro CUI (sans le
préfixe “RO”) dans le champ **ID de la société**.

#### Taxe

Vous devez indiquer le **Type de taxe roumaine SAF-T** (numéro à 3 chiffres)
et le **Code de taxe roumaine SAF-T** (numéro à 6 chiffres) sur chacun des
impôts que vous utilisez. Ceci est déjà fait pour les taxes qui existent par
défaut dans Konvergo ERP. Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Taxes,
sélectionnez la taxe que vous voulez modifier, cliquez sur l’onglet **Options
avancées** et remplissez les champs **type de taxe** et **code de taxe**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le <b>type de taxe</b> et le <b>code de taxe</b> sont des codes définis par l’Agence fiscale roumaine pour la <b>déclaration D.406</b>. Ils figurent dans la feuille de calcul Excel publiée comme guide pour remplir la déclaration, que vous trouverez sur le <a href="https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/strategii_anaf/proiecte_digitalizare/saf_t/">site web de l’Agence fiscale roumaine</a>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/taxes">Taxes</a></p>
</div>

#### Produit

Pour certains types de transactions de marchandises, le **Code Intrastat**
(Cod NC) doit être configuré sur les produits, comme l’exige la loi roumaine :

  * transactions d’importation / d’exportation ;

  * achats / fournitures de produits alimentaires soumis à un taux de TVA réduit ;

  * mouvements intracommunautaires soumis à la déclaration Intrastat ;

  * achats / fournitures soumis à la TVA locale inversée (en fonction du Cod NC) ; et

  * transactions portant sur des produits soumis à accises pour lesquels les droits d’accises sont déterminés sur la base du Cod NC.

Si le Code Intrastat n’est pas déterminé sur un produit non service, le code
par défaut “0” sera utilisé.

Pour configurer les **Codes Intrastat** , allez à Comptabilité ‣ Clients ‣
Produits, sélectionnez un produit et dans l’onglet **Comptabilité** ,
définissez un **Code marchandises**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/reporting/intrastat">Intrastat</a></p>
</div>

#### Facture fournisseur

Vous devez cocher la case **Est autofacture (RO)?** dans l’onglet **Autres
informations** pour toute facture fournisseur qui est une autofacture (c’est-
à-dire une facture fournisseur que vous avez émise vous-même en l’absence
d’une facture reçue d’un fournisseur).

### Générer la déclaration

#### Exporter vos données

Pour exporter la déclaration D.406 au format XML, allez à Comptabilité ‣
Rapports ‣ Grand livre et cliquez sur **SAF-T**.

![Cliquez sur le bouton 'SAF-T' pour exporter la déclaration D.406 en
XML.](../../../_images/romania-saft-button.png)

Vous pouvez ensuite valider et signer le fichier XML avec le logiciel de
validation de l’Agence fiscale roumaine _DUKIntegrator_.

#### Signer le rapport

Téléchargez et installez le logiciel de validation _DUKIntegrator_ via le
[site web de l’Agence fiscale
roumaine](https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/strategii_anaf/proiecte_digitalizare/saf_t/).

Une fois que vous avez généré le XML, ouvrez “DUKIntegrator” et sélectionnez
le fichier que vous venez de générer.

Cliquez sur **Validare + creare PDF** pour créer un PDF **non signé**
contenant votre rapport ou sur **Validare + creare PDF semnat** pour créer un
PDF **signé** contenant votre rapport.

![Le logiciel de validation DUKIntegrator.](../../../_images/romania-
dukintegrator.png)

Si le validateur _DUKIntegrator_ détecte des erreurs ou des anomalies dans vos
données, il génère un fichier expliquant les erreurs. Dans ce cas, vous devez
corriger ces anomalies dans vos données avant de soumettre le rapport à
l’Agence fiscale roumaine.

  *[CUI]: Codul Unic de Inregistrare
  *[CIF]: *Codul de identificare fiscală*

