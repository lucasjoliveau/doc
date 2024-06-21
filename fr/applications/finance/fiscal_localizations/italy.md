# Italie

## Configuration

[Installez](../../general/apps_modules#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation italienne
:

Nom | Nom technique | Description  
---|---|---  
Italie - Comptabilité | `l10n_it` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut  
Italie - Facturation électronique | `l10n_it_edi` | Implémentation de la facturation électronique  
Italie - Facturation électronique | `l10n_it_edi_withholding` | Retenue sur facture électronique  
Italie - Rapports comptables | `l10n_it_reports` | Rapports nationaux  
Italy - Stock DDT | `l10n_it_stock_ddt` | Documents de transport - Documento di Trasporto (DDT)  
![Modules de la localisation italienne](../../../_images/italy-modules.png)

### Informations relatives à l’entreprise

La configuration des informations relatives à l’entreprise vous permet de
correctement configurer la base de données de la comptabilité. Pour ajouter
des informations, allez aux Paramètres ‣ Paramètres généraux et dans la
section **Sociétés** , cliquez sur **Mettre à jour les informations**.
Complétez alors les champs suivants :

  * **Adresse** : l’adresse de la société ;

  * **TVA** : le numéro de TVA de la société ;

  * **Codice Fiscale** : le code fiscal de la société ;

  * **Système fiscal** : le système fiscal de la société ;

![Informations à fournir sur la société](../../../_images/italy-company.png)

### Facturation électronique

Le SdI est le système de facturation électronique utilisé en Italie. Il permet
d’envoyer des factures électronique aux clients et de les recevoir. Les
documents doivent être au format XML et officiellement validés par le système
avant d’être livrés.

Pour pouvoir recevoir des factures et des notifications, le service SdI doit
être informé que les fichiers de l’utilisateur doivent être envoyés à **Konvergo ERP**
et traités en son nom. Pour ce faire, vous devez configurer le **Codice
Destinatario** d’Konvergo ERP sur le portail de l”**Agenzia Delle Entrate**.

  1. Allez à <https://ivaservizi.agenziaentrate.gov.it/portale/> et connectez-vous ;

  2. Allez à la section Fatture e Corrispettivi ;

  3. Définissez l’utilisateur comme Partie légale pour le numéro de TVA dont vous souhaitez configurer l’adresse électronique ;

  4. Dans Servizi Disponibili ‣ Fatturazione Elettronica ‣ Registrazione dell’indirizzo telematico dove ricevere tutte le fatture elettroniche, saisissez le **Codice Destinatario** d’Konvergo ERP `K95IV18` et confirmez.

#### Échange de données informatisé (EDI)

Konvergo ERP utilise le format EDI **FatturaPA** pour la localisation italienne, qui
est activé sur les journaux par défaut lors de l’installation. Lorsque
l”**autorisation de traitement des fichiers** a été accordée, toutes les
**factures clients** et **factures fournisseurs** sont envoyées
automatiquement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez <a href="../accounting/customer_invoices/electronic_invoicing#e-invoicing-configuration"><span class="std std-ref">activer la facturation électronique pour d’autres journaux de ventes et d’achats</span></a> que ceux par défaut.</p>
</div>

Vous pouvez vérifier le statut actuel d’une facture dans le champ
**Facturation électronique**. Le fichier XML se trouve dans le **chatter** de
la facture.

![Statut de la facturation électronique \(en attente de
confirmation\)](../../../_images/italy-test.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/customer_invoices/electronic_invoicing">Facturation électronique (EDI)</a></p>
</div>

### Autorisation de traitement des fichiers (Konvergo ERP)

Puisque les fichiers sont transmis par le serveur d’Konvergo ERP avant d’être envoyés
au service SdI ou reçus par votre base de données, vous devez autoriser Konvergo ERP à
traiter vos fichiers à partir de votre base de données. Pour ce faire, allez à
Comptabilité ‣ Configuration ‣ Paramètres ‣ Facturation électronique.

**Trois** modes sont disponibles :

**Démo**

    

Ce mode simule un environnement dans lequel les factures sont envoyées au
gouvernement. Dans ce mode, les factures doivent être téléchargées
_manuellement_ au format XML et chargées sur le site web de l”**Agenzia delle
Entrate**.

**Test (expérimental)**

    

Ce mode envoie des factures à un service de non-production (c’est-à-dire, de
test) mis à disposition par l”**Agenzia delle Entrate**. L’enregistrement de
cette modification permet à toutes les sociétés de la base de données
d’utiliser cette configuration.

**Officiel**

    

Il s’agit d’un mode de production qui envoie vos factures directement à
l”**Agenzia delle Entrate**.

Une fois que vous avez sélectionnez un mode, vous devez accepter les
**conditions générales** en cochant **Autoriser Konvergo ERP à traiter les factures**
, et puis en cliquant sur **Enregistrer**. Vous pouvez désormais enregistrer
vos transactions dans Konvergo ERP Comptabilité.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>La sélection du mode <b>Test (expérimental)</b> ou <b>Officiel</b> est <b>irréversible</b>. Une fois en mode <b>Officiel</b>, il n’est plus possible de sélectionner les modes <b>Test (expérimental)</b> ou <b>Démo</b> et il en va de même pour le mode <b>Test (expérimental)</b>. Nous recommandons de créer une base de données séparée pour les tests uniquement.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>En mode <b>Test (Expérimental)</b>, toutes les factures envoyées <em>doivent</em> avoir un partenaire qui utilise l’un des des faux <b>Codice Destinatario</b> fournis par l”<b>Agenzia Delle Entrate</b> : <code>0803HR0</code> - <code>N8MIMM9</code> - <code>X9XX79Z</code>. Tout <b>Codice Destinario</b> de production réel de vos clients ne sera pas reconnu comme étant valide lors des tests.</p>
</div> ![Les options de la facturation
électronique en Italie](../../../_images/italy-edi.png)

## Configuration des taxes

De nombreuses fonctionnalités de facturation électronique sont mises en œuvre
en utilisant le système fiscal d’Konvergo ERP. Il est donc très important que les
taxes sont correctement configurées afin de générer des factures correctement
et de gérer d’autres cas d’utilisation de facturation. Par exemple, des
configurations spécifiques sont requises pour le type de taxes
d”**autoliquidation**. Dans le cadre d’une **autoliquidation** , le vendeur ne
facture _pas_ la TVA au client, mais le client paie la TVA _lui-même_ à son
gouvernement. Il existe **deux** types principaux :

  * autoliquidation externe;

  * autoliquidation interne.

### Autoliquidation externe

#### Factures clients

Pour établir une facture d’exportation, assurez-vous que toutes les lignes de
la facture utilisent une taxe d”**autoliquidation**. La localisation
**italienne** contient un **exemple** d’une autoliquidation pour l’exportation
au sein de l’UE à utiliser comme référence (`0% UE`, libellé de facture
`00eu`), qui peut être trouvé dans Comptabilité ‣ Configuration ‣ Taxes. Les
exportations sont exonérées de la TVA et, par conséquent, les taxes
d”**autoliquidation** exigent que la case **Exonération de la taxe (Italie)**
soit cochée et que le type d”**Exonération** et la **Référence de la loi**
soient complétés.

![Paramètres de l'autoliquidation externe](../../../_images/italy-tax.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous devez utiliser un autre type d”<b>Exonération</b>, cliquez sur Action ‣ Dupliquer dans le menu de taxe pour créer une copie d’une taxe similaire existante. Sélectionnez ensuite une autre <b>Exonération</b> et cliquez sur <b>Enregistrer</b>. Répétez ce processus autant de fois que nécessaire pour les différents types d”<b>Exonération</b>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p><b>Renommez</b> vos taxes dans le champ <b>Nom</b> en fonction de leur <b>Exonération</b> pour les identifier facilement.</p>
</div>

Sur votre facture, sélectionnez la taxe correspondante dans le champ
**Taxes**. Vous pouvez trouver les **informations supplémentaires** suivantes
en ouvrant le fichier **XML** de la facture émise :

  * **Adresse SdI (Codice Destinatario)** : doit être complétée pour les pays **UE** et les pays **non UE** ;

  * **ID pays** : doit contenir le pays du fournisseur étranger dans le code ISO (Alpha-2) à deux lettres (par ex. `IT` pour “Italie”) ;

  * **CAP** : doit être complété par `00000` ;

  * **Partita Iva** (**numéro de TVA**) : doit contenir le numéro de **TVA** des **entreprises européennes** et `OO99999999999` (double **lettre** “O”, pas “zéro”) pour les **entreprises non européennes**. Dans le cas de clients particuliers sans numéro de **TVA** , utilisez `0000000` ;

  * **Code fiscal** : pour les entités étrangères qui n’ont pas de **Codice Fiscale** , tout identifiant reconnaissable est valide.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP ne prend pas en charge l’envoi des fichiers XML modifiés par l’utilisateur.</p>
</div>

Pour les **factures** , plusieurs configurations sont techniquement
identifiées par un code **Tipo Documento** :

  * `TD02` \- Acomptes ;

  * `TDO7` \- Facture simplifiée ;

  * `TD08` \- Avoir simplifié ;

  * `TD09` \- Note de débit simplifiée ;

  * `TD24` \- Facture différée.

`TD02``TD07`, `TD08`, and `TD09``TD24`

> Acomptes.
>
> Les factures d”**acompte** sont importées/exportées avec un code **Tipo
> Documento** `TDO2` différent de celui des factures normales. Lors de
> l’importation de la facture, une facture fournisseur normale est créée.
>
> Konvergo ERP exporte les écritures en tant que `TD02` si les conditions suivantes
> sont réunies :

  * Est une facture ;

  * Toutes les lignes de la facture concernent des **lignes de commande** dont l’indicateur `is_downpayment` est `Vrai`.

Factures, avoirs et notes de débit simplifiés

Les factures et les avoirs simplifiés peuvent être utilisés pour certifier les
**transactions nationales** inférieures à **400 €** (hors TVA). Leur statut
est le même que celui d’une facture normale, mais les exigences en matière
d’information sont moindres.

Pour qu’une facture **simplifiée** soit établie, elle doit inclure :

  * Référence de la **facture client** : séquence de numérotation **unique** **sans écarts** ;

  * **Date de facturation** : **date** d’émission de la facture ;

  * **Informations relatives à la société** : les coordonnées complètes du **vendeur** (numéro TVA/TIN, nom, adresse complète) dans Paramètres généraux ‣ Sociétés (section) ;

  * **TVA** : le numéro TVA/TIN de l”**acheteur** (sur leur profil) ;

  * **Total** : le **montant** total (TVA comprise) de la facture.

Dans l”EDI, Konvergo ERP exporte les factures en format simplifié si :

  * Il s’agit d’une transaction **nationale** (c’est-à-dire, le partenaire se situe en Italie) ;

  * Les données de l’acheteur sont **insuffisantes** pour une facture normale ;

  * Les **champs requis** pour une facture normale (adresse, code postal, ville, pays) sont fournis ;

  * Le montant total toutes taxes comprises est **inférieur** à **400 €**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le seuil de 400€ a été défini dans <a href="https://www.gazzettaufficiale.it/eli/id/2019/05/24/19A03271/sg">le décret du 10 mai 2019 publié dans la Gazzetta Ufficiale</a>. Nous vous recommandons de vérifier le montant officiel actuel.</p>
</div>

Factures différées.

La **facture différée** est une facture qui est **émise à un moment
ultérieur** à la vente de marchandises ou à la fourniture de services. Une
**facture différée** doit être émise au plus tard le **15ème jour** du mois
suivant la livraison ciblée par le document.

Il s’agit généralement d’une **facture récapitulative** contenant une liste
des ventes de marchandises ou de services effectuées au cours du mois.
L’entreprise peut **regrouper** les ventes dans **une seule facture** ,
généralement émise à la **fin du mois** à des fins comptables. Les factures
différées sont utilisées par défaut pour les **grossistes** qui ont des
clients récurrents.

Si les marchandises sont transportées par un **transporteur** , chaque
livraison est accompagnée d’un **Documento di Transporto (DDT)** ou **Document
de transport**. La facture différée **doit** indiquer les détails de toutes
les informations du **DDT** pour une meilleure traçabilité.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La facturation électronique des factures différées nécessite le <a href="#italy-modules"><span class="std std-ref">module</span></a> <code>l10n_it_stock_ddt</code>. Dans ce cas, un <b>Tipo Documento</b> <code>TD24</code> dédié est utilisé dans la facturation électronique.</p>
</div>

Konvergo ERP exporte les écritures en tant que `TD24` si les conditions suivantes sont
réunies :

  * Est une facture ;

  * Est associé aux livraisons dont les **DDT** ont une date **différente** de la date d’émission de la facture.

#### Factures fournisseurs

Les entreprises italiennes qui achètent des marchandises ou des services à des
pays membres de l’UE (ou des services des pays non membres de l’UE) doivent
envoyer les informations qui figurent dans la facture fournisseur à
l”**Agenzia delle Entrate**. Cela vous permet de compléter les informations
relatives à la TVA sur votre facture et de l’envoyer. Le vendeur doit être
défini comme **Cedente/Prestatore** et l’acheteur comme
**Cessionario/Committente**. Figurant sur le document **XML** de la facture
fournisseur, les identifiants du fournisseur s’affichent comme
**Cedente/Prestatore** et les identifiants de votre société comme
**Cessionario/Committente**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les factures en auto-facturation ou les intégrations fiscales de factures doivent être émises et envoyées à l’administration fiscale.</p>
</div>

Lorsque vous complétez les taxes sur une facture fournisseur, il est possible
de sélectionner des taxes d”**autoliquidation**. Celles-ci sont
automatiquement activées dans la position fiscale italienne. En allant à
Comptabilité ‣ Configuration ‣ Taxes, les champs d’application de la taxe sur
les **Marchandises** et les **Services** de `10%` et `22%` sont activés et
préconfigurés avec les bonnes grilles fiscales. Celles-ci sont configurées
automatiquement pour assurer l’enregistrement correct des écritures comptables
et l’affichage de la déclaration d’impôt.

Pour les **factures fournisseurs** , **trois** types de configurations sont
techniquement identifiés par un code intitulé **Tipo Documento** :

  * `TD17` \- Acheter des services à des pays **membres de l’UE** et **non membres de l’UE** ;

  * `TD18` \- Acheter des **marchandises** à des pays **membres de l’UE** ;

  * `TD19` \- Acheter des **marchandises** à un fournisseur **étranger** , mais les **marchandises** se trouvent déjà en **Italie** dans un **dépôt TVA**.

`TD17``TD18``TD19`

> Acheter des **services** à des pays **membres de l’UE** et **non membres de
> l’UE** :
>
> Le _vendeur_ étranger facture un service à un prix **hors TVA** , comme il
> n’est pas imposable en Italie. La TVA est payée par l” _acheteur_ en Italie
> ;
>
>   * Dans l’UE : l” _acheteur_ complète les **informations relatives à la
> TVA** due en Italie sur la facture reçue (par ex. **intégration fiscale de
> la facture fournisseur**) ;
>
>   * Non UE : l” _acheteur_ s’envoie lui-même une facture (c’est-à-dire
> **auto-facturation**).
>
>

>
> Konvergo ERP exporte une transaction en tant que `TD17` si les conditions suivantes
> sont réunies :
>
>   * Est une facture fournisseur ;
>
>   * Au moins une taxe sur les lignes de facture cible les grilles fiscales
> VJ ;
>
>   * Toutes les lignes de facture ont des **Services** comme **produits** ou
> une taxe dont le **champ d’application** inclut les **Services**.
>
>

Acheter des **marchandises** à des pays **membres de l’UE** :

Les factures émises au sein de l’UE respectent un **format standard** , donc
une seule intégration de la facture existante est requise.

Konvergo ERP exporte une transaction en tant que `TD18` si les conditions suivantes
sont réunies :

  * Est une facture fournisseur ;

  * Au moins une taxe sur les lignes de facture cible les grilles fiscales VJ ;

  * Toutes les lignes de la facture ont des **produits** **consommables** ou une taxe dont le **champ d’application** inclut les **Marchandises**.

Acheter des **marchandises** à un fournisseur **étranger** , mais les
**marchandises** se trouvent déjà en **Italie** dans un **dépôt TVA** :

  * De l’UE : l” _acheteur_ complète les **informations relatives à la TVA** due en Italie sur la facture reçue (par ex. **Intégration fiscale de la facture fournisseur**) ;

  * Non UE : l” _acheteur_ s’envoie _lui-même_ une facture (c’est-à-dire **auto-facturation**).

Konvergo ERP exporte une écriture en tant que `TD19` si les conditions suivantes sont
réunies :

  * Est une facture fournisseur ;

  * Au moins une taxe sur les lignes de facture cible la grille fiscale VJ3 ;

  * Toutes les lignes de la facture sont des produits **consommables** ou une taxe dont le champ d’application inclut des **marchandises**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/customer_invoices/electronic_invoicing">Facturation électronique (EDI)</a></p>
</div>0

### Autoliquidation interne

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/customer_invoices/electronic_invoicing">Facturation électronique (EDI)</a></p>
</div>1

### Grilles fiscales d’autoliquidation

La localisation italienne a une section **grille fiscale** spécifique pour les
taxes d”**autoliquidation**. Ces grilles fiscales peuvent être identifiées
grâce à l’étiquette VJ et se trouvent dans Comptabilité ‣ Analyse ‣ Rapports
d’audit : Déclaration de TVA.

![Grilles fiscales d'autoliquidation en Italie](../../../_images/italy-
grids.png)

## Saint-Marin

### Factures clients

Saint-Marin et l’Italie ont conclu des accords spéciaux relatifs aux
opérations de facturation électronique. Les **factures** suivent donc les
règles d”**autoliquidation** habituelles. Des exigences supplémentaires ne
sont pas appliquées par Konvergo ERP. Cependant, l’utilisateur est invité par
l”**État** à :

  * Sélectionner une taxe avec l’option **Est exonéré de la taxe (Italie)** cochée et l”**Exonération** définie sur `N3.3` ;

  * Utiliser le **Codice Destinatario** générique du SdI `2R4GT08`. La facture est ensuite envoyée par une agence spécialisée à Saint-Marin à l’entreprise concernée.

### Factures fournisseurs

Lorsqu’une entreprise italienne reçoit une **facture papier** du Saint-Marin,
elle **doit** soumettre cette facture à l”**Agenzia delle Entrate** en
indiquant la valeur spéciale `TD28` dans le champ **Tipo Documento** de la
facture électronique.

`TD28`

Konvergo ERP exporte une écriture en tant que `TD28` si les conditions suivantes sont
réunies :

  * Est une facture fournisseur ;

  * Au moins une taxe sur les lignes de facture cible les grilles fiscales VJ ;

  * Le **pays** du partenaire est **Saint-Marin**.

## Pubblica amministrazione (B2G)

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/customer_invoices/electronic_invoicing">Facturation électronique (EDI)</a></p>
</div>2

### Signature numérique qualifiée

Pour les factures clients et les factures fournisseurs destinées à la
**Pubblica Amministrazione (B2G)** , une **Signature numérique qualifiée** est
requise pour tous les fichiers envoyés via le SdI. Le fichier **XML** doit
être certifié à l’aide d’un certificat qui est soit :

  * une **carte à puce** ;

  * un **jeton USB** ;

  * un **Hardware Security Module (HSM)**.

### CIG, CUP, DatiOrdineAcquisto

Afin d’assurer la traçabilité effective des paiements par les administrations
publiques, les factures électroniques émises aux administrations publiques
doivent contenir :

  * Le CIG, sauf dans les cas d’exonérations des obligations de traçabilité prévus par la loi n° 136 du 13 août 2010 ;

  * Le CUP, dans le cas de factures relatives aux travaux publics.

Si le fichier **XML** l’exige, l”**Agenzia Delle Entrate** peut _uniquement_
procéder au paiement des factures électroniques lorsque le fichier **XML**
contient un CIG et un CUP. Pour chaque facture électronique, il est
**nécessaire** d’indiquer le CUU, qui représente le code d’identification
unique permettant au SdI de délivrer correctement la facture électronique à
l’agence destinataire.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../accounting/customer_invoices/electronic_invoicing">Facturation électronique (EDI)</a></p>
</div>3

  *[SdI]: Sistema di Interscambio
  *[EDI]: Échange de données informatisé
  *[CIG]: Codice Identificativo Gara
  *[CUP]: Codice Unico di Progetto
  *[CUU]: Codice Univoco Ufficio

