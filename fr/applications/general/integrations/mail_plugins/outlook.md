# Plugin Outlook

Odoo permet à des applications externes de se connecter afin d’exécuter des
actions de base de données à partir d’emails. Odoo dispose d’un plugin pour
Outlook qui permet de créer une opportunité à partir du panneau de messagerie.

## Configuration

Le [plugin de messagerie](../mail_plugins.html) Outlook doit être configuré
sur Odoo et sur Outlook.

### Activer le plugin de messagerie

Activez d’abord la fonctionnalité _Plugin de messagerie_ dans la base de
données. Allez aux Paramètres ‣ Paramètres généraux ‣ Intégrations, activez le
Plugin de messagerie, et enregistrez la configuration.

### Installer le plugin Outlook

Téléchargez (Enregistrer la page comme ‣ Page Web, XML uniquement) le fichier
XML suivant à charger ultérieurement :
<https://download.odoocdn.com/plugins/outlook/manifest.xml>.

Ensuite, ouvrez la boîte de messagerie Outlook et sélectionnez n’importe quel
email. Cliquez ensuite sur le bouton Autres actions en haut à droite et
sélectionnez Obtenir des compléments.

![Le bouton Autres actions dans Outlook](../../../../_images/more-actions.png)

Astuce

For locally installed versions of Microsoft Outlook, access the Get Add-ins
menu item while in preview mode (**not** with a message open). First, click on
the … (ellipsis) icon in the upper right of the previewed message, then scroll
down, and click on Get Add-ins.

Allez ensuite à l’onglet Mes compléments sur la gauche.

![Mes compléments dans Outlook](../../../../_images/my-add-ins.png)

Sous Compléments personnalisés vers le bas, cliquez sur \+ Ajouter un
complément personnalisé, et puis sur Ajouter à partir d’un fichier…

![Compléments personnalisés dans Outlook](../../../../_images/custom-add-
ins.png)

Pour l’étape suivante, joignez le fichier `manifest.xml` téléchargé plus tôt
et cliquez sur OK. Ensuite, lisez l’avertissement et cliquez sur Installer.

![Avertissement d'installation d'un complément personnalisé dans
Outlook](../../../../_images/add-in-warning.png)

### Connecter la base de données

Outlook sera maintenant connecté à la base de données Odoo. Ouvrez d’abord un
email dans la boîte de messagerie Outlook, cliquez sur le bouton Autres
actions en haut à droite et sélectionnez Odoo for Outlook.

![Bouton de complément Odoo for Outlook](../../../../_images/odoo-for-
outlook.png)

Le panneau de droite peut désormais afficher **Company Insights**. En bas,
cliquez sur Login.

![Se connecter à la base de données Odoo](../../../../_images/panel-login.png)

Note

Seul un nombre limité de demandes relatives aux **Company Insights**
(_Enrichissement de pistes_) est disponible à titre d’essai. Cette
fonctionnalité nécessite des [crédits prépayés](../mail_plugins.html#mail-
plugins-pricing).

Astuce

Si, après un court instant, le panneau est toujours vide, il est possible que
les paramètres des cookies de votre navigateur l’aient empêché de se charger.
Notez que ces paramètres changent également si votre navigateur est en mode «
Incognito ».

Pour résoudre ce problème, configurez le navigateur pour qu’il autorise
toujours les cookies sur la page du plugin Odoo.

Pour Google Chrome, modifiez les paramètres des cookies du navigateur en
suivant les étapes suivantes :
<https://support.google.com/chrome/answer/95647> et en ajoutant
`download.odoo.com` à la liste des Sites qui peuvent toujours utiliser des
cookies.

Une fois cela fait, vous devez rouvrir le panneau Outlook.

Saisissez à présent l’URL de la base de données Odoo et cliquez sur Login.

![Saisir l'URL de la base de données Odoo](../../../../_images/enter-database-
url.png)

Cliquez ensuite sur Autoriser pour ouvrir la fenêtre contextuelle.

![Avertissement de la nouvelle fenêtre contextuelle](../../../../_images/new-
window-warning.png)

Si l’utilisateur n’est pas connecté à la base de données, saisissez les
informations d’identification. Cliquez sur Autoriser pour permettre au plugin
Outlook de se connecter à la base de données.

![Permettre au plugin Outlook de se connecter à une base de
données](../../../../_images/odoo-permission.png)

### Ajouter un raccourci au plugin

Par défaut, le plugin Outlook peut être ouvert à partir du menu _Autres
actions_. Toutefois, pour gagner du temps, il est possible de l’ajouter à côté
des autres actions par défaut.

Dans la boîte de messagerie Outlook, cliquez sur Paramètres, puis sur Afficher
tous les paramètres d’Outlook.

![Afficher tous les paramètres d'Outlook](../../../../_images/all-outlook-
settings.png)

Sélectionnez maintenant Personnaliser les actions sous Mail, cliquez sur Odoo
for Outlook, et puis sur Enregistrer.

![Action personnalisée Odoo for Outlook](../../../../_images/customize-
actions.png)

Après cette étape, ouvrez n’importe quel email ; le raccourci devrait
s’afficher.

![Action personnalisée Odoo for Outlook](../../../../_images/odoo-outlook-
shortcut.png)

### Utiliser le plugin

Maintenant que le plugin est installé et opérationnel, il suffit de cliquer
sur le `O` [icône Odoo] ou allez aux Autres actions et cliquez sur Odoo for
Outlook pour créer une piste. Le panneau latéral apparaît sur le côté droit et
sous Opportunités, cliquez sur Nouveau. Une nouvelle fenêtre avec
l’opportunité créée dans la base de données Odoo s’affichera.

