# Paramètres

## Vue d’ensemble

Les paramètres vous permettent de gérer la configuration de votre projet.

![../../../_images/interface-settings.png](../../../_images/interface-
settings.png)

## Nom du projet

Le nom de votre projet.

![../../../_images/interface-settings-
projectname.png](../../../_images/interface-settings-projectname.png)

Ceci définit l’adresse qui sera utilisée pour accéder à votre base de données
de production.

Les adresses de vos builds de simulation et de développement sont dérivées de
ce nom et sont assignées automatiquement. Cependant, lorsque vous changez le
nom du projet, seuls les builds futurs utiliseront le nouveau nom.

## Collaborateurs

Gérez les utilisateurs de Github qui ont accès à votre projet.

![../../../_images/interface-settings-
collaborators.png](../../../_images/interface-settings-collaborators.png)

Il y a deux niveaux d’utilisateurs :

  * Admin : a accès à toutes les fonctionnalités d’Odoo.sh.

  * Utilisateur : n’a pas accès aux paramètres du projet, ni aux bases de données de production et de simulation.

Le groupe d’utilisateurs est destiné aux développeurs qui peuvent apporter des
modifications à votre code, mais ne sont pas autorisés à accéder aux données
de production. Les utilisateurs de ce groupe ne peuvent pas se connecter aux
bases de données de production et de simulation à l’aide de la fonctionnalité
_1-click connect_ , mais ils peuvent bien évidemment utiliser leur compte
habituel sur ces bases de données, s’ils en ont, en utilisant leurs
identifiants habituels.

De plus, ils ne peuvent pas utiliser le webshell et n’ont pas accès aux
journaux du serveur.

|  | Utilisateur | Admin  
---|---|---|---  
Développement | Historique | ● | ●  
| 1-click connect | ● | ●  
| Journaux | ● | ●  
| Shell/SSH | ● | ●  
| Emails | ● | ●  
| Mettre à niveau | ● | ●  
| Paramètres | ● | ●  
Production & Simulation | Historique | ● | ●  
| 1-click connect |  | ●  
| Journaux |  | ●  
| Shell/SSH |  | ●  
| Emails |  | ●  
| Monitoring |  | ●  
| Sauvegardes |  | ●  
| Mettre à niveau |  | ●  
| Paramètres | ●* | ●  
Statut |  | ● | ●  
Paramètres |  |  | ●  
  
Note

* Uniquement dans les branches de simulation

## Accès public

Autorisez l’accès public à vos builds de développement.

![../../../_images/interface-settings-public.png](../../../_images/interface-
settings-public.png)

Si cette option est activée, elle expose la page Builds publiquement,
permettant aux visiteurs de se connecter à vos builds de développement.

De plus, les visiteurs ont accès aux journaux, au shell et aux emails de vos
builds de développement.

Les builds de production et de simulation sont exclus, les visiteurs peuvent
uniquement voir leur statut.

## Domaines personnalisés

Pour configurer des domaines additionnels, veuillez aller à l”[onglet des
paramètres](branches.html#odoosh-gettingstarted-branches-tabs-settings) de la
branche correspondante.

## Sous-modules

Configurez les clés de déploiement pour les dépôts privés que vous utilisez
comme sous-modules dans vos branches pour permettre à Odoo.sh de les
télécharger.

Avertissement

Ces paramètres sont uniquement requis pour les **dépôts privés**. Si vous
cherchez à savoir comment configurer vos sous-modules, vous trouverez des
instructions dans le chapitre [Sous-
modules](../advanced/submodules.html#odoosh-advanced-submodules) de cette
documentation.

![../../../_images/interface-settings-
submodules.png](../../../_images/interface-settings-submodules.png)

Lorsqu’un dépôt est privé, il n’est pas possible de télécharger publiquement
ses branches et révisions. Pour cette raison, vous devez configurer une clé de
déploiement pour Odoo.sh, pour que le serveur Git distant permette à notre
plateforme de télécharger les révisions de ce dépôt privé.

Pour configurer la clé de déploiement pour un dépôt privé, procédez comme suit
:

  * dans le champ, collez l’URL SSH de votre sous-dépôt privé et cliquez sur _Add_ ,

    * par ex. _git@github.com:USERNAME/REPOSITORY.git_

    * il peut s’agir d’un autre serveur Git que Github, tel que Bitbucket, Gitlab ou même votre propre serveur auto-hébergé

  * copiez la clé publique,

    * elle devrait ressembler à _ssh-rsa some…random…characters…here…==_

  * dans les paramètres du sous-dépôt privé, ajoutez la clé publique aux clés de déploiement.

    * Github.com : Settings ‣ Deploy keys ‣ Add deploy key

    * Bitbucket.com : Settings ‣ Access keys ‣ Add key

    * Gitlab.com : Settings ‣ Repository ‣ Deploy Keys

    * Auto-hébergé : ajoutez la clé au fichier authorized_keys de l’utilisateur git dans son répertoire .ssh

## Taille de stockage

Cette section présente la taille de stockage utilisée par votre projet.

![../../../_images/interface-settings-storage.png](../../../_images/interface-
settings-storage.png)

La taille de stockage est calculée comme suit :

  * la taille de la base de données PostgreSQL

  * la taille des fichiers disques disponibles dans votre conteneur : filestore de la base de données, répertoire de stockage des sessions, …

Avertissement

Si vous voulez analyser l’utilisateur du disque, vous pouvez exécuter l’outil
[ncdu](https://dev.yorhel.nl/ncdu/man) dans votre Web Shell.

Si la taille de votre base de données de production dépasse ce qui est prévu
dans votre abonnement, elle sera automatiquement synchronisée avec celui-ci.

## Workers de base de données

Il est possible de configurer des workers de base de données supplémentaires
ici. Un plus grand nombre de workers permet d’augmenter la charge que votre
base de données de production est en mesure de gérer. Si vous en ajoutez, ils
seront automatiquement synchronisés avec votre abonnement.

![../../../_images/interface-settings-workers.png](../../../_images/interface-
settings-workers.png)

Avertissement

L’ajout de workers ne résoudra pas par magie tous les problèmes de
performance. Cela permet au serveur de gérer plus de connexions en même temps.
Si certaines opérations sont anormalement lentes, il s’agit probablement d’un
problème de code. Si ce n’est pas dû à vos propres personnalisations, vous
pouvez ouvrir un ticket [ici](https://www.odoo.com/help).

## Branches de simulation

Des branches de simulation supplémentaires vous permettent de développer et de
tester plus de fonctionnalités en même temps. Si vous en ajoutez, elles seront
automatiquement synchronisées avec votre abonnement.

![../../../_images/interface-settings-staging-
branches.png](../../../_images/interface-settings-staging-branches.png)

## Activation

Présente le statut d’activation du projet. Vous pouvez changer le code
d’activation du projet si nécessaire.

![../../../_images/interface-settings-
activation.png](../../../_images/interface-settings-activation.png)

