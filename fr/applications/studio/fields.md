# Champs et widgets

Les champs permettent de structurer les modèles d’une base de données. Si vous
imaginez un modèle sous la forme d’un tableau ou d’une feuille de calcul, les
champs sont les colonnes dans lesquelles les données sont stockées dans les
enregistrements (c’est-à-dire les lignes). Les champs définissent également le
type de données qui y sont stockées. La manière dont les données sont
présentées et formatées dans l”UI est déterminée par leur widget.

D’un point de vue technique, il y a 15 types de champ dans Konvergo ERP. Toutefois,
vous pouvez choisir parmi 20 champs dans Studio, car certains types de champs
sont disponibles plus d’une fois en appliquant un différent widget par défaut.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est uniquement possible d’ajouter de <b>Nouveaux champs</b> aux vues <a href="views#studio-views-general-form"><span class="std std-ref">Formulaire</span></a> et <a href="views#studio-views-multiple-records-list"><span class="std std-ref">Liste</span></a>. Dans les autres vues, vous ne pouvez ajouter que des <b>Champs existants</b> <span class="dfn"><span>(champs déjà présents dans le modèle)</span></span>.</p>
</div>

## Champs simples

Les champs simples contiennent des valeurs de base, telles qu’un texte, des
chiffres, des fichiers, etc.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>

### Texte (`char`)

Le champ **Texte** est utilisé pour un texte court contenant n’importe quel
caractère. Une ligne de texte est affichée lorsque le champ est complété.

  * **Badge** : permet d’afficher la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur dans l’UI, mais il est possible de définir une valeur par défaut.

  * **Copier dans le presse-papiers** : les utilisateurs peuvent copier la valeur en cliquant sur un bouton.

  * **Email** : la valeur devient un lien _mailto_ cliquable.

  * **Image** : permet d’afficher une image à l’aide d’une URL. Il n’est pas possible de modifier la valeur manuellement, mais il est possible de définir une valeur par défaut.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>

  * **Téléphone** : la valeur devient un lien _tel_ cliquable.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>

  * **URL** : la valeur devient une URL cliquable.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Exemples des champs Texte avec différents widgets" class="align-center" src="../../_images/text-examples.png"/>
</div>

### Texte multiligne (`text`)

Le champ **Texte multiligne** est utilisé pour un texte plus long contenant
n’importe quel type de caractère. Deux lignes de texte sont affichées sur l’UI
lorsque le champ est complété.

  * **Copier dans le presse-papiers** : les utilisateurs peuvent copier la valeur en cliquant sur un bouton.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Exemples de champs Texte multiligne avec différents widgets" class="align-center" src="../../_images/multiline-text-examples.png"/>
</div>

### Entier (`integer`)

Le champ **Entier** est utilisé pour tous les nombres entiers (positifs,
négatifs, ou zéro, sans décimale).

  * **Graphique circulaire** : affiche la valeur à l’intérieur d’un cercle de pourcentage, généralement pour une valeur calculée. Il n’est pas possible de modifier la valeur sur l’UI, mais il est possible de définir une valeur par défaut.

  * **Barre de progression** : affiche la valeur à côté d’une barre de progression, généralement pour une valeur calculée. Il n’est pas possible de modifier le champ manuellement, mais il est possible de définir une valeur par défaut.

  * **Poignée** : affiche une icône de poignée pour ordonner manuellement les enregistrements dans la [vue Liste](views#studio-views-multiple-records-list).

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Exemples de champs Entier avec différents widgets" class="align-center" src="../../_images/integer-examples.png"/>
</div>

### Décimale (`float`)

Le champ **Décimale** est utilisé pour tous les nombres décimaux (positifs,
négatifs, ou zéro, avec décimale).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les nombres décimaux sont affichés avec deux décimales après la virgule sur l’UI, mais ils sont stockés dans la base de données avec plus de précision.</p>
</div>

  * **Monétaire** : cette option est similaire à l’utilisation du champ Monétaire. Il est recommandé d’utiliser ce dernier, car il offre plus de fonctionnalités.

  * **Pourcentage** : affiche un caractère de pourcentage `%` après la valeur.

  * **Graphique circulaire** : affiche la valeur à l’intérieur d’un cercle de pourcentage, généralement pour une valeur calculée. Il n’est pas possible de modifier ce champ manuellement, mais il est possible de définir une valeur par défaut.

  * **Barre de progression** : affiche la valeur à côté d’une barre de progression, généralement pour une valeur calculée. Il n’est pas possible de modifier le champ manuellement, mais il est possible de définir une valeur par défaut.

  * **Heure** : la valeur doit respecter le format _hh:mm_ , avec un maximum de 59 minutes.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Exemples de champs décimaux avec différents widgets" class="align-center" src="../../_images/decimal-examples.png"/>
</div>

### Monétaire (`monetary`)

Le champ **Monétaire** est utilisé pour toutes les valeurs monétaires.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsque vous ajoutez d’abord un champ <b>Monétaire</b>, vous avez tendance à vouloir ajouter un champ <b>Devise</b> s’il n’y en a pas déjà un sur le modèle. Konvergo ERP propose d’ajouter le champ <b>Devise</b> pour vous. Une fois qu’il est ajouté, ajoutez de nouveau le champ <b>Monétaire</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>0

### Html (`html`)

Le champ **Html** est utilisé pour ajouter du texte qui peut être édité en
utilisant l’éditeur HTML d’Konvergo ERP.

  * **Texte multiligne** : désactive l’éditeur HTML d’Konvergo ERP pour permettre l’édition de HTML brut.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>1

### Date (`date`)

Le champ **Date** est utilisé pour sélectionner une date sur un calendrier.

  * **Jours restants** : le nombre de jours restants avant l’affichage de la date sélectionnée (par ex. _Dans 5 jours_), en fonction de la date actuelle.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>2

### Date & Heure (`datetime`)

Le champ **Date & Heure** est utilisé pour sélectionner une date sur un
calendrier et une heure sur une horloge. L’heure actuelle de l’utilisateur est
automatiquement utilisée si aucune heure n’est définie.

  * **Date** : utilisé pour enregistrer l’heure sans l’afficher sur l’UI.

  * **Jours restants** : affiche le nombre de jours restants avant la date sélectionnée (par ex. _Dans 5 jours_), en fonction de la date et de l’heure actuelles.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>3

### Case à cocher (`boolean`)

Le champ **Case à cocher** est utilisé lorsqu’une valeur ne peut être que
vraie ou fausse, en cochant ou en décochant une case à cocher.

  * **Bouton** : affiche un bouton radio. Le widget fonctionne sans passer en mode édition.

  * **Bascule** : affiche un bouton à bascule. Le widget fonctionne sans passer en mode édition.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>4

### Sélection (`selection`)

Le champ **Sélection** est utilisé lorsque les utilisateurs doivent
sélectionner une seule valeur parmi un nombre de valeurs prédéfinies.

  * **Badge** : permet d’afficher la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur dans l’UI, mais il est possible de définir une valeur par défaut.

  * **Badges** : affiche simultanément toutes les valeurs sélectionnables à l’intérieur de formes rectangulaires, organisées horizontalement.

  * **Priorité** : affiche des symbôles en forme d’étoile à la place des valeurs, qui peuvent être utilisés pour indiquer un niveau d’importance ou de satisfaction par exemple. Cela a le même effet que de sélectionner le champ Priorité, bien que, pour ce dernier, quatre valeurs de priorité soient déjà prédéfinies.

  * **Radio** : affiche toutes les valeurs sélectionnables en même temps sous forme de boutons radio.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>5

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>6

### Priorité (`selection`)

Le champ **Priorité** permet d’afficher un système d’évaluation à trois
étoiles, qui peut être utilisé pour indiquer un niveau d’importance ou de
satisfaction. Ce type de champ est un champ Sélection avec le widget
**Priorité** sélectionné par défaut et quatre valeurs de priorité prédéfinies.
Par conséquent, les widgets **Badge** , **Badges** , **Radio** , et
**Sélection** ont les mêmes effets que ceux décrits dans la section Sélection.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>8

### Fichier (`binary`)

Le champ **Fichier** permet de charger tout type de fichier ou de signer un
formulaire (widget **Signature**).

  * **Image** : les utilisateurs peuvent charger une image, qui est alors affichée dans la [vue Formulaire](views#studio-views-general-form). L’effet est le même que celui du champ Image.

  * **Visualiseur PDF** : les utilisateurs peuvent charger un fichier PDF, qui peut ensuite être consulté à partir de la [vue Formulaire](views#studio-views-general-form).

  * **Signature** : les utilisateurs peuvent signer le formulaire électroniquement. L’effet est le même que celui du champ Signature.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les widgets autres que ceux par défaut, lorsqu’ils sont disponibles, sont énumérés sous forme de points ci-dessous.</p>
</div>9

### Image (`binary`)

Le champ **Image** permet de charger une image et de l’afficher dans la [vue
Formulaire](views#studio-views-general-form). Ce type de champ est un
champ Fichier avec le widget **Image** sélectionné par défaut. Par conséquent,
les widgets **Fichier** , **Visualiseur PDF** , et **Signature** ont les mêmes
effets que ceux décrits sous la section Fichier.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>0

### Signature (`binary`)

Le champ **Signature** permet de signer le formulaire électroniquement. Ce
type de champ est un champ Fichier avec le widget **Signature** sélectionné
par défaut. Par conséquent, les widgets **Fichier** , **Image** et
**Visualiseur PDF** ont les mêmes effets que ceux décrits sous la section
Fichier.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>1

## Champs relationnels

Les champs relationnels sont utilisés pour lier et afficher les données des
enregistrements d’un autre modèle.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>2

### Many2One (`many2one`)

Le champ **Many2One** est utilisé pour lier un autre enregistrement (d’un
autre modèle) au modèle en cours d’édition. Le nom de l’enregistrement de
l’autre modèle est alors affiché sur l’enregistrement en cours d’édition.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>3 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>4

  * **Badge** : affiche la valeur à l’intérieur d’une forme arrondie, semblable à une étiquette. Il n’est pas possible de modifier la valeur sur l’UI.

  * **Radio** : affiche toutes les valeurs sélectionnables en même temps sous forme de boutons radio.

### One2Many (`one2many`)

Le champ **One2Many** est utilisé pour afficher les relations existantes entre
un enregistrement du modèle actuel et plusieurs enregistrements d’un autre
modèle.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>6

### Lignes (`one2many`)

Le champ **Lignes** permet de créer un tableau avec des lignes et des colonnes
(par ex. les lignes de produits d’une commande).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>8

### Many2Many (`many2many`)

Le champ **Many2Many** permet de lier plusieurs enregistrements d’un autre
modèle à plusieurs enregistrements du modèle actuel. Les champs Many2Many
peuvent utiliser **Désactiver la création** , **Désactiver l’ouverture** ,
**Domaine** , tout comme les champs Many2One.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ceci fonctionne différemment de la sélection directe du <a href="#studio-fields-simple-fields-image"><span class="std std-ref">champ Image</span></a>, puisque l’image n’est pas stockée dans Konvergo ERP lors de l’utilisation d’un champ <b>Texte</b> avec le widget <b>Image</b>. Par exemple, cela peut être utile si vous voulez économiser de l’espace disque.</p>
</div>9

  * **Cases à cocher** : les utilisateurs peuvent sélectionner plusieurs valeurs à l’aide de cases à cocher.

  * **Étiquettes** : les utilisateurs peuvent sélectionner plusieurs valeurs apparaissant dans des formes arrondies, également connues comme des _étiquettes_. L’effet est le même que celui de la sélection du champ Étiquettes.

### Étiquettes (`many2many`)

Le champ **Étiquettes** permet d’afficher plusieurs valeurs d’un autre modèle
dans des formes arrondies, également connues comme des _étiquettes_. Ce type
de champ est un champ Many2Many avec le widget **Étiquettes** sélectionné par
défaut. Par conséquent, les widgets **Cases à cocher** et **Many2Many** ont
les mêmes effets que ceux décrits dans la section Many2Many.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>0 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>1

### Champ associé (`related`)

Un **Champ associé** n’est pas un champ relationnel à proprement parler ;
aucune relation n’est créée entre les modèles. Il utilise une relation
existante pour récupérer et afficher des informations d’un autre
enregistrement.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>2

## Propriétés

  * **Invisible** : Lorsqu’il n’est pas nécessaire que les utilisateurs voient un champ dans l’UI, cochez **Invisible**. Cela permet d’alléger l’UI en n’affichant que les champs essentiels en fonction d’une situation spécifique.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>4

  * **Requis** : Si un champ doit toujours être complété par l’utilisateur avant de pouvoir continuer, cochez **Requis**.

  * **Lecture seule** : Si les utilisateurs ne doivent pas être en mesure de modifier un champ, cochez **Lecture seule**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>5

  * **Libellé** : Le champ **Libellé** est le nom du champ dans l’UI.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Cochez <b>Activer les SMS</b> pour ajouter une option permettant d’envoyer un SMS directement depuis Konvergo ERP à côté du champ.</p>
</div>6

  * **Infobulle d’aide** : Pour expliquer l’utilité d’un champ, écrivez une description sous **Infobulle d’aide**. Elle s’affiche à l’intérieur d’une infobulle lorsque vous passez la souris sur le libellé du champ.

  * **Placeholder** : Pour donner un exemple de la manière dont un champ doit être complété, écrivez-le sous **Placeholder**. Il s’affiche en gris clair à la place de la valeur du champ.

  * **Widget** : Pour changer l’apparence ou la fonctionnalité par défaut d’un champ, sélectionnez un des widgets disponibles.

  * **Valeur par défaut** : Pour ajouter une valeur par défaut à un champ lorsqu’un enregistrement est créé, utilisez **Valeur par défaut**.

  * **Limiter la visibilité aux groupes** : Pour limiter les utilisateurs qui peuvent voir le champ, sélectionnez un groupe d’accès d’utilisateurs.

  *[UI]: Interface utilisateur

