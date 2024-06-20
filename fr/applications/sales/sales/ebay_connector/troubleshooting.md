# Dépannage du connecteur eBay

Pour plus d'infos

Pour en apprendre plus sur le connecteur eBay, consultez également ces pages :

  * [Configuration du connecteur eBay](setup.html)

  * [Comment répertorier un produit ?](manage.html)

  * [Associer des annonces existantes](linking_listings.html)

## Accepter les notifications de suppression de compte

Depuis septembre 2021, **eBay doit prendre en charge les notifications de
suppression/fermeture de compte**. Ainsi, lorsque eBay reçoit une demande de
suppression de compte, tous les partenaires eBay doivent confirmer la
réception de la demande et prendre toutes les mesures appropriées le cas
échéant.

Odoo dispose d’un point de terminaison de notification pour recevoir ces
notifications, confirmer la réception de la demande et réaliser les premières
actions nécessaires pour anonymiser les détails du compte dans _Contacts_ et
supprimer l’accès du client au portail.

Important

Veillez à configurer correctement votre abonnement aux notifications de
suppression du compte marketplace, car eBay peut désactiver temporairement le
compte eBay concerné jusqu’à ce que l’abonnement soit finalisé.

### Vérifier que l’installation d’Odoo est à jour

Afin d’activer le point de terminaison, vous devez installer le module
_Connecteur eBay - Suppression du compte_. Si la base de données d’Odoo a été
créée pour la première fois après septembre 2021, le module est installé
automatiquement et l’administrateur peut passer à l”étape suivante.

#### Mettre à jour Odoo à la dernière version

Le point de terminaison de notification est disponible par un nouveau module
Odoo ; pour pouvoir l’installer, l’administrateur doit s’assurer que le code
source d’Odoo est à jour.

  * Si l’entreprise utilise Odoo sur Odoo.com ou Odoo.sh, le code est déjà à jour, passez donc à l’étape suivante.

  * If the company uses Odoo with an on-premise setup or through a partner, then the administrator must update the installation as detailed in [this documentation page](../../../../administration/on_premise/update.html) or by contacting an integrating partner.

#### Mettre à jour la liste des modules disponibles

Les nouveaux modules doivent être _découverts_ par l’instance Odoo pour être
disponibles dans le menu Apps.

Pour ce faire, activez le [mode
développeur](../../../general/developer_mode.html#developer-mode), et allez
aux Apps -> Mettre à jour la liste des Apps. Un assistant vous demandera de
confirmer.

#### Installer la mise à jour du Connecteur eBay - Suppression du compte

Avertissement

N’installez **jamais** de nouveaux modules dans la base de données de
production sans les avoir testées dans un environnement dupliqué ou de
simulation. Pour les clients Odoo.com, une base de données dupliquée peut être
créée à partir de la page de gestion de la base de données. Pour les
utilisateurs Odoo.sh, l’administrateur doit utiliser une base de données de
simulation ou dupliquée. Pour les utilisateurs On premise, l’administrateur
doit utiliser un environnement de simulation - contactez votre partenaire
d’intégration pour plus d’informations sur la façon de tester un nouveau
module dans une configuration particulière.

Pour installer le module, allez au menu Apps, supprimez le filtre `Apps` et
recherchez `eBay`. Si le module _Connecteur eBay - Suppression du compte_ s’y
trouve et est marqué comme installé, la base de données Odoo est déjà à jour
et l’administrateur peut passer à l’étape suivante. Si le module n’est pas
encore installé, procédez maintenant à son installation.

### Récupérer les détails du point de terminaison d’Odoo

Les détails du point de terminaison se trouvent dans Ventes ‣ Configuration ‣
Paramètres ‣ eBay. Saisissez d’abord des valeurs de texte aléatoires dans les
champs App Key production et Cert Key production. Cliquez sur Générer le jeton
pour récupérer le Jeton de vérification.

![Générez un jeton de vérification dans Odoo.](../../../../_images/generate-
token1.png)

### S’abonner aux notifications de suppression de compte

Allez au [portail développeur d’eBay](https://go.developer.ebay.com/).
Configurez les paramètres de notification/suppression du compte dans eBay en
allant à la section `Bonjour [nom d'utilisateur]` en haut à droite de l’écran,
puis allez aux Alertes & Notifications.

![Aperçu du tableau de bord Alertes & Notifications
d'eBay](../../../../_images/ebay-your-account.png)

Pour s’abonner aux notifications de suppression/fermeture, eBay a besoin de
quelques détails :

  * Une _adresse email_ à laquelle les notifications seront envoyées si le point de terminaison est inaccessible.

  * Les _détails du point de terminaison_ :

    * L’URL vers le point de terminaison de notification de suppression de compte d’Odoo

    * Un jeton de vérification

![Champs dédiés pour saisir les détails du point de
terminaison](../../../../_images/ebay-notification-endpoint.png)

Astuce

L’administrateur peut modifier les deux derniers champs une fois que le champ
de l’adresse email est rempli.

### Vérifier la connectivité au point de terminaison

Après avoir défini les détails du point de terminaison récupéré dans le
tableau de bord d’eBay, pensez à tester la connectivité avec le bouton Envoyer
une notification de test.

> Vous devriez recevoir le message de confirmation suivant : « Une
> notification de test a été envoyée avec succès ! »

![Bouton pour envoyer la notification de test](../../../../_images/test-
notification.png)

Pour plus d'infos

  * [Comment répertorier un produit ?](manage.html)

  * [Associer des annonces existantes](linking_listings.html)

  * [Configuration du connecteur eBay](setup.html)

