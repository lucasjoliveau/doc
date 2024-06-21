# Connecter une balance

Vous pouvez connecter une balance à l”IoT box sur une base de données Konvergo ERP en
quelques étapes simples. Après la configuration, vous pouvez utiliser
l’application _Point de Vente_ pour peser les produits, ce qui est utile si
leurs prix sont calculés sur la base de leur poids.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>In EU member states, <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG">certification is legally required</a>
to use a scale as an integrated device.</p></li>
<li><p>Konvergo ERP is not certified in several countries, including France, Germany, and Switzerland. If you
reside in one of these countries, you can still use a scale but without integration to your
Konvergo ERP database.</p></li>
<li><p>Alternatively, you have the option to acquire a <em>non-integrated</em> certified scale that prints
certified labels, which can then be scanned into your Konvergo ERP database.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG">Directive 2014/31/EU of the European Parliament</a></p>
</div>

## Connexion

Pour lier la balance à l”IoT box, connectez-la avec un câble USB.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans certains cas, vous aurez besoin d’un port série vers adaptateur <abbr title="Universal Serial Bus">USB</abbr>.</p>
</div>

Si la balance est [compatible avec l’IoT Box
d’Konvergo ERP](https://www.odoo.com/page/iot-hardware), il n’y a rien à configurer,
parce que la balance sera automatiquement détectée dès sa connexion.

![Détection automatique de l'IoT Box.](../../../../_images/iot-choice.png)

Il se peut que l”IoT box doive être redémarrée et que les pilotes de la
balance doivent être téléchargés sur la box dans certains cas. Pour mettre à
jour les pilotes, allez à la page d’accueil de l”IoT box et cliquez sur la
**Liste des pilotes**. Cliquez ensuite sur **Charger les pilotes**.

![Vue des paramètres de l'IoT Box et de la liste des
pilotes.](../../../../_images/driver-list.png)

Si le chargement des pilotes ne permet toujours pas de faire fonctionner la
balance, il se peut que la balance ne soit pas compatible avec l”IoT box
d’Konvergo ERP. Dans ce cas, vous devez utiliser une autre balance.

## Utiliser une balance dans un système de point de vente (PdV)

Pour utiliser la balance dans l’application *Point de Vente, allez à
l’application PdV ‣ Menu à trois points sur le PdV ‣ Paramètres, puis activez
la fonctionnalité IoT box. Une fois cela fait, la balance peut être
configurée.

Sélectionnez la balance dans le menu déroulant **Balance électronique**.
Cliquez ensuite sur **Enregistrer** pour enregistrer les changements, le cas
échéant.

![Liste des outils externes qui peuvent être utilisés avec Point de Vente et
l'IoT Box.](../../../../_images/electronic-scale-feature.png)

La balance est désormais disponible dans toutes les sessions du PdV. Si un
produit a un produit basé sur le poids, le fait de cliquer sur l’écran **PdV**
ouvre l’écran de la balance, où le caissier peut peser le produit et ajouter
le bon prix au panier.

![Vue du tableau de bord de la balance électronique lorsqu'aucun article n'est
pesé.](../../../../_images/scale-view.png)

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus
  *[PdV]: Point de Vente

