# Worldline

La connexion d’un terminal de paiement vous permet d’offrir un flux de
paiement fluide à vos clients et facilite le travail de vos caissiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Worldline payment terminals require an <a href="../../../../general/iot">IoT Box</a>.</p></li>
<li><p>Worldline is currently only available in Belgium, the Netherlands and Luxembourg.</p></li>
<li><p>Konvergo ERP is compatible with Worldline terminals that use the CTEP protocol (e.g., the Yomani XR and
Yoximo terminals). If you have any doubts, contact your payment provider to ensure your
terminal’s compatibility.</p></li>
</ul>
</div>

## Configuration

### Connecter une IoT Box

Connecting a Worldline Payment Terminal to Konvergo ERP is a feature that requires an
IoT Box. For more information on how to connect one to your database, please
refer to the [IoT documentation](../../../../general/iot/config/connect).

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

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line">Voici un exemple d’une séquence d’adresse IP : <code>10.30.19.4:8069</code>.</div>
<div class="line">Sur l’écran du <em>nom d’hôte</em>, tapez 10 ‣ OK ‣ 30 ‣ OK ‣ 19 ‣ OK ‣ 4 ‣ OK ‣ OK.</div>
</div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’adresse IP de votre IoT Box est disponible dans la base de données de votre application IoT Box.</p>
</div>

#### Numéro de port

Sur l’écran _Numéro de port_ , saisissez **9001** (ou **9050** pour Windows)
et cliquez sur OK (_ECR protocole SSL non_) ‣ OK. Cliquez trois fois sur
**Stop** ; le terminal redémarre automatiquement.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>For <b>Windows</b> IoT devices, it is necessary to add a firewall exception. Follow the
<a href="../../../../general/iot/config/windows_iot#iot-windows-wordline"><span class="std std-ref">additional instructions in the Windows IoT documentation</span></a> to add the
exception to Windows Firewall.</p>
</div>

### Configuration du mode de paiement

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **Worldline** in the **Use a Payment Terminal** field.
Then, select your terminal device in the **Payment Terminal Device** field.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Une fois le mode de paiement créé, vous pouvez le sélectionner pour l’utiliser
dans vos paramètres PdV. Pour ce faire, allez aux [paramètres
PdV](../../configuration#configuration-settings), cliquez sur
**Modifier** et ajoutez le mode de paiement dans la section **Paiements**.

<div class="alert alert-info" id="worldline-yomani-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Mot de passe technicien : <code>1235789</code></p></li>
<li><p>Pour joindre l’assistance technique de Worldline, appelez le <code>02 727 61 11</code> et choisissez « marchand ». Votre appel sera automatiquement transféré vers le bon service.</p></li>
<li><p>Configurez le terminal de caisse si vous avez à la fois un terminal client et un terminal de caisse.</p></li>
<li><p>Pour éviter de bloquer le terminal, vérifiez au préalable la configuration initiale.</p></li>
<li><p>Définissez une adresse IP fixe au routeur de votre IoT Box pour éviter de perdre la connexion.</p></li>
</ul>
</div>

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez _Worldline_ comme mode de
paiement. Vérifiez le montant et cliquez sur _Envoyer_. Une fois le paiement
effectué, le statut passe à _Paiement réussi_.

Une fois votre paiement traité, le type de carte utilisée et l’ID de la
transaction apparaissent sur l’enregistrement du paiement.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>En cas de problèmes de connexion entre Konvergo ERP et le terminal de paiement, forcez le paiement en cliquant sur <em>Forcer la validation</em>, ce qui vous permet de valider la commande. Cette option n’est disponible qu’après avoir reçu un message d’erreur vous informant que la connexion a échoué.</p></li>
<li><p>Pour annuler la demande de paiement, cliquez sur <b>annuler</b>.</p></li>
</ul>
</div>

