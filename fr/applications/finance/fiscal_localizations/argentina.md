# Argentine

## Webinars

Vous trouverez ci-dessous des vidéos avec une description générale de la
localisation et la façon de la configurer.

  * [Webinar - Localización de Argentina](https://www.youtube.com/watch?v=_H1HbU-wKVg).

  * [eCommerce - Localización de Argentina](https://www.youtube.com/watch?v=5gUi2WWfRuI).

Pour plus d'infos

[Tutoriel intelligent - Localización de
Argentina](https://www.odoo.com/slides/smart-tutorial-localizacion-de-
argentina-130)

## Configuration

### Installation des modules

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
argentine :

Nom | Nom technique | Description  
---|---|---  
Argentine - Comptabilité | `l10n_ar` | Le [package de localisation fiscale](../fiscal_localizations.html#fiscal-localizations-packages) par défaut, qui représente la configuration minimale pour qu’une entreprise puisse opérer en Argentine conformément aux réglementations et directives AFIP.  
Rapports comptables argentins | `l10n_ar_reports` | État comptable de la TVA et état récapitulatif de la TVA.  
Facturation électronique argentine | `l10n_ar_edi` | Comprend toutes les exigences techniques et fonctionnelles permettant de générer des factures électroniques via un service web, conformément aux réglementations AFIP.  
eCommerce argentin | `l10n_ar_website_sale` | (facultatif) Permet à l’utilisateur de voir le Type d’identification et la Responsabilité AFIP dans le formulaire de paiement eCommerce afin de créer des factures électroniques.  
  
### Configurer votre société

Lorsque les modules de localisation sont installés, la première étape consiste
à configurer les données de la société. En plus des informations essentielles,
un champ clé à remplir est le Type de responsabilité AFIP, qui représente
l’obligation et la structure fiscale de la société.

![Sélectionnez le type de responsabilité AFIP.](../../../_images/select-
responsibility-type.png)

### Plan comptable

Dans l’application Comptabilité, vous pouvez choisir entre trois différents
packages de plan comptable. Ils sont basés sur le type de responsabilité AFIP
d’une société et tiennent compte de la différence entre les sociétés qui n’ont
pas besoin d’autant de comptes et celles qui ont des exigences fiscales plus
complexes :

  * Monotributista (227 comptes) ;

  * IVA Exento (290 comptes) ;

  * Responsable Inscripto (298 comptes).

![Sélectionnez le package de localisation fiscale.](../../../_images/select-
fiscal-package.png)

### Configurer les données de base

#### Identifiants de facturation électronique

##### Environnement

L’infrastructure AFIP est répliquée dans deux environnements distincts,
**test** et **production**.

L’environnement de test permet aux entreprises de tester leurs bases de
données jusqu’à ce qu’elles sont prêtes à passer à un environnement de
**production**. Puisque ces deux environnements sont totalement isolés l’un de
l’autre, les certificats numériques d’une instance ne sont pas valides dans
l’autre.

Pour sélectionner un environnement de la base de données, allez à Comptabilité
‣ Paramètres ‣ Localisation argentine et choisissez Prueba (Test) ou
Producción (Production).

![Sélectionnez un environnement de base de données AFIP : Test ou
Production.](../../../_images/select-environment.png)

##### Certificats AFIP

La facturation électronique et les autres services AFIP fonctionnent avec des
Web Services (WS) fournis par l’AFIP.

Afin de permettre la communication avec l’AFIP, la première étape consiste à
demander un Certificat numérique si vous n’en avez pas encore un.

  1. Générer une demande de signature de certificat (Odoo). Lorsque cette option est sélectionnée, un fichier avec l’extension `.csr` (demande de signature de certificat) est généré et vous permet de demander le certificat dans le portail AFIP.

![Demandez un certificat.](../../../_images/request-certificate.png)

  2. Générer un certificat (AFIP). Accédez au portail AFIP et suivez les instructions fournies dans [ce document](https://drive.google.com/file/d/17OKX2lNWd1bjUt3NxfqcCKBkBh-Xlpo-/view) pour obtenir un certificat.

  3. Charger un certificat et une clé privée (Odoo). Une fois que le certificat est généré, chargez-le dans Odoo à l’aide de l’icône Crayon à côté du champ Certificat et sélectionnez le fichier correspondant.

![Chargez le certificat et la clé privée.](../../../_images/upload-
certificate-private-key.png)

Astuce

Si vous avez besoin de configurer le Certificat d’homologation, consultez la
documentation officielle de l’AFIP : [Certificat
d’homologation](http://www.afip.gob.ar/ws/documentacion/certificados.asp). De
plus, Odoo permet à l’utilisateur de tester la facturation électronique
localement sans Certificat d’homologation. Le message suivant s’affiche dans
le chatter pendant les tests en local :

![Facture validée en local parce que vous êtes dans un environnement de test
sans certificat/clés de test.](../../../_images/local-testing.png)

#### Partenaire

##### Type d’identification et TVA

Dans le cadre de la localisation argentine, les types de document définis par
l’AFIP sont désormais disponibles dans le **formulaire partenaire**. Cette
information est indispensable pour la plupart des transactions. Six Types
d’identification sont disponibles par défaut, ainsi que 32 types désactivés.

![Une liste des types de document de la localisation argentine dans Odoo, tels
que définis par l'AFIP.](../../../_images/identification-types.png)

Note

La liste complète des Types d’identification définis par l’AFIP est incluse
dans Odoo, mais seuls les plus courants sont activés.

##### Type de responsabilité AFIP

En Argentine, le type de document et les transactions avec les clients et les
fournisseurs sont définis en fonction du type de responsabilité AFIP. Ce champ
doit être défini dans le **Formulaire partenaire**.

![Sélectionnez le type de responsabilité AFIP.](../../../_images/select-afip-
responsibility-type.png)

#### Taxes

Dans le cadre du module de localisation, les taxes sont créées
automatiquement, ainsi que leur compte financier et leur configuration, par
ex. 73 taxes pour Responsable Inscripto.

![Une liste des taxes de la localisation argentine, ainsi que le montant
financier et la configuration dans Odoo.](../../../_images/automatic-tax-
configuration.png)

##### Types de taxes

L’Argentine possède plusieurs types de taxes, les plus courantes sont :

  * TVA : il s’agit de la TVA normale, qui peut avoir différents pourcentages ;

  * Perception : paiement anticipé d’une taxe appliquée aux factures clients ;

  * Retention : paiement anticipé d’une taxe appliquée aux paiements.

##### Taxes spéciales

Certaines taxes argentines ne s’appliquent pas à toutes les entreprises et ces
options moins courantes sont désactivées dans Odoo par défaut. Avant de créer
une nouvelle taxe, vérifiez d’abord si cette taxe n’est pas désactivée.

![Une liste affichant les options de taxes argentines moins courantes qui sont
désactivées dans Odoo par défaut.](../../../_images/special-inactive-
taxes.png)

#### Types de document

Dans certains pays de l’Amérique latine, y compris l’Argentine, certaines
transactions comptables telles que les factures clients et les factures
fournisseurs sont classées par types de document définis par les autorités
fiscales publiques. En Argentine, l”[AFIP](https://www.afip.gob.ar/) est
l’autorité publique chargée de définir de telles transactions.

Le type de document est une information essentielle qui doit clairement
figurer sur les rapports imprimés, les factures clients et les pièces
comptables répertoriant les écritures.

Chaque type de document peut avoir une séquence unique par journal auquel il
est assigné. Dans le cadre de la localisation, le type de document comprend le
pays dans lequel le document est applicable (ces données sont créées
automatiquement lors de l’installation du module de localisation).

Les informations requises pour les Types de document sont complétées par
défaut, de sorte que l’utilisateur n’a rien à remplir dans cette vue :

![Une liste des types de documents dans Odoo.](../../../_images/default-
document-type-info.png)

Note

Plusieurs types de documents sont désactivés par défaut, mais peuvent être
activés si nécessaire.

##### Lettres

Pour l’Argentine, les Types de documents comprennent une lettre qui permet
d’indiquer le type de transaction ou d’opération. Par exemple, lorsqu’une
facture client est liée à :

  * une transaction B2B, un document de type A doit être utilisé ;

  * une transaction B2C, un document de type B doit être utilisé ;

  * une transaction d’exportation, un document de type E doit être utilisé.

Les documents inclus dans la localisation ont déjà la lettre appropriée
associée à chaque Type de document, il n’est donc pas nécessaire de procéder à
une configuration supplémentaire.

![Les types de documents regroupés par lettre.](../../../_images/document-
types-grouped-by-letters.png)

##### Utilisation sur les factures

Le Type de document sur chaque transaction est déterminé par :

  * La pièce comptable liée à la facture (si le journal utilise des documents) ;

  * Les conditions appliquées en fonction du type d’expéditeur et de destinataire (par ex. le type de régime fiscal de l’acheteur et le type de régime fiscal du vendeur).

### Journaux

Dans la localisation argentine, le journal peut avoir une approche différente
en fonction de son utilisation et de son type interne. Pour configurer des
journaux, allez à Comptabilité ‣ Configuration ‣ Journaux.

Pour les journaux de ventes et d’achats, il est possible d’activer l’option
Utiliser des documents, qui permet d’activer une liste de types de documents
associés aux factures clients et fournisseurs. Pour plus de détails sur les
factures, consultez la section 2.3 types de document.

Si les journaux de ventes ou d’achats n’ont pas l’option Utiliser des
documents activée, ils ne pourront pas créer de factures fiscales, ce qui
signifie que leur utilisation sera principalement limitée au suivi des
mouvements de comptes liés aux processus de contrôle interne.

#### Informations AFIP (ou Point de Vente AFIP)

Le Système PdV AFIP est uniquement visible dans les journaux de **Ventes** et
définit le type de PdV AFIP qui sera utilisé pour gérer les transactions pour
lesquelles le journal est créé.

Le PdV AFIP définit :

  1. les séquences des types de documents liés au service web ;

  2. la structure et les données du fichier de factures électroniques.

![Le champ Système PdV AFIP disponible dans les journaux de ventes dans
Odoo.](../../../_images/sales-journal.png)

##### Services web

Les **Services web** permettent de générer des factures à différentes fins.
Voici quelques options :

  * wsfev1 : Facture électronique : c’est le service le plus courant et est utilisé pour générer des factures pour les types de documents A, B, C, M sans détail par poste ;

  * wsbfev1 : Bon fiscal électronique : pour ceux qui facturent des biens d’équipement et qui souhaitent bénéficier des bons fiscaux électroniques accordés par le ministère de l’Économie. Pour plus d’informations, consultez [Bon fiscal](https://www.argentina.gob.ar/acceder-un-bono-por-fabricar-bienes-de-capital) ;

  * wsfexv1 : Facture d’exportation électronique : permet de générer des factures pour les clients internationaux ou les transactions qui impliquent des processus d’exportation, le type de document associé est le type « E ».

![Services web.](../../../_images/web-services.png)

Voici quelques champs utiles à connaître lorsque l’on travaille avec des
services web :

  * Numéro PdV AFIP : le numéro configuré dans l’AFIP pour identifier les opérations liées à ce PdV AFIP ;

  * Adresse PdV AFIP : le champ lié à l’adresse commerciale enregistrée pour le PdV, qui est généralement la même adresse que celle de la société. Par exemple, si une entreprise possède plusieurs boutiques (localisations fiscales), l’AFIP demandera que l’entreprise ait un PdV AFIP par site. Ce lieu figurera sur le rapport de facturation ;

  * Livre unifié : lorsque le système PdV AFIP est « Preimpresa », les types de documents (applicables au journal) portant la même lettre partageront la même séquence. Par exemple :

    * Facture : FA-A 0001-00000002 ;

    * Avoir : NC-A 0001-00000003 ;

    * Note de débit : ND-A 0001-00000004.

#### Séquences

Sur la première facture, Odoo se synchronise automatiquement avec l’AFIP et
affiche la dernière séquence utilisée.

Note

Lors de la création des Journaux d’achats, vous pouvez définir s’ils sont liés
ou non à des types de documents. Dans le cas où l’option d’utiliser des
documents est sélectionnée, il n’est pas nécessaire d’associer manuellement
les séquences de type de document, puisque le numéro de document est fourni
par le fournisseur.

## Utilisation et tests

### Facture

Les informations suivantes s’appliquent à la création de factures une fois que
les partenaires et les journaux sont créés et correctement configurés.

#### Attribution du type de document

Lorsque le partenaire est sélectionné, le champ Type de document est
automatiquement complété en fonction du type de document AFIP :

  * **Facture pour un client IVA Responsable Inscripto, préfixe A** est le type de document qui indique toutes les taxes et les informations relatives au client en détail.

![Facture pour un client IVA Responsable Inscripto, préfixe
A.](../../../_images/prefix-a-invoice-for-customer.png)

  * **Facture pour un client final, préfixe B** est le type de document qui n’indique pas les taxes, puisque les taxes sont comprises dans le montant total.

![Facture pour un client final, préfixe B.](../../../_images/prefix-b-invoice-
for-end-customer.png)

  * **Facture d’exportation, préfixe E** est le type de document utilisé lors de l’exportation de marchandises et qui indique l’incoterm.

![Facture d'exportation, préfixe E](../../../_images/prefix-e-exporation-
invoice.png)

Même si certaines factures utilisent le même journal, le préfixe et la
séquence sont donnés par le champ Type de document.

Le Type de document le plus courant sera automatiquement défini pour les
différentes combinaisons de type de responsabilité AFIP, mais il peut être mis
à jour manuellement par l’utilisateur avant de confirmer la facture.

#### Éléments de la facture électronique

Si vous utilisez des facture électroniques et toutes les informations sont
correctes, la facture est comptabilisée de manière standard, sauf s’il y a une
erreur. Lorsqu’un message d’erreur s’affiche, il indique le problème et
propose une solution. Si l’erreur subsiste, la facture reste en brouillon
jusqu’à ce que le problème est résolu.

Une fois que la facture est comptabilisée, les informations relatives à la
validation et au statut AFIP s’affichent dans l’onglet AFIP, notamment :

  * Autorisation AFIP : numéro CAE ;

  * Date d’expiration : date limite pour livrer la facture aux clients (normalement 10 jours après la génération du numéro CAE) ;

  * Résultat : indique si la facture a été Aceptado en AFIP (acceptée par l’AFIP) et/ou Aceptado con Observaciones (acceptée avec remarques).

![Statut AFIP.](../../../_images/afip-status.png)

#### Taxes sur les factures

En fonction du Type de responsabilité AFIP, la TVA peut s’appliquer
différemment sur le rapport PDF :

  * A. Hors taxes : dans ce cas, le montant taxé doit être clairement identifié dans le rapport. Cette condition s’applique lorsque le client a le type de responsabilité AFIP : **Responsable Inscripto** ;

![Hors taxes.](../../../_images/tax-amount-excluded.png)

  * B. Taxes comprises : dans ce cas, le montant taxé est inclus dans le prix du produit, le sous-total et les totaux. Cette condition s’applique lorsque le client a les types de responsabilité AFIP suivants :

    * IVA Sujeto Exento ;

    * Consumidor Final ;

    * Responsable Monotributo ;

    * IVA liberado.

![Taxes comprises.](../../../_images/tax-amount-included.png)

#### Cas d’utilisation particuliers

##### Factures pour des services

Pour les factures électroniques qui comprennent des Services, l’AFIP demande
de déclarer la date de début et la date de fin du service. Vous pouvez
compléter cette information dans l’onglet Autres informations.

![Factures pour des services.](../../../_images/invoices-for-services.png)

Si les dates ne sont pas sélectionnées manuellement avant la validation de la
facture, les valeurs seront remplies automatiquement en considérant le premier
et le dernier jour du mois de la facture.

![Dates des services.](../../../_images/service-dates.png)

##### Factures d’exportation

Les factures liées aux Transactions d’exportation exigent que le champ Système
PdV AFIP du journal est défini sur **Preuve exportation - Web Service** pour
que le bon type de document puisse être sélectionné.

![Journal d'exportation.](../../../_images/exporation-journal.png)

Lorsque le client indiqué dans la facture a un type de responsabilité AFIP
défini sur Cliente / Proveedor del Exterior \- Ley N° 19.640, Odoo attribue
automatiquement :

  * le journal lié au service web d’exportation ;

  * le type de document d’exportation ;

  * la position fiscale : Compras/Ventas al exterior ;

  * Concepto AFIP : Produits / Exportation définitive de marchandises ;

  * Exonération d’impôts.

![Champs de la facture d'exportation complétés automatiquement dans
Odoo.](../../../_images/export-invoice.png)

Note

Les documents d’exportation nécessitent l’activation et la configuration des
Incoterms que vous pouvez trouver dans Autres informations ‣ Comptabilité.

![Facture d'exportation - Incoterm.](../../../_images/export-invoice-
incoterm.png)

##### Bon fiscal

Le Bon fiscal électronique est utilisé par les personnes qui facturent des
biens d’équipement et qui souhaitent bénéficier des Bons fiscaux électroniques
accordés par le ministère de l’Économie.

Pour ces transactions, il est important de prendre en considération les
exigences suivantes :

  * Devise (selon le tableau des paramètres) et devis de la facture ;

  * Taxes ;

  * Zone ;

  * Détailler chaque élément ;

    * Code selon la Nomenclature commune du Mercosur (NCM) ;

    * Description complète ;

    * Prix unitaire net ;

    * Quantité ;

    * Unité de mesure ;

    * Bonus ;

    * Taux de TVA.

##### Facture de crédit électronique MiPyMe (FCE)

En ce qui concerne les factures aux PME, il existe plusieurs types de document
classés comme **MiPyME** (micro, pequeñas y medianas empresas), également
connus sous le nom de **Facture de crédit électronique** (ou **FCE - Factura
de Crédito Electrónico** en espagnol). Cette classification développe un
mécanisme qui améliorer les conditions de financement des petites ou moyennes
entreprises et qui leur permet d’augmenter leur productivité, grâce au
recouvrement anticipé des crédits et des créances émises par leurs clients
et/ou fournisseurs.

Pour ces transactions, il est important de prendre en considération les
exigences suivantes :

  * types de documents spécifiques (201, 202, 206, etc) ;

  * l’émetteur doit être éligible par l’AFIP aux transactions MiPyMe ;

  * le montant doit être supérieur à 100.000 ARS ;

  * un compte bancaire de type CBU doit être lié à l’émetteur, sinon la facture ne peut pas être validée. Voici un exemple de message d’erreur :

![Erreur de relation de compte bancaire.](../../../_images/bank-account-
relation-error.png)

Pour configurer le Mode de paiement, allez aux paramètres et sélectionnez SDC
ou ADC.

![Mode de paiement.](../../../_images/transmission-mode.png)

Pour changer le Mode de paiement sur une facture particulière, allez à
l’onglet Autres informations et changez-le avant de confirmer.

Note

Le fait de changer le Mode de paiement ne changera pas le mode défini dans les
Paramètres.

![Mode de paiement sur la facture.](../../../_images/transmission-mode-on-
invoice.png)

Lors de la création d”un avoir ou d’une note de débit lié(e) à un document FCE
:

  * cliquez sur les boutons Avoir et Note de débit, pour que toutes les informations de la facture soient copiées dans l”Avoir et la Note de crédit ;

  * le lettre du document doit être la même que celle du document d’origine (soit A, soit B) ;

  * la même devise que le document d’origine doit être utilisée. Lors de l’utilisation d’une devise secondaire, il y a une différence de change si le taux de change est différent entre le jour de l’émission et la date du paiement. Il est possible de créer un avoir/une note de débit pour diminuer/augmenter le montant à payer en ARS.

![Boutons Avoir & Note de débit.](../../../_images/credit-debit-notes-
button.png)

Lors de la création d’un Avoir, nous avons deux scénarios :

  1. le FCE est rejeté, donc le champ FCE, est Annulation ? sur l”Avoir doit être défini sur _Vrai_ ; ou ;

  2. l”Avoir est créé pour annuler le document FCE. Dans ce cas, le champ FCE, est Annulation ? doit être _vide_ (faux).

![FCE: Es Cancelación?](../../../_images/fce-es-cancelation.png)

#### Rapport imprimé de la facture

Le rapport PDF lié aux factures électroniques qui ont été validées par l’AFIP
comprend un code-barres en bas du format qui représente le numéro CAE. La date
d’expiration s’affiche également comme l’exige la loi.

![Rapport imprimé de la facture.](../../../_images/invoice-printed-report.png)

#### Résolution des problèmes et audit

À des fins de résolution des problèmes et d’audit, il est possible d’obtenir
des informations détaillées sur un numéro de facture qui a été précédemment
envoyé à l’AFIP. Pour récupérer ces informations, activez le [mode
développeur](../../general/developer_mode.html#developer-mode), allez au menu
Comptabilité et cliquez sur le bouton Consulter la facture dans AFIP.

![Consulter la facture dans AFIP.](../../../_images/consult-invoice-in-
afip.png) ![Détails de la facture consultée dans
AFIP.](../../../_images/consult-invoice-in-afip-details.png)

Vous pouvez également récupérer le dernier numéro utilisé dans AFIP pour un
type de document spécifique et un numéro PdV comme référence, afin d’éviter
tout problème lors de la synchronisation des séquences entre Odoo et l’AFIP.

![Consultez le dernier numéro de facture.](../../../_images/consult-last-
invoice-number.png)

### Factures fournisseurs

En fonction du journal d’achats sélectionné sur la facture fournisseur, le
Type de document est désormais un champ obligatoire. Cette valeur est remplie
automatiquement en fonction du type de responsabilité AFIP de l’expéditeur et
du client, mais la valeur peut être modifiée si nécessaire.

![Modifier le journal et le type de document.](../../../_images/changing-
journal-document-type.png)

Le champ Numéro de document doit être complété manuellement et le format est
validé automatiquement. Cependant, si le format n’est pas valide, une erreur
utilisateur s’affiche et indique le format attendu.

![Numéro de document de la facture fournisseur.](../../../_images/vendor-bill-
document-number.png)

Le numéro de la facture fournisseur est structuré de la même manière que les
factures clients, sauf que la séquence du document est saisie par
l’utilisateur dans le format suivant : _Préfixe du document - Lettre - Numéro
du document_.

#### Validez le numéro de la facture fournisseur dans AFIP

Comme la plupart des entreprises ont des contrôles internes pour vérifier que
la facture fournisseur est associée à un document AFIP valide, vous pouvez
configurer une validation automatique dans Comptabilité ‣ Paramètres ‣
Localisation argentine ‣ Valider le document dans AFIP avec les niveaux
suivants :

  * Non disponible : la vérification n’est pas effectuée (c’est la valeur par défaut) ;

  * Disponible : la vérification est effectuée. Si le numéro n’est pas validé, un avertissement s’affiche et la facture fournisseur peut toujours être enregistrée ;

  * Obligatoire : la vérification est effectuée et si le numéro de document n’est pas valide, l’utilisateur ne peut pas enregistrer la facture fournisseur.

![Vérifiez la validité des factures fournisseurs dans
AFIP.](../../../_images/verify-vendor-bills.png)

##### Valider les factures fournisseurs dans Odoo

Lorsque les paramètres de validation du fournisseur sont activés, un bouton
Vérifier dans AFIP s’affiche sur la facture fournisseur dans Odoo à côté du
champ Code d’autorisation AFIP.

![Vérifier dans AFIP.](../../../_images/verify-on-afip.png)

Si la facture fournisseur n’est pas validée dans AFIP, la valeur Rejeté
s’affiche sur le tableau de bord et les détails de l’échec de la validation
sont ajoutés dans le chatter.

![Échec de l'autorisation AFIP.](../../../_images/afip-auth-rejected.png)

#### Cas d’utilisation particuliers

##### Postes exonérés

Certains transactions comprennent des postes qui ne font pas partie du montant
de base de la TVA, tels que la factures de carburant et d’essence.

La facture fournisseur sera enregistrée en utilisant un poste pour chaque
produit qui fait partie du montant de base de la TVA et un poste
supplémentaire pour enregistrer le montant du poste exonéré.

![Exonéré de la TVA.](../../../_images/vat-exempt.png)

##### Taxes de perception

La facture fournisseur est enregistrée en utilisant un poste pour chaque
produit qui fait partie du montant de base de la TVA et la taxe de perception
peut être ajoutée à n’importe quelle ligne de produit. Par conséquent, il y
aura un groupe de taxe pour la TVA et un autre groupe pour la perception. La
valeur par défaut de la perception est toujours 0,10.

Pour modifier la perception TVA et définir le bon montant, vous devez cliquer
sur l’icône Crayon à côté du montant de Perception. Après avoir configuré le
montant de la perception TVA, la facture peut être validée.

![Saisissez le montant de la perception.](../../../_images/enter-perception-
amount.png)

### Gestion des chèques

Pour installer le module de _Gestion des chèques de tiers et des chèques
différés/électroniques_ , allez aux Apps et recherchez le module par son nom
technique `l10n_latam_check` et cliquez sur le bouton Activer.

![Module l10n_latam_check.](../../../_images/l10n-latam-check-module.png)

Ce module permet de configurer les journaux et les paiements pour :

  * Créer, gérer et contrôler vos différents types de chèques

  * Optimiser la gestion des **chèques propres** et des **chèques de tiers**

  * Disposer d’un moyen simple et efficace pour gérer les dates d’expiration de vos propres chèques et des chèques de tiers

Une fois toutes les configurations effectuées pour le flux des factures
électroniques argentines, il est également nécessaire de compléter certaines
configurations pour les flux des chèques propres et des chèques de tiers.

#### Chèques propres

Configurez le journal de banque utilisé pour créer vos propres chèques en
allant à Comptabilité ‣ Configuration ‣ Journaux, en sélectionnant le journal
de banque et en ouvrant l’onglet Paiements sortants.

  * Les Chèques doivent être disponibles comme Mode de paiement. Si ce n’est pas le cas, cliquez sur Ajouter une ligne et saisissez `Chèques` sous Mode de paiement pour les ajouter.

  * Activez le paramètre Utiliser les chèques différés et électroniques.

Note

La dernière configuration **désactive** la possibilité d’imprimer les chèques,
mais permet de :

  * Saisir manuellement les numéros de chèque

  * Ajouter un champ pour attribuer la date de paiement du chèque

![Configurations du journal de banque.](../../../_images/bank-journal-
conf.png)

##### Gestion des chèques propres

Les chèques propres peuvent être créés directement à partir de la facture
fournisseur. Pour ce faire, cliquez sur le bouton Enregistrer un paiement.

Dans la fenêtre modale d’enregistrement du paiement, sélectionnez le journal
de banque à partir duquel le paiement doit être effectué et indiquez la Date
d’encaissement du chèque et le Montant.

![Fenêtre contextuelle de paiement avec les options de chèques propres
activées.](../../../_images/payment-popup-vendorbill.png)

Note

Pour gérer les chèques du jour, le champ Date d’encaissement du chèque doit
être laissé vide ou rempli avec la date du jour. Pour gérer les chèques
différés, la Date d’encaissement du chèque doit être fixée dans le futur.

Pour gérer vos propres chèques existants, allez à Comptabilité ‣ Fournisseurs
‣ Chèques propres. Cette fenêtre affiche des informations essentielles telles
que les dates auxquelles les chèques doivent être payés, la quantité totale de
chèques et le montant total payé en chèques.

![Emplacement du menu Chèques propres](../../../_images/checks-menu-
vendorbill.png)

Il est important de noter que la liste est préfiltrée par les chèques qui
n’ont **pas** encore été **lettrés** avec un relevé bancaire - qui n’ont pas
encore été débités de la banque - ce qui peut être vérifié dans le champ Est
lettré avec un relevé bancaire. Si vous voulez voir tous vos propres chèques,
supprimez le filtre Aucun rapprochement bancaire en cliquant sur le symbôle X.

![Organisation et filtrage du menu des Chèques
propres](../../../_images/check-menu-list-vendorbill.png)

##### Annuler un chèque propre

Pour annuler un chèque propre créé dans Odoo, allez à Comptabilité ‣
Fournisseurs ‣ Chèques propres et sélectionnez le chèque à annuler, puis
cliquez sur le bouton Annuler le chèque. Cette opération interrompt le
lettrage avec les factures fournisseurs et les relevés bancaires et laisse le
chèque dans un statut **annulé**.

![Bouton Cheque vacío pour annuler les chèques
propres](../../../_images/empty-check-button.png)

#### Chèques de tiers

Afin d’enregistrer les paiements effectués par chèques de tiers, vous devez
configurer deux journaux spécifiques. Pour ce faire, allez à Comptabilité ‣
Configuration ‣ Journaux et créez deux nouveaux journaux :

  * `Chèques de tiers`

  * `Chèques de tiers rejetés`

Note

Vous pouvez créer manuellement d’autres journaux si vous avez plusieurs points
de vente et que vous avez besoin de journaux pour ceux-ci.

Pour créer le journal _Chèques de tiers_ , cliquez sur le bouton Nouveau et
configurez les éléments suivants :

  * Saisissez `Chèques de tiers` en tant que Nom du journal

  * Sélectionnez Espèces comme Type

  * Dans l’onglet Pièces comptables, définissez Compte d’espèces sur `1.1.1.02.010 Cheques de Terceros`, saisissez le Code court de votre choix et sélectionnez une Devise

![Compte d'espèces automatiquement créé.](../../../_images/auto-cash-
account.png)

Les modes de paiement disponibles sont énumérés dans les onglets _paiements_ :

  * Pour les nouveaux chèques de tiers entrants, allez à l’onglet Paiements entrants ‣ Ajouter une ligne et sélectionnez Nouveaux chèques de tiers. Cette méthode est utilisée pour créer de _nouveaux_ chèques de tiers.

  * Pour les chèques de tiers existants entrants et sortants, allez à l’onglet Paiements entrants ‣ Ajouter une ligne et sélectionnez Chèques de tiers existants. Répétez la même étape pour l’onglet des Paiements sortants. Cette méthode est utilisée pour recevoir et/ou payer des factures fournisseurs à l’aide de chèques déjà _existants_ ainsi que pour les virements internes.

Astuce

Vous pouvez supprimer des modes de paiement préexistants qui apparaissent par
défaut lors de la configuration des journaux de chèques de tiers.

![Modes de paiement automatiquement créés.](../../../_images/auto-payment-
methods.png)

Vous devez également créer et/ou configurer le journal des _Chèques de tiers
rejetés_. Ce journal est utilisé pour gérer les chèques de tiers rejetés et
peut être utilisé pour envoyer les chèques rejetés au moment de l’encaissement
ou lorsqu’ils proviennent de fournisseurs.

Pour créer le journal des _Chèques de tiers rejetés_ , cliquez sur le bouton
Nouveau et configurez les éléments suivants :

  * Saisissez `Chèques de tiers rejetés` en tant que Nom du journal

  * Sélectionnez Espèces comme Type

  * Dans l’onglet Pièces comptables, définissez Compte d’espèces sur `1.1.1.01.002 Chèques de tiers rejetés`, saisissez un Code court de votre choix et sélectionnez une Devise

Utilisez les mêmes modes de paiement que le journal _Chèques de tiers_.

##### Nouveau chèques de tiers

Pour enregistrer un _nouveau_ chèque de tiers pour une facture client, cliquez
sur le bouton Enregistrer le paiement. Dans la fenêtre contextuelle, vous
devez sélectionner Chèques de tiers comme journal pour l’enregistrement du
paiement.

Sélectionnez Nouveaux chèques de tiers en tant que Mode de paiement et
remplissez le Numéro de chèque, la Date de paiement et Chèque bancaire. Vous
pouvez également manuellement ajouter le Numéro de TVA de l’émetteur du
chèque, mais il est automatiquement rempli par le numéro de TVA du client lié
à la facture.

![Fenêtre contextuelle de paiement avec les options de Nouveaux chèques tiers
activées.](../../../_images/third-party-payment-popup.png)

##### Chèques de tiers existants

Pour payer une facture fournisseur avec un chèque _existant_ , cliquez sur le
bouton Enregistrer le paiement. Dans la fenêtre contextuelle, vous devez
sélectionner Chèques de tiers comme journal pour l’enregistrement du paiement.

Sélectionnez Chèques de tiers existants comme Mode de paiement, et
sélectionnez un chèque dans le champ Chèque. Ce champ affiche **tous les
chèques existants disponibles* à utiliser pour le paiement des factures
fournisseurs.

![Fenêtre contextuelle de paiement avec les options de Chèques de tiers
existants activées.](../../../_images/existing-third-party-popup.png)

Lorsque vous utilisez un **chèque de tiers existant** , vous pouvez revoir les
opérations liées à celui-ci. Par exemple, vous pouvez voir si un chèque de
tiers utilisé pour payer une facture client a été utilisé ultérieurement comme
chèque de tiers existant pour payer une facture fournisseur.

Pour ce faire, allez à Comptabilité ‣ Clients ‣ Chèques de tiers ou
Comptabilité ‣ Fournisseurs ‣ Chèques propres selon le cas et cliquez sur un
chèque. Dans le champ Journal du chèque en cours, cliquez sur => Opérations du
chèque pour afficher l’historique et les mouvements du chèque.

![Menu des opérations du chèque.](../../../_images/check-operations-
menulist.png)

Le menu affiche également des informations essentielles liées à ces
opérations, telles que :

  * Le Type de paiement, qui permet de déterminer s’il s’agit d’un paiement _envoyé_ à un fournisseur ou un paiement _reçu_ d’un client

  * Le Journal dans lequel le chèque est actuellement enregistré

  * Le **partenaire** associé à l’opération (client ou fournisseur).

## Rapports

Dans le cadre de la localisation, les rapports financiers de l’Argentine ont
été ajoutés au tableau de bord de Comptabilité. Accédez à ces rapports en
allant à Comptabilité ‣ Analyse ‣ Rapports argentins.

![Rapports argentins.](../../../_images/argentinian-reports.png)

### Rapports TVA

#### Livre des ventes TVA

Ce rapport enregistre toutes les ventes qui servent de base à la comptabilité
pour déterminer la TVA (débiteur fiscal).

Le livre des Ventes TVA peut être exporté dans un fichier `.zip`. Cliquez sur
le bouton LIVRE TVA (ZIP) dans le coin supérieur gauche, qui contient les
fichiers `.txt` que vous pouvez charger sur le portail AFIP.

![Livre des ventes TVA.](../../../_images/sales-vat-book.png)

#### Livre des achats TVA

Le livre des Achats TVA peut être exporté dans un fichier `.zip` : cliquez sur
le bouton LIVRE TVA (ZIP) dans le coin supérieur gauche, qui contient des
fichiers `.txt` que vous pouvez charger sur le portail AFIP.

![Livre des achats TVA.](../../../_images/purchases-vat-book.png)

#### Récapitulatif TVA

Tableau croisé dynamique conçu pour vérifier les totaux de TVA du mois. Ce
rapport s’utilise en interne et n’est pas envoyé à l’AFIP.

![Récapitulatif TVA.](../../../_images/vat-summary.png)

### IIBB (Impôt sur le revenu brut) - Rapports

#### IIBB (Impôt sur le revenu brut) - Ventes par province

Tableau croisé dynamique dans lequel vous pouvez valider le revenu brut dans
chaque province. Affidavit pour les taxes correspondantes à payer, il n’est
donc pas envoyé à l’AFIP.

![IIBB Ventes par province](../../../_images/iibb-sales-jurisdiction.png)

#### IIBB (Impôt sur le revenu brut) - Ventes par province

Tableau croisé dynamique dans lequel vous pouvez valider les achats bruts dans
chaque province. Affidavit pour les taxes correspondantes à payer, il n’est
donc pas envoyé à l’AFIP.

![IIBB Achats par province.](../../../_images/iibb-purchases-jurisdiction.png)

  *[AFIP]: Administración Federal de Ingresos Públicos

