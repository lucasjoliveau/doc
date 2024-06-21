# Gérer des factures fournisseurs

Une _facture fournisseur_ est une facture reçue pour des produits et/ou des
services qu’une entreprise achète auprès d’un fournisseur. Les factures
fournisseurs enregistrent les dettes au fur et à mesure qu’elles arrivent des
fournisseurs et peuvent inclure des montants dus pour les biens et/ou les
services achetés, les taxes à la vente, les frais de transport et de
livraison, et plus encore.

Dans Konvergo ERP, une facture fournisseur peut être créée à différents moments du
processus d’achat, en fonction de la politique de _contrôle des factures_
choisie dans les paramètres de l’application _Achats_.

## Politiques de contrôle des factures

Pour voir et modifier la politique de contrôle des factures par défaut, allez
à l’application Achats ‣ Configuration ‣ Paramètres et faites défiler jusqu’à
la section **Facturation**.

Il y a deux options de politique de **Contrôle des factures** : **Quantités
commandées** et **Quantités reçues**. Après avoir sélectionné une politique,
cliquez sur **Enregistrer** pour enregistrer les changements.

![Politiques de contrôle des factures dans les paramètres de l'application
Achats.](../../../../_images/manage-configuration-settings.png)

La politique sélectionnée sera la politique par défaut pour chaque nouveau
produit créé. Les politiques sont définies comme suit :

  * **Quantités commandées** : crée une facture fournisseur dès qu’un bon de commande est confirmé. Les produits et les quantités du bon de commande sont utilisés pour générer une facture brouillon.

  * **Quantités reçues** : la facture n’est créée qu”**après** qu’une partie de la commande totale a été reçue. Les produits et les quantités **reçus** sont utilisés pour générer une facture brouillon.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si un produit a besoin d’une politique de contrôle différente, la politique de contrôle des factures par défaut peut être remplacée en allant à l’onglet <b>Achats</b> dans un modèle de produit et en modifiant le champ <b>Politique de contrôle</b>.</p>
</div> ![Champ de politique de contrôle sur un formulaire de
produit.](../../../../_images/manage-product-form.png)

### Correspondance à trois voies

La _correspondance à trois voies_ garantit que les factures fournisseurs ne
sont payées qu’après avoir reçu une partie ou la totalité des produits du bon
de commande.

Pour l’activer, allez à l’application Achats ‣ Configuration ‣ Paramètres et
faites défiler jusqu’à la section **Facturation**. Cochez ensuite la case à
côté de **Correspondance à trois voies : achats, réceptions et factures** et
cliquez sur **Enregistrer** pour enregistrer les changements.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La <b>correspondance à trois voies</b> fonctionnera <b>uniquement</b> lorsque la politique de <b>Contrôle des factures</b> est définie sur <b>Quantités reçues</b>.</p>
<img alt="Fonctionnalité de correspondance à trois voies activée dans les paramètres de l'application Achats." class="align-center" src="../../../../_images/manage-three-way-matching.png"/>
</div>

## Créer et gérer des factures fournisseurs sur les réceptions

Lorsque des produits sont reçus dans l’entrepôt d’une entreprise, des
réceptions sont créées. Une fois que l’entreprise traite les quantités reçues,
elle peut choisir de créer une facture fournisseur directement depuis la
réception de l’entrepôt. En fonction de la politique de contrôle des factures
sélectionnée dans les paramètres, la création de la facture fournisseur
s’effectue à différentes étapes du processus d’approvisionnement.

### Lorsque la politique de contrôle des factures est définie sur quantités
commandées

Pour créer et gérer des factures fournisseurs sur les réceptions en utilisant
la politique de contrôle des factures _quantités commandées_ , allez d’abord à
l’application Achats ‣ Configuration ‣ Paramètres, faites défiler jusqu’à la
section **Facturation** et définissez **Contrôle des factures** sur
**Quantités commandées**. Cliquez ensuite sur **Enregistrer** pour enregistrer
les changements.

Allez ensuite à l’application Achats et cliquez sur **Créer** pour créer une
nouvelle demande de prix. Cette action fait apparaître un formulaire détaillé
de demande de prix vierge.

Sur le formulaire détaillé vierge, ajoutez un fournisseur à la demande de prix
dans le champ **Fournisseur** et ajoutez des produits aux lignes de
**Produit** en cliquant sur **Ajouter une ligne**.

Confirmez ensuite la demande de prix en cliquant sur le bouton **Conformer la
commande** en haut du formulaire. La demande de prix est alors transformée en
bon de commande.

Cliquez ensuite sur le bouton **Créer une facture fournisseur** pour créer une
facture fournisseur pour le bon de commande.

Le fait de cliquer sur le bouton **Créer une facture fournisseur** révèle la
page **Facture brouillon** pour le bon de commande.

Sur la **Facture brouillon** , cliquez sur le bouton **Modifier** pour
modifier la facture et ajoutez une date de facturation dans le champ **Date de
facturation**. le cas échéant, ajoutez des produits supplémentaires aux lignes
de **Produit** en cliquant sur **Ajouter une ligne** l’onglet **Lignes de
facture**.

Ensuite, confirmez la facture en cliquant sur le bouton **Confirmer** sur la
page **Facture brouillon**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Puisque la politique de contrôle des factures est définie sur <em>quantités commandées</em>, la facture brouillon peut être confirmée dès qu’elle est créée, avant la réception des produits.</p>
</div>

Sur la nouvelle **facture fournisseur** , ajoutez un numéro de **Référence de
la facture** , qui peut être utilisé pour faire correspondre la facture avec
d’autres documents (tels que le bon de commande). Puis cliquez sur Confirmer ‣
Enregistrer un paiement. Une fenêtre contextuelle apparaît, dans laquelle vous
pouvez choisir un **Journal** de paiement ; un **Mode de paiement** et un
**Compte bancaire destinataire** dans un menu déroulant.

De plus, vous pouvez modifier le **Montant** de la facture, la **Date de
paiement** et le **Mémo** (Numéro de référence) dans cette fenêtre
contextuelle. Une fois que vous avez fini, cliquez sur **Créer un paiement**
pour finaliser la création de la **Facture fournisseur**. Une bannière verte
**En paiement** s’affiche sur la demande de prix.

![Formulaire de facture fournisseur pour la politique de contrôle des
quantités commandées.](../../../../_images/manage-draft-vendor-bill.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Chaque facture fournisseur offre la possibilité d”<b>Ajouter un avoir</b> ou d”<b>Ajouter une note de débit</b>. Un <em>avoir</em> est généralement émis lorsqu’un vendeur ou un fournisseur récupère une certaine quantité de produits auprès du client auquel ils ont été vendus, alors que les <em>notes de débit</em> sont réservées aux marchandises retournées par le client/l’acheteur au vendeur ou fournisseur.</p>
</div>

### Lorsque la politique de contrôle des factures est définie sur quantités
reçues

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous tentez de créer une facture fournisseur sans avoir reçu les produits (alors que vous utilisez la politique de contrôle de factures <em>quantités reçues</em>), un message d’erreur s’affiche et les paramètres doivent être modifiés avant de poursuivre.</p>
</div>

Pour créer et gérer des factures fournisseurs sur des réceptions en utilisant
la politique de contrôle des factures _quantités reçues_ , allez d’abord à
l’application Achats ‣ Configuration ‣ Paramètres, faites défiler jusqu’à la
section **Facturation** et définissez le **Contrôle des factures** sur
**Quantités reçues**. Cliquez ensuite sur **Enregistrer** pour enregistrer les
changements.

Ensuite, allez à l’application Achats et cliquez sur **Créer** pour créer une
nouvelle demande de prix. Un formulaire détaillé de demande de prix vierge
s’affiche.

Sur le formulaire détaillé vierge, ajoutez un fournisseur à la demande de prix
dans le champ **Fournisseur** et ajoutez des produits aux lignes de
**Produit** en cliquant sur **Ajouter une ligne**.

Confirmez ensuite la demande de prix en cliquant sur le bouton **Conformer la
commande** en haut du formulaire. La demande de prix est alors transformée en
bon de commande.

Enfin, cliquez sur le bouton **Créer une facture fournisseur** pour créer une
facture fournisseur pour le bon de commande.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le fait de cliquer sur <b>Créer une facture fournisseur</b> avant d’avoir reçu des produits fera apparaître une fenêtre contextuelle d”<b>Erreur d’utilisateur</b>. Le <b>Bon de commande</b> requiert qu’au moins une partie des articles qui figurent sur le bon de commande soit livrée avant de créer une facture fournisseur.</p>
</div> ![Fenêtre contextuelle d'erreur d'utilisateur pour la
politique de contrôle des quantités reçues.](../../../../_images/manage-user-
error-popup.png)

Ensuite, cliquez sur le bouton intelligent **Réception** pour afficher le
formulaire de réception de l’entrepôt.

Sur le formulaire de réception de l’entrepôt, cliquez sur Valider ‣ Appliquer
pour indiquer les quantités **faites**. Retournez ensuite au Bon de commande
(via le fil d’Ariane) et cliquez sur le bouton **Créer une facture
fournisseur** sur le formulaire du bon de commande.

Cette opération fait apparaître une **Facture brouillon** pour le bon de
commande. Sur la **Facture brouillon** , cliquez sur le bouton **Modifier** et
ajoutez une **Date de facturation**. Le cas échéant, ajoutez des produits
supplémentaires aux lignes de **Produit** en cliquant sur **Ajouter une
ligne**.

Ensuite, cliquez sur le bouton **Confirmer** pour confirmer la **Facture
brouillon**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Puisque la politique de contrôle des factures est définie sur <em>quantités reçues</em>, la facture brouillon peut <b>uniquement</b> être confirmée lorsqu’au moins certaines quantités sont reçues.</p>
</div>

Sur la nouvelle **facture fournisseur** , ajoutez un numéro de **Référence de
la facture** , qui peut être utilisé pour faire correspondre la facture avec
d’autres documents (tels que le bon de commande). Puis cliquez sur Confirmer ‣
Enregistrer un paiement. Une fenêtre contextuelle apparaît, dans laquelle vous
pouvez choisir un **Journal** de paiement ; un **Mode de paiement** et un
**Compte bancaire destinataire** dans un menu déroulant.

De plus, vous pouvez modifier le **Montant** de la facture, la **Date de
paiement** et le **Mémo** (Numéro de référence) dans cette fenêtre
contextuelle. Une fois que vous avez fini, cliquez sur **Créer un paiement**
pour finaliser la création de la facture fournisseur. Une bannière verte **En
paiement** s’affiche sur la demande de prix.

## Créer et gérer des factures fournisseurs dans Comptabilité

Vous pouvez également créer des factures fournisseurs directement à partir de
l’application _Comptabilité_ , **sans** devoir créer un bon de commande
auparavant. Pour ce faire, allez à l’application Comptabilité ‣ Fournisseurs ‣
Factures fournisseurs et cliquez sur **Créer**. Un formulaire détaillé de
facture fournisseur vierge s’affiche.

Sur le formulaire détaillé de facture fournisseur vierge, ajoutez un
fournisseur dans le champ **Fournisseur** et ajoutez des produits aux lignes
de **Produit** (dans l’onglet **Lignes de facture**) en cliquant sur **Ajouter
une ligne**. Ensuite, ajoutez une date de facturation dans le champ **Date de
facturation** et toute autre information nécessaire. Cliquez enfin sur
**Confirmer** pour confirmer la facture fournisseur.

À partir de là, cliquez sur l’onglet **Écritures comptables** pour voir (ou
modifier) les journaux de **Compte** qui ont été complétés en fonction de la
configuration des formulaires **Fournisseur** et **Produit** correspondants.

Cliquez ensuite sur **Ajouter un avoir** ou **Ajouter une note de débit** pour
avoir un avoir ou une note de débit à la facture. Ou alors, ajoutez un numéro
de **Référence de facture** (en mode **Édition**).

Une fois que vous avez terminé, cliquez sur Enregistrer un paiement ‣ Créer un
paiement pour finaliser la **Facture fournisseur**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour associer la facture fournisseur à un bon de commande existant, cliquez sur le menu déroulant à côté de <b>Saisie automatique</b> et sélectionnez un bon de commande dans le menu. Les informations du bon de commande seront automatiquement complétées dans la facture fournisseur.</p>
<img alt="Liste déroulante de saisie automatique sur une facture fournisseur brouillon." class="align-center" src="../../../../_images/manage-auto-complete.png"/>
</div>

## Facturation par lot

Les factures fournisseurs peuvent être traitées et gérées par lots dans
l’application _Comptabilité_.

Pour ce faire, allez à l’application Comptabilité ‣ Fournisseurs ‣ Factures
fournisseurs. Puis cochez la **case** dans le coin supérieur gauche de la
page, à côté de la colonne **Numéro** , sous le bouton **Créer**. Cette action
permet de sélectionner toutes les factures fournisseurs dont le **Statut** est
**Comptabilisé** ou **Brouillon**.

À partir de là, cliquez sur l’icône d’engrenage **Action** pour exporter,
supprimer ou envoyer & imprimer les factures ; cliquez sur l’icône
**Imprimer** pour imprimer les factures clients ou fournisseurs ; ou cliquez
sur **Enregistrer un paiement** pour créer et traiter le paiement de plusieurs
factures fournisseurs en une fois.

Lorsque vous sélectionnez **Enregistrer un paiement** , une fenêtre
contextuelle s’affiche. Dans cette fenêtre contextuelle, sélectionnez le
journal approprié dans le champ **Journal** , choisissez une date de paiement
dans le champ **Date de paiement** et choisissez un **Mode de paiement**. Vous
avez également la possibilité de **Regrouper des paiements** dans cette
fenêtre contextuelle.

Lorsque vous avez terminé, cliquez sur le bouton **Créer un paiement** , ce
qui crée une liste de pièces comptables dans une page séparée. Ces pièces
comptables sont toutes associées à leurs factures fournisseurs appropriées.

![Fenêtre contextuelle d'enregistrer un paiement pour une facturation par
lot.](../../../../_images/manage-batch-billing.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’option <b>Enregistrer un paiement</b> pour les factures fournisseurs par lot fonctionne uniquement pour les pièces comptables dont le <b>Statut</b> est défini sur <b>Comptabilisé</b>.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="control_bills">Politiques de contrôle des factures</a></p>
</div>

