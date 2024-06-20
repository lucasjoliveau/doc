# Unsplash

**Unsplash** est une bibliothèque reconnue de photos d’archives intégrée à
Odoo.

Si votre base de données est hébergée sur **Odoo Online** , vous pouvez
accéder aux illustrations d’Unsplash sans configuration.

Si votre base de données est hébergée sur **Odoo.sh ou on-premise** , procédez
comme suit :

  1. Pour **générer une clé d’accès Unsplash** , créez ou connectez-vous à un [compte Unsplash](https://unsplash.com).

  2. Accédez à votre [tableau de bord des applications](https://unsplash.com/oauth/applications), cliquez sur Nouvelle application, cochez toutes les cases et cliquez sur Accepter les conditions.

  3. Dans la fenêtre contextuelle, saisissez le Nom de votre application, commençant par le préfixe `Odoo:` (par ex. `Odoo : connexion`), pour qu’Unsplash la reconnaisse comme une instance Odoo. Ajoutez ensuite une Description et cliquez sur Créer une application.

  4. Sur la page des détails de l’application, faites défiler vers le bas jusqu’à la section Clés et copiez la Clé d’accès et l”ID de l’application.

  5. Dans Odoo, allez aux Paramètres généraux et activez la fonctionnalité Bibliothèque d’image Unsplash. Saisissez ensuite la Clé d’accès et l”ID d’application d’Unsplash.

Avertissement

En tant que non-utilisateur d’Odoo Online, vous êtes limité à une clé de test
avec un maximum de 50 requêtes Unsplash par heure.

