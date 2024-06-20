# Connecter une IoT box à Odoo

Une IoT (Internet of Things - Internet des objets) box est un dispositif
micro-informatique qui permet de connecter des périphériques d’entrée et de
sortie à une base de données Odoo. Un abonnement à l”IoT box est nécessaire
pour utiliser l”IoT box avec une connexion sécurisée. Un ordinateur est
également nécessaire pour configurer l”IoT box.

Pour plus d'infos

[FAQ IoT Box](https://www.odoo.com/app/iot-faq)

Commencez le processus de configuration de l”IoT en [installant l’application
IoT](../../apps_modules.html#general-install) sur la base de données Odoo via
l’application Apps.

![L'application Internet of Things \(IoT\) sur la base de données
Odoo.](../../../../_images/install-iot-app.png)

Ensuite, après avoir installé l” _app IoT_ , allez à l’application IoT ‣ IoT
Box et cliquez sur le bouton Connecter situé dans le coin supérieur gauche du
tableau de bord des IoT Box.

![Connecter une IoT Box à la base de données
Odoo.](../../../../_images/connect-iot.png)

Nous recommandons deux façons de connecter l”IoT box à la base de données
après l’installation de l” _application IoT_. Suivez les étapes de l’une des
deux sections pour connecter l”IoT box via une connexion Ethernet câblée ou
via WiFi.

![Étapes de connexion pour une connexion câblée ou une connexion
WiFi.](../../../../_images/connect-iot-box.png)

Important

The disk image that the IoT box SD card is formatted with is unique to the
version of the Odoo database that the IoT box is running on. Ensure that the
IoT box is [flashed](updating_iot.html#iot-config-flash) with the most up-to-
date disk image.

## Connexion Ethernet

Vous trouverez ci-après la procédure à suivre pour connecter l”IoT box à la
base de données Odoo via un câble Ethernet (par l’intermédiaire du port
Ethernet; RJ-45).

Tout d’abord, connectez tous les périphériques câblés à l”IoT box (ethernet,
périphériques USB, etc.). Un écran HDMI doit au moins être connecté. Branchez
ensuite l”IoT box sur une source d’alimentation.

Immédiatement après la mise sous tension et le démarrage de l’unité, lisez le
_code d’appariement_ sur l’écran ou sur la page imprimée par une imprimante de
reçus connectée à l”IoT box.

Avertissement

Par défaut, l”IoT box affiche le _code d’appariement_ pendant un maximum de 5
minutes après le démarrage de l’unité. Après 5 minutes, le _code
d’appariement_ disparaît pour des raisons de sécurité et l”IoT box doit être
redémarrée manuellement en débranchant l’unité de la source d’alimentation
pendant dix secondes et en la rebranchant.

Note

Si aucun écran n’est relié à l”IoT box, le _code d’appariement_ est accessible
à partir de la page d’accueil de l”IoT box en cliquant sur le bouton Affichage
PdV. Consultez Connecter l’IoT Box manuellement à l’aide du jeton pour savoir
comment accéder à la page d’accueil de l”IoT box.

Sur l’ordinateur, allez à l’application IoT ‣ IoT Box, puis cliquez sur le
bouton Connecter situé dans le coin supérieur gauche du tableau de bord des
IoT Box. Saisissez le _code d’appariement_ dans le champ Code d’appariement et
cliquez sur le bouton Appairer. La base de données est maintenant connectée à
l”IoT box et celle-ci apparaît sur la page des IoT Box.

## Connexion WiFi

Vous trouverez ci-après la procédure à suivre pour connecter l”IoT box à la
base de données Odoo via une connexion WiFi.

Tout d’abord, assurez-vous qu’aucun câble Ethernet n’est branché sur l”IoT
box. Ensuite, connectez tous les périphériques câblés à l”IoT box
(périphériques USB, etc.).

Après avoir connecté les périphériques, branchez l”IoT box sur une source
d’alimentation. Sur l’ordinateur, allez à l’application IoT ‣ IoT Box, puis
cliquez sur le bouton Connecter situé dans le coin supérieur gauche du tableau
de bord des IoT Box. Copiez ensuite le Jeton de la section connexion WiFi, car
il sera utilisé ultérieurement pour connecter la base de données Odoo à l”IoT
box.

De retour sur l’ordinateur, allez aux réseaux WiFi disponibles et connectez-
vous au réseau WiFi de l”IoT box. Le réseau WiFi diffusé par l”IoT box
commencera par `IoTBox-xxxxxxxxxx`.

![Réseaux WiFi disponibles sur l'ordinateur.](../../../../_images/connect-iot-
wifi.png)

Lors de la connexion au WiFi de l”IoT box, un navigateur sera automatiquement
redirigé vers l’assistant de Configuration de l’Iot Box. Donnez un nom à l”IoT
box, puis collez le _jeton_ précédemment copié dans le champ Jeton de serveur
et cliquez sur Suivant.

![Saisissez le jeton de serveur dans l'IoT box.](../../../../_images/server-
token.png)

Note

Si l’assistant de connexion WiFi de l”IoT box ne démarre pas, consultez la
documentation relative à la connexion à l’aide d’un jeton.

Choisissez à présent le réseau WiFi auquel l”IoT box se connectera (saisissez
le mot de passe s’il y en a un) et cliquez sur Connecter. Attendez quelques
secondes et le navigateur sera redirigé vers la page d’accueil de l”IoT box.
Il se peut que l’ordinateur doive être reconnecté manuellement à la connexion
WiFi d’origine si cela ne se fait pas automatiquement.

![Configurer le WiFi pour l'IoT box.](../../../../_images/configure-wifi-
network-iot.png)

Après avoir effectué chaque étape, l”IoT box devrait apparaître lorsque vous
allez à l’application IoT ‣ IoT Box sur la base de données Odoo.

![L'IoT Box a été configuré avec succès sur la base de données
Odoo.](../../../../_images/iot-box-connected.png)

Important

Il se peut que l”IoT box doive être redémarrée manuellement après avoir réussi
à se connecter via le WiFi pour la box apparaisse dans l” _application IoT_
sur la base de données Odoo. Pour ce faire, il suffit de débrancher l’appareil
et de le rebrancher sur la source d’alimentation après dix secondes.

## Connecter l’IoT Box manuellement à l’aide du jeton

Vous pouvez connecter l”IoT box manuellement à l’application IoT à l’aide du
_jeton_ , à partir d’un ordinateur. Vous pouvez trouver le _jeton_ en allant à
l’application IoT ‣ IoT Box et en cliquant sur Connecter.

Dans la section Connexion WiFi de la page Connecter une IoT Box qui s’affiche,
cliquez sur Copier à droite du Jeton. Ce jeton sera saisi sur la page
d’accueil de l”IoT box.

Accédez à la page d’accueil de l”IoT box en saisissant l’adresse IP de l”IoT
box dans une fenêtre de navigateur à partir d’un ordinateur sur le même réseau
que l”IoT box (de préférence via une connexion Ethernet).

Note

Il est possible d’accéder à l’adresse IP via la console d’administration du
routeur auquel l”IoT box est connectée ou en connectant une imprimante de reçu
à l”IoT box. Un reçu sera imprimé avec l’adresse IP de l”IoT box.

Sur la page d’accueil de l”IoT box, saisissez le _jeton_ dans la section
Serveur en cliquant sur Configurer. Puis collez le _jeton_ dans le champ Jeton
de serveur et cliquez sur Connecter. L”IoT box sera alors connectée à la base
de données Odoo.

## Schéma de l’IoT Box

### Raspberry Pi 4

![../../../../_images/iot-box-schema.png](../../../../_images/iot-box-
schema.png)

Le schéma de l’IoT box d’Odoo (Raspberry Pi 4) avec indications.

### Raspberry Pi 3

![../../../../_images/iox-box-schema-3.png](../../../../_images/iox-box-
schema-3.png)

Le schéma de l’IoT box d’Odoo (Raspberry Pi 3) avec indications.

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus
  *[IP]: Internet Protocol

