# Applications et modules

Vous pouvez installer, mettre à niveau et désinstaller toutes les applications
et tous les modules depuis le tableau de bord Applications .

Par défaut, un filtre _Applications_ est appliqué. Si vous souhaitez
rechercher des modules, cliquez sur _Filtres_ et sélectionnez _Extra_.

![Ajouter un filtre "Extra" dans Odoo Applications](../../_images/apps-search-
filter.png)

Avertissement

Odoo n’est _pas un smartphone_ et ses applications ne doivent pas être
installées ou désinstallées négligemment. Soyez prudent lorsque vous ajoutez
ou supprimez des applications et des modules sur votre base de données, car
cela peut avoir un impact sur vos frais d’abonnement.

  * **L’installation ou la désinstallation d’applications et la gestion des utilisateurs dépendent de vous.**

En tant qu’administrateur de votre base de données, vous êtes responsable de
son utilisation, car c’est vous qui connaissez le mieux le fonctionnement de
votre organisation.

  * **Les applications Odoo ont des dépendances.**

L’installation de certaines applications et fonctionnalités avec des
dépendances peut également entraîner l’installation d’applications et de
modules supplémentaires qui sont techniquement requis, même si vous ne les
utilisez pas activement.

  * **L’essai de l’installation/la suppression de l’application sur une copie de votre base de données.**

De cette façon, vous pouvez savoir quelles dépendances d’application peuvent
être nécessaires ou quelles données peuvent être effacées.

## Installer des applications et des modules

Allez aux Applications et cliquez sur le bouton _Activer_ de l’application que
vous souhaitez installer.

Note

Si le module que vous recherchez n’est pas répertorié, vous pouvez **mettre à
jour la liste des applications**.

Pour cela, activez le [mode développeur](developer_mode.html#developer-mode),
puis allez aux Applications ‣ Mettre à jour la liste des applications et
cliquez sur _Mettre à jour_.

## Mettre à niveau des applications et des modules

On some occasions, new improvements or app features are added to [supported
versions of Odoo](../../administration/supported_versions.html). To be able to
use them, you must **upgrade** your app.

Allez aux Applications, cliquez sur le _menu déroulant_ de l’application que
vous souhaitez mettre à niveau, puis sur _Mettre à jour_.

## Désinstaller des applications et des modules

Allez aux Applications, cliquez sur le _menu déroulant_ de l’application que
vous souhaitez désinstaller, puis sur _Désinstaller_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Certaines applications ont des dépendances, ce qui signifie qu’une application
en nécessite une autre. Par conséquent, la désinstallation d’une application
peut entraîner la désinstallation de plusieurs applications et modules. Odoo
vous avertit des applications et modules dépendants qui sont affectés par
cette désinstallation.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

Pour terminer la désinstallation, cliquez sur _Confirmer_.

Danger

La désinstallation d’une application désinstalle également toutes ses
dépendances et efface définitivement leurs données.

