# Réapprovisionner sur commande (MTO)

_Réapprovisionner sur commande_ , également connu comme _MTO_ (fabrication à
la commande), est une stratégie de réassort qui crée un ordre brouillon pour
un produit chaque fois qu’une commande client est créée pour ce produit. Pour
les produits qui sont achetés auprès d’un fournisseur, une demande de prix est
créée, alors que la commande d’un produit fabriqué en interne entraîne la
création d’un ordre de fabrication. La création d’une demande de prix ou d’un
ordre de fabrication se fait chaque fois qu’une commande client est créée,
indépendamment du niveau de stock actuel du produit commandé.

## Désarchiver la route Réapprovisionner sur commande (MTO)

Konvergo ERP définit la route MTO par défaut sur _archivé_ , car MTO est un flux de
travail de niche qui n’est utilisé que par certaines entreprises. Cependant,
il est facile de désarchiver la route en quelques étapes simples.

Pour ce faire, allez à Inventaire ‣ Configuration ‣ Routes. Sur la page des
**Routes** , cliquez sur le bouton **Filtres** et sélectionnez l’option
**Archivé**. Cette option permet d’afficher toutes les options qui sont
actuellement archivées.

![Le filtre archivé sur la page des routes.](../../../../../_images/archived-
filter.png)

Cochez la case à côté de **Réapprovisionner sur commande (MTO)** , puis
cliquez sur le bouton **Action** pour faire apparaître un menu déroulant. Dans
le menu déroulant, sélectionnez **Désarchiver**.

![L'action désarchiver sur la page des
routes.](../../../../../_images/unarchive-button.png)

Enfin, supprimez le filtre **Archivé** de la barre **Rechercher…**. La page
**Routes** affiche désormais toutes les routes disponibles, y compris la route
**Réapprovisionner sur commande (MTO)** , qui peut être sélectionnée dans
l’onglet Inventaire de chaque page de produit.

![La route MTO apparaît sur la page Routes après avoir été
désarchivée.](../../../../../_images/unarchived-mto.png)

## Configurer un produit pour utiliser la route MTO

La route MTO ayant été désarchivée, les produits peuvent maintenant être
correctement configurés pour utiliser le réapprovisionnement à la commande.
Pour ce faire, allez à Inventaire ‣ Produits ‣ Produits, puis sélectionnez un
produit existant ou cliquez sur **Créer** pour en configurer un nouveau.

Sur la page du produit, sélectionnez l’onglet **Inventaire** et activez la
route **Réapprovisionner sur commande (MTO)** dans la section **Routes** ,
ainsi qu’une autre route.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La route <b>Réapprovisionner sur commande (MTO)</b> ne <b>fonctionne pas</b> à moins qu’une autre route ne soit sélectionnée. Konvergo ERP a en effet besoin de savoir comment réapprovisionner le produit lorsqu’une commande est passée pour celui-ci (acheter, fabriquer, etc.).</p>
</div> ![Sélectionnez la route MTO et une seconde route dans
l'onglet Inventaire.](../../../../../_images/select-routes.png)

Si le produit est acheté auprès d’un fournisseur pour honorer des commandes,
cochez la case **Peut être acheté** sous le nom du produit. L’onglet
**Achats** apparaît alors à côté des autres onglets de paramétrage ci-dessous.

Sélectionnez l’onglet **Achats** et précisez un **Fournisseur** et le **Prix**
auquel il vend le produit.

![Activez "Peut être acheté" et précisez un
fournisseur.](../../../../../_images/specify-vendor.png)

Si le produit est fabriqué, assurez-vous qu’une nomenclature est configurée
pour ce produit. Pour ce faire, cliquez sur le bouton intelligent
**Nomenclature** en haut de l’écran, puis cliquez sur **Créer** sur la page
**Nomenclature** pour configurer une nouvelle nomenclature pour le produit.

Sur le formulaire de nomenclature vierge, ajoutez les composants utilisés pour
fabriquer le produit dans l’onglet **Composants** , ainsi que les opérations
requises pour le flux de travail de fabrication dans l’onglet **Opérations**.

Cliquez enfin sur **Enregistrer** pour enregistrer la nomenclature.

## Honorer une commande client en utilisant la route MTO

Après avoir configuré un produit pour utiliser la route MTO, un ordre de
réassort est créé chaque fois qu’une commande client incluant le produit est
créé. Le type d’ordre créé dépend également de la seconde route sélectionnée
en plus de la route MTO.

Par exemple, si la seconde route sélectionnée est _Acheter_ , un bon de
commande est créé lors de la confirmation d’une commande client.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Lorsque la route <abbr title="make to order">MTO</abbr> est activée pour un produit, un ordre de réassort est toujours créé lors de la confirmation d’une commande client. C’est le cas même si le stock du produit disponible est suffisant pour honorer la commande, sans acheter ou fabriquer d’unités supplémentaires.</p>
</div>

Alors que la route MTO peut être utilisée en même temps qu’une variété
d’autres routes, la route _Acheter_ est utilisée comme exemple pour ce flux de
travail. Allez à l’application Ventes, puis cliquez sur **Créer** , ce qui
ouvre un formulaire de devis vierge.

Sur le formulaire de devis vierge, ajoutez un **Client** , puis cliquez sur
**Ajouter un produit** dans l’onglet **Lignes de la commande** et saisissez un
produit qui a été configuré pour utiliser les routes _MTO_ et _Acheter_.
Cliquez sur **Confirmer** et le devis se transforme en commande client.

Un bouton intelligent **Achat** apparaît dans le coin supérieur droit de la
commande client. Le fait de cliquez dessus ouvre la demande de prix associée à
la commande client.

Cliquez sur **Confirmer la commande** pour confirmer la demande de prix et la
transformer en bon de commande. Un bouton vert **Recevoir les produits**
apparaît en haut du bon de commande. Une fois que les produits sont reçus,
cliquez sur **Recevoir les produits** pour les enregistrer dans l’inventaire.

Retournez à la commande en cliquant sur le fil d’Ariane **Bons de commande**
ou en allant à Ventes ‣ Commandes ‣ Commandes et en sélectionnant la commande
client.

Enfin, cliquez sur le bouton intelligent **Livraison** dans le coin supérieur
droit de la commande pour être redirigé vers le bon de livraison. Une fois que
les produits ont été expédiés au client, cliquez sur **Valider** pour
confirmer la livraison.

  *[MTO]: make to order

