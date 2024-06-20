# Connecter une balance

Vous pouvez connecter une balance à l”IoT box sur une base de données Odoo en
quelques étapes simples. Après la configuration, vous pouvez utiliser
l’application _Point de Vente_ pour peser les produits, ce qui est utile si
leurs prix sont calculés sur la base de leur poids.

Important

  * In EU member states, [certification is legally required](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG) to use a scale as an integrated device.

  * Odoo is not certified in several countries, including France, Germany, and Switzerland. If you reside in one of these countries, you can still use a scale but without integration to your Odoo database.

  * Alternatively, you have the option to acquire a _non-integrated_ certified scale that prints certified labels, which can then be scanned into your Odoo database.

Pour plus d'infos

[Directive 2014/31/EU of the European Parliament](https://eur-
lex.europa.eu/legal-
content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)

## Connexion

Pour lier la balance à l”IoT box, connectez-la avec un câble USB.

Note

Dans certains cas, vous aurez besoin d’un port série vers adaptateur USB.

Si la balance est [compatible avec l’IoT Box
d’Odoo](https://www.odoo.com/page/iot-hardware), il n’y a rien à configurer,
parce que la balance sera automatiquement détectée dès sa connexion.

![Détection automatique de l'IoT Box.](../../../../_images/iot-choice.png)

Il se peut que l”IoT box doive être redémarrée et que les pilotes de la
balance doivent être téléchargés sur la box dans certains cas. Pour mettre à
jour les pilotes, allez à la page d’accueil de l”IoT box et cliquez sur la
Liste des pilotes. Cliquez ensuite sur Charger les pilotes.

![Vue des paramètres de l'IoT Box et de la liste des
pilotes.](../../../../_images/driver-list.png)

Si le chargement des pilotes ne permet toujours pas de faire fonctionner la
balance, il se peut que la balance ne soit pas compatible avec l”IoT box
d’Odoo. Dans ce cas, vous devez utiliser une autre balance.

## Utiliser une balance dans un système de point de vente (PdV)

Pour utiliser la balance dans l’application *Point de Vente, allez à
l’application PdV ‣ Menu à trois points sur le PdV ‣ Paramètres, puis activez
la fonctionnalité IoT box. Une fois cela fait, la balance peut être
configurée.

Sélectionnez la balance dans le menu déroulant Balance électronique. Cliquez
ensuite sur Enregistrer pour enregistrer les changements, le cas échéant.

![Liste des outils externes qui peuvent être utilisés avec Point de Vente et
l'IoT Box.](../../../../_images/electronic-scale-feature.png)

La balance est désormais disponible dans toutes les sessions du PdV. Si un
produit a un produit basé sur le poids, le fait de cliquer sur l’écran PdV
ouvre l’écran de la balance, où le caissier peut peser le produit et ajouter
le bon prix au panier.

![Vue du tableau de bord de la balance électronique lorsqu'aucun article n'est
pesé.](../../../../_images/scale-view.png)

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus
  *[PdV]: Point de Vente

