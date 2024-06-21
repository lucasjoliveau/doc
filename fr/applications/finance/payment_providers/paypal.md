# PayPal

[Paypal](https://www.paypal.com/) est un fournisseur de paiement en ligne
américain disponible dans le monde entier, et l’un des rares à ne pas facturer
de frais d’abonnement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>While PayPal is available in <a href="https://www.paypal.com/webapps/mpp/country-worldwide">over 200 countries/regions</a>, only <a href="https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies">a selection of currencies are
supported</a>.</p>
</div>

## Paramètres dans PayPal

Pour accéder aux paramètres de votre compte PayPal, connectez-vous à PayPal,
ouvrez les **Paramètres du compte** et ouvrez le menu **Paiements sur site
marchand**.

![Menu du compte PayPal](../../../_images/paypal-account.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Notez que, pour que PayPal fonctionne <b>dans Konvergo ERP</b>, les options <a href="#paypal-auto-return"><span class="std std-ref">Renvoi automatique</span></a>, <a href="#paypal-pdt"><span class="std std-ref">PDT</span></a>, et <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a> <b>doivent</b> toutes être activées.</p>
</div>

### Renvoi automatique

La fonctionnalité **Renvoi automatique** redirige les clients automatiquement
vers Konvergo ERP une fois le paiement traité.

Depuis **Paiements sur site marchand** , allez à Préférences de réception de
paiements sur site marchand ‣ Mettre à jour ‣ Renvoi automatiquement pour les
paiements sur site marchand ‣ Renvoi automatique et sélectionnez **Activé**.
Saisissez l’adresse de votre base de données Konvergo ERP (par ex.
`https://yourcompany.odoo.com`) dans le champ **URL de renvoi** et
**enregistrez**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>N’importe quelle URL fait l’affaire. Konvergo ERP n’a besoin d’activer ce paramètre que parce qu’il utilise une autre URL.</p>
</div>

### Transfert des données de paiement (PDT)

Le PDT permet de recevoir des confirmations de paiement, d’afficher le statut
du paiement aux clients et de vérifier l’authenticité des paiements. Dans
Préférences de réception de paiements sur site marchand ‣ Mettre à jour,
faites défiler jusqu’à **Transfert des données de paiement** et sélectionnez
**Activé**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>PayPal affiche votre <b>Jeton d’identité PDT</b> dès que les options <a href="#paypal-auto-return"><span class="std std-ref">Renvoi automatique</span></a> et <a href="#paypal-pdt"><span class="std std-ref">Transfert des données de paiement (PDT)</span></a> sont activées. Si vous avez besoin du <b>Jeton d’identité PDT</b>, désactivez et réactivez le <b>Transfert des données de paiement</b> pour afficher à nouveau le jeton.</p>
</div>

### Notification instantanée de paiement (IPN)

L’option IPN est similaire au **PDT** , mais permet d’envoyer davantage de
notifications, telles que des notifications de rétrofacturation. Pour activer
l’option **IPN** , allez à Paiements sur site marchand ‣ Notifications
instantanées de paiement ‣ Mettre à jour et cliquez sur **Choisir les
paramètres IPN**. Saisissez une **URL de notification** , sélectionnez
**Recevoir messages IPN (Activé)** , et **enregistrez**.

### Compte PayPal facultatif

Nous conseillons de ne pas demander aux clients de se connecter avec un compte
PayPal lors du paiement. Il est préférable et plus accessible pour les clients
de payer avec une carte de crédit/débit. Pour désactiver cette invite, allez à
Paramètres du compte ‣ Paiements sur site marchand ‣ Mettre à jour et
sélectionnez **Activé** pour l’option **Compte PayPal facultatif**.

### Format des messages de paiement

Si vous utilisez des caractères accentués (ou autre chose que des caractères
latins primaires) pour les noms ou les adresses des clients, vous **devez**
configurer le format d’encodage de la demande de paiement envoyée par Konvergo ERP à
PayPal. Si vous ne le faites pas, certaines transactions échoueront sans
notification.

Pour ce faire, allez à [votre compte de
production](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-
language-encoding). Cliquez ensuite sur **Plus d’options** et définissez les
deux formats d’encodage par défaut comme **UTF-8**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Pour les paiements cryptés sur site web et l’erreur EWP_SETTINGS, consultez la <a href="https://developer.paypal.com/docs/online/">documentation Paypal</a>.</p></li>
<li><p>Configurez votre <a href="#paypal-testing"><span class="std std-ref">compte Paypal Sandbox</span></a>, puis suivez ce <a href="https://sandbox.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding">lien</a> pour configurer le format d’encodage dans un environnement de test.</p></li>
</ul>
</div>

## Paramètres dans Konvergo ERP

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p>
</div>

### Identifiants

Konvergo ERP a besoin de vos **Identifiants API** pour se connecter à votre compte
PayPal. Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Fournisseurs de
paiement et **activez** PayPal. Ensuite, saisissez vos identifiants de compte
PayPal dans l’onglet **Identifiants** :

  * **Email** : l’adresse email de connexion à PayPal ;

  * **Jeton d’identité PDT** : la clé utilisée pour vérifier l’authenticité des transactions ;

  * **Utiliser IPN** : activez cette option pour que PayPal fonctionne correctement dans Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Enregistrez le <b>Jeton d’identité PDT</b> pour plus tard.</p>
</div>

Pour définir le **Jeton d’identité PDT** , activez le [mode
développeur](../../general/developer_mode#developer-mode) et récupérez le
jeton en suivant les étapes de configuration de Transfert des données de
paiement (PDT).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L”<b>Identifiant du marchand</b> de PayPal n’est pas requis dans Konvergo ERP.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous testez PayPal avec un <a href="#paypal-testing"><span class="std std-ref">compte PayPal Sandbox</span></a>, définissez le <b>Statut</b> sur <b>Mode test</b>. Nous vous recommandons de le faire sur une base de données de test Konvergo ERP, plutôt que sur votre base de données principale.</p>
</div>

### Frais supplémentaires

You can charge [extra fees](../payment_providers#payment-providers-extra-
fees) to customers choosing to pay with PayPal in order to cover the
transaction fees PayPal charges you.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Vous pouvez vous référer à <a href="https://www.paypal.com/webapps/mpp/paypal-fees">Frais Paypal</a> afin de configurer les frais.</p></li>
<li><p><a href="https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index_en.htm">Les commerçants de l’UE</a> ne sont pas autorisés à facturer des frais pour les paiements par carte de crédit.</p></li>
</ul>
</div>

## Environnement de test

### Configuration

Grâce aux comptes sandbox de PayPal, vous pouvez tester l’ensemble du flux de
paiement dans Konvergo ERP.

Connectez-vous au [Site de développeur de
PayPal](https://developer.paypal.com/) avec vos identifiants PayPal, ce qui
crée deux comptes sandbox :

  * Un compte professionnel (à utiliser en tant que marchand, par ex. [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator%40example.com));

  * Un compte personnel par défaut (à utiliser en tant qu’acheteur, par ex. [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer%40example.com)).

Connectez-vous au sandbox PayPal avec votre compte professionnel et suivez les
mêmes instructions de configuration. Saisissez vos identifiants sandbox dans
Konvergo ERP (Comptabilité ‣ Configuration ‣ Fournisseurs de paiement ‣ PayPal dans
l’onglet **Identifiants** et assurez-vous que le statut est défini sur **Mode
test**. Nous recommandons de faire cela sur une base de données Konvergo ERP, plutôt
que sur votre base de données principale.

Lancez une transaction test depuis Konvergo ERP en utilisant le compte personnel
sandbox.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Notez que, pour que PayPal fonctionne <b>dans Konvergo ERP</b>, les options <a href="#paypal-auto-return"><span class="std std-ref">Renvoi automatique</span></a>, <a href="#paypal-pdt"><span class="std std-ref">PDT</span></a>, et <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a> <b>doivent</b> toutes être activées.</p>
</div>0

  *[PDT]: Transfert des données de paiement
  *[IPN]: Notification instantanée de paiement

