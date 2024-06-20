# Rendre les postes de travail indisponibles à l’aide de Congés

Dans Odoo, les _postes de travail_ sont utilisés pour exécuter des opérations
de fabrication à des emplacements spécifiques. Cependant, si un poste de
travail ne peut pas être utilisé pour une raison quelconque, les ordres de
travail commencent à s’empiler sur le poste de travail jusqu’à ce qu’il est de
nouveau opérationnel.

Par conséquent, il est nécessaire de rendre le poste de travail indisponible
dans Odoo pour que la plateforme envoie les nouveaux ordres de travail à
d’autres postes de travail qui sont opérationnels. Grâce à l’application
_Congés_ d’Odoo, il est possible de rendre un poste de travail indisponible
pendant une certaine période. Cela garantit que les opérations de fabrication
peuvent continuer jusqu’à ce que le poste de travail impacté est de nouveau
disponible.

## Configuration

Avant qu’un poste de travail peut être désigné comme indisponible, la
plateforme Odoo doit d’abord être configurée correctement. Tout d’abord, il
est nécessaire d’activer le [mode
développeur](../../../general/developer_mode.html#developer-mode). Cette
opération permet d’afficher le bouton intelligent Congés dans la fenêtre
contextuelle Heures de travail sur chaque poste de travail.

Activez le mode développeur en allant aux Paramètres, faites défiler jusqu’en
bas de la page et cliquez sur Activer le mode développeur dans l’en-tête
Outils développeur.

![Le bouton "Activer le mode développeur".](../../../../_images/developer-
mode-button.png)

Ensuite, installez l’application _Congés_. Il s’agit de l’application utilisée
pour assigner des congés à toutes les ressources dans Odoo, y compris les
employés et les postes de travail. Allez aux Apps, puis saisissez `Congés`
dans la barre Rechercher…. La carte du module Congés devrait être la seule à
apparaître sur la page. Cliquez sur le bouton vert Installer sur la carte pour
installer l’application.

![La carte d'installation du module Congés.](../../../../_images/time-off-
install-card.png)

La dernière étape est de correctement configurer les postes de travail. Pour
ce flux de travail, il est nécessaire d’avoir au moins deux postes de travail
: un qui est rendu indisponible et un deuxième qui reçoit les ordres de
travail que l’autre poste ne peut pas accepter. Si le deuxième poste de
travail n’est pas configuré, Odoo ne peut pas acheminer les ordres de travail
depuis le poste de travail indisponible et ils s’empileront dans sa file
d’attente.

Pour créer un poste de travail, allez à Fabrication ‣ Configuration ‣ Postes
de travail ‣ Créer.

Assurez-vous que les deux postes de travail ont le même équipement répertorié
dans l’onglet Équipement. Cela permet d’assurer que les opérations effectuées
dans un poste de travail peuvent également être réalisées dans l’autre.

![L'onglet équipement d'un formulaire de poste de
travail.](../../../../_images/work-center-equipment-tab.png)

Pour le poste de travail qui sera rendu indisponible, sélectionnez le deuxième
poste de travail dans le menu déroulant Postes de travail alternatifs. Odoo
sait maintenant qu’il faut envoyer les ordres de travail au deuxième poste de
travail lorsque le premier est indisponible pour quelle que raison que ce
soit.

![Un formulaire de poste de travail configuré avec un poste de travail
alternatif.](../../../../_images/alternative-work-center-selection.png)

## Ajouter des congés pour un poste de travail

Une fois la configuration terminée, vous pouvez assigner des congés au poste
de travail qui sera rendu indisponible. Allez à Fabrication ‣ Configuration ‣
Postes de travail et sélectionnez le poste de travail affecté. Cliquez sur
Modifier et ensuite sur le bouton ↗ (lien externe) à côté du menu déroulant
Heures de travail.

![Le bouton "Lien externe" des heures de travail sur le formulaire du poste de
travail.](../../../../_images/working-hours-button.png)

Une fenêtre contextuelle intitulée Ouvrir : Heures de travail s’ouvre. Les
heures de travail standards pour le poste de travail y sont répertoriées,
ainsi que d’autres informations. Puisque le mode développeur est activé, un
bouton Congés se trouve dans le coin supérieur droit de la fenêtre
contextuelle. Cliquez dessus pour être redirigé vers la page Congés des
ressources.

![Le bouton Congés sur la fenêtre contextuelle des Heures de
travail.](../../../../_images/time-off-button.png)

Sur cette page, cliquez sur Créer pour configurer une nouvelle entrée de
congés. Sur le formulaire des congés, notez le Motif de la fermeture du poste
de travail (défaillance, maintenance, etc.), définissez la Ressource sur le
poste de travail affecté, et choisissez une Date de début et une Date de fin
pour préciser la période pendant laquelle le poste de travail ne sera pas
disponible. Cliquez sur Enregistrer et l’inactivité du poste de travail est
enregistrée dans Odoo.

![Le formulaire "Congés des ressources".](../../../../_images/time-off-
form.png)

## Acheminer les ordres vers un poste de travail alternatif

Une fois qu’un poste de travail se trouve dans la période d’inactivité
précisée, les ordres de travail qui lui sont envoyés peuvent être
automatiquement acheminés vers un autre poste de travail à l’aide du bouton
Programmer.

Commencez par créer un nouvel ordre de fabrication en sélectionnant Opérations
‣ Ordres de fabrication ‣ Créer. Sur le formulaire de l’ordre de fabrication,
précisez un Produit qui utilise le poste de travail indisponible pour l’une de
ses opérations. Cliquez sur Confirmer pour confirmer l’ordre de travail.

Sur l’ordre de travail confirmé, sélectionnez l’onglet Ordres de travail. Par
défaut, le poste de travail indisponible est indiqué dans la colonne Poste de
travail. Vous trouverez également un bouton vert Programmer dans le coin
supérieur gauche de la page.

![Le bouton Programmer sur un ordre de fabrication.](../../../../_images/mo-
plan-button.png)

Cliquez sur Programmer et le poste de travail répertorié dans l’onglet Ordres
de travail est automatiquement remplacé par le poste de travail alternatif.

![Le poste de travail sélectionné est mis à jour automatiquement après avoir
cliqué sur le bouton Programmer.](../../../../_images/work-center-
planning.png)

Une fois que la période d’inactivité du poste de travail indisponible prend
fin, Odoo reconnaît que le poste de travail est de nouveau disponible. À ce
stade, le fait de cliquer sur le bouton Programmer n’achemine pas les ordres
de travail vers un poste de travail alternatif, à moins que le premier ne soit
à plein régime.

