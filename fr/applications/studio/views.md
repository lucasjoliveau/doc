# Vues

Les vues sont l’interface qui permet d’afficher les données contenues dans un
modèle. Un modèle peut avoir plusieurs vues, qui sont simplement des façons
différentes de présenter les mêmes données. Dans Studio, les vues sont
organisées en quatre catégories : général, enregistrements multiples, ligne du
temps, et analyse.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour modifier la vue par défaut d’un modèle, allez à Studio ‣ Vues ‣ Menu déroulant (⋮) ‣ Définir par défaut.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>

## Vues générales

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous l’onglet <b>Vue</b> de la vue.</p>
</div>

### Formulaire

La vue **Formulaire** est utilisé lors de la création et de l’édition
d’enregistrements, tels que des contacts, des commandes, des produits, etc.

  * Pour structurer un formulaire, glissez et déposez l’élément **Onglets et Colonnes** que vous pouvez trouver sous l’onglet **\+ Ajouter**.

  * Pour empêcher les utilisateurs de créer, d’modifier ou de supprimer des enregistrements, décochez les cases à côté de **Peut créer** , **Peut modifier** ou **Peut supprimer**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Vue formulaire d'un modèle de commande" class="align-center" src="../../_images/form-sales-order.png"/>
</div>

### Activité

La vue **Activité** permet de programmer et d’obtenir une vue d’ensemble des
activités (emails, appels, etc.) liées aux enregistrements.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est uniquement possible de modifier cette vue dans Studio en éditant le code XML.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Vue Activité d'un modèle de piste/opportunité" class="align-center" src="../../_images/activity-lead-opportunity.png"/>
</div>

### Rechercher

La vue **Rechercher** s’ajoute aux autres vues afin de filtrer, regrouper et
chercher des enregistrements.

  * Pour ajouter des **Filtres** personnalisés et les structurer à l’aide de **Séparateurs** , allez à l’onglet **\+ Ajouter** et glissez et déposez-les sous **Filtres**.

  * Pour ajouter un champ existant sous le menu déroulant de recherche, allez à l’onglet **\+ Ajouter** et glissez et déposez-le sous **Champs d’autocomplétion**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="La vue Rechercher d'un modèle de projet dans la vue Kanban" class="align-center" src="../../_images/search-project-kanban.png"/>
</div>

## Vues avec enregistrements multiples

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous l’onglet <b>Vue</b> de la vue.</p>
</div>

### Kanban

La vue **Kanban** est souvent utilisée pour soutenir les flux d’activité en
déplaçant les enregistrements d’une étape à l’autre ou comme moyen alternatif
d’afficher les enregistrements à l’intérieur de _cartes_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si la vue <b>Kanban</b> existe, elle est utilisée par défaut pour afficher les données sur les appareils mobiles à la place de la <a href="#studio-views-multiple-records-list"><span class="std std-ref">vue Liste</span></a>.</p>
</div>

  * Pour empêcher les utilisateurs de créer de nouveaux enregistrements, décochez **Peut créer**.

  * Pour créer des enregistrements directement dans la vue, sous une forme minimaliste, activez la **Création rapide**.

  * Pour modifier la manière dont les enregistrements sont regroupés par défaut, sélectionnez un nouveau groupe sous **Regrouper par défaut par**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>0

### Liste

La vue **Liste** permet de visualiser de nombreux enregistrements à la fois,
de rechercher des enregistrements et d’modifier des enregistrements simples.

  * Pour empêcher les utilisateurs de créer, d’modifier ou de supprimer des enregistrements, décochez les cases à côté de **Peut créer** , **Peut modifier** ou **Peut supprimer**.

  * Pour créer et modifier des enregistrements directement dans la vue, sélectionnez soit **Nouvel enregistrement en haut** , soit **Nouvel enregistrement en bas** sous **Éditable**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>1

  * Pour modifier plusieurs enregistrements à la fois, cochez la case à côté d”**Activer l’édition en masse**.

  * Pour modifier la manière dont les enregistrements sont triés par défaut, sélectionnez un champ sous **Trier par**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>3

### Carte

La vue **Carte** permet d’afficher des enregistrements sur une carte. Par
exemple, elle est utilisée dans l’application Services sur site pour planifier
un itinéraire entre différentes tâches.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>4

  * Pour sélectionner le type de contact à utiliser sur la carte, sélectionnez-le sous le **champ Contact**.

  * Pour masquer le nom ou l’adresse de l’enregistrement, cochez **Masquer le nom** ou **Masquer l’adresse**.

  * Pour ajouter des informations provenant d’autres champs, sélectionnez-les sous **Champs supplémentaires**.

  * Pour qu’une route soit suggérée entre les différents enregistrements, cochez **Activer le routage** et sélectionnez le champ à utiliser pour trier les enregistrements en vue du routage.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>5

## Vues de ligne du temps

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>6

### Calendrier

La vue **Calendrier** est utilisée pour présenter et gérer les enregistrements
dans un calendrier.

  * Pour créer des enregistrements directement dans la vue au lieu d’ouvrir la vue Formulaire, activez la **création rapide**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>7

  * Pour mettre en couleur des enregistrements dans le calendrier, sélectionnez un champ sous **Couleur**. Tous les enregistrements partageant la même valeur pour ce champ sont affichés dans la même couleur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>8

  * Pour afficher les événements qui durent toute la journée en haut du calendrier, sélectionnez un [champ Case à cocher](fields#studio-fields-simple-fields-checkbox) qui indique que l’événement dure toute la journée.

  * Pour choisir l’échelle de temps par défaut utilisée pour afficher les événements, sélectionnez **Jour** , **Semaine** , **Mois** ou **Année** sous le **Mode d’affichage par défaut**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce faire, activez le <a href="../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez à la vue que vous souhaitez modifier, sélectionnez l’onglet <b>Vue</b> et cliquez ensuite sur <b>&lt;/&gt; XML</b>.</p>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>
</div>9 <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>0

### Cohorte

La vue **Cohorte** permet d’examiner le cycle de vie des enregistrements sur
une période donnée. Par exemple, elle est utilisée dans l’application
Abonnements pour afficher le taux de rétention des abonnements.

  * Pour afficher une mesure (c’est-à-dire la valeur agrégée d’un certain champ) par défaut sur la vue, sélectionnez un **Champ de mesure**.

  * Pour choisir l’intervalle de temps utilisé par défaut pour regrouper les résultats, sélectionnez **Jour** , **Semaine** , **Mois** ou **Année** sous **Intervalle**.

  * Pour modifier le **Mode** cohorte, sélectionnez soit **Rétention** le pourcentage d’enregistrements qui restent sur une période de temps, commençant à 100% et diminuant avec le temps, soit **Attrition** le pourcentage d’enregistrements qui quittent sur une période donnée, commençant à 0% et augmentant avec le temps.

  * Pour modifier la progression de la **Ligne de temps** (c’est-à-dire, les colonnes), sélectionnez soit **En avant** (de 0 à +15), soit **En arrière** (de -15 à 0). Dans la plupart des cas, c’est la ligne de temps **en avant** qui est utilisée.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>1

### Gantt

La vue **Gantt** permet de prévoir et examiner la progression globale des
enregistrements. Les enregistrements sont représentés par une barre sous une
échelle de temps.

  * Pour empêcher les utilisateurs de créer ou modifier des enregistrements, décocher **Peut créer** ou **Peut modifier**.

  * Pour remplir les cellules en gris lorsqu’un enregistrement ne doit pas y être créé (par ex. le week-end pour les employés), cochez **Afficher l’indisponibilité**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>2

  * Pour afficher une ligne de total au bas de l’écran, cochez **Afficher une ligne de total**.

  * Pour réduire plusieurs enregistrements dans une seule ligne, cochez **Réduire le premier niveau**.

  * Pour choisir de quelle manière dont les enregistrements sont regroupés par défaut sur les lignes (par ex. par employé ou par projet), sélectionnez un champ sous **Regrouper par défaut par**.

  * Pour définir une échelle de temps par défaut pour afficher des enregistrements, sélectionnez **Jour** , **Semaine** , **Mois** ou **Année** sous **Échelle par défaut**.

  * Pour mettre en couleur les enregistrements sur la vue, sélectionnez un champ sous **Couleur**. Tous les enregistrements partageant la même valeur pour ce champ sont affichés dans la même couleur.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>3

  * Pour spécifier le degré de précision avec lequel chaque échelle de temps doit être divisée, sélectionnez **Quart d’heure** , **Demi-heure** ou **Heure** sous **Précision du jour** , **Demi-journée** ou **Jour** sous **Précision de semaine** et **Précision de mois**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>4

## Vues d’analyse

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>5

### Tableau croisé dynamique

La vue **Tableau croisé dynamique** permet d’explorer et analyser les données
contenues dans les enregistrements de manière interactive. Elle est
particulièrement utile pour agréger des données numériques, créer des
catégories et explorer des données en développant et en réduisant différents
niveaux de données.

  * Pour accéder à tous les enregistrements dont les données sont agrégées dans une cellule, cochez **Accéder aux enregistrements depuis la cellule**.

  * Pour diviser les données en différentes catégories, sélectionnez le ou les champs sous **Regroupement de colonnes** , **Regroupement de lignes - Premier niveau** ou **Regroupement de lignes - Deuxième niveau**.

  * Pour ajouter différents types de données à mesurer à l’aide de la vue, sélectionnez un champ sous **Mesures**.

  * Pour afficher le nombre d’enregistrements composant les données agrégées dans une cellule, cochez **Afficher le nombre**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>6

### Graphique

La vue **Graphique** permet de présenter les données des enregistrements sous
forme de graphique à barres, linéaire ou circulaire.

  * Pour modifier le graphique par défaut, sélectionnez **Barres** , **Linéaire** ou **Circulaire** sous **Type**.

  * Pour choisir une dimension de données par défaut (catégorie), sélectionnez un champ sous **Première dimension** et, le cas échéant, un autre sous **Deuxième dimension**.

  * Pour sélectionner un type de données à mesurer par défaut à l’aide de la vue, sélectionnez un champ sous **Mesure**.

  * _Uniquement pour les graphiques à barres et linéaires_ : Pour trier les différentes catégories de données en fonction de leur valeur, sélectionnez **Ascendant** (de la valeur la plus faible à la valeur la plus élevée) ou **Descendant** (de la valeur la plus élevée à la valeur la plus faible) sous **Tri**.

  * _Uniquement pour les graphiques à barres ou circulaires_ : Pour accéder à tous les enregistrements dont les données sont agrégées sous une catégorie de données sur le graphique, cochez **Accéder aux enregistrements depuis le graphique**.

  * _Uniquement pour les graphiques à barres_ : Lorsque vous utilisez deux dimensions de données (catégories), affichez les deux colonnes l’une au-dessus de l’autre par défaut en cochant **Graphique empilé**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>7

### Tableau de bord

La vue **Tableau de bord** permet d’afficher plusieurs vues d’analyse et
indicateurs clés de performance. Les éléments qui sont affichés sur la vue
dépendent de la configuration des autres vues d’analyse.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier directement les vues standards et les vues héritées, car elles seraient réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et déposant un nouveau champ, une vue héritée Studio spécifique et son XPath, définissant quelle partie de la vue est modifiée, sont automatiquement générés.</p>
</div>8

