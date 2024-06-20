# PayPal

[Paypal](https://www.paypal.com/) est un fournisseur de paiement en ligne
américain disponible dans le monde entier, et l’un des rares à ne pas facturer
de frais d’abonnement.

Note

While PayPal is available in [over 200
countries/regions](https://www.paypal.com/webapps/mpp/country-worldwide), only
[a selection of currencies are
supported](https://developer.paypal.com/docs/reports/reference/paypal-
supported-currencies).

## Paramètres dans PayPal

Pour accéder aux paramètres de votre compte PayPal, connectez-vous à PayPal,
ouvrez les Paramètres du compte et ouvrez le menu Paiements sur site marchand.

![Menu du compte PayPal](../../../_images/paypal-account.png)

Important

Notez que, pour que PayPal fonctionne **dans Odoo** , les options Renvoi
automatique, PDT, et IPN **doivent** toutes être activées.

### Renvoi automatique

La fonctionnalité **Renvoi automatique** redirige les clients automatiquement
vers Odoo une fois le paiement traité.

Depuis Paiements sur site marchand, allez à Préférences de réception de
paiements sur site marchand ‣ Mettre à jour ‣ Renvoi automatiquement pour les
paiements sur site marchand ‣ Renvoi automatique et sélectionnez Activé.
Saisissez l’adresse de votre base de données Odoo (par ex.
`https://yourcompany.odoo.com`) dans le champ URL de renvoi et enregistrez.

Note

N’importe quelle URL fait l’affaire. Odoo n’a besoin d’activer ce paramètre
que parce qu’il utilise une autre URL.

### Transfert des données de paiement (PDT)

Le PDT permet de recevoir des confirmations de paiement, d’afficher le statut
du paiement aux clients et de vérifier l’authenticité des paiements. Dans
Préférences de réception de paiements sur site marchand ‣ Mettre à jour,
faites défiler jusqu’à Transfert des données de paiement et sélectionnez
Activé.

Astuce

PayPal affiche votre **Jeton d’identité PDT** dès que les options Renvoi
automatique et Transfert des données de paiement (PDT) sont activées. Si vous
avez besoin du **Jeton d’identité PDT** , désactivez et réactivez le Transfert
des données de paiement pour afficher à nouveau le jeton.

### Notification instantanée de paiement (IPN)

L’option IPN est similaire au **PDT** , mais permet d’envoyer davantage de
notifications, telles que des notifications de rétrofacturation. Pour activer
l’option **IPN** , allez à Paiements sur site marchand ‣ Notifications
instantanées de paiement ‣ Mettre à jour et cliquez sur Choisir les paramètres
IPN. Saisissez une URL de notification, sélectionnez Recevoir messages IPN
(Activé), et enregistrez.

### Compte PayPal facultatif

Nous conseillons de ne pas demander aux clients de se connecter avec un compte
PayPal lors du paiement. Il est préférable et plus accessible pour les clients
de payer avec une carte de crédit/débit. Pour désactiver cette invite, allez à
Paramètres du compte ‣ Paiements sur site marchand ‣ Mettre à jour et
sélectionnez Activé pour l’option Compte PayPal facultatif.

### Format des messages de paiement

Si vous utilisez des caractères accentués (ou autre chose que des caractères
latins primaires) pour les noms ou les adresses des clients, vous **devez**
configurer le format d’encodage de la demande de paiement envoyée par Odoo à
PayPal. Si vous ne le faites pas, certaines transactions échoueront sans
notification.

Pour ce faire, allez à [votre compte de
production](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-
language-encoding). Cliquez ensuite sur Plus d’options et définissez les deux
formats d’encodage par défaut comme UTF-8.

Astuce

  * Pour les paiements cryptés sur site web et l’erreur EWP_SETTINGS, consultez la [documentation Paypal](https://developer.paypal.com/docs/online/).

  * Configurez votre compte Paypal Sandbox, puis suivez ce [lien](https://sandbox.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding) pour configurer le format d’encodage dans un environnement de test.

## Paramètres dans Odoo

Pour plus d'infos

[Enable a payment provider](../payment_providers.html#payment-providers-add-
new)

### Identifiants

Odoo a besoin de vos **Identifiants API** pour se connecter à votre compte
PayPal. Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Fournisseurs de
paiement et activez PayPal. Ensuite, saisissez vos identifiants de compte
PayPal dans l’onglet Identifiants :

  * Email : l’adresse email de connexion à PayPal ;

  * Jeton d’identité PDT : la clé utilisée pour vérifier l’authenticité des transactions ;

  * Utiliser IPN : activez cette option pour que PayPal fonctionne correctement dans Odoo.

Astuce

Enregistrez le Jeton d’identité PDT pour plus tard.

Pour définir le Jeton d’identité PDT, activez le [mode
développeur](../../general/developer_mode.html#developer-mode) et récupérez le
jeton en suivant les étapes de configuration de Transfert des données de
paiement (PDT).

Note

L”**Identifiant du marchand** de PayPal n’est pas requis dans Odoo.

Important

Si vous testez PayPal avec un compte PayPal Sandbox, définissez le Statut sur
Mode test. Nous vous recommandons de le faire sur une base de données de test
Odoo, plutôt que sur votre base de données principale.

### Frais supplémentaires

You can charge [extra fees](../payment_providers.html#payment-providers-extra-
fees) to customers choosing to pay with PayPal in order to cover the
transaction fees PayPal charges you.

Note

  * Vous pouvez vous référer à [Frais Paypal](https://www.paypal.com/webapps/mpp/paypal-fees) afin de configurer les frais.

  * [Les commerçants de l’UE](https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index_en.htm) ne sont pas autorisés à facturer des frais pour les paiements par carte de crédit.

## Environnement de test

### Configuration

Grâce aux comptes sandbox de PayPal, vous pouvez tester l’ensemble du flux de
paiement dans Odoo.

Connectez-vous au [Site de développeur de
PayPal](https://developer.paypal.com/) avec vos identifiants PayPal, ce qui
crée deux comptes sandbox :

  * Un compte professionnel (à utiliser en tant que marchand, par ex. [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator%40example.com));

  * Un compte personnel par défaut (à utiliser en tant qu’acheteur, par ex. [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer%40example.com)).

Connectez-vous au sandbox PayPal avec votre compte professionnel et suivez les
mêmes instructions de configuration. Saisissez vos identifiants sandbox dans
Odoo (Comptabilité ‣ Configuration ‣ Fournisseurs de paiement ‣ PayPal dans
l’onglet Identifiants et assurez-vous que le statut est défini sur Mode test.
Nous recommandons de faire cela sur une base de données Odoo, plutôt que sur
votre base de données principale.

Lancez une transaction test depuis Odoo en utilisant le compte personnel
sandbox.

Pour plus d'infos

  * [Paiements en ligne](../payment_providers.html)

  *[PDT]: Transfert des données de paiement
  *[IPN]: Notification instantanée de paiement

