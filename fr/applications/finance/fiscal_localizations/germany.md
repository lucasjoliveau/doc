# Allemagne

## Plan comptable allemand

Les plans comptables SKR03 et SKR04 sont tous deux pris en charge dans Konvergo ERP.
Vous pouvez choisir celui que vous voulez utiliser en allant à Comptabilité ‣
Configuration. Choisissez le package souhaité dans la section Localisation
fiscale.

Attention, vous ne pouvez modifier le package comptable que tant que vous
n’avez pas créé d’écriture comptable.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Lorsque vous créez une nouvelle base de données Konvergo ERP Online, SKR03 est installé par défaut.</p>
</div>

## Rapports comptables allemands

Voici la liste des rapports spécifiques à l’Allemagne disponibles dans Konvergo ERP
Enterprise :

  * Bilan

  * Compte de résultat

  * Déclaration de TVA (Umsatzsteuervoranmeldung)

  * TVA intra partenaire

## Exporter d’Konvergo ERP vers Datev

Il est possible d’exporter vos écritures comptables d’Konvergo ERP vers Datev. Pour
pouvoir utiliser cette fonctionnalité, la localisation comptable allemande
doit être installée sur votre base de données Konvergo ERP Enterprise. Allez ensuite à
Comptabilité ‣ Analyse ‣ Grand livre, puis cliquez sur le bouton **Exporter
Datev (csv)**.

## Point de vente en Allemagne : Système de sécurité technique

Le **Kassensicherungsverordnung** (le Règlement de sécurité des caisses
enregistreuses) exige que des systèmes d’enregistrement électroniques - y
compris les systèmes de [point de vente](../../sales/point_of_sale) \-
soient équipés d’un **Système de sécurité technique** (également appelé
**TSS** ou **TSE**).

Konvergo ERP propose un service conforme avec l’aide de
[fiskaly](https://fiskaly.com), une _solution cloud_.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Puisqu’il s’agit d’une solution cloud, une connexion internet fonctionnelle est indispensable.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les seuls taux de TVA autorisés sont fournis par fiskaly. Vous pouvez vérifier ces taux en consultant : <a href="https://developer.fiskaly.com/api/dsfinvk/v0/#tag/VAT-Definition">fiskaly DSFinV-K API: VAT Definition</a>.</p>
</div>

### Configuration

#### Installation des modules

  1. Si votre base de données a été créée avant juin 2021, [mettez à niveau](../../general/apps_modules#general-upgrade) votre application **Point de Vente** (`point_of_sale`) et le module **Restaurant** (`pos_restaurant`).

  2. [Installez](../../general/apps_modules#general-install) les modules **Allemagne - Certification pour point de vente** (`l10n_de_pos_cert`) et **Allemagne - Certification pour Point de Vente de type restaurant** (`l10n_de_pos_res_cert`).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si ces modules ne sont pas répertoriés, <a href="../../general/apps_modules#general-install"><span class="std std-ref">mettez à jour la liste des apps</span></a>.</p>
</div>

![Mise à niveau de Point de Vente d'Konvergo ERP depuis le tableau de bord des
apps.](../../../_images/pos-upgrade.png)

#### Enregistrer votre entreprise auprès de l’autorité financière

Pour enregistrer votre entreprise, allez aux Paramètres ‣ Paramètres généraux
‣ Sociétés ‣ Mettre à jour les informations, complétez les champs suivants et
_enregistrez_.

  * **Nom de la société**

  * **Adresse** valide

  * Numéro de **TVA**

  * **St.-Nr** (Steuernummer) : ce numéro est attribué par l’administration fiscale à toute personne physique ou morale assujettie (par ex. `2893081508152`)

  * **W-IdNr** (Wirtschafts-Identifikationsnummer) : ce numéro est utilisé comme numéro d’identification permanent des personnes économiques actives.

Vous pouvez ensuite **enregistrer votre société via fiskaly** en ouvrant
l’onglet _fiskaly_ et en cliquant sur le bouton _Enregistrement fiskaly_.

![Bouton pour enregistrer une entreprise via fiskaly dans
Konvergo ERP.](../../../_images/fiskaly-registration.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous ne voyez pas le bouton <em>Enregistrement fiskaly</em>, assurez-vous que vous avez <em>enregistré</em> les coordonnées de la société et que vous n’êtes plus en <em>mode édition</em>.</p>
</div>

Une fois l’enregistrement finalisé, de nouveaux champs apparaissent :

  * **ID organisation fiskaly** fait référence à l’ID de votre société du côté de fiskaly.

  * **Clé** et **secret API fiskaly** sont les identifiants que le système utilise pour accéder aux services proposés par fiskaly.

![clés fiskaly affichées dans Konvergo ERP](../../../_images/fiskaly-keys.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est possible de demander de nouveaux identifiants en cas de problème avec les identifiants actuels.</p>
</div>

#### Créer et lier un Système de sécurité technique à votre PdV

![Créez une option TSS à partir d'un point de vente](../../../_images/create-
tss.png)

Pour utiliser votre point de vente en Allemagne, vous devez d’abord lui créer
un TSS.

Pour ce faire, allez à Point de Vente ‣ Configuration ‣ Point de Vente, ouvrez
le point de vente que vous voulez modifier, puis cochez la case à côté de
**Créer TSS** et cliquez sur _Enregistrer_.

![Exemple d'un ID TSS et ID Client de fiskaly dans Konvergo ERP Point de
Vente](../../../_images/tss-ids.png)

Une fois que la création du TSS est réussie, vous trouverez votre **ID TSS**
et **ID Client** dans la section _API fiskaly_.

  * **ID TSS** fait référence à l’ID de votre TSS du côté de fiskaly.

  * **ID Client** fait référence à votre PdV, mais du côté de fiskaly.

### DSFinV-K

![Menu à exporter DSFinV-K](../../../_images/dsfinv-k-export.png)

Lorsque vous clôturez une session PdV, les détails de la commande sont envoyés
au service DSFinV-K de fiskaly.

En cas d’audit, vous pouvez exporter les données envoyées à DSFinV-K en allant
à Point de Vente ‣ Commandes ‣ Exports DSFinV-k.

Ces champs sont obligatoires :

  * **Nom**

  * **Datetime de début** (exporter les données dont la date est supérieure ou égale à la date de début donnée)

  * **Datetime de fin** (exporter les données sont la date est inférieure ou égale à la date de fin donnée)

Laissez le champ **Point de Vente** vide si vous souhaitez exporter les
données de tous vos points de vente. Précisez un Point de Vente si vous
souhaitez seulement exporter les données de ce PdV spécifique.

La création d’un export DSFinV-K entraîne un export du côté de fiskaly.

![Export DSFinV-K en attente dans Konvergo ERP](../../../_images/dsfinv-k-export-
fields.png)

Comme vous pouvez le voir, le **Statut** est _En attente_. Ceci signifie que
l’export a été généré avec succès et est en cours de traitement. Vous devez
cliquer sur _Actualiser le statut_ pour vérifier si l’export est terminé.

## Normes comptables fiscales allemandes : Le guide Konvergo ERP de la conformité aux
normes GoBD

**GoBD** signifie [Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von
Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum
Datenzugriff](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf).
En bref, il s’agit d’une **ligne directrice pour la gestion et la conservation
appropriée des livres, enregistrements et documents sous forme électronique,
ainsi que pour l’accès aux données** , qui est pertinente pour l’autorité
fiscale allemande, la déclaration de TVA et le bilan.

Ces principes ont été écrits et publiés par le Ministère fédéral des Finances
(BMF) en novembre 2014. Depuis janvier 2015, **ils sont devenus la norme** et
remplacent les pratiques précédemment acceptées relatives à la comptabilité
informatisée. Plusieurs changements ont été apportés par le BMF en 2019 et
janvier 2020 pour préciser certains contenus et en raison du développement des
solutions numériques (hébergement cloud, entreprises sans papier, etc.).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP vous donne <b>les moyens d’être en conformité avec les normes GoBD</b>.</p>
</div>

### Que faut-il savoir sur le GoBD lorsqu’on utilise un logiciel de
comptabilité ?

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La meilleure façon de comprendre le GoBD est de lire le <a href="https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf">texte officiel du GoBD</a>. Il est assez long, mais tout à fait compréhensible pour les non-experts. En résumé, voici ce à quoi il faut s’attendre :</p>
</div>

Le **GoBD est contraignant pour les entreprises qui doivent présenter des
comptes, y compris les PME, les indépendants et les entrepreneurs, aux
autorités financières**. À ce titre, **le contribuable lui-même est seul
responsable** de la conservation complète et exhaustive des données fiscales
(données financières et connexes précitées).

Outre les exigences logicielles, l’utilisateur est tenu d’assurer des systèmes
de contrôle interne (_conformément à l’article 146 du Code fiscal allemand_) :

  * Contrôle des droits d’accès ;

  * Séparation des tâches, séparation fonctionnelle ;

  * Contrôles de saisie (notifications d’erreur, contrôles de plausibilité) ;

  * Contrôles de réconciliation lors de la saisie des données ;

  * Contrôles du traitement ;

  * Mesures visant à empêcher la manipulation intentionnelle ou non intentionnelle de logiciels, de données ou de documents.

L’utilisateur doit distribuer les tâches au sein de son organisation entre les
postes concernés (_contrôle_) et vérifier que les tâches sont correctement et
complètement exécutées (_supervision_). Le résultat de ces contrôles doit être
enregistré (_documentation_) et si des erreurs sont constatées pendant ces
contrôles, des mesures appropriées pour corriger la situation doivent être
mises en place (_prévention_).

### Qu’en est-il de la sécurité des données ?

**Le contribuable doit sécuriser le système contre toute perte de données due
à l’effacement, à la suppression ou au vol de données**. Si les écritures ne
sont pas suffisamment sécurisées, la comptabilité sera considérée comme non
conforme aux directives du GoBD.

Une fois que les écritures ont été comptabilisées, elles ne peuvent plus être
modifiées ou supprimées via l’application.

  * Si Konvergo ERP est utilisé dans le cloud, des sauvegardes régulières font partie du service d’Konvergo ERP Online. De plus, des sauvegardes régulières peuvent être téléchargées et sauvegardées sur des systèmes externes.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odooo.com/cloud-sla">Hébergement Cloud Konvergo ERP - Accord de niveau de service</a></p>
</div>

  * Si le serveur est hébergé localement, il incombe à l’utilisateur de créer l’infrastructure de sauvegarde nécessaire.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Dans certains cas, les données doivent être conservées pendant dix ans ou plus. Conservez donc toujours des sauvegardes. C’est d’autant plus important si vous décidez de changer de fournisseur de logiciels.</p>
</div>

### Responsabilité de l’éditeur de logiciel

Étant donné que le GoBD s’applique uniquement entre le contribuable et
l’autorité financière, **l’éditeur de logiciel ne peut aucunement être tenu
responsable de l’exactitude et de la conformité de la documentation des
données transactionnelles financières de ses utilisateurs**. Il peut
simplement fournir les outils nécessaires à l’utilisateur pour qu’il respecte
les directives relatives au logiciel décrites dans le GoBD.

### Comment est-ce qu’Konvergo ERP peut vous aider à être conforme ?

Les maîtres-mots, en matière de GoBD, sont : **traçable, vérifiable, vrai,
clair et continu**. En bref, vous devez disposer d’un archivage à l’épreuve
des audits et Konvergo ERP vous donne les moyens d’atteindre tous ces objectifs :

  1. **Traçabilité et vérifiabilité**

Chaque enregistrement dans Konvergo ERP est estampillé avec le créateur du document,
la date de création, la date de modification et la personne qui l’a modifié.
De plus, les champs pertinents sont trackés, ce qui permet de voir quelle
valeur a été modifiée par qui dans le chatter de l’objet concerné.

  2. **Exhaustivité**

Toutes les données financières doivent être enregistrées dans le système, sans
exception. Konvergo ERP s’assure qu’il n’y a pas d’écart dans la numérotation des
transactions financières. Il incombe à l’utilisateur d’encoder toutes les
données financières dans le système. Puisque toutes les données financières
dans Konvergo ERP sont générées automatiquement, il incombe à l’utilisateur d’encoder
toutes les factures fournisseurs et les opérations diverses.

  3. **Exactitude**

Moyennant une configuration correcte, Konvergo ERP s’assure que les bons comptes sont
utilisés. En outre, les mécanismes de contrôle entre les bons de commande et
les commandes clients et leurs factures respectives reflètent la réalité de
l’entreprise. Il incombe à l’utilisateur de numériser et joindre la facture
fournisseur papier à l’enregistrement correspondant dans Konvergo ERP. _Konvergo ERP Documents
vous permet d’automatiser cette tâche_.

  4. **Comptabilisation et archivage en temps voulu**

Comme la plupart des données financières dans Konvergo ERP sont générées par les
objets transactionnels (par exemple, la facture est comptabilisée lors de la
confirmation), Konvergo ERP assure un archivage immédiat et prêt à l’emploi. Il
incombe à l’utilisateur d’encoder toutes les factures fournisseurs entrantes
dans les meilleurs délais, ainsi que les opérations diverses.

  5. **Ordre**

Les données financières conservées dans Konvergo ERP sont par définition ordonnées et
peuvent être réordonnées en fonction de la plupart des champs présents dans le
modèle. Un ordre spécifique n’est pas imposé par le GoBD, mais le système doit
garantir qu’une transaction financière donnée peut être rapidement trouvée par
un expert tiers. Konvergo ERP s’en charge dès le départ.

  6. **Inaltérabilité**

Avec la localisation allemande d’Konvergo ERP, Konvergo ERP est en standard configuré de telle
manière que la clause d’inaltérabilité peut être respectée sans aucune autre
personnalisation.

### Avez-vous besoin d’un export GoBD ?

En cas de contrôle fiscal, l’autorité fiscale peut demander trois niveaux
d’accès au système comptable (Z1, Z2, Z3). Ces niveaux vont de l’accès direct
à l’interface à la remise des données financières sur un dispositif de
stockage.

En cas de remise des données financières sur un dispositif de stockage, le
format n’est **pas** imposé par le GoBD. Il peut s’agir, par exemple, du
format XLS, CSV, XML, Lotus 123, SAP, AS/400 ou autre. En standard, Konvergo ERP prend
en charge l’export de données financières en format CSV et XLS. Le GoBD
**recommande** l’export dans un format GoBD spécifique basé sur XML (voir «
Ergänzende Informationen zur Datenntträgerüberlassung » §3), mais ce n’est pas
obligatoire.

### Quel est le rôle et la signification de la certification de conformité ?

Le GoBD stipule clairement qu’en raison de la nature d’un logiciel de
comptabilité de pointe, de ses possibilités de configuration, de sa nature
changeante et de ses diverses formes d’utilisation, **aucune certification
légalement contraignante ne peut être délivrée** , pas plus que le logiciel ne
peut être tenu responsable vis-à-vis des autorités publiques. Les certificats
tiers peuvent en effet avoir **une valeur informative** permettant aux clients
de prendre des décisions concernant l’achat de logiciels, mais ils ne sont en
aucun cas légalement contraignants ou n’ont aucune autre valeur juridique (A.
12, § 181).

Un certificat GoBD ne dit rien d’autre que si vous utilisez le logiciel
conformément à ses directives, le logiciel ne vous empêchera pas de respecter
le GoBD. Ces certifications sont très coûteuses en termes de temps et d’argent
et leur valeur est très relative. C’est la raison pour laquelle nous
concentrons nos efforts sur la conformité avec le GoBD, plutôt que de payer
pour un outil de marketing qui n’offre aucune sécurité juridique à nos
clients.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Puisqu’il s’agit d’une solution cloud, une connexion internet fonctionnelle est indispensable.</p>
</div>0

### Que se passe-t-il si vous n’êtes pas en conformité ?

En cas d’infraction, vous pouvez vous attendre à une amende, mais également à
un jugement du tribunal exigeant la mise en œuvre de mesures spécifiques.

  *[TSS]: Système de sécurité technique
  *[DSFinV-K]: Digitale Schnittstelle der Finanzverwaltung für Kassensysteme

