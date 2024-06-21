# Configurer des serveurs ICE avec Twilio

Konvergo ERP Discussion utilise l’API WebRTC et les connexions pair-à-pair pour les
appels vocaux et vidéo. Si l’un des participants à l’appel se trouve derrière
un NAT symétrique, vous devez configurer un serveur ICE pour établir une
connexion avec ce participant. Pour configurer un serveur ICE, créez d’abord
un compte Twilio pour les appels vidéo, puis connectez ce compte Twilio à
Konvergo ERP.

## Créer un compte Twilio

Allez d’abord à [Twilio](https://www.twilio.com) et cliquez sur **S’inscrire**
pour créer un nouveau Compte Twilio. Saisissez votre nom et adresse email,
créez un mot de passe et acceptez les conditions générales de Twilio. Cliquez
ensuite sur **Commencer votre essai gratuit**. Vérifiez votre adresse email
auprès de Twilio, en suivant les instructions.

Saisissez ensuite votre numéro de téléphone dans Twilio. Twilio vous enverra
un SMS contenant un code de vérification. Saisissez le code de vérification
dans Twilio pour vérifier votre numéro de téléphone.

Twilio vous redirige ensuite vers une page d’accueil. Utilisez la liste
suivante pour répondre aux questions de Twilio :

  * À la question **Quel produit Twilio souhaitez-vous utiliser ?** , sélectionnez **Vidéo**.

  * À la question **Qu’avez-vous l’intention de construire avec Twilio ?** , sélectionnez **Autre**.

  * À la question **Comment voulez-vous construire avec Twilio ?** , sélectionnez **Sans aucun code**.

  * À la question **Quel est votre objectif aujourd’hui ?** , sélectionnez **Intégrations tierces**.

![La page d'accueil de Twilio.](../../../_images/twilio-welcome.png)

Le cas échéant, changez le pays de facturation. Enfin, cliquez sur **Démarrer
avec Twilio**.

## Localiser le SID du compte et le jeton d’authentification de Twilio

Pour localiser le SID du compte et le jeton d’authentification, allez au
tableau de bord de votre compte Twilio. Cliquez ensuite sur **Développer**
dans la barre latérale. Dans la section **Informations du compte** , localisez
le **SID du compte** et le **Jeton d’authentification**. Ces deux éléments
sont nécessaires pour connecter Twilio à Konvergo ERP.

![Le SID du compte et le jeton d'authentification de Twilio se trouvent sous
la section Informations du compte.](../../../_images/twilio-acct-info.png)

## Connecter Twilio à Konvergo ERP

Ouvrez la base de données Konvergo ERP et allez aux Paramètres ‣ Paramètres généraux ‣
Discussion. Cochez la case à côté de **Utiliser des serveurs ICE Twilio** et
saisissez le **SID du compte** et le **Jeton d’authentification** du compte
Twilio. Enfin, cliquez sur **Enregistrer** pour appliquer ces changements.

![Activez l'option "Utiliser les serveurs ICE Twilio" dans les Paramètres
généraux d'Konvergo ERP.](../../../_images/connect-twilio-to-odoo.png)

## Définir une liste de serveurs ICE personnalisés

Cette étape n’est pas obligatoire pour configurer Twilio. Cependant, si Twilio
n’est pas configuré ou ne fonctionne pas à un moment donné, Konvergo ERP se rabattra
sur la liste de serveurs ICE personnalisés. L’utilisateur doit définir la
liste de serveurs ICE personnalisés.

Dans les Paramètres ‣ Paramètres généraux ‣ Discussion, cliquez sur le bouton
**Serveurs ICE** sous la **Liste de serveurs ICE personnalisés**.

![Le bouton "Serveurs ICE" dans les Paramètres généraux
d'Konvergo ERP.](../../../_images/custom-ice-servers-list.png)

Konvergo ERP vous redirigera vers la page des **serveurs ICE**. Vous pouvez y définir
votre propre liste de serveurs ICE.

![La page "serveurs ICE" dans Konvergo ERP.](../../../_images/ice-servers-page.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour les instances d’Konvergo ERP on premise, le package <code>python3-gevent</code> est nécessaire pour que le module Discussion puisse exécuter des appels/vidéos sur les serveurs Ubuntu (Linux).</p>
</div>

