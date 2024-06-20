# Branches

## Vue d’ensemble

La vue Branches vous donne une vue d’ensemble des différentes branches de
votre dépôt.

![../../../_images/interface-branches.png](../../../_images/interface-
branches.png)

## Phases

Odoo.sh propose trois différentes phases pour vos branches : production,
simulation et développement.

Vous pouvez changer la phase d’une branche en la glissant et déposant sur le
titre de la section de la phase.

![../../../_images/interface-branches-
stagechange.png](../../../_images/interface-branches-stagechange.png)

### Production

Il s’agit de la branche contenant le code sur lequel tourne votre base de
données de production. Il ne peut y avoir qu’une seule branche de production.

Lorsque vous poussez un nouveau commit vers cette branche, votre serveur de
production est mis à jour avec le code de la nouvelle révision et est ensuite
redémarré.

Si vos changements nécessitent la mise à jour d’un module, comme un changement
d’une vue de formulaire et si vous voulez qu’il soit effectué automatiquement,
montez le numéro de version du module dans son manifeste (___manifest__.py_).
La plateforme se chargera alors d’effectuer la mise à jour pendant laquelle
l’instance sera temporairement indisponible pour des raisons de maintenance.

Cette méthode est similaire à la mise à niveau du module via le menu
Applications ou via le commutateur `-u` de [la ligne de
commande](../../../developer/reference/cli.html).

Si les changements dans le commit empêchent le serveur de redémarrer ou si la
mise à jour du module échoue, le serveur est automatiquement ramené à la
révision précédente du code et la base de données est rétablie telle qu’elle
était avant la mise à jour. Vous avez toujours accès au journal de l’échec de
la mise à jour, ce qui vous permet de résoudre les problèmes.

Les données de démonstration ne sont pas chargées, car elles ne sont pas
destinées à être utilisées dans une base de données de production. Les tests
unitaires ne sont pas effectués, car cela augmenterait le temps
d’indisponibilité de la base de données de production pendant les mises à
jour.

Les partenaires qui utilisent des projets d’essai doivent savoir que leur
branche de production, ainsi que toutes les branches de simulation seront
automatiquement rétablies à la phase de développement après 30 jours.

### Simulation

Les branches de simulation sont destinées à tester vos nouvelles
fonctionnalités avec les données de production sans compromettre la véritable
base de données de production avec des enregistrements de test. Elles créent
des bases de données qui sont des doublons neutralisés de la base de données
de production.

La neutralisation inclut :

  * La désactivation des actions planifiées. Si vous voulez les tester, vous pouvez déclencher leur action manuellement ou les réactiver. Attention : la plateforme les déclenchera moins souvent si personne n’utilise la base de données afin d’économiser des ressources.

  * La désactivation des emails sortants en les interceptant avec un mailcatcher. Une interface permettant de visualiser les emails envoyés par votre base de données est fournie. Ainsi, vous n’avez pas à vous soucier d’envoyer des emails de test à vos clients.

  * La configuration des fournisseurs de paiement et des transporteurs en mode test.

  * La désactivation des services IAP.

La dernière base de données sera maintenue en vie indéfiniment, les plus
anciennes de la même branche peuvent être éligibles à la garbage collection
afin de faire de la place à de nouvelles bases de données. Elle sera valide
pendant 3 mois, après quoi vous devrez reconstruire la branche. Si vous
effectuez des changements de configuration ou de vue dans ces bases de
données, assurez-vous de les documenter ou de les écrire directement dans les
modules de la branche, en utilisant des fichiers de données XML qui remplacent
la configuration ou les vues par défaut.

Les tests unitaires ne sont pas effectués, car, dans Odoo, ils reposent
actuellement sur les données de démonstration, qui ne sont pas chargées dans
la base de données de production. À l’avenir, si Odoo prend en charge
l’exécution des tests unitaires sans les données de démonstration, Odoo.sh
envisagera d’exécuter les tests sur les bases de données de simulation.

### Développement

Les branches de développement créent de nouvelles bases de données en
utilisant les données de démonstration pour exécuter les tests unitaires. Les
modules installés sont ceux compris dans vos branches. Vous pouvez modifier la
liste des modules à installer dans les [paramètres de votre
projet](settings.html#odoosh-gettingstarted-settings-modules-installation).

Lorsque vous poussez un nouveau commit vers une de ces branches, un nouveau
serveur est démarré avec une base de données créée à partir de zéro et la
nouvelle révision de la branche. Les données de démonstration sont chargées et
les tests unitaires sont effectués par défaut. Ceci permet de vérifier si vos
changements ne cassent aucune fonctionnalité testée. Si vous le souhaitez,
vous pouvez désactiver les tests ou autoriser des tests spécifiques à exécuter
avec des étiquettes personnalisées dans les paramètres de la branche.

Comme pour les branches de simulation, les emails ne sont pas envoyés, mais
interceptés par un mailcatcher et les actions planifiées ne sont pas
déclenchées tant que la base de données n’est pas utilisée.

Les bases de données créées pour les branches de développement ont une durée
de vie de trois jours. Passé ce délai, elles feront automatiquement l’objet de
la garbage collection pour faire de la place à de nouvelles bases de données
sans notification préalable.

### Fusionner vos branches

Vous pouvez facilement fusionner vos branches en les glissant et déposant
l’une sur l’autre.

![../../../_images/interface-branches-merge.png](../../../_images/interface-
branches-merge.png)

Si vous voulez tester les changements de vos branches de développement avec
les données de production, vous pouvez :

  * fusionner la branche de développement dans votre branche de simulation, en la glissant et déposant sur la branche de simulation souhaitée,

  * glisser et déposer la branche de développement sur le titre de la section de simulation, pour qu’elle devienne une branche de simulation.

Lorsque vos derniers changements sont prêts à être mis en production, vous
pouvez glisser et déposer votre branche de simulation sur votre branche de
production pour fusionner et déployer vos nouvelles fonctionnalités en
production.

Si vous êtes audacieux, vous pouvez également fusionner vos branches de
développement dans votre branche de production. Cela signifie que vous sautez
l’étape de validation de vos changements avec les données de production par le
biais d’une branche de simulation.

Vous pouvez fusionner vos branches de développement l’une avec l’autre et vos
branches de simulation l’une avec l’autre.

Bien entendu, vous pouvez également utiliser directement `git merge` sur votre
poste de travail pour fusionner vos branches. Odoo.sh sera notifié lorsque les
nouvelles révisions ont été poussées vers vos branches.

La fusion d’une branche de simulation dans la branche de production permet
uniquement de fusionner le code source. Tous les changements de configuration
que vous avez effectués dans les bases de données de simulation ne seront pas
transférés à la base de données de production.

Si vous testez des changements de configuration dans les branches de
simulation et vous voulez qu’ils soient appliqués en production, vous devez :

  * soit écrire les changements de configuration dans des fichiers de données XML qui remplacent la configuration ou les vues par défaut dans vos branches et ensuite monter la version de votre module dans son manifeste (___manifest__.py_) afin de déclencher la mise à jour du module lorsque vous fusionnez votre branche de simulation dans votre branche de production. C’est la meilleure pratique permettant une meilleure scalabilité de vos développements, puisque vous utiliserez les fonctionnalités de versioning de Git pour toutes vos changements de configuration et vous aurez ainsi une traçabilité de vos changements.

  * soit les passer manuellement de votre base de données de simulation à votre base de données de production en les copiant/collant.

## Onglets

### Historique

Une vue d’ensemble de l’historique de votre branche :

  * Les messages des commits et de leurs auteurs,

  * Les différents événements liés à la plateforme, tels que les changements de phase, les importations de base de données, les restaurations de sauvegardes.

![../../../_images/interface-branches-history.png](../../../_images/interface-
branches-history.png)

Pour chaque événement, un statut s’affiche dans le coin supérieur droit. Il
fournit des informations sur l’opération en cours sur la base de données
(installation, mise à jour, importation de la sauvegarde, …) et sur ses
résultats (retours sur les tests, importation de la sauvegarde réussie, …).
Lorsqu’une opération est réussie, vous pouvez accéder à la base de données en
cliquant sur le bouton _connect_.

### Emails

Cet onglet contient le mailcatcher. Il affiche un aperçu des emails envoyés
par votre base de données. Le mailcatcher est disponible pour vos branches de
développement et de simulation, puisque les emails de votre base de données de
production sont réellement envoyés et non interceptés.

![../../../_images/interface-branches-mails.png](../../../_images/interface-
branches-mails.png)

### Shell

Un accès shell à votre conteneur. Vous pouvez exécuter des commandes linux de
base (`ls`, `top`) et ouvrir un shell sur votre base de données en tapant
`psql`.

![../../../_images/interface-branches-shell.png](../../../_images/interface-
branches-shell.png)

Vous pouvez ouvrir plusieurs onglets et les glisser-déposer pour organiser la
présentation comme vous le souhaitez, par exemple côte à côte.

Note

Les instances de shell qui fonctionnent longtemps ne sont pas garanties. Les
shells inactifs peuvent être déconnectés à tout moment afin de libérer des
ressources.

### Editor

Un environnement de développement intégré (IDE) en ligne pour modifier le code
source. Vous pouvez également ouvrir des terminaux, des consoles Python et
même des consoles shell Odoo.

![../../../_images/interface-branches-editor.png](../../../_images/interface-
branches-editor.png)

Vous pouvez ouvrir plusieurs onglets et les glisser-déposer pour organiser la
présentation comme vous le souhaitez, par exemple côte à côte.

### Monitoring

Ce lien contient diverses mesures de monitoring du build actuel.

![../../../_images/interface-branches-
monitoring.png](../../../_images/interface-branches-monitoring.png)

Vous pouvez zoomer, modifier l’intervalle de temps ou sélectionner une mesure
spécifique sur chaque graphique. Sur les graphiques, des annotations vous
aident à faire le lien avec les changements sur le build (importation de la
base de données, git push, etc.).

### Journaux

Une page qui vous permet de jeter un coup d’œil aux journaux de votre serveur.

![../../../_images/interface-branches-logs.png](../../../_images/interface-
branches-logs.png)

Plusieurs journaux sont disponibles :

  * install.log : Les journaux de l’installation de votre base de données. Une branche de développement contient les journaux des tests.

  * pip.log : Les journaux de l’installation des dépendances Python.

  * odoo.log : Les journaux du serveur en cours d’exécution.

  * update.log : Les journaux des mises à jour de la base de données.

  * pg_long_queries.log : Les journaux des requêtes psql qui prennent un temps inhabituel à s’exécuter.

Si de nouvelles lignes sont ajoutées aux journaux, elles seront affichées
automatiquement. Si vous faites défiler la page jusqu’en bas, le navigateur
défilera automatiquement chaque fois qu’une nouvelle ligne est ajoutée.

Vous pouvez interrompre l’extraction des journaux en cliquant sur le bouton
correspondant dans le coin supérieur droit de la page. L’extraction est
automatiquement interrompue après 5 minutes. Vous pouvez la relancer en
cliquant sur le bouton Play.

### Sauvegardes

Une liste des sauvegardes disponibles pour le téléchargement et la
restauration, la possibilité d’effectuer une sauvegarde manuelle et d’importer
une base de données.

![../../../_images/interface-branches-backups.png](../../../_images/interface-
branches-backups.png)

Odoo.sh effectue des sauvegardes quotidiennes de la base de données de
production. Il conserve 7 sauvegardes quotidiennes, 4 hebdomadaires et 3
mensuelles. Chaque sauvegarde inclut le dump de la base de données, le
filestore (pièces jointes, champs binaires), les journaux et les sessions.

Les bases de données de simulation et de développement ne sont pas
sauvegardées. Cependant, vous avez la possibilité de restaurer une sauvegarde
de la base de données de production dans vos branches de simulation, à des
fins de test, ou pour récupérer manuellement des données qui ont été
supprimées accidentellement de la base de données de production.

La liste contient les sauvegardes conservées sur le serveur sur lequel votre
base de données de production est hébergée. Ce serveur ne conserve qu’un mois
de sauvegardes : 7 sauvegardes quotidiennes et 4 hebdomadaires.

Les serveurs de sauvegarde dédiés conservent les mêmes sauvegardes, ainsi que
3 sauvegardes mensuelles supplémentaires. Afin de restaurer ou télécharger une
de ces sauvegardes mensuelles, veuillez [nous
contacter](https://www.odoo.com/help).

Si vous fusionnez un commit mettant à jour la version d’un ou plusieurs
modules (dans `__manifest__.py`), ou leurs dépendances Python liées (dans
`requirements.txt`), Odoo.sh effectue une sauvegarde automatiquement (signalée
avec le type Mise à jour dans la liste), car soit le conteneur sera modifié
par l’installation de nouveaux paquets pip, soit la base de données elle-même
sera modifiée avec la mise à jour du module déclenchée par la suite. Dans ces
deux cas, nous effectuons une sauvegarde, car cela peut potentiellement casser
des choses.

Si vous fusionnez un commit qui ne change que du code sans les changements
susmentionnés, alors aucune sauvegarde n’est effectuée par Odoo.sh, car ni le
conteneur ni la base de données ne sont modifiés et la plateforme considère
que c’est suffisamment sûr. Bien sûr, comme précaution supplémentaire, vous
pouvez faire une sauvegarde manuelle avant de faire des changements importants
dans vos sources de production au cas où quelque chose se passerait mal (ces
sauvegardes manuelles sont disponibles pendant environ une semaine). Pour
éviter les abus, nous limitons les sauvegardes manuelles à 5 par jour.

La fonctionnalité d” _importation de la base de données_ accepte les archives
de base de données dans le format fourni par :

  * le gestionnaire de bases de données Odoo standard (disponible pour les serveurs Odoo On Premise dans `/web/database/manager`)

  * le gestionnaire de bases de données Odoo Online,

  * le bouton de téléchargement des sauvegardes Odoo.sh de l’onglet _Backups_ ,

  * le bouton de téléchargement du dump Odoo.sh dans la [vue Builds](builds.html#odoosh-gettingstarted-builds).

### Mettre à niveau

Disponible pour les branches de production et de simulation des projets
valides.

Pour plus d'infos

[Upgrade documentation](../../upgrade.html)

### Paramètres

Vous trouverez ici certains paramètres qui ne s’appliquent qu’à la branche
actuellement sélectionnée.

![../../../_images/interface-branches-
settings.jpg](../../../_images/interface-branches-settings.jpg)

**Comportement lors d’un nouveau commit**

Pour les branches de développement et de simulation, vous pouvez modifier le
comportement de la branche lors de l’arrivée d’un nouveau commit. Par défaut,
une branche de développement créera un nouveau build et une branche de
simulation mettra à jour le build précédent (voir la Phase de production).
Ceci est particulièrement utile si vous nécessitez une configuration
particulière pour éviter d’avoir à la reconfigurer manuellement à chaque
nouveau commit. Si vous choisissez un nouveau build pour une branche de
simulation, elle fera une nouvelle copie du build de production chaque fois
qu’un commit est poussé. Une branche qui est renvoyée de simulation à
développement sera automatiquement configurée sur “Do nothing”.

**Installation de modules**

Choisissez les modules à installer automatiquement pour vos builds de
développement.

![../../../_images/interface-settings-
modulesinstallation.png](../../../_images/interface-settings-
modulesinstallation.png)

  * L’option _Installer uniquement mes modules_ installera uniquement les modules de la branche. Elle est sélectionnée par défaut. Les [sous-modules](../advanced/submodules.html#odoosh-advanced-submodules) sont exclus.

  * L’option _Installation complète (tous les modules)_ installera les modules de la branche, les modules compris dans les sous-modules et tous les modules standards d’Odoo. Lors de l’installation complète, la suite de tests est désactivée.

  * L’option _Installer une liste de modules_ installera les modules précisés dans le champ juste en dessous de cette option. Les noms sont le nom technique des modules et ils doivent être séparés par des virgules.

Si les tests sont désactivés, la suite de modules standards d’Odoo peut
prendre jusqu’à une heure. Ce paramètre s’applique uniquement aux builds de
développement. Les builds de simulation duplique le build de production et le
build de production n’installe que la base.

**Suite de tests**

Pour les branches de développement, vous pouvez choisir d’activer ou de
désactiver la suite de tests. Elle est désactivée par défaut. Lorsque la suite
de tests est activée, vous pouvez la limiter en définissant des [étiquettes de
test](../../../developer/reference/backend/testing.html#developer-reference-
testing-selection).

**Version d’Odoo**

Uniquement pour les branches de développement, vous pouvez modifier la version
d’Odoo, si vous souhaitez tester un code mis à niveau ou développer des
fonctionnalités, tandis que votre base de données de production est en cours
de mise à niveau vers une version plus récente.

De plus, pour chaque version, vous disposez de deux options concernant la mise
à jour du code :

  * Vous pouvez choisir de bénéficier automatiquement des derniers correctifs de bugs, de sécurité et de performance. Les sources de votre serveur Odoo seront mises à jour chaque semaine. Il s’agit de l’option “Latest”.

  * Vous pouvez choisir d’épingler les sources d’Odoo à une révision spécifique en les sélectionnant dans une liste de dates. Les révisions expirent après 3 mois. Vous serez notifié par email lorsque la date d’expiration approche et si vous ne prenez aucune action, vous serez automatiquement remis à la dernière révision.

**Domaines personnalisés**

Ici, vous pouvez configurer des domaines additionnels pour la branche
sélectionnée. Il est possible d’ajouter d’autres domaines _< name>.odoo.com_
ou vos propres domaines personnalisés. Pour la dernière option, vous devez :

  * posséder ou acheter le nom de domaine,

  * ajouter le nom de domaine dans cette liste,

  * dans le gestionnaire de noms de domaine de votre bureau d’enregistrement, configurer le nom de domaine avec un enregistrement `CNAME` défini sur le nom de domaine de votre base de données de production.

Par exemple, pour associer _www.mycompany.com_ à votre base de données
_mycompany.odoo.com_ :

  * dans Odoo.sh, ajoutez _www.mycompany.com_ aux domaines personnalisés des paramètres de votre projet,

  * dans le gestionnaire de votre nom de domaine (par ex. _godaddy.com_ , _gandi.net_ , _ovh.com_), configurez _www.mycompany.com_ avec un enregistrement `CNAME` ayant pour valeur _mycompany.odoo.com_.

Les domaines nus (par ex. _mycompany.com_) ne sont pas acceptés :

  * ils ne peuvent être configurés qu’à l’aide d’enregistrements `A`,

  * Les enregistrements `A` n’acceptent que les adresses IP comme valeur,

  * l’adresse IP de votre base de données peut changer, à la suite d’une mise à niveau, d’une panne matérielle ou de votre souhait d’héberger votre base de données dans un autre pays ou sur un autre continent.

Par conséquent, les domaines nus pourraient soudainement ne plus fonctionner
en raison de ce changement d’adresse IP.

De plus, si vous voulez que _mycompany.com_ et _www.mycompany.com_
fonctionnent avec votre base de données, le fait que le premier redirige vers
le second fait partie des [meilleures pratiques en matière de
référencement](https://support.google.com/webmasters/answer/7451184?hl=en)
(consultez _Fournir une version d’une URL pour atteindre un document_) afin
d’avoir une URL dominante. Vous pouvez donc simplement configurer
_mycompany.com_ pour qu’il redirige vers _www.mycompany.com_. La plupart des
gestionnaires de domaines ont la possibilité de configurer cette redirection.
C’est ce qu’on appelle communément une redirection web.

**HTTPS/SSL**

Si la redirection est correctement configurée, la plateforme générera
automatiquement un certificat SSL avec [Let’s
Encrypt](https://letsencrypt.org/about/) dans l’heure et votre domaine sera
accessible via HTTPS.

Alors qu’il n’est actuellement plus possible de configurer vos propres
certificats SSL sur la plateforme Odoo.sh, nous envisageons de le faire si la
demande est suffisante.

**Conformité SPF et DKIM**

Si le domaine des adresses email de vos utilisateurs utilisent SPF (Sender
Policy Framework) ou DKIM (DomainKeys Identified Mail), n’oubliez pas
d’autoriser Odoo en tant qu’hôte d’envoi dans les paramètres de votre nom de
domaine pour augmenter la délivrabilité de vos emails sortants. Les étapes de
configuration sont expliquées dans la documentation sur
[SPF](../../../applications/general/email_communication/email_domain.html#email-
communication-spf-compliant) et
[DKIM](../../../applications/general/email_communication/email_domain.html#email-
communication-dkim-compliant).

Avertissement

Oublier de configurer votre SPF ou DKIM pour autoriser Odoo en tant qu’hôte
d’envoi peut conduire à la livraison de vos emails en tant que spam dans la
boîte de réception de vos contacts.

## Commandes shell

Dans le coin supérieur droit de la vue, différentes commandes shell sont
disponibles.

![../../../_images/interface-branches-
shellcommands.png](../../../_images/interface-branches-shellcommands.png)

Chaque commande peut être copiée dans le presse-papiers pour l’utiliser dans
un terminal et certaines commandes peuvent être utilisées directement à partir
de Odoo.sh en cliquant sur le bouton _run_. Dans ce cas, une fenêtre
contextuelle invitera l’utilisateur à définir d’éventuels placeholders, tels
que `<URL>`, `<PATH>`, …

### Clone

Téléchargez le dépôt Git.

    
    
    $ git clone --recurse-submodules --branch master git@github.com:odoo/odoo.git
    

Clone le dépôt _odoo/odoo_.

  * `--recurse-submodules` : Télécharge les sous-modules de votre dépôt. Les sous-modules contenus dans les sous-modules sont également téléchargés.

  * `--branch` : vérifie une branche spécifique du dépôt, _master_ dans ce cas.

Le bouton _run_ n’est pas disponible pour cette commande, car elle est
destinée à être utilisée sur vos appareils.

### Fork

Créez une nouvelle branche basée sur la branche actuelle.

    
    
    $ git checkout -b feature-1 master
    

Crée une nouvelle branche intitulée _feature-1_ basée sur la branche _master_
et procède au checkout.

    
    
    $ git push -u origin feature-1
    

Charge la nouvelle branche _feature-1_ sur votre dépôt distant.

### Merge

Fusionnez la branche actuelle dans une autre branche.

    
    
    $ git merge staging-1
    

Fusionne la branche _staging-1_ dans la nouvelle branche.

    
    
    $ git push -u origin master
    

Charge les changements que vous venez d’ajouter dans la branche _master_ sur
votre dépôt distant.

### SSH

#### Configuration

Afin d’utiliser SSH, vous devez configurer la clé publique SSH de votre profil
(si ce n’est pas déjà fait). Pour ce faire, suivez les étapes suivantes :

  1. [Générez une nouvelle clé SSH](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

  2. [Copiez la clé SSH dans votre presse-papiers](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) (n’appliquez que l’étape 1)

  3. Collez le contenu copié dans les clés SSH de votre profil et cliquez sur « Add »

![../../../_images/SSH-key-pasting.png](../../../_images/SSH-key-pasting.png)

  4. La clé devrait apparaître en dessous

![../../../_images/SSH-key-appearing.png](../../../_images/SSH-key-
appearing.png)

#### Connexion

Pour vous connecter à vos builds en utilisant ssh, exécutez la commande
suivante dans un terminal :

    
    
    $ ssh <build_id>@<domain>
    

Vous trouverez un raccourci pour cette commande dans l’onglet SSH dans le coin
supérieur droit.

![../../../_images/SSH-panel.png](../../../_images/SSH-panel.png)

Si vous disposez des [bons droits d’accès](settings.html#odoosh-
gettingstarted-settings-collaborators) sur le projet, vous obtiendrez un accès
ssh au build.

Note

Les connexions ssh de longue durée ne sont pas garanties. Les connexions
inactives seront déconnectées afin de libérer des ressources.

### Sous-module

Ajoutez une branche d’un autre dépôt dans votre branche actuelle en tant que
_sous-module_.

Les _sous-modules_ vous permettent d’utiliser des modules d’autres dépôts dans
votre projet.

La fonctionnalité des sous-modules est détaillée dans le chapitre [Sous-
modules](../advanced/submodules.html#odoosh-advanced-submodules) de cette
documentation.

    
    
    $ git submodule add -b master <URL> <PATH>
    

Ajoute la branche _master_ du dépôt _< URL>_ en tant que sous-module sous le
chemin _< PATH>_ dans votre branche actuelle.

    
    
    $ git commit -a
    

Enregistre tous les changements en cours.

    
    
    $ git push -u origin master
    

Charge les changements que vous venez d’ajouter dans la branche _master_ sur
votre dépôt distant.

### Supprimer

Supprimez une branche de votre dépôt.

    
    
    $ git push origin :master
    

Supprime la branche de votre dépôt distant.

    
    
    $ git branch -D master
    

Supprime la branche dans votre copie locale du dépôt.

