# Connecter une caméra

Il est possible de connecter une caméra à l”IoT box dans une base de données
Konvergo ERP en quelques étapes seulement. Une fois qu’une caméra est connectée à
l”IoT box, elle peut être utilisée dans le processus de fabrication ou liée à
un point de contrôle qualité. Ceci permet de prendre des photos lorsque vous
atteignez un certain point de contrôle qualité ou lorsque vous appuyez sur une
touche spécifique pendant la fabrication.

## Connexion

Pour connecter une caméra à une IoT box, il suffit de les relier par un câble,
généralement à l’aide d’un câble USB.

Si la caméra est [prise en charge](https://www.odoo.com/page/iot-hardware),
rien ne doit être configuré et elle sera détectée dès sa connexion.

![Caméra reconnue par l'IoT box.](../../../../_images/camera-dropdown.png)

## Lier une caméra à un point de contrôle qualité dans le processus de
fabrication

Dans l’application Qualité, un périphérique peut être configuré sur un **Point
de contrôle qualité**. Pour ce faire, allez à l’application Qualité ‣ Contrôle
qualité ‣ Points de contrôle et ouvrez le **Point de contrôle** souhaité
auquel la caméra doit être liée.

Sur le formulaire du point de contrôle, modifiez le point de contrôle en
sélectionnant le champ **Type** et **Prendre une photo** dans le menu
déroulant. Cette opération fait apparaître un champ intitulé **Périphérique**
, où vous pouvez sélectionner le _périphérique_ lié. Le cas échéant,
**enregistrez** les changements.

![Configuration du périphérique sur le point de contrôle
qualité.](../../../../_images/control-point-device.png)

Vous pouvez à présent utiliser la caméra au point de contrôle qualité
sélectionné. Lorsque vous atteignez ce point de contrôle qualité pendant le
processus de fabrication, la base de données invite l’opérateur à prendre une
photo.

![Interface graphique du périphérique sur le point de contrôle
qualité.](../../../../_images/serial-number-picture.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez également accéder aux points de contrôle qualité en allant à l’application IoT ‣ Périphériques, puis, sélectionnez le périphérique. Allez à l’onglet <b>Points de contrôle qualité</b> où vous pouvez les ajouter au périphérique.</p>
</div>
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Sur un formulaire de contrôle qualité, vous pouvez définir le <b>Type</b> de contrôle sur <b>Prendre une photo</b>. Allez à l’application Qualité ‣ Contrôle qualité ‣ Contrôles qualité ‣ Nouveau pour créer un nouveau contrôle qualité à partir de la page <b>Contrôles qualité</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Quality control points</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Créer des alertes qualité</a></p></li>
</ul>
</div>

## Lier une caméra à un poste de travail dans l’application Fabrication

Pour lier une caméra à une action, elle doit d’abord être configurée sur un
poste de travail. Allez à l’application Fabrication ‣ Configuration ‣ Postes
de travail. Allez ensuite au **Poste de travail** sur lequel une caméra sera
utilisée pour afficher le formulaire détaillé de ce poste de travail. Sur ce
formulaire, ajoutez le périphérique dans l’onglet **Déclencheurs IoT** , dans
la colonne **Périphérique** , en cliquant sur **Ajouter une ligne**.

La caméra peut désormais être liée à l’option libellée **Prendre une photo**
dans la colonne déroulante **Action**. Vous pouvez également ajouter une clé
afin de déclencher l’action.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le premier déclencheur de la liste est choisi en premier. L’ordre des déclencheurs est important et ils peuvent être glissés dans l’ordre souhaité.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sur l’écran de l”<b>Ordre de travail</b>, un graphique de statut indique si la base de données est correctement connectée à la caméra.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Intégrer des appareils IoT</span></a></p>
</div>

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

