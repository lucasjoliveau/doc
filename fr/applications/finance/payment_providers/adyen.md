# Adyen

[Adyen](https://www.adyen.com/) est une entreprise basée aux Pays-Bas qui
propose plusieurs possibilités de paiement en ligne.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Adyen travaille uniquement avec des clients qui traitent <b>plus</b> de <b>10 millions par an</b> ou qui facturent un <b>minimum</b> de <b>1.000</b> transactions ** par mois**.</p>
</div>

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p>
</div>

### Onglet des identifiants

Konvergo ERP a besoin de vos **identifiants API** pour se connecter à votre compte
Adyen. Ils incluent :

  * **Compte marchand** : Le code du compte marchand à utiliser avec Adyen.

  * Clé API : La clé API de l’utilisateur du service web.

  * Clé client: La clé client de l’utilisateur du service web.

  * Clé HMAC: La clé HMAC du webhook.

  * URL Checkout API : L’URL de base pour les points de terminaison de Checkout API.

  * URL Recurring API: l’URL de base pour les points de terminaison de Recurring API.

Vous pouvez copier vos identifiants depuis votre compte Adyen et les coller
dans les champs associés dans l’onglet **Identifiants**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous essayez Adyen en tant que test, avec un <em>compte test</em> Adyen, allez à Comptabilité ‣ Configuration ‣ Fournisseurs de paiement. Cliquez sur <b>Adyen</b>, activez le <b>Mode test</b> et saisissez vos identifiants dans l’onglet <b>Identifiants</b>.</p>
</div>

#### Clé API et Clé client

Afin de récupérer la Clé API et la Clé client, connectez-vous à votre compte
Adyen, allez à Développeurs ‣ Identifiants API.

  * Si vous avez déjà un utilisateur API, ouvrez-le.

  * Si vous n’avez pas encore d’utilisateur API, cliquez sur **Créer de nouveaux identifiants**.

Allez aux Paramètres du serveur ‣ Authentification et copiez ou générez votre
**Clé API**. Veillez à copier votre clé API, car vous ne serez pas autorisé à
l’obtenir plus tard sans en générer une nouvelle.

À présent, allez aux Paramètres client ‣ Authentification et copiez ou générez
votre **Clé client**. Vous y pouvez également autoriser les paiements à partir
de votre site web.

#### Clé HMAC

Afin de récupérer la Clé HMAC, vous devez configurer un webhook de
`notification standard`. Pour ce faire, connectez-vous à votre compte Adyen et
allez à Développeurs ‣ Webhooks ‣ Ajouter un webhook ‣ Ajouter notification
standard.

![Configurez un webhook.](../../../_images/adyen-add-webhook.png)

Ensuite, dans Général ‣ Configuration du serveur ‣ URL, saisissez l’adresse de
votre serveur suivie de `/payment/adyen/notification`.

![Saisissez l'URL de notification.](../../../_images/adyen-webhook-url.png)

Saisissez ensuite Sécurité ‣ Clé HMAC ‣ Générer. Veillez à copier la clé, car
vous ne serez plus autorisé à l’obtenir plus tard sans en générer une
nouvelle.

![Générez une clé HMAC et enregistrez-la.](../../../_images/adyen-hmac-
key.png)

Vous devez enregistrer le webhook pour finaliser sa création.

#### URLs API

Toutes les URLs de l’API Adyen incluent un préfixe spécifique à la zone du
client généré par Adyen. Pour configurer les URLs, suivez les étapes suivantes
:

  1. Connectez-vous à votre compte Adyen et allez à Développeurs ‣ URLs API.

  2. Copiez le **Préfixe** pour votre zone de client en direct (c’est-à-dire, le **centre de données**) et enregistrez-le pour plus tard.

![Copiez le préfixe pour les API Adyen](../../../_images/adyen-api-urls.png)

  3. Dans Konvergo ERP, [allez au fournisseur de paiement Adyen](../payment_providers#payment-providers-add-new).

  4. Dans le champ **URL Checkout API** , saisissez l’URL suivante et remplacez `yourprefix` par le préfixe que vous avez précédemment enregistré : `https://yourprefix-checkout-live.adyenpayments.com/checkout`

  5. Dans le champ **URL Recurring API** , saisissez l’URL suivante et remplacez `yourprefix` par le préfixe que vous avez précédemment enregistré : `https://yourprefix-pal-live.adyenpayments.com/pal/servlet/Recurring`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous testez Adyen, vous pouvez plutôt utiliser les URLs suivantes :</p>
<ul>
<li><p><b>URL Checkout API</b> : <code>https://checkout-test.adyen.com</code></p></li>
<li><p><b>URL Recurring API</b> : <code>https://pal-test.adyen.com/pal/servlet/Recurring</code></p></li>
</ul>
</div>

### Compte d’Adyen

#### Autoriser les paiements d’une origine spécifique

Pour autoriser les paiements provenant de votre site web, suivez les étapes
dans Clé API et Clé client pour aller à votre utilisateur API, puis aller à
Ajouter les origines autorisées, puis ajoutez les URLs à partir desquelles les
paiements seront effectués (les URLs des serveurs hébergeant vos instances
Konvergo ERP).

![Autorise les paiements provenant d'un domaine
spécifique.](../../../_images/adyen-allowed-origins.png)

### Faire une réservation sur une carte

Adyen vous permet de capturer un montant manuellement au lieu d’avoir une
capture immédiate.

To set it up, enable the **Capture Amount Manually** option on Konvergo ERP, as
explained in the [payment providers
documentation](../payment_providers#payment-providers-manual-capture).

Ensuite, ouvrez votre compte marchand Adyen, allez à Compte ‣ Paramètres et
définissez le **Délai de capture** sur **manuel**.

![Paramètres du délai de capture dans
Adyen](../../../_images/adyen_capture_delay.png) <div class="alert alert-warning">
<p class="alert-title">
Prudence</p><ul>
<li><p>Si vous configurez Konvergo ERP pour capturer les montants manuellement, veillez à configurer le <b>délai de capture</b> sur <b>manuel</b> dans Adyen. Sinon, la transaction sera bloquée au statut autorisé dans Konvergo ERP.</p></li>
<li><p>Konvergo ERP ne prend pas encore en charge la capture partielle. Sachez que si vous effectuez une capture partielle à partir de l’interface d’Adyen, Konvergo ERP la gérera comme s’il s’agissait d’une capture intégrale.</p></li>
</ul>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si la transaction n’a pas été capturée après <b>7 jours</b>, le client a le droit de la <b>révoquer</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers">Paiements en ligne</a></p>
</div>

