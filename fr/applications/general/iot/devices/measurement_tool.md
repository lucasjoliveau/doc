# Connecter un outil de mesure

Avec l”IoT box d’Odoo, il est possible de connecter des outils de mesure à la
base de données Odoo afin de les utiliser dans l’application _Qualité_ lors
d’un point de contrôle qualité ou sur un poste de travail pendant le processus
de fabrication.

Vous trouverez la liste des périphériques pris en charge ici : [Périphériques
pris en charge](https://www.odoo.com/page/iot-hardware).

## Connecter via USB (universal serial bus)

Pour ajouter un périphérique connecté via USB, connectez le câble USB à l”IoT
box et le périphérique apparaît dans la base de données Odoo.

![Outil de mesure reconnu par l'IoT box.](../../../../_images/device-
dropdown.png)

## Connecter via Bluetooth

Activez la fonctionnalité Bluetooth sur le périphérique (consultez le manuel
du périphérique pour plus d’explications) et l”IoT box se connecte
automatiquement au périphérique.

![Indicateur Bluetooth sur l'outil de
mesure.](../../../../_images/measurement-tool.jpeg)

## Lier un outil de mesure à un point de contrôle qualité dans le processus de
fabrication

Dans l’application _Qualité_ , un périphérique peut être configuré sur un
point de contrôle qualité. Pour ce faire, allez à l’application Qualité ‣
Contrôle qualité ‣ Points de contrôle et ouvrez le point de contrôle souhaité
auquel l’outil de mesure doit être lié.

À partir de là, modifiez le point de contrôle en sélectionnant le champ Type
et Mesure dans le menu déroulant. Cette opération fait apparaître un champ
intitulé Périphérique, où vous pouvez sélectionner le périphérique lié.

Vous pouvez également configurer les champs Norme et Tolérance. Enregistrez
les changements le cas échéant.

À ce stade, l’outil de mesure est lié au point de contrôle qualité
sélectionné. La valeur, qui doit généralement être modifiée manuellement, est
automatiquement mise à jour pendant l’utilisation de l’outil.

![Saisie de l'outil de mesure dans la base de données
Odoo.](../../../../_images/measurement-control-point.png)

Astuce

Vous pouvez également accéder aux points de contrôle qualité en allant à
l’application IoT ‣ Périphérique, puis sélectionnez le périphérique. Allez à
l’onglet Points de contrôle qualité où vous pouvez les ajouter au
périphérique.

Note

Sur le formulaire détaillé du contrôle qualité, vous pouvez définir le Type de
contrôle sur Mesure. Accédez à la page détaillée d’un nouveau contrôle qualité
en allant à l’application Qualité ‣ Contrôle qualité ‣ Contrôles qualité ‣
Nouveau.

Pour plus d'infos

  * [Quality control points](../../../inventory_and_mrp/quality/quality_management/quality_control_points.html)

  * [Créer des alertes qualité](../../../inventory_and_mrp/quality/quality_management/quality_alerts.html)

## Lier un outil de mesure à un poste de travail dans l’application
Fabrication

Pour lier un outil de mesure à une action, il doit d’abord être configuré sur
un poste de travail. Pour ce faire, allez à l’application Fabrication ‣
Configuration ‣ Postes de travail. Puis sélectionnez le poste de travail
souhaité dans lequel l’outil de mesure sera utilisé.

Sur la page du poste de travail, ajoutez le périphérique dans l’onglet
Déclencheurs IoT dans la colonne Périphérique en sélectionnant Ajouter une
ligne. Ensuite, l’outil de mesure peut être lié à l’option intitulée Prendre
la mesure dans le menu déroulant Action. Vous pouvez ajouter une clé pour
déclencher l’action.

Important

Il convient de noter que le premier déclencheur répertorié est choisi en
premier. L’ordre est important et ces déclencheurs peuvent être glissés dans
n’importe quel ordre.

Note

Sur l’écran de l”Ordre de travail, un graphique de statut indique si la base
de données est correctement connectée à l’outil de mesure.

Pour plus d'infos

[Intégrer des appareils
IoT](../../../inventory_and_mrp/manufacturing/management/using_work_centers.html#workcenter-
iot)

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

