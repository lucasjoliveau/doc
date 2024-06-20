# SIX

La connexion d’un **terminal de paiement SIX** vous permet d’offrir un flux de
paiement fluide à vos clients et de faciliter le travail de vos caissiers.

Avertissement

Même si Worldline a acquis SIX Payment Services et que les deux sociétés
utilisent des terminaux de paiement Yomani, le firmware qu’ils exécutent est
différent. Les terminaux reçus de Worldline ne sont donc pas compatibles avec
cette intégration.

## Configuration

### Installer le module PdV IoT Six

Pour activer le module PdV IoT Six, allez aux Apps, supprimez le filtre Apps
et recherchez **POS IoT Six**. Ce module ajoute le pilote et l’interface
nécessaires à votre base de données pour détecter les terminaux Six.

Note

Ce module remplace le module **PdV Six**.

### Connecter une IoT box

Connecting a Six payment terminal to Odoo is requires [using a Raspberry Pi or
virtual (for Windows OS only) IoT
box](../../../../general/iot/config/connect.html).

### Configurer l’ID du terminal

Allez à la page d’accueil de votre IoT Box, où vous pouvez trouver le champ
Terminal de paiement Six une fois que votre serveur de base de données es
connecté à l’IoT box. Cliquez sur Configurer, remplissez le champ ID terminal
avec l’ID reçu de Six et cliquez sur Connecter. L’ID de votre terminal Six
devrait apparaître dans la section ID terminal actuel.

![Configuration de l'ID du terminal Six](../../../../../_images/terminal-
id.png)

Odoo redémarre automatiquement l’IoT box après la configuration de l’ID du
terminal Six. Si votre terminal Six est en ligne, il sera détecté et connecté
automatiquement à la base de données. Consultez la page d’accueil de l’IoT box
dans la section Paiements pour confirmer la connexion.

![Confirmer la connexion au terminal de paiement
Six](../../../../../_images/id-configured.png)

### Configuration du mode de paiement

Enable the payment terminal [in the application
settings](../../configuration.html#configuration-settings) and [create the
related payment method](../../payment_methods.html). Set the journal type as
Bank and select SIX IOT in the Use a Payment Terminal field. Then, select your
terminal device in the Payment Terminal Device field.

![Créez un nouveau mode de paiement pour le terminal de paiement
Six.](../../../../../_images/new-payment-method.png)

Une fois le mode de paiement créé, vous pouvez le sélectionner pour l’utiliser
dans vos paramètres PdV. Pour ce faire, allez aux [paramètres
PdV](../../configuration.html#configuration-settings), cliquez sur Modifier et
ajoutez le mode de paiement dans la section Paiements.

## Payer avec un terminal de paiement

Lors du traitement d’un paiement, sélectionnez votre mode de paiement Six dans
la section Mode de paiement et cliquez sur Envoyer. Pour annuler la demande de
paiement, cliquez sur Annuler. Une fois le paiement réussi, le statut passe à
Paiement réussi.

![Payer avec Six](../../../../../_images/payment.png)

Note

  * Une fois votre paiement traité, le type de carte utilisée et l’ID de la transaction apparaissent sur l’enregistrement du paiement.

  * La langue utilisée pour les messages d’erreur est la même que le terminal Six. Configurez le terminal pour modifier la langue ou contactez Six.

  * Par défaut, le port utilisé par le terminal Six est `7784`.

Astuce

S’il y a des problèmes de connexion entre le terminal de paiement et Odoo,
vous pouvez toujours forcer la validation du paiement dans Odoo à l’aide du
bouton Forcer la validation.

