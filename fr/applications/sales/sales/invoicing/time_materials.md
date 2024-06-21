# Facturation basée sur le temps et les matériaux

La facturation basée sur le temps et/ou les matériaux est généralement
utilisée lorsqu’il n’est pas possible d’estimer avec précision la taille d’un
projet ou lorsque les exigences d’un projet sont susceptibles de changer.

Cela diffère d’un contrat à prix fixe, lorsqu’un client accepte de payer un
montant total spécifié pour l’exécution du contrat—sans tenir compte de ce qui
doit être payé aux employés, aux sous-traitants, aux vendeurs, aux
fournisseurs, etc.

L’application Konvergo ERP _Ventes_ peut facturer le temps et diverses autres dépenses
(par ex. le transport, l’hébergement), ainsi que les achats nécessaires à
l’exécution d’une commande.

## Configuration de l’application et des paramètres

Tout d’abord, afin de suivre avec précision la progression d’un projet, les
applications Konvergo ERP _Projet_ et _Comptabilité_ **doivent** être installées.

Pour installer l’application _Projet_ , allez au tableau de bord principal
d’Konvergo ERP ‣ Apps. Ensuite, sur la page des **Apps** , localisez le bloc de
l’application **Projet** et cliquez sur **Activer**. La page s’actualise
automatiquement et revient au tableau de bord principal d’Konvergo ERP, où il est
désormais possible d’accéder à l’application _Projet_.

Répétez les mêmes étapes pour installer l’application _Comptabilité_.

Après l’installation, cliquez sur l’icône de l’application **Comptabilité**
dans le tableau de bord principal d’Konvergo ERP et allez à Configuration ‣
Paramètres. Sur la page des **Paramètres** , faites défiler jusqu’à la section
**Analytique** et cochez la case à côté de la **Comptabilité analytique**.

![Présentation de l'activation du paramètre Comptabilité analytique sur la
page des paramètres d'Konvergo ERP Comptabilité.](../../../../_images/analytic-
accounting-setting.png)

Cliquez ensuite sur **Enregistrer** pour enregistrer tous les changements.

Allez ensuite au tableau de bord principal d’Konvergo ERP ‣ application Projet ‣
Configuration ‣ Paramètres. Sur la page des **Paramètres** , dans la section
**Gestion du temps** , assurez-vous que la case à côté de la fonctionnalité
**Feuilles de temps** est cochée.

Cliquez ensuite sur **Enregistrer** pour enregistrer tous les changements.

![Présentation de la fonctionnalité Feuilles de temps sur la page des
paramètres d'Konvergo ERP Projet.](../../../../_images/timesheets-feature.png)

## Configuration du produit service

Une fois que la fonctionnalité _Feuilles de temps_ est activée dans
l’application _Projet_ , il est désormais possible de facturer le temps passé
sur un projet, mais **uniquement** lorsque les configurations de produit
suivantes ont été effectuées.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La facturation du temps passé sur un projet n’est possible <a href="#id1"><span class="problematic" id="id2">**</span></a>qu”<a href="#id3"><span class="problematic" id="id4">**</span></a>avec les produits dont le <em>Type de produit</em> est <em>Service</em>.</p>
</div>

Pour configurer un service, allez d’abord l’application Ventes ‣ Produits ‣
Produits. Sur la page des **Produits** , sélectionnez le produit de service
souhaité à configurer ou cliquez sur **Nouveau** pour créer un nouveau
produit.

Dans le formulaire de produit, dans l’onglet **Informations générales** ,
définissez le **Type de produit** sur **Service**. Ouvrez ensuite le menu
déroulant dans le champ **Politique de facturation** et sélectionnez **Basé
sur les feuilles de temps**.

Ensuite, dans le menu déroulant **Créer à la commande** , sélectionnez
**Projet & Tâche**. Ce paramètre indique que, lorsqu’une commande est créée
avec ce produit de service spécifique, un nouveau projet et une nouvelle tâche
sont créés dans l’application _Projet_.

![Les bons paramètres pour les champs Politique de facturation et Créer à la
commande pour le produit de service.](../../../../_images/service-product-
general-settings.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est possible de choisir l’option <b>Tâche</b> au lieu du menu déroulant <b>Créer à la commande</b>. Si vous avez choisi <b>Tâche</b>, sélectionnez un projet existant dans lequel la tâche sera créée dans le champ <b>Projet</b>, qui ne s’affiche que lorsque vous avez choisi <b>Tâche</b> dans le champ <b>Créer à la commande</b>.</p>
</div>

## Ajouter le temps passé à une commande

Après avoir correctement configuré un produit de service avec les options
_Politique de facturation_ et _Créer à la commande_ , il est possible
d’ajouter le temps passé à une commande.

Pour voir cela en action, allez à l’application Ventes ‣ Nouveau pour ouvrir
un formulaire de devis vierge. Ensuite, ajoutez un **Client** et dans l’onglet
**Lignes de commande** , cliquez sur **Ajouter un produit** , et sélectionnez
le produit de service correctement configuré dans le menu déroulant.

Ensuite, cliquez sur **Confirmer** pour confirmer la commande.

Après avoir confirmé la commande, deux boutons intelligents apparaissent en
haut du formulaire de commande : **Projets** et **Tâches**.

![La présentation des boutons intelligents Projets et Tâches sur une commande
dans Konvergo ERP Ventes.](../../../../_images/projects-tasks-smart-buttons.png)

En cliquant sur le bouton intelligent **Projets** , il affiche le projet
spécifique lié à cette commande. En cliquant sur le bouton intelligent
**Tâches** , il affiche la tâche de projet spécifique liée à cette commande.
Les deux sont également accessibles dans l’application _Projet_.

Pour ajouter le temps passé à une commande, cliquez sur le bouton intelligent
**Tâches**.

Dans le formulaire des tâches, sélectionnez l’onglet **Feuilles de temps**.
Dans l’onglet **Feuilles de temps** , les employés peuvent être assignés au
projet et le temps qu’ils passent à travailler sur la tâche peut être ajouté
par les employés ou par la personne qui a créé la commande.

Pour ajouter un employé et le temps passé à travailler sur la tâche, cliquez
sur **Ajouter une ligne** dans l’onglet **Feuilles de temps**. Ensuite,
sélectionnez la bonne **Date** et le bon **Employé**. Vous avez également la
possibilité d’ajouter une brève description du travail effectué pendant cette
période dans la colonne **Description** , mais ce n’est pas obligatoire.

Enfin, saisissez le temps consacré à la tâche dans la colonne **Heures
passées** et cliquez à côté pour terminer cette ligne dans l’onglet **Feuilles
de temps**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le temps saisi dans la colonne <b>Heures passées</b> est immédiatement reflété dans le champ <b>Temps alloué</b> (situé près du haut du formulaire de tâche) sous la forme d’un pourcentage, qui reflète la proportion du total des heures de travail allouées qui ont été effectuées jusqu’à présent.</p>
<p>Ces mêmes informations se retrouvent sous forme d’heures numériques dans les champs <b>Heures passées</b> et <b>Heures restantes</b>, situés en bas de l’onglet <b>Feuilles de temps</b>.</p>
<img alt="La présentation de l'onglet Feuilles de temps sur un formulaire de tâche dans Konvergo ERP Ventes et Konvergo ERP Projet." class="align-center" src="../../../../_images/timesheets-tab-on-task.png"/>
</div>

Répétez ce processus pour le nombre d’employés et d’heures travaillées sur le
projet.

## Facturer le temps passé

Une fois que tous les employés nécessaires et le temps passé ont été ajoutés à
la tâche du projet, retournez à la commande pour facturer ces heures au
client. Pour ce faire, cliquez sur le bouton intelligent **Commande** en haut
du formulaire de la tâche ou retournez à la commande via le fil d’Ariane,
situé en haut à gauche de l’écran.

De retour sur le formulaire de commande, le temps ajouté à la tâche est
reflété dans l’onglet **Lignes de commande** (dans la colonne **Livré**) et
dans le nouveau bouton intelligent **Heures enregistrées** en haut de la
commande.

Pour facturer au client le temps passé sur le projet, cliquez sur **Créer une
facture** , et sélectionnez **Facture normale** dans la fenêtre contextuelle
**Créer les factures**. Cliquez ensuite sur **Créer une facture brouillon**.

Cette opération fait apparaître une **Facture client brouillon** , qui montre
clairement tout le travail effectué dans l’onglet **Lignes de facture**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Faites attention à la colonne <b>Distribution analytique</b> de la <b>Facture client</b>, car ces informations sont nécessaires pour s’assurer que les autres tâches de facturation du temps/du matériel sont effectuées correctement et avec précision.</p>
<img alt="Facture brouillon montrant le temps passé sur la commande dans Konvergo ERP Ventes." class="align-center" src="../../../../_images/invoice-lines-time.png"/>
</div>

Cliquez sur **Confirmer** pour confirmer la facture et poursuivre le processus
de facturation.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="invoicing_policy">Facturation basée sur les quantités livrées ou commandées</a></p>
</div>

## Configuration des notes de frais

Afin de suivre et facturer les dépenses liées à une commande, l’application
Konvergo ERP _Notes de frais_ **doit** être installée.

Pour installer l’application _Notes de frais_ , allez au tableau de bord
principal d’Konvergo ERP ‣ Apps. Ensuite, sur la page des **Apps** , localisez le bloc
de l’application **Notes de frais** et cliquez sur **Activer**.

La page s’actualise automatiquement et revient au tableau de bord principal
d’Konvergo ERP, où il est maintenant possible d’accéder à l’application **Notes de
frais**.

## Ajouter des dépenses à une commande

Pour ajouter une dépense à une commande, allez d’abord à l’application Notes
de frais. Ensuite, dans le tableau de bord principal des _Notes de frais_ ,
cliquez sur **Nouveau** , ce qui fait apparaître un formulaire de notes de
frais vierge.

Sur la note de frais, ajoutez la **Description** de la dépense (par ex.
`Séjour à l'hôtel`, `Billet d'avion`). Ensuite, dans le champ **Catégorie** ,
sélectionnez l’option appropriée dans le menu déroulant (par ex. **Repas** ,
**Kilométrage** , **Voyage & Hébergement**).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez ajouter et modifier les catégories de dépenses en allant à l’application Notes de frais ‣ Configuration ‣ Catégories de dépenses.</p>
</div>

Saisissez ensuite le montant total de la dépense ans le champ **Total** ,
ainsi que les **Taxes comprises** qui s’appliquent éventuellement. Veillez
ensuite à ce que le bon **Employé** soit sélectionné et désignez qui a payé la
dépense dans le champ **Payé par** : l”**Employé (à rembourser)** ou la
**Société**.

Ensuite, dans le champ **Client à refacturer** , sélectionnez la commande
correspondante dans le menu déroulant. Sélectionnez également les informations
de la même commande dans le champ **Distribution analytique**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le champ <b>Distribution analytique</b> proposera <b>uniquement</b> la commande correspondante en tant qu’option si la commande contient un produit de service dont la facturation est basée sur les <em>Feuilles de temps</em>, les <em>Jalons</em> ou la <em>Quantité livrée</em>.</p>
</div> ![Comment correctement remplir une note de frais qui est
liée à une commande dans Konvergo ERP.](../../../../_images/expense-detail-form.png)

Si des reçus doivent être téléchargés et joints à la note de frais, cliquez
sur le bouton **Joindre le reçu** et chargez les documents nécessaires. Cette
opération n’est **pas** obligatoire, mais elle peut avoir une incidence sur
l’approbation de la dépense.

Lorsque toutes les informations ont été saisies, cliquez sur **Créer un
rapport** pour créer une note de frais détaillant toutes les informations qui
viennent d’être saisies.

![La présentation d'un rapport de note de frais dans Konvergo ERP Notes de
frais.](../../../../_images/expense-report-summary1.png)

Ensuite, vous avez la possibilité de la **Soumettre au manager** pour
approbation. Dès qu’elle est approuvée, vous avez la possibilité de la
**Rapporter dans la prochaine fiche de paie**.

Pour présenter un flux complet dans cet exemple, cliquez sur **Soumettre au
manager**. Le manager cliquerait alors sur **Approuver** pour accepter cette
dépense et sur **Enregistrer les pièces comptables** pour enregistrer cette
dépense dans le journal comptable.

## Facturer les dépenses

Pour facturer une dépense sur une commande à un client, allez à la commande
correspondante, à partir de l’application Ventes ou à partir du rapport de
note de frais dans l’application Notes de frais. Depuis le rapport de note de
frais, cliquez sur le bouton intelligent **Bons de commande** en haut de la
page.

Si le rapport de note de frais était lié à la commande, la dépense
nouvellement configurée a maintenant sa propre ligne dans l’onglet **Lignes de
commande** et peut être facturée au client.

![Une dépense apparaissant dans l'onglet Lignes de commande d'une commande
dans l'application Konvergo ERP Ventes.](../../../../_images/invoice-expense-from-
sales-order.png)

Pour facturer la dépense sur le bon de commande au client, cliquez sur **Créer
une facture** , sélectionnez **Facture normale** dans la fenêtre contextuelle
**Créer les factures** et cliquez sur **Créer une facture brouillon**.

Cette opération fait apparaître une **Facture client brouillon** pour la
dépense. Le processus de facturation peut alors se dérouler comme d’habitude.

![Exemple de facture client pour une note de frais générée à partir d'un bon
de commande dans Konvergo ERP Ventes.](../../../../_images/customer-invoice-for-
expense.png)

## Configuration des achats

Pour facturer à un client les achats effectués dans le cadre d’une commande,
l’application _Achats_ **doit** être installée.

Pour installer l’application _Achats_ , allez au tableau de bord principal
d’Konvergo ERP ‣ Apps. Puis, sur la page **Apps** , localisez le bloc de l’application
**Achats** et cliquez sur **Activer**. La page s’actualise automatiquement et
revient au tableau de bord principal d’Konvergo ERP, où il est maintenant possible
d’accéder à l’application **Achats**.

## Ajouter des achats à une commande

Pour ajouter un achat à une commande, vous devez d’abord créer un bon de
commande. Pour créer un bon de commande, allez à l’application Achats ‣
Nouveau pour faire apparaître un bon de commande vierge.

Ajoutez d’abord un **Fournisseur** au bon d’achat. Ensuite, dans l’onglet
**Produits** , cliquez sur le menu déroulant **options de colonne
supplémentaires** , représenté par les deux lignes horizontales avec des
points, situé à l’extrême droite des en-têtes de colonnes. Dans ce menu
déroulant, sélectionnez **Distribution analytique**.

![Comment ajouter une colonne de distribution analytique sur un bon de
commande dans Konvergo ERP Achats.](../../../../_images/extra-column-analytic-
distribution-option.png)

Après avoir ajouté une colonne **Distribution analytique** aux en-têtes de
l’onglet **Produits** du bon de commande, ajoutez le ou les produits au bon de
commande. Pour ce faire, cliquez sur **Ajouter un produit** , et sélectionnez
le produit souhaité dans ce menu déroulant. Répétez les mêmes étapes pour tous
les produits que vous voulez ajouter.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour qu’un achat soit correctement facturé sur une commande, le produit sur le bon de commande <b>doit</b> être marqué en tant que <b>Peut être inséré dans une note de frais</b>, avoir la <b>Politique de facturation</b> définie sur <b>Quantités livrées</b>, et avoir l’option <b>Au prix coûtant</b> sélectionné dans le champ <b>Refacturer les dépenses</b> du formulaire du produit.</p>
<img alt="Paramètres d'un produit d'un bon de commande pour qu'il puisse être facturé sur une commande dans Konvergo ERP." class="align-center" src="../../../../_images/product-form-settings-invoice-purchase.png"/>
</div>

Sélectionnez ensuite la **Distribution analytique** appropriée associée à la
commande à laquelle ce bon de commande est associé. Pour ce faire, cliquez sur
le champ **Distribution analytique** vide pour faire apparaître une fenêtre
contextuelle **Analytique**.

Ensuite, dans le menu déroulant **Départements** , sélectionnez la
distribution analytique associée à la commande souhaitée pour la facturation
de l’achat.

![Comment sélectionner le département de distribution analytique à partir d'un
bon de commande dans Konvergo ERP.](../../../../_images/analytic-drop-down-
distribution.png)

Une fois que toutes les informations sont saisies dans l’onglet **Produits**
du bon de commande, confirmez la commande en cliquant sur **Confirmer la
commande**. Cliquez ensuite sur **Recevoir les produits** lorsque les produits
ont été reçus. Cette opération crée un formulaire de réception.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si des numéro de série/lot doivent être saisis avant de valider la réception des produits, cliquez sur l’icône des <b>détails</b> représentée par quatre lignes horizontales situées à l’extrême droite de la ligne de produit.</p>
<p>Cela fait apparaître un onglet <b>Opérations détaillées</b>, dans lequel vous pouvez ajouter le <b>Lot/Numéro de série</b> et la quantité <b>Faite</b>. Lorsque vous avez terminé, cliquez sur <b>Confirmer</b> pour confirmer les données.</p>
</div>

Cliquez ensuite sur **Valider** pour valider le bon de commande.

Retournez ensuite au bon de commande via le fil d’Ariane en haut de la page et
cliquez sur **Créer une facture** pour créer une facture fournisseur qui peut
être facturée au client sur la commande associée.

![Facture fournisseur brouillon d'un bon de commande à facturer à un client
dans Konvergo ERP.](../../../../_images/vendor-bill-draft.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Veillez à ce qu’une <b>Date de facturation</b> soit indiquée sur la <b>Facture fournisseur brouillon</b> avant de la confirmer. Si <em>aucune</em> <b>Date de facturation</b> n’est fournie, une fenêtre d’erreur s’ouvre et demande de saisir les informations avant la confirmation.</p>
</div>

Cliquez ensuite sur **Confirmer** pour confirmer la facture fournisseur, qui
est ajoutée automatiquement à la commande, où elle peut être facturée
directement au client associé.

## Facturer les achats

Pour facturer les achats sur une commande à un client, ajoutez d’abord le bon
de commande à la commande et allez ensuite à la commande souhaitée dans
l’application Ventes.

Sur la commande associée au bon d’achat, le produit acheté a maintenant sa
propre ligne de produit dans l’onglet **Lignes de commande** , et il est prêt
à être facturé.

![Le produit du bon de commande sur la commande à facturer au client via Konvergo ERP
Ventes.](../../../../_images/purchase-order-on-sales-order.png)

Pour facturer l’achat au client, cliquez simplement sur **Créer une facture**
, sélectionnez **Facture normale** dans la fenêtre contextuelle **Créer les
factures** , puis cliquez sur **Créer une facture brouillon**.

Cette opération fait apparaître une **Facture client brouillon** avec le
produit de bon de commande nouvellement ajouté dans l’onglet **Lignes de
facture**.

![Facture client brouillon avec un produit d'achat sur la commande dans
Konvergo ERP.](../../../../_images/draft-invoice-with-purchase-product.png)

Pour compléter le processus de facturation, cliquez sur **Confirmer** pour
confirmer la facture et cliquez sur **Enregistrer un paiement** dans le
formulaire contextuel **Enregistrer un paiement**.

