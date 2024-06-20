# Alertes automatiques

Maintenant que vos abonnements sont opérationnels, vous voulez rester à la
page avec vos clients. Un certain degré d’automatisation serait apprécié,
puisque vous n’avez pas envie de parcourir la liste de tous vos abonnés pour
vérifier comment les choses se passent. C’est à cela que sert la
fonctionnalité _Alertes automatiques_.

Par exemple, lorsqu’un client souscrit à votre magazine, vous aimeriez lui
envoyer un email pour lui souhaiter la bienvenue et exprimer votre
reconnaissance. Or, si le taux de satisfaction de vos clients tombe en dessous
de 50%, vous voudrez le contacter pour comprendre les raisons de leur
insatisfaction.

Avec **Odoo Abonnements** , vous pouvez définir des emails automatiques, créer
une tâche « Appeler » pour l’un de vos vendeurs pour qu’il essaie de
comprendre l’insatisfaction de votre client et, enfin, pourquoi ne pas envoyer
automatiquement des enquêtes de satisfaction pour que les clients puissent
évaluer vos services ? Tout cela est désormais possible.

## Créer une nouvelle alerte automatique

L’exemple suivant vous montre comment créer une nouvelle alerte automatique
pour envoyer des enquêtes de satisfaction à vos clients, par email, après un
mois d’abonnement. Pour ce faire, allez à Abonnements ‣ Configuration ‣
Alertes, et créez une nouvelle alerte.

![Nouvelle alerte automatique dans Odoo Abonnements](../../../_images/create-
a-new-automatic-alert.png)

  1. Dans la section _Appliquer sur_ , donnez d’abord un nom à l’alerte. Vous pouvez ensuite choisir d’appliquer cette alerte sur un modèle d’abonnement, sur un client spécifique ou même sur un produit spécifique. Si vous voulez ajouter plus de spécifications, vous pouvez également préciser la valeur de votre MRR, le taux de variation de votre MRR sur une période donnée, le taux de satisfaction et même l’étape sur laquelle vous voulez appliquer cette alerte.

Note

Dans cet exemple, l’alerte est appliquée sur un produit spécifique et l’étape
va de _Non défini_ à _En cours_.

  2. Quant à la section _Action_ , définissez les champs dans les cases _Action_ et _Déclencher sur_. Si la fonction _Déclencher sur_ est définie sur _Modification_ , l’action est déclenchée chaque fois qu’un changement ou un ajout est effectué dans l’abonnement, et que toutes les conditions de la section _Appliquer sur_ sont remplies. Maintenant, si l’action _Déclencher sur_ est définie sur _Condition temporisée_ , cela signifie que l’action est déclenchée sur la base du type de _Date de déclenchement_. Ensuite, vous pouvez choisir votre _Action_. Vous avez le choix entre _Créer l’activité suivante_ , _Définir une étiquette sur l’abonnement_ , _Définir une étape sur l’abonnement_ , _Marquer comme À renouveler_ , _Envoyer un email au client_ et _Envoyer un SMS au client_.

Note

Dans l’exemple ci-dessus, l’action _Déclencher sur_ est définie sur _Condition
temporisée_ , donc il faut préciser une _Date de déclenchement_ et un « Délai
après déclenchement*. Et comme l’action _Envoyer un email au client_ a été
choisie, un _Modèle d’email_ peut être choisi.

Note

Sending a SMS text message in Odoo requires In-App Purchase (IAP) credit or
tokens. For more information on IAP, visit [In-app purchases
(IAP)](../../essentials/in_app_purchase.html). For more information on sending
SMS messages, visit [Les essentiels de
SMS](../../marketing/sms_marketing/essentials/sms_essentials.html).

As a result, this alert sends a rating survey after one month, to the
customers who have purchased that specific product. The survey appears in the
chatter of your respective subscription.

![Enquête de satisfaction dans Odoo Abonnements](../../../_images/rating-
satisfaction-survey.png)

## Modifier une alerte automatique existante

Par défaut, Odoo vous propose une alerte automatique appelée _Prendre des
mesures à l’égard des clients moins satisfaits_.

![Modifier une alerte automatique existante dans Odoo
Abonnements](../../../_images/modify-an-existing-automatic-alert.png)

Cette alerte s’applique à l” _Évaluation de la satisfaction_ de vos clients et
l’action est déclenchée sur une _Condition temporisée_. Si leur taux de
satisfaction est inférieur à 50%, un vendeur contacte le client. Cette action
est automatiquement assignée au vendeur qui gère l’abonnement et la date
d’échéance est de 5 jours après le déclenchement de cette action. Cette alerte
garantit que vos clients sont satisfaits et que des mesures sont prises s’ils
ne le sont pas. Elle contribue à maintenir un taux de rétention des clients
très élevé.

Note

En éditant l’alerte, vous pouvez modifier l’action _Appliquer sur_ , les
sections _Action_ et _Activité_ et les adapter à vos propres besoins.

Pour plus d'infos

  * [Abonnements](../subscriptions.html)

  * [Plans d’abonnement](plans.html)

  * [Produits d’abonnement](products.html)

  * [In-app purchases (IAP)](../../essentials/in_app_purchase.html)

  *[IAP]: In-App Purchase

