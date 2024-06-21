# Ajustements d’inventaire

Dans tout système de gestion d’entrepôt, les inventaires virtuels dans la base
de données ne correspondent pas toujours aux inventaires réels dans
l’entrepôt. L’écart entre les deux quantités peut être dû à des dommages, des
erreurs humaines, des vols ou d’autres facteurs. Ainsi, des ajustements
d’inventaire doivent être effectués pour réconcilier l’écart et s’assurer que
les quantités enregistrées dans la base de données correspondent aux quantités
réelles dans l’entrepôt.

## Page des ajustements d’inventaire

Pour afficher la page des _Ajustements d’inventaire_ , allez à l’application
Inventaire ‣ Opérations ‣ Ajustements d’inventaire.

![Liste des produits en stock sur la page des ajustements
d'inventaire.](../../../../../_images/inventory-adjustments-page.png)

La page des **Ajustements d’inventaire** répertorie tous les produits qui sont
actuellement en stock. Chaque ligne de produit contient les informations
suivantes :

  * **Emplacement** : l’emplacement spécifique dans l’entrepôt où le produit est stocké.

  * **Produit** : le produit dont la qualité est répertoriée sur la ligne de l’ajustement d’inventaire.

  * **Lot/Numéro de série** : l’identifiant de suivi attribué au produit spécifique répertorié. Il peut contenir des lettres, des chiffres ou une combinaison des deux.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un produit spécifique a une quantité supérieure à <code>1.00</code> en stock et que plusieurs numéros de série (ou de lot) lui sont attribués, chaque produit identifié de manière unique s’affiche sur sa propre ligne de produit avec son propre lot/numéro de série, affiché dans la colonne <b>Lot/Numéro de série</b>.</p>
</div>

  * **Quantité en stock** : la quantité du produit actuellement enregistrée dans la base de données.

  * **UdM** : l” _unité de mesure_ dans laquelle le produit est mesuré. Sauf indication contraire (c’est-à-dire, en **Livres** ou en **Onces**), l”UdM par défaut est **Unités**.

  * **Quantité comptée** : la quantité réelle comptée lors d’un inventaire. Ce champ est laissé vide par défaut, mais peut être modifié selon qu’il correspond ou non à la **Quantité en stock**.

  * **Différence** : la différence entre la **Quantité en stock** et la **Quantité comptée** après avoir effectué un inventaire. La différence se calcule automatiquement après chaque ajustement d’inventaire.

  * **Date planifiée** : la date à laquelle un inventaire doit être effectué. Si rien n’est précisé, la date est fixée par défaut au 31 décembre de l’année en cours.

  * **Utilisateur** : la personne assignée à l’inventaire dans la base de données. Il peut s’agir de la personne qui compte physiquement l’inventaire ou qui enregistre le comptage dans la base de données.

  * **Catégorie de produits** : la catégorie attribuée en interne à un produit spécifique. Sauf indication contraire (c’est-à-dire **Consommable** ou **Location**), la _Catégorie de produits_ par défaut est définie sur **All**.

  * **Quantité disponible** : la quantité d’un produit spécifique qui est actuellement disponible, en fonction des commandes, bons de commande ou ordres de fabrication en cours ou non terminés qui pourraient modifier la quantité disponible une fois qu’ils auront été exécutés.

  * **Date comptable** : la date à laquelle les ajustements seront comptabilisés dans l’application Konvergo ERP _Comptabilité_.

  * **Société** : la société dont la base de données contient ces ajustements d’inventaire. La société s’affiche dans le coin supérieur droit de la base de données, à côté de l’utilisateur actuellement connecté.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Certaines colonnes sont masquées par défaut. Pour afficher ces colonnes, cliquez sur le bouton des <b>options supplémentaires</b> (icône des trois petits points) à l’extrême droite de la ligne supérieure du formulaire et sélectionnez la colonne que vous voulez faire apparaître en cochant la case à côté de cette option.</p>
</div>

### Créer un ajustement d’inventaire

Pour créer un nouvel ajustement d’inventaire à partir de la page Ajustements
d’inventaire, cliquez sur **Créer**. Une nouvelle ligne d’ajustement
d’inventaire vierge est ainsi créée au bas de la page.

Sur cette ligne d’ajustement d’inventaire vierge, cliquez sur le menu
déroulant dans la colonne **Produit** et sélectionnez un produit. Si le
produit sélectionné est suivi à l’aide de lots ou de numéros de série, le lot
ou numéro de série souhaité peut également être sélectionné dans le menu
déroulant dans la colonne **Lot/Numéro de série**.

Ensuite, définissez la valeur dans la colonne **Quantité comptée** comme étant
la quantité comptée pour ce produit au cours du processus d’ajustement de
l’inventaire.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La <b>Quantité comptée</b> pour les nouveaux ajustements d’inventaire est fixée par défaut à <code>0,00</code>. Un mouvement d’inventaire avec une <b>Quantité faite</b> de <code>0,00</code> est enregistré dans l’historique des ajustements d’inventaire du produit, et doit donc être défini de manière à refléter la quantité réellement comptée.</p>
</div>

À droite de la colonne **Quantité comptée** , vous pouvez également modifier
la **Date planifiée** et l”**Utilisateur** à l’aide de leurs menus déroulants
respectifs. La modification de la **Date planifiée** change la date à laquelle
l’ajustement d’inventaire doit être traité, et la sélection d’un
**Utilisateur** responsable assigne un utilisateur à l’ajustement d’inventaire
spécifique (à des fins de traçabilité).

Une fois que toutes les modifications ont été apportées à la nouvelle ligne
d’ajustement d’inventaire, cliquez à l’écart de la ligne. Cette opération
permet d’enregistrer l’ajustement et de déplacer la ligne en haut de la page.

Si la **Quantité comptée** est supérieure à la **Quantité en stock** , la
valeur de la colonne **Différence** s’affiche en **vert**. Si la **Quantité
comptée** est inférieure à la **Quantité en stock** , la valeur de la colonne
**Différence** s’affiche en **rouge**. Si les quantités correspondent et n’ont
pas été modifiées, aucune valeur n’apparaît dans la colonne **Différence**.

![Colonne Différence sur la page des ajustements
d'inventaire.](../../../../../_images/difference-column.png)

À ce stade, le comptage (ajustement d’inventaire) est enregistré, mais n’est
pas encore appliqué. Cela signifie que la quantité en stock avant l’ajustement
n’a pas encore été mise à jour pour refléter la nouvelle quantité réellement
comptée.

Il y a deux façons d’appliquer le nouvel ajustement d’inventaire. La première
façon consiste à cliquer sur le bouton **Appliquer** sur la ligne à l’extrême
droite de la page. La deuxième façon consiste à cocher la case à l’extrême
gauche de la ligne. Cela permet d’afficher de nouvelles options en haut de la
page, dont un bouton **Appliquer**. En cliquant sur ce bouton, une fenêtre
contextuelle **Référence/motif de l’ajustement** s’affiche.

Ce menu contextuel permet d’ajouter une référence ou une raison à l’ajustement
d’inventaire. Par défaut, le champ **Référence/motif d’inventaire** est
prérempli avec la date à laquelle l’ajustement est effectué, mais il peut être
modifié pour refléter la référence ou le motif souhaité.

Une fois que vous avez terminé, cliquez sur **Appliquer** pour appliquer
l’ajustement d’inventaire.

![L'option Appliquer à tout applique l'ajustement d'inventaire dès qu'un motif
est précisé.](../../../../../_images/apply-inventory-adjustment.png)

## Compter les produits

Le comptage des produits est une activité récurrente dans un entrepôt. Une
fois l’inventaire terminé, allez à l’application Inventaire ‣ Opérations ‣
Ajustements d’inventaire pour mettre à jour la colonne **Quantité comptée**
pour chaque ligne de produit.

Sur chaque ligne de produit, identifiez si la valeur de la colonne **Quantité
en stock** enregistrée dans la base de données correspond à la valeur
nouvellement comptée. Si la valeur enregistrée et la valeur comptée
correspondent, cliquez sur le bouton **Définir** (icône de cible) à l’extrême
droite de la ligne de produit.

Cette opération permet de copier la valeur de la colonne **Quantité en stock**
dans la colonne **Quantité comptée** et de fixer la valeur de la colonne
**Différence** à `0,00`. Par la suite, une fois appliqué, un mouvement
d’inventaire avec une **Quantité faite** de `0,00` est enregistré dans
l’historique des ajustements d’inventaire du produit.

![Valeur du zéro du mouvement d'ajustement
d'inventaire.](../../../../../_images/zero-move.png)

Si la valeur nouvellement comptée pour un produit donné ne correspond **pas**
à la valeur de la **Quantité en stock** enregistrée dans la base de données,
au lieu de cliquer sur le bouton **Définir** , enregistrez la valeur réelle
dans le champ de la colonne **Quantité comptée**.

Pour ce faire, cliquez sur le champ de la colonne **Quantité comptée** sur la
ligne d’ajustement d’inventaire spécifique pour le produit dont le comptage
est modifié. Une **Quantité comptée** de `0,00` est alors automatiquement
attribuée.

Pour modifier cette valeur, saisissez une nouvelle valeur qui corresponde à la
valeur réelle nouvellement comptée. Cliquez ensuite à l’écart de la ligne.
Cette opération permet d’enregistrer l’ajustement et d’automatiquement ajuster
la valeur de la colonne **Différence**.

Si la **Quantité comptée** est supérieure à la **Quantité en stock** , la
valeur de la colonne **Différence** s’affiche en **vert**. Si la **Quantité
comptée** est inférieure à la **Quantité en stock** , la valeur de la colonne
**Différence** s’affiche en **rouge**. Si les quantités correspondent et n’ont
pas été modifiées, aucune valeur n’apparaît dans la colonne **Différence**.

Par conséquent, une fois appliqué, un mouvement avec la différence entre la
**Quantité en stock** et la **Quantité comptée** est enregistrée dans
l’historique des ajustements d’inventaire du produit.

![Tableau de bord de l'historique des ajustements d'inventaire détaillant une
liste des mouvements de produit antérieurs.](../../../../../_images/history-
inventory-adjustments.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il arrive qu’un comptage ait lieu, mais qu’il ne puisse pas être appliqué immédiatement dans la base de données. Dans l’intervalle entre l’inventaire et l’application de l’ajustement d’inventaire, des mouvements de produits peuvent se produire. Dans ce cas, la quantité en stock dans la base de données peut changer et ne plus correspondre à la quantité comptée. Par mesure de précaution supplémentaire, Konvergo ERP demande une confirmation avant d’appliquer l’ajustement d’inventaire.</p>
</div>

## Modifier la fréquence des inventaires

Par défaut, la _date planifiée_ pour les ajustements d’inventaire est toujours
fixée au 31 décembre de l’année en cours. Toutefois, pour certaines
entreprises, il est essentiel de disposer à tout moment d’un inventaire
précis. Dans ce cas, la date planifiée par défaut peut être modifiée.

Pour modifier la date planifiée par défaut, allez à l’application Inventaire ‣
Configuration ‣ Paramètres. Ensuite, dans la section **Opérations** , repérez
le paramètre **Jour et mois de l’inventaire annuel** , qui comprend un menu
déroulant qui est par défaut défini sur le `31 décembre`.

![Ajouter la prochaine date d'inventaire grâce au paramètre Jour et mois de
l'inventaire annuel.](../../../../../_images/annual-inventory.png)

Pour modifier le jour, cliquez sur **31** , et remplacez-le par un jour
compris entre `1 et 31`, en fonction du mois de l’année souhaité.

Pour modifier le mois, cliquez sur **Décembre** pour faire apparaître le menu
déroulant et sélectionnez le mois souhaité.

Une fois que toutes les modifications ont été apportées, cliquez sur
**Enregistrer** pour enregistrer tous les changements.

### Planifier des inventaires importants

Pour planifier des inventaires importants, tels qu’un inventaire complet de
tout ce qui est actuellement en stock, allez d’abord à l’application
Inventaire ‣ Opérations ‣ Ajustements d’inventaire.

Sélectionnez ensuite les produits souhaités à inventorier en cochant la case à
l’extrême gauche de chaque ligne de produit.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour demander un inventaire de <b>tous</b> les produits actuellement en stock, cochez la case tout en haut du tableau, dans la ligne d’en-tête à côté du libellé <b>Emplacement</b>. <b>Toutes</b> les lignes de produits sont ainsi sélectionnées.</p>
</div> ![Fenêtre contextuelle de demande d'inventaire sur la page
des ajustements d'inventaire.](../../../../../_images/count-popup.png)

Une fois que tous les produits souhaités ont été sélectionnés, cliquez sur le
bouton **Demander un inventaire** en haut de la page. Une fenêtre contextuelle
**Demander un inventaire** s’affiche alors. Dans cette fenêtre, saisissez les
informations suivantes :

  * **Date d’inventaire** : la date prévue de l’inventaire.

  * **Utilisateur** : l’utilisateur en charge de l’inventaire.

  * **Date comptable** : la date à laquelle l’ajustement d’inventaire sera comptabilisé.

  * **Count** : to leave the on-hand quantity of each product line blank, select **Leave Empty**. To pre-fill the on-hand quantity of each product line with the current value recorded in the database, select **Set Current Value**.

Enfin, une fois que vous avez terminé, cliquez sur **Confirmer** pour demander
l’inventaire.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Dans l’application <em>Code-barres</em> d’Konvergo ERP, les utilisateurs peuvent uniquement voir les inventaires qui <b>leur</b> sont assignés et qui sont programmés pour <b>aujourd’hui</b> ou <b>plus tôt</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="cycle_counts">Comptages cycliques</a></p>
</div>

  *[UdM]: Unité de mesure

