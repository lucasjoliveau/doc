# Ingenico

La connexion d’un terminal de paiement vous permet d’offrir un flux de
paiement fluide à vos clients et facilite le travail de vos caissiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Ingenico payment terminals require an <a href="../../../../general/iot">IoT Box</a>.</p></li>
<li><p>Ingenico is currently only available in Belgium, the Netherlands and Luxembourg.</p></li>
<li><p>Konvergo ERP works with the Ingenico Lane/, Desk/, and Move/ payment terminals as they support the TLV
communication protocol through TCP/IP.</p></li>
</ul>
</div>

## Configuration

### Connecter une IoT Box

Connecting an Ingenico payment terminal to Konvergo ERP is a feature that requires an
IoT Box. For more information on how to connect an IoT Box to your database,
please refer to the [IoT
documentation](../../../../general/iot/config/connect).

### Configure the Lane/Desk/Move 5000 terminals for Ingenico BENELUX

  1. Press the function button (**F** on Lane/5000, **⦿** on Desk/5000 and Move/5000).

  2. Go to Kassa menu ‣ Settings Menu and enter the settings password.

  3. Select **Change Connection** and press **OK** on the next screen.

  4. Select **TCP/IP** and **IP-address**.

  5. On the next screen, enter the IP address of your IoT Box.

  6. Enter `9000` as port number and press **OK** on the next screen.

At this point, the terminal restarts and should be displayed in your IoT Box
form in Konvergo ERP.

![../../../../../_images/payment_terminal_02.png](../../../../../_images/payment_terminal_02.png)

### Configuration du mode de paiement

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **Ingenico** in the **Use a Payment Terminal** field.
Then, select your terminal device in the **Payment Terminal Device** field.

![../../../../../_images/payment-method2.png](../../../../../_images/payment-
method2.png)

Une fois le mode de paiement créé, vous pouvez le sélectionner pour l’utiliser
dans vos paramètres PdV. Pour ce faire, allez aux [paramètres
PdV](../../configuration#configuration-settings), cliquez sur
**Modifier** et ajoutez le mode de paiement dans la section **Paiements**.

## Payer avec un terminal de paiement

Dans votre _interface PdV_ , sélectionnez un _mode de paiement_ à l’aide d’un
terminal de paiement lorsque vous traitez un paiement. Vérifiez que le montant
indiqué dans la colonne Soumissionné est celui qui doit être envoyé au
terminal de paiement et cliquez sur _Envoyer_. Dès que le paiement est fait,
le statut passe à _Paiement réussi_.

![../../../../../_images/payment_terminal_05.png](../../../../../_images/payment_terminal_05.png)

Si vous voulez annuler la demande de paiement, cliquez sur annuler. Vous
pouvez toujours réessayer d’envoyer la demande de paiement.

S’il y a un problème avec le terminal de paiement, vous pouvez toujours forcer
le paiement en utilisant le bouton _Forcer la validation_. Cela vous permettra
de valider la commande dans Konvergo ERP même si la connexion entre le terminal et
Konvergo ERP rencontre des problèmes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cette option ne sera disponible que si vous avez reçu un message d’erreur vous indiquant que la connexion a échoué.</p>
</div>

Dès que votre paiement est traité, vous trouverez sur l’enregistrement du
paiement le type de carte utilisée et l’ID de la transition.

![../../../../../_images/payment_terminal_06.png](../../../../../_images/payment_terminal_06.png)

