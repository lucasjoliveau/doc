# Programmes d’installation

Konvergo ERP fournit des programmes d’installation pour les distributions Linux basées
sur Debian (Debian, Ubuntu, etc.), les distributions Linux basées sur RPM
(Fedora, CentOS, RHEL, etc.) et Windows pour les versions Community et
Enterprise.

Les packages nightly **Community** officiels avec toutes les dépendances
nécessaires sont disponibles sur le [serveur
nightly](https://nightly.odoo.com).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les packages nightly peuvent être difficiles à maintenir à jour.</p>
</div>

Les packages **Community** et **Enterprise** officiels peuvent être
téléchargés à partir de la [page de téléchargement
d’Konvergo ERP](https://www.odoo.com/page/download).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is required to be logged in as a paying on-premise customer or partner to download the
Enterprise packages.</p>
</div>

## Linux

### Préparation

Konvergo ERP a besoin d’un serveur [PostgreSQL](https://www.postgresql.org/) pour
fonctionner correctement.

Debian/UbuntuFedora

La configuration par défaut pour le package “deb” d’Konvergo ERP est d’utiliser le
serveur PostgreSQL sur le même hôte que l’instance Konvergo ERP. Exécutez la commande
suivante afin d’installer le serveur PostgreSQL :

    
    
    $ sudo apt install postgresql -y
    

Assurez-vous que la commande `sudo` est disponible et configurée correctement,
puis exécutez la commande suivante pour installer le serveur PostgreSQL :

    
    
    $ sudo dnf install -y postgresql-server
    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p><code>wkhtmltopdf</code> n’est pas installé par <b>pip</b> et doit être installé manuellement dans la <a href="https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3">version 0.12.6</a> pour qu’il prenne en charge les en-têtes et les pieds de page. Consultez la <a href="https://github.com/odoo/odoo/wiki/Wkhtmltopdf">wkhtmltopdf wiki</a> pour plus de détails sur les différentes versions.</p>
</div>

### Dépôt

Konvergo ERP S.A. fournit un dépôt qui peut être utilisé pour installer l’édition
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
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour l’instant, il n’y a pas de dépôt nightly pour l’édition Enterprise.</p>
</div>

### Package de distribution

Au lieu d’utiliser le dépôt, les packages pour les éditions **Community** et
**Enterprise** peuvent être téléchargés à partir de la [page de téléchargement
d’Konvergo ERP](https://www.odoo.com/page/download).

Debian/UbuntuFedora

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le package “deb” d’Konvergo ERP 16 est actuellement compatible avec <a href="https://www.debian.org/releases/buster/">Debian Buster</a> et <a href="https://releases.ubuntu.com/18.04">Ubuntu 18.04</a> ou supérieur.</p>
</div>

Une fois le package téléchargé, exécutez les commandes suivantes **en tant que
racine** pour installer Konvergo ERP en tant que service, créer l’utilisateur
PostgreSQL et automatiquement démarrer le serveur :

    
    
    # dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
    # apt-get install -f # should install the missing dependencies
    # dpkg -i <path_to_installation_package>
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><ul>
<li><p>Le package Debian <code>python3-xlwt</code>, nécessaire pour exporter au format XLS, n’existe pas en Debian Buster ni dans Ubuntu 18.04. Si nécessaire, installez-le manuellement avec ce qui suit :</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install xlwt
</pre></div>
</div>
</li>
<li><p>Le package Python <code>num2words</code> - nécessaire au rendu des montants textuels - n’existe pas dans Debian Buster ni dans Ubuntu 18.04, ce qui pourrait causer des problèmes avec le module <code>l10n_mx_edi</code>. Si nécessaire, installez-le manuellement avec ce qui suit :</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> sudo pip3 install num2words
</pre></div>
</div>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le package “rpm” d’Konvergo ERP 16 est compatible avec Fedora 36.</p>
</div>

Une fois téléchargé, le package peut être installé en utilisant le
gestionnaire de paquets “dnf” :

    
    
    $ sudo dnf localinstall odoo_16.0.latest.noarch.rpm
    $ sudo systemctl enable odoo
    $ sudo systemctl start odoo
    

## Windows

> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>La version Windows est proposée pour faciliter les tests ou l’exécution d’instances locales pour un seul utilisateur, mais le déploiement en production est déconseillé en raison d’un nombre de limitations et de risques associés au déploiement d’Konvergo ERP sur une plateforme Windows.</p>
</div>

  1. Téléchargez le programme d’installation depuis le [serveur nightly](https://nightly.odoo.com) (Community uniquement) ou le programme d’installation Windows depuis la [page de téléchargement d’Konvergo ERP](https://www.odoo.com/page/download) (toutes les éditions).

  2. Exécutez le fichier téléchargé.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Sur Windows 8 et les versions ultérieures, un avertissement intitulé <em>Windows a protégé votre PC</em> pourrait s’afficher. Cliquez sur <b>Informations complémentaires</b> et ensuite sur <b>Exécuter quand même</b> pour continuer.</p>
</div>

  3. Acceptez l’invitation [UAC](https://fr.wikipedia.org/wiki/User_Account_Control)

  4. Suivez les étapes d’installation.

Konvergo ERP démarre automatiquement à la fin de l’installation.

