# Suivi et facturation du temps

Konvergo ERP _Assistance_ permet aux équipes de suivre le nombre d’heures qu’elles
passent sur un ticket et de facturer ce temps à un client. Grâce aux
intégrations avec les applications _Ventes_ , _Feuilles de temps_ et
_Comptabilité_ , les clients peuvent être facturés une fois le travail terminé
ou même avant d’entamer le travail.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Puisque la fonctionnalité <em>Suivi &amp; Facturation du temps</em> requiert l’intégration avec d’autres applications, leur activation peut entraîner l’installation de modules (ou applications) supplémentaires.</p>
<p>L’installation d’une nouvelle application sur une base de données <em>Une App Gratuite</em> déclenche une période d’essai de 15 jours. À la fin de la période d’essai, si aucun abonnement payant n’est ajouté à la base de données, elle ne sera plus active ou accessible.</p>
</div>

## Configurer les fonctionnalités Suivi & Facturation du temps

Avant qu’un client puisse être facturé pour les services d’assistance, il
convient d’activer les fonctionnalités _Suivi & Facturation du temps_. Ces
fonctionnalités doivent être activées sur chaque équipe d” _assistance_ où
elles seront utilisées.

### Activer le suivi et la facturation du temps sur une équipe d’assistance

Pour afficher et activer les fonctionnalités **Suivi & Facturation du temps**
sur une équipe d” _Assistance_ , allez d’abord à Assistance ‣ Configuration ‣
Équipes. Sélectionnez ensuite une équipe dans la liste ou [créez-en une
nouvelle](../overview/getting_started). La page des paramètres de
l’équipe s’affiche.

Sur la page des paramètres de l’équipe, faites défiler jusqu’à la section
**Suivi & Facturation du temps**. Cochez les cases intitulées **Feuilles de
temps** et **Facturation du temps**.

Une fois que la case **Feuilles de temps** est cochée, un nouveau champ
apparaît, intitulé **Projet**.

Le projet sélectionné dans ce champ est l’endroit où toutes les feuilles de
temps pour les tickets de cette équipe seront enregistrées. Cliquez sur le
menu déroulant pour sélectionner un **Projet**.

Pour créer un nouveau projet dans lequel les feuilles de temps seront
enregistrées, cliquez sur le menu déroulant, tapez un nom pour le projet, puis
cliquez sur **Créer**.

![Vue d'une page de paramètres d'une équipe d'assistance mettant l'accent sur
les paramètres de suivi et de facturation du
temps.](../../../../_images/track-bill-enable-settings.png)

### Configurer des produits de service

Lorsque la fonctionnalité **Facturation du temps** est activée, un nouveau
produit est créé dans l’application _Ventes_ , intitulé **Services sur
Feuilles de temps**. Ce produit peut être trouvé via Ventes ‣ Produits ‣
Produits. Recherchez `Services sur Feuilles de temps` dans la barre de
**Recherche…**. C’est le produit qui sera utilisé pour facturer les _services
d’assistance post-payés_ une fois qu’ils ont été effectués.

Sélectionnez **Services sur Feuilles de temps** sur la page du produit. Le
formulaire détaillé du produit s’affiche. Le produit est configuré avec le
**Type de produit** sur **Service** et la **Politique de facturation** sur
**Basé sur les feuilles de temps**.

![Vue d'un produit de service dont la politique de facturation est définie sur
'Basé sur les feuilles de temps'.](../../../../_images/track-bill-product-
based-on-timesheets.png)

Afin de facturer des services d’assistance avant que le travail n’ait été
effectué (également connus sous le nom de _services d’assistance prépayés_),
il faut créer un produit séparé avec une politique de facturation distincte.

Pour créer un nouveau produit de service, allez à Ventes ‣ Produits ‣ Produits
et cliquez sur **Nouveau**. Un formulaire détaillé de produit vierge
s’affiche.

Sur le formulaire du nouveau produit, ajoutez un **Nom du produit** et
définissez le **Type de produit** sur **Service**. Ensuite, définissez la
**Politique de facturation** sur **Prépayé/Prix fixe**. Ceci signifie qu’une
facture peut être générée et que le paiement peut être reçu pour ce produit
avant qu’aucune entrée de feuilles de temps n’ait été enregistrée pour ces
services.

![Vue d'un produit de service dont la politique de facturation est définie sur
'Prépayé/Prix fixe'.](../../../../_images/track-bill-product-prepaid-
fixed.png)

Enfin, définissez le **Prix de vente** et confirmez que l”**Unité de mesure**
est définie sur **Heures**.

## Facturer des services d’assistance prépayés

Lorsque les services d’assistance sont facturés sur la base d’un prix fixe,
une facture peut être créée avant que le travail ne soit achevé. Dans ce cas,
un produit de service dont la politique de facturation est définie sur
**Prépayé/Prix fixe** sera utilisé, comme dans la section ci-dessus.

### Créer une commande avec un produit prépayé

Pour facturer à un client des services d’assistance prépayés, créez d’abord un
bon de commande avec le produit de services d’assistance. Pour ce faire, allez
à Ventes ‣ Commandes ‣ Devis ‣ Nouveau, ce qui fait apparaître un formulaire
de devis vierge.

Ensuite, complétez le formulaire de devis avec les informations relatives au
client.

Allez à l’onglet **Lignes de la commande** du devis et cliquez sur **Ajouter
un produit**. Sélectionnez ensuite le _produit de services prépayés_ configuré
dans les étapes ci-dessus. Mettez à jour le champ **Quantité** avec le nombre
d’heures.

Après avoir mis à jour toutes les autres informations nécessaires,
**confirmez** le devis. Cette opération convertit le devis en une commande.

### Créer et envoyer un facture pour des services prépayés

Une fois la commande confirmée, cliquez sur le bouton **Créer une facture**.
Cette action fait apparaître une fenêtre contextuelle **Créer les factures**.

Si aucun acompte n’est perçu, l’option **Créer une facture** peut rester sur
**Facture normale**. Si un acompte doit être perçu, choisissez entre **Acompte
(pourcentage)** ou **Acompte (montant fixe)**.

Lorsque les informations nécessaires ont été saisies, cliquez sur **Créer une
facture brouillon**.

La facture peut ensuite être envoyée au client pour paiement.

### Créer un ticket d’assistance pour des services prépayés

Pour créer un ticket d” _Assistance_ pour des services prépayés, allez à
Assistance et cliquez sur le bouton **Tickets** pour afficher le pipeline
d’une équipe spécifique. Cliquez sur **Nouveau** pour créer un nouveau ticket.

Sur le formulaire de ticket vierge, donnez un **Titre** au ticket et saisissez
les informations relatives au **Client**.

Après avoir ajouté le nom du client, le champ **Article du bon de commande**
se remplit automatiquement avec l’article du bon de commande prépayé le plus
récent qui a du temps restant.

### Suivre les heures sur un ticket d’assistance

Le temps passé à travailler sur un ticket d” _Assistance_ est suivi dans
l’onglet _Feuilles de temps_ du ticket en question.

Sur le formulaire détaillé du ticket, cliquez sur l’onglet **Feuilles de
temps** et cliquez sur **Ajouter un ligne**. Choisissez un **Employé** ,
ajoutez une **Description** de la tâche et saisissez le nombre d”**Heures
passées**.

Au fur et à mesure que de nouvelles lignes sont ajoutées dans l’onglet
**Feuilles de temps** , le champ **Heures restantes sur le bon de commande**
est automatiquement mis à jour.

![Vue de l'onglet Feuilles de temps d'un ticket avec un accent sur les heures
restantes sur un bon de commande.](../../../../_images/track-bill-remaining-
hours-total.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le nombre d’heures dans l’onglet <b>Feuilles de temps</b> dépasse le nombre d’heures vendues, le champ <b>Heures restantes sur le bon de commande</b> deviendra rouge.</p>
</div>

Au fur et à mesure que des heures sont ajoutées à l’onglet **Feuilles de
temps** , elles sont également automatiquement mises à jour dans le champ
**Livré** sur le bon de commande.

## Facturer des services d’assistance post-payés

Lorsque des services d’assistance sont facturés en fonction du nombre d’heures
passées sur une intervention, il n’est pas possible de créer une facture avant
que le nombre total d’heures nécessaires à la résolution du problème n’ait été
saisi sur une feuille de temps. Dans ce cas, un produit de service dont la
politique de facturation est définie sur **Basé sur les feuilles de temps**
doit être utilisé, comme celui créé ci-dessus.

### Créer un bon de commande avec un produit suivi dans le temps

Pour facturer à un client des services d’assistance post-payés, créez d’abord
un bon de commande avec le _produit de services d’assistance_. Pour ce faire,
allez à Ventes ‣ Commandes ‣ Devis ‣ Nouveau.

Complétez le devis avec les informations relatives au client.

Sur l’onglet **Lignes de la commande** , cliquez sur **Ajouter un produit**.
Sélectionnez le produit de services post-payés configuré dans les étapes
susmentionnées. Après avoir mis à jour toutes les autres informations
nécessaires, **confirmez** le devis.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Contrairement au devis des services prépayés, Konvergo ERP ne permet pas de créer une facture à ce stade. Cela est dû au fait qu’aucun service n’a été effectué : en d’autres termes, rien n’a été livré et il n’y a donc rien à facturer.</p>
</div>

### Créer un ticket d’assistance pour les services suivis dans le temps

Pour enregistrer une entrée de _Feuilles de temps_ pour des services suivis
dans le temps, allez à Assistance et sélectionnez l’équipe appropriée pour
laquelle ces services s’appliquent.

S’il existe déjà un ticket pour cette intervention, sélectionnez-le dans la
vue kanban. Cette action fait apparaître le formulaire de détails du ticket.
S’il n’y a pas de ticket existant pour ce problème client, cliquez sur
**Nouveau** pour créer un nouveau ticket et saisissez les informations
nécessaires relatives au client sur le formulaire détaillé du ticket vierge.

Après avoir sélectionné ou créé un ticket, allez au menu déroulant **Ligne de
commande**. Sélectionnez le bon de commande créé lors de l’étape précédente.

### Suivre les heures d’assistance sur un ticket

Afin de créer une facture pour un produit basé sur des feuilles de temps, il
faut suivre et enregistrer les heures. À ce stade, le service est considéré
comme _livré_. Pour enregistrer les heures pour ce service d’assistance,
cliquez sur l’onglet **Feuilles de temps** du ticket.

Cliquez sur **Ajouter une ligne** pour enregistrer une nouvelle entrée.
Sélectionnez une fiche d”**Employé** dans le menu déroulant et enregistrez les
heures passées dans la colonne **Heures passées**.

Répétez ces étapes si nécessaire jusqu’à ce que toutes les heures passées sur
le problème aient été enregistrées.

![Vue de l'onglet feuilles de temps d'un ticket
d'assistance.](../../../../_images/track-bill-record-timesheet-hours.png)

### Créer une facture pour les heures suivies sur un ticket

Une fois que le problème du client a été résolu et qu’il a été déterminé
qu’aucune nouvelle entrée de feuilles de temps ne sera effectuée, une facture
peut être créée et le client peut être facturé.

Pour ce faire, retournez au bon de commande en cliquant sur le bouton
intelligent **Bon de commande** en haut du ticket.

Avant de créer la facture, confirmez que le nombre dans la colonne **Livré**
correspond au nombre total d”**Heures passées** indiqué dans l’onglet
**Feuilles de temps** du ticket.

![Vue d'un bon de commande avec l'accent sur la colonne
Livré.](../../../../_images/track-bill-delivered-timesheet-hours.png)

Cliquez ensuite sur **Créer une facture**. Cette action permet d’ouvrir une
fenêtre contextuelle **Créer les factures**. Si aucun acompte n’est perçu,
l’option **Créer une facture** peut rester sur **Facture normale**. Si un
acompte doit être perçu, choisissez entre **Acompte (pourcentage)** ou
**Acompte (montant fixe)**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Utilisez le champ <b>Période des feuilles de temps</b> si cette facture doit uniquement inclure des feuilles de temps d’une certaine période. Si ce champ est laissé vide, <em>toutes</em> les feuilles de temps applicables qui n’ont pas encore été facturées seront incluses.</p>
</div> ![Vue de la fenêtre contextuelle de création des factures
montrant les champs de période des feuilles de
temps.](../../../../_images/track-bill-create-invoice-timesheets-period.png)

Lorsque les informations nécessaires ont été saisies, cliquez sur **Créer une
facture**. La facture peut ensuite être envoyée au client pour paiement.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/inventory/product_management/product_replenishment/uom">Unités de mesure</a></p>
</div>

