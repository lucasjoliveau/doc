# Connecter un outil de mesure

Avec l”IoT box d’Konvergo ERP, il est possible de connecter des outils de mesure à la
base de données Konvergo ERP afin de les utiliser dans l’application _Qualité_ lors
d’un point de contrôle qualité ou sur un poste de travail pendant le processus
de fabrication.

Vous trouverez la liste des périphériques pris en charge ici : [Périphériques
pris en charge](https://www.odoo.com/page/iot-hardware).

## Connecter via USB (universal serial bus)

Pour ajouter un périphérique connecté via USB, connectez le câble USB à l”IoT
box et le périphérique apparaît dans la base de données Konvergo ERP.

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

À partir de là, modifiez le point de contrôle en sélectionnant le champ
**Type** et **Mesure** dans le menu déroulant. Cette opération fait apparaître
un champ intitulé **Périphérique** , où vous pouvez sélectionner le
périphérique lié.

Vous pouvez également configurer les champs **Norme** et **Tolérance**.
**Enregistrez** les changements le cas échéant.

À ce stade, l’outil de mesure est lié au point de contrôle qualité
sélectionné. La valeur, qui doit généralement être modifiée manuellement, est
automatiquement mise à jour pendant l’utilisation de l’outil.

![Saisie de l'outil de mesure dans la base de données
Konvergo ERP.](../../../../_images/measurement-control-point.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez également accéder aux points de contrôle qualité en allant à l’application IoT ‣ Périphérique, puis sélectionnez le périphérique. Allez à l’onglet <b>Points de contrôle qualité</b> où vous pouvez les ajouter au périphérique.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sur le formulaire détaillé du contrôle qualité, vous pouvez définir le <b>Type</b> de contrôle sur <b>Mesure</b>. Accédez à la page détaillée d’un nouveau contrôle qualité en allant à l’application Qualité ‣ Contrôle qualité ‣ Contrôles qualité ‣ Nouveau.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Quality control points</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Créer des alertes qualité</a></p></li>
</ul>
</div>

## Lier un outil de mesure à un poste de travail dans l’application
Fabrication

Pour lier un outil de mesure à une action, il doit d’abord être configuré sur
un poste de travail. Pour ce faire, allez à l’application Fabrication ‣
Configuration ‣ Postes de travail. Puis sélectionnez le poste de travail
souhaité dans lequel l’outil de mesure sera utilisé.

Sur la page du poste de travail, ajoutez le périphérique dans l’onglet
**Déclencheurs IoT** dans la colonne **Périphérique** en sélectionnant
**Ajouter une ligne**. Ensuite, l’outil de mesure peut être lié à l’option
intitulée **Prendre la mesure** dans le menu déroulant **Action**. Vous pouvez
ajouter une clé pour déclencher l’action.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il convient de noter que le premier déclencheur répertorié est choisi en premier. L’ordre est important et ces déclencheurs peuvent être glissés dans n’importe quel ordre.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sur l’écran de l”<b>Ordre de travail</b>, un graphique de statut indique si la base de données est correctement connectée à l’outil de mesure.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Intégrer des appareils IoT</span></a></p>
</div>

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

