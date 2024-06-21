# Utiliser des numéros de série pour suivre des produits

Les _Numéros de série_ sont l’une des deux façons d’identifier et de suivre
des produits dans Konvergo ERP. Un numéro de série est un identifiant unique assigné
de manière incrémentielle (ou séquentielle) à un article ou un produit,
utilisé pour le distinguer des autres articles et produits.

Les numéros de série peuvent être composés de différents types de caractères :
ils peuvent être strictement numériques, ils peuvent contenir des lettres et
d’autres symboles typographiques ou ils peuvent être un mélange de tous ces
éléments.

L’assignation de numéros de série à des produits individuels permet de
s’assurer que l’historique de chaque article est identifiable lorsqu’il bouge
dans la chaîne d’approvisionnement. Ceci peut être particulièrement utile pour
les fabricants qui fournissent des services après-vente aux produits qu’ils
vendent et livrent.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="lots">Lot numbers</a></p>
</div>

## Activer les lots et les numéros de série

Pour suivre des produits à l’aide de numéros de série, la fonctionnalité
**Lots & Numéros de série** doit être activée. Pour ce faire, allez à
l’application Inventaire ‣ Configuration ‣ Paramètres, faites défiler jusqu’à
la section **Traçabilité** et cochez la case à côté de **Lots & Numéros de
série**. Pensez à cliquer sur le bouton **Enregistrer** pour enregistrer tous
les changements.

![Paramètre des lots et numéros de série
activé.](../../../../../_images/serial-numbers-enabled-setting.png)

## Configurer le suivi par numéro de série sur les produits

Une fois le paramètre **Lots & Numéros de série** activé, il est possible de
suivre des produits individuels pour être suivis à l’aide de numéros de série.
Pour ce faire, allez à l’application Inventaire ‣ Produits ‣ Produits et
choisissez un produit à suivre.

Sur la fiche du produit, cliquez sur **Modifier** et cliquez sur l’onglet
**Inventaire**.

Sur la fiche du produit, cliquez sur **Modifier** , allez à l’onglet
**Inventaire** et faites défiler jusqu’à la section **Traçabilité**. Ensuite,
sélectionnez l’option **Par numéro de série unique** et cliquez sur
**Enregistrer** pour enregistrer les changements. Il est désormais possible de
sélectionner des nouveaux numéros de série ou des numéros de série existants
et les assigner aux lots nouvellement reçus ou fabriqués de ce produit.

![Le suivi par numéro de série activé sur la fiche du
produit.](../../../../../_images/serial-numbers-product-tracking.png)
<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si un produit n’a pas de numéro de série assigné, une fenêtre contextuelle d’erreur d’utilisateur apparaît. Le message d’erreur stipule que le ou les produits en stock n’ont pas de lot/numéro de série. Cependant, il est possible d’assigner un lot/numéro de série au produit en procédant à un ajustement d’inventaire.</p>
</div>

### Créer de nouveaux numéros de série pour des produits déjà en stock

Il est possible de créer de nouveaux numéros de série pour des produits déjà
en stock auxquels aucun numéro de série n’a été assigné. Pour ce faire, allez
à Inventaire ‣ Produits ‣ Lots/Numéros de série et cliquez sur **Créer**.
Cette opération fait apparaître un formulaire de lots/numéros de série vierge.
Sur ce formulaire, un nouveau **Lot/Numéro de série** est généré
automatiquement.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Bien qu’Konvergo ERP génère automatiquement un nouveau lot/numéro de série pour suivre le numéro le plus récent, il peut être édité et modifié en n’importe quel autre numéro, en cliquant sur la ligne sous le champ <b>Lot/Numéro de série</b> et en changeant le numéro généré.</p>
</div>

Une fois le **Lot/Numéro de série** généré, cliquez sur le champ vierge à côté
du **Produit** pour révéler un menu déroulant. Dans ce menu, sélectionnez le
produit auquel ce nouveau numéro sera assigné.

Ce formulaire permet également d’ajuster la **Quantité** , d’assigner un
numéro de **Référence interne** unique (à des fins de traçabilité) et
d’assigner cette configuration de lot/numéro de série spécifique à un site web
spécifique dans le champ **Site web** (si vous avez plusieurs sites web).

Il est aussi possible d’ajouter une description détaillée à ce lot/numéro de
série spécifique dans l’onglet **Description** en dessous.

Lorsque toutes les configurations souhaitées sont terminées, cliquez sur le
bouton **Enregistrer** pour enregistrer tous les changements.

![Nouveau numéro de série créé pour un produit existant en
stock.](../../../../../_images/serial-numbers-new-serial-number.png)

Une fois qu’un nouveau numéro de série a été créé, assigné au produit souhaité
et enregistré, retournez à la fiche du produit en allant à Produits ‣ Produits
et sélectionnez le produit auquel ce numéro de série nouvellement créé vient
d’être assigné.

Sur la fiche détaillée de ce produit, cliquez sur le bouton intelligent
**Lot/Numéros de série** pour afficher le nouveau numéro de série.

## Gérer des numéros de série pour l’expédition et la réception

Les numéros de série peuvent être assignés à des marchandises **entrantes** et
**sortantes**. Pour les marchandises entrantes, les numéros de série sont
directement assignés sur le bon de commande. Pour les marchandises sortantes,
les numéros de série sont directement assignés sur la commande client.

### Gérer des numéros de série lors des réceptions

Il est possible de directement assigner des numéros de série à des
marchandises **entrantes** sur le bon de commande.

Pour créer un bon de commande, allez à l’application Achats ‣ Créer. Cette
opération fait apparaître un formulaire de demande de prix vierge.

Sur cette demande de prix, complétez les informations nécessaires en ajoutant
un **Fournisseur** et en ajoutant les produits souhaités aux lignes de
**Produit** , en cliquant sur **Ajouter un produit** dans l’onglet
**Produits**.

Choisissez la quantité souhaitée du produit à commander en modifiant le nombre
dans la colonne **Quantité**.

Lorsque les configurations nécessaires sont terminées, cliquez sur **Confirmer
la commande**. Cette action transformera la demande de prix en bon de
commande.

Cliquez ensuite sur le bouton intelligent **Réception** pour afficher le
formulaire de réception de l’entrepôt pour ce bon de commande.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous cliquez sur <b>Valider</b> avant d’assigner un numéro de série aux quantités de produits commandées, une fenêtre contextuelle <b>Erreur d’utilisateur</b> s’affiche. La fenêtre exige la saisie d’un numéro de lot ou de série pour les produits commandés. La demande de prix <b>ne peut pas être</b> validée sans l’assignation d’un numéro de série.</p>
</div> ![Fenêtre contextuelle d'erreur d'utilisateur demandant la
saisie d'un numéro de série.](../../../../../_images/serial-numbers-user-
error-popup.png)

À partir de là, cliquez sur le menu **Options supplémentaires** , représenté
par une icône `hamburger` (quatre lignes horizontales situées à droite de la
colonne **Unité de Mesure** dans l’onglet **Opérations**). Le fait de cliquer
sur cette icône fait apparaître une fenêtre contextuelle **Opérations
détaillées**.

Dans cette fenêtre contextuelle, configurez un nombre de champs différents, y
compris l’assignation d’un numéro de série (ou de numéros de série) dans la
colonne **Nom du lot/numéro de série** , située en bas de la fenêtre.

Il existe trois façons d’y procéder : l’assignation manuelle des numéros de
série, l’assignation automatique des numéros de série et copier/coller les
numéros de série à partir d’une feuille de calcul.

#### Assigner des numéros de série manuellement

Pour assigner des numéros de série manuellement, cliquez sur **Ajouter une
ligne** dans la fenêtre contextuelle **Opérations détaillées** et choisissez
d’abord l’emplacement où le produit sera stocké dans la colonne **Vers**.

Saisissez ensuite un nouveau **Nom de numéro de série** et définissez la
quantité **Fait** dans les colonnes appropriées.

Répétez ce processus pour la quantité de produits affichée dans le champ
**Demande** et jusqu’à ce que le champ **Quantité faite** affiche le bon
nombre (correspondant) de produits traités.

#### Assigner des numéros de série automatiquement

Si une grande quantité de produits nécessite l’assignation de numéros de série
individuels, Konvergo ERP peut automatiquement générer et assigner des numéros de
série à chaque produit individuel.

Pour ce faire, commencez par le champ **Premier NS** dans la fenêtre
contextuelle **Opérations détaillées** et saisissez le premier numéro de série
dans l’ordre d’assignation souhaité.

Ensuite, dans le champ **Nombre de NS** , saisissez le nombre total d’articles
auxquels des numéros de série uniques nouvellement générés doivent être
assignés.

Enfin, cliquez sur **Assigner des numéros de série** et une liste s’affichera
avec de nouveaux numéros de série correspondant à la quantité de produits
commandés.

![L'assignation automatique des numéros de série dans la fenêtre contextuelle
des opérations détaillées.](../../../../../_images/serial-numbers-auto-assign-
sn.png)

#### Copier/coller des numéros de série depuis une feuille de calcul

Pour copier et coller des numéros de série à partir d’une feuille de calcul
existante, remplissez d’abord une feuille de calcul avec tous les numéros de
série reçus du fournisseur (ou choisis manuellement à la réception). Ensuite,
copiez et collez-les dans la colonne **Nom de lot/numéro de série**. Konvergo ERP
créera automatiquement le nombre de lignes nécessaires en fonction du nombre
de numéros collés dans la colonne.

À partir de la, les emplacements **Vers** et les quantités **Fait** peuvent
être saisis manuellement pour chaque ligne de numéro de série.

![Liste des numéros de série copiés dans la feuille de calcul
Excel.](../../../../../_images/serial-numbers-excel-spreadsheet.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour les bons de commande qui incluent de grandes quantités de produits à recevoir, la meilleure méthode d’assignation des numéros de série est d’assigner des numéros de série automatiquement en utilisant le bouton <b>Assigner des numéros de série</b> sur le bon de commande. Cela permet d’éviter la réutilisation ou la duplication des numéros de série et d’améliorer les rapports de traçabilité.</p>
</div>

Une fois qu’un numéro de série a été assigné à toutes les quantités de
produits, cliquez sur le bouton **Confirmer** pour fermer la fenêtre
contextuelle. Cliquez ensuite sur **Valider**.

Un bouton intelligent **Traçabilité** apparaît lors de la validation de la
réception. Cliquez sur le bouton intelligent **Traçabilité** pour voir le
**Rapport de traçabilité** mis à jour, qui inclut : un document de
**Référence** , le **Produit** qui est suivi, le **# de lot/série** , et bien
plus encore.

Une fois qu’un numéro de série a été assigné à toutes les quantités de
produits, cliquez sur **Confirmer** pour fermer la fenêtre contextuelle et
cliquez sur **Valider**. Un bouton intelligent **Traçabilité** apparaît lors
de la validation de la réception. Cliquez sur le bouton intelligent
**Traçabilité** pour voir le **Rapport de traçabilité** mis à jour, qui inclut
: un document de **Référence** , le **Produit** qui est suivi, le **# de
lot/série** , et bien plus encore.

### Gérer des numéros de série sur des bons de livraison

Il est possible de directement assigner des numéros de vert à des marchandises
**sortantes** à partir de la commande client.

Pour créer une commande client, allez à l’application Ventes et cliquez sur le
bouton **Créer**. Cette opération fait apparaître un formulaire de devis
vierge. Sur ce formulaire de devis vierge, complétez les informations
nécessaires en ajoutant un **Client** et en ajoutant des produits aux lignes
de **Produits** (dans l’onglet **Lignes de la commande**), en cliquant sur
**Ajouter un produit**.

Choisissez ensuite la quantité que vous voulez vendre en changeant le nombre
dans la colonne **Quantité**.

Une fois que le devis a été complété, cliquez sur le bouton **Confirmer** pour
confirmer le devis. Lorsque le devis est confirmé, il devient une commande
client et un bouton intelligent **Livraison** apparaît.

Cliquez sur le bouton intelligent **Livraison** pour afficher le formulaire de
réception de l’entrepôt pour cette commande spécifique.

À partir de là, cliquez sur le menu **Options supplémentaires** , représenté
par une icône `hamburger` (quatre lignes horizontales situées à droite de la
colonne **Unité de Mesure** dans l’onglet **Opérations**). Le fait de cliquer
sur cette icône fait apparaître une fenêtre contextuelle **Opérations
détaillées**.

Dans la fenêtre contextuelle, un **Lot/Numéro de série** sera choisi par
défaut, avec chaque produit de la quantité **Réservée** totale avec leur
numéro de série unique (très probablement dans l’ordre séquentiel).

Pour modifier manuellement le numéro de série d’un produit, cliquez sur le
menu déroulent sous le **Lot/Numéro de série** et choisissez (ou saisissez) le
numéro de série souhaité. Notez ensuite les quantités **faites** et cliquez
sur **Confirmer** pour fermer la fenêtre.

Cliquez enfin sur le bouton **Valider** pour livrer les produits.

![Numéros de série listés dans la fenêtre contextuelle des opérations
détaillées.](../../../../../_images/serial-numbers-detailed-operations-
popup.png)

Lors de la validation du bon de livraison, un bouton intelligent
**Traçabilité** apparaît. Cliquez sur le bouton intelligent **Traçabilité**
pour voir le **Rapport de traçabilité** mis à jour, qui inclut : un document
de **Référence** , le **Produit** qui est suivi, la **Date** et le **# de
lot/série** assigné.

Le **Rapport de traçabilité** peut également inclure un reçu de **Référence**
du bon de commande précédent, si les quantités de produits partagent le même
numéro de série assigné lors de la réception de ce bon de commande spécifique.

## Gérer des numéros de série pour différents types d’opérations

Par défaut dans Konvergo ERP, la création de nouveaux numéros de série est uniquement
autorisée lors de la **réception** de produits d’un bon de commande. Il n’est
pas possible d’utiliser des numéros de série **existants**. Pour les commandes
clients, l’inverse est vrai : il n’est pas possible de créer de nouveaux
numéros de série sur le bon de livraison, seuls des numéros de série existants
peuvent être utilisés.

Pour modifier la possibilité d’utiliser de nouveaux numéros de série (ou des
numéros de série existants) sur n’importe quel type d’opération, allez à
l’application Inventaire ‣ Configuration ‣ Types d’opérations et sélectionnez
le **Type d’opération** souhaité.

Pour le type d’opération **Réceptions** , trouvé sur la page des **Types
d’opérations** , il est possible d’activer l’option **Utiliser des
lots/numéros de série existants** en sélectionnant **Réceptions** sur la page
des **Types d’opérations** , en cliquant sur **Modifier** et ensuite en
cochant la case à côté de l’option **Utiliser des lots/numéros de série
existants** (dans la section **Traçabilité**). Enfin, cliquez sur le bouton
**Enregistrer** pour enregistrer les changements.

Pour le type d’opération **Bons de livraison** , situé sur la page des **Types
d’opérations** , il est possible d’activer l’option **Créer de nouveaux
lots/numéros de série** en sélectionnant **Bons de livraison** sur la page des
**Types d’opérations** , en cliquant sur **Modifier** et en cochant la case à
côté de l’option **Créer de nouveaux lots/numéros de série** (dans la section
**Traçabilité**). Assurez-vous de cliquer sur **Enregistrer** pour enregistrer
les changements.

![Le paramètre de traçabilité activé dans le formulaire des types
d'opérations.](../../../../../_images/serial-numbers-operations-types.png)

## Traçabilité des numéros de série

Les fabricants et les entreprises peuvent consulter les rapports de
traçabilité pour voir le cycle de vie complet d’un produit : d’où il vient (et
quand), où il a été stocké et chez qui il est allé.

Pour voir la traçabilité complète d’un produit ou regrouper des produits par
numéros de série, allez à l’application Inventaire ‣ Produits ‣ Lots/Numéros
de série. Cette opération affiche le tableau de bord des **Lots/Numéros de
série**.

À partir de là, les produits auxquels des numéros de série ont été assignés
sont répertoriés par défaut et il est possible de les développer pour afficher
les numéros de série assignés à ces produits.

Pour regrouper par numéros de série (ou lots), supprimez d’abord les filtres
par défaut de la barre de recherche dans le coin supérieur droit. Cliquez
ensuite sur **Regrouper par** et sélectionnez **Ajouter un groupe
personnalisé** , qui affiche un mini menu déroulant. Dans ce mini menu
déroulant, sélectionnez **Lot/Numéro de série** et cliquez sur **Appliquer**.

Cette opération affiche tous les numéros de série et lots existants et il est
possible de les développer pour afficher toutes les quantités des produits
auxquels ce numéro est assigné. Pour des numéros de série uniques qui ne sont
pas réutilisés, il ne doit y avoir qu’un seul produit par numéro de série.

![Page de rapport sur les numéros de série avec listes
déroulantes.](../../../../../_images/serial-numbers-reporting-page.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour obtenir des informations supplémentaires sur un numéro de série (ou de lot) individuel, cliquez sur la ligne correspondant au numéro de série pour révéler le formulaire de <b>Numéro de série</b> de ce numéro de série spécifique. Dans ce formulaire, cliquez sur les boutons intelligents <b>Emplacement</b> et <b>Traçabilité</b> pour voir tous les stocks disponibles qui utilisent ce numéro de série et toutes les opérations effectuées à l’aide de ce numéro de série.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="differences">Difference between lots and serial numbers</a></p>
</div>

