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
localisation fiscale](../fiscal_localizations.html#fiscal-localizations-
packages) française d’Odoo Enterprise comprend la fonctionnalité **Import
FEC** (nom du module : `l10n_fr_fec_import`), qui permet d’importer des
fichiers FEC existants à partir d’anciens logiciels.

Pour activer cette fonctionnalité, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Import comptable, activez **Import FEC** et cliquez sur
_Enregistrer_.

Ensuite, allez à Comptabilité ‣ Configuration ‣ Import FEC, chargez votre
fichier FEC et cliquez sur _Importer_.

Note

L’importation de fichiers FEC d’un exercice différent ne nécessite aucune
action ou calcul particulier.

Si plusieurs fichiers contiennent des « Reports à nouveau » (RAN) avec le
solde initial de l’exercice, il se peut que vous deviez annuler ces écritures
dans l’interface utilisateur. Odoo rend ces écritures (RAN) inutiles.

#### Formats de fichier

Les fichiers FEC ne peuvent être qu’au format CSV, car le format XML n’est pas
pris en charge.

Note

Le fichier FEC CSV a un format de texte brut représentant un tableau de
données, la première ligne étant un en-tête définissant la liste des champs
pour chaque entrée et chaque ligne suivante représentant une entrée comptable,
sans ordre prédéterminé.

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

Les comptes dans Odoo ont généralement un nombre de chiffres qui sont par
défaut pour la localisation fiscale. Puisque le module FEC est lié à la
localisation française, le nombre de chiffres pertinents par défaut est de 6.

Cela signifie que les zéros de fin de code sont coupés à droite et que la
comparaison entre les codes de compte dans le fichier FEC et ceux qui existent
déjà dans Odoo s’effectue uniquement sur les six premiers chiffres des codes.

Example

Le code de compte `65800000` dans le fichier est mis en correspondance avec le
compte `658000` existant dans Odoo et ce compte est utilisé au lieu d’en créer
un nouveau.

##### Indicateur de lettrage

Un compte est techniquement marqué comme “à lettrer” si la première ligne dans
laquelle il apparaît a le champ `EcritureLet` complété, car cet indicateur
signifie que l’écriture comptable sera mise en correspondance avec une autre.

Note

Si ce champ de la ligne n’est pas complété, mais l’écriture doit toujours être
lettrée avec un paiement qui n’a pas encore été enregistré, ce n’est pas un
problème ; le compte est marqué comme compatible dès que l’importation des
lignes d’écriture l’exige.

##### Correspondance entre le type de compte et les modèles

Comme le **type** de compte n’est pas précisé dans le format FEC, les
**nouveaux** comptes sont créés avec le type par défaut _Actif circulant_ et
ensuite, à la fin du processus d’import, ils sont mis en correspondance avec
les modèles de plan comptable installés. L’indicateur de _lettrage_ est
également calculé de cette manière.

La correspondance se fait avec les chiffres les plus à gauche, en commençant
par tous les chiffres, puis 3, puis 2.

Example

Nom | Code | Comparaison complète | Comparaison à 3 chiffres | Comparaison à 2 chiffres  
---|---|---|---|---  
Modèle | `400000` | `400000` | `400` | `40`  
CompteNum | `40100000` | `40100000` | `401` | `40`  
**Résultat** |  |  |  | Correspondance **trouvée**  
  
Le type de compte est ensuite marqué comme _à payer_ et _à lettrer_ selon le
modèle de compte.

##### Journaux

Les journaux sont également comparés à ceux qui existent déjà dans Odoo pour
éviter des doublons, y compris dans le cas d’imports multiples de fichiers
FEC.

Si un code de journal similaire existe déjà dans le système, le code existant
est utilisé au lieu d’en créer un nouveau.

Les nouveaux journaux se voient attribuer un préfixe `FEC-`.

Example

`ACHATS` -> `FEC-ACHATS`

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

Note

  * Un minimum de trois écritures est nécessaire pour pouvoir identifier le type de journal.

  * Un seuil de 70% des écritures doit correspondre à un critère pour qu’un type de journal soit déterminé.

Example

Disons que nous analysons les écritures qui partagent un certain `journal_id`.

Écritures | Nombre | Pourcentage  
---|---|---  
qui ont une ligne de compte de vente et pas de ligne de compte d’achat | 0 | 0  
qui ont une ligne de compte d’achat et pas de ligne de compte de vente | 1 | 25%  
qui ont une ligne de compte de liquidité | 3 | **75%**  
**Total** | 4 | 100%  
  
Le `type` de journal serait `banque`, parce que le pourcentage des écritures
bancaires (75%) dépasse le seuil (70%).

##### Partenaires

Chaque partenaire conserve sa `Référence` du champ `CompAuxNum`.

Note

Ces champs sont consultables, conformément aux anciens imports FEC du côté de
l’expert comptable à des fins fiscales/d’audit.

Astuce

Les utilisateurs peuvent fusionner des partenaires à l’aide de l’application
de nettoyage des données, où les fournisseurs et les clients ou des entrées de
partenaires similaires peuvent être fusionnés avec l’utilisateur, avec l’aide
du système qui les regroupe par entrées similaires.

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

Example

`ACH` \+ `2021/05/01` –> nouvelle écriture dans le journal `ACH` avec le nom
`20210501`.

Si cette tentative échoue, l’utilisateur reçoit un message d’erreur avec
toutes les lignes d’écriture qu sont supposées être déséquilibrées.

##### Informations relatives au partenaire

Si les informations relatives au partenaire sont précisées sur une ligne,
elles sont copiées dans l’écriture comptable elle-même si le Journal ciblé est
de type _créditeur_ ou _débiteur_.

### Export

Si vous avez installé le [package de localisation
fiscale](../fiscal_localizations.html#fiscal-localizations-packages)
française, vous êtes en mesure de télécharger le FEC. Pour ce faire, allez à
Comptabilité ‣ Analyse ‣ France ‣ FEC.

Astuce

Si vous ne voyez pas le sous-menu **FEC** , allez aux Apps, supprimez le
filtre _Apps_ , puis recherchez le module intitulé **France-FEC** et assurez-
vous qu’il est installé.

Pour plus d'infos

  * [Spécifications techniques officielles (fr)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775)

  * [Test-Compta-Demat (Outil de test officiel des fichiers FEC)](https://github.com/DGFiP/Test-Compta-Demat)

## Rapports comptables français

Si vous avez installé la comptabilité française, vous aurez accès à certains
rapports comptables spécifiques à la France :

  * Bilan comptable

  * Compte de résultats

  * Plan de Taxes France

## Se conformer à la législation anti-fraude TVA avec Odoo

Depuis 1er janvier 2018, une nouvelle législation anti-fraude est en vigueur
en France métropolitaine et dans les DOM-TOM. Cette nouvelle législation
stipule certains critères relatifs à l’inaltérabilité, à la sécurisation, à la
conservation et à l’archivage des données de vente. Ces exigences légales sont
implémentées dans Odoo, à partir de la version 9, par le biais d’un module et
d’un certificat de conformité à télécharger.

### Mon entreprise est-elle tenue d’utiliser un logiciel anti-fraude ?

Votre entreprise est tenue d’utiliser un logiciel de caisse anti-fraude comme
Odoo (CGI article 286, I. 3 ° bis) si :

  * Vous êtes assujetti à la TVA (et n’êtes pas concerné par le régime de franchise de la TVA) en France ou dans les DOM-TOM,

  * Certains de vos clients sont des particuliers (B2C).

Cette règle s’applique aux entreprises de toute taille. Les auto-entrepreneurs
sont exemptés de la TVA et ne sont donc pas concernés.

### Se conformer à la législation avec Odoo

Il est très facile de se conformer à cette nouvelle législation avec Odoo.

Your company is requested by the tax administration to deliver a certificate
of conformity testifying that your software complies with the anti-fraud
legislation. This certificate is granted by Odoo SA to Odoo Enterprise users
[here](https://www.odoo.com/my/contract/french-certification/). If you use
Odoo Community, you should [upgrade to Odoo
Enterprise](../../../administration/on_premise/community_to_enterprise.html)
or contact your Odoo service provider.

En cas de non-conformité, votre entreprise risque une amende de 7.500 €.

Pour obtenir la certification, suivez les étapes suivantes :

  * Si vous utilisez l’application **Point de Vente** d’Odoo, [installez](../../general/apps_modules.html#general-install) le module **France - Certification anti-fraude à la TVA pour Point de Vente (CGI 286 I-3 bis)** en allant aux Apps, supprimant le filtre _Apps_ , recherchant _l10n_fr_pos_cert_ , et en installant le module.

  * Assurez-vous qu’un pays est bien défini sur votre entreprise, sinon vos écritures ne seront pas chiffrées pour le contrôle de l’inaltérabilité. Pour modifier les données de votre société, allez dans Configuration ‣ Utilisateurs & Sociétés ‣ Sociétés. Sélectionnez un pays dans la liste. Ne créez pas un nouveau pays.

  * Téléchargez votre certificat de conformité obligatoire délivré par Odoo SA [ici](https://www.odoo.com/my/contract/french-certification/).

Note

  * Pour installer le module dans n’importe quel système créé avant le 18 décembre 2017, vous devez mettre à jour la liste des modules. Pour ce faire, activez le [mode développeur](../../general/developer_mode.html#developer-mode). Allez ensuite dans le menu _Apps_ et cliquez sur _Mettre à jour la liste des modules_ dans le menu supérieur.

  * Si vous utilisez Odoo hébergé sur vos propres serveurs, vous devez mettre à jour votre installation et redémarrer votre serveur.

  * Si vous avez installé la version initiale du module anti-fraude (avant le 18 décembre 2017), vous devez mettre à jour ce dernier. Le nom initial du module était _France - Comptabilité - Certifié CGI 286 I-3 bis_. Après avoir mis à jour la liste des modules, sélectionnez le nouveau module dans le menu _Apps_ et cliquez sur le bouton _Mettre à niveau_. Enfin, vérifiez que le module _l10n_fr_sale_closing_ est installé.

### Fonctionnalités anti-fraude

Le module anti-fraude introduit les fonctionnalités suivantes :

  * **Inaltérabilité** : désactivation de toutes les méthodes d’annulation ou de modification des données clés des commandes PdV, factures clients et pièces comptables ;

  * **Sécurisation** : algorithme de chaînage pour contrôler l’inaltérabilité ;

  * **Conservation** : clôture automatique des ventes avec calcul des totaux périodiques et cumulatifs (quotidiens, mensuels, annuels).

#### Inaltérabilité

Toutes les possibilités d’annulation ou de modification des données clés des
commandes PdV payées, des factures clients confirmées ou des pièces comptables
sont désactivées, si la société est située en France ou dans les DOM-TOM.

Note

Si vous utilisez un environnement multi-sociétés, seuls les documents des
entreprises françaises ou DOM-TOM sont impactés.

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

Note

  * Les clôtures calculent les totaux des pièces comptables des journaux de ventes (Type de journal = Ventes).

  * Dans les environnements multi-sociétés, ces clôtures sont effectuées par entreprise.

  * Les commandes PdV sont comptabilisées en tant que pièces comptables à la clôture de la session de PdV. Vous pouvez clôturer une session de PdV à tout moment. Pour inciter l’utilisateur à le faire chaque jour, le module empêche de reprendre une session ouverte il y a plus de 24 heures. Une telle session doit être clôturée avant de pouvoir vendre à nouveau.

  * Le total d’une période est calculé à partir de toutes les pièces comptables comptabilisées après la clôture précédente du même type, indépendamment de leur date de comptabilisation. Si vous enregistrez une nouvelle transaction de vente pour une période déjà clôturée, elle sera reprise dans la clôture suivante.

Astuce

  * À des fins de test et d’audit, ces clôtures peuvent être générées manuellement en [mode développeur](../../general/developer_mode.html#developer-mode).

  * Ensuite, allez aux Paramètres ‣ Technique ‣ Automatisation ‣ Actions planifiées.

### Responsabilités

Ne désinstallez pas le module ! Les hachages seront réinitialisés et aucune de
vos données précédentes ne sera plus garantie comme étant inaltérable.

Les utilisateurs restent responsables de leur instance Odoo et doivent
l’utiliser avec diligence. Ils ne sont pas autorisés à modifier le code source
qui garantit l’inaltérabilité des données.

Odoo se décharge de toute responsabilité en cas de modification des
fonctionnalités du module causée par des applications tierces non certifiées
par Odoo.

### Plus d’informations

Vous trouverez plus d’informations relatives à cette législation dans les
documents officiels suivants.

Pour plus d'infos

  * [Foire aux questions](https://www.economie.gouv.fr/files/files/directions_services/dgfip/controle_fiscal/actualites_reponses/logiciels_de_caisse.pdf)

  * [Déclaration officielle](http://bofip.impots.gouv.fr/bofip/10691-PGP.html?identifiant=BOI-TVA-DECLA-30-10-30-20160803)

  * [Article 88 de la Loi n° 2015-1785 du 29 décembre 2015 de finances pour 2016](https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=JORFARTI000031732968&categorieLien=id&cidTexte=JORFTEXT000031732865)

