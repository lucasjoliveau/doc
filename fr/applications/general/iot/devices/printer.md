# Connecter une imprimante

Vous pouvez installer une imprimante en quelques étapes faciles. L’imprimante
peut être utilisée pour imprimer des reçus, des étiquettes, des ordres ou même
des rapports des différentes applications d’Odoo. De plus, les actions de
l’imprimante peuvent être assignées comme une _action sur un déclencheur_
pendant le processus de fabrication ou ajoutées à un point de contrôle qualité
ou à un contrôle qualité.

## Connexion

L”IoT box prend en charge des imprimantes connectées via USB, le réseau ou
Bluetooth. Les [imprimantes prises en charge](https://www.odoo.com/page/iot-
hardware) sont automatiquement détectées et apparaissent dans la liste des
Périphériques de l” _application IoT_.

![L'imprimante comme elle apparaît dans la liste des périphériques de
l'application IoT.](../../../../_images/printer-detected.png)

Note

Cela peut prendre jusqu’à deux minutes avant que l’imprimante s’affiche dans
la liste des périphériques de l” _application IoT_.

## Lier une imprimante

### Lier une imprimante aux ordres de travail

Les _Ordres de travail_ peuvent être liés aux imprimantes, via un point de
contrôle qualité, afin d’imprimer des étiquettes pour des produits fabriqués.

Dans l’application _Qualité_ , vous pouvez configurer un périphérique sur un
point de contrôle qualité. Pour ce faire, allez à l’application Qualité ‣
Contrôle qualité ‣ Points de contrôle et ouvrez le point de contrôle souhaité
auquel l’imprimante doit être liée.

Important

Une _Opération de fabrication_ et une _Opération d’ordre de travail_ doivent
être jointes à un point de contrôle qualité avant que le champ Type permette
de sélectionner l’option Imprimer l’étiquette.

À partir de là, modifiez le point de contrôle en sélectionnant le champ Type
et en sélectionnant Imprimer une étiquette dans le menu déroulant des options.
Cette opération fait apparaître un champ Périphérique, où vous pouvez
sélectionner le _périphérique_ relié. Enregistrez les changements le cas
échéant.

![Voici la configuration du point de contrôle
qualité.](../../../../_images/printer-controlpoint.png)

Vous pouvez désormais utiliser l’imprimante sur le point de contrôle qualité
sélectionné. Lorsque vous atteignez ce point de contrôle qualité pendant le
processus de fabrication, la base de données vous donne l’option d’imprimer
des étiquettes pour un produit spécifique.

![../../../../_images/printer-prompt.png](../../../../_images/printer-
prompt.png)

Astuce

Vous pouvez également accéder aux points de contrôle qualité en allant à
l’application IoT ‣ Périphérique, puis sélectionnez le périphérique. Allez à
l’onglet Points de contrôle qualité où vous pouvez les ajouter au
périphérique.

Note

Sur le formulaire détaillé du contrôle qualité, vous pouvez également définir
le Type de contrôle sur Imprimer une étiquette. Pour créer de nouveaux
contrôles qualité, allez à l’application Qualité ‣ Contrôle qualité ‣
Contrôles qualité ‣ Nouveau.

Pour plus d'infos

  * [Quality control points](../../../inventory_and_mrp/quality/quality_management/quality_control_points.html)

  * [Créer des alertes qualité](../../../inventory_and_mrp/quality/quality_management/quality_alerts.html)

### Lier une imprimante à un poste de travail dans l’application Fabrication

Pour lier une imprimante à une action, elle doit d’abord être configurée sur
un poste de travail. Pour ce faire, allez à l’application Fabrication ‣
Configuration ‣ Postes de travail. Sélectionnez ensuite le poste de travail
sur lequel l’imprimante sera utilisée. Ajoutez le périphérique dans l’onglet
Déclencheurs IoT, dans la colonne Périphérique en sélectionnant Ajouter une
ligne.

Vous pouvez alors lier l’imprimante à n’importe laquelle des options suivantes
dans le menu déroulant Actions : Imprimer des étiquettes, Imprimer l’opération
ou Imprimer le bon de livraison. Vous pouvez également ajouter une clé pour
déclencher l’action.

Important

Le premier déclencheur répertorié sur le formulaire est choisi en premier.
L’ordre est donc important et ces déclencheurs peuvent être glissés dans
n’importe quel ordre.

Note

Sur l’écran de l”Ordre de travail, un graphique de statut indique si la base
de données est correctement connectée à l’imprimante.

Pour plus d'infos

[Intégrer des appareils
IoT](../../../inventory_and_mrp/manufacturing/management/using_work_centers.html#workcenter-
iot)

### Lier une imprimante aux rapports

Vous pouvez également lier un type de rapport à une certaine imprimante. Dans
l” _application IoT_ , allez au menu Périphériques et sélectionnez
l’imprimante souhaitée qui doit être configurée.

À partir de là, cliquez sur Modifier, allez à l’onglet Rapports à imprimer et
sélectionnez Ajouter une ligne. Dans la fenêtre qui s’affiche, cochez tous les
types de Rapport qui doivent être liés à cette imprimante.

![L'imprimante répertoriée dans le menu Périphériques
d'IoT.](../../../../_images/printers-listed.png)

Now, each time Print is selected in the control panel, instead of downloading
a PDF, a pop-up appears which displays all the printer(s) linked to the
report. Then Odoo sends the report to the selected printer(s), and
automatically prints it.

Pour plus d'infos

[Impression des commandes du
PdV](../../../sales/point_of_sale/restaurant/kitchen_printing.html)

Astuce

Vous pouvez également configurer les rapports dans le Menu technique avec le
[mode débogage](../../developer_mode.html#developer-mode) activé. Pour ce
faire, allez à l’application Paramètres ‣ Menu technique ‣ Actions ‣ Rapports.
Vous y trouverez le rapport individuel dans cette liste, où vous pouvez
définir le Périphérique IoT sur le rapport.

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

