# Sous-modules

## Vue d’ensemble

Un [sous-module Git](https://git-scm.com/book/en/v2/Git-Tools-Submodules) vous
permet d’intégrer d’autres projets Git dans votre code, sans avoir à copier-
coller tout leur code.

En effet, vos modules personnalisés peuvent dépendre des modules provenant
d’autres dépôts. En ce qui concerne Konvergo ERP, cette fonctionnalité vous permet
d’ajouter des modules à partir d’autres dépôts Git dans les branches de votre
dépôt. L’ajout de ces dépendances de votre branche par le biais de sous-
modules facilite le déploiement de votre code et de vos serveurs, car vous
pouvez cloner les dépôts ajoutés en tant que sous-modules en même temps que
vous clonez votre propre dépôt.

En outre, vous pouvez choisir la branche du dépôt ajouté en tant que sous-
module et vous pouvez décider de la révision que vous voulez. C’est à vous de
décider si vous voulez épingler le sous-module à une révision spécifique et
quand vous voulez mettre à jour vers une révision plus récente.

Dans Konvergo ERP.sh, les sous-modules vous permettent d’utiliser et de dépendre de
modules disponibles dans d’autres dépôts. La plateforme détectera que vous
avez ajouté des modules par le biais de sous-modules dans vos branches et les
ajoutera automatiquement à votre chemin d’accès aux modules complémentaires
pour que vous puissiez les installer dans vos bases de données.

Si vous ajoutez des dépôts privés en tant que sous-modules dans vos branches,
vous devez configurer une clé de déploiement dans les paramètres de votre
projet Konvergo ERP.sh. Sinon, Konvergo ERP.sh ne sera pas autorisé à les télécharger. La
procédure est détaillée dans le chapitre [Paramètres > Sous-
modules](../getting_started/settings#odoosh-gettingstarted-settings-
submodules).

## Ajouter un sous-module

### Avec Konvergo ERP.sh (facile)

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Pour l’instant, cette méthode ne permet pas d’ajouter des dépôts <b>privés</b>. Vous pouvez toutefois le faire <a href="#odoosh-advanced-submodules-withgit"><span class="std std-ref">avec Git</span></a>.</p>
</div>

Sur Konvergo ERP.sh, dans la vue branches de votre projet, choisissez la branche dans
laquelle vous voulez ajouter un sous-module.

Dans le coin supérieur droit, cliquez sur le bouton _Submodule_ et ensuite sur
_Run_.

![../../../_images/advanced-submodules-button.png](../../../_images/advanced-
submodules-button.png)

Une fenêtre contextuelle contenant un formulaire s’affiche. Complétez les
champs comme suit :

  * Repository URL : L’URL SSH du dépôt.

  * Branch : La branche que vous voulez utiliser.

  * Path : Le dossier dans lequel vous voulez ajouter ce sous-module dans votre branche.

![../../../_images/advanced-submodules-dialog.png](../../../_images/advanced-
submodules-dialog.png)

Sur Github, vous pouvez obtenir l’URL du dépôt en cliquant sur le bouton
_Clone or download_ du dépôt. Assurez-vous d” _utiliser SSH_.

![../../../_images/advanced-submodules-github-
sshurl.png](../../../_images/advanced-submodules-github-sshurl.png)

### Avec Git (avancé)

Dans un terminal, dans le dossier où votre dépôt Git est cloné, procédez au
checkout de la branche dans laquelle vous voulez ajouter un sous-module :

    
    
    $ git checkout <branch>
    

Ensuite, ajoutez le sous-module en utilisant la commande suivante :

    
    
    $ git submodule add -b <branch> <git@yourprovider.com>:<username/repository.git> <path>
    

Remplacer

  * _< git@yourprovider.com>:<username/repository.git>_ par l’URL SSH du dépôt que vous voulez ajouter en tant que sous-module,

  * _< branch>_ par la branche que vous voulez utiliser dans le dépôt susmentionné.

  * _< path>_ par le dossier dans lequel vous voulez ajouter ce sous-module.

Commiter et pousser vos changements :

    
    
    $ git commit -a && git push -u <remote> <branch>
    

Remplacer

  * <remote> par le dépôt vers lequel vous voulez pousser vos changements. Pour une configuration Git standard, il s’agit de _origin_.

  * <branch> par la branche vers laquelle vous voulez pousser vos changements. Plus probablement la branche sur laquelle vous avez utilisez `git checkout` dans la première étape.

Vous pouvez lire la [documentation git-scm.com](https://git-
scm.com/book/en/v2/Git-Tools-Submodules) pour plus d’informations sur les
sous-modules Git. Par exemple, si vous voulez mettre à jour vos sous-modules
pour avoir leur dernière version révisée, vous pouvez suivre le chapitre
[Pulling in Upstream changes](https://git-scm.com/book/en/v2/Git-Tools-
Submodules#_pulling_in_upstream_changes_from_the_submodule_remote).

## Ignorer des modules

Si vous ajoutez un dépôt qui contient un grand nombre de modules, il se peut
que vous vouliez en ignorer certains au cas où il y en aurait qui sont
installés automatiquement. Pour ce faire, vous pouvez préfixer votre dossier
de sous-module avec un `.`. La plateforme ignorera ce dossier et vous pouvez
sélectionner vos modules manuellement en créant des liens symboliques vers
ceux-ci depuis un autre dossier.

