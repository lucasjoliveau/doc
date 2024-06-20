# Facturation basée sur les quantités livrées ou commandées

Des politiques commerciales différentes peuvent nécessiter des options de
facturation différentes :

  * La règle _Facturer les produits commandés_ est utilisée par défaut dans Odoo _Ventes_ , ce qui signifie que les clients sont facturés une fois que le bon de commande est confirmé.

  * La règle _Facturer les produits livrés_ facture les clients une fois que la livraison est effectuée. Cette règle est souvent utilisée pour les entreprises qui vendent des matériaux, des liquides ou des denrées alimentaires en grande quantité. Dans ces cas, la quantité commandée peut différer légèrement de la quantité livrée et il est donc préférable de facturer la quantité effectivement livrée.

Le fait de pouvoir disposer de différentes options de facturation offre une
plus grande flexibilité.

## Fonctionnalités de la politique de facturation

Pour activer les fonctionnalités nécessaires de la politique de facturation,
allez à l’application Ventes ‣ Configuration ‣ Paramètres, et dans la section
Facturation, sélectionnez une règle de Politique de facturation : Facturer les
produits commandés ou Facturer les produits livrés.

![Choisir une politique de facturation dans Odoo
Ventes.](../../../../_images/invoicing-policy-setting.png)

Important

Si vous choisissez la règle Facturer les produits livrés, il n’est **pas**
possible d’activer la fonctionnalité Facture automatique, qui permet de
générer automatiquement des factures une fois qu’un paiement en ligne est
confirmé.

## Politique de facturation sur la fiche du produit

Sur n’importe quelle page de produit, via l’application Ventes ‣ Produits ‣
Tableau de bord des produits, trouver l’option Politique de facturation dans
l’onglet Informations générales. Il est possible de la modifier manuellement à
l’aide du menu déroulant.

![Comment modifier votre politique de facturation sur une fiche de produit
dans Odoo Ventes.](../../../../_images/invoicing-policy-general-info-tab.png)

## Impact sur le flux des ventes

Dans Odoo _Ventes_ , le flux de vente de base commence par la création d’un
devis. Ce devis est ensuite envoyé au client. Il doit alors être confirmé, ce
qui transforme le devis en bon de commande. Ce dernier crée à son tour une
facture.

Voici une analyse de l’impact des règles de politique de facturation sur un
flux de vente :

  * Facturer les produits commandés : Aucun impact sur le flux de vente de base. Une facture est créée dès qu’une vente est confirmée.

  * Facturer les produits livrés : Impact mineur sur le flux de vente, car la quantité livrée doit être saisie manuellement sur le bon de commande. Toutefois, vous pouvez installer et utiliser l’application _Inventaire_ pour confirmer la quantité livrée avant de créer une facture avec l’application _Ventes_.

Avertissement

Si un utilisateur tente de créer une facture sans valider la quantité livrée,
le message d’erreur suivant apparaît : Il n’y a aucune ligne facturable. Si un
produit a une politique de facturation basée sur les quantités livrées,
veuillez vous assurer qu’une quantité a été livrée.

![Si la politique de facturation basée sur les quantités livrées est choisie,
assurez-vous qu'une quantité a été livrée.](../../../../_images/invoicing-
policy-error-message.png)

Note

Une fois qu’un devis est confirmé et que le statut passe de Devis envoyé à Bon
de commande, vous pouvez voir les quantités livrées et facturées directement à
partir du bon de commande. C’est vrai pour les deux options de règles de
politique de facturation.

![Comment voir vos quantités livrées et facturées dans Odoo
Ventes.](../../../../_images/invoicing-policy-order-lines.png)

Odoo ajoute automatiquement les quantités à la facture, à la fois les
quantités livrées et facturées, même s’il s’agit d’une livraison partielle,
lorsque le devis est confirmé.

Enfin, il existe différentes options pour créer une facture : Facture normale,
Acompte (pourcentage) ou Acompte (montant fixe).

Pour plus d'infos

Pour en savoir plus, consultez la documentation expliquant les options
d’acompte : [Acomptes](down_payment.html)

