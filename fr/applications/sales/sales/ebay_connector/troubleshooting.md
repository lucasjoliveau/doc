# Dépannage du connecteur eBay

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Pour en apprendre plus sur le connecteur eBay, consultez également ces pages :</p>
<ul>
<li><p><a href="setup">Configuration du connecteur eBay</a></p></li>
<li><p><a href="manage">Comment répertorier un produit ?</a></p></li>
<li><p><a href="linking_listings">Associer des annonces existantes</a></p></li>
</ul>
</div>

## Accepter les notifications de suppression de compte

Depuis septembre 2021, **eBay doit prendre en charge les notifications de
suppression/fermeture de compte**. Ainsi, lorsque eBay reçoit une demande de
suppression de compte, tous les partenaires eBay doivent confirmer la
réception de la demande et prendre toutes les mesures appropriées le cas
échéant.

Konvergo ERP dispose d’un point de terminaison de notification pour recevoir ces
notifications, confirmer la réception de la demande et réaliser les premières
actions nécessaires pour anonymiser les détails du compte dans _Contacts_ et
supprimer l’accès du client au portail.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Veillez à configurer correctement <a href="#ebay-subscribe-account-deletion-notifications"><span class="std std-ref">votre abonnement aux notifications de suppression du compte marketplace</span></a>, car eBay peut désactiver temporairement le compte eBay concerné jusqu’à ce que l’abonnement soit finalisé.</p>
</div>

### Vérifier que l’installation d’Konvergo ERP est à jour

Afin d’activer le point de terminaison, vous devez installer le module
_Connecteur eBay - Suppression du compte_. Si la base de données d’Konvergo ERP a été
créée pour la première fois après septembre 2021, le module est installé
automatiquement et l’administrateur peut passer à l”étape suivante.

#### Mettre à jour Konvergo ERP à la dernière version

Le point de terminaison de notification est disponible par un nouveau module
Konvergo ERP ; pour pouvoir l’installer, l’administrateur doit s’assurer que le code
source d’Konvergo ERP est à jour.

  * Si l’entreprise utilise Konvergo ERP sur Konvergo ERP.com ou Konvergo ERP.sh, le code est déjà à jour, passez donc à l’étape suivante.

  * If the company uses Konvergo ERP with an on-premise setup or through a partner, then the administrator must update the installation as detailed in [this documentation page](../../../../administration/on_premise/update) or by contacting an integrating partner.

#### Mettre à jour la liste des modules disponibles

Les nouveaux modules doivent être _découverts_ par l’instance Konvergo ERP pour être
disponibles dans le menu Apps.

Pour ce faire, activez le [mode
développeur](../../../general/developer_mode#developer-mode), et allez
aux Apps -> Mettre à jour la liste des Apps. Un assistant vous demandera de
confirmer.

#### Installer la mise à jour du Connecteur eBay - Suppression du compte

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>N’installez <b>jamais</b> de nouveaux modules dans la base de données de production sans les avoir testées dans un environnement dupliqué ou de simulation. Pour les clients Konvergo ERP.com, une base de données dupliquée peut être créée à partir de la page de gestion de la base de données. Pour les utilisateurs Konvergo ERP.sh, l’administrateur doit utiliser une base de données de simulation ou dupliquée. Pour les utilisateurs On premise, l’administrateur doit utiliser un environnement de simulation - contactez votre partenaire d’intégration pour plus d’informations sur la façon de tester un nouveau module dans une configuration particulière.</p>
</div>

Pour installer le module, allez au menu Apps, supprimez le filtre `Apps` et
recherchez `eBay`. Si le module _Connecteur eBay - Suppression du compte_ s’y
trouve et est marqué comme installé, la base de données Konvergo ERP est déjà à jour
et l’administrateur peut passer à l’étape suivante. Si le module n’est pas
encore installé, procédez maintenant à son installation.

### Récupérer les détails du point de terminaison d’Konvergo ERP

Les détails du point de terminaison se trouvent dans Ventes ‣ Configuration ‣
Paramètres ‣ eBay. Saisissez d’abord des valeurs de texte aléatoires dans les
champs **App Key production** et **Cert Key production**. Cliquez sur
**Générer le jeton** pour récupérer le **Jeton de vérification**.

![Générez un jeton de vérification dans Konvergo ERP.](../../../../_images/generate-
token1.png)

### S’abonner aux notifications de suppression de compte

Allez au [portail développeur d’eBay](https://go.developer.ebay.com/).
Configurez les paramètres de notification/suppression du compte dans eBay en
allant à la section `Bonjour [nom d'utilisateur]` en haut à droite de l’écran,
puis allez aux **Alertes & Notifications**.

![Aperçu du tableau de bord Alertes & Notifications
d'eBay](../../../../_images/ebay-your-account.png)

Pour s’abonner aux notifications de suppression/fermeture, eBay a besoin de
quelques détails :

  * Une _adresse email_ à laquelle les notifications seront envoyées si le point de terminaison est inaccessible.

  * Les _détails du point de terminaison_ :

    * L’URL vers le point de terminaison de notification de suppression de compte d’Konvergo ERP

    * Un jeton de vérification

![Champs dédiés pour saisir les détails du point de
terminaison](../../../../_images/ebay-notification-endpoint.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>L’administrateur peut modifier les deux derniers champs une fois que le champ de l’adresse email est rempli.</p>
</div>

### Vérifier la connectivité au point de terminaison

Après avoir défini les détails du point de terminaison récupéré dans le
tableau de bord d’eBay, pensez à tester la connectivité avec le bouton
**Envoyer une notification de test**.

> Vous devriez recevoir le message de confirmation suivant : « Une
> notification de test a été envoyée avec succès ! »

![Bouton pour envoyer la notification de test](../../../../_images/test-
notification.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="manage">Comment répertorier un produit ?</a></p></li>
<li><p><a href="linking_listings">Associer des annonces existantes</a></p></li>
<li><p><a href="setup">Configuration du connecteur eBay</a></p></li>
</ul>
</div>

