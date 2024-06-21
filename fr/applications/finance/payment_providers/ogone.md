# Ogone

[Ogone](https://www.ingenico.com/), également connue sous le nom d”**Ingenico
Payment Services** , est une société basée en France qui fournit la
technologie utilisée dans les transactions électroniques sécurisées.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
<li><p><a href="https://epayments-support.ingenico.com/get-started/">Documentation relative à Ogone</a>.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Le fournisseur Ogone est obsolète. Nous vous recommandons d’utiliser plutôt <a href="stripe">Stripe</a>.</p>
</div>

## Paramètres dans Ogone

### Créer un utilisateur API

Connectez-vous à votre compte Ogone et allez à l’onglet **Configuration**.

Vous devez créer un **utilisateur API** qui sera utilisé lors de la création
de transactions à partir d’Konvergo ERP. Bien que vous puissiez utiliser votre compte
principal pour le faire, l’utilisation d’un **utilisateur API** garantit qu’en
cas de fuite des identifiants utilisés dans Konvergo ERP, il n’est pas possible
d’accéder à votre configuration Ogone. De plus, les mots de passe des
**utilisateurs API** n’ont pas besoin d’être mis à jour régulièrement,
contrairement aux utilisateurs habituels.

Pour créer un **utilisateur API** , allez à Configuration ‣ Utilisateurs et
cliquez sur **Nouvel utilisateur**. Les champs suivants doivent être
configurés :

  * **UserID** : vous pouvez choisir ce que vous voulez.

  * **Nom, email et fuseau horaire de l’utilisateur** : vous pouvez saisir les informations que vous voulez.

  * **Profil** : doit être défini sur **Admin**.

  * **Utilisateur spécial pour API** : doit être coché.

Après avoir créé l’utilisateur, vous devez générer un mot de passe.
Enregistrez le mot de passe et l”**UserID** , puisqu’ils seront nécessaires
plus tard au cours de la configuration.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous avez déjà configuré un utilisateur, assurez-vous qu’il est activé sans erreur. Si ce n’est pas le cas, cliquez simplement sur le bouton <b>Activer(Erreurs)</b> pour réinitialiser l’utilisateur.</p>
</div>

### Configurer Ogone pour Konvergo ERP

Ogone doit à présent être configuré pour accepter les paiements depuis Konvergo ERP.
Allez à Configuration ‣ Informations techniques ‣ Paramètres de sécurité
généraux, sélectionnez **SHA-512** en tant qu”**Algorithme de hachage** et
**UTF-8** en tant que **jeu de caractères codés**. Ensuite, allez à l’onglet
**Vérification des données et de l’origine** de la même page et laissez le
champ URL de la section **e-Commerce and Alias Gateway** vide.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous avez besoin d’utiliser un autre algorithme, tel que <code>sha-1</code> ou <code>sha-256</code>, dans Konvergo ERP, activez le <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a> et allez à la page <b>Fournisseurs de paiement</b> dans Comptabilité ‣ Configuration ‣ Fournisseurs de paiement. Cliquez sur <b>Ogone</b>, et dans l’onglet <b>Identifiants</b>, sélectionnez l’algoritme que vous souhaitez utiliser dans le champ <b>Fonction de hachage</b>.</p>
</div>

Vous devez maintenant générer des phrases de passe **SHA-IN**. Les phrases de
passe **SHA-IN** et **SHA-OUT** sont utilisées pour signer numériquement les
demandes et les réponses de transaction entre Konvergo ERP et Ogone. En utilisant ces
phrases de passe secrètes et l’algoritme `sha-1`, les deux systèmes peuvent
s’assurer que les informations qu’ils reçoivent de l’autre n’ont pas été
modifiées ou altérées.

Saisissez la même phrase secrète **SHA-IN** dans les deux champs **Checks for
e-Commerce & Alias Gateway** et **Checks for DirectLink and Batch
(Automatic)**. Vous pouvez laisser le champ d’adresse IP vide.

Vos phrases de passe **SHA-IN** et **SHA-OUT** doivent être différentes et
comporter entre 16 et 32 caractères. Veillez à utiliser les mêmes phrases de
passe **SHA-IN** et **SHA-OUT** dans toute la configuration d’Ogone, car Konvergo ERP
n’autorise qu’une seule phrase de passe **SHA-IN** et une seule phrase de
passe **SHA-OUT**.

Pour récupérer la clé **SHA-OUT** , connectez-vous à votre compte Ogone, allez
à Configuration ‣ Informations techniques ‣ Feedback de transaction ‣ Tous les
modes de soumission des transactions, et obtenez ou générez votre **Clé API**
et **Clé client**. Veillez à copier votre clé API, car vous ne serez pas
autorisé à l’obtenir plus tard sans en générer une nouvelle.

Une fois que vous avez terminé, allez à Configuration ‣ Informations
techniques ‣ Feedback de transaction et vérifiez les options suivantes :

  * Les champs **URL** pour la **redirection HTTP dans le navigateur** peuvent être laissés vides, car Konvergo ERP précisera ces URLs pour chaque demande de transaction.

  * L’option **J’aimerais recevoir des paramètres de feedback de transaction sur les URLs de redirection** doit être cochée.

  * L’option **Requête HTTP directe de serveur à serveur** doit être définie sur `En ligne, mais passer à une requête différée lorsque la requête en ligne échoue`.

  * Les deux champs **URL** doivent contenir la même URL, avec `<example>` remplacé par votre base de données : `https://<example>/payment/ogone/return`.

  * Le champ **Paramètres dynamiques d’eCommerce** doit contenir les valeurs suivantes : `ALIAS`, `AMOUNT`, `CARDNO`, `CN`, `CURRENCY`, `IP`, `NCERROR` `ORDERID`, `PAYID`, `PM`, `STATUS`, `TRXDATE`. D’autres paramètres peuvent être inclus (si vous avez une autre intégration avec Ogone qui les requiert), mais ne sont pas conseillés.

  * Dans la section **Tous les modes de soumission des transactions** , complétez la phrase de passe **SHA-OUT** et désactiver `requête HTTP de changement de statut`.

Pour permettre à vos clients d’enregistrer les identifiants de carte de crédit
en vue d’une utilisation ultérieure, allez à Configuration ‣ Alias ‣ Mes
informations d’alias. Depuis cet onglet, vous pouvez configurer la façon dont
l’utilisateur peut avoir ses détails de carte enregistrés, pendant combien de
temps les informations sont enregistrées, si une case à cocher pour
enregistrer les informations de la carte doit être affichée, etc.

## Paramètres dans Konvergo ERP

Pour configurer Ogone dans Konvergo ERP, allez à Comptabilité ‣ Configuration ‣
Fournisseurs de paiement et ouvrez le fournisseur Ogone. Dans l’onglet
**Identifiants** , saisissez le **PSPID** de votre compte Ogone et remplissez
les autres champs tels que configurés dans votre portail Ogone.

