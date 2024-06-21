# Gérer les entrepôts et les emplacements

## Terminologie

### Entrepôt

Dans Konvergo ERP, un **Entrepôt** est le bâtiment/l’endroit actuel où les articles
d’une entreprise sont stockés. Vous pouvez configurer plusieurs entrepôts dans
Konvergo ERP et l’utilisateur peut créer des mouvements entre les entrepôts.

### Emplacement

Un **Emplacement** est un lieu spécifique dans l’entrepôt. Il peut s’agir d’un
sous-emplacement de l’entrepôt (une étagère, un étage, une allée, etc.). Par
conséquent, un emplacement fait partie d’un seul entrepôt et il est impossible
de lier un emplacement à plusieurs entrepôts. Dans Konvergo ERP, autant d’emplacements
que nécessaire peuvent être configurés dans un même entrepôt.

Il y a trois types d’emplacements :

  * Les **Emplacements physiques** sont des emplacements internes qui font partie des entrepôts que l’entreprise possède. Il peut s’agir des zones de chargement et de déchargement de l’entrepôt, d’une étagère, d’un département, etc.

  * Les **Emplacements partenaires** sont des zones dans un entrepôt d’un client et/ou d’un fournisseur. Ils fonctionnent de la même manière que les emplacements physiques, à la seule différence qu’ils n’appartiennent pas à la société de l’utilisateur.

  * Les **Emplacements virtuels** sont des zones qui n’existent pas, mais où les produits peuvent être placés lorsqu’ils ne se trouvent pas encore (ou plus) physiquement dans un inventaire. Ils sont utiles pour enregistrer les produits perdus (**Perte d’inventaire**) ou pour comptabiliser les produits qui sont en route vers l’entrepôt (**Approvisionnements**).

Dans Konvergo ERP, les emplacements sont organisés hiérarchiquement. Vous pouvez
organiser vos emplacements comme une arborescence, avec des relations parent-
enfant. Cela vous donne des niveaux plus détaillés de l’analyse des opérations
de stock et de l’organisation de vos entrepôts.

## Configuration

Pour activer les emplacements, allez à Configuration ‣ Paramètres et activez
**Emplacements de stockage**. Cliquez ensuite sur **Enregistrer**.

![Activer la fonctionnalité des emplacements de stockage dans les paramètres
d'Konvergo ERP Inventaire.](../../../../../_images/storage-location-warehouse-
setting.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To manage several routes within the warehouses, also enable <b>Multi-Step Routes</b> and
check <a href="use_routes">Routes and push/pull rules</a>.</p>
</div>

## Créer un nouvel entrepôt

Pour créer un entrepôt, allez à Configuration ‣ Gestion de l’entrepôt ‣
Entrepôts et cliquez sur **Créer**.

Complétez ensuite un **Nom d’entrepôt** et un **Nom court**. Le nom court
comporte cinq caractères au maximum.

![Champ nom court d'un entrepôt dans Konvergo ERP
Inventaire.](../../../../../_images/create-new-warehouse.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le <b>Nom court</b> apparaît sur les ordres de transfert et les autres documents d’entrepôt. Konvergo ERP recommande d’utiliser un nom compréhensible comme « WH/[premières lettres du lieu] ».</p>
</div>

À présent, retournez au tableau de bord de l”**Inventaire**. Vous y verrez que
les nouvelles opérations liées à l’entrepôt nouvellement créé ont été
automatiquement générées.

![Le tableau de bord de l'application Inventaire affichant les nouveaux types
de transfert pour l'entrepôt nouvellement créé.](../../../../../_images/new-
transfer-types.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’ajout d’un deuxième entrepôt activera automatiquement le paramètre <b>Emplacements</b>.</p>
</div>

## Créer un nouvel emplacement

Pour créer un emplacement, allez à Configuration ‣ Gestion de l’entrepôt ‣
Emplacements et cliquez sur **Créer**.

Complétez ensuite un **Nom d’emplacement** et un **Emplacement parent** et
cliquez sur **Enregistrer**.

![Créer un nouvel emplacement d'entrepôt dans Konvergo ERP
Inventaire.](../../../../../_images/create-new-location.png)

