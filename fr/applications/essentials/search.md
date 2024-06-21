# Rechercher et filtrer des enregistrements

Konvergo ERP utilise des filtres pour uniquement inclure les enregistrements les plus
importants en fonction de l’objectif de la vue sur laquelle vous vous trouvez.
Cependant, vous pouvez modifier le filtre par défaut ou rechercher des valeurs
spécifiques.

## Filtres préconfigurés

Vous pouvez modifier la sélection d’enregistrements par défaut en cliquant sur
**Filtres** et en sélectionnant un ou plusieurs **filtres préconfigurés**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Sur le rapport d’analyse des ventes, seuls des enregistrements à l’étape de commande client sont sélectionnés par défaut. Cependant, vous pouvez <em>également</em> inclure des enregistrements à l’étape du devis en sélectionnant les <b>Devis</b>. De plus, vous pouvez <em>uniquement</em> inclure des enregistrements d’une année précise, par exemple <em>2022</em>, en sélectionnant Date de la commande ‣ 2022.</p>
<img alt="Utiliser des filtres préconfigurés dans le rapport d'analyse des ventes" class="align-center" src="../../_images/preconfigured-filters.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous sélectionnez des filtres préconfigurés du même groupe (par ex. qui ne sont <em>pas</em> séparés par une ligne horizontale), les enregistrements peuvent correspondre à <em>n’importe quelle</em> condition pour être inclus. Cependant, si vous sélectionnez des filtres de groupes différents, les enregistrements doivent correspondre à <em>toutes</em> les conditions pour être inclus.</p>
</div>

## Filtres personnalisés

Vous pouvez créer des filtres personnalisés en utilisant la plupart des champs
présents sur le modèle en cliquant sur Filtres ‣ Ajouter un filtre
personnalisé, en sélectionnant un champ, un opérateur, une valeur et en
cliquant sur **Appliquer**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Vous pouvez <em>uniquement</em> inclure des enregistrements d’un seul vendeur dans le rapport d’analyse des ventes, par exemple <em>Mitchell Admin</em>, en sélectionnant le champ <b>vendeur</b>, l’opérateur <b>est égal à</b> et la valeur <code>Mitchell Admin</code>.</p>
<img alt="Utiliser un filtre personnalisé dans le rapport d'analyse des ventes" class="align-center" src="../../_images/custom-filter.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si les enregistrements doivent <em>seulement</em> correspondre à une condition parmi plusieurs, cliquez sur <b>Ajouter une condition</b> avant d’appliquer un filtre personnalisé. Si les enregistrements doivent correspondre à <em>toutes</em> les conditions, ajoutez plutôt de nouveaux filtres personnalisés.</p>
</div>

## Rechercher des valeurs

Vous pouvez utiliser le champ de recherche pour rechercher rapidement des
valeurs spécifiques et les ajouter comme filtre. Vous pouvez soit écrire la
valeur complète que vous cherchez et sélectionner le champ souhaité, soit
écrire une partie de la valeur, cliquer sur le bouton du menu déroulant
(**⏵**) devant le champ choisi et sélectionner la valeur exacte que vous
cherchez.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Au lieu d’ajouter un filtre personnalisé pour sélectionner des enregistrements pour lesquels <em>Mitchell Admin</em> est le vendeur sur le rapport d’analyse des ventes, vous pouvez écrire <code>Mitch</code>, cliquer sur le bouton du menu déroulant (<b>⏵</b>) à côté de <b>Rechercher Vendeur pour: Mitch</b>, et sélectionner <b>Mitchell Admin</b>.</p>
<img alt="Rechercher une valeur spécifique dans le rapport d'analyse des ventes" class="align-center" src="../../_images/search-values.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’utilisation du champ de recherche équivaut à l’utilisation de l’opérateur <em>contient</em> lorsque vous ajoutez un filtre personnalisé. Si vous saisissiez une valeur partielle et sélectionnez directement le champ souhaité, <em>tous</em> les enregistrements contenant les caractères que vous avez saisis pour le champ sélectionné seront inclus.</p>
</div>

## Regrouper des enregistrements

Vous pouvez cliquer sur **Regrouper par** en dessous du champ de recherche
pour regrouper des enregistrements en fonction d’un des **groupes
préconfigurés**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Vous pouvez regrouper les enregistrements par vendeur sur le rapport d’analyse des ventes en cliquant sur <b>Regrouper par</b> et en sélectionnant <b>Vendeur</b>. Aucun enregistrement n’est filtré.</p>
<img alt="Regrouper des enregistrements sur le rapport de vente des analyses" class="align-center" src="../../_images/group.png"/>
</div>

Vous pouvez **personnaliser les groupes** en utilisant une large sélection de
champs présents sur le modèle. Pour ce faire, cliquez sur Regrouper par ‣
Ajouter un groupe personnalisé, sélectionnez un champ et cliquez sur
**Appliquer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez utiliser plusieurs groupes en même temps. Le premier groupe sélectionné est le cluster principal, le suivant divise davantage les catégories du groupe principal, et ainsi de suite.</p>
</div>

