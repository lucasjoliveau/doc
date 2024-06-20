# Comment répertorier un produit ?

Odoo propose deux façons de répertorier un produits sur eBay et Odoo :

  1. (_Preferred method_) Make a product in Odoo and list the item eBay.

     * Cliquez sur Vendre l’article sur eBay dans le menu supérieur du modèle de produit. Vous pouvez accéder au modèle de produit en allant à l’application Ventes ‣ Produits ‣ Produit et en sélectionnant le produit individuel.

  2. (_Less preferred method_) List the item on eBay, then create the product in Odoo, and finally link product to the item on eBay.

     * Cliquez sur Associer avec une annonce eBay existante dans le menu supérieur du modèle de produit. Vous pouvez accéder au modèle de produit en allant à l’application Ventes ‣ Produit ‣ Produit et en sélectionnant le produit individuel.

Note

Lorsqu’une commande est placée et l’annonce de la commande n’est pas associée
à un produit, eBay créera un produit consommable. Ces consommables doivent
être modifiés sur la _commande_ en brouillon afin de représenter un produit
stockable et l’utilisateur peut ensuite l’associer à l’annonce.

Pour plus d'infos

Pour en apprendre plus sur le connecteur eBay, consultez également ces pages :

  * [Configuration du connecteur eBay](setup.html)

  * [Associer des annonces existantes](linking_listings.html)

  * [Dépannage du connecteur eBay](troubleshooting.html)

## Répertorier sans variantes

Accéder au modèle de produit en allant à l’application Ventes ‣ Produits ‣
Produit et en sélectionnant le produit individuel.

Afin de répertorier un produit, sélectionnez le champ Vendre sur eBay sur un
modèle de produit. L’option Vendre sur eBay se trouve dans un onglet eBay ou
sous le Nom du produit. Cliquez sur Enregistrer le cas échéant.

![Le formulaire de modèle d'eBay dans le modèle de produit dans
Odoo.](../../../../_images/manage-ebay-template.png)

Lorsque la case Utiliser la quantité en stock est cochée, la quantité définie
sur eBay sera la _Quantité prévue*_ dans Odoo (application _Inventaire_
d’Odoo).

Le Modèle de description permet à l’administrateur d’utiliser les modèles dans
les annonces. Le modèle par défaut n’utilise que le champ Description eBay du
produit. Du HTML peut être utilisé dans le Modèle de description et dans la
Description eBay dans Odoo 14. À partir d’Odoo 15, la fonctionnalité de la
boîte à outils peut être utilisée dans le modèle et la description. Tapez
simplement une barre oblique `/` pour afficher un menu avec formatage, mise en
page et options de texte. Pour ajouter une image, tapez `/image`.

Pour utiliser des images dans l’annonce, vous avez l’option de les ajouter en
tant que _pièces jointes_ sur le modèle du produit.

Pour plus d'infos

For more information on template configuration in Odoo visit: [Modèles
d’email](../../../general/companies/email_template.html).

## Répertorier avec variantes

Lorsque la case Vendre sur eBay est cochée sur un produit contenant des
versions avec Prix fixe en tant que Type d’annonce, le formulaire eBay est
légèrement différent. Allez à l’onglet Versions ou cliquez sur Configurer des
versions dans le menu supérieur pour configurer les paramètres de la version.
Vous pouvez configurer le prix pour chaque version.

Lorsque vous modifiez le Type d’annonce en Prix fixe, Odoo affiche un tableau
des variantes au bas de l’onglet eBay, dans lequel vous pouvez saisir le Prix
fixe et la décision de Publier sur eBay des variantes spécifiques, ainsi que
d’autres options.

![Le type d'annonce à prix fixe dans l'onglet eBay dans un formulaire de
produit dans Odoo Ventes.](../../../../_images/fixed-listing-price.png)

## Identifiants de produit

Les identifiants de produits tels qu’EAN, UPC, Brand ou MPN sont requis pour
la plupart des catégories d’eBay.

### Identifiants EAN et UPC

Le module gère les identifiants EAN et UPC avec le champ Code-barres de la
variante du produit. Si le champ Code-barres est vide ou si la valeur n’est
pas valide, les valeurs EAN et UPC seront définies sur “Non applicable” comme
il est recommandé par eBay.

Vous pouvez trouver les codes-barres sur le modèle de produit, dans l’onglet
Informations générales. Accédez d’abord au modèle de produit en allant à
l’application Ventes ‣ Produits ‣ Produit et en sélectionnant le produit
individuel.

### Répertorier avec des caractéristiques de produit

Afin d’ajouter des caractéristiques d’un article, vous devez créer un attribut
de produit avec une seule valeur dans l’onglet Attributs & Variantes sur le
formulaire de produit. Voici quelques exemples de caractéristiques : `MPN` ou
`Brand`. Les valeurs Brand et MPN sont des caractéristiques de l’article et
doivent être définies dans l’onglet Attributs & Variantes sur le formulaire du
produit. Si ces valeurs ne sont pas définies, l’option “Non applicable” sera
utilisée pour l’annonce eBay.

## Traiter des factures et des paiements

### Enregistrer un paiement

Lorsqu’une commande eBay est placée, elle est toujours payée à l’avance, via
le site d’eBay. À aucun moment, les utilisateurs payent les articles sur eBay
via Odoo. Par conséquent, dès que les commandes sont synchronisées dans Odoo à
partir d’eBay, elles sont déjà payées. Les fonctionnalités de facturation et
de paiement d’Odoo ne sont pas utilisées. Cependant, vous devez créer des
factures et les marquer comme payées afin de « fermer » la _commande_.

Les utilisateurs peuvent choisir de créer des factures en masse et de les
enregistrer en lots. Pour ce faire, allez aux devis dans la vue de liste en
allant à l’application Ventes ‣ Commandes ‣ Devis. Dans le coin supérieur
droit, sélectionnez l’icône de la vue de liste. Passez la souris sur les
icônes pour afficher le nom de chacune. Cochez ensuite sur la gauche les cases
des commandes pour lesquelles les factures doivent être établies et allez au
menu Action ou ⚙️ [Icône d’engrenage]. Cliquez sur Créer des factures.

Une fenêtre contextuelle apparaît et vous pouvez cliquer sur le bouton Créer
et voir la facture. Un nouvel écran s’affiche avec les factures nouvellement
créées. Ensuite, sélectionnez-les toutes en cochant la case à côté de Nombre
dans la ligne d’en-tête de la liste, ce qui sélectionnera tous les
enregistrements. Accédez ensuite au menu Action et cliquez sur Enregistrer les
écritures. Après cette étape, une fenêtre contextuelle s’affiche et vous
pouvez cliquer sur Enregistrer les pièces comptables. Les factures ne seront
plus en _brouillon_ et seront _comptabilisées_.

### Lettrer des paiements

Les utilisateurs utilisent généralement PayPal pour recevoir des paiements
d’eBay, puis envoient des sommes forfaitaires de PayPal sur leur compte
bancaire. Pour lettrer ces revenus, les utilisateurs peuvent lettrer un
transfert PayPal avec toutes les factures concernées.

Allez d’abord au Tableau de bord de Comptabilité via l’application
Comptabilité ‣ Tableau de bord ‣ Banque. Créez une nouvelle transaction et
saisissez le Libellé `ventes eBay`. Complétez le montant Montant et saisissez
une date de relevé. Cliquez sur Créer et modifier.

Dans le champ Solde final, saisissez le même montant que vous avez saisi dans
le champ Montant. Cliquez sur Enregistrer. Ensuite, ouvrez le nouveau solde
qui doit être lettré. Sous l’onglet intitulé : Rapprocher des écritures
existantes, sélectionnez les écritures qui sont incluses dans ce solde.

Après avoir ajouté toutes les écritures nécessaires, cliquez sur Valider pour
terminer le lettrage. Pour vérifier le paiement, allez à la section Clients ‣
Factures et sélectionnez la facture client concernée. Le libellé _Payé_ doit
apparaître dans la colonne Statut du paiement.

Pour plus d'infos

  * [Dépannage du connecteur eBay](troubleshooting.html)

  * [Associer des annonces existantes](linking_listings.html)

  * [Configuration du connecteur eBay](setup.html)

