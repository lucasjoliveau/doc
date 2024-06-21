# Plugin Gmail

Le _Plugin Gmail_ connecte une base de données Konvergo ERP à une boîte de messagerie
Gmail, de sorte que les utilisateurs peuvent garder une trace de tout leur
travail entre Gmail et Konvergo ERP, sans perdre aucune information.

## Utilisateurs d’Konvergo ERP Online

Pour les bases de données hébergées sur Konvergo ERP Online (ou Konvergo ERP.sh), suivez les
étapes ci-dessous pour configurer le plugin Gmail.

### Installer le plugin Gmail

Tout d’abord, connectez-vous au compte Gmail que l’utilisateur souhaite
connecter à Konvergo ERP.

À partir de la boîte de réception Gmail, cliquez sur l’icône du signe plus
dans le panneau latéral droit pour accéder aux modules complémentaires. Si le
panneau latéral n’est pas visible, cliquez sur l’icône en forme de flèche dans
le coin inférieur droit de la boîte de réception pour le faire apparaître.

![Icône du signe plus dans le panneau latéral de la boîte de réception
Gmail.](../../../../_images/gmail-side-panel.png)

Ensuite, tapez `Konvergo ERP` dans la barre de recherche et trouvez **Konvergo ERP Inbox
Addin**.

![Konvergo ERP Inbox Addin dans Google Workspace
Marketplace.](../../../../_images/google-workspace-marketplace.png)

Vous pouvez également vous rendre directement sur la page **Konvergo ERP Inbox Addin**
sur [Google Workspace
Marketplace](https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275).

Une fois que vous avez trouvé le plugin, cliquez sur **Installer** et ensuite
sur **Continuer** pour commencer l’installation.

Ensuite, sélectionnez le compte Gmail que l’utilisateur souhaite connecter à
Konvergo ERP. Cliquez sur **Autoriser** pour permettre à Konvergo ERP d’accéder au compte
Google. Google affichera alors une fenêtre contextuelle confirmant que
l’installation a réussi.

### Configurer la base de données Konvergo ERP

La fonctionnalité **Plugin de messagerie** doit être activée dans la base de
données Konvergo ERP afin d’utiliser le plugin Gmail. Pour activer la fonctionnalité,
allez aux Paramètres ‣ Paramètres généraux. Sous la section **Intégrations** ,
activez **Plugin de messagerie** et cliquez ensuite sur **Enregistrer**.

![La fonctionnalité Plugin de messagerie dans les
paramètres.](../../../../_images/mail-plugin-setting.png)

### Configurer la boîte de réception Gmail

Dans la boîte de réception Gmail, une icône Konvergo ERP mauve est à présent visible
dans le panneau de droite. Cliquez sur l’icône Konvergo ERP pour ouvrir la fenêtre du
plugin Konvergo ERP. Sélectionnez ensuite n’importe quel email dans la boîte de
réception. Cliquez sur **Autoriser l’accès** dans la fenêtre du plugin pour
accorder à Konvergo ERP l’accès à la boîte de réception Gmail.

![Le bouton Autoriser l'accès dans la barre latérale droite du panneau de
plugin Konvergo ERP.](../../../../_images/authorize-access.png)

Ensuite, cliquez sur **Connexion** , saisissez l’URL de la base de données
Konvergo ERP que l’utilisateur souhaite connecter à la boîte de messagerie Gmail et
connectez-vous à la base de données.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Utilisez l’URL générale pour la base de données et pas l’URL d’une page spécifique de la base de données. Par exemple, utilisez <code>https://mycompany.odoo.com</code>, au lieu de <code>https://mycompany.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Enfin, cliquez sur **Autoriser** pour permettre à Gmail d’accéder à la base de
données Konvergo ERP. Le navigateur affichera ensuite un message **Success!**. Fermez
ensuite la fenêtre. La boîte de réception Gmail et la base de données Konvergo ERP
sont à présent connectées.

## Utilisateurs d’Konvergo ERP On-Premise

Pour les bases de données hébergées sur serveur autres que Konvergo ERP Online (ou
Konvergo ERP.sh), suivez les étapes ci-dessous pour configurer le plugin Gmail.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans le cadre de ses lignes directrices en matière de sécurité, Konvergo ERP demande aux créateurs de modules complémentaires de fournir une liste des URL pouvant être utilisées dans les actions et les redirections lancées par le module complémentaire. Ceci permet de protéger les utilisateurs en garantissant, par exemple, qu’aucun module complémentaire ne les redirige vers un site web malveillant. (En savoir plus sur <a href="https://developers.google.com/apps-script/manifest/allowlist-url">Google Apps Script</a>.)</p>
<p>Étant donné que Konvergo ERP ne peut répertorier que le domaine <code>odoo.com</code> et non le domaine unique du serveur de chaque client sur serveur, les clients sur serveur ne peuvent pas installer le plugin Gmail à partir de Google Workspace Marketplace.</p>
</div>

### Installer le plugin Gmail

Tout d’abord, accédez au [répertoire GitHub](https://github.com/odoo/mail-
client-extensions) pour les Plugins de messagerie Konvergo ERP. Ensuite, cliquez sur
le bouton vert **Code** et sur **Download ZIP** pour télécharger les fichiers
du plugin de messagerie sur l’ordinateur de l’utilisateur.

![Téléchargez le fichier ZIP à partir du répositoire GitHub d'Konvergo ERP pour les
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
ouvrez le fichier intitulé **appsscript.json**. Dans la section
**urlFetchWhitelist** , remplacez toutes les références à `odoo.com` avec le
domaine du serveur unique du client Konvergo ERP.

Ensuite, dans le même fichier **gmail** , ouvrez le fichier intitulé
**README.md**. Suivez les instructions dans le fichier **README.md** pour
pousser les fichiers Gmail Plugin en tant que projet Google.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’ordinateur doit être en mesure d’exécuter des commandes Linux afin de suivre les instructions du fichier <b>README.md</b>.</p>
</div>

Ensuite, partagez le projet Google avec le compte Gmail que l’utilisateur
souhaite connecter à Konvergo ERP. Cliquez sur **Publish** (Publier) et **Deploy from
manifest** (Déployer à partir du fichier manifeste). Enfin, cliquez sur
**Install the add-on** pour installer le plugin Gmail.

### Configurer la base de données Konvergo ERP

La fonctionnalité **Plugin de messagerie** doit être activée dans la base de
données Konvergo ERP afin d’utiliser le plugin Gmail. Pour activer la fonctionnalité,
allez aux Paramètres ‣ Paramètres généraux. Sous la section **Intégrations** ,
activez **Plugin de messagerie** et cliquez ensuite sur **Enregistrer**.

![La fonctionnalité Plugin de messagerie dans les
paramètres.](../../../../_images/mail-plugin-setting.png)

### Configurer la boîte de réception Gmail

Dans la boîte de réception Gmail, une icône Konvergo ERP mauve est à présent visible
dans le panneau de droite. Cliquez sur l’icône Konvergo ERP pour ouvrir la fenêtre du
plugin Konvergo ERP. Sélectionnez ensuite n’importe quel email dans la boîte de
réception. Cliquez sur **Autoriser l’accès** dans la fenêtre du plugin pour
accorder à Konvergo ERP l’accès à la boîte de réception Gmail.

![Le bouton Autoriser l'accès dans la barre latérale droite du panneau de
plugin Konvergo ERP.](../../../../_images/authorize-access.png)

Ensuite, cliquez sur **Connexion** , saisissez l’URL de la base de données
Konvergo ERP que l’utilisateur souhaite connecter à la boîte de messagerie Gmail et
connectez-vous à la base de données.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Utilisez l’URL générale pour la base de données et pas l’URL d’une page spécifique de la base de données. Par exemple, utilisez <code>https://mycompany.odoo.com</code>, au lieu de <code>https://mycompany.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Enfin, cliquez sur **Autoriser** pour permettre à Gmail d’accéder à la base de
données Konvergo ERP. Le navigateur affichera ensuite un message **Success!**. Fermez
ensuite la fenêtre. La boîte de réception Gmail et la base de données Konvergo ERP
sont à présent connectées.

