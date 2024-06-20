# Utiliser des E-wallets et des cartes-cadeaux

Avec Odoo, les clients peuvent utiliser des **E-wallets** et des **cartes-
cadeaux** pour leurs achats en ligne et en magasin.

Pour activer les e-wallets et les cartes-cadeaux pour l’eCommerce et le Point
de Vente (PdV), activez d’abord les Remises, Fidélité & Cartes-cadeaux dans
Ventes ‣ Configuration ‣ Paramètres ‣ Tarif. Une fois la fonctionnalité
activée, allez à Ventes ‣ Produits ‣ Cartes-cadeaux & e-wallet et créez un
nouveau programme de e-wallet ou de carte-cadeau.

## E-wallets

Les e-wallets permettent aux clients d’enregistrer des crédits sur leur compte
en ligne et d’utiliser ces crédits comme mode de paiement lors de l’achat
d’articles dans une boutique en ligne ou un magasin traditionnel. Les
e-wallets peuvent également être utilisés pour centraliser plusieurs cartes-
cadeaux.

Avant de créer un programme e-wallet, il faut créer un produit de **recharge**
e-wallet. Les recharges sont des crédits numériques prédéfinis ajoutés à un
e-wallet en échange de leur équivalent en monnaie réelle. Ces crédits peuvent
alors être utilisés comme mode de paiement dans la boutique eCommerce ou PdV.
Les valeurs des recharges peuvent varier.

Example

Une recharge de 50 $ coûte 50 $ et ajoute le même montant de crédits au
e-wallet.

Pour créer un produit de recharge, allez à Ventes ‣ Produits ‣ Produits et
créez un nouveau produit. Sur la fiche produit, configurez les options comme
suit :

  * Nom du produit : donnez un nom au produit de recharge (par exemple `Recharge de 50 $`)

  * Peut être vendu : activé

  * Type de produit : sélectionnez Service

  * Politique de facturation : sélectionnez Prépayé/Prix fixe

  * Créer à la commande : sélectionnez Rien

  * Prix de vente : saisissez le montant de la recharge

Note

Pour avoir des recharges e-wallet de montants différents, créez plusieurs
produits de recharge et modifiez le prix de vente en conséquence.

Une fois la recharge créée, allez à ventes ‣ Produits ‣ Cartes-cadeaux &
e-wallet pour créer un programme e-wallet. Les options de configuration
suivantes sont disponibles :

  * Nom du programme : donnez un nom au programme e-wallet

  * Type de programme : sélectionnez E-wallet

  * Produits e-wallet : sélectionnez la recharge e-wallet créée auparavant. Répétez le processus si vous avez créé des recharges de montants différents.

  * Modèle d’email : sélectionnez le modèle d’email utilisé pour l’email envoyé au client. Pour créer un nouveau modèle, cliquez sur le champ, sélectionnez Recherche avancée et cliquez ensuite sur Créer.

  * Devise : sélectionnez la devise à utiliser pour le programme e-wallet

  * Société : sélectionnez la société pour laquelle le programme est valable et disponible

  * Disponible sur : sélectionnez les applications sur lesquelles le programme est valable et disponible

  * Site web : sélectionnez le site web sur lequel le programme est valable et disponible. Laissez ce champ vide pour inclure tous les sites web

  * Point de vente : sélectionnez le PdV sur lequel le programme est valable et disponible. Laissez ce champ vide pour inclure tous les points de vente.

![Page de configuration du programme e-wallet](../../../../_images/ewallet-
configuration.png)

Une fois le programme configuré, cliquez sur le bouton Générer un e-wallet
dans le coin supérieur gauche pour générer les e-wallets. Les e-wallets
peuvent être générés en fonction des clients et/ou des étiquettes des clients.
La quantité est automatiquement adaptée en fonction des clients et des
étiquettes des clients. Définissez ensuite la valeur e-wallet. Enfin,
définissez la période de validité Valide jusqu’au, si applicable.

Les e-wallets générés sont accessibles via le bouton intelligent e-wallets
dans le coin supérieur droit. De là, vous pouvez envoyer ou partager les
e-wallets par email ou par URL.

![Boutons d'envoi et de partage pour les
e-wallets](../../../../_images/ewallet-share.png)

Cliquez sur un e-wallet pour modifier la date de fin de validité, le
partenaire ou le solde. Le code d’un e-wallet ne peut _pas_ être modifié,
supprimé ou dupliqué.

## Cartes-cadeaux

Les cartes-cadeaux peuvent être achetées par les clients et utilisées comme
mode de paiement lors du passage en caisse dans une boutique d’eCommerce ou un
PdV.

Avant de créer un nouveau programme de carte-cadeau, vous devez créer un
produit de carte-cadeau. Pour ce faire, allez à Ventes ‣ Produits ‣ Produits
et créez un produit. Sur la fiche produit, configurez les options comme suit :

  * Nom du produit : donnez un nom au produit de carte-cadeau

  * Peut être vendu : activé

  * Type de produit : sélectionnez Service

  * Politique de facturation : sélectionnez Prépayé/Prix fixe

  * Créer à la commande : sélectionnez Rien

  * Prix de vente : saisissez le montant de la carte-cadeau

Note

Pour avoir des cartes-cadeaux de montants différents, créez plusieurs produits
de carte-cadeau et modifiez le prix de vente en conséquence.

Une fois le produit de carte-cadeau créé, allez à Ventes ‣ Produits ‣ Cartes-
cadeaux & e-wallet pour Créer un programme de carte-cadeau. Les opérations de
configuration suivantes sont disponibles :

  * Nom du programme : donnez un nom au programme de carte-cadeau

  * Type de programme : sélectionnez Carte-cadeau

  * Produits carte-cadeau : sélectionnez le produit de carte-cadeau créé auparavant. Répétez le processus si vous avez créé des cartes-cadeaux de montants différents.

  * Modèle d’email : sélectionnez le modèle Carte-cadeau : Informations de la carte-cadeau par défaut ou créez un nouveau modèle en cliquant sur le champ, en sélectionnant Recherche avancée et ensuite en cliquant sur Créer.

  * Imprimer le rapport : sélectionnez Carte-cadeau

  * Devise : sélectionnez la devise pour utiliser le programme de carte-cadeau

  * Société : sélectionnez la société pour laquelle le programme est valable et disponible

  * Disponible sur : sélectionnez les applications sur lesquelles le programme est valable et disponible

  * Site web : sélectionnez le site web sur lequel le programme est valable et disponible. Laissez ce champ vide pour inclure tous les sites web

  * Point de vente : sélectionnez le PdV sur lequel le programme est valable et disponible. Laissez ce champ vide pour inclure tous les points de vente.

![Page de configuration du programme de carte-
cadeau](../../../../_images/giftcard-configuration.png)

Une fois le programme configuré, cliquez sur le bouton Générer des cartes-
cadeaux dans le coin supérieur gauche pour générer des cartes-cadeaux. Des
cartes-cadeaux peuvent être générées soit pour des Clients anonymes ou des
Clients sélectionnés. Définissez la Quantité à générer pour les Clients
anonymes ou sélectionnez les Clients et/ou les Étiquettes des clients pour les
Clients sélectionnés. Ensuite, définissez la valeur de la carte-cadeau et la
période de validité Valide jusqu’au, si applicable.

Les cartes-cadeaux générées sont accessibles via le bouton intelligent Cartes-
cadeaux dans le coin supérieur droit. De là, vous pouvez envoyer ou partager
les cartes-cadeaux via email ou par URL.

![Boutons d'envoi et de partage pour les cartes-
cadeaux](../../../../_images/giftcard-share.png)

Cliquez sur une carte-cadeau pour modifier la date de fin de validité, le
partenaire ou le solde. Le code d’une carte-cadeau ne peut _pas_ être modifié,
supprimé ou dupliqué.

  *[PdV]: Point de Vente

