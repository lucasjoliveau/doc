# France

## FEC - Fichier des écritures comptables

Un fichier d’audit FEC Fichier des écritures comptables reprend l’ensemble des
données et écritures comptables enregistrées dans tous les journaux comptables
d’un exercice. Les écritures du fichier doivent être classées par ordre
chronologique.

Depuis le 1er janvier 2014, chaque entreprise française est tenue de générer
et de transmettre ce fichier à la demande de l’administration fiscale à des
fins d’audit.

### Import FEC

Pour faciliter l’intégration de nouveaux utilisateurs, le [package de
localisation fiscale](../fiscal_localizations#fiscal-localizations-
packages) française d’Konvergo ERP Enterprise comprend la fonctionnalité **Import
FEC** (nom du module : `l10n_fr_fec_import`), qui permet d’importer des
fichiers FEC existants à partir d’anciens logiciels.

Pour activer cette fonctionnalité, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Import comptable, activez **Import FEC** et cliquez sur
_Enregistrer_.

Ensuite, allez à Comptabilité ‣ Configuration ‣ Import FEC, chargez votre
fichier FEC et cliquez sur _Importer_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><div class="line-block">
<div class="line">L’importation de fichiers FEC d’un exercice différent ne nécessite aucune action ou calcul particulier.</div>
<div class="line">Si plusieurs fichiers contiennent des « Reports à nouveau » (RAN) avec le solde initial de l’exercice, il se peut que vous deviez annuler ces écritures dans l’interface utilisateur. Konvergo ERP rend ces écritures (RAN) inutiles.</div>
</div>
</div>

#### Formats de fichier

Les fichiers FEC ne peuvent être qu’au format CSV, car le format XML n’est pas
pris en charge.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>

Notre module s’attend à ce que les fichiers répondent aux exigences techniques
suivantes :

  * **Encodage** : UTF-8, UTF-8-SIG et iso8859_15.

  * **Séparateur** : l’un des séparateurs suivants : `;` ou `|` ou `,` ou `TAB`.

  * **Fins de ligne** : les groupes de caractères CR+LF (`\r\n`) et LF (`\n`) sont tous deux pris en charge.

  * **Format de date** : `%Y%m%d`

#### Description et utilisation des champs

# | Nom du champ | Description | Utilisation | Format  
---|---|---|---|---  
01 | JournalCode | Code du journal | `journal.code` et `journal.name` si `JournalLib` n’est pas fourni | Alphanumérique  
02 | JournalLib | Libellé de journal | `journal.name` | Alphanumérique  
03 | EcritureNum | Numérotation propre à chaque numéro de séquence du journal de l’écriture | `move.name` | Alphanumérique  
04 | EcritureDate | Date de l’entrée comptable | `move.date` | Date (aaaaMMjj)  
05 | CompteNum | Numéro de compte | `account.code` | Alphanumérique  
06 | CompteLib | Libellé du compte | `account.name` | Alphanumérique  
07 | CompAuxNum | Numéro du compte secondaire (peut être vide) | `partner.ref` | Alphanumérique  
08 | CompAuxLib | Libellé du compte secondaire (peut être vide) | `partner.name` | Alphanumérique  
09 | PieceRef | Référence du document | `move.ref` et `move.name` si `EcritureNum` n’est pas fourni | Alphanumérique  
10 | PieceDate | Date du document | `move.date` | Date (aaaaMMjj)  
11 | EcritureLib | Libellé de l’écriture comptable | `move_line.name` | Alphanumérique  
12 | Débit | Montant débiteur | `move_line.debit` | Flottant  
13 | Crédit | Montant créditeur (le nom de champ « Crédit » n’est pas autorisé) | `move_line.credit` | Flottant  
14 | EcritureLet | Référence croisée de l’écriture comptable (peut être vide) | `move_line.fec_matching_number` | Alphanumérique  
15 | DateLet | Date de l’écriture comptable (peut être vide) | non utilisé | Date (aaaaMMjj)  
16 | ValidDate | Date de validation de l’écriture comptable | non utilisé | Date (aaaaMMjj)  
17 | Montantdevise | Montant en devise (peut être vide) | `move_line.amount_currency` | Flottant  
18 | Idevise | Identifiant de la devise (peut être vide) | `currency.name` | Alphanumérique  
  
Ces deux champs peuvent être trouvés à la place des autres dans le sens
mentionné ci-dessus.

12 | Montant | Montant | `move_line.debit` ou `move_line.credit` | Flottant  
---|---|---|---|---  
13 | Sens | « C » pour Crédit ou « D » pour Débit | détermine `move_line.debit` ou `move_line.credit` | Caractère  
  
#### Détails de la mise en œuvre

Les entités comptables suivantes sont importées à partir des fichiers FEC :
**Comptes, Journaux, Partenaires** , et **Écritures**.

Notre module détermine l’encodage, le caractère de fin de ligne et le
séparateur utilisés dans le fichier.

Une vérification est ensuite effectuée pour voir si chaque ligne a le bon
nombre de champs en fonction de l’en-tête.

Si la vérification est positive, le fichier est lu dans son intégralité,
conservé en mémoire et analysé. Les entités comptables sont importées par
type, dans l’ordre suivant.

##### Comptes

Chaque écriture comptable est liée à un compte, qui doit être déterminé par le
champ `CompteNum`.

##### Correspondance des codes

Si un code de compte similaire existe déjà dans le système, le code existant
est utilisé au lieu d’en créer un nouveau.

Les comptes dans Konvergo ERP ont généralement un nombre de chiffres qui sont par
défaut pour la localisation fiscale. Puisque le module FEC est lié à la
localisation française, le nombre de chiffres pertinents par défaut est de 6.

Cela signifie que les zéros de fin de code sont coupés à droite et que la
comparaison entre les codes de compte dans le fichier FEC et ceux qui existent
déjà dans Konvergo ERP s’effectue uniquement sur les six premiers chiffres des codes.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Le code de compte <code>65800000</code> dans le fichier est mis en correspondance avec le compte <code>658000</code> existant dans Konvergo ERP et ce compte est utilisé au lieu d’en créer un nouveau.</p>
</div>

##### Indicateur de lettrage

Un compte est techniquement marqué comme “à lettrer” si la première ligne dans
laquelle il apparaît a le champ `EcritureLet` complété, car cet indicateur
signifie que l’écriture comptable sera mise en correspondance avec une autre.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si ce champ de la ligne n’est pas complété, mais l’écriture doit toujours être lettrée avec un paiement qui n’a pas encore été enregistré, ce n’est pas un problème ; le compte est marqué comme compatible dès que l’importation des lignes d’écriture l’exige.</p>
</div>

##### Correspondance entre le type de compte et les modèles

Comme le **type** de compte n’est pas précisé dans le format FEC, les
**nouveaux** comptes sont créés avec le type par défaut _Actif circulant_ et
ensuite, à la fin du processus d’import, ils sont mis en correspondance avec
les modèles de plan comptable installés. L’indicateur de _lettrage_ est
également calculé de cette manière.

La correspondance se fait avec les chiffres les plus à gauche, en commençant
par tous les chiffres, puis 3, puis 2.

<div class="alert alert-success">
<p class="alert-title">
Example</p><table class="table docutils">
<colgroup>
<col style="width: 14%"/>
<col style="width: 14%"/>
<col style="width: 20%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Nom</p></th>
<th class="head"><p>Code</p></th>
<th class="head"><p>Comparaison complète</p></th>
<th class="head"><p>Comparaison à 3 chiffres</p></th>
<th class="head"><p>Comparaison à 2 chiffres</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Modèle</p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400000</code></p></td>
<td><p><code>400</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-odd"><td><p>CompteNum</p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>40100000</code></p></td>
<td><p><code>401</code></p></td>
<td><p><code>40</code></p></td>
</tr>
<tr class="row-even"><td><p><b>Résultat</b></p></td>
<td></td>
<td></td>
<td></td>
<td><p>Correspondance <b>trouvée</b></p></td>
</tr>
</tbody>
</table>
</div>

Le type de compte est ensuite marqué comme _à payer_ et _à lettrer_ selon le
modèle de compte.

##### Journaux

Les journaux sont également comparés à ceux qui existent déjà dans Konvergo ERP pour
éviter des doublons, y compris dans le cas d’imports multiples de fichiers
FEC.

Si un code de journal similaire existe déjà dans le système, le code existant
est utilisé au lieu d’en créer un nouveau.

Les nouveaux journaux se voient attribuer un préfixe `FEC-`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><code>ACHATS</code> -&gt; <code>FEC-ACHATS</code></p>
</div>

Les journaux ne sont _pas_ archivés et l’utilisateur est autorisé à les
traiter comme il le souhaite.

##### Détermination du type de journal

Le type de journal n’est pas non plus précisé dans le format (comme pour les
comptes) et il est donc créé avec le type `général` par défaut.

À la fin du processus d’import, le type est déterminé selon ces règles
concernant les écritures et les comptes liés :

  * `banque` : Les écritures dans ces journaux ont toujours une ligne (débit ou crédit) affectant un compte de liquidité.

`espèces` / `banque` peuvent être interchangés, donc `banque` est défini
partout lorsque cette condition est remplie.

  * `vente` : Les écritures dans ces journaux ont principalement des lignes de débit sur les comptes clients et des lignes de crédit sur les comptes des impôts sur les revenus.

Le débit/crédit est inversé pour les écritures comptables de remboursement de
ventes.

  * `achat` : Les écritures dans ces journaux ont principalement des lignes de crédit sur des comptes fournisseurs et des lignes de débit sur des comptes des charges.

Le débit/crédit est inversé pour les écritures comptables de remboursement
d’achats.

  * `général` : pour tout le reste.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Un minimum de trois écritures est nécessaire pour pouvoir identifier le type de journal.</p></li>
<li><p>Un seuil de 70% des écritures doit correspondre à un critère pour qu’un type de journal soit déterminé.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Disons que nous analysons les écritures qui partagent un certain <code>journal_id</code>.</p>
<table class="table docutils">
<colgroup>
<col style="width: 76%"/>
<col style="width: 9%"/>
<col style="width: 15%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Écritures</p></th>
<th class="head"><p>Nombre</p></th>
<th class="head"><p>Pourcentage</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>qui ont une ligne de compte de vente et pas de ligne de compte d’achat</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
<tr class="row-odd"><td><p>qui ont une ligne de compte d’achat et pas de ligne de compte de vente</p></td>
<td><p>1</p></td>
<td><p>25%</p></td>
</tr>
<tr class="row-even"><td><p>qui ont une ligne de compte de liquidité</p></td>
<td><p>3</p></td>
<td><p><b>75%</b></p></td>
</tr>
<tr class="row-odd"><td><p><b>Total</b></p></td>
<td><p>4</p></td>
<td><p>100%</p></td>
</tr>
</tbody>
</table>
<p>Le <code>type</code> de journal serait <code>banque</code>, parce que le pourcentage des écritures bancaires (75%) dépasse le seuil (70%).</p>
</div>

##### Partenaires

Chaque partenaire conserve sa `Référence` du champ `CompAuxNum`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ces champs sont consultables, conformément aux anciens imports FEC du côté de l’expert comptable à des fins fiscales/d’audit.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les utilisateurs peuvent fusionner des partenaires à l’aide de l’application de nettoyage des données, où les fournisseurs et les clients ou des entrées de partenaires similaires peuvent être fusionnés avec l’utilisateur, avec l’aide du système qui les regroupe par entrées similaires.</p>
</div>

##### Écritures

Les écritures sont immédiatement comptabilisées et lettrées après leur
soumission, en utilisant le champ `EcritureLet` pour effectuer la
correspondance entre les écritures elles-mêmes.

Le champ `EcritureNum` représente le nom des écritures. Nous avons remarqué
qu’il arrive parfois qu’il ne soit pas rempli. Dans ce cas, le champ
`PieceRef` est utilisé.

##### Problèmes d’arrondi

Il existe une tolérance d’arrondi avec une précision liée à la devise sur le
débit et le crédit (par ex. 0.01 pour EUR). En dessous de cette tolérance, une
nouvelle ligne est ajoutée à l’écriture, intitulée _Différence d’arrondi à
l’import_ , ciblant les comptes :

  * `658000` Charges diverses de gestion courante, pour les débits ajoutés

  * `758000` Produits divers de gestion courante, pour les crédits ajoutés

##### Nom d’écriture manquant

Si le champ `EcritureNum` n’est pas complété, il se peut que le champ
`PieceRef` ne permette pas de déterminer le nom de l’écriture (il peut être
utilisé comme référence de la ligne de l’écriture), ce qui ne permet pas de
savoir quelles lignes doivent être regroupées en une seule écriture et empêche
la création d’écritures équilibrées.

Une dernière tentative est faite en regroupant toutes les lignes du même
journal et de la même date (`JournalLib`, `EcritureDate`). Si ce regroupement
génère des écritures équilibrées (somme(crédit) - somme(débit) = 0), chaque
combinaison différente de journal et de date crée une nouvelle écriture.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>0

Si cette tentative échoue, l’utilisateur reçoit un message d’erreur avec
toutes les lignes d’écriture qu sont supposées être déséquilibrées.

##### Informations relatives au partenaire

Si les informations relatives au partenaire sont précisées sur une ligne,
elles sont copiées dans l’écriture comptable elle-même si le Journal ciblé est
de type _créditeur_ ou _débiteur_.

### Export

Si vous avez installé le [package de localisation
fiscale](../fiscal_localizations#fiscal-localizations-packages)
française, vous êtes en mesure de télécharger le FEC. Pour ce faire, allez à
Comptabilité ‣ Analyse ‣ France ‣ FEC.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>1 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>2

## Rapports comptables français

Si vous avez installé la comptabilité française, vous aurez accès à certains
rapports comptables spécifiques à la France :

  * Bilan comptable

  * Compte de résultats

  * Plan de Taxes France

## Se conformer à la législation anti-fraude TVA avec Konvergo ERP

Depuis 1er janvier 2018, une nouvelle législation anti-fraude est en vigueur
en France métropolitaine et dans les DOM-TOM. Cette nouvelle législation
stipule certains critères relatifs à l’inaltérabilité, à la sécurisation, à la
conservation et à l’archivage des données de vente. Ces exigences légales sont
implémentées dans Konvergo ERP, à partir de la version 9, par le biais d’un module et
d’un certificat de conformité à télécharger.

### Mon entreprise est-elle tenue d’utiliser un logiciel anti-fraude ?

Votre entreprise est tenue d’utiliser un logiciel de caisse anti-fraude comme
Konvergo ERP (CGI article 286, I. 3 ° bis) si :

  * Vous êtes assujetti à la TVA (et n’êtes pas concerné par le régime de franchise de la TVA) en France ou dans les DOM-TOM,

  * Certains de vos clients sont des particuliers (B2C).

Cette règle s’applique aux entreprises de toute taille. Les auto-entrepreneurs
sont exemptés de la TVA et ne sont donc pas concernés.

### Se conformer à la législation avec Konvergo ERP

Il est très facile de se conformer à cette nouvelle législation avec Konvergo ERP.

Your company is requested by the tax administration to deliver a certificate
of conformity testifying that your software complies with the anti-fraud
legislation. This certificate is granted by Konvergo ERP SA to Konvergo ERP Enterprise users
[here](https://www.odoo.com/my/contract/french-certification/). If you use
Konvergo ERP Community, you should [upgrade to Konvergo ERP
Enterprise](../../../administration/on_premise/community_to_enterprise)
or contact your Konvergo ERP service provider.

En cas de non-conformité, votre entreprise risque une amende de 7.500 €.

Pour obtenir la certification, suivez les étapes suivantes :

  * Si vous utilisez l’application **Point de Vente** d’Konvergo ERP, [installez](../../general/apps_modules#general-install) le module **France - Certification anti-fraude à la TVA pour Point de Vente (CGI 286 I-3 bis)** en allant aux Apps, supprimant le filtre _Apps_ , recherchant _l10n_fr_pos_cert_ , et en installant le module.

  * Assurez-vous qu’un pays est bien défini sur votre entreprise, sinon vos écritures ne seront pas chiffrées pour le contrôle de l’inaltérabilité. Pour modifier les données de votre société, allez dans Configuration ‣ Utilisateurs & Sociétés ‣ Sociétés. Sélectionnez un pays dans la liste. Ne créez pas un nouveau pays.

  * Téléchargez votre certificat de conformité obligatoire délivré par Konvergo ERP SA [ici](https://www.odoo.com/my/contract/french-certification/).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>3

### Fonctionnalités anti-fraude

Le module anti-fraude introduit les fonctionnalités suivantes :

  * **Inaltérabilité** : désactivation de toutes les méthodes d’annulation ou de modification des données clés des commandes PdV, factures clients et pièces comptables ;

  * **Sécurisation** : algorithme de chaînage pour contrôler l’inaltérabilité ;

  * **Conservation** : clôture automatique des ventes avec calcul des totaux périodiques et cumulatifs (quotidiens, mensuels, annuels).

#### Inaltérabilité

Toutes les possibilités d’annulation ou de modification des données clés des
commandes PdV payées, des factures clients confirmées ou des pièces comptables
sont désactivées, si la société est située en France ou dans les DOM-TOM.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>4

#### Sécurisation

Pour garantir l’inaltérabilité, chaque commande ou pièce comptable est
chiffrée à la validation. Ce numéro (ou hachage) est calculé à partir des
données clés du document et à partir du hachage des documents précédents.

Le module introduit une interface permettant à l’utilisateur de tester
l’inaltérabilité des données. Si une information est modifiée dans un document
après sa validation, le test échouera. L’algorithme recalcule tous les
hachages et les compare avec les hachages initiaux. En cas d’échec, le système
indique le premier document corrompu enregistré dans le système.

Les utilisateurs qui bénéficient de droits d’accès de type _Gestionnaire_
peuvent lancer le contrôle d’inaltérabilité. Pour les commandes PdV, allez au
Point de Vente ‣ Analyse ‣ Relevés français. Pour les factures et écritures
comptables, allez à Facturation/Comptabilité ‣ Analyse ‣ Relevés français.

#### Conservation

Le système traite également des clôtures automatiques des ventes sur une base
quotidienne, mensuelle ou annuelle. Ces clôtures calculent de façon distincte
le total des ventes de la période, ainsi que les grands totaux cumulés depuis
la toute première écriture de vente enregistrée dans le système.

Les clôtures sont accessibles depuis le menu _Relevés français_ des
applications Point de Vente, Facturation et Comptabilité.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>6

### Responsabilités

Ne désinstallez pas le module ! Les hachages seront réinitialisés et aucune de
vos données précédentes ne sera plus garantie comme étant inaltérable.

Les utilisateurs restent responsables de leur instance Konvergo ERP et doivent
l’utiliser avec diligence. Ils ne sont pas autorisés à modifier le code source
qui garantit l’inaltérabilité des données.

Konvergo ERP se décharge de toute responsabilité en cas de modification des
fonctionnalités du module causée par des applications tierces non certifiées
par Konvergo ERP.

### Plus d’informations

Vous trouverez plus d’informations relatives à cette législation dans les
documents officiels suivants.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fichier FEC CSV a un format de texte brut représentant un tableau de données, la première ligne étant un en-tête définissant la liste des champs pour chaque entrée et chaque ligne suivante représentant une entrée comptable, sans ordre prédéterminé.</p>
</div>7

