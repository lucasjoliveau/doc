# Modèles, modules et applications

Les modèles déterminent la structure logique d’une base de données et la
manière dont les données sont stockées, organisées et manipulées. En d’autres
termes, un modèle est un tableau d’informations qui peut être lié à d’autres
tableaux. Un modèle représente généralement un concept commercial tel qu’une
_commande_ , un _contact_ ou un _produit_.

Les modules et les applications contiennent plusieurs éléments, tels que des
modèles, des vues, des fichiers de données, des contrôleurs web et des données
web statistiques.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Toutes les applications sont des modules. Les modules autonomes de plus grande taille sont généralement appelés applications, tandis que les autres modules servent généralement de compléments à ces applications.</p>
</div>

## Fonctionnalités suggérées

Lorsque vous créez un nouveau modèle ou une nouvelle application avec Studio,
vous pouvez choisir d’ajouter jusqu’à 14 fonctionnalités pour accélérer le
processus de création. Ces fonctionnalités regroupent des champs, des
paramètres par défaut et des vues qui sont généralement utilisés ensemble pour
fournir une fonctionnalité standard. La plupart de ces fonctionnalités peuvent
être ajoutées ultérieurement, mais le fait de les ajouter dès le départ
facilite grandement le processus de création des modèles. De plus, dans
certains cas, ces fonctionnalités interagissent entre elles afin d’accroître
leur utilité.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Créer un modèle avec les fonctionnalités <a href="#studio-models-modules-apps-suggested-features-picture"><span class="std std-ref">Image</span></a> et <a href="#studio-models-modules-apps-suggested-features-pipeline-stages"><span class="std std-ref">Étapes de pipeline</span></a> activées permet d’ajouter l’image dans la disposition des cartes de la <a href="views#studio-views-multiple-records-kanban"><span class="std std-ref">vue Kanban</span></a>.</p>
<img alt="Combinaison des fonctionnalités d'image et d'étapes de pipeline dans la vue Kanban" class="align-center" src="../../_images/picture-pipeline-kanban.png"/>
</div>

### Détails de contact

Sélectionner **Détails de contact** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) un [champ
Many2One](fields#studio-fields-relational-fields-many2one) lié au module
_Contact_ et deux de ses [champs associés](fields#studio-fields-
relational-fields-related-field) : **Téléphone** et **Email**. Le champ
**Contact** est également ajouté à la [vue Liste](views#studio-views-
multiple-records-list) et la [vue Carte](views#studio-views-multiple-
records-map) est activée.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Fonctionnalité des détails de contact sur la vue Formulaire" class="align-center" src="../../_images/contact1.png"/>
</div>

### Assignation à un utilisateur

Sélectionner **Assignation à un utilisateur** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) un [champ
Many2One](fields#studio-fields-relational-fields-many2one) lié au modèle
de _Contact_ , avec le **Domaine** suivant : `Partage de l'utilisateur n'est
pas défini` pour uniquement permettre la sélection d” _Utilisateurs internes_.
De plus, le widget **many2one_avatar_user** est utilisé pour afficher l’avatar
de l’utilisateur. Le champ **Responsable** est également ajouté à la [vue
Liste](views#studio-views-multiple-records-list).

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Fonctionnalité de l'assignation à un utilisateur dans la vue Formulaire" class="align-center" src="../../_images/user-assignment.png"/>
</div>

### Date & Calendrier

Sélectionner **Date & Calendrier** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) un [champ de
Date](fields#studio-fields-simple-fields-date) et activer la [vue
Calendrier](views#studio-views-timeline-calendar).

### Plage de dates & Gantt

Sélectionner **Plage de dates & Gantt** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) deux [champs de
Date](fields#studio-fields-simple-fields-date) l’un à côté de l’autre :
un pour définir une date de début et l’autre pour définir une date de fin, en
utilisant le widget **daterange** et d’activer la [vue
Gantt](views#studio-views-timeline-gantt).

### Étapes de pipeline

Sélectionner **Étapes de pipeline** permet d’activer la [vue
Kanban](views#studio-views-multiple-records-kanban) et d’ajouter
plusieurs champs tels que [Priorité](fields#studio-fields-simple-fields-
priority) et **Statut Kanban** , ainsi que trois étapes : **Nouveau** , **En
cours** et **Fait**. Les champs **Barre d’état du pipeline** et **Statut
Kanban** sont ajoutés à la [vue Formulaire](views#studio-views-general-
form). Le champ **Couleur** est ajouté à la [vue Liste](views#studio-
views-multiple-records-list).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La fonctionnalité des <b>Étapes de pipeline</b> peut être ajoutée ultérieurement.</p>
</div>

### Étiquettes

Sélectionner **Étiquettes** permet d’ajouter aux vues
[Formulaire](views#studio-views-general-form) et
[Liste](views#studio-views-multiple-records-list) un [champ
Étiquettes](fields#studio-fields-relational-fields-tags), ce qui crée un
modèle _Étiquette_ avec des droits d’accès préconfigurés.

### Image

Sélectionner **Image** permet d’ajouter un [champ Image](fields#studio-
fields-simple-fields-image) dans le coin supérieur droit de la [vue
Formulaire](views#studio-views-general-form).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La fonctionnalité <b>Image</b> peut être ajoutée ultérieurement.</p>
</div>

### Lignes

Sélectionner **Lignes** : permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) un [champ
Lignes](fields#studio-fields-relational-fields-lines) à l’intérieur d’un
composant **Onglet**.

### Notes

Sélectionner **Notes** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) un [champ
Html](fields#studio-fields-simple-fields-html) utilisant toute la largeur
du formulaire.

### Valeur monétaire

Sélectionner **Valeur monétaire** permet d’ajouter aux vues
[Formulaire](views#studio-views-general-form) et
[Liste](views#studio-views-multiple-records-list) un [champ
Monétaire](fields#studio-fields-simple-fields-monetary). Les vues
[Graphique](views#studio-views-reporting-graph) et [Tableau croisé
dynamique](views#studio-views-reporting-pivot) sont également activées.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Un champ <em>Devise</em> est ajouté et masqué à la vue.</p>
</div>

### Société

Sélectionner **Société** permet d’ajouter aux vues
[Formulaire](views#studio-views-general-form) et
[Liste](views#studio-views-multiple-records-list) un [champ
Many2One](fields#studio-fields-relational-fields-many2one) lié au modèle
de _Société_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cela n’est utile que si vous travaillez dans un environnement multi-sociétés.</p>
</div>

### Tri personnalisé

Sélectionner **Tri personnalisé** permet d’ajouter à la [vue
Liste](views#studio-views-multiple-records-list) une icône de poignée de
déplacement pour manuellement réorganiser les enregistrements.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Fonctionnalité de tri personnalisé dans la vue Liste" class="align-center" src="../../_images/list-drag-handle.png"/>
</div>

### Chatter

Sélectionner **Chatter** permet d’ajouter à la [vue
Formulaire](views#studio-views-general-form) des fonctionnalités de
chatter (envoi de messages, publication de notes et planification
d’activités).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La fonctionnalité <b>Chatter</b> peut être ajoutée ultérieurement.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Créer un modèle avec les fonctionnalités <a href="#studio-models-modules-apps-suggested-features-picture"><span class="std std-ref">Image</span></a> et <a href="#studio-models-modules-apps-suggested-features-pipeline-stages"><span class="std std-ref">Étapes de pipeline</span></a> activées permet d’ajouter l’image dans la disposition des cartes de la <a href="views#studio-views-multiple-records-kanban"><span class="std std-ref">vue Kanban</span></a>.</p>
<img alt="Combinaison des fonctionnalités d'image et d'étapes de pipeline dans la vue Kanban" class="align-center" src="../../_images/picture-pipeline-kanban.png"/>
</div>0

### Archivage

Sélectionner **Archivage** permet d’ajouter aux vues
[Formulaire](views#studio-views-general-form) et
[Liste](views#studio-views-multiple-records-list) l’action **Archiver**
et de masquer les enregistrements archivés des recherches et des vues par
défaut.

## Exporter et importer des personnalisations

Lorsque vous effectuez une personnalisation avec Studio, un nouveau module
intitulé **Personnalisations Studio** est ajouté à votre base de données.

Pour exporter ces personnalisations, allez au Tableau de bord principal ‣
Studio ‣ Personnalisations ‣ Exporter pour télécharger un fichier ZIP
contenant toutes les personnalisations.

Pour importer et installer ces personnalisations dans une autre base de
données, connectez la base de données de destination et allez au Tableau de
bord principal ‣ Studio ‣ Personnalisations ‣ Importer et chargez le fichier
ZIP exporté avant de cliquer sur le bouton **Importer**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Créer un modèle avec les fonctionnalités <a href="#studio-models-modules-apps-suggested-features-picture"><span class="std std-ref">Image</span></a> et <a href="#studio-models-modules-apps-suggested-features-pipeline-stages"><span class="std std-ref">Étapes de pipeline</span></a> activées permet d’ajouter l’image dans la disposition des cartes de la <a href="views#studio-views-multiple-records-kanban"><span class="std std-ref">vue Kanban</span></a>.</p>
<img alt="Combinaison des fonctionnalités d'image et d'étapes de pipeline dans la vue Kanban" class="align-center" src="../../_images/picture-pipeline-kanban.png"/>
</div>1

