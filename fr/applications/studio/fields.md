# Champs et widgets

Les champs permettent de structurer les modèles d’une base de données. Si vous
imaginez un modèle sous la forme d’un tableau ou d’une feuille de calcul, les
champs sont les colonnes dans lesquelles les données sont stockées dans les
enregistrements (c’est-à-dire les lignes). Les champs définissent également le
type de données qui y sont stockées. La manière dont les données sont
présentées et formatées dans l”UI est déterminée par leur widget.

D’un point de vue technique, il y a 15 types de champ dans Odoo. Toutefois,
vous pouvez choisir parmi 20 champs dans Studio, car certains types de champs
sont disponibles plus d’une fois en appliquant un différent widget par défaut.

Astuce

Il est uniquement possible d’ajouter de Nouveaux champs aux vues
[Formulaire](views.html#studio-views-general-form) et
[Liste](views.html#studio-views-multiple-records-list). Dans les autres vues,
vous ne pouvez ajouter que des Champs existants (champs déjà présents dans le
modèle).

## Champs simples

Les champs simples contiennent des valeurs de base, telles qu’un texte, des
chiffres, des fichiers, etc.

Note

Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont
énumérés sous forme de points ci-dessous.

### Texte (`char`)

Le champ Texte est utilisé pour un texte court contenant n’importe quel
caractère. Une ligne de texte est affichée lorsque le champ est complété.

  * Badge : permet d’afficher la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur dans l’UI, mais il est possible de définir une valeur par défaut.

  * Copier dans le presse-papiers : les utilisateurs peuvent copier la valeur en cliquant sur un bouton.

  * Email : la valeur devient un lien _mailto_ cliquable.

  * Image : permet d’afficher une image à l’aide d’une URL. Il n’est pas possible de modifier la valeur manuellement, mais il est possible de définir une valeur par défaut.

Note

Ceci fonctionne différemment de la sélection directe du champ Image, puisque
l’image n’est pas stockée dans Odoo lors de l’utilisation d’un champ Texte
avec le widget Image. Par exemple, cela peut être utile si vous voulez
économiser de l’espace disque.

  * Téléphone : la valeur devient un lien _tel_ cliquable.

Astuce

Cochez Activer les SMS pour ajouter une option permettant d’envoyer un SMS
directement depuis Odoo à côté du champ.

  * URL : la valeur devient une URL cliquable.

Example

![Exemples des champs Texte avec différents widgets](../../_images/text-
examples.png)

### Texte multiligne (`text`)

Le champ Texte multiligne est utilisé pour un texte plus long contenant
n’importe quel type de caractère. Deux lignes de texte sont affichées sur l’UI
lorsque le champ est complété.

  * Copier dans le presse-papiers : les utilisateurs peuvent copier la valeur en cliquant sur un bouton.

Example

![Exemples de champs Texte multiligne avec différents
widgets](../../_images/multiline-text-examples.png)

### Entier (`integer`)

Le champ Entier est utilisé pour tous les nombres entiers (positifs, négatifs,
ou zéro, sans décimale).

  * Graphique circulaire : affiche la valeur à l’intérieur d’un cercle de pourcentage, généralement pour une valeur calculée. Il n’est pas possible de modifier la valeur sur l’UI, mais il est possible de définir une valeur par défaut.

  * Barre de progression : affiche la valeur à côté d’une barre de progression, généralement pour une valeur calculée. Il n’est pas possible de modifier le champ manuellement, mais il est possible de définir une valeur par défaut.

  * Poignée : affiche une icône de poignée pour ordonner manuellement les enregistrements dans la [vue Liste](views.html#studio-views-multiple-records-list).

Example

![Exemples de champs Entier avec différents widgets](../../_images/integer-
examples.png)

### Décimale (`float`)

Le champ Décimale est utilisé pour tous les nombres décimaux (positifs,
négatifs, ou zéro, avec décimale).

Note

Les nombres décimaux sont affichés avec deux décimales après la virgule sur
l’UI, mais ils sont stockés dans la base de données avec plus de précision.

  * Monétaire : cette option est similaire à l’utilisation du champ Monétaire. Il est recommandé d’utiliser ce dernier, car il offre plus de fonctionnalités.

  * Pourcentage : affiche un caractère de pourcentage `%` après la valeur.

  * Graphique circulaire : affiche la valeur à l’intérieur d’un cercle de pourcentage, généralement pour une valeur calculée. Il n’est pas possible de modifier ce champ manuellement, mais il est possible de définir une valeur par défaut.

  * Barre de progression : affiche la valeur à côté d’une barre de progression, généralement pour une valeur calculée. Il n’est pas possible de modifier le champ manuellement, mais il est possible de définir une valeur par défaut.

  * Heure : la valeur doit respecter le format _hh:mm_ , avec un maximum de 59 minutes.

Example

![Exemples de champs décimaux avec différents widgets](../../_images/decimal-
examples.png)

### Monétaire (`monetary`)

Le champ Monétaire est utilisé pour toutes les valeurs monétaires.

Note

Lorsque vous ajoutez d’abord un champ Monétaire, vous avez tendance à vouloir
ajouter un champ Devise s’il n’y en a pas déjà un sur le modèle. Odoo propose
d’ajouter le champ Devise pour vous. Une fois qu’il est ajouté, ajoutez de
nouveau le champ Monétaire.

Example

![Exemple d'un champ Monétaire et de son champ Devise](../../_images/monetary-
example.png)

### Html (`html`)

Le champ Html est utilisé pour ajouter du texte qui peut être édité en
utilisant l’éditeur HTML d’Odoo.

  * Texte multiligne : désactive l’éditeur HTML d’Odoo pour permettre l’édition de HTML brut.

Example

![Exemples de champs Html avec différents widgets](../../_images/html-
example.png)

### Date (`date`)

Le champ Date est utilisé pour sélectionner une date sur un calendrier.

  * Jours restants : le nombre de jours restants avant l’affichage de la date sélectionnée (par ex. _Dans 5 jours_), en fonction de la date actuelle.

Example

![Exemples de champs Date avec différents widgets](../../_images/date-
examples.png)

### Date & Heure (`datetime`)

Le champ Date & Heure est utilisé pour sélectionner une date sur un calendrier
et une heure sur une horloge. L’heure actuelle de l’utilisateur est
automatiquement utilisée si aucune heure n’est définie.

  * Date : utilisé pour enregistrer l’heure sans l’afficher sur l’UI.

  * Jours restants : affiche le nombre de jours restants avant la date sélectionnée (par ex. _Dans 5 jours_), en fonction de la date et de l’heure actuelles.

Example

![Exemples des champs Date & Heure avec différents
widgets](../../_images/date-time-examples.png)

### Case à cocher (`boolean`)

Le champ Case à cocher est utilisé lorsqu’une valeur ne peut être que vraie ou
fausse, en cochant ou en décochant une case à cocher.

  * Bouton : affiche un bouton radio. Le widget fonctionne sans passer en mode édition.

  * Bascule : affiche un bouton à bascule. Le widget fonctionne sans passer en mode édition.

Example

![Exemples de champs Case à cocher avec différents
widgets](../../_images/checkbox-examples.png)

### Sélection (`selection`)

Le champ Sélection est utilisé lorsque les utilisateurs doivent sélectionner
une seule valeur parmi un nombre de valeurs prédéfinies.

  * Badge : permet d’afficher la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur dans l’UI, mais il est possible de définir une valeur par défaut.

  * Badges : affiche simultanément toutes les valeurs sélectionnables à l’intérieur de formes rectangulaires, organisées horizontalement.

  * Priorité : affiche des symbôles en forme d’étoile à la place des valeurs, qui peuvent être utilisés pour indiquer un niveau d’importance ou de satisfaction par exemple. Cela a le même effet que de sélectionner le champ Priorité, bien que, pour ce dernier, quatre valeurs de priorité soient déjà prédéfinies.

  * Radio : affiche toutes les valeurs sélectionnables en même temps sous forme de boutons radio.

Astuce

Par défaut, les boutons radio sont organisés verticalement. Cochez Affichez
horizontalement pour modifier la façon dont ils sont affichés.

Example

![Exemples de champs Sélection avec différents
widgets](../../_images/selection-examples.png)

### Priorité (`selection`)

Le champ Priorité permet d’afficher un système d’évaluation à trois étoiles,
qui peut être utilisé pour indiquer un niveau d’importance ou de satisfaction.
Ce type de champ est un champ Sélection avec le widget Priorité sélectionné
par défaut et quatre valeurs de priorité prédéfinies. Par conséquent, les
widgets Badge, Badges, Radio, et Sélection ont les mêmes effets que ceux
décrits dans la section Sélection.

Astuce

Pour modifier le nombre d’étoiles disponibles en ajoutant ou supprimant des
valeurs, cliquez sur Modifier les valeurs. Notez que la première valeur est
égale à 0 étoiles (c’est-à-dire, lorsqu’aucune sélection n’est faite), donc
quatre valeurs donnent un système d’évaluation à trois étoiles par exemple.

Example

![Exemple d'un champ Priorité](../../_images/priority-example.png)

### Fichier (`binary`)

Le champ Fichier permet de charger tout type de fichier ou de signer un
formulaire (widget Signature).

  * Image : les utilisateurs peuvent charger une image, qui est alors affichée dans la [vue Formulaire](views.html#studio-views-general-form). L’effet est le même que celui du champ Image.

  * Visualiseur PDF : les utilisateurs peuvent charger un fichier PDF, qui peut ensuite être consulté à partir de la [vue Formulaire](views.html#studio-views-general-form).

  * Signature : les utilisateurs peuvent signer le formulaire électroniquement. L’effet est le même que celui du champ Signature.

Example

![Exemples de champs Fichier avec différents widgets](../../_images/file-
examples.png)

### Image (`binary`)

Le champ Image permet de charger une image et de l’afficher dans la [vue
Formulaire](views.html#studio-views-general-form). Ce type de champ est un
champ Fichier avec le widget Image sélectionné par défaut. Par conséquent, les
widgets Fichier, Visualiseur PDF, et Signature ont les mêmes effets que ceux
décrits sous la section Fichier.

Astuce

Pour modifier l’affichage des images chargées, sélectionnez Petite, Moyenne ou
Grande dans l’option Taille.

### Signature (`binary`)

Le champ Signature permet de signer le formulaire électroniquement. Ce type de
champ est un champ Fichier avec le widget Signature sélectionné par défaut.
Par conséquent, les widgets Fichier, Image et Visualiseur PDF ont les mêmes
effets que ceux décrits sous la section Fichier.

Astuce

Pour donner aux utilisateurs l’option Automatique lorsqu’ils doivent dessiner
leur signature, sélectionnez un des champs Autocompléter avec disponibles
(Texte, Many2One et Champ associé sur le modèle uniquement). La signature est
générée automatiquement à l’aide des données du champ sélectionné.

## Champs relationnels

Les champs relationnels sont utilisés pour lier et afficher les données des
enregistrements d’un autre modèle.

Note

Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont
énumérés sous forme de points ci-dessous.

### Many2One (`many2one`)

Le champ Many2One est utilisé pour lier un autre enregistrement (d’un autre
modèle) au modèle en cours d’édition. Le nom de l’enregistrement de l’autre
modèle est alors affiché sur l’enregistrement en cours d’édition.

Example

Sur le modèle _Commande_ , le champ Client est un champ Many2One qui pointe
vers le modèle _Contact_. Cela permet de lier **plusieurs** commandes à **un
seul** contact (client).

![Diagramme affichant une relation many2one](../../_images/many2one-
diagram.png)

Astuce

  * Pour empêcher les utilisateurs de créer un nouvel enregistrement dans le modèle lié, cochez Désactiver la création.

  * Pour empêcher les utilisateurs d’ouvrir des enregistrements dans une fenêtre contextuelle, cochez Désactiver l’ouverture.

  * Pour aider les utilisateurs à ne sélectionner que le bon enregistrement, cliquez sur Domaine pour créer un filtre.

  * Badge : affiche la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur sur l’UI.

  * Radio : affiche toutes les valeurs sélectionnables en même temps sous forme de boutons radio.

### One2Many (`one2many`)

Le champ One2Many est utilisé pour afficher les relations existantes entre un
enregistrement du modèle actuel et plusieurs enregistrements d’un autre
modèle.

Example

Vous pouvez ajouter un champ One2Many au modèle _Contact_ pour consulter les
**nombreuses** commandes d”**un seul** client.

![Diagramme affichant une relation one2many](../../_images/one2many-
diagram.png)

Note

Pour utiliser un champ One2Many, les deux modèles doivent déjà avoir été liés
à l’aide d’un champ Many2One. Les relations One2Many n’existent pas
indépendamment : une recherche inverse des relations Many2One existantes est
effectuée.

### Lignes (`one2many`)

Le champ Lignes permet de créer un tableau avec des lignes et des colonnes
(par ex. les lignes de produits d’une commande).

Astuce

Pour modifier les colonnes, cliquez sur le champ Lignes et ensuite Modifier la
vue liste. Pour modifier le formulaire qui apparaît lorsqu’un utilisateur
clique sur Ajouter une ligne, cliquez plutôt sur Modifier la vue formulaire.

Example

![Exemple d'un champ Lignes](../../_images/lines-example.png)

### Many2Many (`many2many`)

Le champ Many2Many permet de lier plusieurs enregistrements d’un autre modèle
à plusieurs enregistrements du modèle actuel. Les champs Many2Many peuvent
utiliser Désactiver la création, Désactiver l’ouverture, Domaine, tout comme
les champs Many2One.

Example

Sur le modèle _Tâche_ , le champ Assignés est un champ Many2Many qui pointe
vers le modèle _Contact_. Cela permet à un seul utilisateur d’être assigné à
**plusieurs** tâches et à **plusieurs** utilisateurs d’être assignés à une
seule tâche.

![Diagramme affichant des relations many2many](../../_images/many2many-
diagram.png)

  * Cases à cocher : les utilisateurs peuvent sélectionner plusieurs valeurs à l’aide de cases à cocher.

  * Étiquettes : les utilisateurs peuvent sélectionner plusieurs valeurs apparaissant dans des formes arrondies, également connues comme des _étiquettes_. L’effet est le même que celui de la sélection du champ Étiquettes.

### Étiquettes (`many2many`)

Le champ Étiquettes permet d’afficher plusieurs valeurs d’un autre modèle dans
des formes arrondies, également connues comme des _étiquettes_. Ce type de
champ est un champ Many2Many avec le widget Étiquettes sélectionné par défaut.
Par conséquent, les widgets Cases à cocher et Many2Many ont les mêmes effets
que ceux décrits dans la section Many2Many.

Astuce

Pour afficher des étiquettes avec différentes couleurs de fond, cochez
Utiliser des couleurs.

Example

![Exemple d'un champ Étiquettes](../../_images/tags-example.png)

### Champ associé (`related`)

Un Champ associé n’est pas un champ relationnel à proprement parler ; aucune
relation n’est créée entre les modèles. Il utilise une relation existante pour
récupérer et afficher des informations d’un autre enregistrement.

Example

Pour afficher l’adresse email d’un client sur le modèle _Commande_ utilisez le
Champ associé `partner_id.email` en sélectionnant Client et ensuite Email.

## Propriétés

  * Invisible : Lorsqu’il n’est pas nécessaire que les utilisateurs voient un champ dans l’UI, cochez Invisible. Cela permet d’alléger l’UI en n’affichant que les champs essentiels en fonction d’une situation spécifique.

Example

Dans la vue _Formulaire_ du modèle _Contact_ , le champ Titre n’apparaît que
lorsque Individuel est sélectionné, car ce champ n’est pas utile pour une
Société.

Note

L’attribut Invisible s’applique également à Studio. Pour afficher les champs
masqués dans Studio, cliquez sur l’onglet Vue d’une vue et cochez Afficher les
éléments invisibles.

  * Requis : Si un champ doit toujours être complété par l’utilisateur avant de pouvoir continuer, cochez Requis.

  * Lecture seule : Si les utilisateurs ne doivent pas être en mesure de modifier un champ, cochez Lecture seule.

Note

Vous pouvez choisir d’appliquer ces trois propriétés uniquement à des
enregistrements spécifiques en cliquant sur Conditionnel et en créant un
filtre.

  * Libellé : Le champ Libellé est le nom du champ dans l’UI.

Note

Ce nom n’est pas le même que celui utilisé dans la base de données PostgreSQL.
Pour afficher et modifier ce dernier, activez le [mode
développeur](../general/developer_mode.html#developer-mode), et modifiez le
nom technique.

  * Infobulle d’aide : Pour expliquer l’utilité d’un champ, écrivez une description sous Infobulle d’aide. Elle s’affiche à l’intérieur d’une infobulle lorsque vous passez la souris sur le libellé du champ.

  * Placeholder : Pour donner un exemple de la manière dont un champ doit être complété, écrivez-le sous Placeholder. Il s’affiche en gris clair à la place de la valeur du champ.

  * Widget : Pour changer l’apparence ou la fonctionnalité par défaut d’un champ, sélectionnez un des widgets disponibles.

  * Valeur par défaut : Pour ajouter une valeur par défaut à un champ lorsqu’un enregistrement est créé, utilisez Valeur par défaut.

  * Limiter la visibilité aux groupes : Pour limiter les utilisateurs qui peuvent voir le champ, sélectionnez un groupe d’accès d’utilisateurs.

  *[UI]: Interface utilisateur

