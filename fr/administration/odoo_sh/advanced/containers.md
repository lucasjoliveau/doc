# Conteneurs

## Vue d’ensemble

Chaque build est isolé dans son propre conteneur (conteneur d’espace de noms
Linux).

La base est un système Ubuntu, où sont installées toutes les dépendances
nécessaires à Odoo, ainsi que des paquets utiles courants.

Si vous projet nécessite des dépendances Python supplémentaires ou des
versions plus récentes, vous pouvez définir un fichier `requirements.txt` dans
la racine de vos branches pour les lister. La plateforme se chargera
d’installer ces dépendances dans vos conteneurs. La documentation relative aux
[spécificateurs d’exigences
pip](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-
specifiers) peut vous aider à écrire un fichier `requirements.txt`. Pour avoir
un exemple concret, consultez le [fichier requirements.txt
d’Odoo](https://github.com/odoo/odoo/blob/16.0/requirements.txt).

Les fichiers `requirements.txt` des sous-modules sont également pris en
compte. La plateforme recherche les fichiers `requirements.txt` dans chaque
dossier contenant des modules Odoo : pas dans le dossier du module lui-même,
mais dans leur dossier parent.

## Structure du répertoire

Puisque les conteneurs sont basés sur Ubuntu, la structure de leur répertoire
suit la norme de la hiérarchie des systèmes de fichiers (Filesystem Hierarchy
Standard) de Linux. [L’arborescence du système de fichiers
d’Ubuntu](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview#Main_directories)
vous explique les principaux répertoires.

Voici les répertoires pertinents d’Odoo.sh :

    
    
    .
    ├── home
    │    └── odoo
    │         ├── src
    │         │    ├── odoo                Odoo Community source code
    │         │    │    └── odoo-bin       Odoo server executable
    │         │    ├── enterprise          Odoo Enterprise source code
    │         │    ├── themes              Odoo Themes source code
    │         │    └── user                Your repository branch source code
    │         ├── data
    │         │    ├── filestore           database attachments, as well as the files of binary fields
    │         │    └── sessions            visitors and users sessions
    │         └── logs
    │              ├── install.log         Database installation logs
    │              ├── odoo.log            Running server logs
    │              ├── update.log          Database updates logs
    │              └── pip.log             Python packages installation logs
    └── usr
         ├── lib
         │    ├── python2.7
         │         └── dist-packages       Python 2.7 standard libraries
         │    ├── python3
         │         └── dist-packages       Python 3 standard libraries
         │    └── python3.5
         │         └── dist-packages       Python 3.5 standard libraries
         ├── local
         │    └── lib
         │         ├── python2.7
         │         │    └── dist-packages  Python 2.7 third-party libraries
         │         └── python3.5
         │              └── dist-packages  Python 3.5 third-party libraries
         └── usr
              └── bin
                   ├── python2.7           Python 2.7 executable
                   └── python3.5           Python 3.5 executable
    

Python 2.7 et 3.5 sont tous deux installés dans les conteneurs. Cependant :

  * Si votre projet est configuré pour utiliser Odoo 10.0, le serveur Odoo fonctionne avec Python 2.7.

  * Si votre projet est configuré pour utiliser Odoo 11.0 ou les versions ultérieures, le serveur Odoo fonctionne avec Python 3.5.

## Shell de base de données

Lorsque vous accédez à un conteneur avec le shell, vous pouvez accéder à la
base de données à l’aide de _psql_.

    
    
    odoo@odoo-addons-master-1.odoo.sh:~$ psql
    psql (9.5.2, server 9.5.11)
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    odoo-addons-master-1=>
    

**Attention !** [Utilisez des
transactions](https://www.postgresql.org/docs/current/static/sql-begin.html)
(_BEGIN…COMMIT/ROLLBACK_) pour toutes les déclarations _sql_ conduisant à des
changements (_UPDATE_ , _DELETE_ , _ALTER_ , …), surtout pour votre base de
données de production.

Le mécanisme des transactions est votre filet de sécurité en cas d’erreur. Il
vous suffit de revenir sur vos changements pour ramener votre base de données
à son état antérieur.

Par exemple, il peut arriver que vous oubliiez de définir votre condition
_WHERE_.

    
    
    odoo-addons-master-1=> BEGIN;
    BEGIN
    odoo-addons-master-1=> UPDATE res_users SET password = '***';
    UPDATE 457
    odoo-addons-master-1=> ROLLBACK;
    ROLLBACK
    

Dans ce cas, vous pouvez revenir en arrière pour annuler les changements non
désirés que vous venez de faire par erreur, et réécrire la déclaration :

    
    
    odoo-addons-master-1=> BEGIN;
    BEGIN
    odoo-addons-master-1=> UPDATE res_users SET password = '***' WHERE id = 1;
    UPDATE 1
    odoo-addons-master-1=> COMMIT;
    COMMIT
    

Cependant, n’oubliez pas d’effectuer un commit ou un rollback de votre
transaction après l’avoir effectuée. Les transactions ouvertes pourraient
verrouiller des enregistrements dans vos tableaux et votre base de données en
cours d’exécution peut attendre qu’ils soient libérés. Cela peut bloquer le
serveur indéfiniment.

De plus, dans la mesure du possible, utilisez vos bases de données de
simulation pour d’abord tester vos déclarations. Vous disposerez ainsi d’un
filet de sécurité supplémentaire.

## Faire fonctionner un serveur Odoo

Vous pouvez démarrer une instance de serveur Odoo à partir d’un shell de
conteneur. Vous ne serez pas en mesure d’y accéder depuis le monde extérieur
avec un navigateur, mais vous pouvez par exemple :

  * utiliser le shell Odoo,

    
    
    $  odoo-bin shell
    >>> partner = env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1)
    >>> partner.name
    'ASUSTeK'
    >>> partner.name = 'Odoo'
    >>> env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1).name
    'Odoo'
    

  * installer un module,

    
    
    $  odoo-bin -i sale --without-demo=all --stop-after-init
    

  * mettre à jour un module,

    
    
    $  odoo-bin -u sale --stop-after-init
    

  * effectuer des tests pour un module,

    
    
    $  odoo-bin -i sale --test-enable --log-level=test --stop-after-init
    

Dans les commandes susmentionnées, l’argument :

  * `--without-demo=all` empêche de charger les données de démonstration pour tous les modules

  * `--stop-after-init` arrête immédiatement l’instance du serveur après qu’elle ait effectué les opérations demandées.

D’autres options sont disponibles et détaillées dans la [documentation
CLI](../../../developer/reference/cli.html).

Vous pouvez trouver dans les journaux (_~/logs/odoo.log_) le chemin des
modules complémentaires utilisé par Odoo.sh pour faire fonctionner votre
serveur. Cherchez «  _odoo: addons paths_ »:

    
    
    2018-02-19 10:51:39,267 4 INFO ? odoo: Odoo version 16.0
    2018-02-19 10:51:39,268 4 INFO ? odoo: Using configuration file at /home/odoo/.config/odoo/odoo.conf
    2018-02-19 10:51:39,268 4 INFO ? odoo: addons paths: ['/home/odoo/data/addons/16.0', '/home/odoo/src/user', '/home/odoo/src/enterprise', '/home/odoo/src/themes', '/home/odoo/src/odoo/addons', '/home/odoo/src/odoo/odoo/addons']
    

**Attention** , surtout avec votre base de données de production. Les
opérations que vous effectuez en exécutant cette instance de serveur Odoo ne
sont pas isolées : les changements seront effectifs dans la base de données.
Effectuez toujours vos tests dans vos bases de données de simulation.

## Débogage dans Odoo.sh

Le débogage d’un build Odoo.sh n’est pas vraiment différent de celui d’une
autre application Python. Cet article explique uniquement les spécificités et
les limites de la plateforme Odoo.sh et suppose que vous savez déjà utiliser
un débogueur.

Note

Si vous ne savez pas encore comment déboguer une application Python, il existe
de nombreux cours d’introduction que vous pouvez facilement trouver sur
Internet.

Vous pouvez utiliser `pdb`, `pudb` ou `ipdb` pour déboguer votre code sur
Odoo.sh. Comme le serveur est exécuté en dehors d’un shell, vous ne pouvez pas
lancer le débogueur directement à partir du backend de votre instance Odoo,
car le débogueur a besoin d’un shell pour fonctionner.

  * [pdb](https://docs.python.org/3/library/pdb.html) est installé par défaut dans chaque conteneur.

  * Si vous voulez utiliser [pudb](https://pypi.org/project/pudb/) ou [ipdb](https://pypi.org/project/ipdb/) vous devez l’installer avant.

Pour ce faire, vous avez deux options :

>     * temporaire (uniquement dans le build actuel) :
>  
>         >         $  pip install pudb --user
>  
>
> ou
>  
>         >         $  pip install ipdb --user
>  
>
>     * permanent : ajoutez `pudb` ou `ipdb` au fichier `requirements.txt` de
> votre projet.

Modifiez ensuite le code où vous voulez déclencher le débogueur et ajoutez
ceci :

    
    
    import sys
    if sys.__stdin__.isatty():
        import pdb; pdb.set_trace()
    

La condition `sys.__stdin__.isatty()` est un hack qui détecte si vous faites
fonctionner Odoo à partir d’un shell.

Enregistrez le fichier et exécutez ensuite le Shell Odoo :

    
    
    $ odoo-bin shell
    

Enfin, _via_ le Shell Odoo, vous pouvez déclencher le morceau de
code/fonction/méthode que vous voulez déboguer.

![Capture d'écran d'une console montrant ``pdb`` qui fonctionne dans un shell
Odoo.sh.](../../../_images/pdb_sh.png)

