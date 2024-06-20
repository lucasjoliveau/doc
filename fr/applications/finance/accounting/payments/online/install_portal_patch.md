# Installer le patch pour désactiver le paiement des factures en ligne

Suite à de récents changements dans Odoo 16, vous pourriez être averti que la
désactivation du paramètre Paiement des factures en ligne entraînera la
désinstallation de modules. Si vous souhaitez désactiver la fonctionnalité
sans désinstaller des modules, suivez les étapes ci-dessous pour installer le
module **Paiement - Compte / Patch de paiement des factures en ligne**.

Note

Si votre base de données Odoo est créée après la publication du module
**Paiement - Compte / Patch de paiement des factures en ligne** , vous n’avez
rien à faire.

Pour vérifier si le module est déjà installé, allez à Apps, supprimez le
filtre `Apps` et recherchez `account_payment`. Si le module **Paiement -
Compte / Patch de paiement des factures en ligne** s’affiche et est marqué
comme installé, votre base de données Odoo est déjà à jour et vous pouvez
désactiver la fonctionnalité sans effet secondaire.

## Mettre à jour Odoo à la dernière version

La possibilité de désactiver le paramètre Paiement des factures en ligne sans
effets secondaires est disponible grâce à un nouveau module Odoo ; pour
pouvoir l’installer, vous devez vous assurer que votre code source Odoo est à
jour.

Si vous utilisez Odoo par le biais d’Odoo.com ou de la plateforme Odoo.sh,
votre code est déjà à jour et vous pouvez procéder à l’étape suivante.

If you use Odoo with an on-premise setup or through a partner, you must update
your installation as detailed in [this documentation
page](../../../../../administration/on_premise/update.html), or by contacting
your integrating partner.

## Mettre à jour la liste des modules disponibles

De nouveaux modules doivent être _découverts_ par votre instance Odoo pour
être disponibles dans le menu **Apps**.

Pour ce faire, activez le [mode
développeur](../../../../general/developer_mode.html#developer-mode), et allez
à Apps ‣ Mettre à jour la liste des Apps. Un assistant vous demandera une
confirmation.

## Installez le module Patch de paiement des factures en ligne.

Avertissement

Vous ne devez jamais installer de nouveaux modules sur votre base de données
de production sans les tester dans un environnement dupliqué ou de simulation.
Pour les clients d’Odoo.com, une base de données dupliquée peut être créée à
partir de le page de gestion de la base de données. Pour les utilisateurs
Odoo.sh, vous devez utiliser une base de données dupliquée ou une base de
données de simulation. Pour les utilisateurs On premise, vous devez utiliser
un environnement de simulation - contactez votre partenaire d’intégration pour
plus d’informations sur la façon de tester un nouveau module dans votre
configuration particulière.

Le module devrait maintenant être disponible dans votre menu Apps. Supprimez
le filtre `Apps` et recherchez `account_payment` ; le module Paiement - Compte
/ Patch de paiement des factures en ligne devrait être disponible pour
l’installation. Si vous ne trouvez pas le module après avoir mis à jour la
liste des modules disponibles, cela signifie que votre code source Odoo n’est
pas à jour ; reprenez la première étape de cette page.

Une fois le module installé, la désactivation de la fonctionnalité
fonctionnera comme prévu et ne vous demandera pas de désinstaller des
applications ou des modules installés.

