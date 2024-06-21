# Unsplash

**Unsplash** est une bibliothèque reconnue de photos d’archives intégrée à
Konvergo ERP.

Si votre base de données est hébergée sur **Konvergo ERP Online** , vous pouvez
accéder aux illustrations d’Unsplash sans configuration.

Si votre base de données est hébergée sur **Konvergo ERP.sh ou on-premise** , procédez
comme suit :

  1. Pour **générer une clé d’accès Unsplash** , créez ou connectez-vous à un [compte Unsplash](https://unsplash.com).

  2. Accédez à votre [tableau de bord des applications](https://unsplash.com/oauth/applications), cliquez sur **Nouvelle application** , cochez toutes les cases et cliquez sur **Accepter les conditions**.

  3. Dans la fenêtre contextuelle, saisissez le **Nom de votre application** , commençant par le préfixe `Konvergo ERP:` (par ex. `Konvergo ERP : connexion`), pour qu’Unsplash la reconnaisse comme une instance Konvergo ERP. Ajoutez ensuite une **Description** et cliquez sur **Créer une application**.

  4. Sur la page des détails de l’application, faites défiler vers le bas jusqu’à la section **Clés** et copiez la **Clé d’accès** et l”**ID de l’application**.

  5. Dans Konvergo ERP, allez aux Paramètres généraux et activez la fonctionnalité **Bibliothèque d’image Unsplash**. Saisissez ensuite la **Clé d’accès** et l”**ID d’application** d’Unsplash.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>En tant que non-utilisateur d’Konvergo ERP Online, vous êtes limité à une clé de test avec un maximum de 50 requêtes Unsplash par heure.</p>
</div>

