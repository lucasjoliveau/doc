# Connecter une pédale de commande

Lorsque vous travaillez dans un environnement de fabrication, il est toujours
préférable pour un opérateur d’avoir les deux mains libres à tout moment.
L”IoT box d’Konvergo ERP permet d’utiliser une pédale de commande.

En effet, avec une pédale de commande, l’opérateur peut passer d’un écran à
l’autre et effectuer des actions en utilisant son pied. Cette fonctionnalité
peut être configurée en quelques étapes sur le poste de travail dans
l’application _Fabrication_.

## Connexion

Pour connecter une pédale de commande à l”IoT box, il suffit de relier les
deux appareils par un câble. Le plus souvent, cela se fait à l’aide d’un câble
USB.

Si la pédale de commande est un [périphérique pris en
charge](https://www.odoo.com/page/iot-hardware), vous ne devez rien
configurer, car le périphérique sera automatiquement détecté dès sa connexion.

![Pédale de commande reconnue par l'IoT box.](../../../../_images/footswitch-
dropdown.png)

## Lier une pédale de commande à un post de travail dans l’application
Fabrication d’Konvergo ERP.

Pour lier une pédale de commande à une action, elle doit d’abord être
configurée sur un poste de travail. Allez à l’application Fabrication ‣
Configuration ‣ Postes de travail. Ensuite, allez au **Poste de travail**
souhaité sur lequel la pédale de commande sera utilisée et ajoutez le
périphériques dans l’onglet **Déclencheurs IoT** , dans la colonne
**Périphérique** , en sélectionnant **Ajouter une ligne**. Cela signifie aussi
que la pédale de commande peut être liée à une option dans la colonne
déroulante **Action** et il est possible d’ajouter une clé pour la déclencher.
Une exemple d’une **Action** dans l’application _Fabrication_ pourrait être
les boutons **Valider** ou **Marquer comme fait** sur un ordre de travail de
fabrication.

![Configuration du déclenchement de la pédale de commande dans la base de
données Konvergo ERP](../../../../_images/footswitch-example.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il faut noter que le premier déclencheur répertorié est choisi en premier. L’ordre est donc important et ces déclencheurs peuvent être glissés dans n’importe quel ordre. Dans l’image ci-dessus, l’utilisation de la pédale de commande permet de sauter automatiquement la partie du processus sur laquelle vous êtes en train de travailler.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sur l’écran de l”<b>Ordre de travail</b>, un graphique de statut indique si la base de données est correctement connectée à la pédale de commande.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Intégrer des appareils IoT</span></a></p>
</div>

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

