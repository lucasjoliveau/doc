# Votre premier module

## Vue d’ensemble

Ce chapitre vous aide à créer votre premier module Konvergo ERP et à le déployer dans
votre projet Konvergo ERP.sh.

Ce tutoriel nécessite que [vous ayez créé un projet sur
Konvergo ERP.sh](create#odoosh-gettingstarted-create) et que vous connaissiez
l’URL de votre dépôt Github.

L’utilisation de base de Git et de Github est expliquée.

Les hypothèses suivantes sont faites :

  * _~/src_ est le répertoire où se trouvent les dépôts Git liés à vos projets Konvergo ERP,

  * _odoo_ est l’utilisateur Github,

  * _odoo-addons_ est le dépôt Github,

  * _feature-1_ est le nom d’une branche de développement,

  * _master_ est le nom de la branche de production,

  * _my_module_ est le nom du module.

Remplacez-les par les valeurs de votre choix.

## Créer la branche de développement

### À partir de Konvergo ERP.sh

Dans la vue Branches :

  * cliquez sur le bouton `+` à côté de la phase de développement,

  * choisissez la branche _master_ dans la sélection _Fork_ ,

  * saisissez _feature-1_ dans le champ _To_.

![pic1](../../../_images/firstmodule-development-+.png)
![pic2](../../../_images/firstmodule-development-fork.png)

Une fois le build créé, vous pouvez accéder à l’éditeur et naviguez vers le
dossier _~/src/user_ pour accéder au code de votre branche de développement.

![../../../_images/firstmodule-development-
editor.png](../../../_images/firstmodule-development-editor.png)
![../../../_images/firstmodule-development-editor-
interface.png](../../../_images/firstmodule-development-editor-interface.png)

### À partir de votre ordinateur

Clonez votre dépôt Github sur votre ordinateur :

    
    
    $ mkdir ~/src
    $ cd ~/src
    $ git clone https://github.com/odoo/odoo-addons.git
    $ cd ~/src/odoo-addons
    

Créez une nouvelle branche :

    
    
    $ git checkout -b feature-1 master
    

## Créer la structure du module

### Échafauder le module

Bien qu’il ne soit pas nécessaire, l’échafaudage permet d’éviter la
fastidieuse configuration de la structure de base du module Konvergo ERP. Vous pouvez
échafauder un nouveau module en utilisant l’exécutable _odoo-bin_.

À partir de l’éditeur Konvergo ERP.sh, dans un terminal :

    
    
    $ odoo-bin scaffold my_module ~/src/user/
    

Or, from your computer, if you have an [installation of
Konvergo ERP](../../on_premise/source):

    
    
    $ ./odoo-bin scaffold my_module ~/src/odoo-addons/
    

Si vous ne voulez pas installer Konvergo ERP sur votre ordinateur, vous pouvez
également [`télécharger ce modèle de structure de
module`](../../../_downloads/b7f3a4243ae7f3166cd5c4d23a256739/my_module.zip)
dans lequel vous remplacez toutes les occurrences de _my_module_ par le nom de
votre choix.

La structure suivante sera générée :

    
    
    my_module
    ├── __init__.py
    ├── __manifest__.py
    ├── controllers
    │   ├── __init__.py
    │   └── controllers.py
    ├── demo
    │   └── demo.xml
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── security
    │   └── ir.model.access.csv
    └── views
        ├── templates.xml
        └── views.xml
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>N’utilisez pas de caractères spéciaux autres que le trait de soulignement ( _ ) pour le nom de votre module, même pas un trait d’union ( - ). Ce nom est utilisé pour les classes Python de votre module et le fait d’avoir un nom de classe avec des caractères spéciaux autres que le trait de soulignement n’est pas valide en Python.</p>
</div>

Décommenter le contenu des fichiers :

  * _models/models.py_ , un exemple de modèle avec ses champs,

  * _views/views.xml_ , une arborescence et une vue formulaire, avec les menus qui les ouvrent,

  * _demo/demo.xml_ , des enregistrements de démonstration pour l’exemple de modèle ci-dessus,

  * _controllers/controllers.py_ , un exemple de contrôleur implémentant quelques routes,

  * _views/templates.xml_ , deux exemples de vues qweb utilisées par les routes du contrôleur susmentionné,

  * ___manifest__.py_ , le manifeste de votre module, y compris par exemple son titre, sa description et les fichiers de données à charger. Vous devez simplement décommenter le fichier de données de la liste de contrôle d’accès :
    
        # 'security/ir.model.access.csv',
    

### Manuellement

Si vous voulez créer votre structure de module manuellement, vous pouvez
suivre le tutoriel [Getting
started](../../../developer/tutorials/getting_started) pour comprendre la
structure d’un module et le contenu de chaque fichier.

## Pousser la branche de développement

Phasez les changements à commiter

    
    
    $ git add my_module
    

Commitez vos changements

    
    
    $ git commit -m "My first module"
    

Poussez vos changements vers votre dépôt distant

À partir d’un terminal d’éditeur Konvergo ERP.sh :

    
    
    $ git push https HEAD:feature-1
    

La commande susmentionnée est expliquée dans la section [Commiter & pousser
vos changements](online-editor#odoosh-gettingstarted-online-editor-push)
du chapitre sur l”[Éditeur en ligne](online-editor#odoosh-gettingstarted-
online-editor). Ces pages expliquent le fait que vous serez invité à saisir
votre nom d’utilisateur et votre mot de passe et ce que vous devez faire si
vous utilisez l’authentification à deux facteurs.

Ou, à partir du terminal de votre ordinateur :

    
    
    $ git push -u origin feature-1
    

Vous devez uniquement préciser _-u origin feature-1_ pour la première poussée.
À partir de là, pour pousser vos futurs changements à partir de votre
ordinateur, vous pouvez simplement utiliser

    
    
    $ git push
    

## Tester votre module

Votre branche devrait apparaître dans vos branches de développement dans votre
projet.

![../../../_images/firstmodule-test-branch.png](../../../_images/firstmodule-
test-branch.png)

Dans la vue branches de votre projet, vous pouvez cliquer sur le nom de votre
branche dans le panneau de navigation de gauche pour accéder à son historique.

![../../../_images/firstmodule-test-branch-
history.png](../../../_images/firstmodule-test-branch-history.png)

Vous pouvez voir ici les changements que vous venez de pousser, y compris le
commentaire que vous avez défini. Une fois la base de données prête, vous
pouvez y accéder en cliquant sur le bouton _Connect_.

![../../../_images/firstmodule-test-
database.png](../../../_images/firstmodule-test-database.png)

Si votre projet Konvergo ERP.sh est configuré pour installer votre module
automatiquement, vous le verrez directement parmi les applications de base de
données. Sinon, il sera disponible dans les applications à installer.

Vous pouvez ensuite faire ce que vous voulez avec votre module, créer de
nouveaux enregistrements et testez vos fonctionnalités et boutons.

## Tester avec les données de production

Pour cette étape, vous devez avoir une base de données de production. Vous
pouvez la créer si vous ne l’avez pas encore.

Une fois que vous avez testé votre module dans un build de développement avec
les données de démonstration et que vous pensez qu’il est prêt, vous pouvez le
tester avec les données de production à l’aide d’une branche de simulation.

Vous pouvez soit :

  * Faire de votre branche de développement une branche de simulation, en la glissant et déposant sur le titre de la section de _simulation_.

![../../../_images/firstmodule-test-
devtostaging.png](../../../_images/firstmodule-test-devtostaging.png)

  * La fusionner dans une base de simulation existante, en la glissant et déposant dans la branche de simulation donnée.

![../../../_images/firstmodule-test-
devinstaging.png](../../../_images/firstmodule-test-devinstaging.png)

Vous pouvez également utiliser la commande `git merge` pour fusionner vos
branches.

Cela créera un nouveau build de simulation, qui dupliquera la base de données
de production et l’exécutera en utilisant un serveur mis à jour avec les
derniers changements de votre branche.

![../../../_images/firstmodule-test-
mergedinstaging.png](../../../_images/firstmodule-test-mergedinstaging.png)

Une fois la base de données prête, vous pouvez y accéder en cliquant sur le
bouton _Connect_.

### Installer votre module

Votre module ne sera pas installé automatiquement, vous devez l’installer
depuis le menu Applications. En effet, la finalité du build de simulation est
de tester le comportement de vos changements comme s’ils avaient été effectués
sur votre production, et sur votre production, vous ne voudriez pas que votre
module soit installé automatiquement, mais plutôt à la demande.

Il se peut que votre module n’apparaisse pas non plus tout de suite dans vos
applications à installer, vous devez d’abord mettre à jour votre liste
d’applications :

  * Activez le [mode développeur](../../../applications/general/developer_mode#developer-mode)

  * dans le menu Applications, cliquez sur le bouton _Mise à jour de la liste des applications_ ,

  * dans la fenêtre contextuelle qui apparaît, cliquez sur le bouton _Mettre à jour_.

![../../../_images/firstmodule-test-
updateappslist.png](../../../_images/firstmodule-test-updateappslist.png)

Votre module apparaîtra ensuite dans la liste des applications disponibles.

![../../../_images/firstmodule-test-
mymoduleinapps.png](../../../_images/firstmodule-test-mymoduleinapps.png)

## Déployer en production

Une fois que vous avez testé votre module dans une branche de simulation avec
vos données de production et vous pensez qu’il est prêt pour la production,
vous pouvez fusionner votre branche dans la branche de production.

Glissez et déposez votre branche de simulation sur la branche de production.

![../../../_images/firstmodule-test-
mergeinproduction.png](../../../_images/firstmodule-test-
mergeinproduction.png)

Vous pouvez également utiliser la commande `git merge` pour fusionner vos
branches.

Cette opération fusionnera les derniers changements de votre branche de
simulation dans la branche de production et mettra à jour votre serveur de
production avec ces derniers changements.

![../../../_images/firstmodule-test-
mergedinproduction.png](../../../_images/firstmodule-test-
mergedinproduction.png)

Une fois la base de données prête, vous pouvez y accéder en cliquant sur le
bouton _Connect_.

### Installer votre module

Votre module ne sera pas installé automatiquement, vous devez l’installer
manuellement comme il est expliqué dans la section susmentionnée sur
l’installation de votre module dans les bases de données de simulation.

## Ajouter un changement

Cette section explique comment ajouter un changement dans votre module en
ajoutant un nouveau champ dans un modèle et en le déployant.

À partir de l’éditeur Konvergo ERP.sh,

    

  * navigez vers le dossier _~/src/user/my_module_ de votre module,

  * ensuite, ouvrez le fichier _models/models.py_.

Ou, à partir de votre ordinateur,

    

  * utilisez le navigateur de fichiers de votre choix pour naviguer vers le dossier _~/src/odoo-addons/my_module_ de votre module,

  * ensuite, ouvrez le fichier _models/models.py_ à l’aide de l’éditeur de votre choix, tel que _Atom_ , _Sublime Text_ , _PyCharm_ , _vim_ , …

Ensuite, après le champ de description

    
    
    description = fields.Text()
    

Ajoutez un champ datetime

    
    
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    

Ensuite, ouvrez le fichier _views/views.xml_.

Après

    
    
    <field name="value2"/>
    

Ajoutez

    
    
    <field name="start_datetime"/>
    

Ces changements altèrent la structure de la base de données en ajoutant une
colonne à un tableau et en modifiant une vue stockée dans la base de données.

Pour que ces changements soient appliqués dans les bases de données
existantes, telles que votre base de données de production, le module doit
être mis à jour.

Si vous voulez que la mise à jour soit effectuée automatiquement par la
plateforme Konvergo ERP.sh lorsque vous poussez vos changements, montez la version de
votre module dans son manifeste.

Ouvez le manifeste du module ___manifest__.py_.

Remplacer

    
    
    'version': '0.1',
    

par

    
    
    'version': '0.2',
    

La plateforme détectera le changement de version et déclenchera la mise à jour
du module lors du déploiement de la nouvelle révision.

Naviguez vers votre dossier Git.

Ensuite, à partir d’un terminal Konvergo ERP.sh :

    
    
    $ cd ~/src/user/
    

Ou, à partir du terminal de votre ordinateur :

    
    
    $ cd ~/src/odoo-addons/
    

Ensuite, phasez vos changements à commiter

    
    
    $ git add my_module
    

Commitez vos changements

    
    
    $ git commit -m "[ADD] my_module: add the start_datetime field to the model my_module.my_module"
    

Poussez vos changements :

À partir d’un terminal Konvergo ERP.sh :

    
    
    $ git push https HEAD:feature-1
    

Ou, à partir du terminal de votre ordinateur :

    
    
    $ git push
    

La plateforme créera ensuite un nouveau build pour la branche _feature-1_.

![../../../_images/firstmodule-test-addachange-
build.png](../../../_images/firstmodule-test-addachange-build.png)

Une fois que vous avez testé vos changements, vous pouvez fusionner vos
changements dans la branche de production, par exemple en glissant et déposant
la branche sur la branche de production dans l’interface Konvergo ERP.sh. Comme vous
avez monté la version du module dans le manifeste, la plateforme mettra à jour
le module automatiquement et votre nouveau champ sera disponible directement.
Sinon, vous pouvez mettre à jour manuellement le module dans la liste des
applications.

## Utiliser une bibliothèque Python externe

Si vous voulez utiliser une bibliothèque Python externe qui n’est pas
installée par défaut, vous pouvez définir un fichier _requirements.txt_
listant les bibliothèques externes dont dépendent vos modules.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Il n’est pas possible d’installer ou de mettre à niveau des paquets système sur une base de données Konvergo ERP.sh (par ex. des paquets apt). Cependant, dans certaines conditions, il est possible d’envisager l’installation de paquets. Ceci s’applique également aux <b>modules Python</b> nécessitant des paquets système pour leur compilation et aux <b>modules Konvergo ERP tiers</b>.</p></li>
<li><p>Les <b>extensions PostgreSQL</b> ne sont pas prises en charge sur Konvergo ERP.sh.</p></li>
<li><p>Pour plus d’informations, consultez notre <a href="https://www.odoo.sh/faq#install_dependencies">FAQ</a>.</p></li>
</ul>
</div>

La plateforme utilisera ce fichier pour installer automatiquement les
bibliothèques Python dont votre projet a besoin.

La fonctionnalité est expliquée dans cette section en utilisant la
[bibliothèque Unidecode](https://pypi.python.org/pypi/Unidecode) dans votre
module.

Créez un fichier _requirements.txt_ dans le dossier racine de votre dépôt

À partir de l’éditeur Konvergo ERP.sh, créez ou ouvrez le fichier
~/src/user/requirements.txt.

Ou, à partir de votre ordinateur, créez et ouvrez le fichier ~/src/odoo-
addons/requirements.txt.

Ajoutez

    
    
    unidecode
    

Utilisez ensuite la bibliothèque dans votre module, par exemple pour supprimer
les accents des caractères dans le champ du nom de votre modèle.

Ouvrez le fichier _models/models.py_.

Avant

    
    
    from odoo import models, fields, api
    

Ajoutez

    
    
    from unidecode import unidecode
    

Après

    
    
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    

Ajoutez

    
    
    @api.model
    def create(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).create(values)
    
    def write(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).write(values)
    

L’ajout d’une dépendance Python nécessite une montée de la version du module
pour que la plateforme puisse l’installer.

Modifiez le manifeste du module ___manifest__.py_

Remplacer

    
    
    'version': '0.2',
    

par

    
    
    'version': '0.3',
    

Phasez et validez vos changements :

    
    
    $ git add requirements.txt
    $ git add my_module
    $ git commit -m "[IMP] my_module: automatically remove special chars in my_module.my_module name field"
    

Ensuite, poussez vos changements :

Dans un terminal Konvergo ERP.sh :

    
    
    $ git push https HEAD:feature-1
    

Dans le terminal de votre ordinateur :

    
    
    $ git push
    

