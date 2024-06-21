# Connecter une IoT box à Konvergo ERP

Une IoT (Internet of Things - Internet des objets) box est un dispositif
micro-informatique qui permet de connecter des périphériques d’entrée et de
sortie à une base de données Konvergo ERP. Un abonnement à l”IoT box est nécessaire
pour utiliser l”IoT box avec une connexion sécurisée. Un ordinateur est
également nécessaire pour configurer l”IoT box.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odoo.com/app/iot-faq">FAQ IoT Box</a></p>
</div>

Commencez le processus de configuration de l”IoT en [installant l’application
IoT](../../apps_modules#general-install) sur la base de données Konvergo ERP via
l’application Apps.

![L'application Internet of Things \(IoT\) sur la base de données
Konvergo ERP.](../../../../_images/install-iot-app.png)

Ensuite, après avoir installé l” _app IoT_ , allez à l’application IoT ‣ IoT
Box et cliquez sur le bouton **Connecter** situé dans le coin supérieur gauche
du tableau de bord des IoT Box.

![Connecter une IoT Box à la base de données
Konvergo ERP.](../../../../_images/connect-iot.png)

Nous recommandons deux façons de connecter l”IoT box à la base de données
après l’installation de l” _application IoT_. Suivez les étapes de l’une des
deux sections pour connecter l”IoT box via une connexion Ethernet câblée ou
via WiFi.

![Étapes de connexion pour une connexion câblée ou une connexion
WiFi.](../../../../_images/connect-iot-box.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The disk image that the <abbr title="Internet of Things">IoT</abbr> box SD card is formatted with is unique
to the version of the Konvergo ERP database that the <abbr title="Internet of Things">IoT</abbr> box is running on.
Ensure that the <abbr title="Internet of Things">IoT</abbr> box is <a href="updating_iot#iot-config-flash"><span class="std std-ref">flashed</span></a> with
the most up-to-date disk image.</p>
</div>

## Connexion Ethernet

Vous trouverez ci-après la procédure à suivre pour connecter l”IoT box à la
base de données Konvergo ERP via un câble Ethernet (par l’intermédiaire du port
Ethernet; RJ-45).

Tout d’abord, connectez tous les périphériques câblés à l”IoT box (ethernet,
périphériques USB, etc.). Un écran HDMI doit au moins être connecté. Branchez
ensuite l”IoT box sur une source d’alimentation.

Immédiatement après la mise sous tension et le démarrage de l’unité, lisez le
_code d’appariement_ sur l’écran ou sur la page imprimée par une imprimante de
reçus connectée à l”IoT box.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Par défaut, l”<abbr title="Internet of Things">IoT</abbr> box affiche le <em>code d’appariement</em> pendant un maximum de 5 minutes après le démarrage de l’unité. Après 5 minutes, le <em>code d’appariement</em> disparaît pour des raisons de sécurité et l”<abbr title="Internet of Things">IoT</abbr> box doit être redémarrée manuellement en débranchant l’unité de la source d’alimentation pendant dix secondes et en la rebranchant.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si aucun écran n’est relié à l”<abbr title="Internet of Things">IoT</abbr> box, le <em>code d’appariement</em> est accessible à partir de la page d’accueil de l”<abbr title="Internet of Things">IoT</abbr> box en cliquant sur le bouton <b>Affichage PdV</b>. Consultez <a href="#iot-connect-token"><span class="std std-ref">Connecter l’IoT Box manuellement à l’aide du jeton</span></a> pour savoir comment accéder à la page d’accueil de l”<abbr title="Internet of Things">IoT</abbr> box.</p>
</div>

Sur l’ordinateur, allez à l’application IoT ‣ IoT Box, puis cliquez sur le
bouton **Connecter** situé dans le coin supérieur gauche du tableau de bord
des IoT Box. Saisissez le _code d’appariement_ dans le champ **Code
d’appariement** et cliquez sur le bouton **Appairer**. La base de données est
maintenant connectée à l”IoT box et celle-ci apparaît sur la page des IoT Box.

## Connexion WiFi

Vous trouverez ci-après la procédure à suivre pour connecter l”IoT box à la
base de données Konvergo ERP via une connexion WiFi.

Tout d’abord, assurez-vous qu’aucun câble Ethernet n’est branché sur l”IoT
box. Ensuite, connectez tous les périphériques câblés à l”IoT box
(périphériques USB, etc.).

Après avoir connecté les périphériques, branchez l”IoT box sur une source
d’alimentation. Sur l’ordinateur, allez à l’application IoT ‣ IoT Box, puis
cliquez sur le bouton **Connecter** situé dans le coin supérieur gauche du
tableau de bord des IoT Box. Copiez ensuite le **Jeton** de la section
**connexion WiFi** , car il sera utilisé ultérieurement pour connecter la base
de données Konvergo ERP à l”IoT box.

De retour sur l’ordinateur, allez aux réseaux WiFi disponibles et connectez-
vous au réseau WiFi de l”IoT box. Le réseau WiFi diffusé par l”IoT box
commencera par `IoTBox-xxxxxxxxxx`.

![Réseaux WiFi disponibles sur l'ordinateur.](../../../../_images/connect-iot-
wifi.png)

Lors de la connexion au WiFi de l”IoT box, un navigateur sera automatiquement
redirigé vers l’assistant de Configuration de l’Iot Box. Donnez un nom à l”IoT
box, puis collez le _jeton_ précédemment copié dans le champ **Jeton de
serveur** et cliquez sur **Suivant**.

![Saisissez le jeton de serveur dans l'IoT box.](../../../../_images/server-
token.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si l’assistant de connexion WiFi de l”<abbr title="Internet of Things">IoT</abbr> box ne démarre pas, consultez la documentation relative à la <a href="#iot-connect-token"><span class="std std-ref">connexion à l’aide d’un jeton</span></a>.</p>
</div>

Choisissez à présent le réseau WiFi auquel l”IoT box se connectera (saisissez
le mot de passe s’il y en a un) et cliquez sur **Connecter**. Attendez
quelques secondes et le navigateur sera redirigé vers la page d’accueil de
l”IoT box. Il se peut que l’ordinateur doive être reconnecté manuellement à la
connexion WiFi d’origine si cela ne se fait pas automatiquement.

![Configurer le WiFi pour l'IoT box.](../../../../_images/configure-wifi-
network-iot.png)

Après avoir effectué chaque étape, l”IoT box devrait apparaître lorsque vous
allez à l’application IoT ‣ IoT Box sur la base de données Konvergo ERP.

![L'IoT Box a été configuré avec succès sur la base de données
Konvergo ERP.](../../../../_images/iot-box-connected.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il se peut que l”<abbr title="Internet of Things">IoT</abbr> box doive être redémarrée manuellement après avoir réussi à se connecter via le WiFi pour la box apparaisse dans l”<em>application IoT</em> sur la base de données Konvergo ERP. Pour ce faire, il suffit de débrancher l’appareil et de le rebrancher sur la source d’alimentation après dix secondes.</p>
</div>

## Connecter l’IoT Box manuellement à l’aide du jeton

Vous pouvez connecter l”IoT box manuellement à l’application IoT à l’aide du
_jeton_ , à partir d’un ordinateur. Vous pouvez trouver le _jeton_ en allant à
l’application IoT ‣ IoT Box et en cliquant sur **Connecter**.

Dans la section **Connexion WiFi** de la page **Connecter une IoT Box** qui
s’affiche, cliquez sur **Copier** à droite du **Jeton**. Ce jeton sera saisi
sur la page d’accueil de l”IoT box.

Accédez à la page d’accueil de l”IoT box en saisissant l’adresse IP de l”IoT
box dans une fenêtre de navigateur à partir d’un ordinateur sur le même réseau
que l”IoT box (de préférence via une connexion Ethernet).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est possible d’accéder à l’adresse <abbr title="Internet Protocol">IP</abbr> via la console d’administration du routeur auquel l”<abbr title="Internet of Things">IoT</abbr> box est connectée ou en connectant une imprimante de reçu à l”<abbr title="Internet of Things">IoT</abbr> box. Un reçu sera imprimé avec l’adresse <abbr title="Internet Protocol">IP</abbr> de l”<abbr title="Internet of Things">IoT</abbr> box.</p>
</div>

Sur la page d’accueil de l”IoT box, saisissez le _jeton_ dans la section
**Serveur** en cliquant sur **Configurer**. Puis collez le _jeton_ dans le
champ **Jeton de serveur** et cliquez sur **Connecter**. L”IoT box sera alors
connectée à la base de données Konvergo ERP.

## Schéma de l’IoT Box

### Raspberry Pi 4

![../../../../_images/iot-box-schema.png](../../../../_images/iot-box-
schema.png)

Le schéma de l’IoT box d’Konvergo ERP (Raspberry Pi 4) avec indications.

### Raspberry Pi 3

![../../../../_images/iox-box-schema-3.png](../../../../_images/iox-box-
schema-3.png)

Le schéma de l’IoT box d’Konvergo ERP (Raspberry Pi 3) avec indications.

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus
  *[IP]: Internet Protocol

