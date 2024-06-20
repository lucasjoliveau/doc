# Vues

Les vues sont l’interface qui permet d’afficher les données contenues dans un
modèle. Un modèle peut avoir plusieurs vues, qui sont simplement des façons
différentes de présenter les mêmes données. Dans Studio, les vues sont
organisées en quatre catégories : général, enregistrements multiples, ligne du
temps, et analyse.

Astuce

Pour modifier la vue par défaut d’un modèle, allez à Studio ‣ Vues ‣ Menu
déroulant (⋮) ‣ Définir par défaut.

Note

Vous pouvez modifier des vues en utilisant l’éditeur XML intégré. Pour ce
faire, activez le [mode développeur](../general/developer_mode.html#developer-
mode), allez à la vue que vous souhaitez modifier, sélectionnez l’onglet Vue
et cliquez ensuite sur </> XML.

Important

Si vous modifiez une vue à l’aide de l’éditeur XML, évitez de modifier
directement les vues standards et les vues héritées, car elles seraient
réinitialisées et ne seraient pas conservées en cas de mise à jour ou de mise
à niveau du module. Veillez toujours à sélectionner les bonnes vues héritées
de Studio. En effet, lorsque vous modifiez une vue dans Studio en glissant et
déposant un nouveau champ, une vue héritée Studio spécifique et son XPath,
définissant quelle partie de la vue est modifiée, sont automatiquement
générés.

## Vues générales

Note

Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous
l’onglet Vue de la vue.

### Formulaire

La vue Formulaire est utilisé lors de la création et de l’édition
d’enregistrements, tels que des contacts, des commandes, des produits, etc.

  * Pour structurer un formulaire, glissez et déposez l’élément Onglets et Colonnes que vous pouvez trouver sous l’onglet \+ Ajouter.

  * Pour empêcher les utilisateurs de créer, d’modifier ou de supprimer des enregistrements, décochez les cases à côté de Peut créer, Peut modifier ou Peut supprimer.

Example

![Vue formulaire d'un modèle de commande](../../_images/form-sales-order.png)

### Activité

La vue Activité permet de programmer et d’obtenir une vue d’ensemble des
activités (emails, appels, etc.) liées aux enregistrements.

Note

Il est uniquement possible de modifier cette vue dans Studio en éditant le
code XML.

Example

![Vue Activité d'un modèle de piste/opportunité](../../_images/activity-lead-
opportunity.png)

### Rechercher

La vue Rechercher s’ajoute aux autres vues afin de filtrer, regrouper et
chercher des enregistrements.

  * Pour ajouter des Filtres personnalisés et les structurer à l’aide de Séparateurs, allez à l’onglet \+ Ajouter et glissez et déposez-les sous Filtres.

  * Pour ajouter un champ existant sous le menu déroulant de recherche, allez à l’onglet \+ Ajouter et glissez et déposez-le sous Champs d’autocomplétion.

Example

![La vue Rechercher d'un modèle de projet dans la vue
Kanban](../../_images/search-project-kanban.png)

## Vues avec enregistrements multiples

Note

Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous
l’onglet Vue de la vue.

### Kanban

La vue Kanban est souvent utilisée pour soutenir les flux d’activité en
déplaçant les enregistrements d’une étape à l’autre ou comme moyen alternatif
d’afficher les enregistrements à l’intérieur de _cartes_.

Note

Si la vue Kanban existe, elle est utilisée par défaut pour afficher les
données sur les appareils mobiles à la place de la vue Liste.

  * Pour empêcher les utilisateurs de créer de nouveaux enregistrements, décochez Peut créer.

  * Pour créer des enregistrements directement dans la vue, sous une forme minimaliste, activez la Création rapide.

  * Pour modifier la manière dont les enregistrements sont regroupés par défaut, sélectionnez un nouveau groupe sous Regrouper par défaut par.

Example

![Vue kanban d'un modèle de projet](../../_images/kanban-project.png)

### Liste

La vue Liste permet de visualiser de nombreux enregistrements à la fois, de
rechercher des enregistrements et d’modifier des enregistrements simples.

  * Pour empêcher les utilisateurs de créer, d’modifier ou de supprimer des enregistrements, décochez les cases à côté de Peut créer, Peut modifier ou Peut supprimer.

  * Pour créer et modifier des enregistrements directement dans la vue, sélectionnez soit Nouvel enregistrement en haut, soit Nouvel enregistrement en bas sous Éditable.

Note

Cela empêche les utilisateurs d’ouvrir des enregistrements dans la vue
Formulaire à partir de la vue Liste.

  * Pour modifier plusieurs enregistrements à la fois, cochez la case à côté d”Activer l’édition en masse.

  * Pour modifier la manière dont les enregistrements sont triés par défaut, sélectionnez un champ sous Trier par.

Astuce

Pour ajouter une icône de déplacement afin de manuellement réorganiser les
enregistrements, ajoutez un [champ entier](fields.html#studio-fields-simple-
fields-integer) avec le widget Poignée.

![Icône de poignée de déplacement permettant de trier les enregistrements
manuellement dans la vue Liste](../../_images/list-drag-handle.png)

Example

![Vue Liste d'un modèle de commande](../../_images/list-sales-order.png)

### Carte

La vue Carte permet d’afficher des enregistrements sur une carte. Par exemple,
elle est utilisée dans l’application Services sur site pour planifier un
itinéraire entre différentes tâches.

Note

Un [champ Many2One](fields.html#studio-fields-relational-fields-many2one) lié
au modèle _Contact_ est requis pour activer la vue, car l’adresse du contact
est utilisée pour positionner les enregistrements sur la carte.

  * Pour sélectionner le type de contact à utiliser sur la carte, sélectionnez-le sous le champ Contact.

  * Pour masquer le nom ou l’adresse de l’enregistrement, cochez Masquer le nom ou Masquer l’adresse.

  * Pour ajouter des informations provenant d’autres champs, sélectionnez-les sous Champs supplémentaires.

  * Pour qu’une route soit suggérée entre les différents enregistrements, cochez Activer le routage et sélectionnez le champ à utiliser pour trier les enregistrements en vue du routage.

Example

![Vue Carte du modèle de tâche](../../_images/map-task.png)

## Vues de ligne du temps

Note

  * Lorsque vous activez l’une des vues de ligne de temps pour la première fois, vous devez sélectionner les champs [Date](fields.html#studio-fields-simple-fields-date) ou [Date & Heure](fields.html#studio-fields-simple-fields-date-time) sur votre modèle qui doivent être utilisés pour définir quand les enregistrements commencent et s’arrêtent afin de les afficher dans la vue. Vous pouvez modifier le Champ de date de début et le Champ de date de fin après avoir activé la vue.

  * Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous l’onglet Vue de la vue.

### Calendrier

La vue Calendrier est utilisée pour présenter et gérer les enregistrements
dans un calendrier.

  * Pour créer des enregistrements directement dans la vue au lieu d’ouvrir la vue Formulaire, activez la création rapide.

Note

Cette option ne fonctionne que sur des modèles spécifiques qui peuvent être
_créés rapidement_ à l’aide d’un simple _nom_. Cependant, la plupart des
modèles ne prennent pas en charge la création rapide et ouvrent la vue
Formulaire pour compléter les champs requis.

  * Pour mettre en couleur des enregistrements dans le calendrier, sélectionnez un champ sous Couleur. Tous les enregistrements partageant la même valeur pour ce champ sont affichés dans la même couleur.

Note

Puisque le nombre de couleurs est limité, une même couleur peut être attribuée
à des valeurs différentes.

  * Pour afficher les événements qui durent toute la journée en haut du calendrier, sélectionnez un [champ Case à cocher](fields.html#studio-fields-simple-fields-checkbox) qui indique que l’événement dure toute la journée.

  * Pour choisir l’échelle de temps par défaut utilisée pour afficher les événements, sélectionnez Jour, Semaine, Mois ou Année sous le Mode d’affichage par défaut.

Note

Vous pouvez également utiliser un Champ de délai pour afficher la durée de
l’événement en heures en sélectionnant un champ [Décimale](fields.html#studio-
fields-simple-fields-decimal) ou [Entier](fields.html#studio-fields-simple-
fields-integer) sur le modèle qui précise la durée de l’événement. Cependant,
si vous définissez un champ de date de fin, le champ de délai ne sera pas pris
en compte.

Example

![Vue Calendrier du modèle d'un événement](../../_images/calendar-event.png)

### Cohorte

La vue Cohorte permet d’examiner le cycle de vie des enregistrements sur une
période donnée. Par exemple, elle est utilisée dans l’application Abonnements
pour afficher le taux de rétention des abonnements.

  * Pour afficher une mesure (c’est-à-dire la valeur agrégée d’un certain champ) par défaut sur la vue, sélectionnez un Champ de mesure.

  * Pour choisir l’intervalle de temps utilisé par défaut pour regrouper les résultats, sélectionnez Jour, Semaine, Mois ou Année sous Intervalle.

  * Pour modifier le Mode cohorte, sélectionnez soit Rétention le pourcentage d’enregistrements qui restent sur une période de temps, commençant à 100% et diminuant avec le temps, soit Attrition le pourcentage d’enregistrements qui quittent sur une période donnée, commençant à 0% et augmentant avec le temps.

  * Pour modifier la progression de la Ligne de temps (c’est-à-dire, les colonnes), sélectionnez soit En avant (de 0 à +15), soit En arrière (de -15 à 0). Dans la plupart des cas, c’est la ligne de temps en avant qui est utilisée.

Example

![Vue cohorte du modèle d'abonnement](../../_images/cohort-subscription.png)

### Gantt

La vue Gantt permet de prévoir et examiner la progression globale des
enregistrements. Les enregistrements sont représentés par une barre sous une
échelle de temps.

  * Pour empêcher les utilisateurs de créer ou modifier des enregistrements, décocher Peut créer ou Peut modifier.

  * Pour remplir les cellules en gris lorsqu’un enregistrement ne doit pas y être créé (par ex. le week-end pour les employés), cochez Afficher l’indisponibilité.

Note

Le modèle sous-jacent doit prendre en charge cette fonctionnalité, qui ne peut
pas être ajoutée à l’aide de Studio. Elle est prise en charge pour les
applications Projet, Congés, Planification et Fabrication.

  * Pour afficher une ligne de total au bas de l’écran, cochez Afficher une ligne de total.

  * Pour réduire plusieurs enregistrements dans une seule ligne, cochez Réduire le premier niveau.

  * Pour choisir de quelle manière dont les enregistrements sont regroupés par défaut sur les lignes (par ex. par employé ou par projet), sélectionnez un champ sous Regrouper par défaut par.

  * Pour définir une échelle de temps par défaut pour afficher des enregistrements, sélectionnez Jour, Semaine, Mois ou Année sous Échelle par défaut.

  * Pour mettre en couleur les enregistrements sur la vue, sélectionnez un champ sous Couleur. Tous les enregistrements partageant la même valeur pour ce champ sont affichés dans la même couleur.

Note

Puisque le nombre de couleurs est limité, une même couleur peut être attribuée
à des valeurs différentes.

  * Pour spécifier le degré de précision avec lequel chaque échelle de temps doit être divisée, sélectionnez Quart d’heure, Demi-heure ou Heure sous Précision du jour, Demi-journée ou Jour sous Précision de semaine et Précision de mois.

Example

![Vue Gantt du modèle de planification d'un poste](../../_images/gantt-
planning.png)

## Vues d’analyse

Note

Sauf indication contraire, les paramètres décrits ci-dessous se trouvent sous
l’onglet Vue de la vue.

### Tableau croisé dynamique

La vue Tableau croisé dynamique permet d’explorer et analyser les données
contenues dans les enregistrements de manière interactive. Elle est
particulièrement utile pour agréger des données numériques, créer des
catégories et explorer des données en développant et en réduisant différents
niveaux de données.

  * Pour accéder à tous les enregistrements dont les données sont agrégées dans une cellule, cochez Accéder aux enregistrements depuis la cellule.

  * Pour diviser les données en différentes catégories, sélectionnez le ou les champs sous Regroupement de colonnes, Regroupement de lignes - Premier niveau ou Regroupement de lignes - Deuxième niveau.

  * Pour ajouter différents types de données à mesurer à l’aide de la vue, sélectionnez un champ sous Mesures.

  * Pour afficher le nombre d’enregistrements composant les données agrégées dans une cellule, cochez Afficher le nombre.

Example

![Vue tableau croisé dynamique d'un modèle de rapport
d'achats](../../_images/pivot-purchase-report.png)

### Graphique

La vue Graphique permet de présenter les données des enregistrements sous
forme de graphique à barres, linéaire ou circulaire.

  * Pour modifier le graphique par défaut, sélectionnez Barres, Linéaire ou Circulaire sous Type.

  * Pour choisir une dimension de données par défaut (catégorie), sélectionnez un champ sous Première dimension et, le cas échéant, un autre sous Deuxième dimension.

  * Pour sélectionner un type de données à mesurer par défaut à l’aide de la vue, sélectionnez un champ sous Mesure.

  * _Uniquement pour les graphiques à barres et linéaires_ : Pour trier les différentes catégories de données en fonction de leur valeur, sélectionnez Ascendant (de la valeur la plus faible à la valeur la plus élevée) ou Descendant (de la valeur la plus élevée à la valeur la plus faible) sous Tri.

  * _Uniquement pour les graphiques à barres ou circulaires_ : Pour accéder à tous les enregistrements dont les données sont agrégées sous une catégorie de données sur le graphique, cochez Accéder aux enregistrements depuis le graphique.

  * _Uniquement pour les graphiques à barres_ : Lorsque vous utilisez deux dimensions de données (catégories), affichez les deux colonnes l’une au-dessus de l’autre par défaut en cochant Graphique empilé.

Example

![Graphique à barres du modèle de rapport d'analyse des ventes dans la vue
Graphique](../../_images/graph-sales-report.png)

### Tableau de bord

La vue Tableau de bord permet d’afficher plusieurs vues d’analyse et
indicateurs clés de performance. Les éléments qui sont affichés sur la vue
dépendent de la configuration des autres vues d’analyse.

Example

![Vue tableau de bord du modèle de rapport d'analyse des
ventes](../../_images/dashboard-sales-report.png)

