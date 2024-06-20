# Worldline

La connexion d’un terminal de paiement vous permet d’offrir un flux de
paiement fluide à vos clients et facilite le travail de vos caissiers.

Important

  * Worldline payment terminals require an [IoT Box](../../../../general/iot.html).

  * Worldline is currently only available in Belgium, the Netherlands and Luxembourg.

  * Odoo is compatible with Worldline terminals that use the CTEP protocol (e.g., the Yomani XR and Yoximo terminals). If you have any doubts, contact your payment provider to ensure your terminal’s compatibility.

## Configuration

### Connecter une IoT Box

Connecting a Worldline Payment Terminal to Odoo is a feature that requires an
IoT Box. For more information on how to connect one to your database, please
refer to the [IoT documentation](../../../../general/iot/config/connect.html).

### Configurer le protocole

Depuis votre terminal, cliquez sur « . » ‣ 3 ‣ stop ‣ 3 ‣ 0 ‣ 9. Saisissez le
mot de passe technicien **« 1235789 »** et cliquez sur OK ‣ 4 ‣ 2. Ensuite,
cliquez sur Changer ‣ CTEP (comme Protocole ECR) ‣ OK. Cliquez trois fois sur
**OK** sur les écrans suivants (_CTEP ticket ECR_ , _Largeur du ticket ECR_ et
_Jeu de caractères_). Finalement, appuyez trois fois sur **Stop** ; le
terminal redémarrera automatiquement.

### Définir l’adresse IP

Depuis votre terminal, cliquez sur « . » ‣ 3 ‣ stop ‣ 3 ‣ 0 ‣ 9. Saisissez le
mot de passe technicien **« 1235789 »** et cliquez sur OK ‣ 4 ‣ 9. Ensuite,
cliquez sur Changer ‣ TCP/IP (écran _Configuration physique TCP_) ‣ OK ‣ OK
(écran _Configuration client TCP_).

Finalement, configurez le nom d’hôte et le numéro de port.

#### Nom d’hôte

Pour configurer le nom d’hôte, saisissez les numéros de séquence de l’adresse
IP de votre IoT Box et cliquez sur **OK** à chaque « . » jusqu’au symbole des
deux points.

Cliquez ensuite deux fois sur **OK**.

Example

Voici un exemple d’une séquence d’adresse IP : `10.30.19.4:8069`.

Sur l’écran du _nom d’hôte_ , tapez 10 ‣ OK ‣ 30 ‣ OK ‣ 19 ‣ OK ‣ 4 ‣ OK ‣ OK.

Note

L’adresse IP de votre IoT Box est disponible dans la base de données de votre
application IoT Box.

#### Numéro de port

Sur l’écran _Numéro de port_ , saisissez **9001** (ou **9050** pour Windows)
et cliquez sur OK (_ECR protocole SSL non_) ‣ OK. Cliquez trois fois sur
**Stop** ; le terminal redémarre automatiquement.

Avertissement

For **Windows** IoT devices, it is necessary to add a firewall exception.
Follow the [additional instructions in the Windows IoT
documentation](../../../../general/iot/config/windows_iot.html#iot-windows-
wordline) to add the exception to Windows Firewall.

### Configuration du mode de paiement

Enable the payment terminal [in the application
settings](../../configuration.html#configuration-settings) and [create the
related payment method](../../payment_methods.html). Set the journal type as
Bank and select Worldline in the Use a Payment Terminal field. Then, select
your terminal device in the Payment Terminal Device field.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Une fois le mode de paiement créé, vous pouvez le sélectionner pour l’utiliser
dans vos paramètres PdV. Pour ce faire, allez aux [paramètres
PdV](../../configuration.html#configuration-settings), cliquez sur Modifier et
ajoutez le mode de paiement dans la section Paiements.

Astuce

  * Mot de passe technicien : `1235789`

  * Pour joindre l’assistance technique de Worldline, appelez le `02 727 61 11` et choisissez « marchand ». Votre appel sera automatiquement transféré vers le bon service.

  * Configurez le terminal de caisse si vous avez à la fois un terminal client et un terminal de caisse.

  * Pour éviter de bloquer le terminal, vérifiez au préalable la configuration initiale.

  * Définissez une adresse IP fixe au routeur de votre IoT Box pour éviter de perdre la connexion.

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez _Worldline_ comme mode de
paiement. Vérifiez le montant et cliquez sur _Envoyer_. Une fois le paiement
effectué, le statut passe à _Paiement réussi_.

Une fois votre paiement traité, le type de carte utilisée et l’ID de la
transaction apparaissent sur l’enregistrement du paiement.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png)

Note

  * En cas de problèmes de connexion entre Odoo et le terminal de paiement, forcez le paiement en cliquant sur _Forcer la validation_ , ce qui vous permet de valider la commande. Cette option n’est disponible qu’après avoir reçu un message d’erreur vous informant que la connexion a échoué.

  * Pour annuler la demande de paiement, cliquez sur **annuler**.

