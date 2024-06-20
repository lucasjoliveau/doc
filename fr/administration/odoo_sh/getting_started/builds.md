# Builds

## Vue d’ensemble

Dans Odoo.sh, un build est considéré comme une base de données chargée par un
serveur Odoo ([odoo/odoo](https://github.com/odoo/odoo) &
[odoo/enterprise](https://github.com/odoo/enterprise)) fonctionnant sur une
révision spécifique du dépôt de votre projet dans un environnement
conteneurisé. Sa finalité est de tester le bon comportement du serveur, de la
base de données et des fonctionnalités avec cette révision.

![../../../_images/interface-builds.png](../../../_images/interface-
builds.png)

Dans cette vue, une ligne représente une branche et une cellule d’une ligne
représente un build de cette branche.

La plupart du temps, les builds sont créés à la suite des poussées vers les
branches de votre dépôt Github. Ils peuvent également être créés lorsque vous
effectuez d’autres opérations, telles que l’importation d’une base de données
sur Odoo.sh ou la demande d’un rebuild pour une branche de votre projet.

Un build est considéré comme réussi si aucune erreur ou avertissement
n’apparaît lors de sa création. Un build réussi est vert.

Un build est considéré comme échoué si des erreurs surviennent lors de sa
création. Un build échoué est en rouge.

Si des avertissements apparaissent pendant la création, mais qu’il n’y a pas
d’erreurs, le build est considéré comme presque réussi. Il est en jaune pour
informer le développeur que les avertissements ont été soulevés.

Les builds ne créent pas toujours une base de données à partir de zéro. Par
exemple, lors de la poussée d’un changement vers la branche de production, le
build créé démarre simplement le serveur avec votre nouvelle révision et tente
d’y charger la base de données de production actuelle. Si aucune erreur
n’apparaît, le build est considéré comme réussi, sinon échoué.

## Phases

### Production

Le premier build d’une branche de production crée une base de données à partir
de zéro. Si ce build est réussi, cette base de données est considérée comme la
base de données de production de votre projet.

À partir de ce moment, les poussées vers la branche de production créeront de
nouveaux builds qui tenteront de charger la base de données à l’aide d’un
serveur fonctionnant avec la nouvelle révision.

Si le build est réussi ou a des avertissements sans avoir des erreurs, la base
de données de production fonctionnera désormais avec ce build, ainsi qu’avec
la révision associée à ce build.

Si le build ne parvient pas à charger ou mettre à jour la base de données, le
dernier build réussi est réutilisé pour charger la base de données et donc la
base de données s’exécute à l’aide d’un serveur fonctionnant avec la dernière
révision réussie.

Le build utilisé pour exécuter la base de données de production est toujours
le premier build de la liste. Si un build échoue, il est placé après le build
qui exécute actuellement la base de données de production.

### Simulation

Les builds de stimulation dupliquent la base de données de production et
tentent de charger ce doublon avec les révisions des branches de simulation.

Chaque fois que vous poussez une nouvelle révision vers une branche de
simulation, le build créé utilise une nouvelle copie de la base de données de
production. Les bases de données ne sont pas réutilisées entre les builds de
la même branche. Ceci garantit que :

  * les builds de simulation utilisent des bases de données proches de celles de la production, de sorte que vous n’effectuez pas des tests avec des données obsolètes,

  * vous pouvez faire tous les tests nécessaires dans la même base de données de simulation et vous pouvez ensuite demander un rebuild lorsque vous voulez redémarrer avec une nouvelle copie de la production.

Néanmoins, cela signifie que si vous faites des changements de configuration
dans les bases de données de démonstration et que vous ne les appliquez pas
dans la production, ils ne seront pas transmis au prochain build de la même
branche de simulation.

### Développement

Les builds de développement créent de nouvelles bases de données, chargent les
données de démonstration et exécutent les tests unitaires.

Un build sera considéré comme échoué et en rouge si les tests échouent pendant
l’installation, par ils sont censés soulever des erreurs en cas de problème.

Si tous les tests réussissent et qu’il n’y a pas d’erreur, le build sera
considéré comme réussi.

En fonction de la liste des modules à installer et tester, un build de
développement peut prendre jusqu’à une heure pour être prêt. Ceci est dû au
grand nombre de tests dans la suite de modules Odoo par défaut.

## Fonctionnalités

La branche de production apparaît toujours en premier lieu, puis les autres
branches sont classées en fonction du dernier build créé. Vous pouvez filtrer
les branches.

![../../../_images/interface-builds-branches.png](../../../_images/interface-
builds-branches.png)

Pour chaque branche, vous pouvez accéder à la base de données du dernier build
à l’aide du lien _Connect_ et accéder au code de la branche à l’aide du lien
_Github_. Pour les branches autres que la production, vous pouvez créer un
nouveau build qui utilisera la dernière révision de la branche à l’aide du
lien _rebuild_. Le dernier lien n’est pas disponible lorsqu’il y a déjà un
build en cours pour la branche.

![../../../_images/interface-builds-build.png](../../../_images/interface-
builds-build.png)

Pour chaque build, vous pouvez accéder aux changements de révision en
utilisant le bouton avec l’icône Github. Vous pouvez accéder à la base de
données du build en tant qu’administrateur à l’aide du bouton _Connect_. Vous
pouvez également accéder à la base de données avec un autre utilisateur en
utilisant le bouton _Connect as_ dans le menu déroulant du bouton _Connect_.

![../../../_images/interface-builds-build-
dropdown.png](../../../_images/interface-builds-build-dropdown.png)

Dans le menu déroulant du build, vous pouvez accéder aux mêmes fonctionnalités
que dans [la vue des branches](branches.html#odoosh-gettingstarted-branches-
tabs) : _Journaux_ , _Web Shell_ , _Editor_ , _Emails sortants_. Vous avez
également la possibilité de _télécharger un dump_ de la base de données du
build.

