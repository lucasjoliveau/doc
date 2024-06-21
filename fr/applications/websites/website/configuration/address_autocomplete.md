# Autocomplétion des adresses

Vous pouvez utiliser l’API Google Places sur votre site web pour vous assurer
que les adresses de livraison de vos utilisateurs existent et que le
transporteur les comprend. L’API Google Places permet aux développeurs
d’accéder aux informations détaillées sur les lieux à l’aide de requêtes HTTP.
L’autocomplétion prédit une liste de lieux lorsque l’utilisateur commence à
taper l’adresse.

![Exemple d'autocomplétion d'une adresse](../../../../_images/address-
autocomplete-example.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://mapsplatform.google.com/maps-products">Plateforme Google Maps</a></p></li>
<li><p><a href="https://developers.google.com/maps/documentation/places/web-service/autocomplete">Documentation Développeur Google : API Google Places</a></p></li>
</ul>
</div>

Pour ce faire, allez au Site Web ‣ Configuration ‣ Paramètres et activez
l”**Autocomplétion des adresses** dans la section **Référencement**.

![Activez l'autocomplétion des adresses](../../../../_images/enable-address-
autocomplete.png)

Insérez votre **Clé API Google Places** dans le champ **Clé API**. Si vous
n’en avez pas, créez la vôtre dans la [Console Google
Cloud](https://console.cloud.google.com/getting-started) et suivez les étapes
suivantes.

## Étape 1 : Activer l’API Google Places

**Create a New Project:** To enable the **Google Places API** , you first need
to create a project. To do so, click **Select a project** in the top left
corner, **New Project** , and follow the prompts to set up your project.

**Enable the Google Places API:** Go to the **Enabled APIs & Services** and
click **\+ ENABLE APIS AND SERVICES.** Search for **« Places API »** and
select it. Click on the **« Enable »** button.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le tarif de Google dépend du nombre de requêtes et de leur complexité.</p>
</div>

## Étape 2 : Créer des identifiants d’API

Allez à [API & Services –>
Identifiants](https://console.cloud.google.com/apis/credentials).

**Create credentials:** To create your credentials, go to **Credentials** ,
click **Create Credentials** , and select **API key**.

<div class="admonition-restrict-the-api-key-optional alert">
<p class="alert-title">
Restreindre la Clé API (Facultatif)</p><p>Pour des raisons de sécurité, vous pouvez restreindre l’utilisation de votre clé API. Pour vous allez à la section <b>restrictions API</b> pour préciser à quelles API votre clé peut avoir accès. Pour l’API Google Places, vous pouvez la restreindre pour uniquement autoriser des requêtes de sites web ou d’applications spécifiques.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Save Your API Key: copy your API key and securely store it.</p></li>
<li><p>Ne la partagez pas publiquement et ne l’exposez pas dans un code côté client.</p></li>
</ul>
</div>

