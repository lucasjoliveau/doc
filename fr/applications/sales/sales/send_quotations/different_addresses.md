# Livrer et facturer à des adresses différentes

Les particuliers et les sociétés utilisent souvent des adresses distinctes
pour la facturation et la livraison. Avec l’application _Ventes_ d’Odoo, les
contacts peuvent préciser différentes adresses pour la livraison et la
facturation.

## Paramètres

Pour correctement utiliser plusieurs adresses dans Odoo, allez à l’application
Ventes ‣ Configuration ‣ Paramètres et faites défiler jusqu’à la section Devis
& Commandes. Cochez ensuite la case à côté de l’option Adresses du client et
cliquez sur Enregistrer.

![Activez le paramètre Adresses du client.](../../../../_images/customer-
addresses-setting.png)

## Configuration du formulaire de contact

Pour ajouter plusieurs adresses à un contact, allez à l’application Ventes ‣
Commandes ‣ Clients et supprimez tous les filtres par défaut de la barre de
recherche. Cliquez ensuite sur le client souhaité pour ouvrir leur formulaire
de contact.

Astuce

Vous pouvez également accéder aux formulaires de contact via l’application
_Contacts_.

Sur le formulaire de contact, cliquez sur Modifier, puis sur Ajouter, qui se
trouve dans l’onglet Contacts & Adresses. Cette opération fait apparaître un
formulaire contextuel Créer contact dans lequel vous pouvez configurer des
adresses supplémentaires.

![Ajoutez un contact/une adresse au formulaire de
contact.](../../../../_images/contact-form-add-address1.png)

Dans le formulaire contextuel Créer contact, commencez par cliquer sur le
champ Autre adresse par défaut pour afficher un menu déroulant d’options
relatives à l’adresse.

Sélectionnez l’une des options suivantes :

  * Contact : ajoute un autre contact au formulaire de contact existant.

  * Adresse de facturation : ajoute une adresse de facturation spécifique à un formulaire de contact existant.

  * Adresse de livraison : ajoute une adresse de livraison spécifique au formulaire de contact existant.

  * Autre adresse : ajoute une adresse alternative au formulaire de contact existant.

  * Adresse personnelle : ajoute une adresse personnelle au formulaire de contact existant.

Lorsque vous avez sélectionné une option, saisissez les informations de
contact correspondantes à utiliser pour ce type d’adresse spécifié.

![Créez un nouveau contact/une nouvelle adresse sur un formulaire de
contact.](../../../../_images/create-contact-window1.png)

Cliquez ensuite sur Enregistrer & Fermer pour enregistrer l’adresse et fermer
la fenêtre Créer contact. Ou cliquez sur Enregistrer & Nouveau pour
enregistrer l’adresse et immédiatement en saisir une autre.

## Adresse ajoutée aux devis

Lorsqu’un client est ajouté à un devis, les champs Adresse de facturation et
Adresse de livraison se remplissent automatiquement en fonction des adresses
précisées sur le formulaire de contact du client.

![Les adresses de facturation et de livraison se remplissent automatiquement
dans un devis.](../../../../_images/quotation-address-autopopulate.png)

Il est également possible de modifier l”Adresse de facturation et l”Adresse de
livraison directement à partir du devis en cliquant sur le bouton Modifier,
puis sur les boutons de lien interne ➡️ (flèche droite) à côté de chaque ligne
d’adresse.

Ces adresses peuvent être mises à jour à tout moment pour garantir
l’exactitude de la facturation et de la livraison.

Astuce

Si des modifications sont apportées à un formulaire dans Odoo, y compris aux
formulaires de _Contact_ , n’oubliez pas de cliquer sur Enregistrer pour
enregistrer les modifications dans la base de données.

