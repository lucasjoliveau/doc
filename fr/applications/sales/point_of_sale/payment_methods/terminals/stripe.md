# Stripe

La connexion d’un terminal de paiement vous permet d’offrir un flux de
paiement fluide à vos clients et facilite le travail de vos caissiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Stripe payment terminals do not require an <a href="../../../../general/iot">IoT Box</a></p></li>
<li><p>Stripe terminals can be used in many countries, but not worldwide. Check the <a href="https://support.stripe.com/questions/global-availability-for-stripe-terminal">global
availability for Stripe Terminal</a>.</p></li>
<li><p>Stripe’s integration works with <a href="https://docs.stripe.com/terminal/smart-readers">Stripe Terminal smart readers</a></p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../../finance/payment_providers/stripe">Stripe as payment provider</a></p></li>
<li><p><a href="https://stripe.com/payments/payment-methods">List of payment methods supported by Stripe</a></p></li>
</ul>
</div>

## Configuration

### Configuration du mode de paiement

Activez **Stripe** dans les paramètres en allant à Point de Vente ‣
Configuration ‣ Paramètres ‣ Terminaux de paiement et activez **Stripe**.

Créez ensuite le mode de paiement :

  * Allez à Point de Vente ‣ Configuration ‣ Modes de paiement, cliquez sur **Créer** et complétez le champ **Mode** avec le nom de votre mode de paiement ;

  * Définissez le champ **Journal** comme **Bank** et le champ **Utiliser un terminal de paiement** comme **Stripe** ;

  * Saisissez le numéro de série de votre terminal de paiement dans le champ **Numéro de série Stripe** ;

  * Cliquez sur **N’oubliez pas de terminer la connexion de Stripe avant d’utiliser ce mode de paiement.**

![formulaire de création d'un mode de paiement](../../../../../_images/create-
method-stripe.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Cliquez sur <b>Identifier le client</b> pour proposer ce mode de paiement <b>uniquement</b> aux clients identifiés. Si vous souhaitez que les clients non identifiés puissent utiliser Stripe, ne cochez pas le champ <b>Identifier le client</b>.</p></li>
<li><p>Le <b>Compte débiteur</b> et le <b>Compte intermédiaire</b> peuvent rester vides pour utiliser les comptes par défaut.</p></li>
<li><p>Vous trouverez le numéro de série de votre terminal de paiement sous l’appareil ou sur le <a href="https://dashboard.stripe.com">tableau de bord de Stripe</a>.</p></li>
</ul>
</div>

### Connecter Stripe à Konvergo ERP

Cliquez sur **Connecter Stripe**. Ceci vous redirige automatiquement vers une
page de configuration. Complétez toutes les informations pour créer votre
compte Stripe et liez-le à Konvergo ERP. Une fois les formulaires complétés, vous
trouverez les clés API (**Clé Publishable** et **Clé Secrète**) sur le site
web de **Stripe**. Pour ce faire, cliquez sur **Get your Secret and
Publishable keys** , cliquez sur les clés pour les copier et collez-les dans
les champs correspondants dans Konvergo ERP. Votre terminal est prêt à être configuré
dans un PdV.

![formulaire de connexion de Stripe](../../../../../_images/stripe-
connect.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Si vous utilisez <b>Stripe</b> exclusivement dans le Point de Vente, vous avez uniquement besoin de la <b>Clé secrète</b> pour utiliser votre terminal.</p></li>
<li><p>Si vous utilisez Stripe comme <b>fournisseur de paiement</b>, le <b>Statut</b> peut rester défini comme <b>Désactivé</b>.</p></li>
<li><p>Pour les bases de données hébergées <b>sur serveur</b>, le bouton <b>Connecter Stripe</b> ne fonctionne pas. Pour récupérer les clés API manuellement, connectez-vous à votre <a href="https://dashboard.stripe.com">tableau de bord Stripe</a>, tapez <code>API</code> dans la barre de recherche et cliquez sur <b>Développeurs &gt; API</b>.</p></li>
</ul>
</div>

### Configurer le terminal de paiement

Balayez vers la droite sur votre terminal de paiement, cliquez sur
**Paramètres** , saisissez le code PIN administrateur, validez et sélectionnez
votre réseau.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>L’appareil doit être connecté à un réseau WI-FI sécurisé.</p></li>
<li><p>Votre base de données Konvergo ERP et votre terminal de paiement doivent partager le même réseau.</p></li>
<li><p>Vous devez saisir le code PIN administrateur pour accéder aux paramètres de votre terminal de paiement. Par défaut, ce code est <code>07139</code>.</p></li>
</ul>
</div>

### Lier le mode de paiement à un PdV

Pour appliquer un **mode de paiement** à votre point de vente, allez à Point
de Vente ‣ Configuration ‣ Paramètres. Sélectionnez le PdV, faites défiler
vers le bas jusqu’à la section **Paiements** et ajoutez votre mode de paiement
et ajoutez votre mode de paiement pour **Stripe** dans le champ **Modes de
paiement**.

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez **Stripe** comme mode de
paiement. Vérifiez le montant et cliquez sur **Envoyer**. Une fois le paiement
effectué, le statut passe à **Paiement réussi**. Pour annuler la demande de
paiement, cliquez sur **annuler**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><div class="line-block">
<div class="line">En cas de problèmes de connexion entre Konvergo ERP et le terminal de paiement, forcez le paiement en cliquant sur <b>Forcer la validation</b>, ce qui vous permet de valider la commande.</div>
<div class="line">Cette option ne sera disponible qu’après avoir reçu un message d’erreur vous informant que la connexion a échoué.</div>
</div>
</li>
<li><p>Le terminal doit avoir un niveau de batterie d’au moins 10% pour pouvoir être utilisé.</p></li>
<li><p>L’appareil ne fonctionne pas pour les paiements inférieurs à 0,50 €.</p></li>
</ul>
</div>

## Troubleshooting

### Terminal de paiement indisponible dans votre compte Stripe

Si le terminal de paiement n’est pas disponible dans votre compte Stripe, vous
devez l’ajouter manuellement :

  1. Connectez-vous à votre [tableau de bord Stripe](https://dashboard.stripe.com) et allez à Tableau de bord Stripe ‣ Paiements ‣ Lecteurs ‣ Emplacements ;

  2. Ajoutez un emplacement en cliquant sur le bouton **\+ Nouveau** ou en sélectionnant un emplacement déjà créé ;

  3. Cliquez sur le bouton **\+ Nouveau** dans la case **Lecteurs** et complétez les informations requises.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous devez fournir un <b>code d’enregistrement</b>. Pour récupérer ce code, balayez vers la droite, saisissez le code PIN administrateur (par défaut : <code>07139</code>), validez et cliquez sur <b>Générer un code d’enregistrement</b>.</p>
</div>

