# Éditeur en ligne

## Vue d’ensemble

L’éditeur en ligne vous permet d’modifier le code source de vos builds depuis
un navigateur web. Il vous permet également d’ouvrir des terminaux, des
consoles Python, des consoles Shell Odoo et des
[Notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html).

![../../../_images/interface-editor.png](../../../_images/interface-
editor.png)

Vous pouvez accédez à l’éditeur d’un build via [les onglets
Branches](branches.html#odoosh-gettingstarted-branches-tabs), [le menu
déroulant des builds](builds.html#odoosh-gettingstarted-builds-dropdown-menu)
ou en ajoutant _/odoo-sh/editor_ au nom de domaine de votre build (par ex.
_https://odoo-addons-master-1.dev.odoo.com/odoo-sh/editor_).

## Modifier le code source

Le répertoire de travail est constitué des dossiers suivants :

    
    
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
    

Vous pouvez modifier le code source (fichiers sous _/src_) dans les builds de
développement et de simulation.

Note

Vos changements ne seront pas propagés dans un nouveau build, vous devez les
commiter dans votre code source si vous voulez qu’ils persistent.

Pour les builds de production, le code source est en lecture seule, car
effectuer des changements locaux sur un serveur de production n’est pas une
bonne pratique.

  * Le code source de votre dépôt Github se trouve sous _/src/user_ ,

  * Le code source d’Odoo se trouve sous

    * _/src/odoo_ ([odoo/odoo](https://github.com/odoo/odoo)),

    * _/src/enterprise_ ([odoo/enterprise](https://github.com/odoo/enterprise)),

    * _/src/themes_ ([odoo/design-themes](https://github.com/odoo/design-themes)).

Pour ouvrir un fichier dans l’éditeur, il suffit de double-cliquer dessus dans
le panneau du navigateur de fichiers à gauche.

![../../../_images/interface-editor-open-file.png](../../../_images/interface-
editor-open-file.png)

Vous pouvez commencer à effectuer vos changements. Vous pouvez enregistrer vos
changements en allant au menu File ‣ Save .. File ou en utilisant le raccourci
``Ctrl`+`S``.

![../../../_images/interface-editor-save-file.png](../../../_images/interface-
editor-save-file.png)

Si vous enregistrez un fichier Python qui se trouve dans le chemin des modules
complémentaires de votre serveur Odoo, Odoo le détectera et rechargera
automatiquement pour que vos changement soient reflétés immédiatement sans
avoir à redémarrer le serveur manuellement.

![../../../_images/interface-editor-
automaticreload.gif](../../../_images/interface-editor-automaticreload.gif)

Cependant, si le changement concerne une donnée stockée dans la base de
données, telle que le libellé d’un champ ou une vue, vous devez mettre à jour
le module correspondant pour appliquer le changement. Vous pouvez mettre à
jour le module du fichier actuellement ouvert en utilisant le menu Odoo ‣
Update current module. Notez que le fichier considéré comme actuellement
ouvert est le fichier ciblé dans l’éditeur de texte, et non le fichier mis en
évidence dans le navigateur de fichiers.

![../../../_images/interface-editor-update-current-
module.png](../../../_images/interface-editor-update-current-module.png)

Vous pouvez également ouvrir un terminal et exécuter la commande :

    
    
    $ odoo-bin -u <comma-separated module names> --stop-after-init
    

## Commiter & pousser vos changements

Vous avez la possibilité de commiter et de pousser vos changements vers votre
dépôt Github.

  * Ouvrez un terminal (File ‣ New ‣ Terminal),

  * Changez le répertoire en _~/src/user_ en utilisant `cd ~/src/user`,

  * Phasez vos changements en utilisant `git add`,

  * Commitez vos changements en utilisant `git commit`,

  * Poussez vos changements en utilisant `git push https HEAD:<branch>`.

Dans cette dernière commande,

  * _https_ est le nom de votre dépôt distant Github _HTTPS_ (par ex. <https://github.com/username/repository.git>),

  * HEAD est la référence de la dernière révision que vous avez commitée,

  * <branch> doit être remplacé par le nom de la branche vers laquelle vous souhaitez pousser les changements, très probablement la branche actuelle si vous travaillez dans un build de développement.

![../../../_images/interface-editor-commit-
push.png](../../../_images/interface-editor-commit-push.png)

Note

Le SSH distant Github n’est pas utilisé, car votre clé privée SSH n’est pas
hébergée dans vos conteneurs de build (pour des raisons évidentes de
sécurité), ni transmise via un Agent SSH (puisque vous accédez à cet éditeur
via un navigateur web) et vous ne pouvez donc pas vous authentifier auprès de
Github en utilisant un SSH. Vous devez utilise le HTTPS distant de votre dépôt
Github pour pousser vos changements, qui est automatiquement nommé _https_
dans vos dépôts Git distants. Vous serez invité à saisir votre nom
d’utilisateur et mot de passe Github. Si vous avez activé l’authentification à
deux facteurs sur Github, vous pouvez créer un [jeton d’accès
personnel](https://help.github.com/articles/creating-a-personal-access-token-
for-the-command-line/) et l’utiliser comme mot de passe. Il suffit d’accorder
l’autorisation d’accéder au `repo`.

Note

Le dossier source Git _~/src/user_ n’est pas extrait sur une branche, mais
plutôt sur une révision détachée, puisque les builds fonctionnent sur des
révisions spécifiques plutôt que sur des branches. En d’autres termes, cela
signifie que vous pouvez avoir plusieurs builds sur la même branche, mais sur
des révisions différentes.

Une fois que vos changements sont poussés, en fonction du [comportement de
poussée de votre branche](branches.html#odoosh-gettingstarted-branches-tabs-
settings), un nouveau build peut être créé. Vous pouvez continuer à travailler
dans l’éditeur à partir duquel vous avez poussé, car il aura la même révision
que le nouveau build créé, mais assurez-vous toujours de travailler dans un
éditeur d’un build qui utilise la dernière révision de votre branche.

## Consoles

Vous pouvez ouvrir des consoles Python, qui sont des [shells interactifs
IPython](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html).
L’un des aspects les plus intéressants de l’utilisation d’une console Python
plutôt que d’un shell IPython dans un terminal est la [richesse des
possibilités
d’affichage](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-
display). Grâce à cela, vous pouvez afficher des objets en HTML.

Vous pouvez par exemple afficher les cellules d’un fichier CSV en utilisant
[pandas](https://pandas.pydata.org/pandas-docs/stable/tutorials.html).

![../../../_images/interface-editor-console-python-read-
csv.png](../../../_images/interface-editor-console-python-read-csv.png)

Vous pouvez également ouvrir une console Shell Odoo pour faire tout ce que
vous voulez avec le registre Odoo et les méthodes de modèle de votre base de
données. Vous pouvez également directement lire ou écrire sur vos
enregistrements.

Avertissement

Dans une Console Odoo, les transactions sont automatiquement commitées. Cela
signifie, par exemple, que les changements apportés aux enregistrements sont
effectivement appliqués dans la base de données. Si vous changez le nom d’un
utilisateur, le nom de l’utilisateur est également changé dans votre base de
données. Vous devez donc utiliser les consoles Odoo avec précaution sur vos
bases de données de production.

Vous pouvez utiliser _env_ pour invoquer des modèles de votre registre de
bases de données, par ex. `env['res.users']`.

    
    
    env['res.users'].search_read([], ['name', 'email', 'login'])
    [{'id': 2,
    'login': 'admin',
    'name': 'Administrator',
    'email': 'admin@example.com'}]
    

La classe `Pretty` vous permet d’afficher facilement des listes et des dicts
d’une manière attrayante, en utilisant l”[affichage
riche](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-
display) susmentionné.

![../../../_images/interface-editor-console-odoo-
pretty.png](../../../_images/interface-editor-console-odoo-pretty.png)

Vous pouvez également utiliser [pandas](https://pandas.pydata.org/pandas-
docs/stable/tutorials.html) pour afficher des graphiques.

![../../../_images/interface-editor-console-odoo-
graph.png](../../../_images/interface-editor-console-odoo-graph.png)

