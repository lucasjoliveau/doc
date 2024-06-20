# Plugin Gmail

Le _Plugin Gmail_ connecte une base de données Odoo à une boîte de messagerie
Gmail, de sorte que les utilisateurs peuvent garder une trace de tout leur
travail entre Gmail et Odoo, sans perdre aucune information.

## Utilisateurs d’Odoo Online

Pour les bases de données hébergées sur Odoo Online (ou Odoo.sh), suivez les
étapes ci-dessous pour configurer le plugin Gmail.

### Installer le plugin Gmail

Tout d’abord, connectez-vous au compte Gmail que l’utilisateur souhaite
connecter à Odoo.

À partir de la boîte de réception Gmail, cliquez sur l’icône du signe plus
dans le panneau latéral droit pour accéder aux modules complémentaires. Si le
panneau latéral n’est pas visible, cliquez sur l’icône en forme de flèche dans
le coin inférieur droit de la boîte de réception pour le faire apparaître.

![Icône du signe plus dans le panneau latéral de la boîte de réception
Gmail.](../../../../_images/gmail-side-panel.png)

Ensuite, tapez `Odoo` dans la barre de recherche et trouvez Odoo Inbox Addin.

![Odoo Inbox Addin dans Google Workspace
Marketplace.](../../../../_images/google-workspace-marketplace.png)

Vous pouvez également vous rendre directement sur la page Odoo Inbox Addin sur
[Google Workspace
Marketplace](https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275).

Une fois que vous avez trouvé le plugin, cliquez sur Installer et ensuite sur
Continuer pour commencer l’installation.

Ensuite, sélectionnez le compte Gmail que l’utilisateur souhaite connecter à
Odoo. Cliquez sur Autoriser pour permettre à Odoo d’accéder au compte Google.
Google affichera alors une fenêtre contextuelle confirmant que l’installation
a réussi.

### Configurer la base de données Odoo

La fonctionnalité Plugin de messagerie doit être activée dans la base de
données Odoo afin d’utiliser le plugin Gmail. Pour activer la fonctionnalité,
allez aux Paramètres ‣ Paramètres généraux. Sous la section Intégrations,
activez Plugin de messagerie et cliquez ensuite sur Enregistrer.

![La fonctionnalité Plugin de messagerie dans les
paramètres.](../../../../_images/mail-plugin-setting.png)

### Configurer la boîte de réception Gmail

Dans la boîte de réception Gmail, une icône Odoo mauve est à présent visible
dans le panneau de droite. Cliquez sur l’icône Odoo pour ouvrir la fenêtre du
plugin Odoo. Sélectionnez ensuite n’importe quel email dans la boîte de
réception. Cliquez sur Autoriser l’accès dans la fenêtre du plugin pour
accorder à Odoo l’accès à la boîte de réception Gmail.

![Le bouton Autoriser l'accès dans la barre latérale droite du panneau de
plugin Odoo.](../../../../_images/authorize-access.png)

Ensuite, cliquez sur Connexion, saisissez l’URL de la base de données Odoo que
l’utilisateur souhaite connecter à la boîte de messagerie Gmail et connectez-
vous à la base de données.

Note

Utilisez l’URL générale pour la base de données et pas l’URL d’une page
spécifique de la base de données. Par exemple, utilisez
`https://mycompany.odoo.com`, au lieu de
`https://mycompany.odoo.com/web#cids=1&action=menu`.

Enfin, cliquez sur Autoriser pour permettre à Gmail d’accéder à la base de
données Odoo. Le navigateur affichera ensuite un message Success!. Fermez
ensuite la fenêtre. La boîte de réception Gmail et la base de données Odoo
sont à présent connectées.

## Utilisateurs d’Odoo On-Premise

Pour les bases de données hébergées sur serveur autres que Odoo Online (ou
Odoo.sh), suivez les étapes ci-dessous pour configurer le plugin Gmail.

Note

Dans le cadre de ses lignes directrices en matière de sécurité, Odoo demande
aux créateurs de modules complémentaires de fournir une liste des URL pouvant
être utilisées dans les actions et les redirections lancées par le module
complémentaire. Ceci permet de protéger les utilisateurs en garantissant, par
exemple, qu’aucun module complémentaire ne les redirige vers un site web
malveillant. (En savoir plus sur [Google Apps
Script](https://developers.google.com/apps-script/manifest/allowlist-url).)

Étant donné que Odoo ne peut répertorier que le domaine `odoo.com` et non le
domaine unique du serveur de chaque client sur serveur, les clients sur
serveur ne peuvent pas installer le plugin Gmail à partir de Google Workspace
Marketplace.

### Installer le plugin Gmail

Tout d’abord, accédez au [répertoire GitHub](https://github.com/odoo/mail-
client-extensions) pour les Plugins de messagerie Odoo. Ensuite, cliquez sur
le bouton vert Code et sur Download ZIP pour télécharger les fichiers du
plugin de messagerie sur l’ordinateur de l’utilisateur.

![Téléchargez le fichier ZIP à partir du répositoire GitHub d'Odoo pour les
plugins de messagerie.](../../../../_images/gh-download-zip.png)

Ouvez le fichier ZIP sur l’ordinateur. Allez ensuite à mail-client-extensions-
master ‣ gmail ‣ src ‣ views, et ouvrez le fichier `login.ts` à l’aide d’un
éditeur de texte, tel que Notepad (Windows), TextEdit (Mac) ou Visual Studio
Code.

Supprimez les trois lignes de texte suivantes du fichier `login.ts` :

    
    
    if (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
         return notify("The URL must be a subdomain of odoo.com");
    }
    

Ceci supprime la contrainte du domaine `odoo.com` dans le programme plugin
Gmail.

Ensuite, dans le fichier ZIP, allez à mail-client-extensions-master ‣ gmail et
ouvrez le fichier intitulé appsscript.json. Dans la section urlFetchWhitelist,
remplacez toutes les références à `odoo.com` avec le domaine du serveur unique
du client Odoo.

Ensuite, dans le même fichier gmail, ouvrez le fichier intitulé README.md.
Suivez les instructions dans le fichier README.md pour pousser les fichiers
Gmail Plugin en tant que projet Google.

Note

L’ordinateur doit être en mesure d’exécuter des commandes Linux afin de suivre
les instructions du fichier README.md.

Ensuite, partagez le projet Google avec le compte Gmail que l’utilisateur
souhaite connecter à Odoo. Cliquez sur Publish (Publier) et Deploy from
manifest (Déployer à partir du fichier manifeste). Enfin, cliquez sur Install
the add-on pour installer le plugin Gmail.

### Configurer la base de données Odoo

La fonctionnalité Plugin de messagerie doit être activée dans la base de
données Odoo afin d’utiliser le plugin Gmail. Pour activer la fonctionnalité,
allez aux Paramètres ‣ Paramètres généraux. Sous la section Intégrations,
activez Plugin de messagerie et cliquez ensuite sur Enregistrer.

![La fonctionnalité Plugin de messagerie dans les
paramètres.](../../../../_images/mail-plugin-setting.png)

### Configurer la boîte de réception Gmail

Dans la boîte de réception Gmail, une icône Odoo mauve est à présent visible
dans le panneau de droite. Cliquez sur l’icône Odoo pour ouvrir la fenêtre du
plugin Odoo. Sélectionnez ensuite n’importe quel email dans la boîte de
réception. Cliquez sur Autoriser l’accès dans la fenêtre du plugin pour
accorder à Odoo l’accès à la boîte de réception Gmail.

![Le bouton Autoriser l'accès dans la barre latérale droite du panneau de
plugin Odoo.](../../../../_images/authorize-access.png)

Ensuite, cliquez sur Connexion, saisissez l’URL de la base de données Odoo que
l’utilisateur souhaite connecter à la boîte de messagerie Gmail et connectez-
vous à la base de données.

Note

Utilisez l’URL générale pour la base de données et pas l’URL d’une page
spécifique de la base de données. Par exemple, utilisez
`https://mycompany.odoo.com`, au lieu de
`https://mycompany.odoo.com/web#cids=1&action=menu`.

Enfin, cliquez sur Autoriser pour permettre à Gmail d’accéder à la base de
données Odoo. Le navigateur affichera ensuite un message Success!. Fermez
ensuite la fenêtre. La boîte de réception Gmail et la base de données Odoo
sont à présent connectées.

