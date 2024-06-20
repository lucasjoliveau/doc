# Programmes de remise et de fidélité

Les applications _Ventes_ , _eCommerce_ et _Point de Vente_ d’Odoo permettent
aux utilisateurs de créer des programmes de remise et de fidélité que les
clients peuvent utiliser lors de leur shopping en ligne et en magasin. Ces
programmes proposent des options de prix plus variées, publiques et
temporelles que les [listes de prix](prices/pricing.html).

## Configurer les paramètres

Pour commencer à utiliser des programmes de remise et de fidélité, allez à
Ventes ‣ Configuration ‣ Paramètres. Sous l’en-tête Tarif, activez le
paramètre Remises, Fidélité & Cartes-Cadeaux en cochant la case à côté de la
fonctionnalité. Finalement, cliquez sur Enregistrer pour enregistrer les
modifications.

## Configurer des programmes de remise et de fidélité

Pour créer des programmes de remise et de fidélité, allez à Ventes ‣ Produits
‣ Remise & Fidélité.

Si aucun programme de remise ou de fidélité n’a encore été créé, Odoo propose
un choix de modèles pour vous aider à créer le premier programme. Choisissez
l’une des cartes modèles ou cliquez sur Nouveau pour créer un nouveau
programme à partir de zéro.

Ou, s’il existe déjà des programmes, sélectionnez un programme existant pour
le modifier.

![Cartes modèles de programmes de remise et de
fidélité.](../../../../_images/price-discount-loyalty.png)

Note

Les modèles n’apparaissent que lorsqu’aucun programme n’a été créé et ils
disparaissent dès que le premier programme est créé.

La création ou l’édition d’un programme ouvre le formulaire du programme.

Le formulaire du programme contient les options suivantes :

  * Nom du programme : Saisissez le nom du programme. Le nom du programme n’est _pas_ visible pour le client.

  * Type de programme : Sélectionnez le type de programme souhaité.

  * Devise : Sélectionnez la devise utilisée pour le programme.

  * Unité de points : Saisissez le nom des points utilisés pour le programme des Cartes de fidélité (par ex. `Points de fidélité`). Le nom de l’unité des points _est_ visible pour le client. Ce champ n’est disponible que lorsque le Type de programme est défini sur Cartes de fidélité.

  * Validité : Sélectionnez la date jusqu’à laquelle le programme est valide. Laissez ce champ vide pour qu’il n’y ait pas de date de fin, ce qui signifie que le programme est toujours valide et n’expire pas.

  * Limite d’utilisation : Cochez cette case et saisissez un nombre pour limiter le nombre de fois que le programme peut être utilisé pendant la période de Validité.

  * Société : Dans le cas de plusieurs sociétés, choisissez la société pour laquelle le programme est disponible.

  * Disponible sur : Sélectionnez la ou les applications sur lesquelles le programme est disponible.

  * Site web : Sélectionnez le ou les sites web sur lesquels le programme est disponible. Laissez ce champ vide pour que le programme soit disponible sur tous les sites web.

  * Point de Vente : Sélectionnez le ou les points de vente où le programme est disponible. Laissez ce champ vide pour que le programme soit disponible dans tous les PdV.

![Les options du programme dans le formulaire du programme de
fidélité.](../../../../_images/price-programs.png)

Note

Les options disponibles sur le formulaire du programme varient en fonction du
Type de programme sélectionné.

Toutes les cartes, tous les codes, tous les bons de réduction, etc. qui ont
été générés pour le programme sont accessibles via le bouton intelligent situé
dans le coin supérieur droit du formulaire.

![Bouton intelligent des éléments du programme sur le formulaire du programme
de fidélité.](../../../../_images/price-programs-items.png)

### Types de programme

Les différents Types de programme disponibles sur le formulaire du programme
sont :

  * Bons de réduction : Générez et partagez des codes promo à usage unique qui donnent un accès immédiat aux récompenses.

  * Bons de réduction pour la prochaine commande : Générez et partagez des codes promo à usage unique qui donnent accès à des récompenses lors de la prochaine commande du client.

  * Loyalty Cards: When making purchases, the customer accumulates points to exchange for rewards on current and/or future orders.

  * Promotions : Définissez des règles conditionnelles pour la commande de produits qui, lorsqu’elles sont remplies, donnent accès à des récompenses pour le client.

  * Code de remise : Définissez des codes de remises qui, lorsqu’ils sont saisis au moment du paiement, permettent au client de bénéficier de remises.

  * Achetez X Recevez Y : Pour chaque article X acheté, le client reçoit 1 crédit. Après avoir accumulé un certain nombre de crédits, le client peut les échanger contre un article Y.

### Règles conditionnelles

Ensuite, configurez les Règles conditionnelles qui déterminent quand le
programme s’applique à la commande d’un client.

Dans l’onglet Règles & Récompenses, cliquez sur Ajouter à côte de Règles
conditionnelles pour ajouter des _conditions_ au programme. La fenêtre
contextuelle Créer des règles conditionnelles s’affiche.

![Onglet Règles & Récompenses du formulaire du programme de
fidélité.](../../../../_images/price-conditional-rewards.png)

Note

Les options des Règles conditionnelles varient en fonction du Type de
programme sélectionné.

Les options suivantes sont disponibles pour configurer les règles
conditionnelles :

  * Code de remise : Saisissez un code personnalisé à utiliser pour le programme Code de remise ou utilisez le code par défaut généré par Odoo. Ce champ n’est disponible que lorsque le Type de programme est défini sur Code de remise.

  * Quantité minimale : Saisissez le nombre minimum de produits qui doivent être achetés pour accéder à la récompense. Définissez la quantité minimale sur au moins `1` pour vous assurer que le client doit effectuer un achat pour accéder à la récompense.

  * Achat minimum : Saisissez le montant minimum (en devise), toutes taxes comprises ou hors taxes, qui doit être dépensé pour accéder à la récompense. Si une quantité minimale _et_ un montant d’achat minimal sont saisis, la commande du client doit remplir ces deux conditions.

  * Produits : Sélectionnez le ou les produits spécifiques pour le(s)quel(s) le programme s’applique. Laissez ce champ vide pour l’appliquer à tous les produits.

  * Catégories : Sélectionnez la catégorie des produits à laquelle le programme s’applique. Choisissez All pour l’appliquer à toutes les catégories de produits.

  * Étiquette du produit : Sélectionnez une étiquette pour appliquer le programme aux produits ayant cette étiquette spécifique.

  * Accorder : Saisissez le nombre de points que le client reçoit par commande, par devise dépensé ou par unité payée (pour les programmes Cartes de fidélité et Achetez X Recevez Y).

![Fenêtre de configuration des règles conditionnelles pour un programme de
remise ou de fidélité.](../../../../_images/price-conditions.png)

Cliquez sur Enregistrer & fermer pour enregistrer la règle et fermer la
fenêtre contextuelle ou cliquez sur Enregistrer & Nouveau pour enregistrer la
règle et en créer une nouvelle immédiatement.

### Récompenses

Dans l’onglet Règles & Récompenses du formulaire de programme, cliquez sur
Ajouter à côté de Récompenses pour ajouter des _récompenses_ au programme. La
fenêtre contextuelle Créer des récompenses s’affiche.

Note

Les options des Récompenses varient en fonction du Type de programme
sélectionné.

Les options suivantes sont disponibles pour configurer les récompenses :

  * Type de récompense : Sélectionnez le type de récompense parmi Produit gratuit, Remise et Expédition gratuite. Les autres options de configuration des récompenses dépendent du Type de récompense sélectionné.

    * Produit gratuit :

      * Quantité récompensée : Sélectionnez le nombre de produits gratuits offerts au client.

      * Produit : Sélectionnez le produit offert en récompense. Un seul produit peut être sélectionné.

      * Étiquette de produit : Sélectionnez une étiquette pour préciser le produit gratuit pouvant faire l’objet d’une récompense.

    * Remise :

      * Remise : Saisissez le montant de la remise en pourcentage, devise par point ou devise par commande. Sélectionnez ensuite si la remise s’applique à l’ensemble de la Commande, uniquement au Produit le moins cher de la commande ou uniquement à des Produits spécifiques.

      * Remise maximale : Saisissez le montant maximum (en devise) que cette récompense peut accorder comme remise. Laissez ce champ à `0` pour ne pas fixer de limite.

    * Expédition gratuite :

      * Remise maximale : Saisissez le montant maximum (en devise) que cette récompense peut accorder comme remise. Laissez ce champ à `0` pour ne pas fixer de limite.

  * En échange de : Saisissez le nombre de points requis pour échanger la récompense (pour les programmes Cartes de fidélité et Achetez X Recevez Y).

  * Description sur la commande : Saisissez la description de la récompense, qui est affichée au client lors du paiement.

![Fenêtre de configuration des récompenses pour un programme de remise ou de
fidélité.](../../../../_images/price-rewards.png)

  *[PdV]: Points de vente

