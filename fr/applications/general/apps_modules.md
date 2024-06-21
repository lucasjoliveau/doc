# Applications et modules

Vous pouvez installer, mettre à niveau et désinstaller toutes les applications
et tous les modules depuis le tableau de bord Applications .

Par défaut, un filtre _Applications_ est appliqué. Si vous souhaitez
rechercher des modules, cliquez sur _Filtres_ et sélectionnez _Extra_.

![Ajouter un filtre "Extra" dans Konvergo ERP Applications](../../_images/apps-search-
filter.png) <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Konvergo ERP n’est <em>pas un smartphone</em> et ses applications ne doivent pas être installées ou désinstallées négligemment. Soyez prudent lorsque vous ajoutez ou supprimez des applications et des modules sur votre base de données, car cela peut avoir un impact sur vos frais d’abonnement.</p>
<ul>
<li><div class="line-block">
<div class="line"><b>L’installation ou la désinstallation d’applications et la gestion des utilisateurs dépendent de vous.</b></div>
<div class="line">En tant qu’administrateur de votre base de données, vous êtes responsable de son utilisation, car c’est vous qui connaissez le mieux le fonctionnement de votre organisation.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>Les applications Konvergo ERP ont des dépendances.</b></div>
<div class="line">L’installation de certaines applications et fonctionnalités avec des dépendances peut également entraîner l’installation d’applications et de modules supplémentaires qui sont techniquement requis, même si vous ne les utilisez pas activement.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>L’essai de l’installation/la suppression de l’application sur une copie de votre base de données.</b></div>
<div class="line">De cette façon, vous pouvez savoir quelles dépendances d’application peuvent être nécessaires ou quelles données peuvent être effacées.</div>
</div>
</li>
</ul>
</div>

## Installer des applications et des modules

Allez aux Applications et cliquez sur le bouton _Activer_ de l’application que
vous souhaitez installer.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le module que vous recherchez n’est pas répertorié, vous pouvez <b>mettre à jour la liste des applications</b>.</p>
<p>Pour cela, activez le <a href="developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, puis allez aux Applications ‣ Mettre à jour la liste des applications et cliquez sur <em>Mettre à jour</em>.</p>
</div>

## Mettre à niveau des applications et des modules

On some occasions, new improvements or app features are added to [supported
versions of Konvergo ERP](../../administration/supported_versions). To be able to
use them, you must **upgrade** your app.

Allez aux Applications, cliquez sur le _menu déroulant_ de l’application que
vous souhaitez mettre à niveau, puis sur _Mettre à jour_.

## Désinstaller des applications et des modules

Allez aux Applications, cliquez sur le _menu déroulant_ de l’application que
vous souhaitez désinstaller, puis sur _Désinstaller_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Certaines applications ont des dépendances, ce qui signifie qu’une application
en nécessite une autre. Par conséquent, la désinstallation d’une application
peut entraîner la désinstallation de plusieurs applications et modules. Konvergo ERP
vous avertit des applications et modules dépendants qui sont affectés par
cette désinstallation.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

Pour terminer la désinstallation, cliquez sur _Confirmer_.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>La désinstallation d’une application désinstalle également toutes ses dépendances et efface définitivement leurs données.</p>
</div>

