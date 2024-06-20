# Entrepôt par défaut de l’utilisateur

La configuration d’un **entrepôt par défaut** peut s’avérer utile pour les
techniciens de terrain qui conservent un stock dans leur camionnette ou pour
ceux qui se réapprovisionnent toujours dans le même entrepôt. Cela permet
également aux opérateurs de terrain de passer d’un entrepôt à l’autre à partir
de leur profil.

Les produits figurant dans les commandes créées lors des interventions sur le
terrain sont toujours prélevés dans l’entrepôt par défaut, permettant de
conserver un inventaire précis.

Pour plus d'infos

[Inventaire](../../inventory_and_mrp/inventory.html)

## Configuration

Pour configurer un entrepôt par défaut de l’utilisateur, la fonctionnalité
[emplacements de
stockage](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations.html)
doit être activée dans l’application **Inventaire**. Il est également
nécessaire d’avoir plus d’un entrepôt dans votre base de données.

Vous pouvez le configurer pour votre profil ou pour tous les utilisateurs.

Pour plus d'infos

[Gérer les entrepôts et les
emplacements](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses_locations.html)

### Pour votre profil

Pour configurer un entrepôt par défaut pour vous-même, cliquez sur votre
**icône de profil** dans le coin supérieur droit de l’écran, allez à Mon
profil ‣ Préférences ‣ Entrepôt par défaut. Sélectionnez l’entrepôt par défaut
dans le menu déroulant.

### Pour tous les utilisateurs

Pour configurer un entrepôt par défaut pour un utilisateur spécifique, allez
aux Paramètres ‣ Utilisateurs ‣ Gérer les utilisateurs, sélectionnez un
utilisateur et allez à l’onglet Préférences. Faites défiler jusqu’à Inventaire
et sélectionnez l’entrepôt par défaut dans le menu déroulant.

![Sélection d'un entrepôt par défaut sur un profil
d'utilisateur.](../../../_images/user-default.png)

## Utiliser dans les tâches de services sur site

Une fois qu’un entrepôt par défaut a été configuré pour un utilisateur, les
matériaux utilisés pour une commande liée à une tâche de Services sur site
sont prélevés de cet entrepôt particulier. Ouvrez la commande liée, allez à
l’onglet Autres informations, faites défiler jusqu’à Livraison. L’entrepôt par
défaut est appliqué correctement.

Une fois que la tâche de services sur site est marquée comme achevée, le stock
de l’entrepôt par défaut est mis à jour automatiquement.

