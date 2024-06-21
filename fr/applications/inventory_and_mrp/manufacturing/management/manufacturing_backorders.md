# Reliquats de fabrication

Il arrive que la quantité totale d’un ordre de fabrication ne puisse pas être
produite immédiatement. Dans ce cas, Konvergo ERP _Fabrication_ permet la fabrication
de quantités partielles de l’ordre et la création d’un _reliquat_ pour la
quantité restante.

Dans l’application _Fabrication_ , la création d’un reliquat divise l’ordre de
fabrication original en deux ordres. L’étiquette de référence pour chaque
ordre est l’étiquette utilisée pour l’ordre original, suivie d’un tiret et
d’un chiffre supplémentaire pour indiquer qu’il s’agit d’un reliquat.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Une société crée un ordre de fabrication avec l’étiquette de référence <em>WH/MO/00175</em>, pour 10 unités du <em>Produit X</em>. Après avoir lancé l’ordre de fabrication, l’employé travaillant sur la ligne de production se rend compte qu’il n’y a suffisamment de composants en stock que pour produire cinq unités du produit.</p>
<p>Au lieu d’attendre qu’une quantité suffisante de composants est en stock, la société fabrique cinq unités et crée un reliquat pour les cinq autres. Elle divise l’ordre de fabrication en deux ordres séparés : <em>WH/MO/00175-001</em> et <em>WH/MO/00175-002</em>.</p>
<p>L’ordre <em>001</em> contient les cinq unités qui ont été fabriquées et est immédiatement marqué comme <b>Fait</b>. L’ordre <em>002</em> contient les cinq unités qui doivent encore être fabriquées et sont marquées comme <b>En cours</b>. Une fois que les composants restants sont disponibles, l’employé revient à l’ordre <em>002</em> et fabrique les unités restantes avant de fermer l’ordre.</p>
</div>

## Créer un reliquat de fabrication

Pour créer un reliquat pour une partie de l’ordre de fabrication, allez à
Fabrication ‣ Opérations ‣ Ordres de fabrication. Sélectionnez un ordre de
fabrication avec une quantité de deux ou plus ou créez-en un en cliquant sur
**Créer**.

Si un nouvel ordre de fabrication est créé, sélectionnez un produit dans le
menu déroulant **Produit** et saisissez une quantité de deux ou plus dans le
champ **Quantité** , puis cliquez sur **Confirmer** pour confirmer l’ordre.

Après avoir fabriqué la quantité à produire immédiatement, saisissez ce nombre
dans le champ **Quantité** en haut de l’ordre de fabrication.

![Le champ quantité sur un ordre de
fabrication.](../../../../_images/quantity-field.png)

Cliquez ensuite sur **Valider** , et une fenêtre contextuelle **Vous avez
produit moins que la demande initiale** s’ouvre, à partir de laquelle un
reliquat peut être créé. Cliquez sur **Créer un reliquat** pour diviser
l’ordre de fabrication en deux ordres séparés, avec les étiquettes de
référence _WH/MO/XXXXX-001_ et _WH/MO/XXXXX-002_.

![Le bouton Créer un reliquat dans la fenêtre contextuelle "Vous avez produit
moins que la demande initiale".](../../../../_images/create-backorder-
button.png)

L’ordre _001_ contient les articles qui ont été fabriqués et est clôturé
immédiatement. L’ordre _002_ est le reliquat qui contient les articles qui
n’ont pas encore été fabriqués et qui reste ouvert, pour être terminé à une
date ultérieure.

Une fois que les unités restantes peuvent être fabriquées, allez à Fabrication
‣ Opérations ‣ Ordres de fabrication, et sélectionnez l’ordre de fabrication
en reliquat. Si toutes les unités restantes sont fabriquées immédiatement, il
suffit de cliquer sur **Valider** pour fermer l’ordre.

Si seulement une partie des unités est fabriquée immédiatement, créez un autre
reliquat pour le reste en suivant les étapes détaillées dans cette section.

## Créer un reliquat à partir de la vue de tablette

Les reliquats pour les ordres de fabrication peuvent également être créés à
partir de la vue de tablette de l’ordre de travail.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Afin d’utiliser la vue de tablette, la fonctionnalité <em>Ordres de travail</em> doit être activée. Pour l’activer, allez à Fabrication ‣ Configuration ‣ Paramètres. Sur la page des <b>Paramètres</b>, cochez la case à côté de l’option <b>Ordres de travail</b>, puis cliquez sur <b>Enregistrer</b> pour enregistrer les changements. L’onglet <b>Ordres de travail</b> apparaît alors sur les ordres de travail, à partir desquels la vue de tablette peut être ouverte.</p>
<img alt="Le paramètre des ordres de travail sur la page des paramètres de Fabrication." class="align-center" src="../../../../_images/work-orders-setting.png"/>
</div>

Pour créer un reliquat à partir de la vue de tablette, allez à Fabrication ‣
Opérations ‣ Ordres de fabrication. Sélectionnez un ordre de fabrication avec
une quantité de deux ou plus ou créez-en un en cliquant sur **Créer**.

Si un nouvel ordre de fabrication est créé, sélectionnez un produit dans le
menu déroulant **Produit** et saisissez une quantité de deux ou plus dans le
champ **Quantité** , puis cliquez sur **Confirmer** pour confirmer l’ordre.

Après avoir confirmé l’ordre de fabrication, sélectionnez l’onglet **Ordres de
travail** et cliquez sur le bouton **📱 (vue de tablette)** situé sur la ligne
du premier ordre de travail pour ouvrir la vue de tablette.

![Le bouton de la vue de tablette pour un ordre de travail sur un ordre de
fabrication.](../../../../_images/tablet-view-button.png)

Une fois dans la vue de tablette, saisissez la quantité fabriquée
immédiatement dans le champ **Unités** en haut à gauche de la vue de tablette.

![Le champ Unités dans la vue de tablette.](../../../../_images/units-
field.png)

Les étapes du reste du flux de travail varient selon que l’ordre de
fabrication en cours de traitement nécessite la réalisation d’un seul ordre de
travail ou de plusieurs ordres de travail.

### Un seul ordre de travail

Si l’ordre de fabrication ne nécessite qu’un seul ordre de travail, terminez
l’ordre de travail et cliquez sur **Marquer comme fait et fermer l’ordre de
fabrication**. L’ordre de fabrication est fermé et un reliquat est
automatiquement créé pour les unités qui doivent encore être fabriquées.

![Le bouton Marquer comme fait et fermer l'ordre de fabrication dans la vue de
tablette d'un ordre de travail.](../../../../_images/madacmo-button.png)

Une fois que les unités restantes sont prêtes à être fabriquées, allez à
Fabrication ‣ Opérations ‣ Ordres de fabrication, puis sélectionnez l’ordre de
fabrication en reliquat, qui est intitulé à l’aide de l’étiquette de référence
du reliquat original avec _002_ ajouté à la fin.

Sur l’ordre de fabrication en reliquat, sélectionnez l’onglet **Ordres de
travail** et cliquez sur le bouton **📱 (vue de tablette)** sur la ligne de
l’ordre de travail pour ouvrir la vue de tablette. Si toutes les unités du
reliquat seront terminées immédiatement, cliquez simplement sur **Marquer
comme fait et fermer l’ordre de fabrication** après avoir terminé l’ordre de
travail.

Si seules certaines des unités restantes seront fabriquées immédiatement,
saisissez le nombre dans le champ **Unités** en haut à gauche de la vue de
tablette, puis cliquez sur **Marquer comme fait et fermer l’ordre de
fabrication** pour créer un autre reliquat pour les unités restantes. Le
nouveau reliquat peut être traité en suivant les étapes détaillées dans cette
section.

### Plusieurs ordres de travail

Si l’ordre de travail nécessite la réalisation de plusieurs ordres de travail,
terminez le premier ordre de travail et cliquez sur **Enregistrer la
production**. Ceci divise l’ordre de fabrication en deux ordres séparés,
intitulés _WH/MO/XXXXX-001_ et _WH/MO/XXXXX-002_ , _XXXXX_ étant le numéro de
l’ordre original.

![Le bouton Enregistrer la production sur un ordre de
travail.](../../../../_images/record-production-button.png)

La vue de tablette affiche par défaut le premier ordre de travail de l’ordre
de fabrication _002_. Puisque cet ordre de fabrication ne sera pas terminé
immédiatement, quittez la vue de tablette en cliquant deux fois sur le bouton
**⬅️ (retour)**. Vous reviendrez alors à l’ordre _001_.

Pour terminer l’ordre _001_ , sélectionnez l’onglet **Ordres de travail** et
cliquez sur le bouton **vue de tablette** situé sur la ligne du prochain ordre
de travail. Enfin, terminez les ordres de travail restants, puis cliquez sur
**Marquer comme fait et fermer l’ordre de fabrication** pour fermer l’ordre de
fabrication.

Une fois que les unités restantes sont prêtes à être fabriquées, allez à
Fabrication ‣ Opérations ‣ Ordres de fabrication, puis sélectionnez l’ordre
_002_. Sélectionnez l’onglet **Ordres de travail** et cliquez le bouton **vue
de tablette** situé sur la ligne du premier ordre de travail.

Si toutes les unités du reliquat sont terminées immédiatement, cliquez
simplement sur **Marquer comme fait et fermer l’ordre de fabrication** après
avoir terminé tous les ordres de travail.

Si seules certaines des unités restantes seront fabriquées immédiatement,
saisissez le nombre dans le champ **Unités** en haut à gauche de la vue de
tablette, puis cliquez sur **Enregistrer la production** pour créer un
reliquat additionnel pour les unités restantes, avec _003_ à la fin de son
étiquette de référence.

Le reliquat _002_ et le reliquat _003_ peuvent être terminés en suivant les
étapes détaillées dans cette section.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est également possible de créer un reliquat au milieu d’un ordre de fabrication, lorsque certains des ordres de travail ont déjà été terminés, mais pas tous. Dans ce cas, le ou les ordres de travail sont marqués comme <b>terminés</b> sur le reliquat.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un ordre de fabrication pour quatre chaises nécessite la réalisation de deux ordres de travail : <em>Peinture</em> et <em>Assemblage</em>. Alors que l’étape de peinture peut être réalisée immédiatement pour les quatre chaises, il n’y a suffisamment de vis que pour assembler deux d’entre elles.</p>
<p>Par conséquent, l’employé chargé de la production des chaises commence par peindre les quatre chaises et marquer l’ordre de travail <em>Peinture</em> comme <b>Terminé</b> pour chacune d’entre elles. Il passe ensuite à l’ordre de travail <em>Assemblage</em>. Il assemble deux des quatre chaises, saisit ce nombre dans le champ <b>Unités</b> de la vue de tablette et clique sur <b>Enregistrer la production</b>.</p>
<p>Un ordre de fabrication en reliquat est créé pour les deux chaises restantes. Sur le reliquat, l’ordre de travail <em>Peinture</em> est déjà marqué comme <b>Terminé</b> et il ne reste plus que l’ordre de travail <em>Assemblage</em> à terminer.</p>
<p>Une fois les vis disponibles, l’employé chargé de la fabrication assemble les chaises restantes et clique sur <b>Marquer comme fait et fermer l’ordre de fabrication</b> pour terminer l’ordre de travail <em>Assemblage</em> et fermer l’ordre de fabrication en reliquat.</p>
</div>
</div>

