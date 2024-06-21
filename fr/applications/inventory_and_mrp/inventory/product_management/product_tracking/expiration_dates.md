# Dates d’expiration

Dans Konvergo ERP, les _dates d’expiration_ peuvent être utilisées pour gérer et
suivre les cycles de vie des produits périssables, de l’achat à la vente.
l’utilisation des dates d’expiration réduit les pertes de produits dues à une
expiration inattendue, et permet d’éviter d’envoyer des produits périmés aux
clients.

Dans Konvergo ERP, seuls les produits qui sont suivis à l’aide de _lots_ et de
_numéros de série_ peuvent se voir assigner des informations relatives à
l’expiration. Une fois qu’un lot ou un numéro de série a été assigné, une date
d’expiration peut être définie. Ceci est particulièrement utile pour les
entreprises (telles que les fabricants de produits alimentaires) qui achètent
et vendent régulièrement, ou exclusivement, des produits périssables.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="lots">Lot numbers</a></p></li>
<li><p><a href="serial_numbers">Utiliser des numéros de série pour suivre des produits</a></p></li>
</ul>
</div>

## Activer les dates d’expiration

Pour activer l’utilisation des _dates d’expiration_ , allez à l’application
Inventaire ‣ Configuration ‣ Paramètres, et faites défiler jusqu’à la section
**Traçabilité**. Ensuite, cochez la case pour activer la fonctionnalité **Lots
& Numéros de série**.

Une fois que cette fonctionnalité est activée, une nouvelle option s’affiche
permettant d’activer les **Dates d’expiration**. Cochez cette case pour
activer la fonctionnalité et assurez-vous d”**Enregistrer** les changements.

![Les paramètres lots et numéros de série et dates d'expiration
activés.](../../../../../_images/expiration-dates-enabled-settings.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Une fois que la fonctionnalité <b>Lots &amp; Numéros de série</b> est activée, des fonctionnalités supplémentaires apparaissent permettant d”<b>Afficher des lots et des numéros de série sur les bons de livraison</b> ; d”<b>Afficher des lots et des numéros de série sur les factures</b> et d”<b>Afficher des dates d’expiration sur les bons de livraison</b>. L’activation de ces fonctionnalités contribue à la traçabilité de bout en bout, ce qui facilite la gestion des rappels de produits, l’identification des « mauvais » lots de produits, etc.</p>
</div>

## Configurer des dates d’expiration sur des produits

Une fois que les fonctionnalités **Lots & Numéros de série** et **Dates
d’expiration** ont été activées dans les paramètres de l’application
_Inventaire_ , les informations relatives à l’expiration peuvent être
configurées sur des produits individuels.

Pour ce faire, allez à l’application Inventaire ‣ Produits ‣ Produits, et
sélectionnez un produit à modifier. La sélection d’un produit affiche la fiche
du produit pour cet article en particulier. Sur la fiche du produit, cliquez
sur **Modifier** dans le coin supérieur gauche pour effectuer des changements.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour que les produits soient suivis à l’aide de lots ou de numéros de série ou pour configurer des informations relatives à l’expiration, les produits <em>doivent</em> avoir leur <b>Type de produit</b> défini sur <b>Produit stockable</b> dans l’onglet <b>Informations générales</b>.</p>
</div>

Ensuite, cliquez sur l’onglet **Inventaire** et faites défiler jusqu’à la
section **Traçabilité**. À partir de là, assurez-vous que vous avez coché
**Par numéro de série unique** ou **Par lots**.

Une fois cela fait, une nouvelle case **Date d’expiration** s’affiche qui doit
également être cochée. Lorsque les deux options sont activées, un nouveau
champ **Dates** s’affiche à droite.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un produit est en stock avant d’activer le suivi par lot ou par numéro de série, il peut être nécessaire de procéder à un ajustement d’inventaire afin d’assigner des numéros de lots au stock existant.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour le traitement de grandes quantités de produits lors de réceptions ou de livraisons, il est recommandé d’effectuer un suivi par lot, pour que plusieurs produits puissent être rattachés au même lot, en cas de problème.</p>
</div> ![Configuration des dates d'expiration
sur la fiche du produit.](../../../../../_images/expiration-dates-product-
configuration.png)

Sous le champ **Dates** , il y a quatre catégories d’informations relatives à
l’expiration pour configurer le produit :

  * **Délai d’expiration** : le nombre de jours après la réception des produits (d’un fournisseur ou en stock après la production) au cours desquels les marchandises peuvent devenir dangereuses et ne doivent pas être utilisées ou consommées.

  * **Date limite d’utilisation optimale** : le nombre de jours avant la date d’expiration au cours desquels les marchandises commencent à se détériorer, **sans** nécessairement être déjà dangereuses.

  * **Délai avant retrait** : le nombre de jours avant la date d’expiration au cours desquels les marchandises doivent être retirées du stock.

  * **Délai avant alerte** : le nombre de jours avant la date d’expiration au cours desquels une alerte doit être déclenchée pour les marchandises d’un lot particulier ou contenant un numéro de série particulier.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les valeurs saisies dans ces champs calculent automatiquement la date d’expiration des marchandises entrées dans le stock, qu’elles soient achetées auprès d’un fournisseur ou fabriquées en interne.</p>
</div>

Une fois que toutes les informations relatives à l’expiration ont été
configurées, cliquez sur **Enregistrer** pour enregistrer tous les
changements.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le champ <b>Dates</b> n’est pas renseigné avec des valeurs pour les informations relatives à l’expiration, les dates (et les lots) peuvent être assignées manuellement lors es réceptions et livraisons dans l’entrepôt et hors de l’entrepôt. Même lorsqu’elles sont assignées, elles peuvent toujours être remplacées et modifiées manuellement si nécessaire.</p>
</div>

## Définir des dates d’expiration sur les réceptions avec des lots & numéros
de série

Il est possible de générer des dates d’expiration pour les marchandises
**entrantes** directement à partir du bon de commande. Pour créer un bon de
commande, allez à l’application Achats et cliquez sur **Créer** pour créer une
nouvelle demande de prix.

Complétez ensuite les informations en ajoutant un **Fournisseur** et ajoutez
des produits aux lignes de **Produits** en cliquant sur **Ajouter un
produit**.

Choisissez la quantité souhaitée à commander en changeant le nombre dans la
colonne **Quantité** et cliquez sur **Confirmer la commande**. Cette action
transforme la demande de prix en bon de commande.

Cliquez sur le bouton intelligent **Réception** en haut du bon de commande
pour accéder au formulaire de réception de l’entrepôt.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous cliquez sur <b>Valider</b> avant d’assigner un numéro de série aux quantités de produits commandées, une fenêtre contextuelle <b>Erreur d’utilisateur</b> s’affiche. La fenêtre contextuelle demande de saisir un lot ou un numéro de série pour les produits commandés. La demande de prix ne peut pas être validée sans l’assignation d’un lot ou d’un numéro de série.</p>
<img alt="Fenêtre contextuelle d'erreur d'utilisateur lors de la validation d'une commande sans numéro de lot." class="align-center" src="../../../../../_images/expiration-dates-user-error-popup.png"/>
</div>

À partir de là, cliquez sur l’icône de menu (hamburger) des **Options
supplémentaires** située à l’extrême droite de la ligne de produit. Lorsque
vous cliquez sur cette icône, une fenêtre contextuelle **Opérations
détaillées** s’affiche.

Dans cette fenêtre contextuelle, cliquez sur **Ajouter une ligne** et assignez
un lot ou un numéro de série dans le champ **Nom du lot/numéro de série**.

Une date d’expiration est automatiquement complétée en fonction de la
configuration sur la fiche du produit (si elle a été configurée précédemment).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le champ <b>Dates</b> sur la fiche produit n’a pas été configuré, cette date peut être saisie manuellement.</p>
</div>

Une fois la date d’expiration établie, notez les quantités **faites** et
cliquez sur **Confirmer** pour fermer la fenêtre contextuelle. Enfin, cliquez
sur **Valider**.

![La fenêtre contextuelle des opérations détaillées affichant les dates
d'expiration des produits commandés.](../../../../../_images/expiration-dates-
detailed-operations-popup.png)

Un bouton intelligent **Traçabilité** apparaît lors de la validation de la
réception. Cliquez sur le bouton intelligent **Traçabilité** pour voir le
**Rapport de traçabilité** mis à jour, qui inclut ; un document de
**Référence** ; le **Produit** qui est suivi ; le **Lot/# de série** ; et bien
plus encore.

## Définir des dates d’expiration sur des produits fabriqués

Il est également possible de générer des dates d’expiration pour des produits
fabriqués en interne. Pour assigner des dates d’expiration à des produits
fabriqués, un ordre de fabrication (OF) doit être complété.

Pour créer un OF, allez à l’application Fabrication ‣ Opérations ‣ Ordres de
fabrication et cliquez sur **Créer**. Choisissez un produit à fabriquer dans
le menu déroulant du champ **Produit** , puis sélectionnez la **Quantité** à
produire.

![Ordre de fabrication pour un produit avec date
d'expiration.](../../../../../_images/expiration-dates-manufacturing-
order.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour fabriquer un produit, il faut qu’il y ait des matières premières à consommer dans les lignes de la colonne <b>Produit</b>. Pour ce faire, vous pouvez créer une <b>Nomenclature</b> pour le <b>Produit</b> ou ajouter manuellement des matières premières à consommer en cliquant sur <b>Ajouter une ligne</b>.</p>
</div>

Une fois que tout est prêt, cliquez sur **Confirmer**.

À côté de **Lot/Numéro de série** , sélectionnez un numéro de lot existant
dans le menu déroulant ou cliquez sur le signe **+** vert pour automatiquement
assigner un nouveau numéro de lot.

Ensuite, sélectionnez un nombre d’unités dans le champ **Quantité** et cliquez
sur **Marquer comme terminé**.

Cliquez sur l’icône de **Lien externe** dans le champ **Lot/Numéro de série**
assigné. Une fenêtre contextuelle s’affiche, révélant un formulaire détaillé
pour ce numéro particulier.

Dans cette fenêtre contextuelle, dans l’onglet **Dates** , toutes les
informations relatives à l’expiration précédemment configurées pour le produit
sont affichées. Ces mêmes informations sont également disponibles sur le
formulaire détaillé de ce produit spécifique ou en allant à l’application
Inventaire ‣ Produits ‣ Lots/Numéros de série.

![L'onglet Dates avec des informations relatives à l'expiration d'un numéro de
lot spécifique.](../../../../../_images/expiration-dates-dates-tab-lot-
number.png)

## Vendre des produits avec des dates d’expiration

La vente de produits périssables avec date d’expiration se fait de la même
manière que pour tout autre type de produit. La première étape de la vente de
produits périssables consiste à créer une commande client.

Pour ce faire, allez à l’application Ventes ‣ Créer pour créer un nouveau
devis et compléter les informations sur le formulaire de commande.

Ajoutez un **Client** , cliquez sur **Ajouter un produit** pour ajouter les
produits souhaités aux lignes de **Produit** et définissez une **Quantité**
pour les produits.

Puis cliquez sur l’onglet **Autres informations**. Dans la section
**Livraison** , modifiez la **Date de livraison** à une date après la date
prévue et cliquez sur l’icône de **case à cocher verte** pour confirmer la
date. Cliquez enfin sur **Confirmer** pour confirmer la commande.

Ensuite, cliquez sur le bouton intelligent **Livraison** en haut de la
commande pour accéder au formulaire de réception de l’entrepôt.

Sur le formulaire de réception de l’entrepôt, cliquez sur **Valider** et
**Appliquer** dans la fenêtre contextuelle qui s’affiche, afin de traiter
automatiquement toutes les quantités **faites** et de livrer les produits au
client.

Si les produits sont livrés avant la **Date d’alerte** définie sur la fiche du
produit, aucune alerte ne sera créée.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Une fois que la fonctionnalité <b>Lots &amp; Numéros de série</b> est activée, des fonctionnalités supplémentaires apparaissent permettant d”<b>Afficher des lots et des numéros de série sur les bons de livraison</b> ; d”<b>Afficher des lots et des numéros de série sur les factures</b> et d”<b>Afficher des dates d’expiration sur les bons de livraison</b>. L’activation de ces fonctionnalités contribue à la traçabilité de bout en bout, ce qui facilite la gestion des rappels de produits, l’identification des « mauvais » lots de produits, etc.</p>
</div>0 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Une fois que la fonctionnalité <b>Lots &amp; Numéros de série</b> est activée, des fonctionnalités supplémentaires apparaissent permettant d”<b>Afficher des lots et des numéros de série sur les bons de livraison</b> ; d”<b>Afficher des lots et des numéros de série sur les factures</b> et d”<b>Afficher des dates d’expiration sur les bons de livraison</b>. L’activation de ces fonctionnalités contribue à la traçabilité de bout en bout, ce qui facilite la gestion des rappels de produits, l’identification des « mauvais » lots de produits, etc.</p>
</div>1

## Afficher les dates d’expiration pour les lots & numéros de série

Pour afficher (et/ou regrouper) tous les produits avec des dates d’expiration
par numéro de lot, allez à l’application Inventaire ‣ Produits ‣ Lots/Numéros
de série.

Sur cette page, supprimez tous les filtres de recherche par défaut de la barre
**Recherche…**. Puis cliquez sur **Regrouper par** , choisissez **Ajouter un
groupe personnalisé** et sélectionnez le paramètre **Date d’expiration** dans
le menu déroulant. Enfin, cliquez sur **Appliquer** pour appliquer le filtre.

Cette opération permet de répertorier tous les produits périssables, leur date
d’expiration et le numéro de lot qui leur a été assigné.

![Regrouper par dates d'expiration sur la page des lots et numéros de
série.](../../../../../_images/expiration-dates-group-by-dates.png)

### Alertes d’expiration

Pour voir les alertes d’expiration, allez à l’application Inventaire ‣
Produits ‣ Lots/Numéros de série.

Puis cliquez sur un **Lot/Numéro de série** avec des produits périssables.
Cette action affiche le formulaire détaillé du numéro de série. Sur ce
formulaire, cliquez sur l’onglet **Dates** pour voir toutes les informations
relatives à l’expiration des produits.

Pour modifier le formulaire, cliquez sur **Modifier** dans le coin supérieur
gauche du formulaire, puis modifiez la **Date d’expiration** à la date
d’aujourd’hui (ou à une date antérieure) et cliquez sur **Enregistrer** pour
enregistrer les modifications.

Après l’enregistrement, le formulaire de numéro de lot affiche une **Alerte
d’expiration** rouge en haut du formulaire pour indiquer que les produits de
ce lot sont soit périmés, soit bientôt périmés. À partir de là, retournez à la
page **Lots/Numéros de série** (via le fil d’Ariane).

Pour voir la nouvelle alerte d’expiration ou toutes les alertes d’expiration
pour les produits qui sont périmés (ou qui périment bientôt), supprimez tous
les filtres de recherche dans la barre de **Recherche…** sur le tableau de
bord **Lots/Numéros de série**.

Cliquez ensuite sur **Filtres** et choisissez **Alertes d’expiration**.

![Alerte d'expiration pour un produit qui a dépassé la date
d'expiration.](../../../../../_images/expiration-dates-expiration-alert.png)

  *[OF]: ordre de fabrication

