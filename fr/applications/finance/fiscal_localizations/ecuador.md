# Équateur

## Introduction

Avec la localisation équatorienne, vous pouvez générer des documents
électroniques avec son XML, son folio fiscal, sa signature électronique et sa
connexion directe à l’administration fiscale SRI.

Les documents pris en charge sont les factures, les avoirs, les notes de
débit, les preuves d’achat et les retenues.

La localisation comprend également des automatisations permettant de prévoir
facilement la retenue à la source à appliquer sur chaque facture d’achat.

Pour plus d'infos

  * [App Tour - Localización de Ecuador](https://www.youtube.com/watch?v=BQOXVSDeeK8)

  * [Tutoriel intelligent - Localización de Ecuador](https://www.odoo.com/slides/smart-tutorial-localizacion-de-ecuador-170)

### Glossaire

Voici quelques termes essentiels à la localisation équatorienne :

  * **SRI** signifie _Servicio de Rentas Internas_ , l’organisation gouvernementale qui veille au paiement des taxes en Equateur.

  * **EDI** signifie _Electronic Data Interchange_ ou _Échange de données informatisé_ , qui fait référence à l’envoi de documents électroniques.

  * **RIMPE** signifie _Regimen Simplificado para Emprendedores y Negocios_ , le type de contribuable qualifié pour le SRI.

## Configuration

### Installation des modules

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
équatorienne :

Nom | Nom technique | Description  
---|---|---  
Équateur - Comptabilité | `l10n_ec` | Le [package de localisation par défaut](../fiscal_localizations.html) ajoute des caractéristiques comptables pour la localisation équatorienne, qui représentent la configuration minimale requise pour qu’une entreprise puisse opérer en Equateur conformément aux directives établies par le SRI. L’installation du module charge automatiquement le plan comptable, les taxes, les types de documents, les types de support fiscal. De plus, la génération des déclarations 103 et 104 est automatique.  
EDI comptabilité équatorienne | `l10n_ec_edi` | Inclut toutes les exigences techniques et fonctionnelles pour générer et valider des [documents électroniques](../accounting/customer_invoices/electronic_invoicing.html), conformément à la documentation technique publiée par le SRI. Les documents autorisés sont les factures, les avoirs, les notes de crédit, les retenues et les preuves d’achat.  
  
Note

Lorsque vous installez une base de données à partir de zéro en sélectionnant
l”`Équateur` comme pays, Odoo installe automatiquement le module de base
Équateur - Comptabilité.

### Configurer votre société

Pour configurer les informations de votre société, allez à l’application
Contacts et recherchez le nom donné à votre entreprise ou activez le [mode
développeur](../../general/developer_mode.html#developer-mode) et allez à
Société ‣ Contact et modifiez le contact pour configurer les informations
suivantes :

  1. Cochez l’option Société en haut du formulaire

     * Nom

     * Adresse

     * Numéro d’identification

     * Type de contribuable

     * Téléphone

     * Email

  2. Chargez le logo de la société et enregistrez

![Complétez les données de la société équatorienne dans Odoo
Contacts.](../../../_images/ecuador-company.png)

### Documents électroniques

Pour charger les informations de vos documents électroniques, allez à
Comptabilité ‣ Configuration ‣ Paramètres et recherchez **Localisation
équatorienne**.

Configurez les informations suivantes :

  * Dénomination juridique de la société

  * Utiliser les serveurs de production : cochez la case si votre société va utiliser les documents électroniques dans l’environnement de production. Ne cochez pas la case si vous voulez utiliser l’environnement de test pour les documents électroniques.

  * Régime : sélectionnez si votre société est en Régime général ou si elle est qualifiée de RIMPE.

  * Obligation de tenir des livres comptables : cochez la case si votre société est dans cette situation.

  * Taxes par défaut pour les retenues à la source

  * Émission de retenues : cochez la case si votre société effectue des retenues à la source électroniques.

  * Retenue sur les biens de consommation : saisissez le code de la retenue lorsque vous achetez des marchandises.

  * Retenue sur les services : saisissez le code de la retenue lorsque vous achetez des services.

  * Retenue sur les cartes de crédit : saisissez le code de la retenue lorsque vous achetez avec la carte de crédit.

  * Numéro agent de retenue : saisissez le numéro de l’agent de retenue de la société, si applicable dans votre société.

  * Certificat électronique : chargez le certificat électronique et le mot de passe, puis enregistrez.

  * Numéro contribuable spécial : si votre société est qualifiée de contribuable spécial, saisissez son numéro de contribuable spécial dans le champ.

![Signature électronique pour l'Équateur.](../../../_images/electronic-
signature.png)

Note

Lors de la configuration des retenues dans le menu de configuration, ces
retenues suggérées sont uniquement destinées aux fournisseurs nationaux
lorsqu’aucune retenue n’est configurée sur leur _type de contribuable_. En
outre, la retenue sur les cartes de crédit est toujours utilisée lorsqu’un
mode de paiement SRI par carte de crédit ou de débit est utilisé.

### Retenue de la TVA

Cette configuration s’applique uniquement si vous êtes qualifié d” _Agent de
retenue_ par le SRI, sinon ignorez cette étape. Pour configurer votre retenue
de la TVA, allez à Comptabilité ‣ Comptabilité ‣ Configuration ‣ SRI
équatorien : Type de contribuable SRI.

Vous devez configurer le pourcentage de retenue qui s’applique à chaque type
de contribuable. Précisez la Retenue de la TVA sur les marchandises et la
Retenue de la TVA sur les services.

![Configuration du Type de contribuable pour
l'Équateur.](../../../_images/contributor-type.png)

Astuce

Si le Type de contribuable est `RIMPE`, configurez également le pourcentage de
Retenue sur les bénéfices.

### Points d’impression

Pour configurer vos points d’impression, allez à Comptabilité ‣ Configuration
‣ Comptabilité : Journaux.

Les points d’impression doivent être configurés pour chaque type de document
électronique dont vous avez besoin. Par exemple: Factures clients, Avoirs et
Notes de débit.

Pour chaque point d’impression, vous devez configurer les informations
suivantes :

  * Nom du journal : dans ce format `[Entité d'émission]-[Point d'émission] [Type de document]`, par exemple. `001-001 Documents de vente`.

  * Type : fait référence au type de journal. Sélectionnez `Vente`.

  * Utiliser des documents ? : cette case est automatiquement cochée. Laissez-la cochée.

  * Entité d’émission : configurez le numéro d’établissement.

  * Point d’émission : configurez le point d’impression.

  * Adresse d’émission : configurez l’adresse de l’établissement.

  * Compte des revenus par défaut : configurez le compte des revenus par défaut.

  * Séquence d’avoir dédiée : cochez la case si des _Avoirs_ doivent être générés à partir de ce point d’impression - journal.

  * Code court : Il s’agit du code unique de la séquence des pièces comptables. Saisissez un code unique à 5 chiffres, par exemple : `VT001`.

Les factures clients, les avoirs et les notes de débit doivent utiliser le
même journal que le Point d’émission et le Point d’entité doit être unique par
journal.

![Configurez un point d'impression pour le type de document électronique
équatorien des factures clients.](../../../_images/printer-point.png)

Note

Dans l’onglet Paramètres avancés, cochez la case Facturation électronique pour
l’activer pour l’Équateur.

Pour plus d'infos

[Facturation électronique
(EDI)](../accounting/customer_invoices/electronic_invoicing.html)

### Retenue

Un journal des retenues doit être défini, allez à Comptabilité ‣ Configuration
‣ Comptabilité : Journaux où vous pouvez configurer les informations suivantes
:

  * Nom du journal : dans ce format `[Entité d'émission]-[Point d'émission] [Type de document]`, par exemple. `001-001 Retenue`.

  * Type : fait référence au type de journal. Sélectionnez `Divers`.

  * Type de retenue : Configurez la Retenue sur les achats.

  * Utiliser des documents ? : cette case est automatiquement cochée. Laissez-la cochée.

  * Entité d’émission : configurez le numéro d’établissement.

  * Point d’émission : configurez le point d’impression.

  * Adresse d’émission : configurez l’adresse de l’établissement.

  * Compte par défaut : configurez le compte des revenus par défaut.

  * Code court : Il s’agit du code unique de la séquence des pièces comptables. Saisissez un code unique à 5 chiffres, par exemple : `RT001`.

![Configurez la retenue pour le type de retenue des documents électroniques
équatoriens](../../../_images/withhold.png)

Note

Dans l’onglet Paramètres avancés, cochez la case Facturation électronique pour
activer l’envoi des factures électroniques pour la retenue.

### Preuves d’achat

Lorsque vous utilisez des preuves d’achat, un journal spécifique doit être
créé. Allez à Comptabilité ‣ Configuration ‣ Comptabilité : Journaux et
configurez les informations suivantes :

  * Nom du journal : dans ce format `[Entité d'émission]-[Point d'émission] [Type de document]`, par exemple. `001-001 Retenue`.

  * Type : fait référence au type de journal. Sélectionnez `Divers`.

  * Preuves d’achat : cochez la case pour activer les preuves d’achat.

  * Utiliser des documents ? : cette case est automatiquement cochée. Laissez-la cochée.

  * Entité d’émission : configurez le numéro d’établissement.

  * Point d’émission : configurez le point d’impression.

  * Adresse d’émission : configurez l’adresse de l’établissement.

  * Code court : Il s’agit du code unique de la séquence des pièces comptables. Saisissez un code unique à 5 chiffres, par exemple : `RT001`.

![Configurez les preuves d'achat pour le type de retenue des documents
électroniques.](../../../_images/purchase-liqudations.png)

Note

Dans l’onglet Paramètres avancés, cochez la case Facturation électronique pour
activer l’envoi des factures électroniques pour la retenue.

### Configurer les données de base

#### Plan comptable

Le [plan comptable](../accounting/get_started/chart_of_accounts.html) est
installé par défaut dans l’ensemble des données du module de localisation. Les
comptes sont mappés automatiquement dans Taxes, Compte fournisseur par défaut
et Compte client par défaut.

Le plan comptable pour l’Équateur est basé sur la version la plus récente de
la Superintendencia de Compañías, qui est regroupée en plusieurs catégories et
est compatible avec la comptabilité IFRS.

Vous pouvez ajouter ou supprimer des comptes selon les besoins de
l’entreprise.

#### Produits

En plus des informations de base dans vos produits, vous devez ajouter la
configuration du code de retenue (taxe) qui s’applique.

Allez à Comptabilité ‣ Fournisseurs : Produits dans l’onglet « Achats ».

![Produit pour l'Équateur.](../../../_images/products.png)

#### Contacts

Configurez les informations suivantes lorsque vous créez un contact :

  * Cochez l’option Société en haut si le contact a un numéro RUC ou cochez Particulier si le contact a un numéro de cédula ou de passeport.

  * Nom

  * Adresse : Rue est un champ requis pour confirmer la facture électronique.

  * Numéro d’identification : sélectionnez un type d’identification : `RUC`, `Cedula`, ou `Passeport`.

  * Type de contribuable : sélectionnez le type de contribuable SRI du contact.

  * Téléphone

  * Email

![Contacts pour l'Équateur.](../../../_images/contacts.png)

Note

Le Type de contribuable SRI permet de configurer les retenues de TVA et de
bénéfices qui s’appliquent lorsque vous utilisez ce contact sur une facture
fournisseur et que vous créez ensuite une retenue à partir de ce contact.

#### Revoir vos taxes

Dans le cadre du module de localisation, les taxes sont créées automatiquement
avec leur configuration et comptes financiers correspondants.

![Taxes pour l'Équateur.](../../../_images/taxes.png)

Les options suivantes ont été configurées automatiquement :

  * Support fiscal : à configurer uniquement pour la TVA. Cette option est utile lorsque vous enregistrez des retenues sur les achats.

  * Code ATS : à configurer uniquement pour les codes de retenue à la source. Cette option est importante lorsque vous enregistrez la retenue.

  * Grilles de taxes : configurez les codes de la déclaration 104 s’il s’agit de la TVA et configurez les codes de la déclaration 103 s’il s’agit d’une retenue à la source.

  * Nom de taxe :

    * Pour la TVA, formatez le nom comme suit : `TVA [pourcentage] (104, [code déclaration] [code support fiscal] [nom court support fiscal])`

    * Pour les retenues à la source, formatez le nom comme suit : `Code ATS [Pourcentage de retenue] [nom de la retenue]`

Une fois que le module équatorien est installé, les taxes les plus courantes
sont configurées automatiquement. Si vous devez créer une taxe supplémentaire,
vous devez vous baser sur la configuration des taxes existantes.

![Taxes avec support fiscal pour l'Équateur.](../../../_images/taxes-with-tax-
support.png)

#### Revoir vos types de documents

Certaines transactions comptables, telles que les _Factures clients_ et les
_Factures fournisseurs_ , sont classées par types de documents. Ceux-ci sont
définis par les autorités fiscales, en l’espèce le SRI.

Chaque type de document peut avoir une séquence unique par journal auquel il
est assigné. Dans le cadre de la localisation, le type de document inclut le
pays sur lequel le document s’applique ; et les données sont créées
automatiquement lors de l’installation du module de localisation.

Les informations requises pour les types de documents sont comprises par
défaut, donc l’utilisateur n’a rien à compléter.

![Types de documents pour l'Équateur.](../../../_images/document-types.png)

## Flux de travail

Une fois que vous avez configuré votre base de données, vous pouvez
enregistrer vos documents.

### Documents de vente

#### Factures clients

Les Factures clients sont des documents électroniques qui, une fois validés,
sont envoyés au SRI. Ces documents peuvent être créés à partir de votre
commande client ou manuellement. Ils doivent contenir les données suivantes :

  * Client : saisissez les informations du client.

  * Journal : sélectionnez l’option qui correspond au point d’impression de la facture client.

  * Type de document : saisissez le type de document dans ce format `(01) Facture`.

  * Mode de paiement (SRI) : sélectionnez le mode de paiement de la facture.

  * Produits : précisez le produit avec les bonnes taxes.

![Facture client pour l'Équateur.](../../../_images/customer-invoice.png)

#### Avoir client

L”[Avoir client](../accounting/customer_invoices/credit_notes.html) est un
document électronique qui, après validation, est envoyé au SRI. Vous devez
avoir une facture validée (comptabilisée) pour pouvoir enregistrer un avoir.
Sur la facture, il y a un bouton intitulé Avoir, cliquez sur ce bouton pour
être redirigé vers le formulaire Créer un avoir, puis complétez les
informations suivantes :

  * Méthode de crédit : sélectionnez le type de méthode de crédit.

    * Remboursement partiel : utilisez cette option lorsque vous devez saisir le premier numéro des documents et s’il s’agit d’un avoir partiel.

    * Remboursement intégral : utilisez cette option si l’avoir concerne la totalité de la facture et si vous voulez que l’avoir soit validé automatiquement et lettré avec la facture.

    * Remboursement intégral et nouvelle facture brouillon : utilisez cette option si l’avoir concerne la totalité de la facture et si vous voulez que l’avoir soit validé automatiquement et lettré avec la facture, et qu’une nouvelle facture brouillon soit établie automatiquement.

  * Motif : saisissez le motif de l’avoir.

  * Date d’annulation : sélectionnez les options spécifiques.

  * Date d’extourne : saisissez la date.

  * Utiliser un journal spécifique : sélectionnez le point d’impression de votre avoir ou laissez-le vide si vous voulez utiliser le même journal que la facture d’origine.

Une fois que vous avez terminé, vous pouvez cliquer sur le bouton Extourner.

![Ajouter un avoir client pour l'Équateur.](../../../_images/add-customer-
credit-note.png)

Lorsque vous utilisez l’option Remboursement partiel, vous pouvez modifier le
montant de l’avoir et puis le valider. Avant de valider l’avoir, vérifiez les
informations suivantes :

  * Client : saisissez les informations du client.

  * Journal : sélectionnez le point d’impression de l’avoir client.

  * Type de document : il s’agit du type de document `(04) Avoir`.

  * Produits : vous devez préciser le produit avec les bonnes taxes.

![Avoir client pour l'Équateur.](../../../_images/customer-credit-note.png)

#### Note de débit client

La Note de débit client est un document électronique qui, après validation,
est envoyé au SRI. Vous devez avoir une facture validée (comptabilisée) pour
pouvoir enregistrer une note de débit. Il y a un bouton intitulé Note de débit
sur la facture, cliquez sur ce bouton pour être redirigé vers le formulaire
Créer une note de débit, puis complétez les informations suivantes :

  * Motif : saisissez le motif de la note de débit.

  * Date de la note de débit : sélectionnez les options spécifiques.

  * Copier les lignes : sélectionnez cette option si vous devez enregistrer une note de débit avec les mêmes lignes que la facture.

  * Utiliser un journal spécifique : sélectionnez le point d’impression de votre avoir ou laissez-le vide si vous voulez utiliser le même journal que la facture d’origine.

Une fois que vous avez terminé, vous pouvez cliquer sur le bouton Créer une
note de débit.

![Ajouter une note de débit client pour l'Équateur.](../../../_images/add-
customer-debit-note.png)

Vous pouvez modifier le montant de la note de débit, puis la valider. Avant de
valider la note de débit, vérifiez les informations suivantes :

  * Client : saisissez les informations du client.

  * Journal : sélectionnez le point d’impression de l’avoir client.

  * Type de document : il s’agit du type de document `(05) Note de débit`.

  * Produits : vous devez préciser le produit avec les bonnes taxes.

![Note de débit client pour l'Équateur.](../../../_images/customer-debit-
note.png)

#### Retenue client

La Retenue client est un document non électronique pour votre entreprise. Ce
document est émis par le client afin d’appliquer une retenue à la vente.

Vous devez avoir une facture validée (comptabilisée) pour pouvoir enregistrer
une retenue client. Sur la facture, il y a un bouton intitulé Ajouter une
retenue, cliquez sur ce bouton pour être redirigé vers le formulaire Retenue
client, puis complétez les informations suivantes :

  * Numéro de document : saisissez le numéro de la retenue.

  * Lignes de retenue : sélectionnez les taxes que le client retient.

Avant de valider la retenue, vérifiez que les montants de chaque taxe sont
identiques à ceux du document d’origine.

![Retenue client pour l'Équateur.](../../../_images/customer-withhold.png)

### Documents d’achat

#### Facture fournisseur

La Facture fournisseur est un document non électronique pour votre entreprise.
Ce document est émis par votre fournisseur lorsque votre entreprise effectue
un achat.

Les factures fournisseurs peuvent être créées à partir du bon de commande ou
manuellement. Elles doivent contenir les informations suivantes :

  * Fournisseur : saisissez les coordonnées du fournisseur.

  * Date de facturation : sélectionnez la date de la facture.

  * Journal : il s’agit du journal pour les factures fournisseurs.

  * Type de document : il s’agit du type de document `(01) Facture`.

  * Numéro de document : saisissez le numéro du document.

  * Mode de paiement (SRI) : sélectionnez le mode de paiement de la facture.

  * Produits : précisez le produit avec les bonnes taxes.

![Achats pour l'Équateur.](../../../_images/purchase-invoice.png)

Important

Lors de la création de la retenue sur achats, vérifiez que les bases (montants
de base) sont corrects. Si vous devez modifier le montant de la taxe de la
Facture fournisseur, cliquez sur le bouton Modifier. Sinon, dans l’onglet
Écritures comptables, cliquez sur le bouton Modifier et réglez l’ajustement
comme vous le souhaitez.

#### Preuve d’achat

La Preuve d’achat est un document électronique qui, après validation, est
envoyé au SRI.

Les sociétés émettent ce type de document électronique lorsqu’elles achètent
et que le fournisseur n’émet pas de facture en raison d’un ou de plusieurs des
cas suivants :

  * Les services ont été fournis par des non-résidents d’Équateur.

  * Les services fournis par des sociétés étrangères sans résidence ni établissement en Équateur.

  * L’achat de biens ou de services auprès des personnes physiques sans RUC qui, en raison de leur niveau culturel ou de leur rusticité, ne sont pas en mesure d’émettre des reçus de vente ou des factures clients.

  * Le remboursement de l’achat de biens ou de services aux employés en situation de dépendance (employés à temps plein).

  * Les services fournis par les membres des organes collégiaux dans l’exercice de leur fonction.

Ces types de documents électroniques peuvent être créés à partir du Bon de
commande ou manuellement à partir de la vue de formulaire des Factures
fournisseurs. Ils doivent contenir les données suivantes :

  * Fournisseur : saisissez les coordonnées du fournisseur.

  * Journal : sélectionnez le journal pour la Preuve d’achat avec le bon point d’impression.

  * Type de document : il s’agit du type de document `(03) Preuve d'achat`.

  * Numéro de document : saisissez le numéro de document (séquence), vous ne devrez le faire qu’une seule fois, puis la séquence sera automatiquement attribuée pour les documents suivants.

  * Mode de paiement (SRI) : sélectionnez le mode de paiement de la facture.

  * Produits : précisez le produit avec les bonnes taxes.

Une fois que vous avez vérifié les informations, vous pouvez valider la Preuve
d’achat.

![Preuve d'achat pour l'Équateur.](../../../_images/purchase-liquidation.png)

#### Retenue sur les achats

La Retenue sur les achats est un document électronique qui, après validation,
est envoyé au SRI.

Vous devez avoir une facture validée pour pouvoir enregistrer une Retenue sur
les achats. Sur la facture, il y a un bouton intitulé Ajouter une retenue,
cliquez sur ce bouton pour être redirigé vers le formulaire de Retenue, puis
complétez les informations suivantes :

  * Numéro de document : saisissez le numéro de document (séquence), vous ne devrez le faire qu’une seule fois, puis la séquence sera automatiquement attribuée pour les documents suivants.

  * Lignes de retenue : Les taxes apparaissent automatiquement en fonction de la configuration des produits et des fournisseurs. Vous devez vérifier si les taxes et le support fiscal sont corrects et, si ce n’est pas le cas, vous pouvez modifier et sélectionner les taxes et le support fiscal corrects.

Une fois que vous avez vérifié les informations, vous pouvez valider la
Retenue.

![Retenue sur les achats pour l'Équateur.](../../../_images/purchase-
withhold.png)

Note

Vous ne pouvez pas modifier le support fiscal d’une taxe qui n’a pas été
incluse dans la configuration des taxes utilisées sur la Facture fournisseur.
Pour ce faire, allez à la taxe appliquée à la Facture fournisseur et modifiez
le Support fiscal.

Une retenue à la source peut être divisée en une ou plusieurs lignes, selon
que deux ou plusieurs pourcentages de retenue s’appliquent ou non.

Example

Le système propose une retenue de TVA de 30% avec le support fiscal 01. Vous
pouvez ajouter votre retenue de TVA de 70% sur une nouvelle ligne avec le même
support fiscal. Le système vous y autorise pour autant que le total des bases
corresponde au total de la Facture fournisseur.

## Rapports financiers

En Équateur, les sociétés doivent présenter certains rapports fiscaux au SRI.
Dans Odoo, nous avons deux des principaux rapports financiers utilisés par les
entreprises. Il s’agit des déclarations 103 et 104.

Pour obtenir ces rapports, allez à l’application Comptabilité et sélectionnez
Analyse ‣ Rapports de relevé ‣ Déclaration de TVA, puis filtrez par
`Déclaration fiscale 103` ou `Déclaration fiscale 104`.

### Déclaration 103

Ce rapport contient des informations sur les retenues à la source au cours
d’une période donnée, qui peuvent être déclarées mensuellement ou
semestriellement.

Vous pouvez consulter les informations nécessaires au rapport, qui comprennent
les montants de base et de taxe, ainsi que le code fiscal entre parenthèses
afin de le déclarer au SRI.

![Déclaration 103 pour l'Équateur.](../../../_images/103-form.png)

### Déclaration 104

Ce rapport contient des informations sur la TVA et la retenue à la source pour
une période donnée, qui peut être mensuelle ou semestrielle.

Vous pouvez consulter les informations nécessaires au rapport, qui comprennent
les montants de base et de taxe, ainsi que le code fiscal entre parenthèses
afin de le déclarer au SRI.

![Déclaration 104 pour l'Équateur.](../../../_images/104-form.png)

### ATS report

[Install](../../general/apps_modules.html#general-install) the _ATS Report_
(`l10n_ec_reports_ats`) module to enable downloading the ATS report in XML
format.

Note

The Ecuadorian _ATS Report_ module is dependent on the previous installation
of the _Accounting_ app and the _Ecuadorian EDI module_.

#### Configuration

To issue electronic documents, ensure your company is configured as explained
in the electronic invoice section.

In the ATS, every document generated in Odoo (invoices, vendor bills, sales
and purchases withholdings, credit notes, and debit notes) will be included.

##### Factures fournisseurs

When generating a vendor bill, it is necessary to register the authorization
number from the invoice that the vendor generated for the purchase. To do so,
go to Accounting ‣ Vendors ‣ Bills and select the bill. Then, enter the number
from the vendor’s invoice in the Authorization Number field.

##### Credit and debit notes

When generating a credit note or debit note manually or through importation,
it is necessary to link this note to the sales invoice that is being modified
by it.

Note

Remember to add all required information to the documents before downloading
the ATS file. For example, add the _Authorization Number_ and the _SRI Payment
Method_ on documents, when needed.

#### XML generation

To generate the ATS report, go to Accounting ‣ Reports ‣ Tax Report and choose
a time period for the desired ATS report, then click ATS.

The downloaded XML file is ready to be uploaded to _DIMM Formularios_.

![ATS report download for Ecuador in Odoo Accounting.](../../../_images/ats-
report.png)

Note

When downloading the ATS report, Odoo generates a warning pop-up alerting the
user if a document(s) has missing or incorrect data. Nevertheless, the user
can still download the XML file.

  *[SRI]: servicio de rentas internas
  *[ATS]: Anexo Transaccional Simplificado

