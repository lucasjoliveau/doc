# Connecter un écran

Dans Konvergo ERP, une IoT box peut être connectée à un écran. Après l’avoir
configuré, l’écran peut être utilisé pour afficher une commande Point de Vente
(PdV) à un client.

![../../../../_images/screen-pos-client-
display.png](../../../../_images/screen-pos-client-display.png)

Un exemple d’une commande de PdV (Point de Vente) sur un écran.

Accédez à l’écran client en allant à la page d’accueil de l”IoT box et en
cliquant sur le bouton **Affichage PdV**. Vous pouvez accéder à la page
d’accueil de l”IoT box en allant à l’application IoT ‣ IoT Box et en cliquant
sur le lien de la page d’accueil de l”IoT box.

## Connexion

La façon de connecter l’écran à l”IoT box dépend du modèle.

IoT Box model 4IoT Box model 3

Connectez jusqu’à deux écrans à l’aide de câbles micro-HDMI situés sur le côté
de l”IoT box. Deux écrans connectés peuvent diffuser différents contenus (voir
Utilisation de l’écran).

Connectez l’écran à l’aide d’un câble HDMI sur le côté de l”IoT box.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../config/connect#iot-connect-schema"><span class="std std-ref">Voir le schéma Raspberry Pi</span></a>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Vous devez connecter l’écran ou les écrans avant d’allumer l”<abbr title="Internet of Things">IoT</abbr> box. Si elle est déjà allumée, connectez l’écran ou les écrans et redémarrez l”<abbr title="Internet of Things">IoT</abbr> box en la débranchant pendant dix secondes et en la rebranchant sur sa source d’alimentation.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>L’utilisation d’adaptateurs HDMI/micro HDMI peut entraîner des problèmes qui se traduiront par un écran noir vide. Il est recommandé d’utiliser un câble spécifique pour la connexion de l’écran.</p>
</div>

Si la connexion a réussi, l’écran doit afficher l”**affichage client du PdV**.

![L'Affichage client PdV par défaut qui s'affiche lorsqu'un écran est connecté
avec succès à une IoT box.](../../../../_images/screen-pos-client-display-no-
order.png)

L’écran doit également apparaître dans la liste des **Écrans** sur la page
d’accueil de l”IoT box. Il est également possible de voir l’écran en allant à
l’application IoT ‣ Périphériques.

![Un exemple d'un nom d'écran affiché sur la page d'accueil de l'IoT
box.](../../../../_images/screen-screen-name-example.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si aucun écran n’est sélectionné, un écran par défaut intitulé <b>Écran distant</b> sera utilisé à la place. Cela indique qu’aucun matériel n’est connecté.</p>
<blockquote>
<div><img alt="Le nom d'écran &quot;Affichage distant&quot; sera utilisé si aucun écran n'est détecté." class="align-center" src="../../../../_images/screen-no-screen.png"/>
</div></blockquote>
</div>

## Utilisation

### Afficher les commandes du Point de Vente aux clients

Pour utiliser l’écran dans l” _application Point de Vente_ , allez à Point de
Vente ‣ Configuration ‣ Point de Vente, sélectionnez un PdV, cliquez sur
**Modifier** si nécessaire et activez la fonctionnalité **IoT Box**.

Sélectionnez ensuite l’écran dans le menu déroulant **Affichage client**.
Cliquez ensuite sur **Enregistrer** , le cas échéant.

![Connecter l'écran à l'application Point de
Vente.](../../../../_images/screen-pos-screen-config.png)

L’écran est à présent disponible pour les sessions de PdV. Une icône d’écran
s’affiche dans le menu en haut de l’écran pour indiquer le statut de connexion
de l’écran.

![L'icône "écran" sur l'affichage du Point de Vente affiche le statut de la
connexion avec l'écran.](../../../../_images/screen-pos-icon.png)

L’écran affiche automatiquement les commandes du PdV et se met à jour lorsque
des modifications sont apportées à la commande.

![Un exemple d'écran affichant une commande du
PdV.](../../../../_images/screen-pos-client-display.png)

### Afficher un site web à l’écran

Ouvrez la vue de formulaire de l’écran en allant à l’application IoT ‣
Périphériques ‣ Affichage client. Cette fonctionnalité permet à l’utilisateur
de choisir une URL de site web à afficher à l’écran en complétant le champ
**Afficher l’URL**.

  *[IoT]: Internet of Things
  *[PdV]: Point de Vente

