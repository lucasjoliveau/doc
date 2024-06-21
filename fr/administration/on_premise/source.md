# Installation par la source

L””installation” de la source ne consiste pas à installer Konvergo ERP, mais à
l’exécuter directement à partir de la source.

L’utilisation de la source d’Konvergo ERP peut être plus pratique pour les
développeurs de modules, car elle est plus facilement accessible que
l’utilisateur de programmes d’installation.

Elle rend le démarrage et l’arrêt d’Konvergo ERP plus flexibles et plus explicites que
les services configurés par les programmes d’installation. De plus, elle
permet d’outrepasser les paramètres en utilisant [des paramètres de ligne de
commande](../../developer/reference/cli#reference-cmdline) sans avoir à
éditer un fichier de configuration.

Enfin, elle offre un plus grand contrôle sur la configuration du système et
permet de conserver (et d’exécuter) plus facilement plusieurs versions d’Konvergo ERP
côte à côte.

## Récupérer les sources

Il y a deux façons d’obtenir le code source d’Konvergo ERP : sous forme d”**archive**
ZIP ou via **Git** :

### Archive

Édition Community :

  * [Page de téléchargement d’Konvergo ERP](https://www.odoo.com/page/download)

  * [Dépôt Community GitHub](https://github.com/odoo/odoo)

  * [Serveur Nightly](https://nightly.odoo.com)

Édition Enterprise :

  * [Page de téléchargement d’Konvergo ERP](https://www.odoo.com/page/download)

  * [Dépôt Enterprise GitHub](https://github.com/odoo/enterprise)

### Git

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous devez d’abord installer <a href="https://git-scm.com/">Git</a> et il est recommandé d’avoir une connaissance de base des commandes Git pour continuer.</p>
</div>

Pour cloner un dépôt Git, choisissez entre le clonage avec HTTPS ou SSH. Dans
la plupart des cas, la meilleure option est HTTPS. Cependant, choisissez SSH
si vous souhaitez contribuer au code source d’Konvergo ERP ou lorsque vous suivez le
[tutoriel de démarrage du
développeur](../../developer/tutorials/getting_started).

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
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>

## Préparation

### Python

Konvergo ERP a besoin de **Python 3.7** ou d’une version ultérieure pour fonctionner.

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

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si Python 3 est déjà installé, assurez-vous que la version est 3.7 ou supérieure, car les versions précédentes ne sont pas compatibles avec Konvergo ERP.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-5-TGludXg=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-5-TGludXg=" name="TGludXg=" role="tab" tabindex="0">Linux</button><button aria-controls="panel-5-V2luZG93cw==" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-5-V2luZG93cw==" name="V2luZG93cw==" role="tab" tabindex="-1">Windows</button><button aria-controls="panel-5-TWFjIE9T" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-5-TWFjIE9T" name="TWFjIE9T" role="tab" tabindex="-1">Mac OS</button></div><div aria-labelledby="tab-5-TGludXg=" class="sphinx-tabs-panel group-tab" id="panel-5-TGludXg=" name="TGludXg=" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python3 --version
</pre></div>
</div>
</div><div aria-labelledby="tab-5-V2luZG93cw==" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-5-V2luZG93cw==" name="V2luZG93cw==" role="tabpanel" tabindex="0"><div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:\&gt;</span> python --version
</pre></div>
</div>
</div><div aria-labelledby="tab-5-TWFjIE9T" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-5-TWFjIE9T" name="TWFjIE9T" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python3 --version
</pre></div>
</div>
</div></div>
<p>Vérifiez que <a href="https://pip.pypa.io">pip</a> est également installé pour cette version.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-6-TGludXg=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-6-TGludXg=" name="TGludXg=" role="tab" tabindex="0">Linux</button><button aria-controls="panel-6-V2luZG93cw==" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-6-V2luZG93cw==" name="V2luZG93cw==" role="tab" tabindex="-1">Windows</button><button aria-controls="panel-6-TWFjIE9T" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-6-TWFjIE9T" name="TWFjIE9T" role="tab" tabindex="-1">Mac OS</button></div><div aria-labelledby="tab-6-TGludXg=" class="sphinx-tabs-panel group-tab" id="panel-6-TGludXg=" name="TGludXg=" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> pip3 --version
</pre></div>
</div>
</div><div aria-labelledby="tab-6-V2luZG93cw==" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-6-V2luZG93cw==" name="V2luZG93cw==" role="tabpanel" tabindex="0"><div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:\&gt;</span> pip --version
</pre></div>
</div>
</div><div aria-labelledby="tab-6-TWFjIE9T" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-6-TWFjIE9T" name="TWFjIE9T" role="tabpanel" tabindex="0"><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> pip3 --version
</pre></div>
</div>
</div></div>
</div>

### PostgreSQL

Konvergo ERP utilise PostgreSQL en tant que système de gestion de base de données.

LinuxWindowsMac OS

Utilisez un gestionnaire de paquets pour télécharger et installer PostgreSQL
(versions prises en charge : 12.0 ou supérieur). Il est possible d’y parvenir
en exécutant ce qui suit :

    
    
    $ sudo apt install postgresql postgresql-client
    

[Téléchargez PostgreSQL](https://www.postgresql.org/download/windows)
(versions prises en charge : 12.0 ou supérieur) et installez-le.

Utilisez [Postgres.app](https://postgresapp.com) pour télécharger et installer
PostgreSQL (versions prises en charge : 12.0 ou supérieur).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour que les outils de ligne de commande fournis avec Postgres.app soient disponibles, assurez-vous de configurer la variable <code>$PATH</code> en suivant les <a href="https://postgresapp.com/documentation/cli-tools">instructions relatives aux outils CLI de Postgres.app</a>.</p>
</div>

Par défaut, le seul utilisateur est `postgres`. Comme Konvergo ERP ne permet pas de se
connecter en tant que `postgres`, créez un nouvel utilisateur PostgreSQL.

LinuxWindowsMac OS

    
    
    $ sudo -u postgres createuser -d -R -S $USER
    $ createdb $USER
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’utilisateur PostgreSQL ayant le même nom que l’identifiant Unix, il est possible de se connecter à la base de données sans mot de passe.</p>
</div>

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
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’utilisateur PostgreSQL ayant le même nom que l’identifiant Unix, il est possible de se connecter à la base de données sans mot de passe.</p>
</div>

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

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Using pip may lead to security issues and broken dependencies; only do this if you
know what you are doing.</p>
</div>

Comme certains packages Python nécessitent une étape de compilation, ils
requièrent l’installation d’un système de gestion de bibliothèque.

Sur Debian/Ubuntu, la commande suivante doit installer ces bibliothèques
requises :

    
    
    $ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
    

Les dépendances Konvergo ERP sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire Konvergo ERP Community.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les packages Python dans <code>requirements.txt</code> sont basés sur leur version stable/LTS Debian/Ubuntu correspondante au moment de la publication d’Konvergo ERP. Par exemple, pour Konvergo ERP 15.0, la version du package <code>python3-babel</code> est 2.8.0 dans Debian Bullseye et 2.6.0 dans Ubuntu Focal. La version la plus basse est alors choisie dans le fichier <code>requirements.txt</code>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il peut être préférable de ne pas mélanger les packages de modules Python entre les différentes instances d’Konvergo ERP ou avec le système. Cependant, il est possible d’utiliser <a href="https://pypi.org/project/virtualenv/">virtualenv</a> pour créer des environnements Python isolés.</p>
</div>

Allez jusqu’au chemin de l’installation Konvergo ERP Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences pour installer les exigences pour
l’utilisateur actuel.

    
    
    $ cd /CommunityPath
    $ pip install -r requirements.txt
    

Avant d’installer les dépendances, téléchargez et installez les [Outils de
développement pour Visual
Studio](https://visualstudio.microsoft.com/downloads/). Sélectionnez **outils
de développement C++** dans l’onglet **Charges de travail** et installez-les
lorsque vous y êtes invité.

Les dépendances d’Konvergo ERP sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire d’Konvergo ERP Community.

> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il peut être préférable de ne pas mélanger les packages de modules Python entre les différentes instances d’Konvergo ERP ou avec le système. Cependant, il est possible d’utiliser <a href="https://pypi.org/project/virtualenv/">virtualenv</a> pour créer des environnements Python isolés.</p>
</div>

Allez jusqu’au chemin de l’installation Konvergo ERP Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences dans un terminal **avec privilèges
d’administrateur** :

    
    
    C:\> cd \CommunityPath
    C:\> pip install setuptools wheel
    C:\> pip install -r requirements.txt
    

Les dépendances d’Konvergo ERP sont répertoriées dans le fichier `requirements.txt`
situé à la racine du répertoire d’Konvergo ERP Community.

> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>0

Allez jusqu’au chemin de l’installation Konvergo ERP Community (`CommunityPath`) et
exécutez **pip** sur le fichier d’exigences :

    
    
    $ cd /CommunityPath
    $ pip3 install setuptools wheel
    $ pip3 install -r requirements.txt
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>1

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>3

## Exécuter Konvergo ERP

Une fois que toutes les dépendances sont installées, Konvergo ERP peut être lancé en
exécutant `odoo-bin`, l’interface en ligne de commande du serveur. Elle se
situe à la racine du répertoire Konvergo ERP Community.

Pour configurer le serveur, vous pouvez définir des [arguments de ligne de
commande](../../developer/reference/cli#reference-cmdline-server) ou un
[fichier de configuration](../../developer/reference/cli#reference-
cmdline-config).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>4

Les configurations nécessaires les plus courantes sont les suivantes :

  * Utilisateur et mot de passe PostgreSQL.

  * Chemins d’accès personnalisés au-delà des chemins par défaut pour charger vos propres modules.

Une façon typique d’exécuter le serveur serait :

LinuxWindowsMac OS

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Konvergo ERP Community et `mydb`
est le nom de la base de données PostgreSQL.

    
    
    C:\> cd CommunityPath/
    C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Konvergo ERP Community, `dbuser`
est le login PostgreSQL, `dbpassword` est le mot de passe PostgreSQL et `mydb`
est le nom de la base de données PostgreSQL.

    
    
    $ cd /CommunityPath
    $ python3 odoo-bin --addons-path=addons -d mydb
    

Où `CommunityPath` est le chemin de l’installation Konvergo ERP Community et `mydb`
est le nom de la base de données PostgreSQL.

Une fois que le serveur a démarré (le journal INFO `odoo.modules.loading:
Modules loaded.` est imprimé), ouvrez <http://localhost:8069> dans un
navigateur web et connectez-vous à la base de données Konvergo ERP avec le compte
administrateur de base : utilisez `admin` comme adresse email et, à nouveau,
`admin` comme mot de passe.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Le dépôt Enterprise git ne contient pas l’intégralité du code source d’Konvergo ERP</b>. Il ne s’agit que d’une collection de modules complémentaires. Le code principal du serveur se trouve dans la version Community. Exécuter la version Enterprise signifie exécuter le serveur à partir de la version Community avec l’option <code>addons-path</code> configurée sur le dossier contenant la version Enterprise. Vous devez cloner à la fois les dépôts Community et Enterprise pour avoir une installation Konvergo ERP Enterprise qui fonctionne.</p>
</div>6

