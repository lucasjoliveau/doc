# Utiliser des contrats-cadres pour créer des conventions d’achat avec des
fournisseurs

Les contrats-cadres sont des conventions d’achat à long terme entre une
société et un fournisseur pour livrer des produits sur base régulière à un
prix prédéterminé. Les contrats-cadres sont utiles lorsque les produits sont
toujours achetés auprès du même fournisseur, mais dans des quantités
différentes et à des moments différents.

En simplifiant le processus de commande, les contrats-cadres permettent non
seulement de gagner du temps, mais aussi de l’argent, puisqu’ils peuvent être
avantageux lors de la négociation de prix de gros avec les fournisseurs.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="calls_for_tenders">Créer des demandes de prix alternatives pour plusieurs fournisseurs</a></p>
</div>

## Créer un nouveau contrat-cadre

Pour créer des contrats-cadres, vous devez d’abord activer la fonctionnalité
_Conventions d’achat_ dans les paramètres de l’application _Achats_. Pour ce
faire, allez à Achats ‣ Configuration ‣ Paramètres et dans la section
**Commandes** , cochez la case à côté de **Conventions d’achat**. Vous pourrez
ainsi créer des contrats-cadres et des demandes de prix alternatives.

![La fonctionnalité Conventions d'achat activée dans les paramètres de
l'application Achats.](../../../../_images/blanket-orders-settings-page.png)

Pour créer un contrat-cadre, allez à Achats ‣ Commandes ‣ Contrats-cadres et
cliquez sur **Nouveau**. Cela permet d’accéder à un formulaire de contrat-
cadre vierge.

À partir de ce nouveau formulaire de contrat-cadre, il est possible de
configurer plusieurs champs et paramètres, de manière à ce qu’il y ait des
règles prédéterminées que la convention récurrente à long terme doit respecter
:

  * **Responsable des achats** : il s’agit de l’utilisateur assigné à ce contrat-cadre en particulier. Par défaut, il s’agit de l’utilisateur qui a créé la convention ; il est possible de modifier l’utilisateur directement dans le menu déroulant à côté de ce champ.

  * **Type de convention** : il s’agit du type de convention d’achat dans laquelle ce contrat-cadre est classé. Dans Konvergo ERP, les contrats-cadres sont les seules conventions d’achat officielles.

  * **Fournisseur** : il s’agit du fournisseur auquel cette convention est liée, soit une fois, soit de manière récurrente. Le fournisseur peut être sélectionné directement dans le menu déroulant à côté de ce champ.

  * **Devise** : il s’agit de la devise convenue qui sera utilisée pour cet échange. Si plusieurs devises ont été activées dans la base de données, la devise peut être modifiée dans le menu déroulant à côté de ce champ.

  * **Date limite de la convention** : il s’agit de la date à laquelle cette convention d’achat doit expirer (si vous le souhaitez). Si ce contrat-cadre ne doit pas prendre fin, laissez ce champ vide.

  * **Date de commande** : il s’agit de la date du contrat-cadre si un nouveau devis est créé directement à partir du formulaire de contrat-cadre. Si un nouveau devis est créé, cette valeur sera automatiquement complétée dans le champ _Échéance de commande_ sur la demande de prix.

  * **Date de livraison** : il s’agit de la date de livraison prévue pour les produits figurant sur une demande de prix directement créée à partir du formulaire de contrat-cadre. Si un nouveau devis est créé, cette valeur sera automatiquement complétée dans le champ _Arrivée prévue_ de la demande de prix.

  * **Document d’origine** : il s’agit du bon de commande d’origine auquel ce contrat-cadre sera lié. Si ce contrat-cadre ne doit être lié à aucun bon de commande existant, laissez ce champ vide.

  * **Société** : il s’agit de la société assignée à ce contrat-cadre spécifique. Par défaut, il s’agit de la société sous laquelle est répertorié l’utilisateur qui a créé le contrat-cadre. Si la date de données n’est pas une base de données multi-sociétés, ce champ ne peut pas être modifié et sera complété par défaut par la seule société répertoriée dans la base de données.

![Nouvelle convention d'achat de contrat-cadre avec ajout de
produits.](../../../../_images/blanket-orders-new-agreement.png)

Une fois que tous les champs pertinents ont été complétés, cliquez sur
**Ajouter une ligne** pour ajouter des produits dans la colonne **Produit**.
Modifiez ensuite la quantité de chaque produit dans la colonne **Quantité**
(si vous le souhaitez) et définissez un prix dans la colonne **Prix
unitaire**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Lors de l’ajout de produits à un nouveau contrat-cadre, les prix préexistants des produits ne seront pas ajoutés automatiquement aux lignes de produits. Les prix doivent être assignés manuellement en modifiant la valeur dans la colonne <b>Prix unitaire</b> pour qu’elle corresponde à un prix convenu avec le fournisseur sélectionné. Sinon, le prix restera <b>0</b>.</p>
</div>

Pour afficher et modifier les paramètres par défaut des contrats-cadres
directement à partir du formulaire du contrat-cadre, cliquez sur le **lien
interne (icône de flèche)** à côté du champ **Type de convention** où est
complété **Contrat-cadre**. Vous accéderez ainsi aux paramètres du contrat-
cadre.

De là, vous pouvez modifier les paramètres des contrats-cadres. Dans la
section **Type de convention** , le nom du **Type de convention** peut être
modifié (si vous le souhaitez), ainsi que le **Type de sélection de la
convention**. Deux options peuvent être activées pour le type de sélection :

  * **Sélectionner une seule demande de prix (exclusif)** : lorsqu’un bon de commande est confirmé, les autres bons de commande seront annulés.

  * **Sélectionner plusieurs demandes de prix (non exclusif)** : lorsqu’un bon de commande est confirmé, les autres bons de commande ne seront **pas** annulés. En revanche, il est autorisé d’avoir plusieurs bons de commande.

Dans la section **Données pour nouveaux devis** , les paramètres relatifs à la
manière dont les lignes de produits et les quantités seront renseignées sur
les nouveaux devis utilisant cette convention d’achat peuvent être modifiés à
côté des champs **Lignes** et **Quantités**.

![Page de modification du type de convention d'achat pour les contrats-
cadres.](../../../../_images/blanket-orders-edit-agreement-type.png)

Deux options peuvent être activées pour les **Lignes** :

  * **Utiliser les lignes de la convention** : lors de la création d’un nouveau devis, les lignes de produits seront précomplétées avec les mêmes produits que ceux du contrat-cadre, si ce dernier est sélectionné dans le nouveau devis.

  * **Ne pas créer des lignes de demande de prix automatiquement** : lors de la création d’un nouveau devis et la sélection d’un contrat-cadre existant, les paramètres seront repris dans le nouveau devis, mais les lignes de produits ne seront pas complétées.

Deux options peuvent être activées pour les **Quantités** :

  * **Utiliser les quantités de la convention** : lors de la création d’un nouveau devis, les quantités de produit répertoriées sur le contrat-cadre seront précomplétées dans les lignes de produits, si ce contrat-cadre est sélectionné sur le nouveau devis.

  * **Définir les quantités manuellement** : lors de la création d’un nouveau devis et la sélection d’un contrat-cadre existant, les lignes de produits seront précomplétées, mais toutes les quantités seront mises à **0**. Les quantités devront être définies manuellement par l’utilisateur.

Une fois que les modifications souhaitées ont été effectuées (le cas échéant),
cliquez sur **Nouveau** (via le fil d’Ariane en haut de la page) pour revenir
au formulaire de contrat-cadre et cliquez sur **Confirmer** pour enregistrer
cette nouvelle convention d’achat. Une fois confirmé, le contrat-cadre passe
de _Brouillon_ à _En cours_ , ce qui signifie que cette convention peut être
sélectionnée et utilisée lors de la création de nouvelles demandes de prix.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Après la création et la confirmation d’un contrat-cadre, il est toujours possible d’modifier, d’ajouter et de supprimer des produits, quantités et prix de la convention d’achat.</p>
</div>

## Créer une nouvelle demande de prix à partir du contrat-cadre

Après avoir confirmé un contrat-cadre, de nouveaux devis peuvent être créés
directement à partir du formulaire de contrat-cadre qui utilisera les règles
définies sur le formulaire et complétera le nouveau devis avec les
informations correctes. De plus, ce nouveau devis sera automatiquement lié à
ce formulaire de contrat-cadre via le bouton intelligent **Demandes de
prix/Commandes** en haut à droite du formulaire.

Pour créer un nouveau devis à partir du formulaire de contrat-cadre, cliquez
sur **Nouveau devis**. Ceci permet d’accéder à une nouvelle demande de prix
vierge, qui est précomplété avec les informations correctes, en fonction des
paramètres configurés sur le formulaire de contrat-cadre.

À partir du nouveau formulaire de demande de prix, cliquez sur **Envoyer par
email** pour écrire et envoyer un email au fournisseur répertorié ; cliquez
sur **Imprimer la demande de prix** pour générer un PDF imprimable du devis ;
ou, une fois prêt, cliquez sur **Confirmer la commande** pour confirmer le bon
de commande.

![Nouveau devis avec des produits et des règles copiés du contrat-
cadre.](../../../../_images/blanket-orders-new-quotation.png)

Une fois que le bon de commande a été confirmé, revenez au formulaire de
contrat-cadre (via le fil d’Ariane en haut de la page). Sur le formulaire de
contrat-cadre figure désormais une demande de prix dans le bouton intelligent
**Demandes de prix/Commandes** en haut à droite du formulaire. Cliquez sur le
bouton intelligent **Demandes de prix/Commandes** pour voir le bon de commande
qui vient d’être créé.

![Bouton intelligent des demandes de prix et commandes sur un formulaire de
contrat-cadre.](../../../../_images/blanket-orders-rfq-smart-button.png)

## Créer un nouveau contrat-cadre à partir d’une demande de prix

Pour créer une nouvelle demande de prix, allez à l’application Achats et
cliquez sur **Nouveau**.

Ajoutez ensuite les informations au formulaire de demande de prix : ajoutez un
fournisseur dans le menu déroulant à côté du champ **Fournisseur** et cliquez
sur **Ajouter un produit** pour sélectionner un produit dans le menu déroulant
dans la colonne **Produit**. Ensuite, définissez la quantité que vous voulez
acheter dans la colonne **Quantité** et modifiez le prix d’achat dans la
colonne **Prix unitaire** , si vous le souhaitez.

En cliquant sur l’icône des **options supplémentaires (deux points)** , des
options de visibilité supplémentaires peuvent être ajoutées à la ligne.
Répétez ces étapes pour ajouter autant d’options supplémentaires que vous le
souhaitez, y compris l”**UdM** (Unité de mesure) dans laquelle vous achetez
les produits et la date d”**Arrivée prévue**.

Avant de confirmer le nouveau devis et de créer un bon de commande, cliquez
sur le menu déroulant à côté du champ **Contrat-cadre** et saisissez un
nouveau nom pour le nouveau contrat-cadre. Ceci permet de créer une toute
nouvelle convention d’achat et de enregistrer les informations saisies dans
les champs du formulaire de bon de commande, ainsi que les informations sur le
produit saisies dans les lignes de produits.

À partir du nouveau formulaire de demande de prix, cliquez sur **Envoyer par
email** pour écrire et envoyer un email au fournisseur répertorié ; cliquez
sur **Imprimer la demande de prix** pour générer un PDF imprimable du devis ;
ou, une fois prêt, cliquez sur **Confirmer la commande** pour confirmer le bon
de commande.

![Nouveau contrat-cadre créé directement à partir du
devis.](../../../../_images/blanket-orders-new-blanket-order.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour voir le contrat-cadre nouvellement créé, allez à Commandes ‣ Contrats-cadres et cliquez sur le nouveau contrat-cadre. De là, vous pouvez modifier les paramètres et les règles si vous le souhaitez.</p>
</div>

## Contrats-cadres et réassort

Une fois qu’un contrat-cadre est confirmé, une nouvelle ligne fournisseur est
ajoutée à l’onglet **Achat** des produits figurant sur le contrat-cadre. Cela
rend les contrats-cadres particulièrement utiles pour le [réassort
automatisé](../products/reordering), car les informations relatives au
**fournisseur** , au **prix** et à la **Convention** sont reprises dans la
ligne fournisseur. Ces informations sont utilisées pour déterminer où, quand
et à quel prix ce produit peut être réapprovisionné.

![Fiche de produit avec l'accord de réassort lié au contrat-
cadre.](../../../../_images/blanket-orders-automated-replenishment.png)

