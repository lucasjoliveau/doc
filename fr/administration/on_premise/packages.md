# Programmes d’installation

Odoo fournit des programmes d’installation pour les distributions Linux basées
sur Debian (Debian, Ubuntu, etc.), les distributions Linux basées sur RPM
(Fedora, CentOS, RHEL, etc.) et Windows pour les versions Community et
Enterprise.

Les packages nightly **Community** officiels avec toutes les dépendances
nécessaires sont disponibles sur le [serveur
nightly](https://nightly.odoo.com).

Note

Les packages nightly peuvent être difficiles à maintenir à jour.

Les packages **Community** et **Enterprise** officiels peuvent être
téléchargés à partir de la [page de téléchargement
d’Odoo](https://www.odoo.com/page/download).

Note

It is required to be logged in as a paying on-premise customer or partner to
download the Enterprise packages.

## Linux

### Préparation

Odoo a besoin d’un serveur [PostgreSQL](https://www.postgresql.org/) pour
fonctionner correctement.

Debian/UbuntuFedora

La configuration par défaut pour le package “deb” d’Odoo est d’utiliser le
serveur PostgreSQL sur le même hôte que l’instance Odoo. Exécutez la commande
suivante afin d’installer le serveur PostgreSQL :

    
    
    $ sudo apt install postgresql -y
    

Assurez-vous que la commande `sudo` est disponible et configurée correctement,
puis exécutez la commande suivante pour installer le serveur PostgreSQL :

    
    
    $ sudo dnf install -y postgresql-server
    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    

Avertissement

`wkhtmltopdf` n’est pas installé par **pip** et doit être installé
manuellement dans la [version
0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) pour
qu’il prenne en charge les en-têtes et les pieds de page. Consultez la
[wkhtmltopdf wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) pour plus de
détails sur les différentes versions.

### Dépôt

Odoo S.A. fournit un dépôt qui peut être utilisé pour installer l’édition
**Community** en exécutant les commandes suivantes :

Debian/UbuntuFedora

    
    
    $ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
    $ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/16.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
    $ sudo apt-get update && sudo apt-get install odoo
    

Utilisez la commande habituelle `apt-get upgrade` pour maintenir
l’installation à jour.

    
    
    $ sudo dnf config-manager --add-repo=https://nightly.odoo.com/16.0/nightly/rpm/odoo.repo
    $ sudo dnf install -y odoo
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

Note

Pour l’instant, il n’y a pas de dépôt nightly pour l’édition Enterprise.

### Package de distribution

Au lieu d’utiliser le dépôt, les packages pour les éditions **Community** et
**Enterprise** peuvent être téléchargés à partir de la [page de téléchargement
d’Odoo](https://www.odoo.com/page/download).

Debian/UbuntuFedora

Note

Le package “deb” d’Odoo 16 est actuellement compatible avec [Debian
Buster](https://www.debian.org/releases/buster/) et [Ubuntu
18.04](https://releases.ubuntu.com/18.04) ou supérieur.

Une fois le package téléchargé, exécutez les commandes suivantes **en tant que
racine** pour installer Odoo en tant que service, créer l’utilisateur
PostgreSQL et automatiquement démarrer le serveur :

    
    
    # dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
    # apt-get install -f # should install the missing dependencies
    # dpkg -i <path_to_installation_package>
    

Avertissement

  * Le package Debian `python3-xlwt`, nécessaire pour exporter au format XLS, n’existe pas en Debian Buster ni dans Ubuntu 18.04. Si nécessaire, installez-le manuellement avec ce qui suit :
    
        $ sudo pip3 install xlwt
    

  * Le package Python `num2words` \- nécessaire au rendu des montants textuels - n’existe pas dans Debian Buster ni dans Ubuntu 18.04, ce qui pourrait causer des problèmes avec le module `l10n_mx_edi`. Si nécessaire, installez-le manuellement avec ce qui suit :
    
        $ sudo pip3 install num2words
    

Note

Le package “rpm” d’Odoo 16 est compatible avec Fedora 36.

Une fois téléchargé, le package peut être installé en utilisant le
gestionnaire de paquets “dnf” :

    
    
    $ sudo dnf localinstall odoo_16.0.latest.noarch.rpm
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

## Windows

> Avertissement
>
> La version Windows est proposée pour faciliter les tests ou l’exécution
> d’instances locales pour un seul utilisateur, mais le déploiement en
> production est déconseillé en raison d’un nombre de limitations et de
> risques associés au déploiement d’Odoo sur une plateforme Windows.

  1. Téléchargez le programme d’installation depuis le [serveur nightly](https://nightly.odoo.com) (Community uniquement) ou le programme d’installation Windows depuis la [page de téléchargement d’Odoo](https://www.odoo.com/page/download) (toutes les éditions).

  2. Exécutez le fichier téléchargé.

Avertissement

Sur Windows 8 et les versions ultérieures, un avertissement intitulé _Windows
a protégé votre PC_ pourrait s’afficher. Cliquez sur **Informations
complémentaires** et ensuite sur **Exécuter quand même** pour continuer.

  3. Acceptez l’invitation [UAC](https://fr.wikipedia.org/wiki/User_Account_Control)

  4. Suivez les étapes d’installation.

Odoo démarre automatiquement à la fin de l’installation.

