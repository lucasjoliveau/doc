# Stripe

La connexion d’un terminal de paiement vous permet d’offrir un flux de
paiement fluide à vos clients et facilite le travail de vos caissiers.

Important

  * Stripe payment terminals do not require an [IoT Box](../../../../general/iot.html)

  * Stripe terminals can be used in many countries, but not worldwide. Check the [global availability for Stripe Terminal](https://support.stripe.com/questions/global-availability-for-stripe-terminal).

  * Stripe’s integration works with [Stripe Terminal smart readers](https://docs.stripe.com/terminal/smart-readers)

Pour plus d'infos

  * [Stripe as payment provider](../../../../finance/payment_providers/stripe.html)

  * [List of payment methods supported by Stripe](https://stripe.com/payments/payment-methods)

## Configuration

### Configuration du mode de paiement

Activez **Stripe** dans les paramètres en allant à Point de Vente ‣
Configuration ‣ Paramètres ‣ Terminaux de paiement et activez Stripe.

Créez ensuite le mode de paiement :

  * Allez à Point de Vente ‣ Configuration ‣ Modes de paiement, cliquez sur Créer et complétez le champ Mode avec le nom de votre mode de paiement ;

  * Définissez le champ Journal comme Bank et le champ Utiliser un terminal de paiement comme Stripe ;

  * Saisissez le numéro de série de votre terminal de paiement dans le champ Numéro de série Stripe ;

  * Cliquez sur N’oubliez pas de terminer la connexion de Stripe avant d’utiliser ce mode de paiement.

![formulaire de création d'un mode de paiement](../../../../../_images/create-
method-stripe.png)

Note

  * Cliquez sur Identifier le client pour proposer ce mode de paiement **uniquement** aux clients identifiés. Si vous souhaitez que les clients non identifiés puissent utiliser Stripe, ne cochez pas le champ Identifier le client.

  * Le Compte débiteur et le Compte intermédiaire peuvent rester vides pour utiliser les comptes par défaut.

  * Vous trouverez le numéro de série de votre terminal de paiement sous l’appareil ou sur le [tableau de bord de Stripe](https://dashboard.stripe.com).

### Connecter Stripe à Odoo

Cliquez sur Connecter Stripe. Ceci vous redirige automatiquement vers une page
de configuration. Complétez toutes les informations pour créer votre compte
Stripe et liez-le à Odoo. Une fois les formulaires complétés, vous trouverez
les clés API (Clé Publishable et Clé Secrète) sur le site web de **Stripe**.
Pour ce faire, cliquez sur Get your Secret and Publishable keys, cliquez sur
les clés pour les copier et collez-les dans les champs correspondants dans
Odoo. Votre terminal est prêt à être configuré dans un PdV.

![formulaire de connexion de Stripe](../../../../../_images/stripe-
connect.png)

Note

  * Si vous utilisez **Stripe** exclusivement dans le Point de Vente, vous avez uniquement besoin de la **Clé secrète** pour utiliser votre terminal.

  * Si vous utilisez Stripe comme **fournisseur de paiement** , le Statut peut rester défini comme Désactivé.

  * Pour les bases de données hébergées **sur serveur** , le bouton Connecter Stripe ne fonctionne pas. Pour récupérer les clés API manuellement, connectez-vous à votre [tableau de bord Stripe](https://dashboard.stripe.com), tapez `API` dans la barre de recherche et cliquez sur Développeurs > API.

### Configurer le terminal de paiement

Balayez vers la droite sur votre terminal de paiement, cliquez sur Paramètres,
saisissez le code PIN administrateur, validez et sélectionnez votre réseau.

Note

  * L’appareil doit être connecté à un réseau WI-FI sécurisé.

  * Votre base de données Odoo et votre terminal de paiement doivent partager le même réseau.

  * Vous devez saisir le code PIN administrateur pour accéder aux paramètres de votre terminal de paiement. Par défaut, ce code est `07139`.

### Lier le mode de paiement à un PdV

Pour appliquer un **mode de paiement** à votre point de vente, allez à Point
de Vente ‣ Configuration ‣ Paramètres. Sélectionnez le PdV, faites défiler
vers le bas jusqu’à la section Paiements et ajoutez votre mode de paiement et
ajoutez votre mode de paiement pour **Stripe** dans le champ Modes de
paiement.

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez Stripe comme mode de paiement.
Vérifiez le montant et cliquez sur Envoyer. Une fois le paiement effectué, le
statut passe à Paiement réussi. Pour annuler la demande de paiement, cliquez
sur annuler.

Note

  * En cas de problèmes de connexion entre Odoo et le terminal de paiement, forcez le paiement en cliquant sur Forcer la validation, ce qui vous permet de valider la commande.

Cette option ne sera disponible qu’après avoir reçu un message d’erreur vous
informant que la connexion a échoué.

  * Le terminal doit avoir un niveau de batterie d’au moins 10% pour pouvoir être utilisé.

  * L’appareil ne fonctionne pas pour les paiements inférieurs à 0,50 €.

## Troubleshooting

### Terminal de paiement indisponible dans votre compte Stripe

Si le terminal de paiement n’est pas disponible dans votre compte Stripe, vous
devez l’ajouter manuellement :

  1. Connectez-vous à votre [tableau de bord Stripe](https://dashboard.stripe.com) et allez à Tableau de bord Stripe ‣ Paiements ‣ Lecteurs ‣ Emplacements ;

  2. Ajoutez un emplacement en cliquant sur le bouton \+ Nouveau ou en sélectionnant un emplacement déjà créé ;

  3. Cliquez sur le bouton \+ Nouveau dans la case Lecteurs et complétez les informations requises.

Note

Vous devez fournir un **code d’enregistrement**. Pour récupérer ce code,
balayez vers la droite, saisissez le code PIN administrateur (par défaut :
`07139`), validez et cliquez sur Générer un code d’enregistrement.

