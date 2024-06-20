# Installation par la source

L””installation” de la source ne consiste pas à installer Odoo, mais à
l’exécuter directement à partir de la source.

L’utilisation de la source d’Odoo peut être plus pratique pour les
développeurs de modules, car elle est plus facilement accessible que
l’utilisateur de programmes d’installation.

Elle rend le démarrage et l’arrêt d’Odoo plus flexibles et plus explicites que
les services configurés par les programmes d’installation. De plus, elle
permet d’outrepasser les paramètres en utilisant [des paramètres de ligne de
commande](../../developer/reference/cli.html#reference-cmdline) sans avoir à
éditer un fichier de configuration.

Enfin, elle offre un plus grand contrôle sur la configuration du système et
permet de conserver (et d’exécuter) plus facilement plusieurs versions d’Odoo
côte à côte.

## Récupérer les sources

Il y a deux façons d’obtenir le code source d’Odoo : sous forme d”**archive**
ZIP ou via **Git** :

### Archive

Édition Community :

  * [Page de téléchargement d’Odoo](https://www.odoo.com/page/download)

  * [Dépôt Community GitHub](https://github.com/odoo/odoo)

  * [Serveur Nightly](https://nightly.odoo.com)

Édition Enterprise :

  * [Page de téléchargement d’Odoo](https://www.odoo.com/page/download)

  * [Dépôt Enterprise GitHub](https://github.com/odoo/enterprise)

### Git

Note

Vous devez d’abord installer [Git](https://git-scm.com/) et il est recommandé
d’avoir une connaissance de base des commandes Git pour continuer.

Pour cloner un dépôt Git, choisissez entre le clonage avec HTTPS ou SSH. Dans
la plupart des cas, la meilleure option est HTTPS. Cependant, choisissez SSH
si vous souhaitez contribuer au code source d’Odoo ou lorsque vous suivez le
[tutoriel de démarrage du
développeur](../../developer/tutorials/getting_started.html).

LinuxWindowsMac OS

Clone with HTTPSClone with SSH

    
    
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/odoo/enterprise.git
    
    
    
    $ git clone git@github.com:odoo/odoo.git
    $ git clone git@github.com:odoo/enterprise.git
    

Clone with HTTPSClone with SSH

    
    
    C:\> git clone https://github.com/odoo/odoo.git
    C:\> git clone https://github.com/odoo/enterprise.git
    
    
    
    C:\> git clone git@github.com:odoo/odoo.git
    C:\> git clone git@github.com:odoo/enterprise.git
    

Clone with HTTPSClone with SSH

    
    
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/odoo/enterprise.git
    
    
    
    $ git clone git@github.com:odoo/odoo.git
    $ git clone git@github.com:odoo/enterprise.git
    

Note

**Le dépôt Enterprise git ne contient pas l’intégralité du code source
d’Odoo**. Il ne s’agit que d’une collection de modules complémentaires. Le
code principal du serveur se trouve dans la version Community. Exécuter la
version Enterprise signifie exécuter le serveur à partir de la version
Community avec l’option `addons-path` configurée sur le dossier contenant la
version Enterprise. Vous devez cloner à la fois les dépôts Community et
Enterprise pour avoir une installation Odoo Enterprise qui fonctionne.

## Préparation

### Python

Odoo a besoin de **Python 3.7** ou d’une version ultérieure pour fonctionner.

LinuxWindowsMac OS

Utilisez un gestionnaire de paquets pour télécharger et installer Python 3 si
nécessaire.

[Téléchargez la dernière version de Python
3](https://www.python.org/downloads/windows/) et installez-la.

Pendant l’installation, cochez **Ajouter Python 3 au CHEMIN** , ensuite
cliquez sur **Personnaliser l’installation** et veillez à cocher **pip**.

Utilisez un gestionnaire de paquets ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)) pour télécharger et installer Python 3
si nécessaire.

Note

Si Python 3 est déjà installé, assurez-vous que la version est 3.7 ou
supérieure, car les versions précédentes ne sont pas compatibles avec Odoo.

LinuxWindowsMac OS

    
    
    $ python3 --version
    
    
    
    C:\> python --version
    
    
    
    $ python3 --version
    

Vérifiez que [pip](https://pip.pypa.io) est également installé pour cette
version.

LinuxWindowsMac OS

    
    
    $ pip3 --version
    
    
    
    C:\> pip --version
    
    
    
    $ pip3 --version
    

### PostgreSQL

Odoo utilise PostgreSQL en tant que système de gestion de base de données.

LinuxWindowsMac OS

Utilisez un gestionnaire de paquets pour télécharger et installer PostgreSQL
(versions prises en charge : 12.0 ou supérieur). Il est possible d’y parvenir
en exécutant ce qui suit :

    
    
    $ sudo apt install postgresql postgresql-client
    

[Téléchargez PostgreSQL](https://www.postgresql.org/download/windows)
(versions prises en charge : 12.0 ou supérieur) et installez-le.

Utilisez [Postgres.app](https://postgresapp.com) pour télécharger et installer
PostgreSQL (versions prises en charge : 12.0 ou supérieur).

Astuce

Pour que les outils de ligne de commande fournis avec Postgres.app soient
disponibles, assurez-vous de configurer la variable `$PATH` en suivant les
[instructions relatives aux outils CLI de
Postgres.app](https://postgresapp.com/documentation/cli-tools.html).

Par défaut, le seul utilisateur est `postgres`. Comme Odoo ne permet pas de se
connecter en tant que `postgres`, créez un nouvel utilisateur PostgreSQL.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

Note

L’utilisateur PostgreSQL ayant le même nom que l’identifiant Unix, il est
possible de se connecter à la base de données sans mot de passe.

  1. Ajoutez le dépôt `bin` de PostgreSQL (par défaut : `C:\Program Files\PostgreSQL\<version>\bin`) au `PATH`.

  2. Créez un utilisateur postgres avec un mot de passe en utilisant le guide pg admin :

    1. Ouvrez **pgAdmin**.

    2. Double-cliquez sur le serveur pour créer une connexion.

    3. Sélectionnez Objet ‣ Créer ‣ Rôle Login/Groupe.

    4. Saisissez le nom d’utilisateur dans le champ **Nom de rôle** (par ex. `odoo`).

    5. Ouvrez l’onglet **Définition** , saisissez un mot de passe (par ex. `odoo`), et cliquez sur **Enregistrer**.

    6. Ouvrez l’onglet **Privilèges** et définissez **Peut se connecter ?** sur `Oui` et **Créer une base de données ?** sur `Oui`.

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

Note

L’utilisateur PostgreSQL ayant le même nom que l’identifiant Unix, il est
possible de se connecter à la base de données sans mot de passe.

### Dépendances

LinuxWindowsMac OS

L’utilisation des **packages de distribution** est la méthode préférée
d’installer les dépendances. Il est également possible d’installer les
dépendances Python avec **pip**.

Debian/UbuntuInstall with pip

Sur Debian/Ubuntu, les commandes suivantes doivent installer les packages
suivants :

    
    
    $ cd odoo #CommunityPath
    $ sudo ./setup/debinstall.sh
    

The `setup/debinstall.sh` script will parse the
[debian/control](https://github.com/odoo/odoo/blob/16.0/debian/control) file
and install the found packages.

Avertissement

Using pip may lead to security issues and broken dependencies; only do this if
you know what you are doing.

Comme certains packages Python nécessitent une étape de compilation, ils
requièrent l’installation d’un système de gestion de bibliothèque.

Sur Debian/Ubuntu, la commande suivante doit installer ces bibliothèques
requises :

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Les dépendances Odoo sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire Odoo Community.

Note

Les packages Python dans `requirements.txt` sont basés sur leur version
stable/LTS Debian/Ubuntu correspondante au moment de la publication d’Odoo.
Par exemple, pour Odoo 15.0, la version du package `python3-babel` est 2.8.0
dans Debian Bullseye et 2.6.0 dans Ubuntu Focal. La version la plus basse est
alors choisie dans le fichier `requirements.txt`.

Astuce

Il peut être préférable de ne pas mélanger les packages de modules Python
entre les différentes instances d’Odoo ou avec le système. Cependant, il est
possible d’utiliser [virtualenv](https://pypi.org/project/virtualenv/) pour
créer des environnements Python isolés.

Allez jusqu’au chemin de l’installation Odoo Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences pour installer les exigences pour
l’utilisateur actuel.

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Avant d’installer les dépendances, téléchargez et installez les [Outils de
développement pour Visual
Studio](https://visualstudio.microsoft.com/downloads/). Sélectionnez **outils
de développement C++** dans l’onglet **Charges de travail** et installez-les
lorsque vous y êtes invité.

Les dépendances d’Odoo sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire d’Odoo Community.

> Astuce
>
> Il peut être préférable de ne pas mélanger les packages de modules Python
> entre les différentes instances d’Odoo ou avec le système. Cependant, il est
> possible d’utiliser [virtualenv](https://pypi.org/project/virtualenv/) pour
> créer des environnements Python isolés.

Allez jusqu’au chemin de l’installation Odoo Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences dans un terminal **avec privilèges
d’administrateur** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Les dépendances d’Odoo sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire d’Odoo Community.

> Astuce
>
> Il peut être préférable de ne pas mélanger les packages de modules Python
> entre les différentes instances d’Odoo ou avec le système. Cependant, il est
> possible d’utiliser [virtualenv](https://pypi.org/project/virtualenv/) pour
> créer des environnements Python isolés.

Allez jusqu’au chemin de l’installation Odoo Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences :

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

Avertissement

Les dépendances non Python doivent être installées à l’aide d’un gestionnaire
de paquets ([Homebrew](https://brew.sh/),
[MacPorts](https://www.macports.org)).

  1. Téléchargez et installez les **Outils de ligne de commande** :
    
        $ xcode-select --install
    

  2. Utilisez le gestionnaire de paquets pour installer des dépendances non Python.

Note

Pour les langues utilisant une **interface de droite à gauche** (telle que
l’arabe ou l’hébreu), le package `rtlcss` est requis.

LinuxWindowsMac OS

  1. Téléchargez et installez **nodejs** et **npm** à l’aide d’un gestionnaire de paquets.

  2. Installez `rtlcss` :
    
        $ sudo npm install -g rtlcss
    

  1. Téléchargez et installez [nodejs](https://nodejs.org/en/download).

  2. Installez `rtlcss` :
    
        C:\> npm install -g rtlcss
    

  3. Modifiez la variable `PATH` de l’environnement système pour ajouter le fichier où se trouve `rtlcss.cmd` (généralement : `C:\Users\<user>\AppData\Roaming\npm\`).

  1. Téléchargez et installez **nodejs** à l’aide d’un gestionnaire de paquets ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).

  2. Installez `rtlcss` :
    
        $ sudo npm install -g rtlcss
    

Avertissement

`wkhtmltopdf` n’est pas installé par **pip** et doit être installé
manuellement dans la [version
0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) pour
qu’il prenne en charge les en-têtes et les pieds de page. Consultez la
[wkhtmltopdf wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) pour plus de
détails sur les différentes versions.

## Exécuter Odoo

Une fois que toutes les dépendances sont installées, Odoo peut être lancé en
exécutant `odoo-bin`, l’interface en ligne de commande du serveur. Elle se
situe à la racine du répertoire Odoo Community.

Pour configurer le serveur, vous pouvez définir des [arguments de ligne de
commande](../../developer/reference/cli.html#reference-cmdline-server) ou un
[fichier de configuration](../../developer/reference/cli.html#reference-
cmdline-config).

Astuce

Pour l’édition Enterprise, ajoutez le chemin vers les modules complémentaires
`enterprise` à l’argument `addons-path`. Notez qu’il doit précéder les autres
chemins dans `addons-path` pour que les modules complémentaires soient chargés
correctement.

Les configurations nécessaires les plus courantes sont les suivantes :

  * Utilisateur et mot de passe PostgreSQL.

  * Chemins d’accès personnalisés au-delà des chemins par défaut pour charger vos propres modules.

Une façon typique d’exécuter le serveur serait :

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Odoo Community et `mydb`
est le nom de la base de données PostgreSQL.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Odoo Community, `dbuser`
est le login PostgreSQL, `dbpassword` est le mot de passe PostgreSQL et `mydb`
est le nom de la base de données PostgreSQL.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Odoo Community et `mydb`
est le nom de la base de données PostgreSQL.

Une fois que le serveur a démarré (le journal INFO `odoo.modules.loading:
Modules loaded.` est imprimé), ouvrez <http://localhost:8069> dans un
navigateur web et connectez-vous à la base de données Odoo avec le compte
administrateur de base : utilisez `admin` comme adresse email et, à nouveau,
`admin` comme mot de passe.

Astuce

  * From there, create and manage new [users](../../applications/general/users.html).

  * Le compte utilisateur utilisé pour vous connecter à l’interface web d’Odoo diffère de l’argument CLI [`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r).

Pour plus d'infos

[La liste des arguments CLI pour odoo-bin](../../developer/reference/cli.html)

