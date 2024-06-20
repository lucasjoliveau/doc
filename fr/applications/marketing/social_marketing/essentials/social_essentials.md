# Les essentiels du marketing social

L’application Odoo _Marketing social_ aide les spécialistes du marketing à
créer et planifier des posts, gérer plusieurs comptes de réseaux sociaux, à
analyser l’efficacité du contenu et à communiquer directement avec les adeptes
des réseaux sociaux en un seul endroit centralisé.

## Comptes de réseaux sociaux

Afin de créer des posts sociaux et d’analyser le contenu avec l’application
Odoo _Marketing social_ , vous **devez** ajouter les comptes de réseaux
sociaux en tant que _flux_ sur le tableau de bord principal de l’application.

Note

Sachez que les profils personnels **ne peuvent pas** être ajoutés en tant que
flux. L’utilisation principale d’Odoo _Marketing social_ est de gérer et
d’analyser les comptes professionnels sur les plateformes de réseaux sociaux.

Avertissement

Odoo _Marketing social_ a quelques limitations en ce qui concerne les comptes
de réseaux sociaux. Par exemple, Odoo **ne peut pas** gérer une grande
quantité de pages différentes (par ex. ~40 pages) sous la même société. Les
mêmes limitations sont présentes dans un environnement multi-sociétés en
raison de la façon dont l’API est construite.

Avertissement

Dans les environnements multi-sociétés, si chaque société n’active pas une
page en même temps, il en résultera une erreur d’autorisation.

Par exemple, si Société 1 est la seule société sélectionnée sur le tableau de
bord principal d’Odoo et active _Facebook Page 1_ et _Facebook Page 2_ , ces
pages seront accessibles sur le tableau de bord _Marketing social_.

Toutefois, si dans cette même base de données, l’utilisateur ajoute Société 2
dans le menu déroulant de l’en-tête et tente d’ajouter ces mêmes flux, une
erreur d’autorisation apparaît.

![Affichage de l'erreur d'autorisation qui apparaît lors d'une tentative
incorrecte d'ajouter un flux.](../../../../_images/permission-error.png)

### Flux de réseaux sociaux

Pour ajouter un compte d’entreprise des réseaux sociaux en tant que flux,
allez à l’application Marketing social et cliquez sur le bouton Ajouter un
flux dans le coin supérieur gauche. Cette opération fait apparaître une
fenêtre contextuelle Ajouter un flux.

![Affichage de la fenêtre contextuelle qui s'ouvre lorsque vous cliquez sur
Ajouter un flux dans Odoo.](../../../../_images/add-stream-social-popup.png)

Dans la fenêtre contextuelle Ajouter un flux, choisissez le Lier un nouveau
compte pour une entreprise à partir de n’importe quelle plateforme populaire :
Facebook, Instagram, LinkedIn, Twitter, et YouTube.

Après avoir cliqué sur la plateforme de réseaux sociaux souhaitée dans la
fenêtre contextuelle Ajouter un flux, Odoo redirige immédiatement vers la page
d’autorisation de ce réseau social, où la permission doit être accordée pour
qu’Odoo puisse ajouter ce compte de réseau social particulier en tant que flux
dans l’application _Marketing social_.

![Exemple d'un tableau de bord de marketing social rempli avec des flux de
réseaux sociaux et du contenu.](../../../../_images/social-marketing-
dashboard.png)

Une fois l’autorisation accordée, Odoo revient au Feed du tableau de bord
principal Marketing social et une nouvelle colonne avec les posts de ce compte
est ajoutée. Des comptes/flux peuvent être ajoutés à tout moment.

Important

Une page Facebook peut être ajoutée tant que le compte Facebook qui accorde
l’autorisation est l’administrateur de la page. Il convient également de noter
que plusieurs pages peuvent être ajoutées pour des flux différents.

Note

Les comptes Instagram sont ajoutés via une connexion Facebook parce qu’ils
utilisent la même API. En d’autres termes, un compte Instagram doit être lié à
un compte Facebook pour qu’il apparaisse en tant que flux dans Odoo.

### Posts

En cliquant sur un post dans un flux de réseaux sociaux, une fenêtre
contextuelle présentant le contenu de ce post spécifique, ainsi que toutes les
données d’engagement qui y sont liées (par ex. les likes, les commentaires,
etc.).

![Exemple d'une fenêtre contextuelle d'un post de réseau social dans
l'application Odoo Marketing social.](../../../../_images/social-post-
popup.png)

Si l’utilisateur le souhaite, il peut laisser un nouveau commentaire sur le
post à partir de la fenêtre contextuelle du post, en saisissant un commentaire
dans le champ Écrire un commentaire… et en cliquant sur Enter pour publier ce
commentaire.

### Créer des pistes à partir des commentaires

Odoo _Marketing social_ vous permet également de créer des pistes directement
à partir des commentaires des réseaux sociaux.

Pour créer une piste à partir d’un commentaire laissé sur un post de réseau
social, cliquez sur le post souhaité à partir du tableau de bord afin de faire
apparaître la fenêtre contextuelle de ce post spécifique. Ensuite, faites
défiler jusqu’au commentaire souhaité et cliquez sur l’icône des trois points
verticaux à droite de ce commentaire.

Cette opération fait apparaître un menu déroulant avec l’option : Créer une
piste.

![Le menu déroulant à côté d'un commentaire révèle l'option de créer une
piste.](../../../../_images/create-lead-drop-down.png)

Lorsque vous cliquez sur Créer une piste dans le menu déroulant du
commentaire, une fenêtre contextuelle Convertir le poste en piste s’affiche.

![La fenêtre contextuelle permettant de convertir un piste en piste qui
s'affiche dans Odoo Marketing social.](../../../../_images/convert-post-to-
lead-popup.png)

Dans cette fenêtre contextuelle, sélectionnez Créer un nouveau client, Lier à
un client existant, ou Ne pas lier à un client.

Note

Si vous sélectionnez Lier à un client existant, un nouveau champ Client
s’affiche en dessous de ces options, dans lequel vous pouvez choisir un client
à lier à cette piste.

Une fois que vous avez fait la sélection souhaitée, cliquez sur le bouton
Convertir au bas de la fenêtre contextuelle Convertir le poste en piste. Cette
opération fait apparaître un formulaire détaillé vierge de la piste, où vous
pouvez saisir et traiter les informations nécessaires.

![Un nouveau formulaire détaillé de la piste généré à partir d'un commentaire
de réseaux sociaux dans Odoo Marketing social.](../../../../_images/new-lead-
detail-form-comments.png)

### Statistiques

Lorsqu’un flux de comptes de réseaux sociaux est ajouté au tableau de bord
_Marketing Social_ , chaque flux affiche et relie également les KPIs de la
plateforme de réseaux sociaux spécifique (si la plateforme en dispose).

Pour être redirigé vers les statistiques et les métriques liées aux KPIs d’un
compte de réseau social, cliquez sur le lien Statistiques situé en haut de
chaque flux.

![Présentation du lien vers les statistiques sur le tableau de bord de
l'application Marketing social.](../../../../_images/social-marketing-
insights-link.png)

Note

Dans un environnement multi-sociétés, si vous n’avez pas sélectionné _toutes_
les pages, la désauthentification se produit.

Par exemple, s i les sociétés ont 3 pages _Facebook_ , mais n’accordent
l’accès qu’à 1 seule et essaient d’accorder l’accès à une autre
ultérieurement, elles seront désauthentifiées et l’accès aux statistiques,
analyses de la page initiale sera perdu.

Veillez donc à ajouter _toutes_ les pages pour _toutes_ les sociétés dans un
environnement multi-sociétés pour éviter ce problème. Si une page est
désauthentifiée, il suffit de supprimer le flux et de le rétablir.

## Créer et publier du contenu pour les réseaux sociaux

Odoo _Marketing social_ offre la possibilité de créer et de publier le contenu
pour les comptes de réseaux sociaux directement à travers l’application.

Pour créer du contenu pour les comptes de réseaux sociaux, allez à
l’application Marketing social, et cliquez sur Nouveau post situé dans le coin
supérieur droit du tableau de bord du _Marketing social_.

![Bouton Nouveau post sur le tableau de bord principal de l'application Odoo
Marketing Social.](../../../../_images/new-post-button-social-marketing-
dashboard.png)

Ou, allez à l’application Marketing social ‣ Posts et cliquez sur le bouton
Nouveau.

![Bouton nouveau sur le page des Posts sociaux dans l'application Odoo
Marketing social.](../../../../_images/new-button-social-posts-page.png)

L’une ou l’autre des options permet d’afficher un formulaire de post vierge
qui peut être personnalisé et configuré de différentes manières.

![Page de post vierge dans Odoo Marketing social.](../../../../_images/blank-
post-detail-page.png)

### Formulaire de post

Le formulaire des posts sur les réseaux sociaux dans Odoo _Marketing social_
dispose de nombreuses options de configuration.

#### Société

Si vous travaillez dans un environnement multi-sociétés, le premier champ dans
la section Votre post du formulaire de post est Société. Sélectionnez dans le
champ la société qui doit être liée à ce post spécifique sur les réseaux
sociaux.

#### Publier sur

Si vous travaillez dans un environnement à une seule société, le premier champ
de la section Votre post du formulaire de post Publier sur. Dans ce champ,
déterminez sur quels réseaux sociaux (flux) ce post doit être publié et/ou aux
visiteurs de quel site web ce post doit être envoyé, par le biais d’une
notification push, en cochant la case à côté des options souhaitées.

Odoo propose automatiquement tous les comptes de réseaux sociaux disponibles
qui ont été liés à la base de données. Si le compte d’un réseau social n’a pas
été ajouté en tant que flux à l’application _Marketing social_ , il
n’apparaîtra **pas** en tant qu’option sur le modèle du post.

Vous pouvez sélectionner plusieurs réseaux sociaux (flux) et sites web dans le
champ Publier sur. Vous _devez_ sélectionner au moins **une** option dans le
champ Publier sur.

Important

Pour que l’option Notification push apparaisse sur le formulaire du post sur
les réseaux sociaux dans Odoo _Marketing social_ , veillez à activer la
fonctionnalité _Activer les notifications push_ dans l’application _Site Web_.

Pour ce faire, allez à l’application Site Web ‣ Configuration ‣ Paramètres,
activez Activer les notifications push, complétez les champs correspondants et
cliquez sur Enregistrer.

#### Message

Ensuite, vous avez le champ Message où vous pouvez créer le contenu principal
du post.

Dans le champ Message, écrivez le message souhaité pour le post social. Après
l’avoir rédigé, cliquez en dehors du champ Message pour prévisualiser le post
qui sera publié sur tous les comptes des réseaux sociaux sélectionnés
précédemment (et/ou sites web, comme notifications push).

![Prévisualisation d'un post sur les réseaux sociaux
](../../../../_images/visual-samples-social-media-outlets-preview.png)

Astuce

Vous pouvez également ajouter des émojis directement au texte dans le champ
Message. Cliquez simplement sur l’icône 🙂 (smiley), situé sur la ligne du
champ Message à l’extrême droite. En cliquant sur cette icône, un menu
déroulant contenant de nombreux émojis s’affiche.

Note

Si vous choisissez Twitter dans le champ Publier sur, un compteur de
caractères apparaît sous le champ Message.

#### Joindre des images

Si vous voulez utiliser des images dans le post, cliquez sur le bouton Joindre
des images dans le champ Joindre des images situé sous le champ Message. Odoo
ouvre alors une fenêtre contextuelle, dans laquelle vous pouvez sélectionnez
l’image souhaitée sur le disque dur et la charger.

Après avoir chargé et joint l’image souhaitée, Odoo affiche une nouvelle
prévisualisation du post sur les réseaux sociaux, avec l’image nouvellement
ajoutée, sur le côté droit du formulaire.

![Exemples visualisés de posts avec des images nouvellement ajoutées dans Odoo
Marketing social.](../../../../_images/attach-images-visual-social-post-
sample.png)

#### Campagne

Vous avez ensuite le champ Campagne. Ce champ non obligatoire permet de
rattacher ce post à une campagne marketing spécifique.

Pour ajouter ce post à une campagne préexistant, cliquez sur le champ Campagne
vide pour faire apparaître un menu déroulant contenant toutes les campagnes
existantes dans la base de données. Sélectionnez le campagne souhaitée dans ce
menu déroulant pour ajouter ce post à cette campagne.

Pour créer une nouvelle campagne directement à partir du formulaire du post,
commencez par taper le nom de la nouvelle campagne dans le champ vierge
Campagne et sélectionnez Créer ou Créer et modifier….

![Le menu déroulant propose les options Créer ou Créer et modifier dans le
champ Campagne.](../../../../_images/campaign-drop-down-menu-options.png)

Cliquer sur Créer crée la campagne, qui peut être modifiée/personnalisée
ultérieurement.

Cliquer sur Créer et modifier… permet de créer la campagne et d’afficher une
fenêtre contextuelle Créer la campagne dans laquelle vous pouvez immédiatement
configurer l”Identifiant de la campagne, le Responsable, et les Étiquettes.

![La fenêtre contextuelle permettant de créer une campagne qui apparaît sur un
formulaire de post.](../../../../_images/create-campaign-popup.png)

Lorsque tous les paramètres souhaités ont été saisis, cliquez sur Enregistrer
& Fermer pour enregistrer la campagne et revenir au formulaire du post.

#### Quand

Ensuite, dans le champ Quand, choisissez Envoyer maintenant pour qu’Odoo
publie le post immédiatement ou Planifier ultérieurement pour qu’Odoo publie
le post à une date et une heure ultérieures.

Si vous sélectionnez Planifier ultérieurement, un nouveau champ Date planifiée
apparaît. Le fait de cliquer sur le champ vide fait apparaître un calendrier
contextuel, dans lequel vous pouvez sélectionner une date et une heure future.

![Fenêtre contextuelle permettant de planifier une date qui s'affiche sur le
formulaire du post dans Odoo.](../../../../_images/schedule-post-calendar-
popup.png)

Après avoir sélectionné la date et l’heure souhaitée, cliquez sur Appliquer.
Odoo publiera ensuite le post à cette date et heure spécifiques sur le ou les
comptes prédéfinis sur les réseaux sociaux.

Note

Lors de la planification d’un post, le bouton Publier en haut du formulaire du
post devient Planifier. N’oubliez pas de cliquer sur Planifier après avoir
complété le formulaire du post.

Cela permet de bloquer la date et l’heure auxquelles Odoo doit envoyer le post
et de changer le statut du post en Planifié.

#### Options de notification push

Si vous choisissez une (ou plusieurs) options [Notification push] dans le
champ Publier sur, une section spécifique relative aux Options de
notifications push apparaît au bas du formulaire du post.

![Section avec les options de notification push sur un formulaire du
post.](../../../../_images/push-notification-options-section.png)

Il convient de noter qu” _aucun_ de ces champs n’est obligatoire.

Le premier champ de la section est Titre de la notification. Dans ce champ,
vous trouverez l’option d’ajouter un titre personnalisé à la notification push
qui sera envoyée.

Pour désigner une page spécifique du site web qui doit déclencher cette
notification push, saisissez l’URL de cette page dans le champ URL cible.
Ensuite, lorsqu’un visiteur atteint cette page spécifique, Odoo affiche la
notification push.

Sous ce champ, vous avez l’option d’ajouter une Image d’icône personnalisée à
la notification push. Cette icône s’affiche à côté de la notification push.

Pour charger une nouvelle image, cliquez sur l’icône de crayon ✏️ lorsque vous
survolez l’icône de caméra de l”Image d’icône. Cette opération fait apparaître
une fenêtre contextuelle dans laquelle l’image d’icône souhaitée peut être
chargée depuis le disque sur.

Une fois que c’est fait, Odoo met automatiquement à jour l’aperçu visuel de la
façon dont l’icône apparaît sur la notification push.

Note

Ensuite, si le post est planifié pour être publié plus tard, vous avez la
possibilité de s’assurer que le post est envoyé dans le fuseau horaire du
visiteur, en activant l’option Heure locale. Si cette option est activée, Odoo
enverra le post à l’heure appropriée, prédéterminée, en tenant compte de
l’emplacement du visiteur.

![L'option de l'heure locale dans la section des options de notification
push.](../../../../_images/push-notification-local-time.png)

Ensuite, vous avez le champ FAire correspondre tous les enregistrements. Ce
champ permet de cibler un groupe spécifique de destinataires dans la base de
données, en fonction de certains critères et peut être appliqué pour
correspondre à toutes les règles ou à l”une des règles.

Pour utiliser ce champ, cliquez sur le bouton \+ Ajouter une condition qui
fait apparaître un champ de règle de type équation.

Dans le champ de règle de type équation, précisez les critères spécifiques
qu’Odoo doit prendre en compte lors de l’envoi de ce post à une audience cible
particulier.

![Les conditions de notification push sont configurées pour correspondre à un
nombre spécifique d'enregistrements dans la base de
données.](../../../../_images/push-notification-condition.png)

Pour ajouter une règle supplémentaire, cliquez sur le signe plus ➕ à l’extrême
droit de la règle.

Pour ajouter une branche (séries de règles supplémentaires sur la base de la
règle précédente, pour cibler davantage l’audience), cliquez sur l”icône de
branche unique, située à droite du signe plus ➕.

Enfin, cliquez sur l’icône de la corbeille 🗑️ pour supprimer n’importe quelle
règle.

La taille de l’audience cible de destinataires spécifique est représentée par
le nombre d”enregistrements affichés sous les règles.

## Page des posts

Pour avoir une vue d’ensemble de tous les posts, allez à l’application
Marketing social ‣ Posts. Sur la page des Posts sociaux, vous pouvez consulter
et accéder à chaque post qui a été créé et publié avec Odoo.

Il y a quatre options d’affichage différentes pour les données de la page des
Posts sociaux : _kanban_ , _calendrier_ , _liste_ et _tableau croisé
dynamique_.

Les options d’affichage se trouvent dans le coin supérieur droit de la page
des Posts, sous la barre de recherche.

Kanban viewCalendar viewList viewPivot view

Par défaut, Odoo affiche les posts dans une vue kanban. Les informations sur
cette page peuvent encore être triées davantage en utilisant la barre latérale
de gauche, où vous pouvez consulter et analyser tous les comptes et posts
connectés.

La vue kanban est représentée par une icône de graphique à barres renversée
dans le coin supérieur droit.

![La vue kanban de la page des posts dans l'application Odoo Marketing
social.](../../../../_images/posts-page-kanban.png)

L’option d’affichage de calendrier affiche une représentation visuelle des
posts sous forme de calendrier de la date à laquelle les posts ont été publiés
ou sont planifiés. Cette option fournit une vue d’ensemble claire d’une
journée, d’une semaine ou d’un mois planifié et Odoo affiche tous les posts en
brouillon, planifiés et publiés.

En cliquant sur une date, un formulaire de post vierge s’ouvre, dans lequel
vous pouvez créer une post qu’Odoo publiera à cette date/heure spécifique.

La vue calendrier est représentée par une icône de calendrier dans le coin
supérieur droit.

![Exemple de la vue calendrier dans Odoo Marketing
social.](../../../../_images/calendar-view.png)

L’option d’affichage en liste est similaire à l’option kanban, mais au lieu de
blocs individuels, toutes les informations relatives au post sont affichées
dans une liste claire. Chaque ligne de la liste affiche les Comptes sociaux,
le Message, et le Statut de chaque post.

Une barre latérale utile à gauche organise tous les posts par Statut et
répertorie tous les Comptes sociaux connectés.

La vue liste est représentée par quatre lignes verticales dans le coin
supérieur droit.

![Vue de l'option de liste sur la page des posts dans Odoo Marketing
social.](../../../../_images/list-view2.png)

L’option d’affichage tableau croisé dynamique fournit un tableau de grille
entièrement personnalisable, où différentes mesures de données peuvent être
ajoutées et analysées.

![L'option d'affichage de tableau croisé dynamique sur la page des posts dans
Odoo Marketing social.](../../../../_images/pivot-view.png)

L’option d’affichage du tableau croisé dynamique offre de nombreuses options
analytiques, permettant une analyse approfondie et détaillée des différents
posts et métriques.

Cliquez sur n’importe quel signe plus ➕ à côté d’une ligne dans le tableau
croisé dynamique pour afficher d’autres options de mesure à ajouter à la
grille.

Dans le tableau croisé dynamique, vous avez l’option d”Insérer dans une
feuille de calcul, située à droite du menu déroulant Mesures, dans le coin
supérieur gauche de la page Posts sociaux.

À côté de l’option Insérer dans une feuille de calcul se trouvent trois
options, spécifiques au tableau croisé dynamique.

De gauche à droite, les options sont les suivantes :

  * Inverser les axes, qui permet d’intervertir les axes _X_ et _Y_ dans la grille.

  * Tout déplier, qui développe chaque ligne de la grille, affichant ainsi des informations plus détaillées à son sujet.

  * Télécharger, qui vous permet de télécharger instantanément le tableau croisé dynamique sous forme de feuille de calcul.

## Visiteurs

Pour avoir une vue d’ensemble de toutes les personnes qui ont visiter le(s)
site(s) web connecté(s) à la base de données, allez à l’application Marketing
social ‣ Visiteurs.

![Vue de la page des visiteurs dans l'application Odoo Marketing
social.](../../../../_images/visitors.png)

Ici, Odoo fournit une présentation détaillée de toutes les informations
pertinentes des visiteurs dans une vue kanban par défaut. Si les coordonnées
des visiteurs figurent déjà dans la base de données, vous avez la possibilité
de leur envoyer un Email et.ou un SMS.

Il est également possible d’afficher les mêmes données des visiteurs sous
forme de liste ou de graphique. Ces options d’affichage se trouvent dans le
coin supérieur droit de la page des Visiteurs.

## Page des réseaux sociaux

Une autre façon de relier rapidement les comptes de réseaux sociaux à Odoo
_Marketing social_ peut se faire sur la page des Réseaux sociaux. Pour accéder
à la page des Réseaux sociaux, allez à l’application Marketing social ‣
Configuration ‣ Réseaux sociaux.

Sur la page des Réseaux sociaux, vous trouverez une collection de toutes les
options de réseaux sociaux, chacune avec un bouton Lier un compte : Facebook,
Instagram, LinkedIn, Twitter, YouTube, et Notifications push.

![Vue de la page des réseaux sociaux dans l'application Odoo Marketing
social.](../../../../_images/social-media-page.png)

## Page des comptes sociaux

Pour voir une liste de tous les comptes sociaux et sites web liés à la base de
données, allez à l’application Marketing social ‣ Configuration ‣ Comptes
sociaux. Cette page Comptes sociaux affiche le Nom, le Pseudonyme/Nom court,
la plateforme de Réseaux sociaux, la personne qui l’a Créé, et la Société à
laquelle il est associé.

![Vue de la page des comptes sociaux dans l'application Odoo Marketing
social.](../../../../_images/social-accounts-page.png)

Pour modifier les comptes sociaux sur cette page, sélectionnez simplement le
compte souhaité dans la liste sur cette page et effectuez les modifications
nécessaires.

## Page des flux sociaux

Pour afficher une page séparée avec tous les flux de réseaux sociaux qui ont
été ajoutés au tableau de bord principal du _Marketing social_ , allez à
l’application Marketing social ‣ Configuration ‣ Flux sociaux.

![Vue de la page des comptes sociaux dans l'application Odoo Marketing
social.](../../../../_images/social-streams-page.png)

Ici, les informations du flux social sont organisées sous forme de liste avec
les Réseaux sociaux, le Titre du flux, le Type de flux (par ex. Posts, Mot
clé, etc.), la personne qui l’a Créé, et la Société à laquelle il est associé.

Pour modifier les informations d’un flux, cliquez simplement sur le flux
souhaité dans la liste et effectuez les modifications nécessaires.

Pour plus d'infos

[Campagnes de marketing social](social_campaigns.html)

