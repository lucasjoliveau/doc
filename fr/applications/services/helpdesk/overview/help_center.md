# Centre d’assistance

Odoo _Assistance_ s’intègre aux applications _Forums_ , _eLearning_ et
_Connaissances_ pour créer le _centre d’assistance_.

![Aperçu de la page des paramètres d'une équipe mettant en évidence les
fonctionnalités du centre d'assistance.](../../../../_images/help-center-
enable-features.png)

Le _centre d’assistance_ est un lieu centralisé où les équipes et les clients
peuvent rechercher et partager des informations détaillées sur les produits et
les services.

Note

Pour activer n’importe laquelle de ces fonctionnalités sur une équipe d”
_Assistance_ , (_Forums_ , _eLearning_ , ou _Connaissances_), la Visibilité de
l’équipe doit être définie sur Tous les utilisateurs internes et les
utilisateurs portail invités. Consultez [Démarrer](getting_started.html) pour
plus d’informations sur les paramètres et la configuration de l’équipe d”
_Assistance_.

Avertissement

Puisque toutes les fonctionnalités du _centre d’assistance_ nécessitent d’être
intégrées aux autres applications, leur activation peut entraîner
l’installation de modules ou d’applications supplémentaires.

L’installation d’une nouvelle application sur une base de données _Une app
gratuite_ déclenche une période d’essai de 15 jours. À la fin de la période
d’essai, si aucun abonnement payant n’est ajouté à la base de données, elle ne
sera plus active ou accessible.

## Connaissances

L’application _Connaissances_ d’Odoo est une bibliothèque collaborative où les
utilisateurs peuvent sauvegarder, modifier et partager des informations.
L’application _Connaissances_ est représentée dans la base de données par une
icône de _livre_.

![Vue d'un message dans Assistance mettant en évidence l'icône de livre de
Connaissances.](../../../../_images/help-center-knowledge-book-icon.png)

### Activer Connaissances sur une équipe d’assistance

Pour activer la fonctionnalité _Connaissances_ sur une équipe d” _Assistance_
, allez à Assistance ‣ Configuration ‣ Équipes et sélectionnez une équipe ou
créez-en une [nouvelle](getting_started.html).

Lorsqu’une équipe a été sélectionnée ou créée, Odoo affiche le formulaire
détaillé de cette équipe.

Sur le formulaire détaillé de l’équipe, faites défiler jusqu’à la section
Self-Service. Cochez la case à côté de Connaissances pour activer la
fonctionnalité _Connaissances_. Une fois la case cochée, un nouveau champ
libellé Article apparaît.

Le fait de cliquer sur le champ Article fait apparaître un menu déroulant. Au
début, il n’y a qu’une seule option dans le menu déroulant, intitulée Help,
qu’Odoo propose par défaut. Sélectionnez Help dans le menu déroulant pour
choisir cet article.

Astuce

Pour créer un nouvel article, allez à l’application Connaissances, puis passez
le curseur à côté de l’en-tête de la section Espace de travail, située dans la
barre latérale gauche. En déplaçant le curseur à cet endroit, vous verrez
apparaître une icône masquée ➕ (signe plus).

Cliquez sur ➕ (signe plus) pour créer un nouvel article dans l”Espace de
travail. Dans le coin supérieur droit de la page, cliquez sur le bouton
Partager et faites basculer le commutateur Partager sur internet sur Article
publié. L’article peut alors être ajouté à l’équipe d” _Assistance_.

Une fois qu’un article a été créé et assigné à une équipe d” _Assistance_ , le
contenu peut être ajouté et organisé via l’application _Connaissances_.

Pour plus d'infos

[Modifier des articles de
Connaissances](../../../productivity/knowledge/articles_editing.html)

### Rechercher des articles à partir d’un ticket d’assistance

Lorsque les membres d’une équipe d” _Assistance_ tentent de résoudre un
ticket, ils peuvent rechercher dans le contenu de l’application
_Connaissances_ pour avoir plus d’informations relatives à la question.

Pour rechercher des articles de _Connaissances_ , ouvrez un ticket — soit à
partir du tableau de bord de l’application _Assistance_ , soit en allant à
l’application Assistance ‣ Tickets ‣ Tous les tickets, et en sélectionnant un
Ticket dans la liste.

Lorsqu’un Ticket est sélectionné, Odoo affiche le formulaire détaillé de ce
ticket.

Cliquez sur l’icône Connaissances (livre), située au-dessus du chatter pour
ouvrir une fenêtre de recherche.

![Vue d'une fenêtre de recherche de Connaissances sur un ticket
d'assistance.](../../../../_images/help-center-knowledge-search.png)

Astuce

Il est également possible de rechercher des articles de _Connaissances_ en
appuyant sur **Ctrl + K** pour ouvrir la palette de commande, puis en tapant
**?** , suivi par le nom de l’article souhaité.

Lorsqu’Odoo affiche l’article souhaité, cliquez dessus ou mettez en
surbrillance le titre de l”Article et appuyez sur **Enter**. Cette option
permet d’ouvrir l’article dans l’application Connaissances.

Pour ouvrir l’article dans un nouvel onglet, appuyez sur **Ctrl + Enter**.

Astuce

Si une recherche plus approfondie est nécessaire, appuyez sur **Alt + B**. Une
page séparée s’affiche, dans laquelle vous pouvez effectuer une recherche plus
détaillée.

#### Partager des articles avec le centre d’assistance

Pour qu’un article de _Connaissances_ soit disponible aux clients et aux
visiteurs du site web, il doit être publié.

Note

Même si l’article _Help_ a été activé sur une équipe, Odoo ne partagera pas
tous les sous-articles sur le site web. Les articles individuels destinés aux
clients **doivent** être publiés pour être visibles sur le site web.

Pour publier un article, allez jusqu’à l’article souhaité, en suivant les
étapes ci-dessus et cliquez sur l’icône Partager dans le coin supérieur droit.
Un menu apparaît alors. Faites basculer le bouton intitulé Partager sur
internet sur Article publié.

![Vue d'un article de connaissances mettant en évidence les options de partage
et de publication.](../../../../_images/help-center-knowledge-sharing.png)

### Résoudre des tickets avec des modèles

Il est possible d’ajouter des boîtes de _modèle_ aux articles de
_Connaissances_ pour permettre de le réutiliser, de le copier, de l’envoyer
comme message ou de l’ajouter à la description d’un ticket. Cela permet aux
équipes de maintenir une certaine cohérence lorsqu’elles répondent aux tickets
des clients et de minimiser le temps passé à répondre à des questions
répétées.

#### Ajouter des modèles aux articles

Pour créer un modèle, allez à Connaissances ‣ Help. Cliquez sur un sous-
article existant ou créez un nouvel article en cliquant sur l’icône ➕ (signe
plus) à côté de _Help_.

Tapez `/` pour ouvrir la Boîte à outils et afficher une liste de
[commandes](../../../productivity/knowledge/articles_editing.html).
Sélectionnez ou tapez `modèle`. Un bloc de modèle gris sera ajouté à la page.
Ajoutez le contenu que vous voulez à ce bloc.

![Vue d'un modèle dans Connaissances mettant en évidence les options d'envoi
et de copie.](../../../../_images/help-center-knowledge-template-options.png)

Note

Les modèles afficheront uniquement les options Utiliser comme description ou
Envoyer en tant que message s’ils sont accessibles directement depuis
_Assistance_.

#### Utiliser des modèles dans les tickets

Les modèles peuvent être utilisés pour répondre directement à un ticket d”
_Assistance_ sous forme de message ou pour ajouter des informations à la
description du ticket.

Pour utiliser des modèles dans un ticket d” _Assistance_ , ouvrez d’abord un
ticket, soit à partir du tableau de bord Assistance, soit en allant à
Assistance ‣ Tickets ‣ Tous les tickets et en sélectionnant un Ticket dans la
liste.

Cliquez sur l’icône Connaissances (livre) au-dessus du chatter du ticket. Une
fenêtre de recherche s’affiche. Dans cette fenêtre de recherche, sélectionnez
ou recherchez l’article souhaité. Cette option permet d’afficher la page de
l’article dans l’application _Connaissances_ d’Odoo.

Pour utiliser un modèle afin de répondre à un ticket, cliquez sur Envoyer en
tant que message dans le coin supérieur droit de la boîte de modèle, située
dans le corps de l’article.

Une fenêtre contextuelle Composer un email s’affiche. Dans cette fenêtre,
sélectionnez les destinataires, faites les ajouts ou les modifications
nécessaires au modèle, puis cliquez sur Envoyer.

Astuce

Pour utiliser un modèle afin d’ajouter des informations à la description d’un
ticket, cliquez sur Utiliser comme description dans le coin supérieur droit de
la boîte de modèle, située dans le corps de l’article. Cela ne remplace pas le
texte existant dans la description d’un ticket. Le modèle sera ajouté en tant
que texte supplémentaire.

## Forum de la communauté

Un _Forum de la communauté_ offre aux clients un espace où ils peuvent
répondre aux questions des autres et partager des informations. En intégrant
un forum à une équipe d” _Assistance_ , les tickets soumis par les clients
peuvent être convertis en posts et partagés.

### Activer les forums sur une équipe d’assistance

Pour activer les Forums de la communauté sur une équipe d” _Assistance_ ,
allez à l’application Assistance ‣ Configuration ‣ Équipes et sélectionnez une
équipe ou créez-en une [nouvelle](getting_started.html).

La sélection ou la création d’une équipe fait apparaître le formulaire
détaillé de cette équipe. Faites défiler jusqu’à la section Self-Service des
fonctionnalités et activez Forum de la communauté, en cochant la case à côté
de la fonctionnalité.

Lorsqu’il est activé, un nouveau champ libellé Forums apparaît en dessous.

Cliquez sur le champ Forums vide pour faire apparaître un menu déroulant. Par
défaut, il n’y a qu’une seule option pour commencer, intitulée Help. C’est
l’option qu’Odoo a automatiquement créée lorsque la fonctionnalité Forums de
la communauté a été activée. Sélectionnez Help dans le menu déroulant pour
activer ce forum.

Pour créer un nouveau forum, tapez un nom dans le champ Forums vide, puis
cliquez sur l’option Créer et Modifier. Il est possible de sélectionner
plusieurs forums dans ce champ.

Pour plus d'infos

Consultez la [documentation sur le forum](../../../websites/forum.html) pour
apprendre comment configurer, utiliser et modérer un forum.

### Créer un post de forum à partir d’un ticket d’assistance

Lorsqu’une équipe d” _Assistance_ a un _Forum_ activé, les tickets soumis à
cette équipe peuvent être convertis en posts de forum.

Pour ce faire, sélectionnez un ticket, soit dans le pipeline d’une équipe,
soit dans Tickets ‣ Tous les tickets dans l’application Assistance.

En haut du formulaire détaillé du ticket, cliquez sur le bouton Partager sur
le forum.

![Aperçu de la page des forums d'un site web pour montrer ceux qui sont
disponibles dans Odoo Assistance.](../../../../_images/help-center-share-on-
forum.png)

Lorsque vous cliquez sur ce bouton, une fenêtre contextuelle s’affiche. Vous
pouvez y modifier le poste et le titre pour corriger d’éventuelles faute de
frappe ou supprimer toute information relative au propriétaire ou au client.
Des Étiquettes peuvent être ajoutées pour aider à organiser le post dans le
forum, ce qui permet aux utilisateurs de le retrouver plus facilement. Lorsque
toutes les modifications ont été effectuées, cliquez sur Créer et voir le
post.

## eLearning

Les cours Odoo _eLearning_ proposent aux clients des formations et des
contenus supplémentaires sous forme de vidéos, présentations et
certifications/quiz. Ces formations supplémentaires permettent aux clients de
résoudre les problèmes et de trouver des solutions par eux-mêmes. Ils peuvent
également mieux comprendre les services et les produits qu’ils utilisent.

### Activer les cours eLearning sur une équipe d’assistance

Pour activer les cours d” _eLearning_ sur une équipe d” _Assistance_ , allez à
Assistance ‣ Configuration ‣ Équipes et sélectionnez une équipe ou créez-en
une [nouvelle](getting_started.html).

Sur la page des paramètres de l’équipe, faites défiler jusqu’à la section
Self-Service et cochez la case à côté d”eLearning. Un nouveau champ intitulé
Cours apparaît en dessous.

Cliquez sur le champ vide à côté de Cours sous la fonctionnalité eLearning
pour faire apparaître un menu déroulant. Sélectionnez un cours disponible dans
le menu déroulant ou tapez un titre dans le champ et cliquez sur Créer et
modifier pour créer un nouveau cours à partir de cette page. Plusieurs cours
peuvent être assignés à une seule équipe.

### Créer un cours d’eLearning

Un nouveau cours d” _eLearning_ peut être créé à partir de la page des
paramètres de l’équipe d”Assistance, comme dans l’étape ci-dessus, ou à partir
de l’application _eLearning_.

Pour créer un cours directement dans l’application _eLearning_ , allez à
eLearning ‣ Nouveau. Ceci révèle un modèle de cours vierge qui peut être
personnalisé et modifié selon les besoins.

Sur la page de modèle du cours, ajoutez un Titre de cours et en dessous, des
Étiquettes.

Cliquez sur l’onglet Options. Sous Droits d’accès, choisissez la Politique
d’inscription. Celle-ci détermine quels utilisateurs seront autorisés à suivre
le cours. Sous Affichage, choisissez le Type de cours et la Visibilité. Le
paramètre Visibilité détermine si le cours sera accessible aux visiteurs du
site public ou aux membres.

#### Ajouter du contenu à un cours d’eLearning

Pour ajouter du contenu à un cours, cliquez sur l’onglet Contenu et
sélectionnez Ajouter du contenu. Choisissez le Type de contenu dans le menu
déroulant et chargez le fichier, ou collez le lien, selon les instructions.
Cliquez sur Enregistrer quand vous avez terminé. Cliquez sur Ajouter une
section pour organiser le cours en sections.

![Vue d'un cours en cours de publication dans Odoo
Assistance.](../../../../_images/help-center-elearning-course-contents-
page.png)

Note

Afin d’ajouter une certification à un cours, allez à eLearning ‣ Configuration
‣ Paramètres, cochez la case intitulée Certifications, et cliquez sur
Enregistrer pour activer le paramètre.

Pour plus d'infos

[Tutoriels Odoo : eLearning](https://www.odoo.com/slides/elearning-56)

### Publier un cours d’eLearning

Pour permettre aux clients de s’inscrire à un cours, vous devez publier le
cours et son contenu.

Si le cours est publié, mais que son contenu ne l’est pas, les clients peuvent
s’inscrire au cours sur le site web, mais ils ne pourront pas consulter le
contenu du cours. Ainsi, il peut être intéressant de publier le cours en
premier si son contenu est destiné à être diffusé au fil du temps, par exemple
dans le cas de cours à horaire hebdomadaire.

Pour que l’ensemble du cours soit disponible en une seule fois, chaque élément
du contenu du cours doit d’abord être publié, puis le cours peut être publié.

Pour publier un cours, choisissez un cours dans le tableau de bord
_eLearning_. Sur la page du modèle du cours, cliquez sur le bouton intelligent
Aller au site web

Le frontend de la page web du cours s’affiche alors. En haut de la page web du
cours, faites basculer le commutateur de Non publié sur Publié.

#### Publier le contenu d’un cours d’eLearning depuis le backend

Pour publier le contenu d’un cours d” _eLearning_ depuis le backend,
choisissez un cours dans le tableau de bord d”*eLearning. Sur la page du
modèle de cours, cliquez sur le bouton intelligent Contenus publiés.

Cette opération fait apparaître une page séparée affichant tout le contenu
publié lié à ce cours. Supprimez le filtre Publié par défaut de la barre der
cherche dans le coin supérieur droit, pour afficher tout le contenu lié au
cours - même le cours non publié.

Cliquez sur l’icône ≣ (vue Liste) dans le coin supérieur droit, directement
sous la barre de recherche pour passer à la vue de liste.

Dans la vue Liste, une case à cocher se trouve à l’extrême gauche de l’écran,
au-dessus des cours répertoriés, à gauche de la colonne Titre. Lorsque vous
cliquez sur cette case, tout le contenu du cours est sélectionné en même
temps.

Lorsque tout le contenu du cours est sélectionné, doublez-cliquez sur l’une
des cases de la colonne Est publié. Une fenêtre contextuelle s’affiche et vous
demande de confirmer que tous les enregistrements sélectionnés sont destinés à
être publiés. Cliquez sur OK pour automatiquement publier tout le contenu du
cours.

![Vue du contenu d'un cours en cours de publication dans le backend d'Odoo
Assistance.](../../../../_images/help-center-elearning-publish-back-end.png)

