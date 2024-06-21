# Adyen

La connexion d’un **terminal de paiement Adyen** vous permet d’offrir un flux
de paiement fluide à vos clients et facilite le travail de vos caissiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Adyen payment terminals do not require an <a href="../../../../general/iot">IoT Box</a>.</p></li>
<li><p>Adyen terminals can be used in many countries, but not worldwide. Check the <a href="https://docs.adyen.com/point-of-sale/what-we-support/supported-languages/">List of countries
supported by Adyen</a>.</p></li>
<li><p>Adyen works only with businesses processing more than <b>$10 million annually</b> or invoicing a
minimum of <b>1,000 transactions per month</b>.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/">List of payment methods supported by Adyen</a></p></li>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals/">List of Adyen terminals</a></p></li>
</ul>
</div>

## Configuration

Commencez par créer un compte Adyen sur [le site web
d’Adyen](https://www.adyen.com/). Ensuite, configurez votre terminal en
suivant les étapes décrites sur l’écran de votre terminal.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://docs.adyen.com/point-of-sale/user-manuals">Adyen Docs - Payment terminal quickstart guides</a></p>
</div>

### Générer une clé API Adyen

The **Adyen API key** is used to authenticate requests from your Adyen
terminal. To generate an API key, go to your Adyen account ‣ Developers ‣ API
credentials, and **create** new credentials or select **existing** ones. Click
**Generate an API key** and save the key to paste it into the Konvergo ERP **Adyen API
key** field at the payment method creation.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://docs.adyen.com/development-resources/api-credentials#generate-api-key">Adyen Docs - Identifiants API</a>.</p></li>
</ul>
</div>

### Localiser l’identifiant du terminal Adyen

The **Adyen Terminal Identifier** is the terminal’s serial number, which is
used to identify the hardware.

To find this number, go to your Adyen account ‣ Point of Sale ‣ Terminals,
select the terminal to link with, and save its serial number to paste it into
the Konvergo ERP **Adyen Terminal Identifier** field at the payment method creation.

### Définir les URLs d’événement

For Konvergo ERP to know when a payment is made, you must configure the terminal
**Event URLs**. To do so,

  1. Log in to [Adyen’s website](https://www.adyen.com/);

  2. Go to Adyen’s dashboard ‣ Point of Sale ‣ Terminals and select the connected terminal;

  3. From the terminal settings, click **Integrations** ;

  4. Set the **Switch to decrypted mode to edit this setting** field as **Decrypted** ;

  5. Click the **pencil icon** button and enter your server address, followed by `/pos_adyen/notification` in the **Event URLs** field;

  6. Click **Save** at the bottom of the screen to save changes.

### Configuration du mode de paiement

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **Adyen** in the **Use a Payment Terminal** field.

Finally, fill in the mandatory fields with your Adyen API key, Adyen Terminal
Identifier, and **Adyen Merchant Account**.

![../../../../../_images/payment-method1.png](../../../../../_images/payment-
method1.png)

Une fois le mode de paiement créé, vous pouvez le sélectionner pour l’utiliser
dans vos paramètres PdV. Pour ce faire, allez aux [paramètres
PdV](../../configuration#configuration-settings), cliquez sur
**Modifier** et ajoutez le mode de paiement dans la section **Paiements**.

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez **Adyen** comme mode de
paiement. Vérifiez le montant et cliquez sur **Envoyer**. Une fois le paiement
effectué, le statut passe à **Paiement réussi**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><div class="line-block">
<div class="line">En cas de problèmes de connexion entre Konvergo ERP et le terminal de paiement, forcez le paiement en cliquant sur <b>Forcer la validation</b>, ce qui vous permet de valider la commande.</div>
<div class="line">Cette option ne sera disponible qu’après avoir reçu un message d’erreur vous informant que la connexion a échoué.</div>
</div>
</li>
<li><p>Pour annuler la demande de paiement, cliquez sur <b>annuler</b>.</p></li>
</ul>
</div>

