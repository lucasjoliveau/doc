# Rechercher et filtrer des enregistrements

Odoo utilise des filtres pour uniquement inclure les enregistrements les plus
importants en fonction de l’objectif de la vue sur laquelle vous vous trouvez.
Cependant, vous pouvez modifier le filtre par défaut ou rechercher des valeurs
spécifiques.

## Filtres préconfigurés

Vous pouvez modifier la sélection d’enregistrements par défaut en cliquant sur
Filtres et en sélectionnant un ou plusieurs **filtres préconfigurés**.

Example

Sur le rapport d’analyse des ventes, seuls des enregistrements à l’étape de
commande client sont sélectionnés par défaut. Cependant, vous pouvez
_également_ inclure des enregistrements à l’étape du devis en sélectionnant
les Devis. De plus, vous pouvez _uniquement_ inclure des enregistrements d’une
année précise, par exemple _2022_ , en sélectionnant Date de la commande ‣
2022.

![Utiliser des filtres préconfigurés dans le rapport d'analyse des
ventes](../../_images/preconfigured-filters.png)

Note

Si vous sélectionnez des filtres préconfigurés du même groupe (par ex. qui ne
sont _pas_ séparés par une ligne horizontale), les enregistrements peuvent
correspondre à _n’importe quelle_ condition pour être inclus. Cependant, si
vous sélectionnez des filtres de groupes différents, les enregistrements
doivent correspondre à _toutes_ les conditions pour être inclus.

## Filtres personnalisés

Vous pouvez créer des filtres personnalisés en utilisant la plupart des champs
présents sur le modèle en cliquant sur Filtres ‣ Ajouter un filtre
personnalisé, en sélectionnant un champ, un opérateur, une valeur et en
cliquant sur Appliquer.

Example

Vous pouvez _uniquement_ inclure des enregistrements d’un seul vendeur dans le
rapport d’analyse des ventes, par exemple _Mitchell Admin_ , en sélectionnant
le champ vendeur, l’opérateur est égal à et la valeur `Mitchell Admin`.

![Utiliser un filtre personnalisé dans le rapport d'analyse des
ventes](../../_images/custom-filter.png)

Note

Si les enregistrements doivent _seulement_ correspondre à une condition parmi
plusieurs, cliquez sur Ajouter une condition avant d’appliquer un filtre
personnalisé. Si les enregistrements doivent correspondre à _toutes_ les
conditions, ajoutez plutôt de nouveaux filtres personnalisés.

## Rechercher des valeurs

Vous pouvez utiliser le champ de recherche pour rechercher rapidement des
valeurs spécifiques et les ajouter comme filtre. Vous pouvez soit écrire la
valeur complète que vous cherchez et sélectionner le champ souhaité, soit
écrire une partie de la valeur, cliquer sur le bouton du menu déroulant (⏵)
devant le champ choisi et sélectionner la valeur exacte que vous cherchez.

Example

Au lieu d’ajouter un filtre personnalisé pour sélectionner des enregistrements
pour lesquels _Mitchell Admin_ est le vendeur sur le rapport d’analyse des
ventes, vous pouvez écrire `Mitch`, cliquer sur le bouton du menu déroulant
(⏵) à côté de Rechercher Vendeur pour: Mitch, et sélectionner Mitchell Admin.

![Rechercher une valeur spécifique dans le rapport d'analyse des
ventes](../../_images/search-values.png)

Note

L’utilisation du champ de recherche équivaut à l’utilisation de l’opérateur
_contient_ lorsque vous ajoutez un filtre personnalisé. Si vous saisissiez une
valeur partielle et sélectionnez directement le champ souhaité, _tous_ les
enregistrements contenant les caractères que vous avez saisis pour le champ
sélectionné seront inclus.

## Regrouper des enregistrements

Vous pouvez cliquer sur Regrouper par en dessous du champ de recherche pour
regrouper des enregistrements en fonction d’un des **groupes préconfigurés**.

Example

Vous pouvez regrouper les enregistrements par vendeur sur le rapport d’analyse
des ventes en cliquant sur Regrouper par et en sélectionnant Vendeur. Aucun
enregistrement n’est filtré.

![Regrouper des enregistrements sur le rapport de vente des
analyses](../../_images/group.png)

Vous pouvez **personnaliser les groupes** en utilisant une large sélection de
champs présents sur le modèle. Pour ce faire, cliquez sur Regrouper par ‣
Ajouter un groupe personnalisé, sélectionnez un champ et cliquez sur
Appliquer.

Note

Vous pouvez utiliser plusieurs groupes en même temps. Le premier groupe
sélectionné est le cluster principal, le suivant divise davantage les
catégories du groupe principal, et ainsi de suite.

