# Mises à jour des corrections de bugs

## Introduction

Pour bénéficier des dernières améliorations, des correctifs de sécurité, des
corrections de bugs et des performances accrues, vous pouvez avoir besoin de
mettre à jour votre installation Odoo de temps en temps.

Ce guide ne s’applique que si vous utilisez Odoo sur votre propre
infrastructure d’hébergement. Si vous utilisez une des solutions Odoo Cloud,
les mises à jour sont automatiquement effectuées pour vous.

La terminologie concernant les mises à jour de logiciels est souvent confuse,
voici donc quelques définitions préliminaires :

Mettre à jour (une installation Odoo)

    

Se réfère au processus d’obtention de la dernière révision du code source de
votre édition Odoo actuelle. Par exemple, la mise à jour de votre Odoo
Enterprise 13.0 vers la dernière révision. Cela n’entraîne pas directement des
changements dans le contenu de votre base de données Odoo et peut être annulé
en réinstallant la révision précédente du code source.

Mettre à niveau (une base de données Odoo)

    

Se réfère à une opération complexe de traitement des données au cours de
laquelle la structure et les contenus de votre base de données sont modifiés
de manière permanente pour les rendre compatibles avec une nouvelle version
d’Odoo. Cette opération est irréversible et généralement réalisée via le
[service de mise à niveau des bases de données](https://upgrade.odoo.com)
d’Odoo, lorsque vous décidez de passer à une version plus récente d’Odoo.
Historiquement, ce processus est également appelée une « migration », parce
qu’il implique le déplacement des données au sein de la base de données, même
si la base de données peut se retrouver au même emplacement physique après la
mise à niveau.

Cette page décrit les étapes habituelles nécessaires pour _mettre à jour_ une
installation Odoo vers la dernière version. Si vous voulez avoir plus
d’informations sur la mise à niveau d’une base de données, veuillez plutôt
consulter la [page de mise à niveau d’Odoo](https://upgrade.odoo.com).

## En bref

La mise à jour d’Odoo se fait en réinstallant simplement la dernière version
de votre édition d’Odoo par-dessus de votre installation actuelle. Cela
préservera vos données sans aucune altération, tant que vous ne désinstallez
pas PostgreSQL (le moteur de base de données fourni avec Odoo).

The main reference for updating is logically our [installation
guide](../on_premise.html), which explains the common installation methods.

La mise à jour est également mieux réalisée par la personne qui a déployé Odoo
initialement, car la procédure est très similaire.

Note

Nous recommandons toujours de télécharger une nouvelle version complète et
actualisée d’Odoo, plutôt que d’appliquer manuellement des correctifs, tels
que les correctifs de sécurité qui accompagnent les Avis de sécurité. Les
correctifs sont principalement fournis pour les installations qui sont
fortement personnalisées, ou pour le personnel technique qui préfère appliquer
temporairement des changements minimes tout en testant une mise à jour
complète.

## Étape 1 : Télécharger une version actualisée d’Odoo

La page centrale de téléchargement est <https://www.odoo.com/page/download>.
Si vous voyez un lien « Acheter » pour le téléchargement d’Odoo Enterprise,
assurez-vous que vous êtes connecté à Odoo.com avec le même identifiant que
celui lié à votre abonnement Odoo Enterprise.

Vous pouvez également utiliser le lien de téléchargement unique qui figure
dans votre email de confirmation d’achat d’Odoo Enterprise.

Note

Le téléchargement d’une version actualisée n’est pas nécessaire si vous l’avez
installé via Github (voir ci-dessous).

## Étape 2 : Faire une sauvegarde de votre base de données

La procédure de mise à jour est assez sûre et ne devrait pas altérer vos
données. Cependant, il est toujours recommandé de faire une sauvegarde
complète avant d’effectuer tout changement sur votre installation et de la
stocker dans un endroit sûr, sur un autre ordinateur.

Si vous n’avez pas désactivé l’écran de gestionnaire de bases de données
(voyez [ici](deploy.html#security) pourquoi vous devriez le faire), vous
pouvez l’utiliser (lien en bas de l’écran de sélection de votre base de
données) pour télécharger une sauvegarde de votre ou vos bases de données. Si
vous l’avez désactivé, utilisez la même procédure que pour vos sauvegardes
habituelles.

## Étape 3 : Installer la version actualisée

Choisissez la méthode qui correspond à votre installation actuelle :

### Programmes d’installation

Si vous avez installé Odoo avec un programme d’installation téléchargé sur
notre site web (la méthode recommandée), la mise à jour est très simple. Tout
ce que vous avez à faire est de télécharger le programme d’installation
correspondant à votre système (voir étape #1) et de l’installer sur votre
serveur. Ils sont mis à jour quotidiennement et comprennent les derniers
correctifs de sécurité. En général, il suffit de double-cliquer sur le
programme pour l’installer par-dessus de votre installation actuelle. Après
avoir installé le programme, veillez à redémarrer le service Odoo ou votre
serveur et ça y est.

### Installation de la source (Tarball)

Si vous avez initialement installé Odoo avec la version « tarball » (archive
du code source), vous devez remplacer le répertoire de l’installation par une
version plus récente. Téléchargez d’abord la dernière version de l’archive
tarball sur Odoo.com. Ils sont mis à jour quotidiennement et comprennent les
derniers correctifs de sécurité (voir étape #1). Après avoir téléchargé le
programme, extrayez-le dans un emplacement temporaire sur votre serveur.

Vous obtiendrez un dossier libelé avec la version du code source, par exemple
« odoo-13.0+e.20190719 », qui contient un dossier « odoo.egg-info » et le
dossier du code source réel intitulé « odoo » (pour Odoo 10 et les versions
ultérieures) ou « openerp » (pour les versions plus anciennes). Vous pouvez
ignorer le dossier odoo.egg-info. Localisez le dossier dans lequel votre
installation actuelle est déployée et remplacez-le par le dossier « odoo » ou
« openerp » plus récent qui se trouvait dans l’archive que vous venez
d’extraire.

Veillez à respecter la disposition des dossiers, par exemple le nouveau
dossier « modules complémentaires » inclus dans le code source doit se trouver
exactement au même endroit qu’auparavant. Ensuite, faites attention aux
fichiers de configuration que vous avez pu copier ou modifier manuellement
dans l’ancien dossier et copiez-les par-dessus le nouveau dossier. Enfin,
redémarrez le service Odoo ou le serveur et ça y est.

### Installation de la source (Github)

Si vous avez initialement installé Odoo avec un clone Github complet des
dépôts officiels, la procédure de mise à jour nécessite que vous tiriez le
dernier code source via git. Entrez dans le répertoire de chaque dépôt (le
dépôt principal d’Odoo et le dépôt Enterprise), et exécutez les commandes
suivantes :

    
    
    git fetch
    git rebase --autostash
    

La dernière commande peut rencontrer des conflits de code source si vous avez
édité le code source d’Odoo localement. Le message d’erreur vous donnera la
liste des fichiers présentant des conflits et vous devrez résoudre les
conflits manuellement, en les éditant et en décidant quelle partie du code
vous voulez conserver.

Si vous préférez simplement ignorer les modifications présentant un conflit et
restaurer la version officielle, vous pouvez utiliser la commande suivante :

    
    
    git reset --hard
    

Enfin, redémarrez le service Odoo ou le serveur et ça y est.

### Docker

Veuillez consulter notre [documentation sur les images
Docker](https://hub.docker.com/_/odoo/) pour des instructions de mise à jour
spécifiques.

